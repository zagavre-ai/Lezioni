# Libreria grafica · Storia dell'arte V lez03 (22/11). Fondo bianco, blu notte, blu Telesio, giallo.
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, re
FD='/home/user/Lezioni/kit/caratteri/'
W,H=1920,1080
NOTTE=(11,21,48); TELESIO=(32,96,175); GIALLO=(255,230,0); GRIGIO=(217,223,234)
_f={}
def F(n,s):
    k=(n,s)
    if k not in _f:_f[k]=ImageFont.truetype(FD+{'t':'BricolageGrotesque-ExtraBold.ttf','r':'Figtree-Regular.ttf','b':'Figtree-Bold.ttf','x':'Figtree-ExtraBold.ttf','m':'Figtree-Medium.ttf'}[n],s)
    return _f[k]
IMG='/tmp/w/img2/'
def _logo():
    im=Image.open(IMG+'logo.png').convert('L').crop((22,165,446,306))
    a=Image.eval(im,lambda v:255-v)
    n=Image.new('RGBA',im.size,NOTTE+(0,));n.putalpha(a)
    b=Image.new('RGBA',im.size,(255,255,255,0));b.putalpha(a)
    return n,b
LOGO_N,LOGO_B=_logo()
def logo(img,x,y,w,bianco=False):
    l=(LOGO_B if bianco else LOGO_N);h=round(l.size[1]*w/l.size[0])
    l=l.resize((w,h),Image.LANCZOS);img.paste(l,(x,y),l)
def shadow(img,box,r=18,blur=22,off=(0,10),alpha=70):
    x0,y0,x1,y1=box;pad=blur*3
    s=Image.new('RGBA',(x1-x0+2*pad,y1-y0+2*pad),(0,0,0,0))
    ImageDraw.Draw(s).rounded_rectangle((pad,pad,pad+x1-x0,pad+y1-y0),r,fill=(90,98,115,alpha))
    s=s.filter(ImageFilter.GaussianBlur(blur))
    img.paste(s,(x0-pad+off[0],y0-pad+off[1]),s)
def runs_lines(d,runs,fb,fr,width):
    """runs=[(testo,bold)]: spezza in righe di larghezza <= width; restituisce lista di righe [(parola,bold)]"""
    words=[]
    for t,b in runs:
        for w in t.split(' '):
            if w:words.append((w,b))
    lines=[];cur=[];cw=0;sp=d.textlength(' ',font=fr)
    for w,b in words:
        wl=d.textlength(w,font=fb if b else fr)
        if cur and cw+sp+wl>width:lines.append(cur);cur=[];cw=0
        cw+=(sp if cur else 0)+wl;cur.append((w,b))
    if cur:lines.append(cur)
    return lines
def card_height(runs,width,size=40,lh=1.5,pad=26):
    d=ImageDraw.Draw(Image.new('RGB',(10,10)))
    L=runs_lines(d,runs,F('b',size),F('r',size),width-2*pad-30)
    return round(len(L)*size*lh+2*pad-(size*lh-size)/2)
def draw_card(img,x,y,w,runs,stato='normale',size=40,lh=1.5,pad=26,fill=(255,255,255)):
    """stato: 'acceso' (bordo giallo + pallino), 'normale', 'attenuata'"""
    d=ImageDraw.Draw(img);fb,fr=F('b',size),F('r',size)
    L=runs_lines(d,runs,fb,fr,w-2*pad-30);h=round(len(L)*size*lh+2*pad-(size*lh-size)/2)
    shadow(img,(x,y,x+w,y+h),r=20,blur=14,off=(0,6),alpha=45 if stato!='attenuata' else 25)
    d=ImageDraw.Draw(img)
    d.rounded_rectangle((x,y,x+w,y+h),20,fill=fill)
    if stato=='acceso':
        d.rounded_rectangle((x,y,x+w,y+h),20,outline=GIALLO,width=7)
        d.ellipse((x+w-44,y+16,x+w-20,y+40),fill=GIALLO,outline=NOTTE,width=2)
        col=NOTTE
    elif stato=='attenuata':
        d.rounded_rectangle((x,y,x+w,y+h),20,outline=(228,232,240),width=3);col=(120,128,148)
    else:
        d.rounded_rectangle((x,y,x+w,y+h),20,outline=GRIGIO,width=3);col=NOTTE
    ty=y+pad-(size*lh-size)/2+ (size*lh-size)/2
    for ln in L:
        tx=x+pad;sp=d.textlength(' ',font=fr)
        for i,(wd,b) in enumerate(ln):
            f=fb if b else fr
            d.text((tx,ty),wd,font=f,fill=col)
            tx+=d.textlength(wd,font=f)+sp
        ty+=size*lh
    return h
def wrap_plain(d,text,font,width):
    return [[(l,False)] for l in []] if False else [' '.join(w for w,_ in ln) for ln in runs_lines(d,[(text,False)],font,font,width)]
