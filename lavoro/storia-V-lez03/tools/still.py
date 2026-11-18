# anteprima di un fotogramma di una scheda blu (usa lo stesso JS di schede_spagnolo.py)
import sys,json,os
sys.path.insert(0,'/tmp/w/tools')
import schede_spagnolo as S
from playwright.sync_api import sync_playwright
def stills(jobs):
    """jobs: list of (spec,t,outpng)"""
    out='/tmp/w/build/_still';os.makedirs(out,exist_ok=True)
    open(out+'/p.html','w').write('<!doctype html><meta charset=utf-8><style>%s</style><body>%s'%(S.CSS,S.BODY))
    with sync_playwright() as p:
        b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium',args=['--allow-file-access-from-files','--no-sandbox'])
        pg=b.new_page(viewport={'width':1920,'height':1080},device_scale_factor=1.0)
        for spec,t,png in jobs:
            pg.goto('file://'+out+'/p.html');pg.evaluate("document.fonts.ready");pg.add_script_tag(content=S.JS)
            pg.evaluate("(s)=>init(s)",spec);pg.evaluate("([t,f])=>draw(t,f)",[t,int(t*30)]);pg.screenshot(path=png)
        b.close()
if __name__=='__main__':
    stills([(json.loads(sys.argv[1]),float(sys.argv[2]),sys.argv[3])])
