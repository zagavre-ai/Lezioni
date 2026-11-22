import sys,os,json,re;sys.path.insert(0,'/home/user/Lezioni/lez14')
import schede as S
S.PARTE[9]=[1,2,3,4,5,6,7]
body=S.cover_page(9,False).replace('STORIA V · VIDEOLEZIONE · PARTE 9','STORIA V · MAPPE · VIDEOLEZIONE')
body=body.replace('<div id=avv>','<div style="position:absolute;right:80px;top:150px;font:800 110px Bri;color:#2060AF;letter-spacing:.04em">MAPPE</div><div id=avv>',1)
body=body.replace('<div id=arg>','<style>#arg{width:1700px!important;column-count:2;column-gap:60px;max-height:520px}.ar{break-inside:avoid;margin:0 0 12px!important}</style><div id=arg>',1)
hp=f'{S.WK}/html/COVER_MAPPE.html';open(hp,'w').write(S.pagina(None,body,extra_css=S.COVER_CSS))
out='/tmp/w/disp/cover_mappe.png'
if os.path.exists(out):os.remove(out)
jp=f'{S.WK}/jobs_cover_mappe.json'
json.dump([{'html':hp,'transparent':False,'frames':[{'t':0,'out':out}]}],open(jp,'w'))
S.sh(['node',S.HERE+'/shot2.js',jp],env={**os.environ,'NODE_PATH':'/opt/node-tools/node_modules'},cwd=S.HERE)
