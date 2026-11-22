# -*- coding: utf-8 -*-
# Slide del prof «a finestra»: al massimo 3 card intere, la card in corso si accende quando il prof comincia la frase.
import os, json, hashlib
from PIL import Image, ImageFilter
import rend, contenuti as C, piano as P
W = rend.WORK
MAXFIN = 165.0      # una finestra non resta uguale oltre ~2,7 minuti
GAP = 14

def immagine_alta(chiave):
    """Immagini del prof (PDF) ingrandite 3x con Lanczos + pulizia e nitidezza leggere."""
    src = {'asia': 'p-005.jpg', 'franco': 'p-008.jpg', 'spagna': 'p-011.jpg', 'europa': 'p-014.jpg'}[chiave]
    out = f'{W}/img/hi_{chiave}.png'
    if not os.path.exists(out):
        im = Image.open(f'{W}/img/{src}').convert('RGB')
        im = im.filter(ImageFilter.MedianFilter(3))
        im = im.resize((im.width * 3, im.height * 3), Image.LANCZOS)
        im = im.filter(ImageFilter.UnsharpMask(radius=2.2, percent=90, threshold=2))
        im.save(out)
    return out

_alt = {}
def altezza(ref):
    if ref not in _alt:
        t, s = C.SLIDES[ref[0]][ref[1]]
        _alt[ref] = rend.misura_card(t, s)
    return _alt[ref]

def disponibile(titolo):
    return 685 if len(titolo) <= 38 else 625

def scegli(cards, i0, titolo):
    """indici di card (a partire da i0) che entrano nella schermata, al massimo 3"""
    av = disponibile(titolo); sel = []; tot = 0
    for j in range(i0, min(i0 + 3, len(cards))):
        h = altezza(cards[j]) + (GAP if sel else 0)
        if tot + h > av: break
        sel.append(j); tot += h
    if not sel: sel = [i0]
    if len(sel) == 1 and i0 + 1 >= len(cards) and i0 > 0:   # ultima card: affiancala alla precedente
        sel = [i0 - 1, i0]
    return sel

def segmenti(k):
    """[(t0,t1,tipo,finestra|immagine,card_accesa)] in tempo ORIGINALE; finestra = dict(cards,t0,id)"""
    T = P.TOP[k]; cards = T['cards']; lit = T['lit']; imm = T['imm']; t0, t1 = T['t0'], T['t1']
    E = sorted(set([x[0] for x in lit] + [x for a, b, *_ in imm for x in (a, b)]))
    def acceso(t):
        a = None
        for tt, ix in lit:
            if tt <= t + 1e-6: a = ix
        return a
    segs = []; t = t0; win = None; nid = 0
    while t < t1 - 1e-6:
        im = next(((a, b, c, d) for a, b, c, d in imm if a - 1e-6 <= t < b - 1e-6), None)
        if im:
            nid += 1
            segs.append((t, min(im[1], t1), 'img', dict(id=nid, chiave=im[2], cap=im[3]), None)); t = min(im[1], t1); win = None
            continue
        a = acceso(t)
        if win is None or (a is not None and a not in win['cards']) or (t - win['t0'] >= MAXFIN - 1e-6):
            i0 = a if a is not None else (win['cards'][0] if win else 0)
            nuovo = scegli(cards, i0, T['titolo'])
            if win is not None and nuovo == win['cards']:
                alt = [i0 - 1, i0] if i0 > 0 else nuovo
                if alt != nuovo: nuovo = alt
            nid += 1; win = dict(id=nid, cards=nuovo, t0=t)
        nxt = [e for e in E if e > t + 1e-6]
        nb = min(nxt + [win['t0'] + MAXFIN, t1])
        # un'immagine che comincia dopo: già nei punti di E
        segs.append((t, nb, 'fin', win, a)); t = nb
    return segs

def render_stato(k, st_lit, win, pagina, nome):
    T = P.TOP[k]; cards = T['cards']
    titolo = T['titolo'] if False else P.SLIDE_TITOLO[k]
    lab = f"{k:02d} · {T['titolo']}"
    body = rend.telaio(lab, titolo, pagina, parole=C.CHIAVE[k])
    y = 290 if len(titolo) <= 38 else 340
    for n, j in enumerate(win['cards'], 1):
        ref = cards[j]; ttl, txt = C.SLIDES[ref[0]][ref[1]]
        h = altezza(ref)
        stato = 'norm' if st_lit is None else ('on' if j == st_lit else 'off')
        body += rend.card_html(n, ttl, txt, y, stato); y += h + GAP
    return rend.png(rend.doc(body), nome, name=os.path.basename(nome) + '.html')

IMGCARDS = {
 'asia': [("Leggere la carta", "La «Lunga marcia» (1934-1935) e l’invasione giapponese (1937)"), ("Nella legenda", "Il percorso della marcia e il territorio cinese nel 1936")],
 'spagna': [("Leggere la carta", "La guerra di Spagna (1936-1939)"), ("Territori dei nazionalisti", "Dicembre 1936, dicembre 1937, dicembre 1938, febbraio 1939, marzo 1939")],
}
def render_img(k, chiave, cap, pagina, nome):
    T = P.TOP[k]; titolo = P.SLIDE_TITOLO[k]
    body = rend.telaio(f"{k:02d} · {T['titolo']}", titolo, pagina, parole=C.CHIAVE[k])
    hi = immagine_alta(chiave); im = Image.open(hi)
    cards = IMGCARDS.get(chiave)
    ax, ay, aw, ah = (80, 290, 780, 640) if cards else (80, 290, 1305, 640)
    r = min(aw / im.width, ah / im.height); w, h = int(im.width * r), int(im.height * r)
    ox = ax + (aw - w) // 2; oy = ay + (ah - h) // 2
    body += f'<div class="fig" style="left:{ax}px;top:{ay}px;width:{aw}px;height:{ah}px"><img src="file://{hi}" style="width:{w}px;height:{h}px"></div>'
    if cards:
        y = 290
        for n, (t_, x_) in enumerate(cards, 1):
            body += rend.card_html(n, t_, x_, y, 'norm').replace('class="card ', 'style="width:500px;left:885px" class="card ').replace('style="width:500px;left:885px" class="card  style="top:', 'class="card " style="width:500px;left:885px;top:') if False else (
                f'<div class="card" style="top:{y}px;left:885px;width:500px;padding-left:80px"><div class="n">{n}</div><div class="t" style="font-size:28px">{rend.esc(t_)}</div><div class="s" style="font-size:34px">{rend.esc(x_)}</div></div>')
            y += 300 if n == 1 else 0
    else:
        body += f'<div class="cap" style="left:80px;top:936px;width:1305px;font-size:26px">{rend.esc(cap)}</div>'
    return rend.png(rend.doc(body), nome, name=os.path.basename(nome) + '.html')
