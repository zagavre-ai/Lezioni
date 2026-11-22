# Modelli grafici (HTML) · fondo bianco, blu notte #0B1530, blu Telesio #2060AF, giallo #FFE600
import html, re, base64
from lib import CSS, shot, measure, W, H
LOGO_B = open('/home/user/Lezioni/kit/docenti/Telesio_logo_blu.svg').read()
LOGO_W = LOGO_B.replace('#2060AF', '#FFFFFF')
MATERIA = 'STORIA V'
esc = html.escape

def b64img(p):
    ext = p.rsplit('.', 1)[-1].lower(); mt = 'image/png' if ext == 'png' else 'image/jpeg'
    return f'data:{mt};base64,' + base64.b64encode(open(p, 'rb').read()).decode()

def card_inner(text):
    """«Titoletto: resto» -> il titoletto in grassetto"""
    m = re.match(r'^([^:]{3,80}):\s+(.*)$', text, re.S)
    if m: return f'<b>{esc(m.group(1))}</b>: {esc(m.group(2))}'
    return esc(text)

BASE = CSS + '''
.logo{position:absolute;left:80px;top:46px;width:178px;height:56px}
.logo svg{width:178px;height:56px}
.rule{position:absolute;left:80px;right:80px;top:124px;height:2px;background:#E2E8F0}
.foot{position:absolute;left:80px;right:80px;top:980px;height:2px;background:#E2E8F0}
.fl{position:absolute;left:80px;top:1004px;font:700 24px Fig;letter-spacing:.14em;color:#2060AF}
.fr{position:absolute;right:80px;top:1004px;font:700 24px Fig;letter-spacing:.14em;color:#2060AF}
.lab{position:absolute;left:80px;top:146px;font:700 24px Fig;letter-spacing:.14em;color:#2060AF;text-transform:uppercase}
.tit{position:absolute;left:80px;top:182px;width:1290px;font:800 60px/1.08 Bri;color:#2060AF}
.tit:after{content:"";display:block;width:84px;height:7px;border-radius:4px;background:#2060AF;margin-top:14px}
.cards{position:absolute;left:80px;width:1306px}
.card{position:relative;border:3px solid #D5DEEC;border-radius:20px;background:#fff;padding:18px 30px 18px 54px;font:500 40px/1.5 Fig;color:#0B1530;
  box-shadow:0 10px 26px rgba(70,85,110,.13);margin-bottom:18px;opacity:.5}
.card b{font-weight:800}
.card.on{opacity:1;border:6px solid #FFE600;padding:15px 27px 15px 51px;background:#FFFEF3;box-shadow:0 12px 30px rgba(70,85,110,.2)}
.card .dot{position:absolute;left:20px;top:34px;width:18px;height:18px;border-radius:50%;background:#C9D3E3}
.card.on .dot{background:#FFE600;box-shadow:0 0 0 3px #0B1530}
.sig{display:block;font:600 30px/1.35 Fig;color:#2060AF;margin-top:6px}
.band{position:absolute;left:1428px;top:476px;width:412px;transform:rotate(-2.2deg);background:#FFE600;border-radius:12px;padding:16px 24px 14px;
  box-shadow:0 10px 22px rgba(60,70,90,.25)}
.band .n{font:800 36px/1.1 Bri;color:#0B1530}
.band .m{font:800 21px/1.2 Fig;letter-spacing:.06em;color:#0B1530;margin-top:6px}
.camshadow{position:absolute;left:1428px;top:148px;width:412px;height:309px;border-radius:22px;background:#E7EBF2;box-shadow:0 14px 34px rgba(60,70,90,.30)}
.pc{position:absolute;left:1428px;top:620px;width:412px}
.pc h4{margin:0 0 12px;font:700 22px Fig;letter-spacing:.14em;color:#2060AF}
.pc span{display:inline-block;margin:0 10px 10px 0;padding:7px 16px;border-radius:999px;background:#EEF3FB;border:2px solid #C7D5EC;font:700 26px Fig;color:#0B1530}
'''

