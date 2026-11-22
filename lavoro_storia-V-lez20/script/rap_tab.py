import sys,json,re
sys.path.insert(0,'/tmp/w/b')
from prof import S,mapper
from content import *
META=json.load(open('/tmp/w/b/ch/meta.json'))
def mmss(t): return '%d:%02d'%(t//60,t%60)
out=[]
for part in (1,2):
    TL=json.load(open(f'/tmp/w/b/timeline_P{part}.json'))
    out.append(f'\n#### Parte {part}: fine di ogni pezzo del docente\n\n| Pezzo | Fine (minuto) | Ultime 8 parole (trascrizione) | Frase finita |\n|---|---|---|---|')
    ev=[]
    for n,st,d in TL:
        k=n[1:] if n[0]=='D' and n[1:] in META else None
        if not k: continue
        m=META[k];seg=S[m['i1']];words=seg['testo'].split()[-8:];fin=bool(re.search(r'[.?!]["»]?$',seg['testo'].strip()))
        end=st+0.8+m['dur']-0.12
        out.append(f"| {k} | {mmss(end)} | …{' '.join(words)} | {'sì' if fin else 'NO'} |")
        f,_=mapper([tuple(x) for x in m['iv']])
        for t,kind,v in CHUNKS[k].get('ev',[]):
            if kind!='c': continue
            j=min(range(m['i0'],m['i1']+1),key=lambda i:abs(S[i]['inizio']-t))
            ev.append((st+0.8+f(t),k,v,S[j]['testo'][:70],t-S[j]['inizio']))
    out.append(f'\n#### Parte {part}: accensione delle card (tutti i punti)\n\n| Video | Pezzo | Card | Frase del prof vicina | Scarto da inizio frase |\n|---|---|---|---|---|')
    for t,k,v,tx,dl in ev: out.append(f'| {mmss(t)} | {k} | {v+1} | {tx} | {dl:+.1f} s |')
open('/tmp/w/b/out/tabelle.md','w').write('\n'.join(out))
print('\n'.join(out)[:2500])
