# verifica offline: per ogni frase detta, primo punto in cui la docente la nomina (2 parole chiave in 5 s o 1 parola rara)
import json,sys,re,difflib,unicodedata,numpy as np
from collections import Counter
U=json.load(open('units.json')); SY=json.load(open(sys.argv[1] if len(sys.argv)>1 else 'sync.json'))
W=[]
for l in open('pk.jsonl'): W+=[(float(t),w) for t,w in json.loads(l)['w']]
def norm(s):
    s=unicodedata.normalize('NFD',s.lower());s=''.join(c for c in s if unicodedata.category(c)!='Mn');return re.sub(r"[^a-z0-9 ]",' ',s)
STOP=set(norm('della delle dello degli sono viene vengono questo questa questi queste quello quella anche come nella nelle negli nello sulla sulle dalla dalle alla alle essere hanno della fibra fibre').split())
WT=np.array([t for t,_ in W]);WN=[norm(w).strip() for _,w in W];DF=Counter(WN)
def kws(t): return list(dict.fromkeys(x for x in norm(t).split() if len(x)>=5 and x not in STOP and not x.isdigit()))
def near(k,x): return x==k or (len(x)>=5 and x[:5]==k[:5]) or difflib.SequenceMatcher(None,k,x).ratio()>=.82
def rare(k): return len(k)>=7 and sum(v for x,v in DF.items() if x[:6]==k[:6])<=4
A=SY['align'];out=[];prev=0
for a in A:
    t=a['t'];ks=kws(U[a['i']]['txt'])[:10];lo=max(prev,t-25);hi=t+15
    idx=np.where((WT>=lo)&(WT<=hi))[0];f=None
    for j in idx:
        hk=[k for k in ks if near(k,WN[j])]
        if not hk: continue
        if any(rare(k) for k in hk): f=j;break
        got=set(k for k in ks for q in idx if WT[j]<=WT[q]<=WT[j]+5 for x in [WN[q]] if near(k,x))
        if len(got)>=2: f=j;break
    if f is None: out.append(None);continue
    out.append(t-WT[f]);prev=WT[f]
d=np.array([x for x in out if x is not None])
print('frasi',len(A),'trovate',len(d),'mediana %.1f'%np.median(d),'tardi>1.5:',(d>1.5).sum(),'tardi>3:',(d>3).sum(),'anticipo>15:',(d<-15).sum())
json.dump(out,open('check_out.json','w'))
