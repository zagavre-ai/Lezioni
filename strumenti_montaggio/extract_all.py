import sys;sys.path.insert(0,'/home/claude/w/code')
from profpieces import *
for a in ARG:
    B=snap(build(a));extract_arg(f"a{a['n']}",B);print(a['n'],round(B['dur']),flush=True)
# intro
class A0:pass
a0=dict(segs=[(0,17)])
B=snap(build(a0));extract_arg('a0',B);print('intro',round(B['dur']))
