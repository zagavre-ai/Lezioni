import sys,os,json,glob,subprocess,re
sys.path.insert(0,'/home/user/Lezioni/lez14')
from lib import *
import numpy as np
PZ='/tmp/w/pezzi';FIN='/tmp/w/fin';os.makedirs(FIN,exist_ok=True)
REPO='/home/user/Lezioni'
def sh(c):
    r=subprocess.run(c,capture_output=True,text=True)
    if r.returncode:raise RuntimeError(' '.join(c)[:300]+'\n'+r.stderr[-1200:])
    return r
def ordine(parte):
    def AN(n):return [os.path.basename(x)[:-4] for x in sorted(glob.glob(f'{PZ}/AN{n}_*.mkv'))]
    o=['SIG','CW1' if parte==1 else 'CW2']
    o+=['D0'] if parte==1 else ['RIP2']
    args=[1,2,3] if parte==1 else [4,5,6,7]
    mappa={1:'MAP1',6:'MAP2',7:'MAP3'}
    for n in args:
        o+=[f'T{n}',f'D{n}']+AN(n)+([mappa[n]] if n in mappa else [])+[f'PI{n}',f'PS{n}',f'Q{n}']
    o+=['GL%d'%parte,'FIN%d'%parte]
    o+=['SFIN'] if parte==1 else ['VER','SFIN','CINTRO','COMP']
    return o
def dur(p):return float(sh(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p]).stdout)
def costruisci(parte,out,crf=19,prova=False):
    ped=ordine(parte);mancano=[p for p in ped if not os.path.exists(f'{PZ}/{p}.mkv')]
    if mancano:print('MANCANO',mancano)
    ped=[p for p in ped if p not in mancano]
    D=[dur(f'{PZ}/{p}.mkv') for p in ped];N=len(ped)
    # video: dissolvenza dip-to-white 0,25 s a ogni cambio, un'unica codifica
    fc=[];lab=[]
    for i,p in enumerate(ped):
        f=[]
        if i>0:f.append('fade=t=in:st=0:d=0.25:color=white')
        if i<N-1:f.append(f'fade=t=out:st={D[i]-0.25:.4f}:d=0.25:color=white')
        fc.append(f'[{i}:v]'+(','.join(f) if f else 'null')+f'[v{i}]');lab.append(f'[v{i}]')
    fc.append(''.join(lab)+f'concat=n={N}:v=1:a=0[v]')
    cmd=['ffmpeg','-v','error','-y']
    for p in ped:cmd+=['-i',f'{PZ}/{p}.mkv']
    vid=f'{FIN}/video_P{parte}.mp4'
    cmd+=['-filter_complex',';'.join(fc),'-map','[v]','-r','30','-c:v','libx264','-preset','veryfast','-crf',str(crf),'-pix_fmt','yuv420p',vid]
    sh(cmd)
    # audio: concatenazione + trans.wav a ogni giunzione (inizia 0,5 s prima della giunzione)
    aud=[];off=0;starts=[]
    cmd=['ffmpeg','-v','error','-y']
    for p in ped:cmd+=['-i',f'{PZ}/{p}.mkv']
    cmd+=['-filter_complex',''.join(f'[{i}:a]aresample=48000,aformat=channel_layouts=stereo[a{i}]' + (';' if i<N-1 else '') for i in range(N))+';'+''.join(f'[a{i}]' for i in range(N))+f'concat=n={N}:v=0:a=1[a]','-map','[a]','-f','f32le','-ar','48000','-ac','2',f'{FIN}/a_P{parte}.f32']
    sh(cmd)
    a=np.fromfile(f'{FIN}/a_P{parte}.f32',dtype=np.float32).reshape(-1,2)
    tr=np.frombuffer(sh(['ffmpeg','-v','error','-i',f'{REPO}/kit/suoni/trans.wav','-f','f32le','-ar','48000','-ac','2','-']).stdout.encode('latin1') if False else subprocess.run(['ffmpeg','-v','error','-i',f'{REPO}/kit/suoni/trans.wav','-f','f32le','-ar','48000','-ac','2','-'],capture_output=True).stdout,dtype=np.float32).reshape(-1,2)
    t=0;tl=[]
    for i,p in enumerate(ped):
        tl.append([p,round(t,3),round(D[i],3)]);
        if i>0:
            s=int(round((t-0.5)*48000));s=max(0,s);e=min(len(a),s+len(tr));a[s:e]+=tr[:e-s]*0.8
        t+=D[i]
    a.tofile(f'{FIN}/a2_P{parte}.f32')
    # loudness a due passi (-16 LUFS, picco <= -1,5 dBTP)
    base=['ffmpeg','-v','info','-f','f32le','-ar','48000','-ac','2','-i',f'{FIN}/a2_P{parte}.f32','-af']
    m=subprocess.run(base+['loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json','-f','null','-'],capture_output=True,text=True).stderr
    j=json.loads(m[m.rfind('{'):m.rfind('}')+1])
    af=f"loudnorm=I=-16:TP=-1.5:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}:measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true"
    wav=f'{FIN}/a_P{parte}.wav'
    sh(['ffmpeg','-v','error','-y','-f','f32le','-ar','48000','-ac','2','-i',f'{FIN}/a2_P{parte}.f32','-af',af,'-ar','48000',wav])
    sh(['ffmpeg','-v','error','-y','-i',vid,'-i',wav,'-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','192k','-ar','48000','-movflags','+faststart',out])
    json.dump(tl,open(out.replace('.mp4','_timeline.json'),'w'),ensure_ascii=False)
    print('OK',out,round(t,1),'s',os.path.getsize(out)//1000000,'MB, loudnorm in',j['input_i'])
if __name__=='__main__':
    costruisci(int(sys.argv[1]),sys.argv[2])
