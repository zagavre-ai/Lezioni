import re,bisect
from lib import *
from common import SEG
from spellchecker import SpellChecker
SP=SpellChecker(language='it')
BAD_START=re.compile(r"^(Allora|Ecco|Guardiamo|D'accordo|Okay|Ok|Esatto|Chiaro|Mi |Vi |Cioè|Insomma|Appunto)",re.I)
FILL=re.compile(r"\b(d'accordo|no\?|uh|um|eh|ehm|vero\?|capito|diciamo|insomma|così dire|per così|ah)\b",re.I)
BAD2=re.compile(r'^(Perch[eé]|Per |Che |Se |O |Quando|Mentre|Dove|Cioè|Insomma|Allora|Ecco|Appunto|Mi |Vi )')
def clean(t):
    t=t.strip()
    t=re.sub(r'\b[Bb]elle [EÈéÉ]?po\w*','Belle Époque',t)
    return t
import difflib as _dl
_RAW=open('/tmp/w/slide1.txt').read()
VT=sorted(set(re.findall(r"[A-Za-zÀ-ÿ]{3,}",_RAW)))
VTL={w.lower() for w in VT}
EXTRA=['Madero','Zapata','Villa','Huerta','Obregón','Porfirio','Díaz','Dreyfus','Zola','Fashoda','Tirpitz','Herero','Weltpolitik','Meiji','Qing','Boxer','Yuan','Shikai','Sun','Yat-sen','Tsushima','Transiberiana','Guglielmo','Bismarck','Nicola','Lenin','Roosevelt','Theodore','Sherman','Antitrust','Hawaii','Filippine','Cuba','Panama','Bosnia','Erzegovina','Serbia','Francesco','Ferdinando','Vittoria','Boeri','Sudafrica','Transvaal','Namibia','Manciuria','Corea','Pechino','Berlino','Entente','cordiale','Parliament','Home','Rule','dominions','Lords','Duma','soviet','menscevichi','bolscevichi','panslavista']
VT=sorted(set(VT)|set(EXTRA));VTL|={w.lower() for w in EXTRA}
def fixwords(t):
    out=[];first=True
    def rep(m):
        w=m.group(0)
        if len(w)<=3 or w.lower() in SP or w.lower() in VTL: return w
        c=_dl.get_close_matches(w,VT,n=1,cutoff=0.72)
        if c: return c[0]
        raise ValueError(w)
    try: return re.sub(r"[A-Za-zÀ-ÿ]+",rep,t)
    except ValueError: return None
def ok_words(t,tol=0):
    bad=0
    for tok in re.findall(r"[A-Za-zÀ-ÿ']+",t):
        parts=[p for p in tok.split("'") if p]
        for p in parts:
            if len(p)<=2 or p[0].isupper(): continue
            if p.lower() not in SP: bad+=1
    return bad<=tol

def build_sents():
    out=[];cur=[];st=None;lastt=0
    for seg in SEG:
        for t,tok in seg['parole']:
            if re.fullmatch(r'\s*[.?!]+\s*',tok):
                if cur:
                    txt=''.join(cur).strip()
                    out.append((st,t,txt,tok.strip()))
                cur=[];st=None;continue
            if st is None and tok.strip() and re.match(r'\s*\w',tok): st=t
            if st is None: continue
            cur.append(tok)
        # segment boundary: keep sentence open
    return out
SENTS=build_sents()
DANGLE=set("la il lo le gli i un una di che e a con per in del della dei delle da su al alla perché perche ma o ed come se non si ci".split())
def sentences_in(a,b,tier=1):
    out=[]
    for st,en,tx,p in SENTS:
        if not(a<=st<b-3) or p!='.': continue
        tx=clean(tx)
        n=len(tx)
        if n<(32 if tier==1 else 26) or n>(138 if tier==1 else 150): continue
        if not tx[0].isupper(): continue
        w0=re.match(r"[A-Za-zÀ-ÿ']+",tx).group(0).lower().split("'")[-1]
        if w0 not in SP and len(w0)>2: continue
        if tier==1 and BAD_START.match(tx): continue
        if FILL.search(tx) or BAD2.match(tx) or len(tx.split())<5: continue
        last=re.findall(r"[A-Za-zÀ-ÿ']+",tx)[-1].lower()
        if last in DANGLE: continue
        tx=fixwords(tx)
        if tx is None: continue
        if not ok_words(tx,0 if tier==1 else 1): continue
        tx=tx[0].upper()+tx[1:]
        out.append((st,tx+'.'))
    return out