def frame(label, title, body, page, cam=True, kw=None, name='Giorgio Mazzotti', mat='PROF. DI STORIA', foot=True):
    pc = ''
    if kw:
        pc = '<div class="pc"><h4>PAROLE CHIAVE</h4>' + ''.join(f'<span>{esc(k)}</span>' for k in kw[:5]) + '</div>'
    camh = f'<div class="camshadow"></div><div class="band"><div class="n">{esc(name)}</div><div class="m">{esc(mat)}</div></div>' if cam else ''
    pg = f'<div class="fr">Pagina {page}</div>' if page else ''
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{BASE}</style></head><body>' \
           f'<div class="logo">{LOGO_B}</div><div class="rule"></div><div class="lab">{esc(label)}</div><div class="tit">{title}</div>' \
           f'{body}{camh}{pc}<div class="foot"></div><div class="fl">{MATERIA}</div>{pg}</body></html>'

def cards_html(cards, lit, top):
    """cards: lista di (testo, sigla_nota o None); lit: indice acceso o None"""
    out = f'<div class="cards" style="top:{top}px">'
    for i, c in enumerate(cards):
        t, s = (c if isinstance(c, (tuple, list)) else (c, None))
        cls = 'card on' if i == lit else 'card'
        out += f'<div class="{cls}"><span class="dot"></span>{card_inner(t)}' + (f'<span class="sig">{esc(s)}</span>' if s else '') + '</div>'
    return out + '</div>'

_tb = {}
def cards_top(label, title):
    if title not in _tb:
        h = frame(label, title, '', 0)
        _tb[title] = int(measure(h, "document.querySelector('.tit').getBoundingClientRect().bottom")) + 22
    return _tb[title]
def slide_html(label, title, cards, lit, page, kw=None, cam=True):
    return frame(label, title, cards_html(cards, lit, cards_top(label, title)), page, cam=cam, kw=kw)

def height_of(label, title, cards):
    """altezza totale delle card (px) misurata"""
    h = frame(label, title, cards_html(cards, None, cards_top(label, title)), 0)
    return measure(h, "(()=>{const c=document.querySelector('.cards');const r=c.getBoundingClientRect();return [r.top, r.bottom]})()")

def image_slide_html(label, title, img, caption, page, kw=None, cam=True):
    body = f'<div style="position:absolute;left:80px;top:300px;width:1306px;height:640px;display:flex;gap:40px;align-items:center;justify-content:center">' \
           f'<div style="border:3px solid #D5DEEC;border-radius:20px;padding:14px;background:#fff;box-shadow:0 10px 26px rgba(70,85,110,.13)"><img src="{b64img(img)}" style="display:block;max-height:560px;max-width:760px;border-radius:10px"></div>' \
           f'<div style="flex:1;font:500 36px/1.45 Fig;color:#0B1530">{caption}</div></div>'
    return frame(label, title, body, page, cam=cam, kw=kw)

# ---------- schede animate in blu scuro ----------
DARK = CSS + '''
html,body{background:#0B1530}
.dk{position:absolute;inset:0;background:radial-gradient(1200px 700px at 20% 30%,#1B3A7A 0%,rgba(27,58,122,0) 60%),radial-gradient(900px 700px at 85% 80%,#14306A 0%,rgba(20,48,106,0) 60%),#0B1530}
.dl{position:absolute;left:120px;top:150px;font:700 30px Fig;letter-spacing:.18em;color:#FFE600;text-transform:uppercase}
.dt{position:absolute;left:120px;top:210px;width:1500px;font:800 92px/1.08 Bri;color:#fff}
.ds{position:absolute;left:120px;width:1500px;font:600 44px/1.4 Fig;color:#DCE6F7}
.dlogo{position:absolute;right:100px;bottom:70px;width:300px;height:95px}.dlogo svg{width:300px;height:95px}
.dfoot{position:absolute;left:120px;bottom:70px;font:700 24px Fig;letter-spacing:.14em;color:#9FB6E0}
.bar{position:absolute;left:120px;top:390px;width:140px;height:9px;border-radius:5px;background:#FFE600}
'''
def dark_html(label, title, sub=None, items=None):
    s = ''
    if sub: s += f'<div class="ds" style="top:430px">{esc(sub)}</div>'
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{DARK}</style></head><body><div class="dk"></div>' \
           f'<div class="dl">{esc(label)}</div><div class="dt">{title}</div><div class="bar"></div>{s}' \
           f'<div class="dfoot">{MATERIA}</div><div class="dlogo">{LOGO_W}</div></body></html>'
