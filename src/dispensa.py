# Dispensa A4 orizzontale identica alle slide del video (senza riquadro del prof) + testo invisibile; PDF delle mappe a parte
import sys, os, json, subprocess
sys.path.insert(0, '/tmp/w/build')
import lib
lib.DRAW_CAM = False
import pieces as P, content as K
from PIL import Image, ImageDraw
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4, landscape

pdfmetrics.registerFont(TTFont('Fig', '/root/.fonts/Figtree-Regular.ttf'))
PW, PH = landscape(A4)   # 841.89 x 595.28
OUT = '/tmp/w/build/consegna'; os.makedirs(OUT, exist_ok=True)

def approf_page(i):
    a = K.APPROF[f'A{i}']; page = P.pg(f'APP{i}')
    im = lib.base('Approfondimento', page, False); lib.title(im, a['titolo'], 186, maxw=1700)
    src = P.work_image(a['img'][0]); asp = src.width / src.height
    ph_h = 640; ph_w = min(int(ph_h * asp), 900); ph_h = int(ph_w / asp)
    ph = src.resize((ph_w, ph_h), Image.LANCZOS); lib.paste_photo(im, ph, 80, 300)
    x = 80 + ph_w + 60; y = 300
    for txt, si in a['punti']:
        hh = lib.card_height(None, txt, 1840 - x, 38, 50); lib.draw_card(im, x, y, 1840 - x, None, txt, 'n', 38, 50); y += hh + 16
    return im

def gloss_pages():
    pages = [[0, 1, 2], [3, 4, 5], [6, 7], [8, 9]]; out = []
    for pi in range(4):
        im = lib.base('Glossario', P.pg(f'gloss{pi}'), False); y = lib.title(im, 'Glossario', 186, maxw=1700)
        for k in pages[pi]:
            t, d = K.GLOSSARIO[k]; h = lib.draw_card(im, 80, y, 1760, t, d, 'n'); y += h + 22
        out.append(im)
    return out

def compiti_pages():
    out = []
    for pi in range(3):
        im = lib.base('Compiti', P.pg(f'compiti{pi}'), False); y = lib.title(im, 'Compiti', 186, maxw=1700)
        if pi < 2:
            for k in (2 * pi, 2 * pi + 1): h = lib.draw_card(im, 80, y, 1760, 'Compito %d' % (k + 1), K.COMPITI[k], 'n'); y += h + 22
        else:
            h = lib.draw_card(im, 80, y, 1760, None, 'Svolgi i compiti qui sotto e premi «Consegna»: arrivano al docente nel tuo quaderno dei compiti.', 'n', 44, 58)
        out.append(im)
    return out

def pages():
    L = []   # (immagine, testi)
    def grab(im): t = list(lib.REC); lib.REC.clear(); L.append((im, t))
    lib.REC.clear()
    grab(P.cover_img(True, 5, None))
    grab(P.build_agenda_im())
    for i, n in enumerate(['T1', 'T2', 'T3', 'T4', 'T5'], 1):
        Pz = K.PEZZI_PROF[n]; label = Pz['label']
        for si, sc in enumerate(Pz['scene']):
            page = P.pg(f'{n}_{si}')
            if sc[0] == 'cards': grab(P.slide_cards(sc[1], None, label, page))
            else: grab(P.slide_img(sc[1], sc[3], False, label, page))
        grab(approf_page(i))
    for im in gloss_pages(): grab(im)
    for im in compiti_pages(): grab(im)
    return L

def pdf_from(L, path, titolo):
    s = PW / 1920.0; off = (PH - 1080 * s) / 2
    c = canvas.Canvas(path, pagesize=(PW, PH)); c.setTitle(titolo); c.setAuthor("Centro Studi Telesio"); c.setSubject("Storia dell'arte V")
    tmpd = '/tmp/w/build/work/disp'; os.makedirs(tmpd, exist_ok=True)
    for k, (im, texts) in enumerate(L):
        jp = f'{tmpd}/p{k:02d}.jpg'; im.convert('RGB').save(jp, quality=90)
        c.drawImage(jp, 0, off, width=PW, height=1080 * s)
        t = c.beginText(); t.setTextRenderMode(3); t.setFont('Fig', 8)
        texts = sorted(texts, key=lambda r: 2 if r[2] >= 1000 else (1 if r[1] >= 1428 else 0))
        for txt, x, y, size in texts:
            t.setTextOrigin(x * s, PH - (off + (y + size) * s)); t.textLine(txt)
        c.drawText(t); c.showPage()
    c.save()

if __name__ == '__main__':
    L = pages()
    pdf_from(L, f'{OUT}/Dispensa_Storia_arte_V_Simbolismo_e_Art_Nouveau.pdf', 'Storia dell\'arte V · Simbolismo e Art Nouveau')
    print('dispensa pagine', len(L))

def mappe_pdf():
    """PDF delle mappe: copertina identica a quella delle slide + «MAPPE», poi le due mappe (A4 orizzontale)"""
    from PIL import ImageFont
    lib.REC.clear(); im = P.cover_img(True, 5, None)
    d = ImageDraw.Draw(im); d.rounded_rectangle((80, 196, 460, 262), 16, fill=lib.YEL)
    d.text((104, 200), 'MAPPE', font=lib.font('t', 56), fill=lib.NAVY); lib.rec('MAPPE', 104, 200, 56)
    texts = list(lib.REC); lib.REC.clear()
    pdf_from([(im, texts)], '/tmp/w/build/work/mappe_cover.pdf', "Storia dell'arte V · Mappe")
    out = f'{OUT}/Mappe_Storia_arte_V_Simbolismo_e_Art_Nouveau.pdf'
    subprocess.run(['pdfunite', '/tmp/w/build/work/mappe_cover.pdf', '/tmp/w/build/pdf/mappa_M1.pdf', '/tmp/w/build/pdf/mappa_M2.pdf', out], check=True)
    print(out)
