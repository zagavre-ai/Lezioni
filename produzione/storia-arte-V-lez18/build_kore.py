import sys; sys.path.insert(0,'/home/user/w18')
import build, kore, traceback
S=build.sequenza(); kore.FADE.update(build.colori(S))
for n,ty,fn in S:
    if fn is None or n.startswith('prof_'): continue
    try: print('ok',n,fn(),flush=True)
    except Exception: print('ERR',n,traceback.format_exc()[-500:],flush=True)
print('fatto',flush=True)
