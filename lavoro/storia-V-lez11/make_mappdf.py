import sys,os,re
sys.path.insert(0,'/home/user/work/build')
exec(open('/home/user/work/build/build2.py').read())
from maps import MAPS
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,landscape
from PIL import Image
CSS_C=open(B+'/make_prof.py').read().split('CSS_COVER="""')[1].split('"""')[0]
items=''.join(f'<li>{T["t"]}</li>' for T in TOP)
h=f'<img id=logo src="data:image/svg+xml;base64,{LOGO}"><div id=hl></div><div id=cm>MAPPE</div><div id=c1>STORIA V · VIDEOLEZIONE</div><div id=c2>L\'URSS di Stalin<br>(1924-1939)</div><div id=cb></div><div id=cg>URSS: Unione delle Repubbliche Socialiste Sovietiche</div>'
h+=f'<div id=ca><div class=h>ARGOMENTI</div><ul>{items}</ul></div><div id=fl></div><div id=ft>STORIA V</div><div id=pg>Pagina 1</div>'
r.shot(h,B+'/cover_mappe.png',CSS_C+"#cm{position:absolute;left:80px;top:196px;font:800 110px/1 BG;color:#2060AF;letter-spacing:.04em}#c1{top:330px}#c2{top:380px;font-size:104px}#cb{top:610px}#cg{top:632px}#ca{top:690px}")
W_,H_=landscape(A4);c=canvas.Canvas(B+'/Storia_Lez11_mappe.pdf',pagesize=(W_,H_));c.setTitle("MAPPE · Storia V · L'URSS di Stalin (1924-1939)")
pages=[(B+'/cover_mappe.png',["MAPPE","STORIA V · VIDEOLEZIONE","L'URSS di Stalin (1924-1939)"])]
for nm in ('M1','M23','M4'):
    M=MAPS[nm];txt=[M['q']]+[b[5] for b in M['boxes'].values()]+[a[2] for a in M['arrows'].values() if a[2]]+([M['note']] if M['note'] else [])
    pages.append((f'{B}/mp/{nm}.png',txt))
for fn,txt in pages:
    jp=fn[:-4]+'_pdf.jpg';Image.open(fn).convert('RGB').save(jp,quality=93)
    hh=W_*1080/1920;c.drawImage(jp,0,(H_-hh)/2,W_,hh)
    t=c.beginText(30,H_-40);t.setTextRenderMode(3);t.setFont('Helvetica',10)
    for line in txt: t.textLine(line)
    c.drawText(t);c.showPage()
c.save();print('ok')
