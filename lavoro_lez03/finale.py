import sys,json,os,subprocess,re,time;sys.path.insert(0,'/home/user/Lezioni/lavoro_lez03')
from parti import *
OUTD='/tmp/w/final';os.makedirs(OUTD,exist_ok=True)
def adj(p):
    g=9.6 if 'src' in p else 1.5
    f=p['a'][:-4]+f'_g{g}.wav'
    if not os.path.exists(f):
        af=f'volume={g}dB'+(',alimiter=limit=0.89:attack=3:release=60:level=false' if 'src' in p else '')
        M.sh(['ffmpeg','-v','error','-y','-i',p['a'],'-af',af,'-c:a','pcm_s16le','-ar','48000','-ac','2',f])
    return f
def finale(seq,nome):
    allp,tl=assemble(seq,nome,None)
    for p in allp:p['a_orig']=p['a'];p['a']=adj(p)
    v=f'{OUTD}/{nome}_video.mp4';a=f'{OUTD}/{nome}_audio.wav'
    M.concat_all(allp,v,a)
    # loudnorm a due passate (lineare)
    m=subprocess.run(['ffmpeg','-nostats','-i',a,'-af','loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json','-f','null','-'],capture_output=True,text=True).stderr
    j=json.loads(m[m.rfind('{'):m.rfind('}')+1])
    af=f"loudnorm=I=-16:TP=-1.5:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}:measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true"
    out=f'{OUTD}/{nome}_1080p.mp4'
    M.sh(['ffmpeg','-v','error','-y','-i',v,'-i',a,'-map','0:v','-map','1:a','-c:v','copy','-af',af,'-c:a','aac','-b:a','192k','-ar','48000','-movflags','+faststart',out])
    json.dump(tl,open(f'{OUTD}/timeline_{nome}.json','w'))
    # informazioni sui pezzi del prof (per sincronia e sottotitoli)
    st={n:t for n,t,d in tl};info={}
    for n,p in seq:
        if 'subs' in p:info[n]={'t':st[n],'subs':p['subs']}
    json.dump(info,open(f'{OUTD}/docinfo_{nome}.json','w'))
    n=sum(p['n'] for p in allp);print(nome,'pezzi',len(allp),'durata %.1f min'%(n/1800),'prima di loudnorm',j['input_i'],'LUFS')
    return out,tl
if __name__=='__main__':
    which=sys.argv[1]
    seq=parte1() if which=='1' else parte2()
    finale(seq,f'Parte{which}')
