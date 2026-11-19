# -*- coding: utf-8 -*-
# Slide bianche nel modello Spagnolo (1920x1080): testo/card, immagini del prof, schema di ripasso, glossario, copertina.
import os, sys, json, re, base64, html
from playwright.sync_api import sync_playwright
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dati import *
W = '/tmp/claude-0/l17'
FD = '/home/user/Lezioni/scambio/strumenti/font'
CHROME = '/opt/pw-browsers/chromium-1243/chrome-linux64/chrome'
LOGO = base64.b64encode(open(W + '/logo_blu.svg', 'rb').read()).decode()
CSS = """
@font-face{font-family:'BG';font-weight:800;src:url('file://%(f)s/BricolageGrotesque-ExtraBold.ttf')}
@font-face{font-family:'FG';font-weight:500;src:url('file://%(f)s/Figtree-Medium.ttf')}
@font-face{font-family:'FG';font-weight:700;src:url('file://%(f)s/Figtree-Bold.ttf')}
@font-face{font-family:'FG';font-weight:800;src:url('file://%(f)s/Figtree-ExtraBold.ttf')}
*{box-sizing:border-box;margin:0;padding:0}
body{width:1920px;height:1080px;background:#fff;font-family:'FG';color:#0B1530;position:relative;overflow:hidden}
#logo{position:absolute;left:80px;top:48px;height:58px}
.hl{position:absolute;left:80px;right:80px;top:124px;height:1px;background:#E3E7EF}
.fl{position:absolute;left:80px;right:80px;top:981px;height:1px;background:#E3E7EF}
.lab{position:absolute;left:80px;top:146px;font-weight:700;font-size:26px;letter-spacing:.2em;color:#2060AF;text-transform:uppercase}
.ttl{position:absolute;left:80px;top:196px;font-family:'BG';font-weight:800;font-size:56px;letter-spacing:-.02em;line-height:1.05;color:#0B1530;width:1330px}
.bar{position:absolute;left:80px;width:85px;height:7px;border-radius:4px;background:#2060AF}
.foot{position:absolute;top:1000px;font-weight:700;font-size:22px;letter-spacing:.2em;color:#2060AF;text-transform:uppercase}
.cards{position:absolute;left:80px;top:268px;width:1320px}
.card{display:flex;align-items:flex-start;gap:20px;border:3px solid #E3E7EF;border-radius:20px;padding:8px 20px;margin-bottom:9px;background:#fff;font-size:28px;line-height:1.24;font-weight:500}
.card b{font-weight:800}
.card.on{border-color:#FFE600;background:#FFFBD6;box-shadow:0 8px 24px rgba(255,214,0,.35)}
.num{flex:0 0 46px;height:46px;border-radius:50%;background:#E3E7EF;color:#0B1530;font-weight:800;font-size:26px;display:flex;align-items:center;justify-content:center;margin-top:2px}
.card.on .num{background:#FFE600}
.shadow{position:absolute;left:1428px;top:148px;width:412px;height:310px;border-radius:22px;box-shadow:0 18px 50px rgba(30,40,70,.28);background:#ccc}
.fascia{position:absolute;left:1432px;top:476px;width:408px;height:100px;background:#FFE600;border-radius:8px;transform:rotate(-3deg);box-shadow:0 10px 26px rgba(30,40,70,.25);padding:14px 22px}
.fascia .n{font-family:'BG';font-weight:800;font-size:38px;line-height:1.05;color:#0B1530}
.fascia .r{font-weight:800;font-size:20px;letter-spacing:.06em;margin-top:6px;color:#0B1530}
.pk{position:absolute;left:1428px;top:640px;width:412px;border:3px solid #E3E7EF;border-radius:20px;padding:16px 20px;background:#fff}
.pk h4{font-weight:800;font-size:22px;letter-spacing:.2em;color:#2060AF;margin-bottom:10px}
.pk div{font-weight:700;font-size:28px;line-height:1.3;padding:4px 10px;border-radius:10px;color:#0B1530}
.pk div.on{background:#FFE600}
.imgbox{position:absolute;left:80px;top:290px;width:1320px;height:660px;border-radius:20px;border:3px solid #E3E7EF;display:flex;align-items:center;justify-content:center;background:#fff;box-shadow:0 14px 40px rgba(30,40,70,.10);overflow:hidden}
.imgbox img{width:1290px;height:630px;object-fit:contain}
.tbl{position:absolute;left:80px;top:320px;width:1760px;border-radius:20px;overflow:hidden;border:3px solid #E3E7EF;box-shadow:0 14px 40px rgba(30,40,70,.10)}
.th{display:flex;background:#0B1530;color:#fff;font-weight:800;font-size:26px;letter-spacing:.14em;padding:18px 30px}
.th span:first-child{flex:0 0 620px}
.tr{display:flex;align-items:center;padding:0 30px;height:118px;border-top:2px solid #E3E7EF;font-size:32px;font-weight:500}
.tr span:first-child{flex:0 0 620px;font-weight:800;color:#2060AF;font-size:34px}
.tr.on{background:#FFE600}
.tr.on span:first-child{color:#0B1530}
.pill{position:absolute;left:80px;top:150px;background:#FFE600;border-radius:30px;padding:8px 26px;font-weight:800;font-size:24px;letter-spacing:.2em;color:#0B1530}
.cover-t{position:absolute;left:80px;top:330px;font-family:'BG';font-weight:800;font-size:96px;line-height:1.0;color:#0B1530;letter-spacing:-.02em;width:1100px}
.card2{position:absolute;border:3px solid #E3E7EF;border-radius:24px;background:#fff;box-shadow:0 18px 50px rgba(30,40,70,.12);padding:34px 44px}
.card2 h4{font-weight:800;font-size:24px;letter-spacing:.2em;color:#2060AF;margin-bottom:18px}
.card2 li{font-size:31px;font-weight:700;line-height:1.3;margin-left:34px;margin-bottom:6px}
.gl{position:absolute;left:80px;width:1760px}
.gr{display:flex;align-items:center;border:3px solid #E3E7EF;border-radius:18px;padding:0 28px;height:64px;margin-bottom:7px;font-size:28px;font-weight:500}
.gr b{flex:0 0 440px;font-weight:800;font-size:30px;color:#2060AF}
.gr.on{background:#FFE600;border-color:#FFE600}.gr.on b{color:#0B1530}
""".replace("%(f)s",FD)

