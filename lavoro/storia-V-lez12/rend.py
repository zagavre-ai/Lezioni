# -*- coding: utf-8 -*-
# Disegno delle schermate (HTML -> PNG con Chromium). Modello grafico: Spagnolo lez01.
import os, html, json
from playwright.sync_api import sync_playwright
KIT = '/home/user/Lezioni/kit'
WORK = '/home/user/w12'
LOGO = f'{KIT}/docenti/Telesio_logo_blu.svg'
BLU, NOTTE, GIALLO = '#2060AF', '#0B1530', '#FFE600'
_p = None; _b = None; _pg = None

def pagina():
    global _p, _b, _pg
    if _pg is None:
        _p = sync_playwright().start()
        _b = _p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
        _pg = _b.new_page(viewport={'width': 1920, 'height': 1080})
    return _pg

def chiudi():
    global _p, _b, _pg
    if _b: _b.close(); _p.stop(); _b = _p = _pg = None

def esc(t): return html.escape(t, quote=False)

CSS = f"""
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1920px;height:1080px;overflow:hidden}}
body{{background:#fff;font-family:'Figtree',sans-serif;color:{NOTTE};position:relative}}
.abs{{position:absolute}}
.logo{{position:absolute;left:80px;top:48px;height:62px}}
.hr{{position:absolute;left:80px;width:1760px;height:1px;background:#dfe3ea}}
.lab{{position:absolute;left:80px;top:150px;font:700 26px 'Figtree';letter-spacing:3px;color:{BLU};text-transform:uppercase}}
.tit{{position:absolute;left:80px;top:182px;width:1300px;font:800 60px/1.08 'Bricolage Grotesque';color:{NOTTE}}}
.foot{{position:absolute;left:80px;right:80px;top:1000px;font:700 24px 'Figtree';letter-spacing:2px;color:{BLU};display:flex;justify-content:space-between}}
.card{{position:absolute;left:80px;width:1305px;background:#fff;border:3px solid #dfe3ea;border-radius:22px;padding:10px 28px 12px 96px;box-shadow:0 10px 30px rgba(40,50,80,.10)}}
.card .n{{position:absolute;left:26px;top:14px;width:48px;height:48px;border-radius:50%;background:#fff;border:3px solid {NOTTE};color:{NOTTE};font:800 30px/42px 'Figtree';text-align:center}}
.card .t{{font:700 30px/1.25 'Figtree';color:{BLU};letter-spacing:.5px;margin-bottom:0}}
.card .s{{font:500 40px/1.45 'Figtree';color:{NOTTE}}}
.card.off{{opacity:.55}}
.card.on{{border-color:{GIALLO};border-width:6px;background:#FFFBD6;box-shadow:0 12px 34px rgba(40,50,80,.18)}}
.card.on .n{{background:#fff;color:{NOTTE}}}
.card .dot{{display:none}}
.card.on .dot{{display:block;position:absolute;right:26px;top:26px;width:22px;height:22px;border-radius:50%;background:{GIALLO};border:3px solid {NOTTE}}}
.ombra{{position:absolute;left:1428px;top:148px;width:412px;height:309px;border-radius:14px;background:#e9edf3;box-shadow:0 14px 34px rgba(60,70,90,.30)}}
.band{{position:absolute;left:1428px;top:468px;width:412px;height:104px;background:{GIALLO};transform:rotate(-2deg);box-shadow:0 10px 24px rgba(60,70,90,.28);padding:18px 22px}}
.band .a{{font:800 36px/1.1 'Bricolage Grotesque';color:{NOTTE}}}
.band .b{{font:700 22px/1.4 'Figtree';letter-spacing:1px;color:{NOTTE};margin-top:6px}}
.kw{{position:absolute;left:1428px;top:620px;width:412px}}
.kw .h{{font:700 22px 'Figtree';letter-spacing:3px;color:{BLU};margin-bottom:12px}}
.kw .c{{font:700 28px/1 'Figtree';background:#EEF3FB;border-left:8px solid {BLU};border-radius:10px;padding:11px 16px;margin-bottom:10px;color:{NOTTE}}}
.fig{{position:absolute;background:#fff;border:3px solid #dfe3ea;border-radius:22px;box-shadow:0 10px 30px rgba(40,50,80,.10);display:flex;align-items:center;justify-content:center;overflow:hidden}}
.fig img{{max-width:100%;max-height:100%}}
.cap{{position:absolute;font:600 30px/1.3 'Figtree';color:{NOTTE}}}
"""

