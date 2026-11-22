# Controlli sulla voce del prof: timbro (acuti >4 kHz rispetto a >100 Hz, dB) e sincronia (scarto in secondi) tra video finale e originale.
# uso: python3 controllo_voce.py VIDEO.mp4 timeline.json
import sys, json, subprocess, numpy as np
sys.path.insert(0,'/home/user/Lezioni/lavoro')
import piani
SRC='/tmp/w/lez10/LEZIONE.10.LA.GERMANIA.DA.WEIMAR.AL.NAZISMO.mp4'
def pcm(f,ss,t,sr=48000):
    c=['ffmpeg','-v','error','-ss',str(ss),'-t',str(t),'-i',f,'-vn','-ac','1','-ar',str(sr),'-f','f32le','-']
    return np.frombuffer(subprocess.run(c,capture_output=True).stdout,np.float32)
def ratio(x,sr=48000):
    w=4096;acc=np.zeros(w//2+1);n=0
    for i in range(0,len(x)-w,w):
        s=x[i:i+w]
        if np.sqrt((s**2).mean())<0.02: continue
        acc+=np.abs(np.fft.rfft(s*np.hanning(w)))**2;n+=1
    f=np.fft.rfftfreq(w,1/sr);hi=acc[f>4000].sum();lo=acc[f>100].sum()
    return 10*np.log10(hi/lo) if n and lo>0 else None
def lag(a,b,sr=8000):
    # cross-correlazione dell'inviluppo (scarto in s, positivo = a in ritardo)
    n=min(len(a),len(b));a=np.abs(a[:n]);b=np.abs(b[:n]);k=np.ones(80)/80;a=np.convolve(a,k,'same');b=np.convolve(b,k,'same')
    a-=a.mean();b-=b.mean();M=int(0.3*sr)
    c=np.correlate(a,b[M:-M] if False else b,'full');mid=len(c)//2
    seg=c[mid-M:mid+M];return (np.argmax(seg)-M)/sr
if __name__=='__main__':
    V,TL=sys.argv[1:3];tl={n:(s,d) for n,s,d in json.load(open(TL))}
    P={p['id']:p for p in piani.pezzi()};m={'D0':'D0','D0B':'DI'}|{f'D{n}':f'A{n}' for n in range(1,9)}
    ro=[];rf=[];lags=[]
    for nome,pid in m.items():
        if nome not in tl: continue
        s,d=tl[nome];p=P[pid];s0=p['ranges'][0][0]
        t=min(40,d-1)
        fin=pcm(V,s+1,t,8000);org=pcm(SRC,s0+1,t,8000);lags.append((nome,round(lag(fin,org),3)))
        rf.append(ratio(pcm(V,s,min(d,300)),48000));ro.append(ratio(pcm(SRC,p['ranges'][0][0],min(d,300)),48000))
    print('rapporto >4kHz / >100Hz in dB (originale):',[round(x,1) for x in ro if x is not None])
    print('rapporto >4kHz / >100Hz in dB (video finale):',[round(x,1) for x in rf if x is not None])
    print('scarto audio finale-originale (s):',lags)
