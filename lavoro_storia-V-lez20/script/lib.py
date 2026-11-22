import os, json, html, subprocess, hashlib
B = '/tmp/w/b'
NOTTE = '#0B1530'; BLU = '#2060AF'; GIALLO = '#FFE600'
CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1920px;height:1080px;overflow:hidden;background:#fff;font-family:'Figtree',sans-serif;color:#0B1530}
.logo{position:absolute;left:70px;top:40px;height:72px}
.hr{position:absolute;left:80px;right:80px;top:124px;height:1px;background:#DDE2EA}
.hr2{position:absolute;left:80px;right:80px;top:981px;height:1px;background:#DDE2EA}
.eyebrow{position:absolute;left:80px;top:146px;font-weight:700;font-size:26px;letter-spacing:.14em;color:#2060AF;text-transform:uppercase}
.title{position:absolute;left:80px;top:196px;width:1290px;font-family:'Bricolage Grotesque';font-weight:800;color:#2060AF;line-height:1.08}
.bar{position:absolute;left:80px;height:6px;width:86px;background:#2060AF;border-radius:3px}
.foot{position:absolute;top:1000px;font-weight:700;font-size:22px;letter-spacing:.12em;color:#2060AF}
.cams{position:absolute;left:1428px;top:148px;width:412px;height:309px;border-radius:18px;background:#F3F5F9;box-shadow:0 14px 34px rgba(60,70,90,.22)}
.band{position:absolute;left:1428px;top:470px;width:412px;transform:rotate(-1.4deg);background:#FFE600;border-radius:8px;padding:16px 22px 14px;box-shadow:0 10px 24px rgba(60,70,90,.25)}
.band b{display:block;font-family:'Bricolage Grotesque';font-weight:800;font-size:34px;color:#0B1530}
.band span{font-weight:700;font-size:21px;letter-spacing:.06em;color:#0B1530}
.kw{position:absolute;left:1428px;top:640px;width:412px}
.kw h4{font-weight:700;font-size:22px;letter-spacing:.14em;color:#2060AF;margin-bottom:12px}
.kw div{display:inline-block;background:#fff;border:2px solid #2060AF;border-radius:999px;padding:6px 16px;margin:0 8px 10px 0;font-weight:600;font-size:26px;color:#0B1530}
.card{position:absolute;left:80px;width:1290px;background:#fff;border:3px solid #E3E8F0;border-radius:18px;padding:22px 30px;font-size:40px;line-height:1.5;box-shadow:0 10px 26px rgba(60,70,90,.12);opacity:.55}
.card b{font-weight:800}
.card em{font-style:italic}
.card.on{border-color:#FFE600;opacity:1;box-shadow:0 0 0 5px rgba(255,230,0,.55),0 10px 26px rgba(60,70,90,.18)}
.card i{position:absolute;left:-14px;top:-14px;width:30px;height:30px;border-radius:50%;background:#FFE600;border:3px solid #fff;display:none}
.card.on i{display:block}
.dark{background:radial-gradient(1200px 700px at 20% 10%,#1B3E86 0%,#0B1530 60%,#070D20 100%);color:#fff}
.dark .eyebrow{color:#FFE600}
"""

def pagina(body, extra_css='', dark=False):
    return f"""<!doctype html><html><head><meta charset='utf-8'><style>{CSS}{extra_css}</style></head>
<body class='{'dark' if dark else ''}'>{body}</body></html>"""

NOCAM = False
def chrome(eyebrow, title, pagina_n, materia='STORIA', cam=True, kw=None, dark=False, title_px=70, title_w=1290):
    import lib as _l
    if _l.NOCAM: cam = False
    h = ''
    if not dark:
        h += "<img class='logo' src='file://%s/assets/logo.png'><div class='hr'></div><div class='hr2'></div>" % B
        h += f"<div class='foot' style='left:80px'>{materia}</div><div class='foot' style='right:80px'>Pagina {pagina_n}</div>"
    h += f"<div class='eyebrow'>{html.escape(eyebrow)}</div>"
    h += f"<div class='title' style='font-size:{title_px}px;width:{title_w}px;{'color:#fff' if dark else ''}'>{title}</div>"
    if cam:
        h += "<div class='cams'></div><div class='band'><b>Giorgio Mazzotti</b><span>PROF. DI STORIA</span></div>"
    if kw:
        if True:
            h += "<div class='kw'><h4>PAROLE CHIAVE</h4>" + ''.join(f"<div>{html.escape(k)}</div>" for k in kw[:5]) + "</div>"
    return h

def slide_html(eyebrow, title, cards, active, pagina_n, kw=None, top=330, gap=22):
    """cards: lista di html (testo con <b>); active: indice acceso o None. Altezze reali misurate dal browser (flow verticale)."""
    h = chrome(eyebrow, title, pagina_n, kw=kw, title_px=64)
    h += f"<div style='position:absolute;left:0;top:{top}px;width:1920px'>"
    for i, c in enumerate(cards):
        h += f"<div class='card{' on' if i == active else ''}' style='position:relative;margin-bottom:{gap}px'><i></i>{c}</div>"
    h += '</div>'
    return h

def render_many(jobs):
    """jobs: [(html_str, out_png)] -> scrive html in tmp e lancia node una sola volta"""
    os.makedirs(B + '/h', exist_ok=True)
    L = []
    for s, out in jobs:
        if os.path.exists(out): continue
        f = B + '/h/' + hashlib.md5(out.encode()).hexdigest() + '.html'
        open(f, 'w').write(s)
        L.append({'html': f, 'png': out})
    if L:
        json.dump(L, open(B + '/jobs.json', 'w'))
        subprocess.run(['node', B + '/render.js', B + '/jobs.json'], check=True, cwd='/tmp/w')