POS = {n: i + 1 for i, n in enumerate(GLOBAL_ORDER)}
def esc(s): return html.escape(s)
def P2(n): return POS.get(n, n)

def frame(lab, title, foot_page, body, prof=True, keys=None, active=-1, pill=None, titlesize=None, shorttitle=False, pdf=False):
    h = f"<html><head><meta charset=utf-8><style>{CSS}</style></head><body>"
    h += f"<img id=logo src='data:image/svg+xml;base64,{LOGO}'><div class=hl></div><div class=fl></div>"
    if pill: h += f"<div class=pill>{esc(pill)}</div>"
    else: h += f"<div class=lab>{esc(lab)}</div>"
    ts = f"font-size:{titlesize}px;" if titlesize else ""
    ty = 184 if not pill else 206
    h += f"<div class=ttl style='top:{ty}px;{ts}'>{title}</div><div class=bar style='top:{ty+(80 if len(re.sub('<[^>]+>','',title))>60 and not titlesize else 74)}px;display:none'></div>"
    h += body
    h += f"<div class=foot style='left:80px'>{esc('Storia V · Prof. Giorgio Mazzotti' if (prof or pdf) else 'Storia V')}</div><div class=foot style='right:80px'>Pagina {foot_page}</div>"
    if prof:
        h += "<div class=shadow></div><div class=fascia><div class=n>Giorgio Mazzotti</div><div class=r>PROF. DI STORIA</div></div>"
        if keys:
            h += "<div class=pk><h4>PAROLE CHIAVE</h4>" + "".join(f"<div class='{'on' if i==active else ''}'>{esc(k)}</div>" for i, k in enumerate(keys)) + "</div>"
    return h + "</body></html>"

def cards_from_pdf():
    import fitz
    d = fitz.open(PDF_SLIDE)
    out = {}
    for a in ARG:
        bl = [b[4].strip().replace('\n', ' ') for b in d[a['pag'][0] - 1].get_text('blocks') if b[4].strip()]
        out[a['n']] = bl[1:]
        for p2 in a.get('more', []):
            out[a['n']] += [b[4].strip().replace('\n', ' ') for b in d[p2 - 1].get_text('blocks') if b[4].strip()]
    return out

def disp(s):
    R = [("ventotto giugno","28 giugno"),("ventiquattro maggio","24 maggio"),("ventiquattro ottobre","24 ottobre")]
    return s

def make_states():
    """elenco degli stati slide: chiave -> html"""
    cp = cards_from_pdf()
    S = {}
    return cp, S


def head_body(c):
    m = re.match(r'^(.{3,110}?):\s(.*)$', c)
    return (m.group(1), m.group(2)) if m else ('', c)

