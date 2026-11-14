# uso: trascrivi.py audio16k.wav out.json  -> [[t0,t1,testo],...] segmentando sulle pause
import sys,json,numpy as np,subprocess
sys.path.insert(0,'/home/user/lav/tools');import pk_asr as pk
from multiprocessing import Pool
W,OUT=sys.argv[1:3];SR=16000
x=pk.load(W)
hop=int(0.05*SR);n=len(x)//hop
e=np.array([np.sqrt(np.mean(x[i*hop:(i+1)*hop]**2)+1e-12) for i in range(n)])
thr=max(np.percentile(e,20)*1.5,0.004)
sil=e<thr
# segmenti: tagli nelle pause (>=0.35s) cercando segmenti 6-27 s
segs=[];s=0;i=0
while s<n:
    end=min(n,s+int(12/0.05))
    if end>=n:segs.append((s,n));break
    # miglior pausa nella finestra [s+6s, end]
    best=None;j=s+int(4/0.05)
    while j<end:
        if sil[j]:
            k=j
            while k<end and sil[k]:k+=1
            if k-j>=5 and (best is None or k-j>=best[1]-best[0]):best=(j,k)
            j=k
        else:j+=1
    cut=(best[0]+best[1])//2 if best else end
    segs.append((s,cut));s=cut
def f(sg):
    a,b=sg;return [a*0.05,b*0.05,pk.transcribe(x[a*hop:b*hop])]
if __name__=='__main__':
    with Pool(4) as p:R=p.map(f,segs,chunksize=1)
    json.dump(R,open(OUT,'w'),ensure_ascii=False,indent=0);print(len(R),'segmenti')
