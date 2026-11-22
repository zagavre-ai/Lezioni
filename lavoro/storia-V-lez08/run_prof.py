#!/usr/bin/env python3
import sys,os,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import build_prof as B
O='/tmp/w/work/out'
for gruppo,p0 in [([1,2,3],3),([4,5,6,7],3)]:
    p=p0
    for t in gruppo:
        if os.path.exists(f'{O}/D{t}.mkv') and os.path.exists(f'{O}/D{t}_stati.json') and os.path.getsize(f'{O}/D{t}.mkv')>1e8 and os.path.exists(f'{O}/D{t}.ok'):
            p=json.load(open(f'{O}/D{t}_stati.json'))[-1]['pag']+1; continue
        if t==1 and os.path.exists(f'{O}/D1.mkv'):
            st,pl=B.stati_topic(1,p); p=pl+1
            json.dump([dict(t=s['t'],pag=s['pag'],att=s['att'],si=s['si'],img=s['img'],orig=s['orig']) for s in st],open(f'{O}/D1_stati.json','w'),indent=1); open(f'{O}/D1.ok','w').close()
            print('D1 già fatto, pagina finale',pl,flush=True); continue
        d,pl=B.build(t,p,O); open(f'{O}/D{t}.ok','w').close(); print('D%d'%t,d,pl,flush=True); p=pl+1
open(f'{O}/prof.fatto','w').close()
