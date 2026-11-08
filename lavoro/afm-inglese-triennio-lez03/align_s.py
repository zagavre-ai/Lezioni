# Allineamento per frasi: ogni frase della docente viene assegnata (in ordine) a una frase del PDF.
# L'inizio di una frase del PDF = inizio della prima frase della docente che la introduce.
import json,re,math,unicodedata,difflib,numpy as np,collections,sys
D='/home/claude/lezioni/afm-inglese-triennio-lez03/'
U=json.load(open(D+'units.json'))
SP=json.load(open(D+'sync.json'))['spoken']
W=[]
for l in open(D+'pk.jsonl'): W+=[(float(t),w) for t,w in json.loads(l)['w']]
def norm(w):
    w=unicodedata.normalize('NFD',w.lower());w=''.join(c for c in w if unicodedata.category(c)!='Mn');return re.sub(r'[^a-z0-9]','',w)
STOP=set("""mentre infine inoltre tuttavia oppure secondo questa della delle dello degli dalla dalle dallo dagli nella nelle nello negli sulla sulle sullo sugli alla alle allo agli questo questa questi queste quello quella quelli quelle sono viene vengono essere hanno anche come dove quando mentre perche invece infatti quindi ovvero ossia sostanza diciamo andiamo andare possiamo possono parliamo parlare abbiamo bisogno situazione situazioni determinate determinato determinata realta ovviamente particolare diverse diversi diversa sempre ancora molto tutti tutte tutto ogni loro altre altri altro altra stesso stessa proprio caso esempio riguarda punto vista tipologia tipologie fibra fibre tessile tessili""".split())
def toks(s): return [norm(x) for x in re.split(r"[\s'’/\-,.;:()«»\"?!]+",s) if len(norm(x))>=4 and norm(x) not in STOP]
def stem(x): return x[:6]
# frasi della docente
S=[];cur=None
for k,(t,w) in enumerate(W):
    if cur is None: cur={'t':t,'k0':k,'w':[]}
    cur['w'].append(w)
    if w[-1:] in '.?!' : cur['k1']=k;S.append(cur);cur=None
if cur: cur['k1']=len(W)-1;S.append(cur)
for s in S: s['txt']=' '.join(s['w']);s['st']=set(stem(x) for x in toks(s['txt']))
# idf sui termini delle frasi della docente
df=collections.Counter(x for s in S for x in s['st']);N=len(S)
idf=lambda x: math.log((N+1)/(df.get(x,0)+1))+0.3
UU=[U[i] for i in SP]
for u in UU: u['st']=set(stem(x) for x in toks(u['txt']))
def near(a,b): return a==b or (len(a)>=5 and len(b)>=5 and a[:5]==b[:5]) or difflib.SequenceMatcher(None,a,b).ratio()>=0.84
def sim(u,s):
    if not u['st'] or not s['st']: return 0.0
    sc=0.0
    for a in u['st']:
        if any(near(a,b) for b in s['st']): sc+=idf(a)
    return sc/math.sqrt(len(u['st'])+4)
INTRO=re.compile(r"^(arriviamo|passiamo|per quanto riguarda|prima di|innanzitutto|oltre a|dall'altra parte|nel momento in cui|parliamo|andiamo a vedere|vediamo|un altro|un'altra|altra|altro|infine|inoltre|successivamente|poi|dopo)",re.I)
# finestra temporale ammessa per ogni frase del PDF (pagine del PDF ± margini)
PST={"2": 23.98, "3": 206.16, "4": 465.72, "5": 617.39, "6": 774.58, "7": 984.77, "8": 1102.65, "9": 1227.53, "10": 1340.83, "11": 1530.8, "12": 1677.27, "13": 1835.05, "14": 1997.98, "15": 2121.51, "16": 2282.73}
PEN={"2": 206.16, "3": 447.42, "4": 608.91, "5": 761.86, "6": 982.53, "7": 1083.38, "8": 1218.77, "9": 1329.23, "10": 1512.31, "11": 1660.37, "12": 1830.73, "13": 1988.37, "14": 2110.15, "15": 2244.36, "16": 2377.83}
def okwin(u,s): p=str(u['pg']); return PST.get(p,0)-60<=s['t']<=PEN.get(p,1e9)+90
n,m=len(UU),len(S)
M=np.zeros((n,m))
for i,u in enumerate(UU):
    for j,s in enumerate(S):
        M[i,j]=sim(u,s) if okwin(u,s) else -3.0
# DP: a(j) non decrescente; una frase del PDF può non ricevere frasi (saltata) con penalità
SKIP=0.8
NEG=-1e9
best=np.full((m,n),NEG);bk=np.zeros((m,n),int)
for i in range(n): best[0,i]=M[i,0]-SKIP*i
for j in range(1,m):
    pm=np.maximum.accumulate(best[j-1]-SKIP*np.arange(n)*0)  # placeholder
    # passaggio: dalla frase i' <= i, saltando (i-i'-1) frasi del PDF
    run=NEG;arg=0
    for i in range(n):
        v=best[j-1,i]+SKIP*i
        if v>run: run=v;arg=i
        stay=best[j-1,i]
        mv=run-SKIP*i-(SKIP*0)  # da arg ad i
        if i>0 and arg<i:
            mv2=run-SKIP*i+SKIP  # salto di (i-arg-1)
        else: mv2=NEG
        if stay>=mv2: best[j,i]=stay+M[i,j];bk[j,i]=i
        else: best[j,i]=mv2+M[i,j];bk[j,i]=arg
