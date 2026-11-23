# Generatore delle schermate 1920x1080 (modello Spagnolo/Storia V): slide bianche, schede blu, mappe BES.
import os, glob, html, json
from playwright.sync_api import sync_playwright
MAT = "STORIA DELL'ARTE V"
LOGO = '/home/user/Lezioni/kit/docenti/Telesio_logo_blu.svg'
EXE = glob.glob('/opt/pw-browsers/chromium-*/chrome-linux*/chrome')[0]
CSS = """
html,body{margin:0;width:1920px;height:1080px;overflow:hidden}
*{box-sizing:border-box}
body{font-family:'Figtree';color:#0B1530;background:%BG%}
.logo{position:absolute;left:80px;top:50px;height:54px}
.hl0{position:absolute;left:80px;right:80px;top:124px;height:1px;background:#E2E8F0}
.eb{position:absolute;left:80px;top:146px;font:700 26px 'Figtree';letter-spacing:.14em;color:#2060AF;text-transform:uppercase}
.ti{position:absolute;left:80px;top:196px;width:1300px;font:800 66px/1.08 'Bricolage Grotesque';color:#0B1530}
.bar{position:absolute;left:80px;width:85px;height:6px;border-radius:3px;background:#2060AF}
.ft{position:absolute;left:80px;right:80px;bottom:0;height:99px;border-top:1px solid #E2E8F0}
.ft b{position:absolute;top:20px;font:700 22px 'Figtree';letter-spacing:.12em;color:#2060AF}
.card{position:absolute;left:80px;width:1305px;background:#F5F8FD;border:3px solid #DCE4F0;border-radius:20px;padding:18px 30px;font:400 40px/1.5 'Figtree';color:#0B1530;box-shadow:0 8px 26px rgba(11,21,48,.08)}
.card b{font-weight:800}
.card.dim{opacity:.55}
.card.act{border:6px solid #FFE600;background:#FFFEF2;box-shadow:0 0 0 2px #FFE600,0 10px 28px rgba(11,21,48,.16);padding:15px 27px}
.card.act:before{content:'';position:absolute;left:-14px;top:50%;margin-top:-13px;width:26px;height:26px;border-radius:50%;background:#FFE600;border:3px solid #0B1530}
.cam{position:absolute;left:1428px;top:148px;width:412px;height:309px;border-radius:18px;background:#EEF2F8;box-shadow:0 14px 34px rgba(11,21,48,.22)}
.fascia{position:absolute;left:1428px;top:470px;width:412px;height:104px;background:#FFE600;transform:rotate(-3deg);box-shadow:0 10px 22px rgba(11,21,48,.2);padding:16px 22px}
.fascia .n{font:800 34px 'Bricolage Grotesque';color:#0B1530;line-height:1.1}
.fascia .m{font:700 19px 'Figtree';letter-spacing:.06em;color:#0B1530;margin-top:8px}
.kw{position:absolute;left:1428px;top:640px;width:412px;background:#F5F8FD;border:3px solid #DCE4F0;border-radius:18px;padding:16px 22px}
.kw h4{margin:0 0 8px;font:700 18px 'Figtree';letter-spacing:.14em;color:#2060AF}
.kw div{font:600 26px/1.35 'Figtree';color:#0B1530}
.kw div:before{content:'';display:inline-block;width:10px;height:10px;border-radius:50%;background:#FFE600;border:2px solid #0B1530;margin-right:12px}
.cap{position:absolute;font:600 26px/1.35 'Figtree';color:#0B1530}
.cap small{display:block;font:500 22px/1.35 'Figtree';color:#475569}
.imgbox{position:absolute;border-radius:14px;overflow:hidden;box-shadow:0 14px 34px rgba(11,21,48,.2);background:#fff}
.imgbox img{width:100%;height:100%;object-fit:contain;display:block}
"""
class R:
    def __init__(s):
        s.p = sync_playwright().start(); s.b = s.p.chromium.launch(executable_path=EXE, args=['--no-sandbox'])
        s.pg = s.b.new_page(viewport={'width': 1920, 'height': 1080}); os.makedirs('/tmp/rend', exist_ok=True)
    def close(s): s.b.close(); s.p.stop()
    def page(s, body, out, bg='#fff', css='', transparent=False):
        h = f"<!doctype html><html><head><meta charset=utf-8><style>{CSS.replace('%BG%', 'transparent' if transparent else bg)}{css}</style></head><body>{body}</body></html>"
        f = '/tmp/rend/p.html'; open(f, 'w').write(h); s.pg.goto('file://' + f); s.pg.wait_for_timeout(120)
        s.pg.screenshot(path=out, omit_background=transparent)
    def measure(s, cards, w=1305):
        body = ''.join(f'<div class="card" style="position:relative;left:0;width:{w}px;margin-bottom:10px">{c}</div>' for c in cards)
        s.page(body, '/tmp/rend/m.png')
        return s.pg.evaluate("[...document.querySelectorAll('.card')].map(e=>Math.ceil(e.getBoundingClientRect().height))")
    # --- slide bianca del docente
    def base(s, eyebrow, title, page, prof=True, nl=1):
        top = 196 + (66 * 1.08 * nl) + 24
        h = f'<img class=logo src="file://{LOGO}"><div class=hl0></div><div class=eb>{html.escape(eyebrow)}</div><div class=ti>{title}</div><div class=bar style="top:{int(top)}px"></div>'
        h += f'<div class=ft><b style="left:0">{MAT}</b><b style="right:0">Pagina {page}</b></div>'
        if prof:
            h += '<div class=cam></div><div class=fascia><div class=n>Giorgio Mazzotti</div><div class=m>PROF. DI STORIA DELL\'ARTE</div></div>'
        return h, int(top) + 40
    def slide(s, eyebrow, title, cards, active, page, out, kw=None, prof=True, y0=None, zoom=False):
        if zoom and active is not None: cards = [cards[active].replace('<b>', '<b style="font-size:54px">')]; active = 0
        nl = 2 if len(title) > 40 else 1
        h, y = s.base(eyebrow, title, page, prof, nl)
        hs = s.measure(cards) if not zoom else [330]; y = y0 or y; gap = 22
        y += 10
        for i, (c, hh) in enumerate(zip(cards, hs)):
            cl = 'card' + (' act' if i == active else (' dim' if active is not None and active >= 0 else ''))
            h += f'<div class="{cl}" style="top:{y + (60 if zoom else 0)}px{";font-size:54px;line-height:1.45" if zoom else ""}">{c}</div>'; y += hh + gap
        if kw and prof: h += '<div class=kw><h4>PAROLE CHIAVE</h4>' + ''.join(f'<div>{html.escape(k)}</div>' for k in kw) + '</div>'
        s.page(h, out)
        return y
    def imgslide(s, eyebrow, title, items, page, out, prof=True):
        # items: [(path,x,y,w,h,caption_html)]
        nl = 2 if len(title) > 40 else 1
        h, y = s.base(eyebrow, title, page, prof, nl)
        from PIL import Image as _I
        for p, x, yy, w, hh, cap in items:
            iw, ih = _I.open(p).size; sc = min(w / iw, hh / ih); fw, fh = int(iw * sc), int(ih * sc); fx = x + (w - fw) // 2
            h += f'<div class=imgbox style="left:{fx}px;top:{yy}px;width:{fw}px;height:{fh}px"><img src="file://{os.path.abspath(p)}"></div>'
            if cap: h += f'<div class=cap style="left:{fx}px;top:{yy+fh+12}px;width:{(fw if len(items) > 1 else min(max(fw,820),1385-fx))}px">{cap}</div>'
        s.page(h, out)

