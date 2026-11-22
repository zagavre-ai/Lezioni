import sys,os,json,re
sys.path.insert(0,'/home/user/work/build')
exec(open('/home/user/work/build/build2.py').read())
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,landscape
from PIL import Image
P=json.load(open(B+'/plan.json'));pn={(k,tuple(w)):v for k,w,v in P['pn']}
WIDE="#flow{width:1760px}#ttl{width:1760px}#cards{width:1760px}"
os.makedirs(B+'/pdf',exist_ok=True)
pages=[]  # (png, [righe di testo])
# copertina
cov_txt=["STORIA V · VIDEOLEZIONE","L'URSS di Stalin (1924-1939)","URSS: Unione delle Repubbliche Socialiste Sovietiche","ARGOMENTI"]+[T['t'] for T in TOP]
pages.append((B+'/cover_pdf.png',cov_txt))
import subprocess
src=open(B+'/make_prof.py').read()
# copertina senza webcam e senza benvenuto: riuso cover_a
Image.open(B+'/cover_a.png').convert('RGB').save(B+'/cover_pdf.png')
items=sorted(pn.items(),key=lambda kv:kv[1])
for (key,w),num in items:
    fn=f'{B}/pdf/p{num:03d}.png'
    if key=='FOTO':
        r.shot(foto_html(num,False),fn);pages.append((fn,['01 · L\'ascesa di Stalin','Iosif Stalin']));continue
    p=PAGES[key]
    h,_=frame(p['kick'],p['title'],p['cards'],list(w),None,[],None,num,prof=False,wide=True,fs=40 if key.startswith('p') else 46)
    r.shot(h,fn)
    txt=[p['kick'],re.sub('<[^>]+>','',p['title'])]+[p['cards'][i-1] for i in w]
    pages.append((fn,txt))
def pdf(pages,out,title):
    W_,H_=landscape(A4);c=canvas.Canvas(out,pagesize=(W_,H_));c.setTitle(title)
    for fn,txt in pages:
        im=Image.open(fn).convert('RGB');jp=fn[:-4]+'.jpg';im.save(jp,quality=92)
        h=W_*1080/1920;c.drawImage(jp,0,(H_-h)/2,W_,h)
        t=c.beginText(30,H_-40);t.setTextRenderMode(3);t.setFont('Helvetica',10)
        for line in txt:
            for chunk in [line[i:i+110] for i in range(0,len(line),110)]: t.textLine(chunk)
        c.drawText(t);c.showPage()
    c.save()
pdf(pages,B+'/Storia_Lez11_dispensa.pdf',"L'URSS di Stalin (1924-1939)")
print(len(pages),'pagine')