# ricostruzione
i=int(np.argmax(best[m-1]));A=[0]*m
for j in range(m-1,-1,-1):
    A[j]=i; i=bk[j,i] if j>0 else i
# sistemazione: frasi brevissime e chiusure restano con la frase precedente; introduzioni passano alla successiva
INTRO2=re.compile(r"^(arriviamo|passiamo|per quanto riguarda|prima di|innanzitutto|oltre a|dall'altra parte|nel momento in cui|quando parliamo|quando diciamo|andiamo a vedere|vediamo|infine|inoltre|un altro|un'altra|un ulteriore|altro aspetto|altra|poi abbiamo|abbiamo poi|tra (le|i) |tra questi|tra queste|tuttavia|questo perch|perch|ma in realt)",re.I)
for it in range(3):
    for j in range(1,m):
        if A[j]!=A[j-1]:
            w=len(S[j]['w'])
            tx=S[j]['txt'].strip()
            intro=bool(INTRO2.match(tx)) or tx.endswith('?') or M[A[j],j]>0.3
            if (w<5 and not intro) or (M[A[j],j]<=0.15 and not intro):
                if j+1<m and A[j+1]==A[j]: A[j]=A[j-1]
    for j in range(1,m):
        if A[j]!=A[j-1]:
            p,q=A[j-1],A[j];k=j-1
            while k>0 and A[k]==p and M[p,k]<=0.2 and (INTRO2.match(S[k]['txt'].strip()) or S[k]['txt'].strip().endswith('?') or M[q,k]>0.3) and A[k-1]==p:
                A[k]=q;k-=1
start={};sents=collections.defaultdict(list)
for j,i in enumerate(A):
    sents[i].append(j)
    if i not in start: start[i]=S[j]['t']
out=[]
for i in range(n):
    if i in start: out.append({'i':SP[i],'t':round(start[i],2),'sent':sents[i]})
    else: out.append({'i':SP[i],'t':None,'sent':[]})
# rifinitura a livello di parola: se la frase del PDF comincia a metà della frase precedente della docente
WT=[t for t,_ in W];WN=[norm(w) for _,w in W]
for k,o in enumerate(out):
    if not o['sent'] or k==0: continue
    j=o['sent'][0]
    if j==0: continue
    pj=S[j-1];u=UU[k]
    first=[stem(x) for x in toks(u['txt'])][:1]
    rare=[a for a in first if len(a)>=6 and idf(a)>2.5]
    if not rare: continue
    ks=list(range(pj['k0'],pj['k1']+1));half=ks[int(len(ks)*0.4):]
    hit=None
    for q in half:
        if any(near(a,stem(WN[q])) for a in rare):
            hit=q;break
    if hit is not None:
        # risali all'inizio dell'inciso (dopo l'ultima virgola prima della parola)
        q=hit
        while q>pj['k0'] and not W[q-1][1].endswith(',') and hit-q<6: q-=1
        o['t']=round(W[q][0]-0.25,2);o['mid']=True
OV=json.load(open(D+'override_s.json')) if __import__('os').path.exists(D+'override_s.json') else {}
for o in out:
    v=OV.get(str(o['i']))
    if v is None or v=='no': continue
    if isinstance(v,str) and v.startswith('prev'):
        j=o['sent'][0] if o['sent'] else None
        if j: o['t']=round(S[j-1]['t'],2)
    elif isinstance(v,str) and v.startswith('w:'):   # parola: «w:mentre@1125»
        wd,ap=v[2:].split('@');ap=float(ap)
        c=[t for t,w in W if t>=ap and norm(w)==norm(wd)]
        if c: o['t']=round(c[0]-0.25,2)
    else: o['t']=float(v)
    o['ov']=True
# frasi del PDF senza frasi assegnate: si accendono insieme alla successiva (restano visibili)
for k in range(n-1,-1,-1):
    if out[k]['t'] is None: out[k]['t']=out[k+1]['t'] if k+1<n else S[-1]['t']
# «no»: frase del PDF che la docente non dice (va nelle animazioni, non sulle slide)
NO={int(k) for k,v in OV.items() if v=='no'}
if NO: SP=[i for i in SP if i not in NO];out=[o for o in out if o['i'] not in NO]
json.dump({'S':[{'t':s['t'],'txt':s['txt']} for s in S],'align':out},open(D+'align_s.json','w'),ensure_ascii=False)
json.dump({'spoken':SP,'align':[{'i':o['i'],'t':o['t']} for o in out]},open(D+'sync2.json','w'))
if __name__=='__main__':
    lo,hi=(float(sys.argv[1]),float(sys.argv[2])) if len(sys.argv)>2 else (0,400)
    for o in out:
        if lo<=o['t']<=hi:
            u=U[o['i']];f=S[o['sent'][0]]['txt'][:90] if o['sent'] else '(nessuna frase: si accende con la successiva)'
            print(f"{o['t']:7.1f} #{o['i']:<3} PDF: {u['txt'][:60]!r}\n          VOCE: {f}")
