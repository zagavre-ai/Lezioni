# Schede HTML (1920x1080) della grafica Telesio per le videolezioni S1.
from lib_s1 import *

MATERIA = 'Storia'
DOCENTE = 'Prof. Giorgio Mazzotti'
ANNO = 'Quinto anno'


def head(kicker=None, light=True):
    return '<img class=hd src="%s"><div class=hl></div>' % LOGO_I


def foot():
    return '<div class=ft>%s · %s · %s</div>' % (MATERIA, DOCENTE, ANNO)


def docente_tag(keyword=None):
    t = '<div class=doc></div><div class=tag><b>%s</b><i>%s</i><u>%s</u></div>' % (DOCENTE, MATERIA, ANNO.upper())
    if keyword:
        t += ('<div class=abs style="left:1490px;top:520px;width:380px;border-top:3px solid #2060AF;padding-top:14px">'
              '<div class=kick style="font-size:17px;color:#2060AF">Parole chiave</div>'
              '<div style="font-size:26px;font-weight:700;margin-top:10px;line-height:1.25">%s</div></div>' % E(keyword))
    return t


# ------------------------------------------------------------------ titolo argomento
def titolo_arg(i, n, titolo, parte=None):
    seg = ''.join('<i style="display:block;width:96px;height:5px;border-radius:5px;background:%s"></i>' % ('#E3A95C' if k < i else 'rgba(255,255,255,.2)') for k in range(n))
    body = dark_bg(
        '<div class="ghost abs" style="left:1100px;top:140px;font-size:760px">%02d</div>' % i +
        '<div class="kick abs" style="left:160px;top:300px;font-size:30px;color:#E3A95C;letter-spacing:.38em">Argomento %02d / %02d</div>' % (i, n) +
        '<div class="bg2 abs" style="left:160px;top:370px;width:1200px;font-size:104px;color:#fff">%s</div>' % E(titolo) +
        '<div class=abs style="left:160px;top:860px;display:flex;gap:12px">%s</div>' % seg)
    return page(body, 'dark')


# ------------------------------------------------------------------ slide del docente
def slide(titolo_slide, kicker, cards, att=None, img=None, img_cap=None, keyword=None, intro=False, sottotitolo=None):
    """cards = [(lead, [frasi])]; att = (indice_card, indice_frase) acceso; img = percorso immagine della slide-figura."""
    if intro:
        inner = (head() + '<div class="kick abs" style="left:80px;top:300px;font-size:26px;color:#2060AF">%s · %s</div>' % (MATERIA, ANNO) +
                 '<div class="bg2 abs" style="left:80px;top:360px;width:1300px;font-size:104px">%s</div>' % E(titolo_slide) +
                 '<div class=abs style="left:80px;top:640px;width:1250px;font-size:36px;line-height:1.4;color:#33415f">%s</div>' % E(sottotitolo or '') +
                 '<div class=abs style="left:80px;top:610px;width:140px;height:8px;background:#2060AF"></div>' + docente_tag() + foot())
        return page(inner, 'light')
    top = ('<div class="kick abs" style="left:80px;top:146px;font-size:22px;color:#2060AF;letter-spacing:.22em">%s</div>'
           '<div class="bg2 abs" style="left:80px;top:182px;width:1340px;font-size:46px">%s</div>' % (E(kicker), E(titolo_slide)))
    if img:
        b = b64(img)
        body = (head() + top + '<div class=abs style="left:80px;top:268px;width:1340px;height:690px;display:flex;flex-direction:column;align-items:center;justify-content:center">'
                '<img src="data:image/png;base64,%s" style="max-width:1340px;max-height:%dpx;border-radius:14px;box-shadow:0 12px 36px rgba(20,40,90,.2);background:#fff">%s</div>' % (
                    b, 610 if img_cap else 680, ('<div style="margin-top:16px;font-size:30px;font-weight:600;color:#33415f">%s</div>' % E(img_cap)) if img_cap else '')
                + docente_tag(keyword) + foot())
        return page(body, 'light')
    cs = ''
    for ci, (lead, frasi) in enumerate(cards):
        act = att is not None and att[0] == ci
        txt = ''
        for fi, f in enumerate(frasi):
            if act and att[1] == fi:
                txt += '<mark>%s</mark> ' % E(f)
            else:
                txt += E(f) + ' '
        cs += ('<div class="cd%s"><b>%s</b> %s</div>' % (' on' if act else '', E(lead), txt))
    css = """
:root{--fs:34px;--lh:1.36;--pad:24px;--gap:20px}
#cards{position:absolute;left:80px;top:262px;width:1340px;display:flex;flex-direction:column;gap:var(--gap)}
.cd{background:rgba(255,255,255,.72);border:3px solid #E6EBF3;border-radius:20px;padding:var(--pad) 34px;font-size:var(--fs);line-height:var(--lh);color:#7C879C}
.cd b{color:#8E99B0}
.cd.on{background:#fff;border:5px solid #FFE600;color:#0B1530;box-shadow:0 14px 34px rgba(20,40,90,.14)}
.cd.on b{color:#2060AF}
mark{background:linear-gradient(transparent 62%,#FFE600 62%);color:inherit;padding:0 2px}
"""
    kw = None
    if att is not None:
        kw = cards[att[0]][0].rstrip(':')
    body = head() + top + '<div id=cards>%s</div>' % cs + docente_tag(kw) + foot()
    return page(body, 'light', css)