# ===================== schede blu animate (overlay trasparente) =====================
DCSS = """
.dk .logo{filter:brightness(0) invert(1);opacity:.95}
.dk .hl0{background:rgba(255,255,255,.18)}
.dk .eb{color:#9DC3FF}
.dk .ti{color:#fff}
.dk .bar{background:#FFE600}
.dk .ft b{color:#9DC3FF}
.dk .ft{border-top:1px solid rgba(255,255,255,.18)}
.li{position:absolute;display:flex;align-items:center;gap:26px;font:600 44px/1.3 'Figtree';color:#fff}
.li .n{flex:none;width:54px;height:54px;border-radius:50%;background:#2060AF;color:#fff;font:800 28px 'Bricolage Grotesque';display:flex;align-items:center;justify-content:center}
.li.done{opacity:.82}
.li.act{opacity:1}
.li.act .hl{background:linear-gradient(transparent 62%,rgba(255,230,0,.95) 62%);padding:0 6px;margin:0 -6px;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.li.act .n{background:#FFE600;color:#0B1530}
.dimg{position:absolute;border-radius:18px;overflow:hidden;box-shadow:0 18px 44px rgba(0,0,0,.45);background:#fff}
.dimg img{width:100%;height:100%;object-fit:contain;background:#fff}
.dcap{position:absolute;font:500 26px/1.35 'Figtree';color:#DCE8FF}
.big{position:absolute;left:80px;right:80px;font:800 110px/1.05 'Bricolage Grotesque';color:#fff}
.sub{position:absolute;left:80px;right:80px;font:600 40px/1.35 'Figtree';color:#DCE8FF}
.gl{position:absolute;left:80px;right:80px;font:400 36px/1.35 'Figtree';color:#fff}
.gl b{font:800 38px 'Bricolage Grotesque';color:#FFE600}
.panel{position:absolute;background:rgba(255,255,255,.08);border:3px solid rgba(255,255,255,.22);border-radius:22px;padding:22px 30px}
.panel.act{border:6px solid #FFE600;background:rgba(255,230,0,.10)}
.panel h3{margin:0 0 8px;font:800 40px 'Bricolage Grotesque';color:#FFE600}
.panel p{margin:0;font:500 30px/1.4 'Figtree';color:#fff}
.ck{position:absolute;left:80px;right:80px;padding:20px 34px;border-radius:22px;background:rgba(255,255,255,.08);border:3px solid rgba(255,255,255,.22);font:500 34px/1.42 'Figtree';color:#fff}
.ck.act{border:6px solid #FFE600;padding:17px 31px;background:rgba(255,230,0,.10)}
.ck b{font:800 34px 'Bricolage Grotesque';color:#FFE600;margin-right:10px}
"""
def _dk_base(s, eyebrow, title, nl=1, foot=True, bar=True):
    top = 196 + int(66 * 1.08 * nl) + 24
    h = f'<img class=logo src="file://{LOGO}"><div class=hl0></div>'
    if eyebrow: h += f'<div class=eb>{html.escape(eyebrow)}</div>'
    if title: h += f'<div class=ti>{title}</div>'
    if title and bar: h += f'<div class=bar style="top:{top}px"></div>'
    if foot: h += f'<div class=ft><b style="left:0">{MAT}</b></div>'
    return h, top + 40
