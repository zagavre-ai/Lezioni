# Montaggio completo: Parte 1 e Parte 2 della lezione 3 · Il Realismo
import sys,json,os,subprocess;sys.path.insert(0,'/home/user/Lezioni/lavoro_lez03')
from scene_doc import *
from kore import *
from ap import *
import mappe as MP
import montaggio as M
KIT='/home/user/Lezioni/kit/'
SUON=KIT+'suoni/'
ARGS=['Le nuove sfide del progresso e il racconto della realtà',"L'architettura del ferro, del vetro e l'urbanistica","L'Italia che cambia e l'architettura dell'Eclettismo",
      'La Scuola di Barbizon, Jean-François Millet e Gustave Courbet','Honoré Daumier e i Macchiaioli']
TITOLO='Il Realismo'
def spl(t):return [x.strip() for x in re.split(r'(?<=[.!?])\s+',t) if x.strip()]
def fr(s):return M.nfr(s)
# ------------------------------------------------ schermate bianche
def cover(cam=False,n_args=5):
    img=base(page=1,footer=True,logo_on=True);d=ImageDraw.Draw(img)
    d.text((80,150),"STORIA DELL'ARTE V · VIDEOLEZIONE",font=F('b',30),fill=TELESIO)
    d.text((80,196),TITOLO,font=F('t',150),fill=NOTTE);d.rectangle((80,372,300,380),fill=TELESIO)
    y=430;rows=ARGS[:n_args];h=len(rows)*70+90
    shadow(img,(80,y,1360,y+h),r=20,blur=14,off=(0,6),alpha=45);d=ImageDraw.Draw(img)
    d.rounded_rectangle((80,y,1360,y+h),20,fill=(255,255,255),outline=GRIGIO,width=3)
    d.text((112,y+22),'ARGOMENTI',font=F('b',24),fill=TELESIO)
    for i,a in enumerate(rows):
        d.ellipse((114,y+76+i*70+14,130,y+76+i*70+30),fill=TELESIO)
        d.text((152,y+76+i*70),a,font=F('m',36),fill=NOTTE)
    if cam:cam_frame(img)
    return img
def args_slide(active=None):
    img=base(page=2);d=ImageDraw.Draw(img)
    d.text((80,150),"STORIA DELL'ARTE V · VIDEOLEZIONE",font=F('b',28),fill=TELESIO)
    d.text((80,196),'Di cosa parliamo',font=F('t',100),fill=NOTTE);d.rectangle((80,330,300,338),fill=TELESIO)
    y=390
    for i,a in enumerate(ARGS):
        on=(i==active);h=100
        shadow(img,(80,y,1840,y+h),r=20,blur=12,off=(0,5),alpha=40 if on or active is None else 20);d=ImageDraw.Draw(img)
        d.rounded_rectangle((80,y,1840,y+h),20,fill=(255,255,255),outline=GIALLO if on else GRIGIO,width=8 if on else 3)
        if on:d.ellipse((1790,y+14,1816,y+40),fill=GIALLO,outline=NOTTE,width=2)
        col=NOTTE if (on or active is None) else (120,128,148)
        d.text((112,y+20),str(i+1),font=F('t',54),fill=TELESIO if col==NOTTE else col)
        d.text((190,y+28),a,font=F('b',42),fill=col)
        y+=h+22
    return img
def glossario(active,terms):
    img=rgba();blue_logo(img);d=ImageDraw.Draw(img)
    d.text((140,120),'GLOSSARIO',font=F('t',70),fill=GIALLO)
    for i,(t,df) in enumerate(terms):
        if i>active:break
        col=i%2;row=i//2;x=100+col*880;y=225+row*205;w=840;on=(i==active)
        d.rounded_rectangle((x,y,x+w,y+190),22,fill=(255,255,255,255) if on else (255,255,255,45),outline=GIALLO if on else (255,255,255,80),width=8 if on else 3)
        d.text((x+28,y+14),t,font=F('t',44),fill=TELESIO if on else GIALLO)
        L=wrap_plain(d,df,F('m',32),w-56)
        for j,l in enumerate(L[:3]):d.text((x+28,y+76+j*40),l,font=F('m',32),fill=NOTTE if on else (225,232,248))
    return img
