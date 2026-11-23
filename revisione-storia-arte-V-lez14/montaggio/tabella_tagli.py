import sys,re,json;sys.path.insert(0,'/tmp/w/build')
import plan
from fixes import fix
from engine import *
tl=plan.build();S=tl.segs;off=0;rows=[]
pieces={}
for s in S:
    nm=s['name']
    if s['spec']['k']=='prof':
        key=nm.split('_')[0];f0=s['spec']['f0'];p=pieces.setdefault(key,dict(fin=off,orig0=f0,orig1=f0+s['n'],end=off+s['n']))
        p['orig1']=max(p['orig1'],f0+s['n']);p['end']=off+s['n']
    off+=s['n']
mm=lambda f:'%d:%02d'%(f/30//60,f/30%60)
out=['| Pezzo | Inizio (minuto) | Prime parole | Fine (minuto) | Ultime 6–8 parole | Frase finita |','|---|---|---|---|---|---|']
for k,p in pieces.items():
    a=p['orig0']/30;b=p['orig1']/30
    segs=[g for g in plan.SEG if g['inizio']>=a-0.3 and g['fine']<=b+0.3]
    first=fix(segs[0]['testo']).split()[:6];last_t=fix(' '.join(g['testo'] for g in segs[-3:])).split()
    last=' '.join(last_t[-8:]);done=bool(re.search(r'[.?!]$',last_t[-1])) if last_t else False
    out.append(f"| {k} | {mm(p['fin'])} | {' '.join(first)}… | {mm(p['end'])} | …{last} | {'sì' if done else 'no'} |")
open('/tmp/w/build/tabella_tagli.md','w').write('\n'.join(out));print('\n'.join(out))
