# dispensa A4 orizzontale (identica al video, con strato di testo invisibile) e PDF delle mappe
import sys,os,json,re,subprocess
sys.path.insert(0,'/tmp/claude-0/w/prod')
import build_lez as B
from eng import *
from lib import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image
B.build();IT=B.ITEMS;R=B.REN
pdfmetrics.registerFont(TTFont('Fig','/root/.fonts/Figtree-Regular.ttf'))
def cam_still(t):
    o=W+'/png/cam_%d.png'%int(t)
    if not os.path.exists(o):
        sh(['ffmpeg','-v','error','-y','-ss',str(t),'-i',SRC,'-frames:v','1','-vf','crop=184:138:853:336,scale=412:309:flags=lanczos','-update','1',o])
    return o
def page_png(png,t=None):
    if t is None:return png
    im=Image.open(png).convert('RGB');c=Image.open(cam_still(t)).convert('RGB')
    m=Image.open(W+'/mask_cam.png');im.paste(c,(1428,148),m);o=png[:-4]+'_c.png';im.save(o);return o
pages=[];seen=set()
for it in IT:
    if it.kind=='prof' and it.name!='INTRO':
        last={}
        for (t,p),k in zip(it.states,it.keys):
            kk=('C',k[1],k[2]) if k[0]=='C' else k
            last[kk]=p
        for kk,p in last.items():
            if kk in seen:continue
            seen.add(kk);pages.append((p,it.fr[0][0]+5))
    elif it.kind=='static' and it.name not in ('COPERTINA','ARGOMENTI') and not it.name.startswith('MAPPA'):
        pages.append((it.states[-1][1],None))
    elif it.name=='ARGOMENTI':pages.append((it.states[-1][1],None))
    elif it.name.startswith('MAPPA') and it.name!='MAPPA_FINALE':pages.append((it.states[-2][1],None))
def build_pdf(out,items,cover_extra=''):
    W_,H_=landscape(A4);c=canvas.Canvas(out,pagesize=(W_,H_))
    for p,t in items:
        png=page_png(p,t);jp=png[:-4]+'.jpg'
        if not os.path.exists(jp):Image.open(png).convert('RGB').save(jp,quality=86)
        c.drawImage(jp,0,0,W_,H_)
        txt=R.text.get(p,'')
        to=c.beginText(10,H_-20);to.setTextRenderMode(3);to.setFont('Fig',6)
        for line in re.findall(r'.{1,150}(?:\s|$)',txt):to.textLine(line)
        c.drawText(to);c.setFont('Fig',7);c.showPage()
    c.save()
cover=R.shot(cover(1,False))
# copertina: solo materia e titolo (come la copertina delle slide, senza elenco degli argomenti)
cv=R.shot('<img class="logo" src="%s"><div class="rule"></div><div class="lab" style="top:150px">%s · VIDEOLEZIONE</div><div class="tit" style="top:196px;font-size:104px;line-height:1.02;color:#0B1530;width:1700px">RAZIONALISMO<br>E METAFISICA</div><div class="foot">%s</div><div class="pag">Pagina 1</div><div class="frule"></div>'%(LOGO,MATERIA,MATERIA))
ps=[(cv,None)]+pages
build_pdf(W+'/consegna/Storia_arte_Lez13_slide.pdf',ps)
cvm=R.shot('<img class="logo" src="%s"><div class="rule"></div><div class="lab" style="top:150px">%s · VIDEOLEZIONE</div><div class="tit" style="top:196px;font-size:104px;line-height:1.02;color:#0B1530;width:1700px"><span style="color:#2060AF">MAPPE</span><br>RAZIONALISMO E METAFISICA</div><div class="foot">%s</div><div class="pag">Pagina 1</div><div class="frule"></div>'%(LOGO,MATERIA,MATERIA))
import content as C
def mp(M):return R.shot(mappa(M['titolo'],M['boxes'],M['arrows'],[b[0] for b in M['boxes']],None),MAPCSS)
build_pdf(W+'/consegna/Storia_arte_Lez13_mappe.pdf',[(cvm,None),(mp(C.MAPPE['meta']),None),(mp(C.MAPPE['arch']),None)])
print(len(ps),'pagine slide')
R.close()
