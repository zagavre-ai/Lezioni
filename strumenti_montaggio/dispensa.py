import os, sys, pickle, re
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
pdfmetrics.registerFont(TTFont('Fig','/root/.fonts/Figtree-Bold.ttf'))
pdfmetrics.registerFont(TTFont('FigR','/root/.fonts/Figtree-Regular.ttf'))
PW,PH=landscape(A4)
def pdf(pages,out,titolo,materia='STORIA V',numeri=True):
    """pages: [(png, testo_invisibile, numero)] -> A4 orizzontale; immagine a tutta larghezza; testo invisibile leggibile dalla sintesi vocale"""
    c=canvas.Canvas(out,pagesize=(PW,PH));c.setTitle(titolo);c.setAuthor('Centro Studi Telesio');c.setSubject(materia)
    for i,(png,txt,num) in enumerate(pages):
        w=PW;h=PW*9/16;y=(PH-h)/2+4
        c.drawImage(ImageReader(png),0,y,width=w,height=h)
        # testo invisibile (modalità 3), una riga per blocco, nell'ordine di lettura
        t=c.beginText(14,PH-18);t.setTextRenderMode(3);t.setFont('FigR',7)
        for line in (txt or '').splitlines():
            line=line.strip()
            if line: t.textLine(line)
        c.drawText(t)
        if numeri and num is not None:
            c.setFont('Fig',9);c.setFillColorRGB(0.125,0.376,0.686)
            c.drawString(26,12,materia);c.drawRightString(PW-26,12,f'Pagina {num}')
        c.showPage()
    c.save()
def read_txt(png):
    f=png+'.txt'
    return open(f).read() if os.path.exists(f) else ''
