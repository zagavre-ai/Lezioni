# Dispensa A4 orizzontale (identica al video, con strato di testo invisibile) e PDF delle mappe
import sys,json,re,os,html as H
sys.path.insert(0,'/home/claude/w19/lib')
from piano import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('Fig','/root/.fonts/Figtree-Regular.ttf'))
PW,PH=landscape(A4)
def plain(t): return re.sub(r'\s+',' ',H.unescape(re.sub(r'<[^>]+>',' ',t))).strip()
def page(c,png,testo):
    h=PW*1080/1920;c.setFillColorRGB(1,1,1);c.rect(0,0,PW,PH,fill=1,stroke=0)
    c.drawImage(png,0,(PH-h)/2,PW,h)
    t=c.beginText(20,PH-20);t.setTextRenderMode(3);t.setFont('Fig',8)
    for line in re.findall(r'.{1,150}(?:\s|$)',testo): t.textLine(line.strip())
    c.drawText(t);c.showPage()
def render_pages():
    P=json.load(open(W+'/slide.json'));pages=[];prevkey=None
    os.makedirs(O+'disp',exist_ok=True)
    with B() as b:
        def shot(h,name,txt):
            png=O+'disp/'+name+'.png';b.shot(h,png);pages.append((png,txt))
        shot(cover_html(False,pg=1),'cover',f'STORIA V · VIDEOLEZIONE. {plain(TIT_LEZ)}. Argomenti: '+'. '.join(viste.ARGT[i] for i in range(1,9)))
        for i,items in enumerate([[1,2,3],[4,5,6],[7,8]]):
            shot(argomenti_html(items,2+i,cam=False),f'arg{i}','Di cosa parliamo. '+'. '.join(viste.ARGT[k] for k in items))
        for tl in ('timeline_P1.json','timeline_P2.json'):
            T=json.load(open(W+'/'+tl))
            for it in T:
                if it['tipo']!='prof': continue
                j=json.load(open(f'{OUT}/{it["id"]}.json'))
                for m in j['meta']:
                    key=(m['kind'],m.get('page'),tuple(m.get('win',[])),m.get('key'))
                    if key==prevkey: continue
                    prevkey=key
                    if m['kind']=='img':
                        tit,cap,_=viste.IMG[m['key']];txt=f'{tit}. {cap}'
                        shot(viste.html_img(m['key'],m['argn'],m['pg'],cam=False),f'p{m["pg"]}',txt)
                    else:
                        paras=P[m['page']-1]['par'];h_=slide_html(m['titolo'],viste.kicker(m['argn']),m['pg'],paras,-1,m['win'],m['keys'],cam=False)
                        shot(h_,f'p{m["pg"]}',m['titolo']+'. '+' '.join(plain(spiega(paras[i])) for i in m['win'])+' Parole chiave: '+', '.join(m['keys']))
    return pages
def dispensa(out):
    pages=render_pages();c=canvas.Canvas(out,pagesize=(PW,PH));c.setTitle('Storia V · '+plain(TIT_LEZ));c.setAuthor('Centro Studi Telesio')
    for png,txt in pages: page(c,png,txt)
    c.save();return len(pages)
def mappe_pdf(out):
    os.makedirs(O+'disp',exist_ok=True)
    with B() as b:
        cv=cover_html(False,pg=1).replace('STORIA V · VIDEOLEZIONE','STORIA V · MAPPE')
        cv=cv.replace('<div data-t0','<div data-t0')
        # niente elenco argomenti: copertina identica con la scritta MAPPE
        b.shot(cv+'<div class=abs style="right:80px;top:160px;font:800 80px \'Bricolage Grotesque\';color:#2060AF;letter-spacing:.1em">MAPPE</div>',O+'disp/mcover.png')
    c=canvas.Canvas(out,pagesize=(PW,PH));c.setTitle('Storia V · Mappe');c.setAuthor('Centro Studi Telesio')
    page(c,O+'disp/mcover.png','MAPPE. STORIA V. '+plain(TIT_LEZ))
    for k in (1,2,3):
        m=mappe.MAPPE[k];txt=m['domanda']+' '+' '.join(plain(n['t']) for n in m['nodes'].values())
        page(c,O+f'map{k}.png',txt)
    c.save()
import mappe
if __name__=='__main__':
    if sys.argv[1]=='mappe': mappe_pdf(sys.argv[2])
    else: print(dispensa(sys.argv[2]),'pagine')
