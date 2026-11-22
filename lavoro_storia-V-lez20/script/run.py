import sys,os,json,subprocess,time
sys.path.insert(0,'/tmp/w/b')
import plan
from plan import *
part=int(sys.argv[1])
P,reg=(plan.build_part1() if part==1 else plan.build_part2())
render_many(ST.JOBS)
os.makedirs(f'/tmp/w/b/pp{part}',exist_ok=True)
files=[];t0=time.time()
for i,p in enumerate(P):
    nxt=P[i+1] if i+1<len(P) else None
    out=f'/tmp/w/b/pp{part}/{i:03d}_{p.name}.mp4'
    if not os.path.exists(out+'.ok'):
        if os.path.exists(out): os.remove(out)
        mux(p,nxt,out,crf=(22 if p.cam else 19))
        open(out+'.ok','w').write('1')
    files.append(out);print(i,p.name,round(p.total,2),round(time.time()-t0),flush=True)
# timeline
tl=[];t=0.0
for p in P:
    n=p.name
    if n[0]=='A' and n[1].isdigit(): n='D'+n
    tl.append([n,round(t,3),round(p.total,3)]);t+=p.total
json.dump(tl,open(f'/tmp/w/b/timeline_P{part}.json','w'))
open(f'/tmp/w/b/list_P{part}.txt','w').write(''.join(f"file '{f}'\n" for f in files))
json.dump(dict(PROV=plan.PROV,pages={str(k):v for k,v in reg.d.items()}),open(f'/tmp/w/b/meta_P{part}.json','w'),default=str)
print('TOTALE',round(t,1),'s =',round(t/60,2),'min')