def base(page=None,footer=True,logo_on=True):
    img=Image.new('RGB',(W,H),(255,255,255));d=ImageDraw.Draw(img)
    if logo_on:logo(img,70,38,190)
    if footer:
        d.line((70,1022,1850,1022),fill=(228,232,240),width=2)
        d.text((70,1038),"STORIA DELL'ARTE V",font=F('b',24),fill=TELESIO)
        if page:
            t=f'Pagina {page}';d.text((1850-d.textlength(t,font=F('b',24)),1038),t,font=F('b',24),fill=TELESIO)
    return img
CAMBOX=(1428,148,1840,457)
def cam_frame(img,name='Prof. Giorgio Mazzotti',mat="STORIA DELL'ARTE V"):
    """ombra grigia + riquadro vuoto (il video del prof viene sovrapposto dopo) + fascia gialla col nome e la materia"""
    x0,y0,x1,y1=CAMBOX
    shadow(img,(x0,y0,x1,y1),r=6,blur=18,off=(0,12),alpha=95)
    d=ImageDraw.Draw(img);d.rectangle((x0,y0,x1,y1),fill=(200,205,215))
    d.rectangle((x0+10,y1+6,x1+10,y1+78),fill=(190,170,0))  # ombra fascia
    d.rectangle((x0,y1,x1,y1+72),fill=GIALLO)
    d.text((x0+20,y1+8),name,font=F('x',30),fill=NOTTE)
    d.text((x0+20,y1+44),mat,font=F('b',20),fill=NOTTE)
def keywords(img,kws,y0=590):
    if not kws:return
    d=ImageDraw.Draw(img);x0,x1=1428,1840
    d.text((x0,y0),'PAROLE CHIAVE',font=F('b',22),fill=TELESIO)
    y=y0+40
    for k in kws[:5]:
        wl=runs_lines(d,[(k,True)],F('b',30),F('b',30),x1-x0-40)
        h=len(wl)*40+22
        d.rounded_rectangle((x0,y,x1,y+h),14,fill=(244,247,252),outline=GRIGIO,width=2)
        d.rectangle((x0,y+8,x0+6,y+h-8),fill=GIALLO)
        yy=y+11
        for ln in wl:
            d.text((x0+22,yy),' '.join(w for w,_ in ln),font=F('b',30),fill=NOTTE);yy+=40
        y+=h+12
def title(img,text,y=120,size=58,maxw=1290,x=80):
    d=ImageDraw.Draw(img);f=F('t',size)
    L=wrap_plain(d,text,f,maxw)
    for i,l in enumerate(L):d.text((x,y+i*(size+8)),l,font=f,fill=TELESIO)
    return y+len(L)*(size+8)
def slide_cards(page,titolo,cards,active,kws,label=None):
    """cards: lista di liste-di-run; active: indice acceso (o None)"""
    img=base(page);cam_frame(img);keywords(img,kws)
    d=ImageDraw.Draw(img)
    if label:d.text((80,104),label.upper(),font=F('b',22),fill=TELESIO)
    y=title(img,titolo,y=136 if label else 120)+26
    for i,c in enumerate(cards):
        st='acceso' if i==active else ('normale' if active is None else 'attenuata')
        y+=draw_card(img,80,y,1280,c,st)+22
    return img
def fit_image(src,box):
    x0,y0,x1,y1=box;w,h=src.size;s=min((x1-x0)/w,(y1-y0)/h)
    return src.resize((round(w*s),round(h*s)),Image.LANCZOS),s
def slide_image(page,titolo,imgname,didasc,kws,view=None,label=None):
    """opera grande a sinistra; view=(x0,y0,x1,y1) frazioni per un dettaglio"""
    img=base(page);cam_frame(img);keywords(img,kws)
    d=ImageDraw.Draw(img)
    if label:d.text((80,104),label.upper(),font=F('b',22),fill=TELESIO)
    y=title(img,titolo,y=136 if label else 120,size=50)+14
    src=Image.open(IMG+imgname+'.png').convert('RGB')
    if view:
        w,h=src.size;src=src.crop((round(view[0]*w),round(view[1]*h),round(view[2]*w),round(view[3]*h)))
    box=(80,y,1360,935)
    im,s=fit_image(src,box)
    ix=80+(1280-im.size[0])//2;iy=y
    shadow(img,(ix,iy,ix+im.size[0],iy+im.size[1]),r=4,blur=16,off=(0,10),alpha=80)
    img.paste(im,(ix,iy))
    d=ImageDraw.Draw(img)
    if didasc:
        wl=wrap_plain(d,didasc,F('m',28),1280)
        for i,l in enumerate(wl):d.text((80,iy+im.size[1]+14+i*36),l,font=F('m',28),fill=(70,80,105))
    return img
