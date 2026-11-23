# -*- coding: utf-8 -*-
# Dispensa A4 orizzontale identica al video (stesse slide, stesso ordine) con strato di testo invisibile; PDF delle mappe a parte.
import sys, os, re, json, html as H, subprocess
sys.path.insert(0,'/home/work/build')
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.utils import ImageReader
from PIL import Image
import layout, prof, plan as PL, av
import mappe as MP
from pieces_y import cover_html, TITLE_EX
from lib import render
PARTI={1:[1,2,3],2:[4,5],3:[6,7,8]}
def text_of(htmlfile):
    t=open(htmlfile).read();t=re.sub(r'<style.*?</style>','',t,flags=re.S);t=re.sub(r'<img[^>]*>','',t);t=re.sub(r'<[^>]+>','\n',t);t=H.unescape(t)
    return [l.strip() for l in t.split('\n') if l.strip() and l.strip() not in ('Giorgio Mazzotti','PROF. DI STORIA')]
def webcam_still(t,out):
    if os.path.exists(out):return out
    av.sh(['ffmpeg','-y','-v','error','-ss',f'{t:.2f}','-i',av.SRC,'-frames:v','1','-vf','crop=181:136:856:344,scale=412:310:flags=lanczos,hqdn3d=1.5:1.5:3:3,eq=contrast=1.04:saturation=1.03,cas=0.35',out]);return out
def with_webcam(png,wc,out):
    im=Image.open(png).convert('RGB');w=Image.open(wc).convert('RGB');m=Image.open('/home/work/build/mask.png').convert('L');im.paste(w,(1428,148),m);im.save(out);return out
def pages(P):
    L,plans=layout.layout(P);pg=[]   # (numero, png, html)
    pg.append((1,None,'cover'))
    pg.append((2,f'/home/work/build/lit/dcp{P}_{len(PARTI[P])-1}.png',f'/home/work/build/lit/dcp{P}_{len(PARTI[P])-1}.html'))
    import re as _re
    for n in PARTI[P]:
        pl=plans[n];keys=[];
        for k,v,f in pl['states']:
            if (k,v) not in keys:keys.append((k,v))
        for i,(k,v) in enumerate(keys):
            nm=f"P{P}_n{n}_{k[0]}_{k[1]}_v{v}"
            pg.append((L[n]['prof']+i,f'/home/work/build/sl/{nm}.png',f'/home/work/build/sl/{nm}.html',('webcam',pl['cut'][0]+25)))
        from pieces_x import V,sents
        ns=len(sents(V[f'AP{n}']))
        pg.append((L[n]['ap'],f'/home/work/build/lit/AP{n}_h.png',f'/home/work/build/lit/AP{n}_h.html'))
        for i in range(ns-1): pg.append((L[n]['ap']+i+1,f'/home/work/build/lit/AP{n}_{i}.png',f'/home/work/build/lit/AP{n}_{i}.html'))
        if n in layout.MAPDOPO:
            k=layout.MAPDOPO[n];pg.append((L[n]['map'],f'/home/work/build/lit/map{k}_{len(MP.MAPS[k]["steps"])}.png',f'/home/work/build/lit/map{k}.html'))
        from pieces_x import SCD
        pg.append((L[n]['schema'],f'/home/work/build/lit/RP{n}_3.png',f'/home/work/build/lit/RP{n}_3.html'))
    lg={1:2,2:1,3:2}[P];pg.append((L['gloss'],f'/home/work/build/lit/gl{P}_{lg}.png',f'/home/work/build/lit/gl{P}_{lg}.html'))
    return pg
def make_pdf(items,out,footer=True):
    W,Hh=landscape(A4);c=canvas.Canvas(out,pagesize=(W,Hh));c.setTitle("Storia V · "+TITLE_EX)
    for png,txt in items:
        im=ImageReader(png);iw,ih=Image.open(png).size;h=W*ih/iw;y=(Hh-h)/2
        c.setFillColorRGB(1,1,1);c.rect(0,0,W,Hh,stroke=0,fill=1);c.drawImage(im,0,y,W,h)
        t=c.beginText(10,Hh-20);t.setTextRenderMode(3);t.setFont('Helvetica',8)
        for l in txt: t.textLine(l)
        c.drawText(t);c.showPage()
    c.save()
def dispensa(P,out):
    wd='/home/work/build/docs';os.makedirs(wd,exist_ok=True);items=[]
    # copertina della dispensa: solo materia e titolo
    h=cover_html(P,False,1)
    h=re.sub(r"<div class=kick[^>]*>.*?</div>","<div class=kick style='left:80px;top:168px;font-size:28px'>STORIA V</div>",h,count=1,flags=re.S)
    h=re.sub(r"<div style='position:absolute;left:80px;top:540px.*?</div>","",h,flags=re.S);h=re.sub(r"<div style='position:absolute;left:80px;right:80px;bottom:90px.*?</div>","",h,flags=re.S)
    h=re.sub(r"<div class=foot style='right:80px'>Pagina 1</div>","",h)
    render([(f'dcover{P}',h)],wd)
    items.append((f'{wd}/dcover{P}.png',['STORIA V',TITLE_EX]))
    for p in pages(P)[1:]:
        num,png,htm=p[0],p[1],p[2]
        if len(p)>3:
            wc=webcam_still(p[3][1],f'{wd}/wc_{int(p[3][1])}.png');png=with_webcam(png,wc,f'{wd}/pg_{os.path.basename(png)}')
        items.append((png,text_of(htm) if os.path.exists(htm) else []))
    make_pdf(items,out);return len(items)
def mappe_pdf(P,out):
    ks=[k for n,k in layout.MAPDOPO.items() if n in PARTI[P]]
    if not ks:return 0
    wd='/home/work/build/docs'
    h=cover_html(P,False,1)
    h=re.sub(r"<div class=kick[^>]*>.*?</div>","<div class=kick style='left:80px;top:150px;font-size:28px'>STORIA V · MAPPE</div><div style='position:absolute;left:80px;top:196px;font:800 40px Bri;color:#0B1530;letter-spacing:.2em'>MAPPE</div>",h,count=1,flags=re.S)
    render([(f'mcover{P}',h)],wd)
    items=[(f'{wd}/mcover{P}.png',['STORIA V','MAPPE',TITLE_EX])]
    for k in ks: items.append((f'/home/work/build/lit/map{k}_{len(MP.MAPS[k]["steps"])}.png',text_of(f'/home/work/build/lit/map{k}.html')))
    make_pdf(items,out);return len(items)