def telaio(label, titolo, pagina_n, materia='STORIA', con_prof=True, parole=None, nome=('Giorgio Mazzotti', 'PROF. DI STORIA')):
    h = f'<img class="logo" src="file://{LOGO}"><div class="hr" style="top:125px"></div>'
    h += f'<div class="lab">{esc(label)}</div><div class="tit">{esc(titolo)}</div>'
    h += f'<div class="hr" style="top:981px"></div><div class="foot"><span>{materia}</span><span>Pagina {pagina_n}</span></div>'
    if con_prof:
        h += '<div class="ombra"></div>'
        h += f'<div class="band"><div class="a">{esc(nome[0])}</div><div class="b">{esc(nome[1])}</div></div>'
    if parole:
        h += '<div class="kw"><div class="h">PAROLE CHIAVE</div>' + ''.join(f'<div class="c">{esc(p)}</div>' for p in parole[:5]) + '</div>'
    return h

def doc(body, extra_css=''):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{extra_css}</style></head><body>{body}</body></html>'

def cap(s):  # prima lettera maiuscola (la card comincia sempre con la maiuscola)
    return s[:1].upper() + s[1:]

def card_html(i, titolo, testo, top, stato):
    cls = {'on': 'on', 'off': 'off', 'norm': ''}[stato]
    t = f'<div class="t">{esc(titolo)}</div>' if titolo else ''
    return (f'<div class="card {cls}" style="top:{top}px"><div class="n">{i}</div><div class="dot"></div>{t}'
            f'<div class="s">{esc(cap(testo))}</div></div>')

def png(html_str, out, transparent=False, name='_tmp.html'):
    pg = pagina()
    f = f'{WORK}/_html{os.getpid()}/{name}'; os.makedirs(os.path.dirname(f), exist_ok=True)
    open(f, 'w', encoding='utf8').write(html_str)
    pg.goto('file://' + f); pg.wait_for_timeout(60)
    pg.evaluate('document.fonts.ready')
    pg.screenshot(path=out, omit_background=transparent)
    return out

def misura_card(titolo, testo, larghezza=1305, font=40):
    """altezza di una card (px) misurata nel browser"""
    pg = pagina()
    f = f'{WORK}/_html{os.getpid()}/_m.html'; os.makedirs(os.path.dirname(f), exist_ok=True)
    open(f, 'w', encoding='utf8').write(doc(card_html(1, titolo, testo, 0, 'norm').replace('class="card ', 'id="c" class="card ')))
    pg.goto('file://' + f)
    return pg.evaluate('document.getElementById("c").offsetHeight')

DARK_CSS = f"""
body.dark{{background:linear-gradient(135deg,#071027 0%,#0B1E4A 55%,#12336E 100%);color:#fff}}
.dlogo{{position:absolute;left:80px;top:48px;height:62px;filter:brightness(0) invert(1)}}
.d-lab{{font:700 28px 'Figtree';letter-spacing:5px;color:{GIALLO};text-transform:uppercase}}
.d-tit{{font:800 84px/1.06 'Bricolage Grotesque';color:#fff}}
.d-line{{font:600 44px/1.35 'Figtree';color:#fff}}
"""

def elem(inner, out, estile='', dark=True, extra_css=''):
    """PNG trasparente di un elemento (id=e) posizionato in alto a sinistra; ritorna (w,h)"""
    pg = pagina()
    f = f'{WORK}/_html{os.getpid()}/_e.html'; os.makedirs(os.path.dirname(f), exist_ok=True)
    open(f, 'w', encoding='utf8').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{DARK_CSS}{extra_css} body{{background:transparent!important;width:1920px;height:1080px}}</style></head><body><div id="e" style="position:absolute;left:0;top:0;{estile}">{inner}</div></body></html>')
    pg.goto('file://' + f); pg.wait_for_timeout(50)
    el = pg.query_selector('#e'); bb = el.bounding_box()
    el.screenshot(path=out, omit_background=True)
    return int(round(bb['width'])), int(round(bb['height']))

def base_dark(out):
    body = f'<img class="dlogo" src="file://{LOGO}">'
    return png(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{DARK_CSS}</style></head><body class="dark">{body}</body></html>', out, name='dark.html')

def luce(out):
    from PIL import Image, ImageDraw, ImageFilter
    im = Image.new('RGBA', (1400, 1400), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.ellipse((300, 300, 1100, 1100), fill=(70, 120, 220, 70)); im = im.filter(ImageFilter.GaussianBlur(160)); im.save(out)
