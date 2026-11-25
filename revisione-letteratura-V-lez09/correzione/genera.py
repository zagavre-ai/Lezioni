# Genera: (1) mappa del professore (3 schermate, ramo per ramo) come video muto 118,6 s;
#         (2) pannelli ingranditi del testo (T2 e L'assiuolo). Vettoriale/PIL a 1920x1080.
import sys, os, json
from PIL import Image, ImageDraw, ImageFont, ImageFilter
F='/home/user/Lezioni/kit/caratteri/'
def f(n,s): return ImageFont.truetype(F+n,s)
OUT=sys.argv[1]; os.makedirs(OUT,exist_ok=True)
W,H=1920,1080
NAVY=(11,21,48); BLUE=(32,96,175); YEL=(255,230,0)
COL={ # fill, border  (pesca, celeste, paglierino, menta, lilla)
 'c':((255,218,196),(214,84,38)),'d':((220,235,250),(32,96,175)),
 'k':((255,243,190),(176,128,16)),'e':((220,243,228),(40,150,88)),'l':((230,222,247),(123,79,201))}
LEG=[('c','concetto centrale'),('d','date e sequenze'),('k','parole chiave'),('e','esempi e opere'),('l','conseguenze')]
FS=35; LH=45; PAD=13
fb=f('Figtree-Medium.ttf',FS); ft=f('BricolageGrotesque-ExtraBold.ttf',44)
fl=f('Figtree-Regular.ttf',22); fh=f('Figtree-Bold.ttf',22)
def wrap(d,t,font,w):
    out=[];cur=''
    for wd in t.split(' '):
        tt=(cur+' '+wd).strip()
        if d.textlength(tt,font=font)<=w: cur=tt
        else: out.append(cur);cur=wd
    out.append(cur);return out
_d=ImageDraw.Draw(Image.new('RGB',(10,10)))
class Box:
    def __init__(s,key,text,x,y,w,kind,font=None,center=True):
        s.k=key;s.kind=kind;s.x=x;s.y=y;s.w=w;s.font=font or fb
        s.lines=wrap(_d,text,s.font,w-2*20)
        lh=LH if s.font is fb else 54
        s.h=len(s.lines)*lh+2*PAD;s.lh=lh
    def draw(s,im,hl):
        d=ImageDraw.Draw(im)
        fill,bd=COL[s.kind]
        if hl:
            g=Image.new('RGBA',(W,H),(0,0,0,0));gd=ImageDraw.Draw(g)
            gd.rounded_rectangle((s.x-4,s.y-4,s.x+s.w+4,s.y+s.h+4),14,outline=YEL+(255,),width=10)
            g=g.filter(ImageFilter.GaussianBlur(5));im.paste(g,(0,0),g);d=ImageDraw.Draw(im)
        d.rounded_rectangle((s.x,s.y,s.x+s.w,s.y+s.h),12,fill=fill,outline=YEL if hl else bd,width=6 if hl else 4)
        for i,l in enumerate(s.lines):
            tw=d.textlength(l,font=s.font)
            d.text((s.x+(s.w-tw)/2,s.y+PAD+i*s.lh-2),l,font=s.font,fill=NAVY)
    @property
    def r(s): return s.x+s.w
    @property
    def b(s): return s.y+s.h
    @property
    def cy(s): return s.y+s.h/2
def arrow(d,p,q,wd=5):
    d.line([p,q],fill=NAVY,width=wd)
    import math
    a=math.atan2(q[1]-p[1],q[0]-p[0]);L=22
    pts=[q,(q[0]-L*math.cos(a-0.4),q[1]-L*math.sin(a-0.4)),(q[0]-L*math.cos(a+0.4),q[1]-L*math.sin(a+0.4))]
    d.polygon(pts,fill=NAVY)
