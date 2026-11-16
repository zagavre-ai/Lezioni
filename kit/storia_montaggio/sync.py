# Allineamento slide <-> parlato del docente.
# 1) parole con tempi dalla trascrizione a pezzi: dentro ogni pezzo, il tempo di una parola e' proporzionale ai caratteri
#    sul solo tempo di parlato (maschera di energia, esclude le pause).
# 2) per ogni card della slide: finestra scorrevole di parole, punteggio = parole significative in comune (peso idf).
import json,re,subprocess,numpy as np,unicodedata,math
STOP=set("il lo la i gli le un uno una di a da in con su per tra fra e ed o ma che chi cui non si è sono del dello della dei degli delle al allo alla ai agli alle dal dallo dalla dai dagli dalle nel nello nella nei negli nelle sul sullo sulla sui sugli sulle come più anche poi molto questo questa questi queste quello quella ci ne se ha hanno essere era erano stato stata dopo prima".split())
def norm(w):
    w=unicodedata.normalize('NFD',w.lower());w=''.join(ch for ch in w if unicodedata.category(ch)!='Mn')
    return re.sub(r'[^a-z0-9]','',w)
def stem(w):return w[:6]
def words_with_times(tr,wav):
    x=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',wav,'-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout,np.float32)
    h=800;n=len(x)//h;en=np.sqrt((x[:n*h].reshape(n,h)**2).mean(1))
    thr=max(0.004,np.percentile(en,20)*1.5);act=(en>thr).astype(float)   # 50 ms
    W=[]
    for seg in tr:
        a,b=int(seg['s']/0.05),min(n,int(seg['e']/0.05))
        ws=seg['t'].split()
        if not ws or b<=a:continue
        m=act[a:b];cs=np.concatenate([[0],np.cumsum(m)]);tot=cs[-1]
        if tot<2:cs=np.linspace(0,1,len(m)+1);tot=1
        L=[len(w)+1 for w in ws];cum=np.concatenate([[0],np.cumsum(L)])/sum(L)
        for w,c0 in zip(ws,cum[:-1]):
            k=int(np.searchsorted(cs,c0*tot-1e-9));W.append((round((a+min(k,len(m)))*0.05,2),w))
    return W
def best_start(cardtext,W,lo,hi,idf,win=None):
    """istante in [lo,hi] in cui il parlato assomiglia di piu' alla card (finestra di parole)."""
    ct=[stem(norm(w)) for w in cardtext.split() if norm(w) and norm(w) not in STOP]
    cs=set(ct)
    if not cs:return None,0
    n=win or max(14,int(len(cardtext.split())*1.2))
    idx=[i for i,(t,w) in enumerate(W) if lo<=t<=hi]
    if not idx:return None,0
    best=(0,None)
    stems=[stem(norm(w)) for t,w in W]
    for i in idx:
        seen=set(stems[i:i+n])&cs
        sc=sum(idf.get(s,1.0) for s in seen)/sum(idf.get(s,1.0) for s in cs)
        if sc>best[0]+1e-9:best=(sc,W[i][0])
    return best[1],best[0]
