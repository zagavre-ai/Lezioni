import sys,time;sys.path.insert(0,'/home/claude/w/code')
from lesson import *
r=R();ctx=Ctx(9,r)
t0=time.time()
build_arg(ctx,ARG[4],quiz_think=9.0)
print('clips',[(c['label'][:30],round(c['dur'],1)) for c in ctx.clips],time.time()-t0,flush=True)
m=build_master(ctx,'test5');print(m,dur(m))
r.close()