def base(page):
    im=Image.new('RGB',(W,H),'white');d=ImageDraw.Draw(im)
    d.text((40,28),'MAPPA DEL PROFESSORE',font=fh,fill=BLUE)
    x=W-40
    for k,t in reversed(LEG):
        tw=d.textlength(t,font=fl);x-=tw;d.text((x,28),t,font=fl,fill=NAVY);x-=34
        d.rounded_rectangle((x,30,x+24,52),5,fill=COL[k][0],outline=COL[k][1],width=3);x-=26
    d.line([(40,70),(W-40,70)],fill=(215,220,230),width=2)
    d.text((40,H-52),'LETTERATURA ITALIANA V',font=fh,fill=BLUE)
    t='Pagina %d'%page;d.text((W-40-d.textlength(t,font=fh),H-52),t,font=fh,fill=BLUE)
    return im
TITLE='Giovanni Pascoli · 1855 – 1912'
def S1():
    B={};Y0=100
    B['t']=Box('t',TITLE,40,Y0,790,'c',ft)
    y=Y0+B['t'].h+30
    B['vita']=Box('vita','La vita',40,y,210,'k')
    items=[('d','1855 – nasce a San Mauro di Romagna (Forlì)','d'),('dl','dall’età di 12 anni: lutti familiari e difficoltà economiche','l'),
     ('uni','studia all’università di Bologna: (come docente ha Carducci)','d'),('gr','si laurea in greco','k'),
     ('i06','1906 – insegna all’università di Bologna (prende il posto di Carducci)','d'),
     ('cv','si rifugia spesso nella sua casa di Castelvecchio di Barga (Lucca)','k'),('m','1912 – muore a Bologna','d')]
    yy=y;order=['t','vita']
    for k,t,c in items:
        B[k]=Box(k,t,300,yy,880,c);yy+=B[k].h+12;order.append(k)
    B['pers']=Box('pers','La personalità',1260,Y0+8,330,'k')
    p=[('pess','pessimismo: impossibile per l’uomo cambiare il corso degli eventi'),('senso','il senso della vita è nascosto nelle piccole cose e gioie di ogni giorno'),('soc','idee socialiste')]
    yy=B['pers'].b+36
    for k,t in p: B[k]=Box(k,t,1260,yy,620,'k');yy+=B[k].h+12
    arrows=[('t','vita',lambda B:((B['t'].x+70,B['t'].b),(B['vita'].x+70,B['vita'].y))),
            ('vita','d',lambda B:((B['vita'].r,B['d'].cy),(B['d'].x,B['d'].cy))),
            ('pers','pess',lambda B:((B['pers'].x+B['pers'].w/2,B['pers'].b),(B['pers'].x+B['pers'].w/2,B['pess'].y))),
            ('t','pers',lambda B:((B['t'].r,B['pers'].cy),(B['pers'].x,B['pers'].cy)))]
    order+= ['pers','pess','senso','soc']
    # (key, onset s in segment)
    ev=[('t',0.9),('vita',1.3),('d',4.1),('dl',10.0),('uni',14.6),('gr',19.4),('i06',21.0),('cv',26.6),('m',32.7),('pers',36.5),('pess',38.7),('senso',44.4),('soc',51.1)]
    return B,arrows,ev,['t','vita']
