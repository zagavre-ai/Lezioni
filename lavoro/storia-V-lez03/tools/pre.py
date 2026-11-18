import sys;sys.path.insert(0,'/tmp/w/tools')
import plan
_orig=plan.vdur
def fake(n):
    try: return _orig(n)
    except Exception: return 8.0
plan.vdur=fake
import plan2;plan2.vdur=fake
import parts;parts.vdur=fake
from parts import *
import render_req,build
P1=part1();P2=part2()
render_req.render_all()
dep=lambda s: s['id'].startswith(('map','cover_ben','p0','p1')) and s['k']!='prof' and not s['id'].startswith('prof')
import json
jobs=[]
for part,segs in (('P1',P1),('P2',P2)):
    for i,s in enumerate(segs):
        if dep(s) or s['k']=='card' and not os.path.exists(s['mp4']): continue
        jobs+=build.pieces(part,i,s)
print(len(jobs),'pezzi')
from multiprocessing import Pool
with Pool(3) as p: list(p.imap_unordered(build.do,jobs))
print('fatto')
