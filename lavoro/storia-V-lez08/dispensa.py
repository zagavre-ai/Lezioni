#!/usr/bin/env python3
# Dispensa A4 orizzontale identica al video (stesse slide, stesso ordine) con strato di testo invisibile; PDF delle mappe con copertina «MAPPE».
import os, sys, json, subprocess, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
import lib_slide as L, covers, build_prof as B, kore
O = '/tmp/w/work/out'
PW, PH = landscape(A4)
def pagina(c, png, testo):
    im = Image.open(png).convert('RGB'); w = PW; h = PW * im.height / im.width; y = (PH - h) / 2
    c.drawImage(png, 0, y, w, h)
    t = c.beginText(20, PH - 30); t.setTextRenderMode(3); t.setFont('Helvetica', 10)
    for r in testo.split('\n'):
        for ch in [r[i:i + 110] for i in range(0, max(1, len(r)), 110)]: t.textLine(ch.encode('latin-1', 'replace').decode('latin-1'))
    c.drawText(t); c.showPage()
def slide_larga(si, top, win, pag):
    im = L.cornice(pag=pag, riquadro=False); d = ImageDraw.Draw(im)
    d.text((80, 144), f'{top:02d} · {B.NOMI[top]}'.upper(), font=L.font('Figtree-ExtraBold.ttf', 26), fill=L.TEL)
    ft = L.font('BricolageGrotesque-ExtraBold.ttf', 58); y = 182
    for r in L.wrap(d, B.TIT[si], ft, 1760): d.text((80, y), r, font=ft, fill=L.BLU); y += 68
    d.rounded_rectangle((80, y + 4, 165, y + 10), 3, fill=L.TEL); y += 40
    f = L.font('Figtree-Medium.ttf', 40)
    for i in win:
        txt = B.cardtext(si, i); righe = L.wrap(d, txt, f, 1760 - 90); h = len(righe) * 60 + 44
        L.ombra(im, (80, y, 1840, y + h), 18, 6, 14, 22); d = ImageDraw.Draw(im)
        d.rounded_rectangle((80, y, 1840, y + h), 18, fill=(246, 248, 252), outline=(220, 226, 236), width=2)
        for k, r in enumerate(righe): d.text((144, y + 22 + k * 60), r, font=f, fill=L.BLU)
        y += h + 22
    return im.convert('RGB')
def costruisci(out_pdf, parti):
    """parti: lista di (n, timeline, video_finale)"""
    c = canvas.Canvas(out_pdf, pagesize=(PW, PH)); c.setTitle('Storia · Il dopoguerra italiano (1919-1925) e il fascismo'); n = 0
    tmp = O + '/disp'; os.makedirs(tmp, exist_ok=True)
    pag = covers.cover(False); p = tmp + '/cover.png'; pag.save(p); pagina(c, p, 'STORIA VIDEOLEZIONE\n' + covers.TITOLO)
    p = tmp + '/arg.png'; covers.argomenti(2).convert('RGB').save(p); pagina(c, p, 'Di cosa parliamo\n' + '\n'.join(covers.ARG))
    for pn, tl, vid in parti:
        for nome, t0, d, *_ in tl:
            if nome == 'D0': continue
            if nome.startswith('D') and nome[1:].isdigit():
                top = int(nome[1:]); st = json.load(open(f'{O}/D{top}_stati.json')); vis = set()
                for s in st:
                    key = (s['img'], tuple(s['win']) if s['win'] else None, s['si'])
                    if key in vis: continue
                    vis.add(key); n += 1; p = f'{tmp}/s{top}_{n}.png'
                    if s['img']:
                        L_ = B.render(s['si'], top, [], None, n, s['img']); L_.save(p); pagina(c, p, B.TIT[s['si']])
                    else:
                        slide_larga(s['si'], top, s['win'], n).save(p); pagina(c, p, B.TIT[s['si']] + '\n' + '\n'.join(B.cardtext(s['si'], i) for i in s['win']))
            elif nome[:2] in ('AN', 'MA', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'GL', 'RF', 'CM', 'SP') or re.match(r'^R\d', nome):
                if nome == 'MAPF': continue
                p = f'{tmp}/{pn}_{nome}.png'; tt = max(0.5, d - 0.9)
                subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{t0 + tt:.2f}', '-i', vid, '-frames:v', '1', p], check=True)
                pagina(c, p, nome)
    c.save()
def mappe_pdf(out_pdf):
    c = canvas.Canvas(out_pdf, pagesize=(PW, PH)); c.setTitle('Storia · Il dopoguerra italiano (1919-1925) e il fascismo · MAPPE'); tmp = O + '/disp'
    im = covers.cover(False).convert('RGBA'); d = ImageDraw.Draw(im)
    d.text((1840, 150), 'MAPPE', font=L.font('BricolageGrotesque-ExtraBold.ttf', 110), fill=L.TEL, anchor='ra')
    p = tmp + '/cover_mappe.png'; im.convert('RGB').save(p); pagina(c, p, 'MAPPE\nSTORIA\n' + covers.TITOLO)
    for k in ('M1', 'M2', 'M3'): pagina(c, f'{O}/{k}_finale.png', 'Mappa ' + k[1])
    c.save()
if __name__ == '__main__':
    mappe_pdf(sys.argv[1])