def compito(k,n,testo,fine=None):
    img=rgba();blue_logo(img);d=ImageDraw.Draw(img)
    if fine:
        d.text((140,200),'COMPITI',font=F('b',34),fill=GIALLO)
        d.rounded_rectangle((120,300,1800,640),26,fill=(255,255,255,255),outline=GIALLO,width=8)
        for i,l in enumerate(wrap_plain(d,fine,F('b',52),1560)):d.text((170,340+i*76),l,font=F('b',52),fill=NOTTE)
        return img
    d.text((140,140),f'COMPITO {k} DI {n}',font=F('b',34),fill=GIALLO)
    for size in (46,42,40,38):
        L=wrap_plain(d,testo,F('m',size),1560);h=len(L)*round(size*1.5)+70
        if 220+h<1020:break
    d.rounded_rectangle((120,220,1800,220+h),26,fill=(255,255,255,255),outline=GIALLO,width=8)
    d.ellipse((1750,236,1778,264),fill=GIALLO)
    for i,l in enumerate(L):d.text((170,252+i*round(size*1.5)),l,font=F('m',size),fill=NOTTE)
    return img
# ------------------------------------------------ pezzi
def st(img,sec):return (M.save_png(img),fr(sec))
def title_piece(k):
    img=scheda_titolo(f'Argomento {k} di 5',ARGS[k-1])
    return M.still_piece(f'T{k}',[st(img,4.0)],[(SUON+'titolo.wav',0.2,0.9)],bg=make_bg())
def quiz_piece(k):
    t=['Le nuove sfide del progresso','Ferro, vetro e urbanistica',"L'Italia che cambia e l'Eclettismo",'Barbizon, Millet e Courbet','Daumier e i Macchiaioli'][k-1]
    return M.still_piece(f'Q{k}',[st(quiz_card(k,t),4.0)],[(SUON+'quiz.wav',0.5,0.9)],bg=make_bg())
def pill_lines(nome):
    s=spl(TESTI[nome]);rr=s[1:]
    if len(rr)<4:
        rr=[]
        for x in s[1:]:rr+=[y.strip() for y in re.split(r'(?<=[:;])\s+',x) if y.strip()]
    return s[0],rr
def pill_piece(k,header=None,nome=None,intro=None,prefix='P',jingle='repaso.wav'):
    nome=nome or f'S{k}';tit,righe=pill_lines(nome)
    pv,pd,_=voce(nome);tm=frasi_tempi(nome,righe)
    t0=0.4;iv=None
    ev=[(SUON+jingle,0.0,0.9)]
    if intro:
        iv,idur,_=voce(intro);ev.append((iv,t0,1.0));t0+=idur+0.35
    ev.append((pv,t0,1.0))
    total=t0+pd+1.6
    hdr=header or ARGS[k-1]
    states=[];prev=0.0
    # stati: nessuna riga accesa fino alla prima frase, poi una alla volta
    starts=[0.0]+[t0+t for t in tm]+[total]
    for i in range(len(righe)+1):
        a=starts[i] if i>0 else 0.0
        img=pillola(hdr,righe,i-1) if i>0 else pillola(hdr,[],-1)
        states.append(st(img,max(0.2,starts[i+1]-starts[i]) if i>0 else max(0.2,starts[1]-0.0)))
    return M.still_piece(f'{prefix}{k}',states,ev,bg=make_bg())
