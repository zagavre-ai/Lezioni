# Schede in blu scuro animato (titolo, pillola, quiz, riepilogo, glossario, mappa...). Sfondo animato in loop + livelli di testo trasparenti.
import sys,os,math,subprocess
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from lib import *
import numpy as np
BG='/tmp/w/bg_blu.mp4'
def make_bg(dur=12,fps=30):
    if os.path.exists(BG):return
    w,h=960,540  # calcolato a meta' e poi ingrandito
    yy,xx=np.mgrid[0:h,0:w]
    base=np.zeros((h,w,3),np.float32)
    t0=np.array([8,16,40],np.float32);t1=np.array([20,52,118],np.float32)
    g=(xx/w*0.5+yy/h*0.5)[...,None]
    base=t0*(1-g)+t1*g
    blobs=[(0.2,0.3,260,(40,100,200),0.0),(0.8,0.2,220,(30,80,170),1.7),(0.6,0.8,300,(25,70,160),3.1),(0.1,0.85,200,(60,120,210),4.4),(0.9,0.7,180,(20,60,140),5.3)]
    p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{w}x{h}','-r',str(fps),'-i','-','-vf','scale=1920:1080:flags=bicubic','-c:v','libx264','-preset','veryfast','-crf','16','-pix_fmt','yuv420p',BG],stdin=subprocess.PIPE)
    n=dur*fps
    for i in range(n):
        ph=2*math.pi*i/n
        f=base.copy()
        for bx,by,r,col,o in blobs:
            cx=(bx+0.07*math.sin(ph+o))*w;cy=(by+0.07*math.cos(ph*1+o))*h
            d2=((xx-cx)**2+(yy-cy)**2)/(r*r)
            a=np.exp(-d2*1.6)[...,None]*0.38
            f=f*(1-a)+np.array(col,np.float32)*a
        p.stdin.write(np.clip(f,0,255).astype(np.uint8).tobytes())
    p.stdin.close();p.wait()
def layer():return Image.new('RGBA',(W,H),(0,0,0,0))
def bianco(d,x,y,t,f,anchor='la',fill=(255,255,255)):d.text((x,y),t,font=f,fill=fill,anchor=anchor)
def logo_bianco(im,w=190,pos=(80,44)):
    l=logo(w).copy();a=l.split()[3];wh=Image.new('RGBA',l.size,(255,255,255,255));wh.putalpha(a);im.alpha_composite(wh,pos)
CUR=None
def intestazione(im,materia="STORIA DELL'ARTE V",pagina=None):
    pagina=pagina or CUR
    logo_bianco(im);d=ImageDraw.Draw(im)
    d.text((80,1030),materia,font=fig(22,True),fill=(190,210,245),anchor='lm')
    if pagina:d.text((1840,1030),f'Pagina {pagina}',font=fig(22,True),fill=(190,210,245),anchor='rm')
def scheda_titolo(kicker,titolo_t,sotto=None,size=104):
    im=layer();intestazione(im);d=ImageDraw.Draw(im)
    d.text((960,360),kicker.upper(),font=fig(34,True),fill=GIALLO,anchor='mm')
    f=brico(size);lines=wrap(d,titolo_t,f,1560)
    while len(lines)>3 and size>60:size-=6;f=brico(size);lines=wrap(d,titolo_t,f,1560)
    y=540-(len(lines)-1)*(size+10)//2
    for i,l in enumerate(lines):d.text((960,y+i*(size+10)),l,font=f,fill=(255,255,255),anchor='mm')
    if sotto:d.text((960,y+len(lines)*(size+10)+30),sotto,font=fig(40),fill=(200,218,250),anchor='mm')
    return im
def card_blu(im,x,y,w,testo,stato,size=44,num=None):
    """riga di una pillola/riepilogo: stato on (giallo, bianco) / off (attenuata) / hidden"""
    d=ImageDraw.Draw(im);f=fig(size,False);fb=fig(size,True)
    lines=wrap(d,testo,f,w-110);lh=int(size*1.3);hh=len(lines)*lh+34
    if stato=='hidden':return hh
    on=stato=='on'
    fill=(255,255,255,255) if on else (255,255,255,40)
    ol=GIALLO if on else (255,255,255,70)
    d.rounded_rectangle((x,y,x+w,y+hh),22,fill=fill,outline=ol,width=7 if on else 2)
    d.ellipse((x+28,y+28,x+50,y+50),fill=GIALLO if on else (255,255,255,110))
    for i,l in enumerate(lines):d.text((x+78,y+17+i*lh),l,font=f,fill=NAVY if on else (225,235,252),anchor='la')
    return hh
def altezza_riga(testo,w,size=44):
    d=ImageDraw.Draw(Image.new('RGBA',(10,10)));lines=wrap(d,testo,fig(size),w-110);return len(lines)*int(size*1.3)+34
def scheda_pillola(titolo_t,righe,attiva,size=44,pagina=None):
    im=layer();intestazione(im,pagina=pagina);d=ImageDraw.Draw(im)
    d.text((960,170),'PILLOLA DI RIPASSO',font=fig(30,True),fill=GIALLO,anchor='mm')
    d.text((960,235),titolo_t,font=brico(54),fill=(255,255,255),anchor='mm')
    w=1560;x=180;gap=18
    while True:
        hs=[altezza_riga(r,w,size) for r in righe]
        if sum(hs)+gap*(len(hs)-1)<=680 or size<=34:break
        size-=2
    tot=sum(hs)+gap*(len(hs)-1);y=330+max(0,(660-tot)//2)
    for i,r in enumerate(righe):
        st='hidden' if i>attiva else ('on' if i==attiva else 'off')
        card_blu(im,x,y,w,r,st,size);y+=hs[i]+gap
    return im

def card_blu2(im,x,y,w,termine,testo,stato,size=40):
    d=ImageDraw.Draw(im);f=fig(size,False);fb=fig(size,True)
    words=[(t,True) for t in (termine+':').split()]+[(t,False) for t in testo.split()]
    lines=[[]];cw=0;sp=d.textlength(' ',font=f);inner=w-110
    for t,b in words:
        ww=d.textlength(t,font=fb if b else f)
        if cw+ww>inner and lines[-1]:lines.append([]);cw=0
        lines[-1].append((t,b,ww));cw+=ww+sp
    lh=int(size*1.3);hh=len(lines)*lh+34
    if stato=='hidden':return hh
    on=stato=='on'
    d.rounded_rectangle((x,y,x+w,y+hh),22,fill=(255,255,255,255) if on else (255,255,255,40),outline=GIALLO if on else (255,255,255,70),width=7 if on else 2)
    d.ellipse((x+28,y+28,x+50,y+50),fill=GIALLO if on else (255,255,255,110))
    for i,l in enumerate(lines):
        cx=x+78
        for t,b,ww in l:
            d.text((cx,y+17+i*lh),t,font=fb if b else f,fill=(NAVY if on else (235,242,255)) if not b else (BLU if on else (255,230,120)),anchor='la');cx+=ww+sp
    return hh
def altezza2(termine,testo,w,size=40):
    d=ImageDraw.Draw(Image.new('RGBA',(10,10)));f=fig(size);fb=fig(size,True)
    words=[(t,True) for t in (termine+':').split()]+[(t,False) for t in testo.split()]
    n=1;cw=0;sp=d.textlength(' ',font=f)
    for t,b in words:
        ww=d.textlength(t,font=fb if b else f)
        if cw+ww>w-110 and cw>0:n+=1;cw=0
        cw+=ww+sp
    return n*int(size*1.3)+34