# ------------------------------------------------------------------ approfondimenti
def an_cards(kicker, titolo, items, visibili, parte=None):
    n = len(items)
    cs = ''
    for k, (h, t) in enumerate(items):
        on = k < visibili
        cs += ('<div class="card" style="width:%dpx;padding:34px 36px 36px;opacity:%s;transform:translateY(%dpx);min-height:430px">'
               '<div style="width:56px;height:56px;border-radius:50%%;background:#2060AF;color:#fff;font-weight:800;font-size:30px;display:flex;align-items:center;justify-content:center">%d</div>'
               '<div class=bg2 style="font-size:40px;margin-top:22px">%s</div>'
               '<div style="font-size:30px;line-height:1.38;margin-top:16px;color:#26334f">%s</div></div>'
               % ((1760 - 40 * (n - 1)) // n, 1 if on else 0, 0 if on else 24, k + 1, E(h), E(t)))
    body = (head() + '<div class="kick abs" style="left:80px;top:150px;font-size:24px;color:#2060AF">%s</div>' % E(kicker) +
            '<div class=bg2 style="position:absolute;left:80px;top:196px;font-size:70px;width:1760px">%s</div>' % E(titolo) +
            '<div class=abs style="left:80px;top:360px;width:1760px;display:flex;gap:40px">%s</div>' % cs + foot())
    return page(body, 'light')


def an_timeline(kicker, titolo, items, visibili):
    n = len(items)
    w = 1700
    xs = [140 + k * (w - 80) / max(1, n - 1) for k in range(n)]
    parts = '<div class=abs style="left:140px;top:560px;width:%dpx;height:6px;background:#C9D0DC;border-radius:6px"></div>' % (w - 80)
    if visibili > 0:
        last = xs[min(visibili, n) - 1]
        parts += '<div class=abs style="left:140px;top:560px;width:%dpx;height:6px;background:#2060AF;border-radius:6px"></div>' % (last - 140)
    for k, (d, t) in enumerate(items):
        on = k < visibili
        x = xs[k]
        up = (k % 2 == 0)
        parts += ('<div class=abs style="left:%dpx;top:543px;width:40px;height:40px;margin-left:-20px;border-radius:50%%;background:%s;border:6px solid #fff;box-shadow:0 4px 12px rgba(20,40,90,.3)"></div>' % (x, '#2060AF' if on else '#C9D0DC'))
        top = 330 if up else 620
        cw = 380
        parts += ('<div class="abs" style="left:%dpx;top:%dpx;width:%dpx;opacity:%s;transform:translateY(%dpx)">'
                  '<div class=card style="padding:22px 26px;%s"><div class=bg2 style="font-size:40px;color:#2060AF">%s</div>'
                  '<div style="font-size:30px;line-height:1.3;margin-top:8px">%s</div></div></div>'
                  % (min(max(40, x - cw / 2), 1920 - 40 - cw), top, cw, 1 if on else 0, 0 if on else 20, 'border-color:#FFE600;' if (k == visibili - 1) else '', E(d), E(t)))
    body = (head() + '<div class="kick abs" style="left:80px;top:150px;font-size:24px;color:#2060AF">%s</div>' % E(kicker) +
            '<div class=bg2 style="position:absolute;left:80px;top:196px;font-size:70px;width:1760px">%s</div>' % E(titolo) + parts + foot())
    return page(body, 'light')


def an_stats(kicker, titolo, items, visibili):
    n = len(items)
    cs = ''
    for k, (v, l, frac) in enumerate(items):
        on = k < visibili
        bar = ''
        if frac > 0:
            bar = '<div style="margin-top:26px;height:22px;border-radius:12px;background:#E3E8F1;overflow:hidden"><i style="display:block;height:100%%;width:%d%%;background:#2060AF;border-radius:12px"></i></div>' % int(frac * 100)
        cs += ('<div class=card style="width:%dpx;padding:44px 40px;opacity:%s;transform:translateY(%dpx);min-height:380px">'
               '<div class=bg2 style="font-size:96px;color:#2060AF;line-height:1">%s</div>'
               '<div style="font-size:34px;font-weight:700;margin-top:20px;line-height:1.25">%s</div>%s</div>'
               % ((1760 - 40 * (n - 1)) // n, 1 if on else 0, 0 if on else 24, E(v), E(l), bar))
    body = (head() + '<div class="kick abs" style="left:80px;top:150px;font-size:24px;color:#2060AF">%s</div>' % E(kicker) +
            '<div class=bg2 style="position:absolute;left:80px;top:196px;font-size:70px;width:1760px">%s</div>' % E(titolo) +
            '<div class=abs style="left:80px;top:380px;width:1760px;display:flex;gap:40px">%s</div>' % cs + foot())
    return page(body, 'light')


def an_img(kicker, titolo, img, zoom, caption):
    b = b64(img)
    body = (head() + '<div class="kick abs" style="left:80px;top:150px;font-size:24px;color:#2060AF">%s</div>' % E(kicker) +
            '<div class=bg2 style="position:absolute;left:80px;top:196px;font-size:70px;width:1760px">%s</div>' % E(titolo) +
            '<div class=abs style="left:80px;top:300px;width:1760px;height:650px;overflow:hidden;border-radius:18px;box-shadow:0 12px 36px rgba(20,40,90,.2);background:#fff;display:flex;align-items:center;justify-content:center">'
            '<img src="data:image/png;base64,%s" style="height:%dpx;transform:scale(%.3f)"></div>' % (b, 650, zoom) + foot())
    return page(body, 'light')


# ------------------------------------------------------------------ ripasso, quiz, glossario, fine
def ripasso(titolo, frase, parte=None):
    wave = ''.join('<i style="display:inline-block;width:8px;margin-right:6px;height:%dpx;background:#2060AF;opacity:.8;border-radius:3px;vertical-align:bottom"></i>' % (10 + (k * 37 % 46)) for k in range(34))
    body = dark_bg(
        '<div class="kick abs" style="left:160px;top:330px;font-size:26px;color:#5BD6F0;letter-spacing:.4em">Schema di ripasso</div>'
        '<div class=bg2 style="position:absolute;left:160px;top:390px;font-size:150px;color:#fff">RIPASSO</div>'
        '<div class=bg2 style="position:absolute;left:160px;top:580px;font-size:56px;color:#5BD6F0;width:1500px">%s</div>' % E(titolo) +
        '<div class=abs style="left:160px;top:700px;height:60px">%s</div>' % wave +
        '<div class="glass abs" style="left:160px;top:790px;width:1600px;padding:26px 34px;font-size:32px;line-height:1.4;min-height:130px">%s</div>' % E(frase))
    return page(body, 'dark')


def bande(inner):
    return '<div class=band style="top:0"></div><div class=band style="bottom:0"></div><img class=abs src="%s" style="left:150px;top:130px;height:56px;z-index:6">' % LOGO_W + inner


def quiz(n, titolo):
    body = dark_bg(bande(
        '<div class="abs ghost" style="left:850px;top:120px;font-size:700px">?</div>'
        '<div class="kick abs" style="left:160px;top:300px;font-size:30px;color:#5BD6F0;letter-spacing:.4em">Pausa del video · Quiz</div>'
        '<div class=bg2 style="position:absolute;left:160px;top:370px;font-size:132px;color:#fff">Quiz %d</div>' % n +
        '<div class=bg2 style="position:absolute;left:160px;top:545px;font-size:72px;color:#E3A95C;width:1250px;line-height:1.05">%s</div>' % E(titolo) +
        '<div class="abs" style="left:1380px;top:420px;width:240px;height:240px;border-radius:50%;border:4px solid #5BD6F0"></div>'
        '<div class="abs" style="left:1440px;top:480px;width:120px;height:120px;border-radius:50%;background:#5BD6F0"></div>'
        '<div class="abs" style="left:1480px;top:512px;width:0;height:0;border-left:44px solid #0B1530;border-top:28px solid transparent;border-bottom:28px solid transparent"></div>'
        '<div class="glass abs" style="left:160px;top:740px;padding:24px 46px;font-size:40px;font-weight:700;border-radius:20px">5 domande · per continuare almeno l’80%</div>'
        '<div class=abs style="left:160px;top:880px;font-size:32px;color:#9AA7C2">Rispondi · premi <b style="color:#5BD6F0">Check</b> · poi <b style="color:#5BD6F0">Continua</b></div>'), bande_on=True)
    return page(body, 'dark')


def pausa(titolo_grande, titolo, sotto):
    body = dark_bg(bande(
        '<div class="abs ghost" style="left:850px;top:120px;font-size:700px">?</div>'
        '<div class="kick abs" style="left:160px;top:300px;font-size:30px;color:#5BD6F0;letter-spacing:.4em">Pausa del video · Quiz</div>'
        '<div class=bg2 style="position:absolute;left:160px;top:370px;font-size:132px;color:#fff">%s</div>' % E(titolo_grande) +
        '<div class=bg2 style="position:absolute;left:160px;top:545px;font-size:72px;color:#E3A95C;width:1250px;line-height:1.05">%s</div>' % E(titolo) +
        '<div class="abs" style="left:1380px;top:420px;width:240px;height:240px;border-radius:50%;border:4px solid #5BD6F0"></div>'
        '<div class="abs" style="left:1440px;top:480px;width:120px;height:120px;border-radius:50%;background:#5BD6F0"></div>'
        '<div class="abs" style="left:1480px;top:512px;width:0;height:0;border-left:44px solid #0B1530;border-top:28px solid transparent;border-bottom:28px solid transparent"></div>'
        '<div class="glass abs" style="left:160px;top:760px;padding:22px 42px;font-size:36px;font-weight:700;border-radius:20px">%s</div>' % E(sotto)), bande_on=True)
    return page(body, 'dark')


def glossario(items, visibili):
    cs = ''
    for k, (t, d) in enumerate(items):
        on = k < visibili
        cs += ('<div class=card style="padding:22px 30px;opacity:%s;border-color:%s"><b class=bg2 style="font-size:36px;color:#2060AF">%s</b>'
               '<div style="font-size:30px;line-height:1.3;margin-top:6px;color:#26334f">%s</div></div>' % (1 if on else 0, '#FFE600' if k == visibili - 1 else '#E3E8F1', E(t), E(d)))
    body = (head() + '<div class="kick abs" style="left:80px;top:150px;font-size:24px;color:#2060AF">Glossario</div>'
            '<div class=bg2 style="position:absolute;left:80px;top:196px;font-size:64px">Le parole chiave</div>'
            '<div class=abs style="left:80px;top:300px;width:1760px;display:grid;grid-template-columns:1fr 1fr;gap:20px">%s</div>' % cs + foot())
    return page(body, 'light')


def rf(titolo, items, visibili):
    cs = ''
    for k, (h, t) in enumerate(items):
        on = k < visibili
        cs += ('<div class=card style="padding:30px 38px;opacity:%s;border-color:%s"><b class=bg2 style="font-size:42px;color:#2060AF">%s</b>'
               '<div style="font-size:32px;line-height:1.35;margin-top:10px;color:#26334f">%s</div></div>' % (1 if on else 0, '#FFE600' if k == visibili - 1 else '#E3E8F1', E(h), E(t)))
    body = (head() + '<div class="kick abs" style="left:80px;top:150px;font-size:24px;color:#2060AF">Ripasso finale</div>'
            '<div class=bg2 style="position:absolute;left:80px;top:196px;font-size:64px">%s</div>' % E(titolo) +
            '<div class=abs style="left:80px;top:320px;width:1760px;display:flex;flex-direction:column;gap:22px">%s</div>' % cs + foot())
    return page(body, 'light')


def fine(parte, argomenti, testo):
    lst = ''.join('<div class="glass" style="padding:16px 26px;margin-bottom:14px;font-size:30px;font-weight:600;display:flex;gap:18px;align-items:center;border-radius:16px">'
                  '<span style="width:44px;height:44px;border-radius:50%%;background:#E3A95C;color:#0B1530;font-weight:800;display:flex;align-items:center;justify-content:center;flex:none">%d</span>%s</div>' % (i + 1, E(a)) for i, a in enumerate(argomenti))
    body = dark_bg('<div class="kick abs" style="left:160px;top:320px;font-size:30px;color:#5BD6F0;letter-spacing:.4em">%s</div>' % MATERIA.upper() +
                   '<div class=bg2 style="position:absolute;left:160px;top:380px;font-size:120px;color:#fff">FINE</div>'
                   '<div class=bg2 style="position:absolute;left:160px;top:510px;font-size:120px;color:#E3A95C">PARTE %d</div>' % parte +
                   '<div class=abs style="left:160px;top:720px;width:900px;font-size:30px;line-height:1.35;color:#C9D0DC">%s</div>' % E(testo) +
                   '<div class=abs style="left:1200px;top:330px;width:620px">%s</div>' % lst)
    return page(body, 'dark')


def benvenuto(titolo, parte, argomenti):
    lst = ''.join('<div class="glass" style="padding:16px 26px;margin-bottom:14px;font-size:30px;font-weight:600;display:flex;gap:18px;align-items:center;border-radius:16px">'
                  '<span style="width:44px;height:44px;border-radius:50%%;background:#E3A95C;color:#0B1530;font-weight:800;display:flex;align-items:center;justify-content:center;flex:none">%d</span>%s</div>' % (i + 1, E(a)) for i, a in enumerate(argomenti))
    body = dark_bg('<div class="kick abs" style="left:160px;top:300px;font-size:28px;color:#E3A95C;letter-spacing:.38em">%s · %s · Parte %d</div>' % (MATERIA, DOCENTE, parte) +
                   '<div class=bg2 style="position:absolute;left:160px;top:370px;font-size:104px;color:#fff;width:1100px">%s</div>' % E(titolo) +
                   '<div class=abs style="left:1300px;top:330px;width:520px">%s</div>' % lst)
    return page(body, 'dark')
