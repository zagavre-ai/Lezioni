import json,os,sys,subprocess,shutil
from PIL import Image
sys.path.insert(0,'.')
FPS=30;FD=6;LEAD=12
J=json.load(open('states.json'));ST=J['STATES'];NEWF=J['NEWF'];PROF=J['PROF']
import plan
order=[n for n,a,b in plan.blocks]
# durate nuove complete (mappe incluse) da gen
import importlib
os.makedirs('bl',exist_ok=True);os.makedirs('seg',exist_ok=True);os.makedirs('cc',exist_ok=True);os.makedirs('prof',exist_ok=True)
SRC='/home/user/w/Letteratura_Lez12.mp4'
def png(h): return f'png/{h}.png'
def blend(a,b,k,n,name):
    out=f'bl/{name}_{k}.png'
    if not os.path.exists(out):
        A=Image.open(a).convert('RGB');B=Image.open(b).convert('RGB')
        Image.blend(A,B,(k+1)/(n+1)).save(out,compress_level=1)
    return out
def seqlist(blk,prev_last):
    N=NEWF[blk];states=sorted(ST.get(blk,[]),key=lambda x:x[0]);lines=[]  # (png,frames)
    if not states: raise SystemExit('nessuno stato '+blk)
    seq=[]  # per fotogramma: percorso png
    first=png(states[0][1])
    for f in range(N):
        # stato corrente
        i=max(j for j,(ff,h) in enumerate(states) if ff<=f) if f>=states[0][0] else 0
        cur=png(states[i][1]);fs=states[i][0] if f>=states[0][0] else 0
        k=f-fs
        if i>0 and k<FD:
            seq.append(blend(png(states[i-1][1]),cur,k,FD,f'{blk}_{i}'))
        elif i==0 and prev_last and f<LEAD:
            seq.append(blend(prev_last,cur,f,LEAD,f'{blk}_in'))
        else: seq.append(cur)
    return seq
def write_concat(blk,seq):
    p=f'cc/{blk}.txt';out=[];i=0
    while i<len(seq):
        j=i
        while j+1<len(seq) and seq[j+1]==seq[i]: j+=1
        out.append(f"file '{os.path.abspath(seq[i])}'\nduration {(j-i+1)/FPS:.6f}\n");i=j+1
    out.append(f"file '{os.path.abspath(seq[-1])}'\n")
    open(p,'w').write(''.join(out));return p
X264=['-c:v','libx264','-preset','veryfast','-crf','19','-pix_fmt','yuv420p','-r','30','-g','60','-bf','2','-an']
def encode(blk,prev_last):
    out=f'seg/{blk}.mp4'
    if os.path.exists(out+'.ok'): return seq_last(blk)
    N=NEWF[blk]
    if blk=='SIGLA':
        # 450 fotogrammi della sigla del kit + dissolvenza alla copertina
        last='bl/sigla_last.png'
        subprocess.run(['ffmpeg','-v','error','-y','-sseof','-0.1','-i','/home/user/Lezioni/kit/sigle/Sigla_Letteratura_15s.mp4','-frames:v','1',last],check=True)
        cov=png(ST['INTRO1'][0][1]);seq=[]
        for f in range(450,N):
            k=f-450;seq.append(blend(last,cov,k,30,'sig') if k<30 else cov)
        p=write_concat('SIGLA_b',seq)
        subprocess.run(['ffmpeg','-v','error','-y','-i','/home/user/Lezioni/kit/sigle/Sigla_Letteratura_15s.mp4','-f','concat','-safe','0','-i',p,'-filter_complex','[0:v]fps=30,scale=1920:1080,setsar=1[a];[1:v]fps=30,setsar=1[b];[a][b]concat=n=2:v=1:a=0[v]','-map','[v]','-frames:v',str(N)]+X264+[out],check=True)
    elif blk=='SFIN':
        k=NEWF[blk];kit='/home/user/Lezioni/kit/sigle/Sigla_finale_5s_con_avviso_diritti.mp4'
        subprocess.run(['ffmpeg','-v','error','-y','-i',kit,'-vf',f'fps=30,scale=1920:1080,tpad=stop_mode=clone:stop_duration=3,setsar=1','-frames:v',str(N)]+X264+[out],check=True)
    else:
        seq=seqlist(blk,prev_last);p=write_concat(blk,seq)
        if blk in PROF:
            a,b=PROF[blk];core=round((b-a)*FPS);pc=f'prof/{blk}.mp4'
            vf=f"crop=184:138:846:339,scale=410:308:flags=lanczos,eq=contrast=1.04:saturation=1.03,hqdn3d=1.5:1.5:3:3,cas=0.35"
            subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{a:.3f}','-i',SRC,'-frames:v',str(core),'-vf',vf+',fps=30','-c:v','libx264','-preset','veryfast','-crf','12','-pix_fmt','yuv420p','-an',pc],check=True)
            fo=(core-10)/FPS
            fc=f"[1:v]format=yuva420p[p];[2:v]format=gray[m];[p][m]alphamerge,fade=t=in:st=0:n=10:alpha=1,fade=t=out:st={fo:.4f}:n=10:alpha=1[pf];[0:v][pf]overlay=1428:148:eof_action=pass:format=auto[v]"
            subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',p,'-i',pc,'-loop','1','-i','mask.png','-filter_complex',fc,'-map','[v]','-frames:v',str(N)]+X264+[out],check=True)
        else:
            subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',p,'-vf','fps=30,setsar=1','-frames:v',str(N)]+X264+[out],check=True)
    open(out+'.ok','w').write('1');return seq_last(blk)
def seq_last(blk):
    st=sorted(ST.get(blk,[]),key=lambda x:x[0])
    return png(st[-1][1]) if st else None
if __name__=='__main__':
    only=sys.argv[1:]
    prev=None
    for blk in order:
        if only and blk not in only: prev=seq_last(blk) or prev;continue
        encode(blk,prev);prev=seq_last(blk) or prev;print('ok',blk,flush=True)
