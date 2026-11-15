# allinea ogni card (frase della videodispensa) all'inizio della frase del docente che la introduce
import json,re,sys,unicodedata
def norm(s):
    s=unicodedata.normalize('NFD',s.lower());s=''.join(c for c in s if unicodedata.category(c)!='Mn')
    return re.findall(r"[a-z]+",s)
STOP=set('della delle degli dello nella nelle negli sulla sulle come anche quindi perche sono viene vengono essere tutto tutta questa questo quella quello dove quando altro altri altre poi piu loro alla allo agli alle dalla dalle dagli dallo cosa fatto fatta solo propri proprio'.split())
def key(w):return w[:5]
def kws(s):return [key(w) for w in norm(s) if len(w)>3 and w not in STOP]
def allinea(cards,tr,t0,t1):
    W=[(w[0],key(x)) for s in tr['seg'] for w in s['w'] for x in norm(w[2]) if len(x)>3 and x not in STOP]
    W=[w for w in W if t0-2<=w[0]<=t1+2]
    res=[];pos=0
    for c in cards:
        K=set(kws(c));best=(-1,pos)
        if not K: res.append(None);continue
        for i in range(pos,len(W)):
            win=W[i:i+max(8,len(K)*2)]
            sc=len(K & {w for _,w in win})/len(K)
            # leggera preferenza per la vicinanza
            sc-=0.0005*(i-pos)
            if sc>best[0]+1e-9:best=(sc,i)
        sc,i=best
        if sc>=0.34:
            win=W[i:i+max(8,len(K)*2)];j=next(n for n,(t,w) in enumerate(win) if w in K)
            res.append((round(win[j][0],2),round(sc,2)));pos=i+j+1
        else: res.append((None,round(sc,2)))
    return res
