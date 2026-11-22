import json,re,unicodedata
T=json.load(open('/home/claude/w19/trasc.json'))
P=json.load(open('/home/claude/w19/slide.json'))
def norm(s):
    s=unicodedata.normalize('NFD',s.lower());s=''.join(c for c in s if unicodedata.category(c)!='Mn')
    return re.findall(r'[a-z0-9]+',s)
STOP=set('della delle degli dello dalla nella nelle sono viene stato quella questo questi anche come dopo ogni verso tutti molto tutto fatto sulla sulle poi per con che una uno gli dei del dal nel alla loro non piu sua suoi suo'.split())
def keys(txt):
    return {w for w in norm(re.sub('<[^>]+>','',txt)) if len(w)>=5 and w not in STOP}
cards=[]
for p in P:
    for i,t in enumerate(p['par']):
        if p['n']>1: cards.append((p['n'],i,re.sub('<[^>]+>','',t)))
segw=[set(norm(s['testo'])) for s in T]
def score(ci,si,win=3):
    k=keys(cards[ci][2]);
    if not k: return 0
    w=set().union(*segw[si:si+win]);return len(k&w)/len(k)
# DP: assegna a ogni card un segmento di inizio, ordine crescente, ma tra pagine il prof torna indietro: lo trattiamo card per card in ordine pagina
N=len(T);C=len(cards)
import sys
res=[]
last=0
for ci in range(C):
    best=max(range(N),key=lambda si:(score(ci,si),-abs(si-last)))
    res.append(best)
if __name__=='__main__':
    for ci,(pg,i,t) in enumerate(cards):
        s=res[ci];print(pg,i,round(score(ci,s),2),s,T[s]['inizio'],'|',t[:50],'|',T[s]['testo'][:70])
