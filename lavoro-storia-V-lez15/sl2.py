# -*- coding: utf-8 -*-
# Slide della Lezione 15 (correzioni 22/11): card a 40 px, interlinea 1,5, max 3 card (qui 2 per finestra), fondo bianco.
import os, sys, re, html, base64
from playwright.sync_api import sync_playwright
sys.path.insert(0, '/tmp/claude-0/l15')
from dati import ARG, LEZ_TITOLO, GLOSS, GLOBAL_ORDER
W = '/tmp/claude-0/l15'
FD = '/home/user/Lezioni/scambio/strumenti/font'
CHROME = '/opt/pw-browsers/chromium-1243/chrome-linux64/chrome'
LOGO = base64.b64encode(open(W + '/logo_blu.svg', 'rb').read()).decode()
MATERIA = 'Storia V'
CSS = """
@font-face{font-family:'BG';font-weight:800;src:url('file://%(f)s/BricolageGrotesque-ExtraBold.ttf')}
@font-face{font-family:'FG';font-weight:500;src:url('file://%(f)s/Figtree-Medium.ttf')}
@font-face{font-family:'FG';font-weight:700;src:url('file://%(f)s/Figtree-Bold.ttf')}
@font-face{font-family:'FG';font-weight:800;src:url('file://%(f)s/Figtree-ExtraBold.ttf')}
*{box-sizing:border-box;margin:0;padding:0}
body{width:1920px;height:1080px;background:#fff;font-family:'FG';color:#0B1530;position:relative;overflow:hidden}
#logo{position:absolute;left:80px;top:40px;height:58px}
.hl{position:absolute;left:80px;right:80px;top:116px;height:1px;background:#E3E7EF}
.fl{position:absolute;left:80px;right:80px;top:1000px;height:1px;background:#E3E7EF}
.lab{position:absolute;left:80px;top:134px;font-weight:700;font-size:26px;letter-spacing:.2em;color:#2060AF;text-transform:uppercase}
.main{position:absolute;left:80px;top:176px;width:1300px}
.ttl{font-family:'BG';font-weight:800;font-size:54px;letter-spacing:-.02em;line-height:1.08;color:#0B1530}
.cards{margin-top:26px}
.card{display:flex;align-items:flex-start;gap:20px;border:4px solid #E3E7EF;border-radius:22px;padding:12px 24px;margin-bottom:18px;background:#fff;font-size:40px;line-height:1.5;font-weight:500;color:#0B1530}
.card b{font-weight:800}
.card.dim{opacity:.62}
.card.on{border-color:#FFE600;background:#FFFBD6;box-shadow:0 8px 24px rgba(255,214,0,.35);opacity:1}
.num{flex:0 0 52px;height:52px;border-radius:50%;background:#E3E7EF;color:#0B1530;font-weight:800;font-size:30px;display:flex;align-items:center;justify-content:center;margin-top:12px}
.card.on .num{background:#FFE600}
.foot{position:absolute;top:1018px;font-weight:700;font-size:24px;letter-spacing:.2em;color:#2060AF;text-transform:uppercase}
.shadow{position:absolute;left:1428px;top:148px;width:412px;height:309px;border-radius:22px;box-shadow:0 18px 50px rgba(30,40,70,.28);background:#ccc}
.fascia{position:absolute;left:1432px;top:476px;width:408px;height:100px;background:#FFE600;border-radius:8px;transform:rotate(-3deg);box-shadow:0 10px 26px rgba(30,40,70,.25);padding:14px 22px}
.fascia .n{font-family:'BG';font-weight:800;font-size:38px;line-height:1.05;color:#0B1530}
.fascia .r{font-weight:800;font-size:20px;letter-spacing:.06em;margin-top:6px;color:#0B1530}
.pk{position:absolute;left:1428px;top:640px;width:412px;border:3px solid #E3E7EF;border-radius:20px;padding:16px 18px;background:#fff}
.pk h4{font-weight:800;font-size:24px;letter-spacing:.2em;color:#2060AF;margin-bottom:10px}
.pk div{font-weight:700;font-size:28px;line-height:1.25;padding:5px 10px;border-radius:10px;color:#0B1530;margin-bottom:2px}
.pk div.on{background:#FFE600}
.imgbox{margin-top:24px;width:1300px;height:700px;border-radius:20px;border:3px solid #E3E7EF;display:flex;align-items:center;justify-content:center;gap:24px;background:#fff;box-shadow:0 14px 40px rgba(30,40,70,.10);padding:14px}
.imgbox img{max-height:670px;object-fit:contain}
.pill{position:absolute;left:80px;top:134px;background:#FFE600;border-radius:30px;padding:8px 26px;font-weight:800;font-size:26px;letter-spacing:.2em;color:#0B1530}
.tbl{position:absolute;left:80px;top:330px;width:1760px;border-radius:20px;overflow:hidden;border:3px solid #E3E7EF;box-shadow:0 14px 40px rgba(30,40,70,.10)}
.th{display:flex;background:#0B1530;color:#fff;font-weight:800;font-size:28px;letter-spacing:.14em;padding:18px 30px}
.th span:first-child{flex:0 0 560px}
.tr{display:flex;align-items:center;padding:0 30px;height:132px;border-top:2px solid #E3E7EF;font-size:36px;line-height:1.3;font-weight:500}
.tr span:first-child{flex:0 0 560px;font-weight:800;color:#2060AF;font-size:38px;padding-right:24px}
.tr.on{background:#FFE600}
.tr.on span:first-child{color:#0B1530}
.cover-t{position:absolute;left:80px;top:196px;font-family:'BG';font-weight:800;font-size:84px;line-height:1.02;color:#0B1530;letter-spacing:-.02em;width:1250px}
.bar{position:absolute;left:80px;width:85px;height:7px;border-radius:4px;background:#2060AF}
.card2{position:absolute;border:3px solid #E3E7EF;border-radius:24px;background:#fff;box-shadow:0 18px 50px rgba(30,40,70,.12);padding:28px 40px}
.card2 h4{font-weight:800;font-size:26px;letter-spacing:.2em;color:#2060AF;margin-bottom:14px}
.card2 li{font-size:30px;font-weight:700;line-height:1.28;margin-left:34px;margin-bottom:4px}
.ag{position:absolute;left:80px;width:1760px}
.ar{display:flex;align-items:center;border:4px solid #E3E7EF;border-radius:18px;padding:0 28px;height:68px;margin-bottom:8px;font-size:36px;font-weight:700}
.ar i{font-style:normal;flex:0 0 66px;height:50px;width:50px;border-radius:50%;background:#E3E7EF;font-weight:800;font-size:28px;display:flex;align-items:center;justify-content:center;margin-right:24px;flex:0 0 50px}
.ar.on{background:#FFF7B8;border-color:#FFE600}.ar.on i{background:#FFE600}
.gr{display:flex;align-items:center;border:3px solid #E3E7EF;border-radius:18px;padding:0 28px;height:92px;margin-bottom:10px;font-size:32px;line-height:1.25;font-weight:500}
.gr b{flex:0 0 480px;font-weight:800;font-size:36px;color:#2060AF}
.gr.on{background:#FFE600;border-color:#FFE600}.gr.on b{color:#0B1530}
.cmp{position:absolute;left:80px;top:300px;width:1760px;border:4px solid #E3E7EF;border-radius:24px;padding:36px 48px;font-size:46px;line-height:1.5;font-weight:500;box-shadow:0 14px 40px rgba(30,40,70,.10)}
.cmp .n{display:inline-flex;align-items:center;justify-content:center;width:64px;height:64px;border-radius:50%;background:#FFE600;font-weight:800;font-size:38px;margin-right:22px;vertical-align:middle}
""".replace("%(f)s", FD)

