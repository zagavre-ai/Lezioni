#!/usr/bin/env python3
# Allinea le card delle slide del prof alla trascrizione: tempo (originale) in cui il prof comincia la frase di ogni card.
import json, re, unicodedata
S=json.load(open('/tmp/w/work/trascr.json'))
C=json.load(open('/home/user/Lezioni/lavoro/storia-V-lez08/cards.json'))
def norm(w): return re.sub(r'[^a-z0-9]','',unicodedata.normalize('NFD',w.lower()).encode('ascii','ignore').decode())
W=[]  # (t, parola_norm, indice_segmento)
for si,s in enumerate(S):
    for t,w in s['parole']:
        n=norm(w)
        if n: W.append((t,n,si))
# argomenti: (nome, t0, t1, [indici sezioni nell'ordine in cui le dice il prof])
TOP=[(1,209.6,1010.0,[0]),(2,1010.0,1753.4,[2,1]),(3,1753.4,2587.8,[3]),(4,2587.8,3094.0,[4]),(5,3094.0,4003.7,[5]),(6,4003.7,4831.2,[6]),(7,4831.2,5360.1,[7])]
STOP=set('della delle degli dello nella nelle sono viene stato dalla dalle quale quali anche questo questa nello alla alle agli come dopo molto tutti tutte loro suoi sulla'.split())
def tok(card):
    h,_,r=card.partition(': ')
    ts=[norm(w) for w in (h+' '+r).split()]
    return [t for t in ts if len(t)>=5 and t not in STOP]
def quasi(a,b): return a==b or (len(a)>=6 and len(b)>=6 and (a[:6]==b[:6]))
import math, collections
from collections import Counter
df=Counter()
allst=[w[1][:5] for w in W]
cnt=Counter(allst); N=len(allst)
def idf(st): return math.log(N/(1+cnt.get(st,0)))
out={}
for n,t0,t1,secs in TOP:
    idx=[i for i,w in enumerate(W) if t0-0.01<=w[0]<t1]
    cards=[(si,ci,c) for si in secs for ci,c in enumerate(C[si]['cards'])]
    res=[]
    for k,(si,ci,c) in enumerate(cards):
        T={t[:5] for t in tok(c)}; H={t[:5] for t in tok(c.partition(': ')[0])}
        wsum=sum(idf(t) for t in T) or 1
        best=(-1,idx[0])
        for p,i in enumerate(idx):
            win=allst[i:i+30]; ws=set(win)
            sco=sum(idf(t) for t in T if t in ws)/wsum
            sco+=0.3*sum(idf(t) for t in H if t in set(win[:12]))/(sum(idf(t) for t in H) or 1)
            if sco>best[0]: best=(sco,i)
        wi=best[1]; seg=W[wi][2]
        while seg>0 and not re.search(r'[.?!]["”]?$',S[seg-1]['testo'].strip()) and S[seg]['inizio']-S[seg-1]['fine']<2.5: seg-=1
        res.append(dict(sez=si,card=ci,t=round(S[seg]['inizio'],2),punteggio=round(best[0],2),testo=c))
    out[n]=res
json.dump(out,open('allinea.json','w'),ensure_ascii=False,indent=1)
for n,r in out.items():
    print('== T',n)
    for x in sorted(r,key=lambda x:x['t']): print(' %7.1f %.2f s%d c%d %s'%(x['t'],x['punteggio'],x['sez'],x['card'],x['testo'][:60]))
