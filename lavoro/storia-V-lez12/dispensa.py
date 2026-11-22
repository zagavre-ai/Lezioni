# -*- coding: utf-8 -*-
# Dispensa A4 orizzontale (stesse slide del video, senza riquadro/nome del docente) con strato di testo invisibile; PDF delle mappe a parte.
import os, sys, json
sys.path.insert(0, '/home/user/Lezioni/lavoro/storia-V-lez12')
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
import rend, slide, contenuti as C, piano as P, inserti as I
from PIL import Image
W = '/home/user/w12'; R = f'{W}/consegna'; D = f'{W}/disp'; os.makedirs(D, exist_ok=True)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('Fig', '/root/.fonts/Figtree-Regular.ttf'))

def pagina_pdf(c, png, testi):
    pw, ph = landscape(A4); im = Image.open(png); r = pw / im.width; h = im.height * r
    c.drawImage(png, 0, (ph - h) / 2, pw, h)
    t = c.beginText(20, ph - 20); t.setTextRenderMode(3); t.setFont('Fig', 8)
    for line in testi:
        for part in [line[i:i + 150] for i in range(0, len(line), 150)] or ['']:
            t.textLine(part)
    c.drawText(t); c.showPage()

def cover(mappe=False):
    h = f'<img class="logo" src="file://{rend.LOGO}"><div class="hr" style="top:125px"></div><div class="lab">STORIA · VIDEOLEZIONE</div>'
    if mappe: h += f'<div style="position:absolute;left:80px;top:250px;font:800 70px \'Bricolage Grotesque\';color:{rend.BLU};letter-spacing:6px">MAPPE</div>'
    top = 360 if mappe else 230
    h += f'<div style="position:absolute;left:80px;top:{top}px;width:1500px;font:800 120px/1.05 \'Bricolage Grotesque\';color:{rend.NOTTE}">{rend.esc(C.TITOLO_MAIUSC)}</div><div style="position:absolute;left:80px;top:{top+260}px;width:90px;height:8px;background:{rend.BLU}"></div>'
    h += '<div class="hr" style="top:981px"></div><div class="foot"><span>STORIA</span><span>Pagina 1</span></div>'
    f = f'{D}/cover_{"mappe" if mappe else "disp"}.png'; rend.png(rend.doc(h), f, name='dcov.html'); return f

def pagine_prof(k, pag0):
    """pagine (numero, png, testi) delle slide dell'argomento k, nella numerazione del video"""
    T = P.TOP[k]; segs = slide.segmenti(k); out = []; usate = {}; pag = pag0
    for t0, t1, tp, w, a in segs:
        if t1 - t0 < 0.05 or w['id'] in usate: continue
        usate[w['id']] = pag; png = f'{D}/p{k}_{w["id"]}.png'
        titolo = P.SLIDE_TITOLO[k]; lab = f"{k:02d} · {T['titolo']}"
        body = rend.telaio(lab, titolo, pag, con_prof=False, parole=C.CHIAVE[k])
        testi = [lab, titolo]
        if tp == 'fin':
            y = 290 if len(titolo) <= 38 else 340
            for n, j in enumerate(w['cards'], 1):
                ref = T['cards'][j]; ttl, txt = C.SLIDES[ref[0]][ref[1]]
                body += rend.card_html(n, ttl, txt, y, 'norm'); y += slide.altezza(ref) + slide.GAP
                testi += [ttl, txt[:1].upper() + txt[1:]]
            testi += ['Parole chiave: ' + ', '.join(C.CHIAVE[k])]
            rend.png(rend.doc(body), png, name=f'dp{k}_{w["id"]}.html')
        else:
            slide.render_img(k, w['chiave'], w['cap'], pag, png)
            for t_, x_ in slide.IMGCARDS.get(w['chiave'], []): testi += [t_, x_]
            testi += [w['cap']]
        out.append((pag, png, testi)); pag += 1
    return out, pag

def crea(parte, topics, finali):
    base = {}; p = 3
    for k in range(1, 7): base[k] = p; p += len({w['id'] for *_, w, a in slide.segmenti(k)}) + 2
    c = canvas.Canvas(f'{R}/Storia_Lez12_Parte{parte}_dispensa.pdf', pagesize=landscape(A4))
    c.setTitle(f"Storia · {C.TITOLO}"); c.setAuthor('Centro Studi Telesio')
    pagina_pdf(c, cover(), ['STORIA · VIDEOLEZIONE', C.TITOLO_MAIUSC])
    for k in topics:
        pg, _ = pagine_prof(k, base[k])
        for n, png, testi in pg: pagina_pdf(c, png, testi)
        a = f'{W}/pezzi/app{k}/ultimo.png'; t, pts = C.APPROF_SCHERMO[k]
        pagina_pdf(c, a, ['Approfondimento', t] + pts + [C.VOCI[f'A{k}_APPROF']])
        pagina_pdf(c, f'{W}/pezzi/pil{k}/ultimo.png', ['Ripasso', P.TOP[k]['titolo']] + I.PILLOLA[k])
    for nome, testi in finali: pagina_pdf(c, f'{W}/pezzi/{nome}/ultimo.png', testi)
    c.save()

def mappe():
    c = canvas.Canvas(f'{R}/Storia_Lez12_mappe.pdf', pagesize=landscape(A4)); c.setTitle('Storia · Mappe')
    pagina_pdf(c, cover(True), ['MAPPE', 'STORIA · VIDEOLEZIONE', C.TITOLO_MAIUSC])
    for k in (2, 4, 6):
        m = I.MAPPE[k]; testi = [m['titolo']] + [' / '.join(n[1]) for n in m['nodi']] + [x[2] for x in m['archi'] if x[2]] + ([m['nota']] if m['nota'] else [])
        pagina_pdf(c, f'{W}/pezzi/mappa{k}/ultimo.png', testi)
    c.save()

if __name__ == '__main__':
    crea(1, (1, 2, 3, 4), [])
    crea(2, (5, 6), [('glossario', ['Glossario'] + [f'{a}: {b}' for a, b in C.GLOSSARIO]), ('ripasso', ['Ripasso finale'] + I.RIEP)])
    mappe()
    print('dispense fatte')
