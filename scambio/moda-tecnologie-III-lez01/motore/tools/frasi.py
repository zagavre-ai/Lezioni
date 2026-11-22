# Divide la dispensa in frasi intere (una card = una frase) e le allinea ai tempi della trascrizione.
import re,json,pymupdf,unicodedata
def norm(w):
    w=unicodedata.normalize('NFD',w.lower());w=''.join(c for c in w if unicodedata.category(c)!='Mn')
    return re.sub(r'[^a-z0-9]','',w)
def elementi(path,da=2):
    """paragrafi e punti elenco, ciascuno con pagina di partenza; ogni elemento = [(testo, pagina)] riga per riga"""
    d=pymupdf.open(path);els=[];cur=[]
    for i in range(da-1,len(d)):
        for ln in d[i].get_text().split('\n'):
            s=ln.strip()
            if not s:continue
            if s=='-':
                if cur:els.append(cur)
                cur=[];continue
            cur.append((s,i+1))
    if cur:els.append(cur)
    return els
def spezza_el(el):
    txt='';pos=[]
    for s,p in el:
        if txt:txt+=' '
        pos.append((len(txt),p));txt+=s
    # indici di fine frase
    cuts=[];
    for m in re.finditer(r'[.?!](?=\s+[A-ZÀ-Ý"«])',txt):
        pre=txt[:m.end()]
        if re.search(r'(\bn\.|\bd\.C\.|\ba\.C\.|\bss\.|\bProf\.ssa)$',pre):continue
        cuts.append(m.end())
    out=[];a=0
    for c in cuts+[len(txt)]:
        f=txt[a:c].strip()
        if f:
            pg=[p for o,p in pos if o<=a][-1] if pos else 0
            out.append((pg,f))
        a=c
    return out
def frasi(path):
    out=[]
    for el in elementi(path):
        out+=spezza_el(el)
    return out
def parole_asr(trasc):
    W=[]
    for s in trasc:
        for t,p in s['parole']:
            if p.startswith(' ') or not W: W.append([t,p.strip()])
            else: W[-1][1]+=p
    return [(t,w,norm(w)) for t,w in W]

def allinea(fr,W,finestra=420):
    """per ogni frase: indice parola ASR di inizio e fine (monotono). Restituisce lista di dict."""
    from collections import Counter
    N=len(W);nw=[w[2] for w in W];res=[];prev=0
    for k,(pg,f) in enumerate(fr):
        toks=[norm(x) for x in f.split()];toks=[x for x in toks if x]
        cont=[x for x in toks if len(x)>=4]
        S=set(cont);n=len(toks)
        if not S:S=set(toks)
        best=(-1,prev,prev)
        lenwin=int(n*1.5)+12
        for s in range(prev,min(N-1,prev+finestra)):
            if nw[s] not in S and nw[min(s+1,N-1)] not in S: continue
            seg=nw[s:s+lenwin];found=S&set(seg)
            sc=len(found)/len(S)-0.0004*(s-prev)
            # bonus se le prime 2 parole-chiave compaiono nelle prime 8 parole
            head=set(nw[s:s+8]);first=[x for x in cont[:2]]
            sc+=0.15*sum(x in head for x in first)/max(1,len(first))
            if sc>best[0]:
                last=s
                for j,x in enumerate(seg):
                    if x in S:last=s+j
                best=(sc,s,last)
        sc,s,e=best
        # affina l'inizio: prima parola-chiave della frase trovata vicino a s
        res.append(dict(k=k,pg=pg,testo=f,i0=s,i1=e,t0=W[s][0],t1=W[min(e+1,N-1)][0],sc=round(sc,2)))
        prev=max(e+1,prev+1) if sc>0.35 else prev
    return res