def S2():
    B={};Y0=100
    B['t']=Box('t',TITLE,40,Y0,790,'c',ft)
    y=Y0+B['t'].h+30
    B['poet']=Box('poet','La poetica',40,y,230,'k')
    L=[('es','esponente del Decadentismo italiano','k',None),('sof','la sofferenza della vita si riflette nella poesia','k','vita, un mistero fatto di dolori e ingiustizie'),
       ('nat','la natura come fonte di ispirazione','k','immagini, impressioni e sensazioni'),('lin','linguaggio nuovo: parole e frasi onomatopeiche','k','Don… Don… E mi dicono, Dormi!'),
       ('cor','“corrispondenze”: tra parole ed immagini','k',None)]
    yy=y;arrows=[('t','poet',lambda B:((B['t'].x+70,B['t'].b),(B['poet'].x+70,B['poet'].y))),
                 ('poet','es',lambda B:((B['poet'].r,B['poet'].cy),(B['es'].x,B['es'].cy)))]
    ev=[('t',59.0),('poet',59.4),('es',60.7)]
    tm={'sof':(63.6,64.0),'nat':(70.3,70.7),'lin':(75.3,75.7),'cor':(79.4,None)}
    for k,t,c,r in L:
        B[k]=Box(k,t,320,yy,640,c)
        if r:
            B[k+'r']=Box(k+'r',r,1060,yy,820,'e')
            B[k+'r'].y=yy+(B[k].h-B[k+'r'].h)/2
            arrows.append((k,k+'r',(lambda kk:lambda B:((B[kk].r,B[kk].cy),(B[kk+'r'].x,B[kk+'r'].cy)))(k)))
        yy+=B[k].h+22
    for k,(a,b2) in tm.items():
        ev.append((k,a))
        if b2: ev.append((k+'r',b2))
    return B,arrows,ev,['t','poet']
def S3():
    B={};Y0=100
    B['t']=Box('t',TITLE,40,Y0,790,'c',ft)
    B['op']=Box('op','Le opere',900,Y0+8,230,'k')
    y=Y0+B['t'].h+40
    B['racc']=Box('racc','raccolte poetiche',40,y,400,'k')
    R=[('my','Myricae · 1891 – temi familiari e paesaggistici'),('pp','Primi poemetti · 1897-1909 – condizione dell’uomo'),
       ('cc','Canti di Castelvecchio · 1903 – “piccole cose” e il mistero della morte e del cosmo'),('pc','Poemi Conviviali · 1904 – fatti e miti dell’antichità')]
    yy=y;arrows=[('t','op',lambda B:((B['t'].r,B['op'].cy),(B['op'].x,B['op'].cy))),
                 ('op','racc',lambda B:((B['op'].x+30,B['op'].b),(B['racc'].x+200,B['racc'].y))),
                 ('racc','my',lambda B:((B['racc'].r,B['racc'].cy),(B['my'].x,B['racc'].cy)))]
    for k,t in R: B[k]=Box(k,t,500,yy,1380,'e');yy+=B[k].h+12
    yy+=30
    B['pro']=Box('pro','prosa',40,yy,400,'k')
    B['fa']=Box('fa','Il fanciullino · 1897 – sul significato della poesia: il poeta guarda la realtà con gli occhi stupidi del bambino',500,yy,1380,'e')
    B['pro'].y=yy+(B['fa'].h-B['pro'].h)/2
    yy+=B['fa'].h+14
    B['ora']=Box('ora','orazione',40,yy,400,'k')
    B['gp']=Box('gp','La grande proletaria si è mossa · 1911 – discorso per i caduti della guerra italiana in Libia',500,yy,1380,'e')
    B['ora'].y=yy+(B['gp'].h-B['ora'].h)/2
    arrows+= [('pro','fa',lambda B:((B['pro'].r,B['pro'].cy),(B['fa'].x,B['pro'].cy))),('ora','gp',lambda B:((B['ora'].r,B['ora'].cy),(B['gp'].x,B['ora'].cy)))]
    ev=[('t',87.9),('op',88.3),('racc',88.7),('my',90.3),('pp',95.3),('cc',98.4),('pc',105.6),('pro',109.2),('fa',109.6),('ora',111.0),('gp',111.4)]
    return B,arrows,ev,['t','op']
def render(S,page,visible,hl):
    B,arrows,ev,_=S
    im=base(page);d=ImageDraw.Draw(im)
    for a,b,fn in arrows:
        if a in visible and b in visible: arrow(d,*fn(B))
    for k in visible: B[k].draw(im,k==hl)
    return im
