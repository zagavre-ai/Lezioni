import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from lezione import *
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('Fig','/root/.fonts/Figtree-Regular.ttf'))
D=W+'/mappe_pdf';os.makedirs(D,exist_ok=True)
pdf=canvas.Canvas(W+'/Storia_Lez9_mappe.pdf',pagesize=(841.92,594.96));pdf.setTitle('MAPPE · Storia V · '+TIT_ESATTO)
pages=[('cover',cover_html(None,False,None,1,'MAPPE · STORIA V'))]
for k,m in MAPPE.items():pages.append((k,map_html(m,[n[0] for n in m['nodi']],None,{(a,b) for a,b,_ in m['archi']},pag=len(pages)+1)))
with G.R() as r:
    for k,h in pages:
        r.set(h);p=f'{D}/{k}.jpg';r.pg.screenshot(path=p,type='jpeg',quality=92);txt=r.pg.evaluate('document.body.innerText')
        hh=841.92*1080/1920;pdf.drawImage(p,0,(594.96-hh)/2,841.92,hh)
        t=pdf.beginText(20,570);t.setFont('Fig',8);t.setTextRenderMode(3)
        for ln in txt.split('\n'):
            if ln.strip():t.textLine(ln.strip())
        pdf.drawText(t);pdf.showPage()
pdf.save();print('ok',len(pages))
