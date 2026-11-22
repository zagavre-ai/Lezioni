import sys;sys.path.insert(0,'/tmp/w/b')
from prof import *
from content import CHUNKS
import json,os
def ix(t): return min(range(len(S)),key=lambda i:abs(S[i]['fine']-t))
def ixs(t): return min(range(len(S)),key=lambda i:abs(S[i]['inizio']-t))
meta={}
for n,c in CHUNKS.items():
    i0,i1=ixs(c['a']),ix(c['b'])
    if os.path.exists(f'/tmp/w/b/ch/{n}.ok'):
        iv=intervals(i0,i1);f,d=mapper(iv);meta[n]=dict(i0=i0,i1=i1,dur=d,iv=iv);continue
    d,f,iv=build_chunk(n,i0,i1,'/tmp/w/b/ch')
    open(f'/tmp/w/b/ch/{n}.ok','w').write('1')
    meta[n]=dict(i0=i0,i1=i1,dur=d,iv=iv);print(n,i0,i1,round(d,1),len(iv),flush=True)
json.dump(meta,open('/tmp/w/b/ch/meta.json','w'))
print('FATTO')
