#!/usr/bin/env python3
# Rendering slide nel modello Spagnolo: fondo bianco, card 40 px, riquadro prof 4:3 (412x309 a 1428,148), fascia gialla.
import os, re
from PIL import Image, ImageDraw, ImageFont, ImageFilter
F = '/home/user/Lezioni/kit/caratteri/'
W, H = 1920, 1080
BLU = (11, 21, 48); TEL = (32, 96, 175); GIA = (255, 230, 0)
def font(n, s): return ImageFont.truetype(F + n, s)
def wrap(d, txt, f, maxw):
    out = [];
    for par in txt.split('\n'):
        cur = ''
        for w in par.split():
            t = (cur + ' ' + w).strip()
            if d.textlength(t, font=f) <= maxw: cur = t
            else: out.append(cur); cur = w
        out.append(cur)
    return out
def ombra(im, box, r=18, off=10, blur=22, alpha=60):
    sh = Image.new('RGBA', im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(sh)
    x0, y0, x1, y1 = box; d.rounded_rectangle((x0, y0 + off, x1, y1 + off), r, fill=(90, 100, 120, alpha))
    sh = sh.filter(ImageFilter.GaussianBlur(blur)); im.alpha_composite(sh)
def logo(im):
    p = '/home/user/Lezioni/kit/modello_spagnolo/logo.png'
    d = ImageDraw.Draw(im); d.text((80, 62), 'centro studi', font=font('Figtree-Medium.ttf', 22), fill=TEL)
    d.text((80, 84), 'TELESIO', font=font('Figtree-ExtraBold.ttf', 26), fill=TEL)
def cornice(materia='STORIA', pag=1, riquadro=True, nome='Giorgio Mazzotti', ruolo='PROF. DI STORIA'):
    im = Image.new('RGBA', (W, H), (255, 255, 255, 255)); d = ImageDraw.Draw(im)
    logo(im); d.line((80, 124, 1840, 124), fill=(226, 230, 238), width=2)
    d.line((80, 981, 1840, 981), fill=(226, 230, 238), width=2)
    d.text((80, 1000), f'{materia}', font=font('Figtree-Bold.ttf', 22), fill=TEL)
    d.text((1840, 1000), f'Pagina {pag}', font=font('Figtree-Bold.ttf', 22), fill=TEL, anchor='ra')
    if riquadro:
        ombra(im, (1428, 148, 1840, 457), 20)
        d = ImageDraw.Draw(im); d.rounded_rectangle((1428, 148, 1840, 457), 20, fill=(235, 238, 244))  # il video prof si sovrappone nel montaggio
        # fascia gialla leggermente inclinata
        band = Image.new('RGBA', (440, 120), (0, 0, 0, 0)); bd = ImageDraw.Draw(band)
        bd.rounded_rectangle((10, 10, 430, 100), 8, fill=GIA)
        bd.text((30, 24), nome, font=font('BricolageGrotesque-ExtraBold.ttf', 32), fill=BLU)
        bd.text((30, 66), ruolo, font=font('Figtree-Bold.ttf', 22), fill=BLU)
        band = band.rotate(2, resample=Image.BICUBIC, expand=False)
        ombra(im, (1428, 470, 1840, 565), 8, 6, 10, 45)
        im.alpha_composite(band, (1418, 468))
    return im
def card(im, x, y, w, testo, attiva, size=40, lh=1.5):
    f = font('Figtree-Medium.ttf', size); d = ImageDraw.Draw(im)
    righe = wrap(d, testo, f, w - 90)
    h = int(len(righe) * size * lh) + 44
    ombra(im, (x, y, x + w, y + h), 18, 6, 14, 40 if attiva else 22)
    d = ImageDraw.Draw(im)
    if attiva:
        d.rounded_rectangle((x, y, x + w, y + h), 18, fill=(255, 251, 214), outline=GIA, width=6)
        d.ellipse((x + 22, y + 26, x + 42, y + 46), fill=GIA, outline=(200, 170, 0), width=2)
        col = BLU
    else:
        d.rounded_rectangle((x, y, x + w, y + h), 18, fill=(246, 248, 252), outline=(220, 226, 236), width=2)
        col = (92, 102, 128)
    for i, r in enumerate(righe): d.text((x + 64, y + 22 + int(i * size * lh)), r, font=f, fill=col)
    return h
def slide(titolo, kicker, cards, attiva, pag, parole=None, riquadro=True):
    """cards: lista di frasi intere (max 3); attiva: indice acceso o None"""
    im = cornice(pag=pag, riquadro=riquadro); d = ImageDraw.Draw(im)
    d.text((80, 160), kicker.upper(), font=font('Figtree-ExtraBold.ttf', 26), fill=TEL)
    ft = font('BricolageGrotesque-ExtraBold.ttf', 64); righe = wrap(d, titolo, ft, 1250)[:2]
    y = 205
    for r in righe: d.text((80, y), r, font=ft, fill=BLU); y += 76
    d.rounded_rectangle((80, y + 6, 165, y + 12), 3, fill=TEL); y += 40
    for i, c in enumerate(cards):
        h = card(im, 80, y, 1300, c, attiva == i); y += h + 22
    if y > 975: raise SystemExit(f'slide troppo piena: y={y} {titolo}')
    if parole:
        d = ImageDraw.Draw(im); d.text((1428, 620), 'PAROLE CHIAVE', font=font('Figtree-ExtraBold.ttf', 24), fill=TEL)
        yy = 664
        for p in parole[:5]:
            d.rounded_rectangle((1428, yy, 1840, yy + 48), 10, fill=(255, 247, 150)); d.text((1446, yy + 8), p, font=font('Figtree-Bold.ttf', 28), fill=BLU); yy += 60
    return im.convert('RGB')
if __name__ == '__main__':
    t = ['Un Paese impoverito dal conflitto: al termine della Grande Guerra, l\'Italia si ritrova in una profonda crisi economica, caratterizzata da un altissimo deficit pubblico e da una violenta inflazione che dimezza il potere d\'acquisto dei salari.',
         'Le pesanti conseguenze sociali: il drastico blocco delle commesse statali belliche costringe moltissime aziende alla chiusura improvvisa, provocando un\'ondata di disoccupazione che arriva a colpire oltre due milioni di persone.']
    slide("Il contesto del Dopoguerra e la crisi del \"Biennio Rosso\" (1919-1920)", "01 · Il Biennio rosso", t[:1], 0, 3, ["deficit", "inflazione", "disoccupazione"]).save("/tmp/w/work/prova_slide.png")
