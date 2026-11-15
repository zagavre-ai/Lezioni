#!/usr/bin/env python3
"""Inserisce le mappe nella dispensa A4: 'Mappa della lezione' dopo la copertina, una mappa per argomento alla fine della sua sezione.
uso: dispensa.py dispensa.pdf out.pdf cartella_an "MF2" "2:P1_AN2,3:P1_AN4,17:P1_AN7,..."  (pagina:mappa = dopo quella pagina, 1-based)"""
import sys, pypdf
src, out, an, mf, spec = sys.argv[1:6]
r = pypdf.PdfReader(src); w = pypdf.PdfWriter()
dopo = {int(a): b for a, b in (x.split(':') for x in spec.split(','))}
def add(n):
    w.append(pypdf.PdfReader(f'{an}/{n}/mappa_dispensa.pdf'))
for i, p in enumerate(r.pages, 1):
    w.add_page(p)
    if i == 1: add(mf)
    if i in dopo: add(dopo[i])
w.write(out); print(out, len(r.pages), '->', len(w.pages))
