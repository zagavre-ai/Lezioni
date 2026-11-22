# Sottotitoli .vtt dal montaggio: parole dell'originale (trascrizione con i tempi) portate nei tempi del video finale; correzioni dei termini dal materiale del docente
import json,re,sys
sys.path.insert(0,'/home/claude/w19/lib')
from core import SEG,rel
W='/home/claude/w19'
COR=json.load(open(W+'/correzioni.json')) if __import__('os').path.exists(W+'/correzioni.json') else []
def words():
    out=[]
    for s in SEG:
        cur=None
        for t,w in s['parole']:
            if cur is None or w.startswith(' '):
                if cur: out.append(cur)
                cur=[t,w.strip()]
            else: cur[1]+=w
        if cur: out.append(cur)
    for i in range(len(out)-1):
        if out[i][1]=='prima.' and out[i+1][1].lower().startswith('republika'): out[i][1]='prima'
    return out
def fix(t):
    for a,b in COR: t=re.sub(a,b,t)
    return t
def ts(x):
    h=int(x//3600);m=int(x%3600//60);s=x%60
    return '%02d:%02d:%06.3f'%(h,m,s)
def onset_fn(video):
    import subprocess,numpy as np
    SR=16000
    x=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',video,'-vn','-ac','1','-ar',str(SR),'-f','f32le','-'],capture_output=True).stdout,np.float32)
    e=np.convolve(x**2,np.ones(400)/400,'same');thr=np.percentile(e,60)
    def onset(t):
        i0=int(max(0,t-0.8)*SR);seg=e[i0:int((t+0.8)*SR)]
        if len(seg) and seg[:int(0.5*SR)].mean()<thr*0.5:
            on=i0/SR+np.argmax(seg>thr)/SR
            return on
        return t
    def fix(t):
        c=t
        for _ in range(5):
            n=onset(c)
            if abs(n-c)<0.02: break
            c=n
        return min(max(c,t-0.5),t+0.8)
    return fix
def vtt(tl,pdir,out,video=None):
    WD=words();cues=[];onset=onset_fn(video) if video else (lambda t:t)
    for it in tl:
        if it['tipo'] not in ('prof','intro'): continue
        R=[tuple(x) for x in json.load(open(f'{pdir}/{it["id"]}.json'))['R']]
        ws=[]
        for t,w in WD:
            for x,y in R:
                if x<=t<y: ws.append((it['inizio']+rel(R,t),w));break
        cur=[]
        def flush():
            nonlocal cur
            if not cur: return
            txt=fix(' '.join(w for _,w in cur))
            cues.append([onset(cur[0][0]),cur[-1][0]+0.5,txt]);cur=[]
        for t,w in ws:
            if cur:
                txt=' '.join(x for _,x in cur)+' '+w
                if t-cur[-1][0]>0.9 or len(txt)>80 or t-cur[0][0]>6 or (cur[-1][1][-1:] in '.?!' and len(txt)>28): flush()
            cur.append((t,w))
        flush()
    cues.sort()
    for i in range(len(cues)-1):
        if cues[i][1]>cues[i+1][0]-0.03: cues[i][1]=cues[i+1][0]-0.03
    with open(out,'w') as f:
        f.write('WEBVTT\n\n')
        for i,(a,b,t) in enumerate(cues):
            if len(t)>42:
                m=len(t)//2;k=t.rfind(' ',0,m+8)
                k2=t.find(' ',m)
                if k<0 or (k2>0 and abs(k2-m)<abs(k-m)): k=k2
                t=t[:k]+'\n'+t[k+1:]
            e=max(b,a+0.4)
            if i+1<len(cues): e=min(e,cues[i+1][0]-0.02)
            f.write(f'{i+1}\n{ts(a)} --> {ts(max(e,a+0.05))}\n{t}\n\n')
    return len(cues)