def html_txt(n, active, cp, page, prof=True):
    a = ARG[n - 1]
    cards = ''
    for i, c in enumerate(cp[n]):
        h, b = head_body(c)
        cards += f"<div class='card {'on' if i==active else ''}'><div class=num>{i+1}</div><div><b>{esc(h)}:</b> {esc(b)}</div></div>"
    return frame(f"{P2(n):02d} · {a['nome']}", esc(a['titolo']).replace("casus belli","<i>casus belli</i>"), page,
                 f"<div class=cards>{cards}</div>", keys=[k for k, _ in a['schema']], active=active, titlesize=50, prof=prof, pdf=not prof)

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

def html_cover(page, prof=True, order=None, parte=None):
    order = order or [a['n'] for a in ARG]
    items = ''.join(f"<li>{esc(ARG[n-1]['nome'])}</li>" for n in order)
    h = f"<html><head><meta charset=utf-8><style>{CSS}</style></head><body>"
    h += f"<img id=logo src='data:image/svg+xml;base64,{LOGO}'><div class=hl></div><div class=fl></div>"
    h += "<div class=lab style='top:150px'>STORIA V · VIDEOLEZIONE" + (f" · PARTE {parte}" if parte else "") + "</div>"
    h += "<div class=cover-t style='top:196px;font-size:84px'>" + LEZ_COVER + "</div><div class=bar style='top:300px'></div>"
    h += f"<div class=card2 style='left:80px;top:340px;width:1330px;height:470px'><h4>ARGOMENTI</h4><ul style='columns:2;column-gap:40px'>{items}</ul></div>"
    h += f"<div class=foot style='left:80px'>Storia V · Prof. Giorgio Mazzotti</div><div class=foot style='right:80px'>Pagina {page}</div>"
    if prof: h += "<div class=shadow></div><div class=fascia><div class=n>Giorgio Mazzotti</div><div class=r>PROF. DI STORIA</div></div>"
    return h + "</body></html>"

def html_map(k, frac, page):
    m = MAPPE[k - 1]
    clip = f"clip-path:inset(0 0 {max(0,100-frac*100):.1f}% 0)" if frac < 1 else ''
    body = f"<div class=imgbox style='left:80px;top:268px;width:1760px;height:690px'><img style='width:1720px;height:660px;object-fit:contain;{clip}' src='file:///tmp/claude-0/l17/img/mapc-{m['p']}.png'></div>"
    return frame(f"MAPPA CONCETTUALE · {P2(m['dopo']):02d} · {ARG[m['dopo']-1]['nome']}", esc(m['titolo']), page, body, prof=False, titlesize=50)

def html_newmap(n, stage, page):
    q, centro, rami = NEWMAPS[n]
    css = """<style>
.nm{position:absolute;border-radius:16px;text-align:center;font-weight:700;display:flex;align-items:center;justify-content:center;padding:10px 14px;line-height:1.2}
.c0{left:640px;top:330px;width:640px;height:90px;border:4px solid #E8472E;font-size:34px;font-weight:800;letter-spacing:.06em;background:#fff}
.b1{width:400px;height:130px;top:560px;border:3.5px solid #0E6B7A;font-size:25px;background:#fff;font-weight:800}
.l1{width:400px;height:200px;top:760px;border:3.5px solid #F2A31B;font-size:23px;font-weight:500;background:#fff}
.ln{position:absolute;background:#444;width:3px}.hz{position:absolute;background:#444;height:3px}
</style>"""
    body = css + f"<div class='nm c0'>{esc(centro)}</div>"
    m_ = len(rami); w_ = 340 if m_ >= 5 else (400 if m_ == 4 else 500); st_ = 372 if m_ >= 5 else (444 if m_ == 4 else 560); x0_ = (1920 - ((m_ - 1) * st_ + w_)) // 2
    xs = [x0_ + i * st_ for i in range(m_)]
    body += f"<div class=ln style='left:959px;top:420px;height:70px'></div><div class=hz style='left:{xs[0]+w_//2}px;width:{xs[-1]-xs[0]}px;top:490px'></div>"
    for i, (h, d) in enumerate(rami):
        op = 1 if i < stage else 0
        cx = xs[i] + w_ // 2
        body += f"<div style='opacity:{op}'><div class=ln style='left:{cx}px;top:490px;height:70px'></div><div class='nm b1' style='left:{xs[i]}px;width:{w_}px'>{esc(h[0].upper()+h[1:])}</div><div class=ln style='left:{cx}px;top:690px;height:70px'></div><div class='nm l1' style='left:{xs[i]}px;width:{w_}px'>{esc(DISP(d)[0].upper()+DISP(d)[1:])}</div></div>"
    ttl = f"MAPPA CONCETTUALE · {P2(n):02d} · {ARG[n-1]['nome']}"
    return frame(ttl, esc(q), page, body, prof=False, titlesize=50)

