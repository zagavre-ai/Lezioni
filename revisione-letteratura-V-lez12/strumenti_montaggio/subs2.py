import json,re,sys,difflib,unicodedata
sys.path.insert(0,'.')
import plan,align,data
J=json.load(open('states.json'));START=J['START'];FPS=30
RESP=[(r'Reshèrsh','Recherche'),(r'\bPrust\b','Proust'),(r'\bVulf\b','Woolf'),(r'\bGiudit\b','Judith'),(r'\bScespir\b','Shakespeare'),(r'Nìcce','Nietzsche'),(r'Bergsòn','Bergson'),(r'Fròid','Freud'),(r'Àinstain','Einstein'),(r'Dionìsiaco','dionisiaco'),(r'\bFrance\b','Franz')]
def clean(t):
    for a,b in RESP: t=re.sub(a,b,t)
    return t
def ts(x): h=int(x//3600);m=int(x%3600//60);s=x%60;return '%02d:%02d:%06.3f'%(h,m,s)
def wrap(t):
    if len(t)<=42: return t
    w=t.split(' ');best=None
    for i in range(1,len(w)):
        a=' '.join(w[:i]);b=' '.join(w[i:]);d=abs(len(a)-len(b))
        if best is None or d<best[0]: best=(d,a,b)
    return best[1]+'\n'+best[2]
def chunks(text,maxc=84):
    # frasi, poi spezza su virgole/lunghezza
    out=[]
    for s in re.split(r'(?<=[.!?:;])\s+',text.strip()):
        if not s: continue
        words=s.split(' ');cur=[]
        for w in words:
            cur.append(w)
            if len(' '.join(cur))>=maxc-12 and (w[-1] in ',;:' or len(' '.join(cur))>=maxc): out.append(' '.join(cur));cur=[]
        if cur:
            if out and len(' '.join(cur))<14 and len(out[-1])+len(' '.join(cur))<maxc: out[-1]+=' '+' '.join(cur)
            else: out.append(' '.join(cur))
    return out
def kore_cues(text,aw,t0):
    """aw: parole ASR [(t,w)] già in tempo assoluto del video nuovo; allinea per sequenza"""
    chs=chunks(clean(text))
    sw=[];first=[];last=[]
    for c in chs:
        first.append(len(sw));sw+=[w for w in c.split(' ') if align.nrm(w)];last.append(len(sw)-1)
    A=[align.nrm(w) for w in sw];B=[align.nrm(w) for t,w in aw]
    m=difflib.SequenceMatcher(None,A,B,autojunk=False);mp={}
    for i,j,n in m.get_matching_blocks():
        for k in range(n): mp[i+k]=j+k
    def tm(k,end=False):
        if k in mp: return aw[mp[k]][0]+(0.35 if end else 0)
        # interpola
        lo=max([x for x in mp if x<k],default=None);hi=min([x for x in mp if x>k],default=None)
        if lo is None and hi is None: return t0
        if lo is None: return aw[mp[hi]][0]-0.25*(hi-k)
        if hi is None: return aw[mp[lo]][0]+0.28*(k-lo)
        a,b=aw[mp[lo]][0],aw[mp[hi]][0];return a+(b-a)*(k-lo)/(hi-lo)
    cues=[]
    for c,f,l in zip(chs,first,last):
        a=tm(f);b=tm(l,True)
        if b<a+1.0: b=a+1.0
        cues.append((a,b,c))
    return cues
allc=[]
# --- Kore (blocchi con voce dal vecchio audio)
TA=json.load(open('../testi_altri.json'))
TV={x['nome']:x['testo'] for x in json.load(open('../voci/scambio/letteratura-V-lez12/testi_voci.json'))}
OLDS={n:(a,b) for n,a,b in plan.blocks}
def shifted(blk):
    a,b=OLDS[blk];off=START[blk]/FPS-a+(100/FPS if (blk[0]=='S' and blk[1:].isdigit()) else 0)
    return [(t+off,w) for t,w in align.asr_words(a,b)]
for blk in plan.blocks:
    n=blk[0]
    if n in data.MAPS or n in plan.DSEG: continue
    if n=='INTRO1': text=' '.join(TA['INTRO1'])
    elif n in TV and n.startswith('AN') and n!='ANF': text=TV[n]
    elif n in TA and n!='INTRO1': text=' '.join(TA[n])
    else: continue
    aw=shifted(n);allc+=kore_cues(text,aw,START[n]/FPS)
# --- mappe R1-R6
RW={'AN4':'R1','AN9':'R2','AN14':'R3','AN20':'R4','AN26':'R5','ANF':'R6'}
import os
for blk,r in RW.items():
    j=json.load(open(f'../rtr/{r}_t.json')) if os.path.exists(f'../rtr/{r}_t.json') else None
    if not j: continue
    aw=[]
    for s in j:
        cur=None
        for t,p in s['parole']:
            if p.startswith(' ') or cur is None:
                if cur: aw.append(tuple(cur))
                cur=[t,p.strip()]
            else: cur[1]+=p
        if cur: aw.append(tuple(cur))
    off=START[blk]/FPS+0.5
    aw=[(t+off,w) for t,w in aw if align.nrm(w)]
    allc+=kore_cues(TV[r],aw,off)
# --- prof
prof=open('prof_cues.vtt').read().split('\n\n')
NOISE=re.compile(r"^(that's it\.?|t\.|but|yeah.*|mm\.?|uh|okay\.?|tto quanto|eh letterarche\.?|in\.|d'accord\.?)$",re.I)
FIXP=[(r"D'accord\b","d'accordo"),(r"\bConbre\b","Combray"),(r"\bsviadita\b","sbiadita"),(r"\bstanti\b","istanti"),(r"\bRamarica\b","rammarica"),(r"\bSi ramarica\b","Si rammarica"),(r"semmelle","nelle"),(r"la pollinio e il dionisiaco, soprattutto Dionisia\.","l'apollineo e il dionisiaco, soprattutto il dionisiaco."),(r"\bQualcino\b","Qualcuno"),(r"\bratta psicologica\b","trama psicologica")]
for b in prof[1:]:
    l=b.split('\n')
    if len(l)<3: continue
    m=re.match(r'(\d\d):(\d\d):([\d.]+) --> (\d\d):(\d\d):([\d.]+)',l[1])
    a=int(m[1])*3600+int(m[2])*60+float(m[3]);e=int(m[4])*3600+int(m[5])*60+float(m[6])
    t=' '.join(l[2:]).strip()
    if NOISE.match(t.strip()): continue
    for x,y in FIXP: t=re.sub(x,y,t)
    allc.append((a,e,t))
allc=[c for c in allc if not (45.9<c[0]<51.95 and c[2] in ('sulla narrativa e la saggistica','del primo novecento.','sulla narrativa e la saggistica del primo novecento.'))]
allc.append((46.49,51.9,'Buongiorno e benvenuti alla lezione sulla narrativa e la saggistica del primo Novecento.'))
allc.sort()
# normalizza: nessuna sovrapposizione, max 2 righe, minimo 1 s
out=['WEBVTT\n'];prev=0;k=0
for a,b,t in allc:
    a=max(a,prev+0.02);b=max(b,a+1.0)
    out.append(f'{k+1}\n{ts(a)} --> {ts(b)}\n{wrap(t)}\n');prev=b;k+=1
open('/home/user/w/out/Letteratura_Lez12.vtt','w').write('\n'.join(out))
print(k,'sottotitoli; ultimo',ts(prev))
