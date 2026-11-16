import sys,os,json,subprocess,re,unicodedata
sys.path.insert(0,'/home/user/Lezioni/storia_s7')
from scene import *
from slides20 import *
from anchors20 import *
from spec20 import TITOLO
sys.path.insert(0,'/home/user/Lezioni/kit/tools')
import taglio
W='/tmp/w20/w';VID='/tmp/w20/v20.mp4';AB='/tmp/w20/aB.wav';A16='/tmp/w20/a20.wav'
END=dur(VID)
Wd=json.load(open('/tmp/w20/W20.json'))
def n(w):
    w=unicodedata.normalize('NFD',w.lower());return re.sub(r'[^a-z0-9]','',''.join(c for c in w if unicodedata.category(c)!='Mn'))
TT=[n(w) for t,w in Wd]
def find(phrase,after=0):
    p=[n(x) for x in phrase.split()]
    for i in range(len(TT)-len(p)):
        if Wd[i][0]>=after and TT[i:i+len(p)]==p:return Wd[i][0]
    raise ValueError('frase non trovata: '+phrase)
CUTS=[0]+[find(p,a)-0.3 for p,a in START]
SN=[0.0]+[taglio.snap(t,A16) for t in CUTS[1:]]+[END]
print('tagli',[round(x,2) for x in SN],flush=True)
json.dump(SN,open('/tmp/w20/cuts.json','w'))
S=Shooter();os.makedirs(W+'/png',exist_ok=True);os.makedirs(W+'/pc',exist_ok=True)
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
        for (p,_),m in zip(states,ff):
            while m>0:
                k=min(m,30);m-=k;f.write(f"file '{p}'\nduration {k/FPS:.6f}\n")
        f.write(f"file '{states[-1][0]}'\n")
    T=N/FPS;bg=out+'.bg.mp4'
    run(['nice','-n','5','ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',lst,'-vf','fps=30,format=yuv420p','-frames:v',str(N),'-c:v','libx264','-preset','ultrafast','-crf','8','-r','30',bg])
    run(['nice','-n','5','ffmpeg','-y','-v','error','-i',bg,'-ss',f'{a:.3f}','-t',f'{d+0.5:.3f}','-i',VID,'-ss',f'{a:.3f}','-t',f'{d+0.5:.3f}','-i',AB,
      '-filter_complex',f"[1:v]crop=246:137:846:343,scale=394:218:flags=lanczos,eq=contrast=1.05:saturation=1.1:gamma=1.04[cam];[0:v][cam]overlay=1490:40:shortest=1[v];[2:a]aresample=48000,apad,atrim=0:{T:.6f}[a]",
      '-map','[v]','-map','[a]','-frames:v',str(N),'-c:v','libx264','-preset','ultrafast','-crf','17','-pix_fmt','yuv420p','-r','30','-c:a','aac','-b:a','192k','-ar','48000','-ac','2',out])
    os.remove(bg);open(out+'.ok','w').write('1');os.remove(lst);print(name,round(d,2),flush=True)
dpiece('D0',SN[0],SN[1],[(png('D0',intro_slide_html(TITOLO,[s[0] for s in SLIDES])),SN[1]-SN[0])])
for k,(t,kick,c) in enumerate(SLIDES,1):
    a,b=SN[k],SN[k+1];cards=[(l,sents(r)) for l,r in c];G=GROUPS[k]
    ev=[]
    for ph,aft,ci,si in ANC[k]:
        ev.append((a if ph is None else find(ph,aft)-0.4,ci,si))
    ev=sorted(ev);ev[0]=(a,)+ev[0][1:]
    # card iniziale: se None, stato 'nessuna'
    states=[];ts=[e[0] for e in ev]+[b]
    for i,(tt,ci,si) in enumerate(ev):
        d=ts[i+1]-ts[i]
        if d<=0.05:continue
        g=[x for x in G if (ci in x)] if ci is not None else [G[0]]
        grp=g[0];pc=[cards[x] for x in grp]
        loc=grp.index(ci) if ci is not None else None
        states.append((png(f'D{k}_{ci}',slide_html(t,kick,pc,(loc,None))),d))
    dpiece(f'D{k}',a,b,states)
S.close();print('FATTO',flush=True)