def states(S,page):
    B,arrows,ev,pre=S
    out=[];vis=list(pre)
    for k,t in ev:
        if k not in vis: vis.append(k)
        out.append((t,render(S,page,list(vis),k)))
    out.append(('final',render(S,page,list(vis),None)))
    return out
if __name__=='__main__':
    # sequenza: (tempo inizio, immagine)
    seq=[]
    SEG=[(S1(),2,0.0,57.6),(S2(),3,58.0,87.2),(S3(),4,87.6,118.6)]
    allst=[]
    for S,pg,t0,t1 in SEG:
        st=states(S,pg)
        # primo stato (pre) visibile dall'inizio dello schermo
        first=render(S,pg,S[3],None)
        evs=[(t0,first)]
        for i,(t,im) in enumerate(st[:-1]): evs.append((max(t,t0),im))
        # tenuta finale: dall'ultimo evento alla fine; cattura la mappa intera
        # momento in cui finisce la voce: 3,5 s prima della fine dello schermo
        allst.append((evs,st[-1][1],t0,t1))
    # costruisci lista fotogrammi 30 fps
    FPS=30;N=int(round(118.6*FPS));frames=[]
    timeline=[]
    for evs,fin,t0,t1 in allst:
        for i,(t,im) in enumerate(evs): timeline.append((t,im))
        timeline.append((None,fin))
    # tempi di fine voce per schermo (dove la mappa intera si ferma)
    fin_t=[54.7,83.6,115.2]
    tl=[];fi=0
    for si,(evs,fin,t0,t1) in enumerate(allst):
        for t,im in evs: tl.append((t,im))
        tl.append((fin_t[si],fin))
    tl.sort(key=lambda x:x[0])
    os.makedirs(OUT+'/s',exist_ok=True)
    lines=[]
    imgs=[]
    for i,(t,im) in enumerate(tl):
        p=OUT+'/s/%02d.png'%i;im.save(p);imgs.append(p)
    # dissolvenze 0,4 s ai cambi di schermo
    import math
    cuts=[(57.6,tl,0,1),(87.2,tl,0,2)]
    # indici
    def idx(t): 
        r=0
        for i,(tt,_) in enumerate(tl):
            if tt<=t+1e-6: r=i
        return r
    xf={57.6:(idx(57.5),idx(58.0)),87.2:(idx(87.1),idx(87.6))}
    json.dump({'tl':[t for t,_ in tl],'xf':{str(k):v for k,v in xf.items()}},open(OUT+'/tl.json','w'))
    # per ogni fotogramma scegli immagine
    xfn=0
    for n in range(N):
        t=n/FPS
        pick=idx(t)
        cur=Image.open(imgs[pick]) if False else None
        frames.append((t,pick))
    # scrivi: fotogrammi unici o miscelati
    cache={}
    def get(i):
        if i not in cache: cache[i]=Image.open(imgs[i]).convert('RGB')
        return cache[i]
    # lista concat: durata costante per immagine, fotogrammi singoli per le dissolvenze
    items=[];  # (path,dur)
    n=0
    while n<N:
        t=n/FPS;blend=None
        for c,(a,b) in xf.items():
            c=float(c)
            if c<=t<c+0.4: blend=(c,a,b)
        if blend:
            c,a,b=blend
            im=Image.blend(get(a),get(b),(t-c)/0.4);p=OUT+'/f%05d.png'%n;im.save(p,compress_level=1)
            items.append((p,1/FPS));n+=1;continue
        pick=idx(t);m=n
        while m<N:
            tm=m/FPS
            if idx(tm)!=pick or any(float(c)<=tm<float(c)+0.4 for c in xf): break
            m+=1
        items.append((imgs[pick],(m-n)/FPS));n=m
    with open(OUT+'/lista.txt','w') as fh:
        for p,dur in items: fh.write("file '%s'\nduration %.6f\n"%(os.path.abspath(p),dur))
        fh.write("file '%s'\n"%os.path.abspath(items[-1][0]))
    print('items',len(items))