def allinea2(fr,trasc,W):
    """DP monotono segmenti ASR -> frasi PDF. Restituisce per ogni frase t0 (inizio parlato) e confidenza."""
    import numpy as np
    seg=trasc;n=len(seg);m=len(fr)
    ST=[set(x for x in (norm(w) for w in s['testo'].split()) if len(x)>=4) for s in seg]
    SJ=[set(x for x in (norm(w) for w in f.split()) if len(x)>=4) for _,f in fr]
    sc=np.zeros((n,m),dtype=np.float32)
    for i in range(n):
        T=ST[i]
        if not T:continue
        for j in range(m):
            if SJ[j]:
                o=len(T&SJ[j])
                sc[i,j]=o/len(T)*min(1.0,o/3)-0.28
    NEG=-1e9
    dp=np.full((n,m),NEG,dtype=np.float32);bp=np.zeros((n,m),dtype=np.int32)
    dp[0,:]=sc[0,:]
    for i in range(1,n):
        # miglior precedente con indice <= j (non decrescente)
        run=np.maximum.accumulate(dp[i-1]);arg=np.zeros(m,dtype=np.int32);b=0
        for j in range(m):
            if dp[i-1][j]>=dp[i-1][b]:b=j
            arg[j]=b
        dp[i]=run+sc[i];bp[i]=arg
    j=int(np.argmax(dp[-1]));path=[0]*n
    for i in range(n-1,-1,-1):
        path[i]=j;j=int(bp[i][j])
    # per ogni frase: segmenti assegnati
    ass={}
    for i,j in enumerate(path):ass.setdefault(j,[]).append(i)
    # indici parola per segmento
    first_w=[];k=0
    for s in seg:
        first_w.append(k);k+=len(set())+sum(1 for t,p in s['parole'] if p.startswith(' ') or True) if False else 0
    return path,ass,sc

def allinea3(fr,trasc,pagine_seg):
    """DP monotono segmenti->frasi con IDF, numeri e vincolo di pagina (pagine_seg[i]=pagina PDF 0-based del segmento i)."""
    import numpy as np,math
    from collections import Counter
    n=len(trasc);m=len(fr)
    tk=lambda s:set(x for x in (norm(w) for w in s.split()) if len(x)>=4 or x.isdigit() and len(x)>=1)
    SJ=[tk(f) for _,f in fr];ST=[tk(s['testo']) for s in trasc]
    df=Counter(x for S in SJ for x in S)
    idf={x:math.log((m+1)/(c+0.5)) for x,c in df.items()}
    sc=np.full((n,m),-1.0,dtype=np.float32)
    for i in range(n):
        P=pagine_seg[i]+1;T=ST[i]
        den=sum(idf.get(x,1.5) for x in T) or 1
        for j in range(m):
            if abs(fr[j][0]-P)>1:continue
            o=sum(idf[x] for x in (T&SJ[j]))
            sc[i,j]=o/den-0.22
    NEG=-1e9
    dp=np.full((n,m),NEG,dtype=np.float32);bp=np.zeros((n,m),dtype=np.int32)
    dp[0]=sc[0]
    for i in range(1,n):
        arg=np.zeros(m,dtype=np.int32);b=0
        for j in range(m):
            if dp[i-1][j]>=dp[i-1][b]:b=j
            arg[j]=b
        run=np.maximum.accumulate(dp[i-1]);dp[i]=run+sc[i];bp[i]=arg
    j=int(np.argmax(dp[-1]));path=[0]*n
    for i in range(n-1,-1,-1):
        path[i]=j;j=int(bp[i][j])
    return path,sc

def tempi_frasi(fr,trasc,path,W,sc):
    """t0/t1 per ogni frase: ancorata al primo segmento assegnato, interpolata dove manca"""
    n=len(fr);ass={}
    for i,j in enumerate(path):
        if float(sc[i,j])>0:ass.setdefault(j,[]).append(i)
    t0=[None]*n
    for j,iis in ass.items():t0[j]=trasc[iis[0]]['inizio']
    # interpolazione proporzionale alle parole tra ancore
    anc=[j for j in range(n) if t0[j] is not None]
    for a,b in zip(anc,anc[1:]+[None]):
        ta=t0[a];tb=t0[b] if b is not None else trasc[-1]['fine']
        js=list(range(a,b if b is not None else n))
        L=[len(fr[j][1].split()) for j in js];tot=sum(L);acc=0
        for j,l in zip(js,L):
            if t0[j] is None:t0[j]=ta+(tb-ta)*acc/tot
            acc+=l
    for j in range(anc[0]):t0[j]=0.0
    return t0
