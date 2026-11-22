import json,subprocess
from gfx import *; from lessondata import *
a=ARGS[1]
open('html/t1.html','w').write(slide(f"02 · {a['nome']}",a['tit'],a['cards'][:3],1,7,a['kw']))
open('html/t2.html','w').write(slide(f"02 · {a['nome']}",a['tit'],[a['cards'][1],a['cards'][3]],0,8,a['kw']))
open('html/t3.html','w').write(cover(["Gli anni Sessanta","tra crisi e progressi"],[x['nome'] for x in ARGS],True))
json.dump([{'html':f'{B}/html/t{i}.html','out':f'{B}/png/t{i}.png'} for i in (1,2,3)],open('jobs.json','w'))
