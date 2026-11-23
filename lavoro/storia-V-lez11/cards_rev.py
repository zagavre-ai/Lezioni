import sys,os,json
sys.path.insert(0,'/home/user/work/build')
src=open('/home/user/work/build/cards.py').read().split("for nm,sp in specs:")[0]
exec(src)
for nm,sp in reversed(specs):
    if nm in ('VERIFICA','Q6','Q5','P4','Q4'):
        if os.path.exists(f'{B}/cards/{nm}.ok'): continue
        if os.path.exists(f'{B}/cards/{nm}'): continue   # già in lavorazione dall'altro processo
        schede.render(sp,f'{B}/cards/{nm}',1.0);open(f'{B}/cards/{nm}.ok','w').write('1');print(nm,flush=True)
