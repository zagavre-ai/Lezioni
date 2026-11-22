# Libreria grafica Telesio per le videolezioni (1920x1080). Fondo bianco, blu notte, blu Telesio, giallo solo per evidenziare.
import os,re,textwrap
from PIL import Image,ImageDraw,ImageFont,ImageFilter,ImageChops
W,H=1920,1080
NAVY=(11,21,48);BLU=(32,96,175);GIALLO=(255,230,0);GRIGIO=(120,128,145)
FD='/root/.fonts/'
def F(name,size):return ImageFont.truetype(FD+name,size)
def brico(s):return F('BricolageGrotesque-ExtraBold.ttf',s)
def fig(s,b=False):return F('Figtree-Bold.ttf' if b else 'Figtree-Medium.ttf',s)
def figb(s):return F('Figtree-ExtraBold.ttf',s)
ASSET='/tmp/w/asset/'
os.makedirs(ASSET,exist_ok=True)
LOGO=None
def logo(w=170):
    global LOGO
    p=ASSET+f'logo{w}.png'
    if not os.path.exists(p):
        import logo as L
        L.render('/home/user/Lezioni/kit/docenti/Telesio_logo_blu.svg',w).save(p)
    return Image.open(p)
def tw(d,t,f):return d.textlength(t,font=f)
def wrap(d,t,f,maxw):
    out=[];line=''
    for w in t.split(' '):
        c=(line+' '+w).strip()
        if tw(d,c,f)<=maxw:line=c
        else:out.append(line);line=w
    if line:out.append(line)
    return out
def shadow(im,box,r=22,blur=22,off=(0,10),alpha=60):
    sh=Image.new('RGBA',im.size,(0,0,0,0));d=ImageDraw.Draw(sh)
    x0,y0,x1,y1=box;d.rounded_rectangle((x0+off[0],y0+off[1],x1+off[0],y1+off[1]),r,fill=(70,80,100,alpha))
    sh=sh.filter(ImageFilter.GaussianBlur(blur));im.alpha_composite(sh)
def base(pagina=None,materia="STORIA DELL'ARTE V",etichetta=None):
    im=Image.new('RGBA',(W,H),(255,255,255,255));d=ImageDraw.Draw(im)
    im.alpha_composite(logo(170),(80,44))
    d.line((80,124,1840,124),fill=(225,229,236),width=2)
    d.line((80,981,1840,981),fill=(225,229,236),width=2)
    d.text((80,1011),materia,font=fig(22,True),fill=BLU,anchor='lm')
    if pagina:d.text((1840,1011),f'Pagina {pagina}',font=fig(22,True),fill=BLU,anchor='rm')
    if etichetta:d.text((80,160),etichetta.upper(),font=fig(26,True),fill=BLU,anchor='lm')
    return im
def titolo(im,t,y=196,size=62):
    d=ImageDraw.Draw(im);f=brico(size);lines=wrap(d,t,f,1280)
    while len(lines)>2 and size>44:size-=4;f=brico(size);lines=wrap(d,t,f,1280)
    for i,l in enumerate(lines):d.text((80,y+i*(size+8)),l,font=f,fill=NAVY)
    yy=y+len(lines)*(size+8)+10
    d.rounded_rectangle((80,yy,165,yy+6),3,fill=BLU)
    return yy+34
CAM=(1428,148,412,309)
def prof_box(im,nome="Giorgio Mazzotti",ruolo="PROF. DI STORIA DELL'ARTE",con_buco=True):
    x,y,w,h=CAM;shadow(im,(x,y,x+w,y+h),r=16,blur=18,off=(0,8),alpha=80)
    d=ImageDraw.Draw(im);d.rounded_rectangle((x,y,x+w,y+h),16,fill=(235,238,244))
    # fascia gialla leggermente inclinata
    band=Image.new('RGBA',(430,110),(0,0,0,0));bd=ImageDraw.Draw(band)
    bd.rounded_rectangle((8,8,422,102),8,fill=GIALLO)
    bd.text((28,38),nome,font=brico(40),fill=NAVY,anchor='lm')
    bd.text((28,78),ruolo,font=fig(22,True),fill=NAVY,anchor='lm')
    band=band.rotate(2,resample=Image.BICUBIC,expand=True)
    shadow(im,(x+4,y+h+16,x+w+10,y+h+108),r=10,blur=14,off=(0,6),alpha=60)
    im.alpha_composite(band,(x-12,y+h+4))
