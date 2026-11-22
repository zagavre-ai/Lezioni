#!/usr/bin/env python3
# Piano dei pezzi del prof: intervalli tenuti (su griglia di fotogrammi), mappa tempo originale -> tempo del pezzo, attivazioni card.
import json, re, math
S=json.load(open('/tmp/w/work/trascr.json'))
FPS=30
def q(t): return round(t*FPS)/FPS
FILL={'um','mm','uh','eh','ah','hm','mhm','ehm'}
def fill(s):
    w=re.sub(r'[^a-zà-ù ]','',s['testo'].lower()).split()
    return len(w)<=2 and all(x in FILL for x in w) or (len(w)==1 and w[0] in ('or',) and s['fine']-s['inizio']<1.2)
def fine_frase(s): return bool(re.search(r'[.?!…]["”»]?$',s['testo'].strip()))
SEG=[(i,s) for i,s in enumerate(S)]
# argomenti
TOP={'D0':(0.0,None),'D0b':(None,209.6),
     1:(209.6,1010.0),2:(1010.0,1753.4),3:(1753.4,2587.8),4:(2587.8,3177.1),5:(3177.1,4003.7),6:(4003.7,4831.2),7:(4831.2,5360.5)}
def intervalli(t0,t1,gap_max=2.5):
    """segmenti con inizio in [t0,t1): tiene tutto tranne i riempitivi; pause >2.5 s -> 1 s; ritorna lista [a,b] su griglia fotogrammi"""
    ss=[s for s in S if t0-0.01<=s['inizio']<t1-0.01 and not fill(s)]
    iv=[]
    for k,s in enumerate(ss):
        a=s['inizio']-0.15; b=s['fine']+0.25
        if k==0: a=max(0,s['inizio']-0.15)
        if iv:
            gap=s['inizio']-ss[k-1]['fine']
            pa,pb=iv[-1]
            if gap<=gap_max: iv[-1][1]=b; continue
            # pausa lunga: 0.5 s dopo la fine precedente e 0.5 s prima dell'inizio: totale 1 s
            iv[-1][1]=ss[k-1]['fine']+0.5; a=s['inizio']-0.5
        iv.append([a,b])
    # ultimo: chiudi 0.3 s dopo la fine, ma non oltre l'inizio del segmento successivo meno 0.15
    nxt=[s for s in S if s['inizio']>=t1-0.01]
    lim=(nxt[0]['inizio']-0.15) if nxt else 1e9
    iv[-1][1]=min(ss[-1]['fine']+0.35,lim)
    out=[]
    for a,b in iv:
        a=q(a); b=q(b)
        if out and a<=out[-1][1]: out[-1][1]=max(out[-1][1],b)
        else: out.append([a,b])
    return out
def mappa(iv):
    """funzione tempo originale -> tempo pezzo (None se tagliato)"""
    acc=0.0; tab=[]
    for a,b in iv: tab.append((a,b,acc)); acc+=b-a
    def f(t):
        for a,b,o in tab:
            if a-1e-6<=t<=b+1e-6: return o+(t-a)
        # in un taglio: porta al punto successivo
        for a,b,o in tab:
            if t<a: return o
        return acc
    f.durata=acc
    return f
if __name__=='__main__':
    PIANO={}
    for k,(t0,t1) in TOP.items():
        if k=='D0': 
            # fine intro: ultimo fine-frase con tempo di uscita <=176 s
            ivs=intervalli(0.0,209.6); f=mappa(ivs)
            cand=[s for s in S if s['fine']<209.5 and fine_frase(s)]
            end=None
            for s in cand:
                if f(s['fine'])<=176.0: end=s
            nx=[s for s in S if s['inizio']>end['fine']+0.01 and not fill(s)][0]
            tcut=nx['inizio']
            PIANO['D0']=dict(orig=[0.0,tcut],iv=intervalli(0.0,tcut),ultime=end['testo'][-80:])
            PIANO['D0b']=dict(orig=[tcut,209.6],iv=intervalli(tcut,209.6))
        elif k=='D0b': continue
        else:
            PIANO[str(k)]=dict(orig=[t0,t1],iv=intervalli(t0,t1))
    for k,v in PIANO.items():
        f=mappa(v['iv']); v['durata']=round(f.durata,2); print(k,v['orig'],'durata %.1f'%f.durata,'intervalli',len(v['iv']),v.get('ultime',''))
    json.dump(PIANO,open('piano.json','w'),indent=1)
