import json,re,os,glob,subprocess
W='/home/user/work';B=W+'/build'
VOX=W+'/vc/scambio/storia-V-lez11/vox'
TXT={x['nome']:x['testo'] for x in json.load(open(W+'/vc/scambio/storia-V-lez11/testi_voci.json'))}
def vpath(n):
    if os.path.exists(f'{VOX}/{n}_R2.wav'): return f'{VOX}/{n}_R2.wav'
    for d in (B+'/vox_fix',VOX,B+'/vox_prov'):
        p=f'{d}/{n}.wav'
        if os.path.exists(p): return p
    return None
def dur(p):
    return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout)
UN={'uno':1,'un':1,'due':2,'tre':3,'tré':3,'quattro':4,'cinque':5,'sei':6,'sette':7,'otto':8,'nove':9}
DIEC={'dieci':10,'undici':11,'dodici':12,'tredici':13,'quattordici':14,'quindici':15,'sedici':16,'diciassette':17,'diciotto':18,'diciannove':19}
TENS={'venti':20,'trenta':30,'quaranta':40,'cinquanta':50}
def _val(s):
    s=s.lower()
    if s in DIEC: return DIEC[s]
    for t,v in TENS.items():
        if s.startswith(t[:-1]):
            r=s[len(t)-1:] if s.startswith(t) is False else s[len(t):]
            r=s[len(t):] if s.startswith(t) else s[len(t)-1:]
            if r=='' : return v
            if r in UN: return v+UN[r]
    return None
def cifre(txt):
    def f(m):
        v=_val(m.group(1))
        return str(1900+v) if v is not None else m.group(0)
    txt=re.sub(r'[Mm]illenovecento(\w+)',f,txt)
    def g(m):
        v=_val(m.group(2))
        return m.group(1)+' e '+str(1900+v) if v is not None else m.group(0)
    txt=re.sub(r'(\b19\d\d) e (\w+)',g,txt)
    return txt
def frasi(txt):
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+',txt.strip()) if s.strip()]
def asr_words(n):
    if os.path.exists(f'{VOX}/{n}_R2.wav'): n=n+'_R2'
    p=f'{B}/asr/{n}.json'
    if not os.path.exists(p): return None
    segs=json.load(open(p));w=[]
    for s in segs: w+=s['parole']
    return w
def tempi_frasi(n,txt):
    """[(t_inizio,t_fine,frase)] nel tempo della voce, allineate con l'ASR se c'è, altrimenti proporzionali"""
    fr=frasi(txt);tot=sum(len(f) for f in fr)
    p=vpath(n);d=dur(p) if p else tot/14.0
    w=asr_words(n)
    if w:
        t0=w[0][0];t1=min(d,w[-1][0]+0.35)
        L=[len(x[1].strip()) for x in w];cum=[0];
        for l in L: cum.append(cum[-1]+l)
        T=cum[-1]
        def at(f):
            target=f*T
            for i,c in enumerate(cum[:-1]):
                if cum[i+1]>=target: return w[i][0]
            return t1
        out=[];acc=0
        for f in fr:
            a=at(acc/tot);acc+=len(f);b=at(acc/tot) if acc<tot else t1
            out.append((a,b,f))
        return out
    out=[];acc=0
    for f in fr:
        out.append((0.15+acc/tot*(d-0.3),0.15+(acc+len(f))/tot*(d-0.3),f));acc+=len(f)
    return out
TOP=[
 dict(n=1,t="L'ascesa di Stalin",lines=["L'ascesa","di Stalin"],fs=128,ex="Lenin · Trockij · Bucharin"),
 dict(n=2,t="La grande svolta e i piani quinquennali",lines=["La grande svolta e","i piani quinquennali"],fs=120,ex="1929 · piani quinquennali"),
 dict(n=3,t="La collettivizzazione e la carestia",lines=["La collettivizzazione","e la carestia"],fs=120,ex="kolchoz · kulaki · Holodomor"),
 dict(n=4,t="Il totalitarismo e il Grande Terrore",lines=["Il totalitarismo e","il Grande Terrore"],fs=128,ex="grandi purghe · Gulag"),
 dict(n=5,t="La società staliniana",lines=["La società","staliniana"],fs=128,ex="culto della personalità · Stachanov"),
 dict(n=6,t="La politica estera e le relazioni internazionali",lines=["La politica estera e","le relazioni internazionali"],fs=100,ex="Società delle Nazioni · Fronte unito"),
]
def tfs(t): return 84 if len(t)<=30 else max(52,round(84*30/len(t)))
TITOLO="L'URSS di Stalin (1924-1939)"
