# Allineamento frasi del PDF ↔ parlato della docente (parole con tempi)
import json,re,math,unicodedata,numpy as np,collections
U=json.load(open('/home/claude/lezioni/afm-inglese-triennio-lez01/units.json'))
W=[]
for l in open('/home/claude/lezioni/afm-inglese-triennio-lez01/pk.jsonl'):
    d=json.loads(l); W+=d['w']
PG=[0, 0, 410, 780, 1660, 1980, 2440, 2900, 3255, 3405, 3732, 3732]  # pagine: tempi dai passaggi di argomento nella trascrizione (master)
def pstart(p):return PG[p-1]
def pend(p):return PG[p]
STOP=set("""il lo la i gli le un uno una di a da in con su per tra fra e o ed od che chi cui non più come anche ma se si ci ne è sono essere viene vengono può possono questo questa questi queste quello quella quelli quelle del dello della dei degli delle al allo alla ai agli alle dal dallo dalla dai dagli dalle nel nello nella nei negli nelle sul sullo sulla sui sugli sulle col tutto tutti tutte molto ogni loro suo sua suoi sue essa esse esso essi altre altri altro altra stesso stessa invece infatti quindi ovvero ossia cioè dove quando mentre poi solo così tale tali grande grandi base modo tipo caso parte""".split())
def norm(w):
    w=unicodedata.normalize('NFD',w.lower()); w=''.join(c for c in w if unicodedata.category(c)!='Mn')
    return re.sub(r'[^a-z0-9]','',w)
def stem(w):
    w=norm(w)
    if w.isdigit(): return w
    return w[:6] if len(w)>6 else w
def keys(text):
    ks=[]
    for w in re.split(r"[\s'’/\-,.;:()«»\"]+",text):
        n=norm(w)
        if len(n)<4 and not n.isdigit(): continue
        if n in STOP: continue
        ks.append(stem(w))
    return ks
TW=np.array([t for t,_ in W]); TS=[stem(w) for _,w in W]
df=collections.Counter(TS); N=len(TS)
def idf(k):return math.log((N+1)/(df.get(k,0)+1))
pos=collections.defaultdict(list)
for i,s in enumerate(TS): pos[s].append(TW[i])
T=int(TW[-1])+30; GRID=np.arange(0,T,0.5)
def score_fun(u):
    ks=list(dict.fromkeys(keys(u['txt'])))
    L=max(6,min(45,len(u['txt'])*0.07))
    sc=np.zeros(len(GRID))
    first=np.full(len(GRID),np.inf)
    for k in ks:
        if k not in pos or df[k]>N*0.01: continue
        w=idf(k); ts=np.array(pos[k])
        # per ogni t: c'è un'occorrenza in [t,t+L]?
        j=np.searchsorted(ts,GRID); has=(j<len(ts))
        nxt=np.where(has,ts[np.minimum(j,len(ts)-1)],np.inf)
        hit=(nxt-GRID)<=L
        sc+=w*hit
        first=np.where(hit,np.minimum(first,nxt),first)
    return sc,first,ks
def run(idx=None):
    UU=[U[i] for i in idx] if idx is not None else U
    n=len(UU); M=len(GRID)
    S=[];F=[]
    for u in UU:
        sc,fi,_=score_fun(u)
        p=u['pg']; lo=pstart(p)-150; hi=pend(p)+150
        pen=np.where((GRID>=lo)&(GRID<=hi),0,-50.0)
        S.append(sc+pen-0.002*GRID); F.append(fi)
    # DP monotona: t_i >= t_{i-1}+1s
    gap=2  # celle (1 s)
    best=np.full((n,M),-1e9); arg=np.zeros((n,M),int)
    best[0]=S[0]
    for i in range(1,n):
        prev=best[i-1]
        cm=np.maximum.accumulate(prev); ca=np.zeros(M,int)
        # argmax cumulativo
        ar=np.arange(M); am=np.where(prev==cm,ar,0); am=np.maximum.accumulate(am)
        sh=np.full(M,-1e9); sh[gap:]=cm[:-gap]; sha=np.zeros(M,int); sha[gap:]=am[:-gap]
        best[i]=S[i]+sh; arg[i]=sha
    j=int(np.argmax(best[-1])); path=[j]
    for i in range(n-1,0,-1): j=arg[i][j]; path.append(j)
    path=path[::-1]
    out=[]
    for i,j in enumerate(path):
        t=GRID[j]; f=F[i][j]
        st=f if np.isfinite(f) else t
        # ultima parola chiave della frase, prima dell'inizio della frase successiva
        _,_,ks=score_fun(UU[i]); L=max(6,min(45,len(UU[i]['txt'])*0.07))
        nx=GRID[path[i+1]] if i+1<len(path) else t+L
        hits=sorted(x for k in ks if k in pos and df[k]<=N*0.01 for x in pos[k] if st-0.01<=x<=max(nx,st)+L*0.5)
        hits=[x for x in hits if x<=st+L]
        out.append({'i':int(idx[i]) if idx is not None else i,'first':round(float(st),2),'last':round(float(hits[-1]),2) if hits else round(float(st),2),'grid':float(t),'score':round(float(S[i][j]),2)})
    # inizio = subito dopo l'ultima parola chiave della frase precedente (al massimo 15 s prima della prima parola chiave)
    for k,o in enumerate(out):
        if k==0: o['t']=max(0,o['first']-1.0); continue
        jn=int(np.searchsorted(TW,out[k-1]['last']+0.05)); nxt=float(TW[jn]) if jn<len(TW) else out[k-1]['last']+1.0
        b=max(nxt-0.15, o['first']-15)
        o['t']=round(min(b,o['first']-0.3),2)
    # monotonia sui tempi raffinati
    for k in range(1,len(out)):
        if out[k]['t']<out[k-1]['t']+1.0: out[k]['t']=round(out[k-1]['t']+1.0,2)
    return out
if __name__=='__main__':
    A=run(); json.dump(A,open('/home/claude/lezioni/afm-inglese-triennio-lez01/align.json','w'))
    for a in A:
        u=U[a['i']]; print(a['i'],u['pg'],'%7.1f'%a['t'],'%5.1f'%a['score'],u['txt'][:70])