def ripasso_finale():
    tit,righe=pill_lines('RF');pv,pd,_=voce('RF');tm=frasi_tempi('RF',righe)
    t0=0.5;total=t0+pd+1.6;starts=[0.0]+[t0+t for t in tm]+[total]
    states=[st(pillola('Ripasso finale',[],-1,'RIPASSO'),starts[1])]
    for i in range(len(righe)):states.append(st(pillola('Ripasso finale',righe,i,'RIPASSO'),starts[i+2]-starts[i+1]))
    return M.still_piece('RF',states,[(SUON+'repaso.wav',0.0,0.9),(pv,t0,1.0)],bg=make_bg())
def glossario_piece():
    s=spl(TESTI['GL'])[1:];terms=[(x.split(':')[0].strip(),x.split(':',1)[1].strip()) for x in s]
    pv,pd,_=voce('GL');tm=frasi_tempi('GL',s);t0=0.5;total=t0+pd+1.6;starts=[0.0]+[t0+t for t in tm]+[total]
    states=[st(glossario(-1,terms),starts[1])]
    for i in range(len(terms)):states.append(st(glossario(i,terms),starts[i+2]-starts[i+1]))
    return M.still_piece('GL',states,[(SUON+'titolo.wav',0.0,0.9),(pv,t0,1.0)],bg=make_bg())
def cover_piece():
    pv,pd,_=voce('INTRO');s=spl(TESTI['INTRO']);tm=frasi_tempi('INTRO',s);t0=0.6
    total=t0+pd+1.0
    # le voci degli argomenti: dalla frase 2 in poi
    starts=[0.0]+[t0+t for t in tm[2:]]
    states=[];prev=0.0
    seq=[(0,0.0)]+[(i+1,starts[i+1]) for i in range(5)]
    for j,(n,t) in enumerate(seq):
        t2=seq[j+1][1] if j+1<len(seq) else total
        states.append(st(cover(False,n),max(0.1,t2-t)))
    return M.still_piece('CV',states,[(pv,t0,1.0)])
def args_piece():
    pv,pd,_=voce('ARG');s=spl(TESTI['ARG']);tm=frasi_tempi('ARG',s);t0=0.5;total=t0+pd+1.0
    starts=[0.0]+[t0+t for t in tm[1:]]+[total]
    states=[st(args_slide(None),starts[1])]
    for i in range(5):states.append(st(args_slide(i),starts[i+2]-starts[i+1]))
    return M.still_piece('AR',states,[(pv,t0,1.0)])
def sigla_piece(path,name):
    k=M.key_of('sigla',path);v=f'{M.OUT}/pezzi/{name}_{k}.mp4';a=f'{M.OUT}/pezzi/{name}_{k}.wav'
    if not os.path.exists(v):
        M.sh(['ffmpeg','-v','error','-y','-i',path,'-an','-vf','fps=30,scale=1920:1080,format=yuv420p','-c:v','libx264','-preset','veryfast','-crf','18','-r','30',v])
        M.sh(['ffmpeg','-v','error','-y','-i',path,'-vn','-ac','2','-ar','48000','-c:a','pcm_s16le',a])
    n=round(float(subprocess.run(['ffprobe','-v','error','-count_frames','-select_streams','v:0','-show_entries','stream=nb_read_frames','-of','csv=p=0',v],capture_output=True,text=True).stdout))
    return dict(v=v,a=a,n=n,name=name)
def fine_parte_piece(n):
    img=rgba();blue_logo(img);d=ImageDraw.Draw(img)
    d.text((140,380),f'FINE DELLA PARTE {n}',font=F('t',90),fill=(255,255,255));d.rectangle((140,500,360,510),fill=GIALLO)
    d.text((140,540),'La lezione continua nella Parte 2.',font=F('m',44),fill=(205,216,240))
    return M.still_piece('FP',[st(img,5.2)],[(SUON+'finale.wav',0.0,0.9)],bg=make_bg())
def compiti_intro():
    img=scheda_titolo('Per te','Compiti',None)
    return M.still_piece('CI',[st(img,3.5)],[(SUON+'titolo.wav',0.2,0.9)],bg=make_bg())
