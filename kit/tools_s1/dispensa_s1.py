#!/usr/bin/env python3
"""Dispensa A4 (testo vero, leggibile in bianco e nero) con le mappe concettuali.
uso: python3 dispensa_s1.py spec.py slide.pdf cartella_lavoro uscita.pdf
Richiede in cartella_lavoro/mappe/ i PDF delle mappe: map1..map6.pdf e lez.pdf (mappa dell'intera lezione)."""
import sys, os, importlib.util, io
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfWriter, PdfReader

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, QUI)
from slide_testo import struttura
sp = importlib.util.spec_from_file_location('spec', sys.argv[1])
S = importlib.util.module_from_spec(sp)
sp.loader.exec_module(S)
PDF, W, OUT = sys.argv[2], sys.argv[3], sys.argv[4]
F = '/home/user/Lezioni/kit/tools/mappa_font/'
pdfmetrics.registerFont(TTFont('FG', F + 'Figtree-Regular.ttf'))
pdfmetrics.registerFont(TTFont('FGB', F + 'Figtree-Bold.ttf'))
pdfmetrics.registerFont(TTFont('BG', F + 'BricolageGrotesque-ExtraBold.ttf'))
BLU = colors.HexColor('#2060AF')
NOTTE = colors.HexColor('#0B1530')
H1 = ParagraphStyle('h1', fontName='BG', fontSize=26, leading=30, textColor=NOTTE, spaceAfter=6)
H2 = ParagraphStyle('h2', fontName='BG', fontSize=17, leading=21, textColor=NOTTE, spaceBefore=10, spaceAfter=4)
K = ParagraphStyle('k', fontName='FGB', fontSize=9, leading=12, textColor=BLU, spaceAfter=2)
P = ParagraphStyle('p', fontName='FG', fontSize=11.5, leading=16.5, textColor=colors.black, spaceAfter=5)
PB = ParagraphStyle('pb', parent=P, fontName='FGB')
SM = ParagraphStyle('sm', parent=P, fontSize=9.5, leading=13, textColor=colors.HexColor('#333333'))


def piede(c, d):
    c.saveState()
    c.setFont('FG', 8.5)
    c.setFillColor(colors.HexColor('#555555'))
    c.drawString(20 * mm, 11 * mm, 'Centro Studi Telesio · %s · %s · Quinto anno' % ('Storia', 'Prof. Giorgio Mazzotti'))
    c.drawRightString(190 * mm, 11 * mm, 'Pagina %d' % d.page)
    c.restoreState()


def sezione(story, titolo, kicker):
    story.append(Paragraph(kicker.upper(), K))
    story.append(Paragraph(titolo, H1))
    story.append(Table([['']], colWidths=[40 * mm], rowHeights=[2], style=TableStyle([('LINEABOVE', (0, 0), (-1, 0), 2, BLU)])))
    story.append(Spacer(1, 6))


def pdf_di(story):
    b = io.BytesIO()
    SimpleDocTemplate(b, pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm, topMargin=18 * mm, bottomMargin=20 * mm,
                      title=S.TITOLO, author='Centro Studi Telesio').build(story, onFirstPage=piede, onLaterPages=piede)
    b.seek(0)
    return b


def copertina():
    s = [Spacer(1, 70 * mm), Paragraph('STORIA · QUINTO ANNO', K), Paragraph(S.TITOLO, ParagraphStyle('t', parent=H1, fontSize=44, leading=48)),
         Spacer(1, 8 * mm), Paragraph('Dispensa della videolezione', ParagraphStyle('s', parent=P, fontSize=16, leading=22)),
         Paragraph('Prof. Giorgio Mazzotti', ParagraphStyle('s2', parent=P, fontSize=14)), Spacer(1, 90 * mm),
         Paragraph('Centro Studi Telesio · Milano', SM),
         Paragraph('Dispensa con mappe concettuali, pensata anche per la lettura in bianco e nero e per studenti con DSA e BES.', SM)]
    return pdf_di(s)


w = PdfWriter()


def add(b):
    for pg in PdfReader(b).pages:
        w.add_page(pg)


add(copertina())
lez = os.path.join(W, 'mappe', 'lez.pdf')
if os.path.exists(lez):
    for pg in PdfReader(lez).pages:
        w.add_page(pg)
for a in S.ARG:
    st = []
    sezione(st, a['breve'], 'Argomento %d' % a['id'])
    tt, cards = struttura(PDF, a['pagine'][0])
    st.append(Paragraph('Dalle slide del docente · %s' % tt, K))
    for lead, frs in cards:
        st.append(Paragraph('<b>%s</b> %s' % (lead, ' '.join(frs)), P))
    for an in a['an']:
        st.append(Paragraph(an['titolo'], H2))
        if an['tipo'] in ('cards', 'timeline'):
            for it in an['items']:
                st.append(Paragraph('<b>%s</b>: %s' % (it[0], it[1]) if it[1] else '<b>%s</b>' % it[0], P))
        elif an['tipo'] == 'stats':
            for it in an['items']:
                st.append(Paragraph('<b>%s</b>: %s' % (it[0], it[1]), P))
        else:
            st.append(Paragraph(' '.join(an['voce']), P))
    st.append(Paragraph('Per ripassare', H2))
    st.append(Paragraph(' '.join(a['ripasso'][1:]), P))
    add(pdf_di(st))
    mp = os.path.join(W, 'mappe', 'map%d.pdf' % a['id'])
    if os.path.exists(mp):
        for pg in PdfReader(mp).pages:
            w.add_page(pg)
# glossario
st = []
sezione(st, 'Glossario', 'Le parole chiave')
for p in S.PARTI:
    for t, d in p['glossario']:
        st.append(Paragraph('<b>%s</b>: %s.' % (t, d), P))
add(pdf_di(st))
w.add_metadata({'/Title': S.TITOLO + ' · dispensa', '/Author': 'Centro Studi Telesio'})
w.write(OUT)
print(OUT, len(w.pages), 'pagine')