def parole_chiave(im,kw):
    if not kw:return
    d=ImageDraw.Draw(im);x=1428;y=640
    d.text((x,y),'PAROLE CHIAVE',font=fig(22,True),fill=GRIGIO,anchor='lm');y+=32
    for k in kw[:5]:
        f=fig(30,True);w=int(tw(d,k,f))+36
        d.rounded_rectangle((x,y,x+w,y+48),24,fill=(255,247,170),outline=(224,190,0),width=2)
        d.text((x+18,y+24),k,font=f,fill=NAVY,anchor='lm');y+=58
def card(im,x,y,w,testo,stato='off',size=40):
    """stato: 'on' (bordo+pallino gialli), 'off' (attenuata), 'neutra'. testo con **grassetto** iniziale opzionale."""
    d=ImageDraw.Draw(im);f=fig(size);fb=fig(size,True)
    m=re.match(r'\*\*(.+?)\*\*(.*)',testo,re.S);lead,rest=(m.group(1),m.group(2)) if m else ('',testo)
    inner=w-2*30-(34 if stato!='neutra' else 0)
    # righe: costruzione per parole con font diverso
    words=([(t,True) for t in lead.split(' ') if t]+[(t,False) for t in rest.split(' ') if t])
    lines=[[]];cw=0;sp=tw(d,' ',f)
    for t,b in words:
        ww=tw(d,t,fb if b else f)
        if cw+ww>inner and lines[-1]:lines.append([]);cw=0
        lines[-1].append((t,b,ww));cw+=ww+sp
    lh=int(size*1.3);hh=len(lines)*lh+36
    if stato=='on':fill=(255,255,255);ol=GIALLO;col=NAVY
    elif stato=='off':fill=(245,247,250);ol=(226,230,238);col=(105,112,130)
    else:fill=(255,255,255);ol=(226,230,238);col=NAVY
    shadow(im,(x,y,x+w,y+hh),r=20,blur=16,off=(0,8),alpha=40 if stato!='on' else 70)
    d.rounded_rectangle((x,y,x+w,y+hh),20,fill=fill,outline=ol,width=6 if stato=='on' else 3)
    tx=x+30+(34 if stato!='neutra' else 0)
    if stato!='neutra':
        d.ellipse((x+26,y+24,x+46,y+44),fill=GIALLO if stato=='on' else (200,205,215),outline=(224,190,0) if stato=='on' else None)
    for i,l in enumerate(lines):
        cx=tx
        for t,b,ww in l:
            d.text((cx,y+18+i*lh),t,font=fb if b else f,fill=col if not b else (NAVY if stato!='off' else col));cx+=ww+sp
    return hh
def card_h(testo,w,size=40,stato='on'):
    im=Image.new('RGBA',(10,10));return card(Image.new('RGBA',(W,H)),0,0,w,testo,stato,size)
def fit(im,box):
    bw,bh=box;r=min(bw/im.width,bh/im.height);return im.resize((max(1,int(im.width*r)),max(1,int(im.height*r))),Image.LANCZOS)
def opera(im,path,box,caption=None):
    """Disegna l'opera dentro box=(x,y,w,h), centrata, con ombra; didascalia sotto. Ritorna (x0,y0,x1,y1)."""
    a=Image.open(path).convert('RGBA');bx,by,bw,bh=box
    cap_h=0
    d=ImageDraw.Draw(im)
    if caption:
        fc=fig(24);lines=wrap(d,caption,fc,bw);cap_h=len(lines)*30+10
    a=fit(a,(bw,bh-cap_h));x=bx+(bw-a.width)//2;y=by
    shadow(im,(x,y,x+a.width,y+a.height),r=6,blur=14,off=(0,8),alpha=70);im.alpha_composite(a,(x,y))
    if caption:
        for i,l in enumerate(lines):d.text((bx+bw//2,y+a.height+22+i*30),l,font=fc,fill=(80,88,105),anchor='mm')
    return (x,y,x+a.width,y+a.height+cap_h)
