# allinea il video finale al video originale del prof (solo nei pezzi del docente: INTRO e D*), finestre da 2 s ogni 0,5 s
import numpy as np,sys,json
from scipy.signal import fftconvolve
SR=8000
fin=np.fromfile(sys.argv[1],np.int16).astype(np.float32);src=np.fromfile(sys.argv[2],np.int16).astype(np.float32)
TL=json.load(open(sys.argv[3]))
segs=[(a,a+d) for n,a,d in TL if n=='INTRO' or (n.startswith('D') and n[1:].isdigit())]
W=int(2*SR);H=int(0.5*SR)
cs=np.concatenate([[0],np.cumsum(src.astype(np.float64)**2)])
def ncc(w,a,b):
    a=max(0,a);b=min(len(src),b)
    if b-a<len(w): return -1,0
    seg=src[a:b];c=fftconvolve(seg,w[::-1],mode='valid')
    e=np.sqrt(cs[a+len(w):b+1]-cs[a:b-len(w)+1])+1e-6
    v=c/(e*np.linalg.norm(w)+1e-6);i=int(np.argmax(v));return float(v[i]),a+i
# ricerca globale grossolana sull'inviluppo (100 campioni/s)
def env(x):n=len(x)//80;return np.abs(x[:n*80]).reshape(n,80).mean(1)
ES=env(src)
def globale(s):
    w=env(fin[s:s+int(6*SR)]);w=w-w.mean()
    c=fftconvolve(ES-ES.mean(),w[::-1],mode='valid');cand=np.argsort(c)[-5:]
    best=(-1,0)
    for k in cand:
        sc,p=ncc(fin[s:s+W],k*80-int(2*SR),k*80+int(4*SR)+W)
        if sc>best[0]:best=(sc,p)
    return best
res=[]
for A,B in segs:
    prev=None
    for s in range(int(A*SR),int((B-2)*SR),H):
        w=fin[s:s+W]
        if np.sqrt((w**2).mean())<150: res.append((s/SR,None,0));continue
        best=(-1,0)
        if prev is not None:
            p0=s+int(prev*SR);sc,p=ncc(w,p0-int(1.5*SR),p0+int(1.5*SR)+W)
            if sc<0.55: sc,p=ncc(w,p0-int(5*SR),p0+int(120*SR)+W)
            best=(sc,p)
        if best[0]<0.55: best=globale(s)
        if best[0]>=0.55: prev=(best[1]-s)/SR;res.append((s/SR,round(prev,4),round(best[0],3)))
        else: res.append((s/SR,None,round(best[0],3)))
json.dump({'segs':segs,'res':res},open(sys.argv[4],'w'))
ok=[r for r in res if r[1] is not None];print('finestre',len(res),'agganciate',len(ok),flush=True)