def esc(s): return html.escape(s)

def frame(lab, body, foot_page, prof=True, pill=None, keys=None, active=-1, materia=MATERIA):
    h = f"<html><head><meta charset=utf-8><style>{CSS}</style></head><body>"
    h += f"<img id=logo src='data:image/svg+xml;base64,{LOGO}'><div class=hl></div><div class=fl></div>"
    h += f"<div class=pill>{esc(pill)}</div>" if pill else f"<div class=lab>{esc(lab)}</div>"
    h += body
    h += f"<div class=foot style='left:80px'>{esc(materia)}</div>" + (f"<div class=foot style='right:80px'>Pagina {foot_page}</div>" if foot_page else '')
    if prof:
        h += "<div class=shadow></div><div class=fascia><div class=n>Giorgio Mazzotti</div><div class=r>PROF. DI STORIA</div></div>"
        if keys:
            h += "<div class=pk><h4>PAROLE CHIAVE</h4>" + "".join(f"<div class='{'on' if i == active else ''}'>{esc(k)}</div>" for i, k in enumerate(keys)) + "</div>"
    return h + "</body></html>"

def head_body(c):
    m = re.match(r'^(.{3,110}?):\s(.*)$', c)
    return (m.group(1), m.group(2)) if m else ('', c)

def cards_from_pdf(pdf=None):
    import fitz
    d = fitz.open(pdf or (W + '/src/slide/SLIDE/LEZIONE 15.pdf'))
    out = {}
    for a in ARG:
        bl = [re.sub(r'\s+', ' ', b[4]).strip() for b in d[a['pag'][0] - 1].get_text('blocks') if b[4].strip()]
        out[a['n']] = bl[1:]
    return out

