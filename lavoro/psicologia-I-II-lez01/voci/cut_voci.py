# taglia la voce generata nei marcatori «Taglio»: file (5) e frasi (3)
import json,re,sys,subprocess,numpy as np,wave
src_mp3,src_json,names,outdir=sys.argv[1],sys.argv[2],sys.argv[3].split(','),sys.argv[4]
W=[]
for l in open(src_json): W+=json.loads(l)['w']
def isT(w): return re.sub(r'\W','',w.lower())=='taglio'
x=subprocess.run(['ffmpeg','-v','error','-i',src_mp3,'-ac','1','-ar','48000','-f','f32le','-'],capture_output=True).stdout
x=np.frombuffer(x,np.float32).copy(); SR=48000; T=len(x)/SR
env=np.convolve(np.abs(x),np.ones(480)/480,'same')
def quiet(a,b):  # punto più silenzioso tra a e b
    i0,i1=int(a*SR),int(b*SR)
    if i1<=i0: return a
    return (i0+int(np.argmin(env[i0:i1])))/SR
# gruppi
groups=[];cur=[]
for k,(t,w) in enumerate(W):
    if isT(w) and not (k>0 and re.sub(r'\W','',W[k-1][1].lower())=='nel') and not (k+1<len(W) and re.sub(r'\W','',W[k+1][1].lower()).startswith('automatic')): cur.append(k)
    else:
        if cur: groups.append(cur); cur=[]
if cur: groups.append(cur)
# frasi: segmenti tra gruppi
segs=[];start=0;kinds=[]
for g in groups:
    segs.append((start,g[0]-1));kinds.append(len(g));start=g[-1]+1
segs.append((start,len(W)-1));kinds.append(5)
def tstart(k): return W[k][0]
def tend(k): return W[k+1][0] if k+1<len(W) else T
files=[[]]
for (a,b),kd in zip(segs,kinds):
    files[-1].append((a,b))
    if kd>=4: files.append([])
files=[f for f in files if f]
assert len(files)==len(names),(len(files),len(names))
meta={}
for name,ph in zip(names,files):
    parts=[];pt=[];pos=0.0
    for a,b in ph:
        s=quiet(max(0,tstart(a)-0.35),tstart(a)); e=quiet(tend(b)-0.35 if b+1<len(W) else T-0.05, min(T,tend(b)))
        if b+1<len(W) and isT(W[b+1][1]): e=quiet(W[b][0]+0.25,W[b+1][0])
        y=x[int(s*SR):int(e*SR)]
        f=np.ones_like(y);n=min(len(y)//4,int(.012*SR));f[:n]=np.linspace(0,1,n);f[-n:]=np.linspace(1,0,n);y=y*f
        pt.append(round(pos+0.0,2));parts.append(y);pos+=len(y)/SR
        parts.append(np.zeros(int(.6*SR),np.float32));pos+=.6
    y=np.concatenate(parts[:-1]) if len(parts)>1 else parts[0]
    pk=np.abs(y).max();
    w=wave.open(f'{outdir}/{name}.wav','wb');w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes((np.clip(y,-1,1)*32767).astype('<i2').tobytes());w.close()
    meta[name]={'dur':round(len(y)/SR,2),'phrases':pt,'text':[' '.join(w for _,w in W[a:b+1]) for a,b in ph]}
    print(name,meta[name]['dur'],pt)
json.dump(meta,open(f'{outdir}/meta_{names[0]}.json','w'),ensure_ascii=False,indent=1)
