import sys, os, time
sys.path.insert(0,'/tmp/w/build')
import pieces as P
for nm in sys.argv[1:]:
    ok=f'/tmp/w/build/pieces/{nm}.ok'
    if os.path.exists(ok): continue
    t=time.time()
    if nm.startswith('INTRO'): P.build_intro(nm[-1])
    else: P.build_teacher(nm)
    open(ok,'w').write('1'); print(nm,'fatto in',round(time.time()-t),'s',flush=True)
