# Mappa del docente (Neoclassicismo) ridisegnata nitida nel modello BES: stessa struttura, stesse parole.
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from lib import *
COL={'centrale':((255,218,200),(200,70,20)),'date':((220,236,252),(32,80,200)),'chiave':((255,243,196),(160,105,10)),'esempi':((221,242,228),(25,125,70)),'conseg':((234,226,247),(110,50,200))}
LEG=[('centrale','concetto centrale'),('date','date e sequenze'),('chiave','parole chiave'),('esempi','esempi e opere'),('conseg','conseguenze')]
# (id, x,y,w,h, etichetta(bold)|None, testo, colore, padre)
N=[
 ('c',620,95,680,90,None,"NEOCLASSICISMO · ARTE",'centrale',None),
 ('b1',40,225,400,225,"cos'è","movimento artistico e culturale, che riscopre l'arte classica greco-romana",'chiave','c'),
 ('b2',470,225,400,225,"nasce","in contrasto alle stravaganze del Barocco e del Rococò",'chiave','c'),
 ('b3',1050,225,400,225,"periodo","1750 - 1815: Illuminismo, Rivoluzione francese, Napoleone",'date','c'),
 ('r',1480,225,400,150,None,"rinasce l'interesse per l'arte classica grazie a",'chiave','c'),
 ('r1',1480,400,400,100,None,"scoperta di Pompei ed Ercolano",'esempi','r'),
 ('r2',1480,520,400,100,None,"Winckelmann (archeologo)",'esempi','r'),
 ('A',40,650,560,66,None,"ARCHITETTURA",'chiave','c'),
 ('a1',40,750,560,150,None,"rispetto al Barocco non ci sono decorazioni e le forme sono semplici",'chiave','A'),
 ('a2',40,934,560,110,None,"G. Piermarini, L. Cagnola, L. Pollack",'esempi','a1'),
 ('S',680,650,560,66,None,"SCULTURA",'chiave','c'),
 ('s1',680,750,560,150,None,"soggetti idealizzati, perfetti",'chiave','S'),
 ('s2',680,934,560,110,None,"Antonio Canova",'esempi','s1'),
 ('P',1320,650,560,66,None,"PITTURA",'chiave','c'),
 ('p1',1320,750,560,150,None,"temi storici e mitologici",'chiave','P'),
 ('p2',1320,934,560,110,None,"Jacques-Louis David, J.A. Dominique Ingres",'esempi','p1'),
]
# percorsi delle frecce (polilinee, punta sull'ultimo segmento): id figlio -> punti
EDGE={
 'b1':[(960,185),(960,210),(240,210),(240,222)],
 'b2':[(960,210),(670,210),(670,222)],
 'b3':[(960,210),(1250,210),(1250,222)],
 'r':[(1250,210),(1680,210),(1680,222)],
 'r1':[(1465,300),(1465,450),(1477,450)],
 'r2':[(1465,450),(1465,570),(1477,570)],
 'A':[(960,210),(960,633),(320,633),(320,647)],
 'S':[(960,633),(960,647)],
 'P':[(960,633),(1600,633),(1600,647)],
 'a1':[(320,716),(320,747)],'a2':[(320,900),(320,931)],
 's1':[(960,716),(960,747)],'s2':[(960,900),(960,931)],
 'p1':[(1600,716),(1600,747)],'p2':[(1600,900),(1600,931)],
}
IDX={n[0]:i for i,n in enumerate(N)}
def box(d,n,hl=False,size=34):
    i,x,y,w,h,et,tx,col,par=n;fill,ol=COL[col]
    if hl:fill=(255,230,0)
    d.rounded_rectangle((x,y,x+w,y+h),18,fill=fill,outline=ol,width=5)
    f=fig(size,False);fb=fig(size,True)
    lines=[];
    if et:
        words=[(t,True) for t in (et+':').split()]+[(t,False) for t in tx.split()]
    else:words=[(t,False) for t in tx.split()]
    big=n[0]=='c' or n[0] in('A','S','P')
    if big:f=brico(46 if n[0]=='c' else 38);words=[(t,False) for t in tx.split()]
    cur=[];cw=0;sp=d.textlength(' ',font=f)
    for t,b in words:
        ww=d.textlength(t,font=fb if b else f)
        if cw+ww>w-40 and cur:lines.append(cur);cur=[];cw=0
        cur.append((t,b,ww));cw+=ww+sp
    if cur:lines.append(cur)
    lh=int((46 if n[0]=='c' else 38 if big else size)*1.28);th=len(lines)*lh
    y0=y+(h-th)//2
    for k,l in enumerate(lines):
        tw_=sum(t[2] for t in l)+sp*(len(l)-1);cx=x+(w-tw_)/2
        for t,b,ww in l:
            d.text((cx,y0+k*lh),t,font=fb if b else f,fill=NAVY);cx+=ww+sp
def freccia(d,pts,col=NAVY):
    import math
    for (x0,y0),(x1,y1) in zip(pts[:-1],pts[1:-1]+[pts[-1]]):
        pass
    for i in range(len(pts)-1):
        (x0,y0),(x1,y1)=pts[i],pts[i+1];d.line((x0,y0,x1,y1),fill=col,width=6)
    (x0,y0),(x1,y1)=pts[-2],pts[-1]
    ang=math.atan2(y1-y0,x1-x0);L=22
    p=[(x1+3*math.cos(ang),y1+3*math.sin(ang)),(x1-L*math.cos(ang-0.5),y1-L*math.sin(ang-0.5)),(x1-L*math.cos(ang+0.5),y1-L*math.sin(ang+0.5))]
    d.polygon(p,fill=col)
def stato(k,tutti=False,pagina=None):
    """k: numero di riquadri visibili (0..len(N)); il k-esimo (indice k-1) e' acceso in giallo, salvo tutti=True"""
    im=Image.new('RGBA',(W,H),(255,255,255,255));d=ImageDraw.Draw(im)
    d.text((40,38),"MAPPA · CHE COS'È IL NEOCLASSICISMO?",font=fig(26,True),fill=BLU,anchor='lm')
    x=1840
    for key,t in reversed(LEG):
        f=fig(23,True);w=int(d.textlength(t,font=f));x-=w
        d.text((x,38),t,font=f,fill=NAVY,anchor='lm');x-=44
        d.rounded_rectangle((x,26,x+32,50),6,fill=COL[key][0],outline=COL[key][1],width=3);x-=34
    d.line((40,80,1880,80),fill=(225,229,236),width=2)
    vis=len(N) if tutti else k
    for i in range(vis):
        n=N[i]
        if n[0] in EDGE:freccia(d,EDGE[n[0]])
    for i in range(vis):
        box(d,N[i],hl=(not tutti and i==vis-1))
    d.text((40,1068),"STORIA DELL'ARTE V",font=fig(22,True),fill=BLU,anchor='lm')
    if pagina:d.text((1880,1068),f'Pagina {pagina}',font=fig(22,True),fill=BLU,anchor='rm')
    return im
if __name__=='__main__':
    stato(len(N),True).convert('RGB').save('/tmp/w/mappa_t.png')
