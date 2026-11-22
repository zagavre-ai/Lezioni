# Analisi del video originale del prof: frasi, silenzi, tagli (tutto sulla trascrizione e sull'inviluppo audio)
import json,numpy as np,re,difflib
W=json.load(open('/tmp/w/b/words.json'))   # [t0,t1,parola,fine_frase]
DB=np.load('/tmp/w/b/env_db.npy')            # un valore ogni 10 ms
SIL=-42.0
def speech_end(t,limit):
    """fine reale della parola: dal tempo t avanti finché l'ampiezza resta sotto SIL per 80 ms"""
    i=int(t*100);lim=int(limit*100)
    run=0
    for k in range(i,min(lim,len(DB))):
        if DB[k]<SIL:
            run+=1
            if run>=8:return (k-7)/100
        else:run=0
    return limit
# frasi
SENT=[];s=0
for i,w in enumerate(W):
    if w[3] or i==len(W)-1:
        nxt=W[i+1][0] if i+1<len(W) else W[i][1]+1.5
        SENT.append([W[s][0],speech_end(W[i][1]+0.1,min(nxt,W[i][1]+2.0)),s,i]);s=i+1
def sent_at(t):
    """indice della frase che contiene/precede t"""
    for k,x in enumerate(SENT):
        if x[0]>t:return max(0,k-1)
    return len(SENT)-1
def boundary_near(t,lo=None,hi=None):
    """confine di frase (indice k = inizio della frase k) più vicino a t, con la pausa più lunga nei dintorni; restituisce k"""
    best=None
    for k in range(1,len(SENT)):
        gap=SENT[k][0]-SENT[k-1][1]
        d=abs(SENT[k][0]-t)
        if lo is not None and SENT[k][0]<lo:continue
        if hi is not None and SENT[k][0]>hi:continue
        sc=d-min(gap,2.0)*1.5
        if best is None or sc<best[0]:best=(sc,k)
    return best[1]
def piece_range(k0,k1):
    """pezzo dalle frasi k0 a k1-1 (k1 escluso): inizio 0,15 s prima della frase k0, fine 0,30 s dopo l'ultima frase"""
    a=max(SENT[k0][0]-0.15,(SENT[k0-1][1]+0.05) if k0>0 else 0)
    b=SENT[k1-1][1]+0.30
    if k1<len(SENT):b=min(b,SENT[k1][0]-0.10)
    return a,b
def frames(t):return round(t*30)/30
def silenzi_lunghi(a,b,soglia=2.5):
    """intervalli di silenzio > soglia dentro [a,b]"""
    out=[];i=int(a*100);e=int(b*100);st=None
    for k in range(i,e):
        s=DB[k]<SIL
        if s and st is None:st=k
        if (not s or k==e-1) and st is not None:
            if (k-st)/100>soglia:out.append((st/100,k/100))
            st=None
    return out
def tagli_pause(a,b):
    """sub-intervalli sorgente [(x,y)] di [a,b] con i silenzi >2,5 s ridotti a circa 1 s (0,5 s tenuti da ogni lato)"""
    cur=a;out=[]
    for s,e in silenzi_lunghi(a,b):
        out.append((cur,s+0.5));cur=e-0.5
    out.append((cur,b))
    return [(frames(x),frames(y)) for x,y in out if y-x>0.1]
# --- allineamento delle card sulla trascrizione
def norm(w):return re.sub(r'[^a-zàèéìòù0-9]','',w.lower())
def align_cards(cards_text,t0,t1,min_start=None):
    """per ogni card trova il tempo in cui il prof ne comincia la frase (la prima parola corrispondente), in ordine"""
    idx=[i for i,w in enumerate(W) if t0<=w[0]<=t1]
    toks=[norm(W[i][2]) for i in idx]
    res=[];start=0
    for ci,txt in enumerate(cards_text):
        ct=[norm(x) for x in txt.split() if len(norm(x))>3][:14]
        best=(-1,None)
        for j in range(start,max(start,len(idx)-3)):
            win=toks[j:j+len(ct)+10]
            sc=0
            for c in ct:
                if any(c==x or difflib.SequenceMatcher(None,c,x).ratio()>0.82 for x in win):sc+=1
            sc=sc/len(ct)-0.0003*(j-start)
            if sc>best[0]:best=(sc,j)
        res.append((best[1],best[0]))
        if best[1] is not None and best[0]>0.35:start=best[1]+1
    out=[]
    for j,sc in res:
        out.append((W[idx[j]][0] if j is not None else None,sc))
    return out
if __name__=='__main__':
    print(len(SENT),SENT[0],SENT[-1])
    for t in (178,394,634,675,1031,1281,1342,1566,1708,2018,2278,2481,2781,3099,3185,3279,3374,3455,3538):
        k=boundary_near(t);print(t,'->',k,'%.1f'%SENT[k][0],' '.join(w[2] for w in W[SENT[k][2]:SENT[k][2]+8]))
