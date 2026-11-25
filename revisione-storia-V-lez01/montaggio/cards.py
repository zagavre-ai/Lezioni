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
