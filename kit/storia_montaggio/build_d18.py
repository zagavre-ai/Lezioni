import sys,os,json,subprocess
sys.path.insert(0,'/home/user/Lezioni/storia_s7')
from scene import *
from slides18 import *
from anchors18 import ANC
sys.path.insert(0,'/home/user/Lezioni/kit/tools')
import taglio
W='/tmp/w18/w';VID='/tmp/w18/v18.mp4';AB='/tmp/w18/aB.wav';A16='/tmp/w18/a18.wav'
END=dur(VID)
CUTS=[0,187.1,662.95,1820.8,2186.85,3176.0,3500.7]
SN=[0.0]+[taglio.snap(t,A16) for t in CUTS[1:]]+[END]
print('tagli',SN,flush=True)
json.dump(SN,open('/tmp/w18/cuts.json','w'))
S=Shooter();os.makedirs(W+'/png',exist_ok=True)
def png(key,h):
    p=f'{W}/png/{key}.png'
    if not os.path.exists(p):S.shot(h,p)
    return p
def dpiece(name,a,b,states):
    out=f'{W}/pc/{name}.mp4'
    if os.path.exists(out+'.ok'):return
    d=b-a;N=round(d*FPS)
    ff=[max(1,round(x*FPS)) for _,x in states];ff[-1]=max(1,ff[-1]+N-sum(ff))
    lst=out+'.txt'
    with open(lst,'w') as f:
        for (p,_),n in zip(states,ff):
            while n>0:
                m=min(n,30);n-=m;f.write(f"file '{p}'\nduration {m/FPS:.6f}\n")
        f.write(f"file '{states[-1][0]}'\n")
    T=N/FPS;bg=out+'.bg.mp4'
    run(['nice','-n','5','ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',lst,'-vf','fps=30,format=yuv420p','-frames:v',str(N),'-c:v','libx264','-preset','ultrafast','-crf','8','-r','30',bg])
    run(['nice','-n','5','ffmpeg','-y','-v','error','-i',bg,'-ss',f'{a:.3f}','-t',f'{d+0.5:.3f}','-i',VID,'-ss',f'{a:.3f}','-t',f'{d+0.5:.3f}','-i',AB,
      '-filter_complex',f"[1:v]crop=246:137:846:343,scale=394:218:flags=lanczos,eq=contrast=1.05:saturation=1.1:gamma=1.04[cam];[0:v][cam]overlay=1490:40:shortest=1[v];[2:a]aresample=48000,apad,atrim=0:{T:.6f}[a]",
      '-map','[v]','-map','[a]','-frames:v',str(N),'-c:v','libx264','-preset','ultrafast','-crf','17','-pix_fmt','yuv420p','-r','30','-c:a','aac','-b:a','192k','-ar','48000','-ac','2',out])
    os.remove(bg)
    open(out+'.ok','w').write('1');os.remove(lst);print(name,round(d,2),flush=True)
# D0
dpiece('D0',SN[0],SN[1],[(png('D0',intro_slide_html(TITOLO,[s[0] for s in SLIDES])),SN[1]-SN[0])]) if False else None
from spec18 import TITOLO
dpiece('D0',SN[0],SN[1],[(png('D0',intro_slide_html(TITOLO,[s[0] for s in SLIDES])),SN[1]-SN[0])])
for k,(t,kick,c) in enumerate(SLIDES,1):
    a,b=SN[k],SN[k+1];cards=[(l,sents(r)) for l,r in c]
    anc=ANC[k];states=[];ts=[a]+[x[0] for x in anc[1:]]+[b]
    # il primo ancoraggio parte da 'a'
    st=[(x[1],x[2]) for x in anc]
    for i,(ci,si) in enumerate(st):
        d=ts[i+1]-ts[i]
        if d<=0.05:continue
        states.append((png(f'D{k}_{ci}_{si}',slide_html(t,kick,cards,(ci,si))),d))
    dpiece(f'D{k}',a,b,states)
S.close();print('FATTO',flush=True)
