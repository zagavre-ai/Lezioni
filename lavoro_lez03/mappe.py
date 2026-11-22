# Mappe del prof ridisegnate nel modello BES: stesse parole, stessi rami; costruite ramo per ramo con la voce, riquadro acceso in giallo
import sys;sys.path.insert(0,'/home/user/Lezioni/lavoro_lez03')
from lib import *
import montaggio as M
from PIL import Image,ImageDraw,ImageFilter
import math
COL={'c':((255,220,198),(194,65,12)),'d':((220,238,251),(29,78,216)),'k':((255,243,191),(161,98,7)),'e':((221,243,228),(21,128,61)),'q':((235,227,247),(109,40,217)),'w':((255,255,255),(11,21,48))}
LEG=[('concetto centrale','c'),('date e sequenze','d'),('parole chiave','k'),('esempi e opere','e'),('conseguenze','q')]
MAPIMG='/tmp/w/mapimg/'
def draw_box(img,b,hl=False):
    d=ImageDraw.Draw(img);x,y,w,h=b['r'];fill,edge=COL.get(b['k'],((255,255,255),(0,0,0)))
    if hl:
        d.rounded_rectangle((x-10,y-10,x+w+10,y+h+10),(h//2+10 if b.get('ov') else 22),fill=GIALLO)
    if b['k']=='img':
        im=Image.open(b['img']).convert('RGB');ih=h-b.get('cap',0)
        s=min(w/im.size[0],ih/im.size[1]);im=im.resize((round(im.size[0]*s),round(im.size[1]*s)),Image.LANCZOS)
        ix=x+(w-im.size[0])//2
        d.rectangle((ix-4,y-4,ix+im.size[0]+4,y+im.size[1]+4),fill=(255,255,255),outline=(11,21,48),width=3);img.paste(im,(ix,y))
        f=F('m',34);L=wrap_plain(d,b['t'],f,w+40)
        for i,l in enumerate(L):d.text((x+w/2-d.textlength(l,font=f)/2,y+im.size[1]+10+i*42),l,font=f,fill=NOTTE)
        return
    d.rounded_rectangle((x,y,x+w,y+h),(h//2 if b.get('ov') else 16),fill=fill,outline=edge,width=5)
    f=F(b.get('f','m'),b.get('s',34));L=sum([wrap_plain(d,part,f,w-36) for part in b['t'].split('\n')],[]);lh=f.size*1.28;ty=y+(h-len(L)*lh)/2
    for i,l in enumerate(L):d.text((x+w/2-d.textlength(l,font=f)/2,ty+i*lh),l,font=f,fill=NOTTE)
def _edge(r,toward):
    x,y,w,h=r;cx,cy=x+w/2,y+h/2;dx,dy=toward[0]-cx,toward[1]-cy
    if dx==0 and dy==0:return cx,cy
    sx=(w/2+8)/abs(dx) if dx else 1e9;sy=(h/2+8)/abs(dy) if dy else 1e9;t=min(sx,sy)
    return cx+dx*t,cy+dy*t
def arrow(d,r0,r1,w=8):
    c0=(r0[0]+r0[2]/2,r0[1]+r0[3]/2);c1=(r1[0]+r1[2]/2,r1[1]+r1[3]/2)
    (x0,y0)=_edge(r0,c1);(x1,y1)=_edge(r1,c0)
    d.line((x0,y0,x1,y1),fill=NOTTE,width=w)
    a=math.atan2(y1-y0,x1-x0);L=30
    d.polygon([(x1,y1),(x1-L*math.cos(a-0.42),y1-L*math.sin(a-0.42)),(x1-L*math.cos(a+0.42),y1-L*math.sin(a+0.42))],fill=NOTTE)
def render_map(spec,shown,hl,screen_label,page=None):
    img=Image.new('RGB',(W,H),(255,255,255));d=ImageDraw.Draw(img)
    d.text((60,34),spec['kicker'],font=F('b',22),fill=TELESIO)
    # legenda in alto a destra
    x=1860
    for t,k in reversed(LEG):
        f=F('m',18);tw=d.textlength(t,font=f);x-=tw
        d.text((x,36),t,font=f,fill=NOTTE);x-=34
        fill,edge=COL[k];d.rounded_rectangle((x,38,x+24,56),4,fill=fill,outline=edge,width=3);x-=26
    d.line((60,78,1860,78),fill=(203,213,225),width=2)
    d.text((60,1040),"STORIA DELL'ARTE V",font=F('b',24),fill=TELESIO)
    t=screen_label;d.text((1860-d.textlength(t,font=F('b',24)),1040),t,font=F('b',24),fill=TELESIO)
    B=spec['boxes']
    for a in spec['arrows']:
        if a['to'] in shown and a['frm'] in shown:arrow(d,B[a['frm']]['r'],B[a['to']]['r'])
    for i,b in B.items():
        if i in shown:draw_box(img,b,hl=i in hl)
    return img

# ---------------- specifiche delle quattro schermate (parole del prof, 34-50 px)
def bx(k,r,t,**kw):return dict(k=k,r=r,t=t,**kw)
def A(frm,to):return dict(frm=frm,to=to)
def OV(r,t):return bx('w',r,t,ov=True)
FR_A=dict(kicker='MAPPA DEL PROFESSORE · 1 DI 2',
 boxes={'T':bx('c',(40,380,380,200),'REALISMO\nin Francia',f='x',s=50),
  'l1':OV((520,128,200,64),"cos'è"),'cose':bx('d',(860,95,990,130),'un movimento artistico e culturale sviluppatosi inizialmente in Francia, nella seconda metà del 1800'),
  'l2':OV((520,253,320,64),'viene chiamato'),'rom':bx('k',(940,245,520,80),'secondo Romanticismo'),
  'l3':OV((520,420,260,64),'arte diventa'),'spec':bx('k',(860,350,700,80),'«Specchio della realtà»'),'att':bx('q',(860,450,990,110),'pittura e scultura impongono una nuova attenzione al vero'),
  'l4':OV((520,800,240,64),'nei quadri'),
  'q1':bx('e',(860,660,990,70),'«Arte = frammento di uno specchio»'),'q2':bx('e',(860,742,990,70),'Colori «spessi» dati a spatolate. Nuove inquadrature'),
  'q3':bx('e',(860,824,990,70),'vita quotidiana'),'q4':bx('e',(860,906,990,70),'contadini, paesani')},
 arrows=[A('T','l1'),A('l1','cose'),A('T','l2'),A('l2','rom'),A('T','l3'),A('l3','spec'),A('l3','att'),A('T','l4'),A('l4','q1'),A('l4','q2'),A('l4','q3'),A('l4','q4')])
FR_ORDER=[(['T'],0),(['l1','cose'],1),(['l2','rom'],2),(['l3','spec'],3),(['att'],4),(['l4','q1'],5),(['q2'],6),(['q3'],7),(['q4'],8)]
FR_B=dict(kicker='MAPPA DEL PROFESSORE · 2 DI 2',
 boxes={'T':bx('c',(640,100,640,130),'REALISMO in Francia',f='x',s=50),
  'pit':OV((790,300,340,70),'pittori'),
  'n1':bx('k',(150,430,400,90),'Courbet',f='x',s=44),'n2':bx('k',(760,430,400,90),'Daumier',f='x',s=44),'n3':bx('k',(1370,430,400,90),'Millet',f='x',s=44),
  'f1':bx('k',(150,550,400,80),'«Faccio Arte viva»'),'f2':bx('k',(760,550,400,80),'«Gli ultimi»'),'f3':bx('k',(1370,550,400,80),'la vita della campagna'),
  'i1':bx('img',(100,660,500,340),"Atelier dell'artista 1855",img=MAPIMG+'atelier.png',cap=88),
  'i2':bx('img',(790,660,340,340),'La lavandaia 1863',img=MAPIMG+'lavandaia.png',cap=88),
  'i3':bx('img',(1380,660,380,340),'Le spigolatrici 1867',img=MAPIMG+'spigolatrici.png',cap=88)},
 arrows=[A('T','pit'),A('pit','n1'),A('pit','n2'),A('pit','n3'),A('n1','f1'),A('n2','f2'),A('n3','f3')])
FR_B_ORDER=[(['T','pit'],9),(['n1','f1','i1'],10),(['n2','f2','i2'],11),(['n3','f3','i3'],12)]
IT_A=dict(kicker='MAPPA DEL PROFESSORE · 1 DI 2',
 boxes={'T':bx('c',(40,400,380,200),'REALISMO\nin Italia',f='x',s=50),
  'l1':OV((520,128,200,64),"cos'è"),'cose':bx('d',(860,95,990,130),'movimento artistico e letterario nato nella seconda metà del 1800'),
  'l2':OV((520,330,260,64),'arte diventa'),'spec':bx('k',(860,265,700,80),'«Specchio della realtà»'),'att':bx('q',(860,360,990,110),'pittura e scultura impongono una nuova attenzione al vero'),
  'tenta':bx('k',(520,520,520,130),'tenta di riprodurre la percezione della realtà'),'con':OV((1080,555,130,64),'con'),
  'mac':bx('k',(1250,500,600,80),'«Macchie di colore»'),'pen':bx('k',(1250,600,600,150),'pennellate larghe di colori puri; il colore è sciolto'),
  'l4':OV((520,840,220,64),'pittori'),'macc':bx('d',(860,800,500,80),'macchiaioli',f='b'),'nom':bx('d',(860,900,990,90),'• Fattori   • Sernesi   • Borrani   • Lega',s=38)},
 arrows=[A('T','l1'),A('l1','cose'),A('T','l2'),A('l2','spec'),A('l2','att'),A('T','tenta'),A('tenta','con'),A('con','mac'),A('con','pen'),A('T','l4'),A('l4','macc'),A('macc','nom')])
IT_ORDER=[(['T'],0),(['l1','cose'],1),(['l2','spec'],2),(['att'],3),(['tenta'],4),(['con','mac'],5),(['pen'],6),(['l4','macc','nom'],7)]
IT_B=dict(kicker='MAPPA DEL PROFESSORE · 2 DI 2',
 boxes={'T':bx('c',(560,100,800,130),'REALISMO in Italia',f='x',s=50),
  'vq':bx('c',(560,270,800,90),'nei quadri la vita quotidiana',f='b'),
  'b1':bx('e',(60,410,520,90),'Borghesia toscana',f='b'),'b2':bx('e',(660,410,600,110),'Risorgimento italiano (raccontato dai «non eroi»)',s=34),'b3':bx('e',(1340,410,520,90),'Ambiente',f='b'),
  'i1':bx('img',(30,550,290,400),'Lega Lo stornello 1867',img=MAPIMG+'lo_stornello.png',cap=88),'i2':bx('img',(330,550,290,400),'Fattori La rotonda di Palmieri 1866',img=MAPIMG+'rotonda.png',cap=88),
  'i3':bx('img',(650,550,290,400),'Borrani Le cucitrici delle camicie rosse 1854',img=MAPIMG+'cucitrici.png',cap=88),'i4':bx('img',(960,550,290,400),'Fattori In vedetta 1872',img=MAPIMG+'invedetta.png',cap=88),
  'i5':bx('img',(1280,550,290,400),'Fattori Libecciata 1880',img=MAPIMG+'libecciata.png',cap=88),'i6':bx('img',(1580,550,290,400),'Sernesi Tetti al sole 1860',img=MAPIMG+'tetti.png',cap=88)},
 arrows=[A('T','vq'),A('vq','b1'),A('vq','b2'),A('vq','b3')])
IT_B_ORDER=[(['T','vq'],8),(['b1','i1','i2'],9),(['b2','i3','i4'],10),(['b3','i5','i6'],11)]

FR_FRAGS=["Che cos'è il Realismo in Francia?","È un movimento artistico e culturale","Viene chiamato secondo Romanticismo.","L'arte diventa «specchio della realtà»","pittura e scultura impongono","Nei quadri: «Arte uguale","Colori «spessi»","Vita quotidiana.","Contadini, paesani.","I pittori sono","Courbet,","Daumier,","Millet,"]
IT_FRAGS=["Che cos'è il Realismo in Italia?","È un movimento artistico e letterario","L'arte diventa «specchio della realtà»","pittura e scultura impongono","Tenta di riprodurre","con «macchie di colore»","pennellate larghe","I pittori sono i macchiaioli","Nei quadri, la vita quotidiana.","La borghesia toscana","Il Risorgimento italiano","L'ambiente"]