def N(n): return GLOBAL_ORDER.index(n) + 1
def txt_slide(n, win, active, cp, page, windows=None, prof=True):
    if windows is None:
        from plan2 import windows as _w
        windows = _w(n)
    """win: indice finestra; active: indice card accesa (globale 0..3) o -1"""
    a = ARG[n - 1]; idx = windows[win]; cards = ''
    for k, i in enumerate(idx):
        h, b = head_body(cp[n][i])
        cls = 'on' if i == active else 'dim' if active >= 0 else ''
        cards += f"<div class='card {cls}'><div class=num>{k + 1}</div><div><b>{esc(h)}:</b> {esc(b)}</div></div>"
    body = f"<div class=main><div class=ttl>{esc(a['titolo'])}</div><div class=cards>{cards}</div></div>"
    return frame(f"{N(n):02d} · {a['nome']}", body, page, keys=[k for k, _ in a['schema']], active=active, prof=prof)

def img_slide(n, files, page, active=-1, prof=True):
    a = ARG[n - 1]
    imgs = ''.join(f"<img src='file://{f}'>" for f in files)
    body = f"<div class=main><div class=ttl>{esc(a['titolo'])}</div><div class=imgbox>{imgs}</div></div>"
    return frame(f"{N(n):02d} · {a['nome']}", body, page, keys=[k for k, _ in a['schema']], active=active, prof=prof)

def cover(prof, order=None, page=1):
    order = order or GLOBAL_ORDER
    items = ''.join(f"<li>{esc(ARG[n - 1]['nome'])}</li>" for n in order)
    h = f"<html><head><meta charset=utf-8><style>{CSS}</style></head><body>"
    h += f"<img id=logo src='data:image/svg+xml;base64,{LOGO}'><div class=hl></div><div class=fl></div>"
    h += "<div class=lab>STORIA V · VIDEOLEZIONE</div>"
    h += f"<div class=cover-t>{esc(LEZ_TITOLO).replace(' (', '<br>(')}</div><div class=bar style='top:392px'></div>"
    h += f"<div class=card2 style='left:80px;top:440px;width:1300px;height:330px'><h4>ARGOMENTI</h4><ul style='columns:2;column-gap:36px'>{items}</ul></div>"
    h += f"<div class=foot style='left:80px'>{MATERIA}</div><div class=foot style='right:80px'>Pagina {page}</div>"
    if prof: h += "<div class=shadow></div><div class=fascia><div class=n>Giorgio Mazzotti</div><div class=r>PROF. DI STORIA</div></div>"
    return h + "</body></html>"

def agenda(active, page=2):
    rows = ''.join(f"<div class='ar {'on' if i == active else ''}'><i>{i + 1}</i>{esc(ARG[n - 1]['titolo'])}</div>" for i, n in enumerate(GLOBAL_ORDER))
    body = f"<div class=ag style='top:182px'>{rows}</div>"
    return frame('', body, page, prof=False, pill='DI COSA PARLIAMO')

def schema(n, active, page):
    a = ARG[n - 1]; rows = ''
    for i, (kw, fr) in enumerate(a['schema']):
        txt = re.sub(r'^(Primo|Secondo|Terzo|Quarto|Quinto): ', '', fr); txt = txt[0].upper() + txt[1:]
        rows += f"<div class='tr {'on' if i == active else ''}' style='opacity:{1 if i <= active else 0}'><span>{esc(kw)}</span><span>{esc(DISP(txt))}</span></div>"
    body = f"<div class=main style='top:176px'><div class=ttl>{esc(a['titolo'])}</div></div><div class=tbl><div class=th><span>PAROLA CHIAVE</span><span>DA RICORDARE</span></div>{rows}</div>"
    return frame('', body, page, prof=False, pill='PILLOLA DI STORIA')