VOC=set(w for w in norm(open('/tmp/w/slide1.txt').read()) if len(w)>=5)
def score(tx): return len(set(w for w in norm(tx) if w in VOC))
def pick(a,b,step=22):
    C1=[(t,x,score(x)) for t,x in sentences_in(a,b,1)]
    C2=[(t,x,score(x)) for t,x in sentences_in(a,b,2)]
    picks=[];t=a+1.0;used=-99
    while t<b-8:
        cand=[c for c in C1 if t-10<=c[0]<=t+14 and c[0]>used+12 and c[2]>=2]
        if not cand: cand=[c for c in C1 if t-10<=c[0]<=t+22 and c[0]>used+12 and c[2]>=1]
        if not cand: cand=[c for c in C2 if t-10<=c[0]<=t+22 and c[0]>used+12]
        if not cand: cand=[c for c in C2 if t-10<=c[0]<=t+40 and c[0]>used+12]
        if cand:
            c=max(cand,key=lambda c:c[2]*3+min(len(c[1]),95)/25-abs(c[0]-t)/4)
            picks.append((c[0],c[1]));used=c[0];t=c[0]+step
        else: t+=10
    return picks
if __name__=='__main__':
    p=pick(121.3,1132.24)
    print(len(p))
    for t,x in p[:14]:print(round(t),x)

# ---------------- slide-based cards (testo del docente dalle sue slide, tempi dalla sua voce)
import math
SPAR={int(k):v for k,v in json.load(open('/tmp/w/slide_par.json')).items()}
def _stems(t): return {w[:6] for w in norm(t) if len(w)>=5}
OVR={6:[2923.4,3045,3074,3238,3325],9:[4043.4,4067,4090,4150]}
def slide_pick(a,b,n,mingap=18.0):
    ps=SPAR[n];K=len(ps)
    segs=[s for s in SEG if a-1<=s['inizio']<b-3]
    # window of 2 consecutive segments
    W=[]
    for j,s in enumerate(segs):
        txt=s['testo']+' '+(segs[j+1]['testo'] if j+1<len(segs) else '')
        W.append((s['inizio'],_stems(txt)))
    P=[_stems(p) for p in ps]
    def sc(i,j):
        if not P[i]: return 0
        return len(P[i]&W[j][1])/math.sqrt(len(P[i]))-1.2*abs(W[j][0]-(a+(b-a)*(i+0.3)/K))/(b-a)
    NEG=-1e9
    J=len(W)
    best=[[NEG]*J for _ in range(K)];arg=[[-1]*J for _ in range(K)]
    for j in range(J):
        best[0][j]=sc(0,j)-0.001*(W[j][0]-a) if W[j][0]<a+60 else NEG
    for i in range(1,K):
        run=NEG;rj=-1;ptr=0
        for j in range(J):
            while ptr<J and W[ptr][0]<=W[j][0]-mingap:
                if best[i-1][ptr]>run: run=best[i-1][ptr];rj=ptr
                ptr+=1
            if run>NEG/2:
                best[i][j]=run+sc(i,j);arg[i][j]=rj
    # choose end
    jb=max(range(J),key=lambda j:best[K-1][j]);times=[0]*K
    cur=jb
    for i in range(K-1,-1,-1):
        times[i]=W[cur][0];cur=arg[i][cur] if i>0 else -1
    times[0]=a+0.4
    if n in OVR: times=OVR[n]
    return [(times[i],ps[i]) for i in range(K)]
