import sys,os,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from lib import *
from PIL import Image
CX0,CX1=80,1360
def clean(t):return re.sub(r'\*\*','',t)
def finestra(cards,i,maxn=3):
    """indici visibili: ultimi 3 fino alla card attiva i (per slide con piu' di 3 card)"""
    if len(cards)<=maxn:return list(range(len(cards)))
    a=max(0,min(i-1,len(cards)-maxn)) if i>=0 else 0
    return list(range(a,a+maxn))
def slide(s,attiva,argn,argtit,pagina,tit_override=None):
    """s: dict slide (piano), attiva: indice card attiva (-1 nessuna). Ritorna RGBA con il posto per il prof."""
    im=base(pagina=pagina,etichetta=f"{argn:02d} · {argtit}")
    prof_box(im);parole_chiave(im,s['kw'])
    d=ImageDraw.Draw(im)
    cards=[c[1] for c in s['cards']]
    y0=titolo(im,tit_override or s['titolo'],y=196,size=60 if s['tipo']=='txt' else 52)
    if s['tipo']=='txt':
        vis=finestra(cards,attiva);y=y0+4;gap=22
        for i in vis:
            st='on' if i==attiva else 'off'
            if s.get('fisso') and attiva<0:st='neutra'
            h=card(im,CX0,y,CX1-CX0,cards[i],st);y+=h+gap
        if y-gap>950:print('!! overflow txt',s['titolo'],y)
    else:
        imgs=s['img'];n=len(imgs)
        ar=lambda k:(lambda a:a.width/a.height)(Image.open(ASSET+k+'.png'))
        pan=n==1 and ar(imgs[0][0])>2.0
        top=y0+0
        if pan:
            box=(CX0,top,CX1-CX0,380)
            opera(im,ASSET+imgs[0][0]+'.png',box,imgs[0][1])
            y=top+380+30;vis=finestra(cards,attiva,1) if attiva>=0 else [0]
            for i in ([attiva] if attiva>=0 else []):
                h=card(im,CX0,y,CX1-CX0,cards[i],'on')
        else:
            iw=700;ih=940-top
            if n==1:opera(im,ASSET+imgs[0][0]+'.png',(CX0,top,iw,ih),imgs[0][1])
            else:
                hh=(ih-20)//n
                for j,(k,cap) in enumerate(imgs):opera(im,ASSET+k+'.png',(CX0,top+j*(hh+20),iw,hh),cap)
            cx=CX0+iw+40;cw=CX1-cx;y=top
            idx=[] 
            if attiva>=0:
                idx=[attiva]
                if attiva>0:
                    hp=card_h(cards[attiva-1],cw,stato='off');ha=card_h(cards[attiva],cw,stato='on')
                    if hp+ha+22<=940-top:idx=[attiva-1,attiva]
            for i in idx:
                h=card(im,cx,y,cw,cards[i],'on' if i==attiva else 'off');y+=h+22
            if y>960:print('!! overflow img',s['titolo'],attiva,y)
    return im
if __name__=='__main__':
    import piano
    s=piano.SLIDE[1][3];slide(s,1,1,"Le origini: Grand Tour, musei e moda",5).convert('RGB').save('/tmp/w/t1.png')
    s=piano.SLIDE[1][4];slide(s,1,1,"Le origini: Grand Tour, musei e moda",6).convert('RGB').save('/tmp/w/t2.png')
    s=piano.SLIDE[3][1];slide(s,2,3,"L'architettura in Italia e in Europa",9).convert('RGB').save('/tmp/w/t3.png')
    s=piano.SLIDE[5][4];slide(s,5,5,"La pittura: David e Ingres",9).convert('RGB').save('/tmp/w/t4.png')

def slide_cover_prof(pagina=1):
    im=base(pagina=pagina)
    prof_box(im);d=ImageDraw.Draw(im)
    d.text((80,330),"STORIA DELL'ARTE V",font=fig(34,True),fill=BLU,anchor='lm')
    f=brico(120)
    d.text((80,470),"Il Neoclassicismo",font=f,fill=NAVY,anchor='lm')
    d.rounded_rectangle((80,550,165,556),3,fill=BLU)
    d.text((80,640),"Il ritorno all'antico",font=brico(64),fill=BLU,anchor='lm')
    return im

# ---------- dispensa: una pagina per slide (con tutte le card; le slide lunghe continuano sulla pagina dopo) ----------
def chunks(s):
    """lista di liste di indici di card per pagina di dispensa"""
    cards=[c[1] for c in s['cards']]
    if s['tipo']=='txt':return [list(range(len(cards)))]
    cw=(CX1-(CX0+700+40));ih=940-250
    out=[];cur=[];y=0
    for i,t in enumerate(cards):
        h=card_h(t,cw,size=32,stato='neutra')+18
        if cur and y+h>690:out.append(cur);cur=[];y=0
        cur.append(i);y+=h
    if cur:out.append(cur)
    return out
def slide_dispensa(s,argn,argtit,pagina,chunk,cam_png=None,cont=None):
    im=base(pagina=pagina,etichetta=f"{argn:02d} · {argtit}")
    prof_box(im,nome="",ruolo="") if False else None
    # riquadro: foto del docente (fermo immagine per la stampa) senza fascia con il nome
    x,y,w,h=CAM
    if cam_png and os.path.exists(cam_png):
        c=Image.open(cam_png).convert('RGBA').resize((w,h));m=Image.new('L',(w,h),0);ImageDraw.Draw(m).rounded_rectangle((0,0,w-1,h-1),16,fill=255)
        shadow(im,(x,y,x+w,y+h),r=16,blur=18,off=(0,8),alpha=80);im.paste(c,(x,y),m)
    parole_chiave(im,s['kw'])
    d=ImageDraw.Draw(im)
    cards=[c[1] for c in s['cards']]
    tit=s['titolo']+(' (continua)' if cont else '')
    y0=titolo(im,tit,y=196,size=60 if s['tipo']=='txt' else 52)
    if s['tipo']=='txt':
        yy=y0+4
        for i in chunk:
            hh=card(im,CX0,yy,CX1-CX0,cards[i],'neutra');yy+=hh+22
    else:
        imgs=s['img'];top=y0;iw=700;ih=940-top
        if len(imgs)==1:opera(im,ASSET+imgs[0][0]+'.png',(CX0,top,iw,ih),imgs[0][1])
        else:
            hh=(ih-20)//len(imgs)
            for j,(k,cap) in enumerate(imgs):opera(im,ASSET+k+'.png',(CX0,top,iw,hh) if False else (CX0,top+j*(hh+20),iw,hh),cap)
        cx=CX0+iw+40;cw=CX1-cx;yy=top
        for i in chunk:
            hh=card(im,cx,yy,cw,cards[i],'neutra',size=32);yy+=hh+18
    return im
