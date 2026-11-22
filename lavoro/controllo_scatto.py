import sys,json,subprocess,numpy as np
V,TL=sys.argv[1:3];SR=16000
def rd(f,ss=None,d=None):
    c=['ffmpeg','-v','error']+(['-ss',str(ss),'-t',str(d)] if ss is not None else [])+['-i',f,'-ac','1','-ar',str(SR),'-f','f32le','-']
    return np.frombuffer(subprocess.run(c,capture_output=True).stdout,np.float32)
ref=rd('/home/user/Lezioni/kit/suoni/quiz.wav')[:SR*2]
ref=ref/np.sqrt((ref**2).sum())
bad=0
for n,t,l in json.load(open(TL)):
    if not (n.startswith('Q') or n=='VER'):continue
    s=t-1.0;x=rd(V,s,4.5);best=(-1,0)
    # correlazione normalizzata passo 1 ms
    for k in range(0,int(3.0*SR),16):
        seg=x[k:k+len(ref)]
        if len(seg)<len(ref):break
        nrm=np.sqrt((seg**2).sum())+1e-9;c=float((seg*ref).sum()/nrm)
        if c>best[0]:best=(c,k)
    # raffina a campione
    k0=best[1];bb=(-1,k0)
    for k in range(max(0,k0-32),min(len(x)-len(ref),k0+32)):
        seg=x[k:k+len(ref)];c=float((seg*ref).sum()/(np.sqrt((seg**2).sum())+1e-9))
        if c>bb[0]:bb=(c,k)
    sc=s+bb[1]/SR-(t+0.5);ok=abs(sc)<=0.05;bad+=not ok
    print(n,'atteso %.3f trovato %.3f scarto %+.3f corr %.2f'%(t+0.5,s+bb[1]/SR,sc,bb[0]),'OK' if ok else 'DA CORREGGERE')
sys.exit(1 if bad else 0)
