#!/usr/bin/env python3
# Copertina, slide degli argomenti, spiegone, compiti. Titolo esatto della lezione.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
import lib_slide as L
F = L.font; BLU = L.BLU; TEL = L.TEL
TITOLO = 'Il dopoguerra italiano (1919-1925) e il fascismo'
ARG = ['Il contesto del dopoguerra e il Biennio rosso', 'Vittoria mutilata, Fiume e le elezioni del 1919', 'La nascita del fascismo e lo squadrismo',
       'Il ritorno di Giolitti e le elezioni del 1921', 'La Marcia su Roma e la conquista del potere', 'Il primo governo fascista e la svolta autoritaria',
       'Il delitto Matteotti e il passaggio alla dittatura']
def cover(riquadro, pag=1, n_arg=7, parte=1):
    im = L.cornice(pag=pag, riquadro=riquadro); d = ImageDraw.Draw(im)
    d.text((80, 168), 'STORIA · VIDEOLEZIONE', font=F('Figtree-ExtraBold.ttf', 30), fill=TEL)
    ft = F('BricolageGrotesque-ExtraBold.ttf', 78); righe = L.wrap(d, TITOLO, ft, 1300); y = 215
    for r in righe: d.text((80, y), r, font=ft, fill=BLU); y += 90
    d.rounded_rectangle((80, y + 6, 165, y + 12), 3, fill=TEL); y += 50
    h = 70 + 48 * n_arg
    L.ombra(im, (80, y, 1380, y + h), 22, 8, 18, 40); d = ImageDraw.Draw(im)
    d.rounded_rectangle((80, y, 1380, y + h), 22, fill=(247, 249, 253), outline=(224, 230, 240), width=2)
    d.text((115, y + 22), 'ARGOMENTI', font=F('Figtree-ExtraBold.ttf', 26), fill=TEL)
    for i, a in enumerate(ARG[:n_arg]):
        yy = y + 70 + 48 * i
        d.ellipse((118, yy + 10, 134, yy + 26), fill=TEL); d.text((152, yy), a, font=F('Figtree-Medium.ttf', 32), fill=BLU)
    return im.convert('RGB')
def argomenti(pag=2):
    im = L.cornice(pag=pag, riquadro=True); d = ImageDraw.Draw(im)
    d.text((80, 144), 'STORIA · VIDEOLEZIONE', font=F('Figtree-ExtraBold.ttf', 26), fill=TEL)
    d.text((80, 190), 'Di cosa parliamo', font=F('BricolageGrotesque-ExtraBold.ttf', 64), fill=BLU); d.rounded_rectangle((80, 276, 165, 282), 3, fill=TEL)
    y = 320
    for i, a in enumerate(ARG):
        L.ombra(im, (80, y, 1380, y + 78), 14, 4, 10, 25); d = ImageDraw.Draw(im)
        d.rounded_rectangle((80, y, 1380, y + 78), 14, fill=(247, 249, 253), outline=(224, 230, 240), width=2)
        d.ellipse((104, y + 20, 142, y + 58), fill=TEL); d.text((123, y + 39), str(i + 1), font=F('Figtree-ExtraBold.ttf', 26), fill=(255, 255, 255), anchor='mm')
        d.text((164, y + 18), a, font=F('Figtree-SemiBold.ttf', 36), fill=BLU); y += 92
    return im.convert('RGB')
def compiti_png(domande, pag):
    """scheda dei compiti del docente: domande intere, testo grande"""
    im = L.cornice(pag=pag, riquadro=False); d = ImageDraw.Draw(im)
    d.text((80, 144), 'COMPITI', font=F('Figtree-ExtraBold.ttf', 26), fill=TEL)
    d.text((80, 182), 'Rispondi con parole tue', font=F('BricolageGrotesque-ExtraBold.ttf', 58), fill=BLU); d.rounded_rectangle((80, 262, 165, 268), 3, fill=TEL)
    y = 300
    for i, q in enumerate(domande):
        righe = L.wrap(d, q, F('Figtree-Medium.ttf', 38), 1650); h = len(righe) * 54 + 36
        L.ombra(im, (80, y, 1840, y + h), 16, 5, 12, 25); d = ImageDraw.Draw(im)
        d.rounded_rectangle((80, y, 1840, y + h), 16, fill=(247, 249, 253), outline=(224, 230, 240), width=2)
        d.ellipse((100, y + 18, 136, y + 54), fill=TEL); d.text((118, y + 36), str(i + 1), font=F('Figtree-ExtraBold.ttf', 24), fill=(255, 255, 255), anchor='mm')
        for k, r in enumerate(righe): d.text((160, y + 14 + k * 54), r, font=F('Figtree-Medium.ttf', 38), fill=BLU)
        y += h + 18
    return im.convert('RGB')