def compiti_piece():
    c=json.load(open('/tmp/w/cons/compiti.json'))['esercizi'];n=len(c)
    pv,pd,_=voce('COMPITI')
    frs=['I compiti.']+[x['testo'][:30] for x in c]+['Svolgi i compiti qui sotto']
    # i compiti: Primo/Secondo/... iniziano dopo l'etichetta ordinale
    tm=frasi_tempi('COMPITI',['Primo:','Secondo:','Terzo:','Quarto:','Svolgi i compiti qui sotto'])
    t0=0.5;total=t0+pd+1.2;starts=[t0+t for t in tm]
    states=[st(compito(0,n,'',fine=None) if False else compito(1,n,c[0]['testo']),starts[1]-0.0)]
    for i in range(1,n):states.append(st(compito(i+1,n,c[i]['testo']),starts[i+1]-starts[i]))
    states.append(st(compito(0,n,'',fine='Svolgi i compiti qui sotto e premi Consegna: arrivano al docente nel tuo quaderno dei compiti.'),total-starts[n]))
    return M.still_piece('CP',states,[(pv,t0,1.0)],bg=make_bg())
def verifica_piece():
    pv,pd,_=voce('VER');img=rgba();blue_logo(img);d=ImageDraw.Draw(img)
    d.text((140,330),'VERIFICA',font=F('t',140),fill=GIALLO);d.text((140,500),'DI SBARRAMENTO',font=F('t',70),fill=(255,255,255))
    tbox(d,(140,620),'Dieci domande su tutta la lezione. Per continuare serve almeno l\'80% di risposte esatte.',F('m',40),(205,216,240),maxw=1500)
    t0=3.0;total=t0+pd+1.2
    return M.still_piece('VE',[st(img,total)],[(SUON+'quiz.wav',0.5,0.9),(pv,t0,1.0)],bg=make_bg())
# ---------------------------------------------- mappe
def map_pieces(nome,specA,ordA,specB,ordB,frags,prefix,pageA,pageB):
    pv,pd,_=voce(nome);tm=frasi_tempi(nome,frags)
    tB=tm[9] if prefix=='MFR' else tm[8]
    cut=max(0.5,tB-0.3);out=[]
    for scr,(spec,order,pg) in enumerate(((specA,ordA,pageA),(specB,ordB,pageB)),1):
        if scr==1:ss=0.0;dur=cut
        else:ss=cut;dur=pd-cut
        t0=0.4;shown=set();states=[];ev=[(pv,t0,1.0,ss,dur)]
        steps=[(ids,tm[fi]-ss+t0) for ids,fi in order]
        total=t0+dur+(3.0 if scr==1 else 4.0)
        steps[0]=(steps[0][0],0.0)
        for i,(ids,t) in enumerate(steps):
            shown|=set(ids);nxt=steps[i+1][1] if i+1<len(steps) else t0+dur
            states.append(st(MP.render_map(spec,shown,set(ids),f'Pagina {pg}'),max(0.1,nxt-t)))
        states.append(st(MP.render_map(spec,shown,set(),f'Pagina {pg}'),total-(t0+dur)))
        out.append(M.still_piece(f'{prefix}{scr}',states,ev))
    return out
def mappa_finale():
    pv,pd,_=voce('MAPFIN');sts=[]
    sp=[(MP.FR_A,MP.FR_ORDER),(MP.FR_B,MP.FR_B_ORDER),(MP.IT_A,MP.IT_ORDER),(MP.IT_B,MP.IT_B_ORDER)]
    for s_,o in sp:
        allb=set(sum([x[0] for x in o],[]));sts.append(st(MP.render_map(s_,allb,set(),'Mappa finale'),max(3.5,(0.4+pd+0.8)/4)))
    return M.still_piece('MF',sts,[(pv,0.4,1.0)])