def _test():
    cp = cards_from_pdf()
    render([('t3_1', html_txt(3, 1, cp, 7)), ('t7_2', html_txt(7, 2, cp, 12)), ('t10_0', html_txt(10, 0, cp, 12))], W + '/sl_test')

def html_img(n, imgfile, page, active=-1, prof=True):
    a = ARG[n - 1]
    return frame(f"{P2(n):02d} · {a['nome']}", esc(a['titolo']).replace("casus belli","<i>casus belli</i>"), page,
                 f"<div class=imgbox><img src='file://{imgfile}'></div>", keys=[k for k, _ in a['schema']], active=-1, titlesize=50, prof=prof, pdf=not prof)

def html_schema(n, active, page):
    a = ARG[n - 1]
    rows = ''
    for i, (kw, fr) in enumerate(a['schema']):
        txt = re.sub(r'^(Primo|Secondo|Terzo|Quarto|Quinto): ', '', fr)
        txt = txt[0].upper() + txt[1:]
        rows += f"<div class='tr {'on' if i<=active and i==active else ''}' style='opacity:{1 if i<=active else 0}'><span>{esc(kw)}</span><span>{esc(DISP(txt))}</span></div>"
    body = f"<div class=tbl><div class=th><span>PAROLA CHIAVE</span><span>DA RICORDARE</span></div>{rows}</div>"
    return frame('', esc(a['titolo']).replace("casus belli","<i>casus belli</i>"), page, body, prof=False, pill='PILLOLA DI STORIA', titlesize=50)

UN = {'': 0, 'uno': 1, 'un': 1, 'due': 2, 'tre': 3, 'quattro': 4, 'cinque': 5, 'sei': 6, 'sette': 7, 'otto': 8, 'nove': 9, 'dieci': 10, 'undici': 11, 'dodici': 12, 'tredici': 13,
      'quattordici': 14, 'quindici': 15, 'sedici': 16, 'diciassette': 17, 'diciotto': 18, 'diciannove': 19}
TE = {'venti': 20, 'trenta': 30, 'quaranta': 40, 'cinquanta': 50, 'sessanta': 60, 'settanta': 70, 'ottanta': 80, 'novanta': 90}
def _core(r):
    for t, n in sorted(TE.items(), key=lambda x: -len(x[0])):
        if r.startswith(t) or r.startswith(t[:-1]):
            k = t if r.startswith(t) else t[:-1]
            r2 = r[len(k):]
            if r2 in UN: return str(1900 + n + UN[r2])
    if r in UN: return str(1900 + UN[r])
    return None
def _anno(m):
    r = m.group(1).replace('é', 'e')
    for c in ([r[1:]] if r.startswith('o') else []) + [r]:
        v = _core(c)
        if v: return v
    return m.group(0)
EXTRA = [("quindici milioni", "15 milioni"), ("diciassette milioni", "17 milioni"), ("quaranta milioni", "40 milioni"), ("Risoluzione centottantuno", "Risoluzione 181"), ("Guglielmo secondo", "Guglielmo II"),
         ("ventiquattro ottobre", "24 ottobre"), ("ventiquattro maggio", "24 maggio"), ("ventotto giugno", "28 giugno"), ("ventinove Stati", "29 Stati"), ("centotrentadue miliardi", "132 miliardi")]
def DISP(s):
    s = re.sub(r'millenovecent(\w*)', _anno, s)
    for a, b in EXTRA: s = s.replace(a, b)
    return s

def html_gloss(active, page, terms=None):
    terms = terms or GLOSS
    big = len(terms) <= 6
    rows = ''
    for i, (t, d) in enumerate(terms):
        dd = DISP(d); dd = dd[0].upper() + dd[1:]
        st = "height:104px;font-size:32px;margin-bottom:14px" if big else ""
        rows += f"<div class='gr {'on' if i==active else ''}' style='{st}'><b style='{'font-size:36px' if big else ''}'>{esc(t)}</b><span>{esc(dd)}</span></div>"
    body = f"<div class=gl style='top:290px'>{rows}</div>"
    return frame('GLOSSARIO · PAROLE CHIAVE', 'Glossario', page, body, prof=False, titlesize=50)
