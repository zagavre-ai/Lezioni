import json,re,sys,wave,numpy as np
sys.path.insert(0,'/tmp/w14')
from evid import ricostruisci,W
words=ricostruisci(W)   # [t,word] word include punteggiatura
w=wave.open('/tmp/w14/orig_clean.wav');C=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(float);w.close()
SR=48000
def rms(a,b):
    a=int(a*SR);b=int(b*SR);return float(np.sqrt(np.mean(C[a:b]**2))) if b>a else 0
def cand():
    out=[]
    for i in range(len(words)-1):
        t,wd=words[i];nt=words[i+1][0]
        if re.search(r'[.?!…]["»”]?$',wd) and nt-t>0.45:
            lo=t+0.15;hi=nt-0.02
            if hi-lo<0.12: continue
            xs=np.arange(lo,hi,0.01);e=[rms(x,x+0.01) for x in xs];k=int(np.argmin(e))
            out.append((float(xs[k]+0.005),wd,words[i+1][1],nt-lo))
    return out
CA=cand()
OLD={ # fine del pezzo precedente nel tempo originale (e_prev), per ogni confine tra D consecutivi (anche tra parti)
 'P1_D0|D1':181.17,'P1_D1|D2':940.17,'P1_D2|D3':1340.24,'P1_D3|D4':1760.27,'P1D4|P2D0':2030.44,'P2_D0|D1':2038.29,'P2_D1|D2':2167.29,'P2_D2|D3':2374.32,'P2_D3|D4':2502.35,'P2_D4|D5':2850.40,'P2_D5|D6':3150.45}
res={}
for k,e in OLD.items():
    c=[x for x in CA if x[0]>=e-0.05]
    c=c[0]
    res[k]=c[0]
    print(k,'vecchia fine',e,'-> nuova',round(c[0],2),'(+%.1f s)'%(c[0]-e),'| ...',c[1],'|',c[2])
json.dump(res,open('/tmp/w14/cuts.json','w'))
