# Grafica Telesio per le slide (1920x1080). Render con Playwright. Modello: Spagnolo lez01.
import os,re,json,html
from playwright.sync_api import sync_playwright
HERE=os.path.dirname(os.path.abspath(__file__))
LOGO=open(HERE+'/Telesio_logo_blu.svg').read()
CSS='''
@font-face{font-family:Fig;font-weight:400;src:url(file:///root/.fonts/Figtree-Regular.ttf)}
@font-face{font-family:Fig;font-weight:500;src:url(file:///root/.fonts/Figtree-Medium.ttf)}
@font-face{font-family:Fig;font-weight:600;src:url(file:///root/.fonts/Figtree-SemiBold.ttf)}
@font-face{font-family:Fig;font-weight:700;src:url(file:///root/.fonts/Figtree-Bold.ttf)}
@font-face{font-family:Fig;font-weight:800;src:url(file:///root/.fonts/Figtree-ExtraBold.ttf)}
@font-face{font-family:Bri;font-weight:800;src:url(file:///root/.fonts/BricolageGrotesque-ExtraBold.ttf)}
*{box-sizing:border-box}
html,body{margin:0;width:1920px;height:1080px;background:#fff;overflow:hidden;font-family:Fig;color:#0B1530}
#logo{position:absolute;left:80px;top:46px;width:170px}
#logo svg{width:170px;height:auto}
#hl{position:absolute;left:80px;right:80px;top:124px;height:1px;background:#D9DEE8}
#fl{position:absolute;left:80px;right:80px;top:981px;height:1px;background:#D9DEE8}
#foot{position:absolute;left:80px;top:998px;font:700 20px Fig;letter-spacing:.12em;color:#2060AF}
#pag{position:absolute;right:80px;top:998px;font:700 20px Fig;letter-spacing:.1em;color:#2060AF}
#kick{position:absolute;left:80px;top:146px;font:800 22px Fig;letter-spacing:.14em;color:#2060AF}
#tit{position:absolute;left:80px;top:182px;width:1290px;font:800 58px/1.08 Bri;color:#0B1530}
#bar{position:absolute;left:80px;width:85px;height:6px;background:#2060AF;border-radius:3px}
#cam{position:absolute;left:1428px;top:148px;width:412px;height:309px;border-radius:16px;background:#E8ECF3;box-shadow:0 18px 40px rgba(60,72,100,.28)}
#tag{position:absolute;left:1428px;top:470px;width:416px;padding:18px 26px 16px;background:#FFE600;transform:rotate(-1.6deg);border-radius:8px;box-shadow:0 10px 24px rgba(60,72,100,.22)}
#tag b{display:block;font:800 31px/1.1 Bri;color:#0B1530}
#tag span{display:block;margin-top:5px;font:800 20px Fig;letter-spacing:.04em;color:#0B1530}
#kw{position:absolute;left:1428px;top:640px;width:412px}
#kw h4{margin:0 0 10px;font:800 18px Fig;letter-spacing:.14em;color:#2060AF}
#kw div{display:inline-block;margin:0 8px 8px 0;padding:6px 14px;border-radius:999px;background:#EAF1FB;border:2px solid #C9DAF2;font:700 22px Fig;color:#0B1530}
.card{position:relative;width:1290px;padding:18px 64px 18px 96px;border-radius:20px;background:#fff;border:3px solid #DDE3EE;box-shadow:0 10px 26px rgba(60,72,100,.12);font:500 40px/1.4 Fig;color:#0B1530}
.card b{font-weight:800}
.card.dim{opacity:.5}
.card.on{border:6px solid #FFE600;background:#FFFBE0;box-shadow:0 14px 30px rgba(60,72,100,.18);padding:16px 62px 16px 94px}
.card .n{position:absolute;left:26px;top:20px;width:46px;height:46px;border-radius:50%;background:#2060AF;color:#fff;font:800 26px/46px Fig;text-align:center}
.card.on .n{background:#FFE600;color:#0B1530}
.card.on::after{content:"";position:absolute;right:22px;top:22px;width:20px;height:20px;border-radius:50%;background:#FFE600;border:3px solid #0B1530}
.sig{position:relative;margin-top:20px;width:1290px;padding:10px 22px;border-radius:14px;background:#EAF1FB;font:600 26px/1.35 Fig;color:#0B1530}
.sig b{font-weight:800}
.img{position:absolute;border-radius:16px;box-shadow:0 14px 34px rgba(60,72,100,.25);object-fit:contain;background:#fff}
.cap{position:absolute;font:600 28px/1.35 Fig;color:#0B1530}
'''
def esc(s):
    s=re.sub(r'"([^"]+)"',r'“\1”',s);return html.escape(s,quote=False)
def card_html(t):
    m=re.match(r'^([^:]{3,70}?):\s*(.*)$',t)
    if m and not m.group(1).strip().endswith(')') or (m and '(' in m.group(1)):
        return '<b>'+esc(m.group(1))+':</b> '+esc(m.group(2))
    return esc(t)
def pagina(title,cards,on,sigle=None):
    """restituisce (inner_html, bar_top, fondo_y) ; cards: testi, on: indice acceso o None"""
    nl=1 if len(title)<40 else 2
    th=int(58*1.08*nl);bar=182+th+14;y=bar+36
    body=''
    for i,c in enumerate(cards):
        cls='card '+('on' if on==i else ('dim' if on is not None else ''))
        body+=f'<div class="{cls}"><span class=n>{i+1}</span>{card_html(c)}</div>'
    sg=''
    if sigle:sg='<div class="sig">'+' · '.join(f'<b>{esc(a)}</b> = {esc(b)}' for a,b in sigle)+'</div>'
    return f'<div id="cards" style="position:absolute;left:80px;top:{y}px;width:1290px;display:flex;flex-direction:column;gap:22px">{body}{sg}</div>',bar
def doc(inner,kicker='',title='',bar=0,pag=1,cam=True,kw=None,foot='STORIA V',nome='Giorgio Mazzotti',mat='PROF. DI STORIA',extra=''):
    k=''.join(f'<div>{esc(x)}</div>' for x in (kw or []))
    camh=f'<div id="cam"></div><div id="tag"><b>{esc(nome)}</b><span>{esc(mat)}</span></div>' if cam else ''
    kwh=f'<div id="kw"><h4>PAROLE CHIAVE</h4>{k}</div>' if (cam and kw) else ''
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div id="logo">{LOGO}</div><div id="hl"></div><div id="fl"></div>
<div id="kick">{esc(kicker)}</div><div id="tit">{esc(title)}</div>{('<div id="bar" style="top:%dpx"></div>'%bar) if bar else ''}
{inner}{camh}{kwh}<div id="foot">{esc(foot)}</div><div id="pag">Pagina {pag}</div>{extra}</body></html>'''
class R:
    def __enter__(self):
        self.p=sync_playwright().start();self.b=self.p.chromium.launch(executable_path='/opt/pw-browsers/chromium',args=['--no-sandbox']);self.pg=self.b.new_page(viewport={'width':1920,'height':1080});return self
    def __exit__(self,*a):self.b.close();self.p.stop()
    def set(self,h):
        fp=f'/tmp/claude-0/_r{os.getpid()}.html';open(fp,'w').write(h);self.pg.goto('file://'+fp);self.pg.evaluate("document.fonts.ready");self.pg.wait_for_timeout(80)
    def shot(self,h,path):
        self.set(h);self.pg.screenshot(path=path)
    def heights(self,h):
        self.set(h);return self.pg.evaluate("(()=>{const r=document.getElementById('cards').getBoundingClientRect();return r.bottom})()")
