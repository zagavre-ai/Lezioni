# Grafica comune: pagine HTML 1920x1080 -> PNG (Chromium). Modello Spagnolo: fondo bianco, blu notte #0B1530, blu Telesio #2060AF, giallo #FFE600.
import glob,base64,os
from playwright.sync_api import sync_playwright
CH=glob.glob('/opt/pw-browsers/chromium-*/chrome-linux64/chrome')[0]
FONT=""
LOGO=open('/home/user/Lezioni/kit/docenti/Telesio_logo_blu.svg').read()
class B:
    def __enter__(s):
        s.p=sync_playwright().start();s.b=s.p.chromium.launch(executable_path=CH,args=['--no-sandbox'])
        s.pg=s.b.new_page(viewport={'width':1920,'height':1080});return s
    def __exit__(s,*a):s.b.close();s.p.stop()
    def shot(s,html,out,transparent=False):
        open('/tmp/pagina.html','w').write('<!doctype html><html><head><meta charset=utf-8><style>'+FONT+BASE+'</style></head><body>'+html+'</body></html>')
        s.pg.goto('file:///tmp/pagina.html')
        s.pg.wait_for_timeout(150)
        s.pg.screenshot(path=out,omit_background=transparent)
BASE="""
html,body{margin:0;width:1920px;height:1080px;background:#fff;overflow:hidden;font-family:Figtree;color:#0B1530}
.abs{position:absolute}
"""
def chrome(materia,pagina,kicker=None):
    """cornice: logo, filetto, kicker, piè di pagina (materia, senza nome del docente)"""
    k=f'<div class="abs" style="left:80px;top:146px;font:700 24px Figtree;letter-spacing:.16em;color:#2060AF">{kicker}</div>' if kicker else ''
    return (f'<div class="abs" style="left:80px;top:48px;width:170px">{LOGO}</div>'
            '<div class="abs" style="left:80px;right:80px;top:124px;height:1px;background:#D5DCE8"></div>'+k+
            '<div class="abs" style="left:80px;right:80px;top:980px;height:1px;background:#D5DCE8"></div>'
            f'<div class="abs" style="left:80px;top:1000px;font:700 22px Figtree;letter-spacing:.14em;color:#2060AF">{materia}</div>'
            f'<div class="abs" style="right:80px;top:1000px;font:700 22px Figtree;letter-spacing:.1em;color:#2060AF">Pagina {pagina}</div>')