def dark_page(s, body, out):
    h = f"<!doctype html><html><head><meta charset=utf-8><style>{CSS.replace('%BG%','transparent')}{DCSS}</style></head><body class=dk>{body}</body></html>"
    f = '/tmp/rend/d.html'; open(f, 'w').write(h); s.pg.goto('file://' + f); s.pg.wait_for_timeout(120)
    s.pg.screenshot(path=out, omit_background=True)
R.dark_page = dark_page; R.dk_base = _dk_base

def dark_lines(s, eyebrow, title, lines, active, out, img=None, imgcap=None, y0=None, fs=None):
    h, y = s.dk_base(eyebrow, title, 1 if len(title or '') < 40 else 2)
    x = 80
    if img:
        p, ix, iy, iw, ih = img
        from PIL import Image as _I
        _w, _h = _I.open(p).size; sc = min(iw / _w, ih / _h); iw, ih = int(_w * sc), int(_h * sc)
        h += f'<div class=dimg style="left:{ix}px;top:{iy}px;width:{iw}px;height:{ih}px"><img src="file://{os.path.abspath(p)}"></div>'
        if imgcap: h += f'<div class=dcap style="left:{ix}px;top:{iy+ih+14}px;width:{max(iw,600)}px">{imgcap}</div>'
        x = ix + iw + 70
    y = y0 or y + 20
    for i, t in enumerate(lines):
        if active is None or i > active: continue
        cl = 'li act' if i == active else 'li done'
        wd = 1840 - x
        st = f'left:{x}px;top:{y}px;width:{wd}px' + (f';font-size:{fs}px' if fs else '')
        h += f'<div class="{cl}" style="{st}"><div class=n>{i+1}</div><div class=t><span class=hl>{t}</span></div></div>'
        nch = len(t.replace('<b>', '').replace('</b>', ''))
        per = max(18, int((wd - 90) / ((fs or 44) * 0.5)))
        nl = max(1, -(-nch // per)); y += int(nl * (fs or 44) * 1.3 + 34)
    s.dark_page(h, out)
R.dark_lines = dark_lines

def dark_title(s, eyebrow, title, out, sub=None):
    h, _ = s.dk_base(eyebrow, None, 1)
    h += f'<div class=big style="top:380px">{title}</div>'
    if sub: h += f'<div class=sub style="top:640px">{sub}</div>'
    h += '<div class=bar style="top:600px;width:140px;height:8px"></div>'
    s.dark_page(h, out)
R.dark_title = dark_title