UN = {'': 0, 'uno': 1, 'un': 1, 'due': 2, 'tre': 3, 'quattro': 4, 'cinque': 5, 'sei': 6, 'sette': 7, 'otto': 8, 'nove': 9, 'dieci': 10, 'undici': 11, 'dodici': 12, 'tredici': 13,
      'quattordici': 14, 'quindici': 15, 'sedici': 16, 'diciassette': 17, 'diciotto': 18, 'diciannove': 19}
TE = {'venti': 20, 'trenta': 30, 'quaranta': 40, 'cinquanta': 50, 'sessanta': 60, 'settanta': 70, 'ottanta': 80, 'novanta': 90}
def _anno(m):
    r = m.group(1)
    for t, n in sorted(TE.items(), key=lambda x: -len(x[0])):
        if r.startswith(t) or r.startswith(t[:-1]):
            k = t if r.startswith(t) else t[:-1]
            if r[len(k):] in UN: return str(1900 + n + UN[r[len(k):]])
    if r in UN: return str(1900 + UN[r])
    return m.group(0)
EXTRA = [("quindici milioni", "15 milioni"), ("Risoluzione centottantuno", "Risoluzione 181"), ("ventinove Stati", "29 Stati")]
def DISP(s):
    s = re.sub(r'millenovecento(\w*)', _anno, s)
    for a, b in EXTRA: s = s.replace(a, b)
    return s

def gloss(active, page, terms=None):
    terms = terms or GLOSS; rows = ''
    for i, (t, d) in enumerate(terms):
        dd = DISP(d); dd = dd[0].upper() + dd[1:]
        rows += f"<div class='gr {'on' if i == active else ''}'><b>{esc(t)}</b><span>{esc(dd)}</span></div>"
    return frame('GLOSSARIO · PAROLE CHIAVE', f"<div class=main><div class=ttl>Glossario</div></div><div class=ag style='top:290px'>{rows}</div>", page, prof=False)

def compito(k, testo, page):
    body = f"<div class=main><div class=ttl>Compiti</div></div><div class=cmp><span class=n>{k}</span>{esc(testo)}</div>"
    return frame('COMPITI DEL DOCENTE', body, page, prof=False)

def render(items, outdir):
    os.makedirs(outdir, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME, args=['--allow-file-access-from-files', '--no-sandbox'])
        pg = b.new_page(viewport={'width': 1920, 'height': 1080})
        for name, h in items:
            f = f'{outdir}/{name}.html'; open(f, 'w').write(h)
            pg.goto('file://' + f); pg.wait_for_timeout(250)
            pg.screenshot(path=f'{outdir}/{name}.png')
        b.close()

def an_slide(lab, title, sents, active, shown, page=None):
    """approfondimento animato: titolo + frasi che compaiono e si accendono con la voce (testo 40 px, a tutta larghezza)"""
    cards = ''
    for i, t in enumerate(sents):
        if i >= shown: break
        cls = 'on' if i == active else 'dim' if active >= 0 else ''
        cards += f"<div class='card {cls}' style='width:1760px'><div class=num>{i + 1}</div><div>{esc(DISP(t))}</div></div>"
    body = f"<div class=main style='width:1760px'><div class=ttl>{esc(title)}</div><div class=cards>{cards}</div></div>"
    return frame(lab, body, page, prof=False)

def cover_dispensa():
    h = f"<html><head><meta charset=utf-8><style>{CSS}</style></head><body>"
    h += f"<img id=logo src='data:image/svg+xml;base64,{LOGO}'><div class=hl></div><div class=fl></div>"
    h += "<div class=lab>STORIA V · VIDEOLEZIONE</div>"
    h += f"<div class=cover-t style='top:330px'>{esc(LEZ_TITOLO).replace(' (', '<br>(')}</div><div class=bar style='top:530px'></div>"
    h += f"<div class=foot style='left:80px'>{MATERIA}</div><div class=foot style='right:80px'>Pagina 1</div>"
    return h + "</body></html>"
