# Aggancia ogni slide/scheda al momento in cui il docente ne parla (trascrizione a pause + corrispondenza sfocata).
import json,re,difflib,unicodedata
STOP=set('della delle degli dello nella nelle negli sulla sulle dalla dalle tutti tutte come sono viene vengono molto anche alla alle allo agli quando dove sempre ogni ancora quindi invece essere questo questa questi queste quello quella per con che del dei dal dai nel nei sul sui una uno gli le la il lo un di da in su tra fra'.split())
def norm(s):
    s=unicodedata.normalize('NFD',s.lower());s=''.join(c for c in s if unicodedata.category(c)!='Mn')
    return re.findall(r'[a-z0-9]+',s)
def parole(s):return [w for w in norm(s) if len(w)>=4 and w not in STOP]
IDF={};SOGLIA=2.2
def punteggio(kw,chunk_words):
    sc=0
    for k in kw:
        best=max((difflib.SequenceMatcher(None,k,w).ratio() for w in chunk_words),default=0)
        if best>=0.78:sc+=best*IDF.get(k,1.0)
    return sc
def aggancia(chunks,kwsets,t_lo,t_hi,pesi=None):
    """un tempo per elemento, crescente in [t_lo,t_hi]. Usa le corrispondenze affidabili, il resto per interpolazione sul testo."""
    import math
    from collections import Counter
    IDF.clear();df=Counter(w for kw in kwsets for w in set(kw));N=len(kwsets)
    for w,c in df.items():IDF[w]=1.0+math.log(N/c)*0.6
    idx=[i for i,c in enumerate(chunks) if t_lo-0.01<=c['s']<t_hi]
    n=len(kwsets);pesi=pesi or [1]*n;tot=float(sum(pesi));cum=0;F=[]
    for w in pesi:F.append((cum+w/2)/tot);cum+=w
    W={i:norm(chunks[i]['t']) for i in idx}
    R=t_hi-t_lo
    cand=[]   # per ogni scheda: lista (punteggio, posizione)
    for j,kw in enumerate(kwsets):
        L=[]
        for p,i in enumerate(idx):
            ww=W[i]+(W[idx[p+1]][:6] if p+1<len(idx) else [])
            u=(chunks[i]['s']-t_lo)/R
            sc=punteggio(kw,ww)
            if sc>=SOGLIA:L.append((sc-5.0*abs(u-F[j]),p,sc))
        cand.append(sorted(L,reverse=True)[:6])
    # monotona: programmazione dinamica sulle candidate
    best=[{} for _ in range(n)]
    for j in range(n):
        for (v,p,sc) in cand[j]:
            b=(v,None)
            if j>0:
                for pj,(vj,_) in [(q,t) for k in range(j) for q,t in best[k].items() if q<p]:
                    pass
            best[j][p]=(v,None)
    # versione semplice: massimizza somma con salti (O(n*c^2))
    dp=[{} for _ in range(n)]
    for j in range(n):
        for (v,p,sc) in cand[j]:
            m=(v,None,None)
            for k in range(j-1,-1,-1):
                for q,(vq,_,_) in dp[k].items():
                    if q<p and vq+v>m[0]:m=(vq+v,k,q)
            dp[j][p]=m
    # ricostruzione
    fin=None
    for j in range(n):
        for p,(v,_,_) in dp[j].items():
            if fin is None or v>fin[0]:fin=(v,j,p)
    sel={}
    while fin and fin[1] is not None:
        v,j,p=fin;sel[j]=p
        pv=dp[j][p];fin=(None,pv[1],pv[2]) if pv[1] is not None else None
        if fin:fin=(dp[fin[1]][fin[2]][0],fin[1],fin[2])
    ts=[None]*n;sc=[0]*n
    for j,p in sel.items():ts[j]=chunks[idx[p]]['s'];sc[j]=1
    # interpolazione sul peso del testo
    ancore=[(-0.5,t_lo)]+[(sum(pesi[:j])+pesi[j]/2-0.0,ts[j]) for j in range(n) if ts[j] is not None]+[(tot,t_hi)]
    ancore[0]=(0.0,t_lo)
    for j in range(n):
        if ts[j] is None:
            x=sum(pesi[:j])+pesi[j]/2
            a=max((q for q in ancore if q[0]<=x),key=lambda q:q[0]);b=min((q for q in ancore if q[0]>x),key=lambda q:q[0])
            ts[j]=a[1]+(b[1]-a[1])*(x-a[0])/max(1e-6,b[0]-a[0])
    for j in range(1,n):
        if ts[j]<=ts[j-1]:ts[j]=ts[j-1]+0.5
    return ts,sc
