import os,sys,re,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from asm import *
from asm import _lista
import blu,voci,piano
from lib import *
def png(im,key):
    p=ST+key+'.png';im.save(p);return p
def pezzo_voce(name,layout,n,ev,tv,vpath,vdur,jingles=(),tail=1.2,pre_states=None,fade=(0.35,0.35),extra_end=0):
    """layout(k)->RGBA layer (k=-1 iniziale..n-1); ev: tempi (s dal'inizio della voce) in cui scatta lo stato k (len n);
    tv: istante in cui parte la voce nel pezzo. jingles: [(wav,t,gain_db,durata|None)]"""
    D=snap(tv+vdur+tail+extra_end)
    times=[0]+[tv+e for e in ev]+[D]
    states=[]
    for k in range(-1,n):
        a=times[k+1];b=times[k+2]
        if b-a<1/FPS:continue
        states.append((png(layout(k),f'{name}_{k}'),b-a))
    # arrotondamento a frame
    tot=fr(D);acc=0;st2=[]
    for i,(p,d) in enumerate(states):
        nn=fr(d) if i<len(states)-1 else tot-acc
        if nn<=0:continue
        st2.append((p,nn/FPS));acc+=nn
    v,D=video_stati(name,st2,bg=True,fade=fade)
    parts=[(vpath,tv,0,0,None,25)]
    for wav,t,g,dd in jingles:parts.append((wav,t,g,0,dd,0))
    a=audio_pezzo(name,D,parts)
    return v,a,D
def offsets(testi,prefisso=''):
    """posizioni (frazione 0..1) di inizio di ogni testo dentro la voce (prefisso+testi uniti), calcolate sul testo con numeri in lettere"""
    full=voci.per_voce(prefisso+' '.join(testi));tot=len(full);pos=len(voci.per_voce(prefisso));out=[]
    for t in testi:
        out.append(pos/tot);pos+=len(voci.per_voce(t))+1
    return out
# ---------- schede ----------
def sigla(name,mp4):
    out=CL+name+'.mp4'
    sh(['ffmpeg','-v','error','-y','-i',mp4,'-an','-vf','scale=1920:1080,fps=30,format=yuv420p','-t','15','-c:v','libx264','-preset','veryfast','-crf','19','-g','60','-r','30',out])
    D=float(sh(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',out]).stdout)
    a=CL+name+'.wav'
    sh(['ffmpeg','-v','error','-y','-i',mp4,'-vn','-ar','48000','-ac','2','-c:a','pcm_s16le','-t',f'{D:.4f}',a])
    return out,a,D
def titolo_arg(n,tit,parte_txt=None):
    im=blu.scheda_titolo(f'Argomento {n}',tit)
    p=png(im,f'T{n}')
    v,D=video_stati(f'T{n}',[(p,5.0)],bg=True)
    a=audio_pezzo(f'T{n}',D,[(SND+'trans.wav',0,-6,0,1.6,0),(SND+'titolo.wav',1.3,0,0,None,0)])
    return v,a,D
def quiz_card(n,tit):
    im=blu.layer();blu.intestazione(im);d=ImageDraw.Draw(im)
    d.text((960,330),f'QUIZ · ARGOMENTO {n}',font=fig(34,True),fill=GIALLO,anchor='mm')
    d.text((960,470),'5 domande',font=brico(130),fill=(255,255,255),anchor='mm')
    d.text((960,610),tit,font=fig(46),fill=(205,222,250),anchor='mm')
    d.text((960,720),'Per continuare serve almeno l\'80%',font=fig(40,True),fill=(255,255,255),anchor='mm')
    p=png(im,f'Q{n}')
    v,D=video_stati(f'Q{n}',[(p,5.0)],bg=True)
    a=audio_pezzo(f'Q{n}',D,[(SND+'trans.wav',0,-12,0,0.45,0),(SND+'quiz.wav',0.5,0,0,None,0)])
    return v,a,D
def pillola(n,tit):
    righe=piano_righe(n);vn=f'R{n}';vtxt=voci.VOCI[vn]
    vp,vd,prov=voce(vn,voci.per_voce(vtxt))
    off=offsets(righe,'Ripasso. ')
    tv=2.4
    lay=lambda k:blu.scheda_pillola(tit,righe,k)
    ev=[o*vd for o in off]
    ev[0]=max(0.9,ev[0])
    return pezzo_voce(f'R{n}',lay,len(righe),ev,tv,vp,vd,jingles=[(SND+'repaso.wav',0,-2,2.6)],tail=1.5)
def piano_righe(n):return voci.PIL[f'R{n}']
# ---------- approfondimenti ----------
APPROF={
 1:('goethe',"Jakob Philipp Hackert: Goethe visita il Colosseo a Roma, 1790",[("Due signori","Due signori vestiti alla moda del Settecento"),("Sono figure piccole","Figure piccole e sperdute tra le maestose rovine"),("per contrasto","Per contrasto: la monumentalità dello spazio romano"),("Il soggetto è proprio","Il soggetto è il Grand Tour"),("La veduta è costruita","Una veduta sulla falsariga di Piranesi")]),
 2:('newton',"Étienne-Louis Boullée: Cenotafio di Newton, 1784",[("Doveva essere","Una tomba enorme, di forma sferica"),("Era la tomba di Newton","Newton: lo scienziato inglese, padre della gravità"),("l'esaltazione di figure","L'esaltazione della scienza e della razionalità"),("È l'architettura visionaria","Pure forme geometriche, come la sfera")]),
 3:('scala',"Giuseppe Piermarini: Teatro alla Scala, Milano",[("La pianta è rettangolare","Pianta rettangolare chiara, con due ingressi"),("La facciata è articolata","Facciata su tre livelli rigorosi"),("L'interno ha la forma","Interno a ferro di cavallo: cinque ordini di palchi e il loggione"),("viene inaugurato","Inaugurato con «L'Europa riconosciuta» di Antonio Salieri")]),
 4:('amore_psiche',"Antonio Canova: Amore e Psiche, 1787-1793",[("L'opera raffigura","Il momento poco prima del bacio"),("una grande X","Linee tese e curve che formano una grande X"),("le braccia delle due figure","Le braccia creano un cerchio geometrico perfetto"),("Il marmo viene lavorato","Marmo levigato e patina di cera")]),
 5:('napoleone',"Jacques-Louis David: Napoleone valica il Gran San Bernardo",[("È calmo","Calmo e idealizzato, su un cavallo bianco rampante"),("Nelle fonti storiche","Nelle fonti: a piedi o su un asino"),("Sulle rocce scure","Sulle rocce i nomi di Annibale e Carlo Magno"),("Così inserisce","Napoleone entra nella leggenda della storia universale")]),
}
def video_approf(name,states,art,box,D):
    """sfondo blu + livelli di testo + opera con zoom lento (zoompan)"""
    from PIL import Image as I
    bx,by,bw,bh=box
    a=I.open(ASSET+art+'.png');r=min(bw/a.width,bh/a.height);fw,fh=int(a.width*r)//2*2,int(a.height*r)//2*2
    ox=bx+(bw-fw)//2;oy=by+(bh-fh)//2
    big=ST+f'{name}_art.png';a.convert('RGB').resize((fw*2,fh*2),I.LANCZOS).save(big)
    lst,n=_lista(states,name);N=n
    out=CL+name+'.mp4'
    fl=(f"[1:v]fps=30,format=rgba[s];[0:v]fps=30,format=yuv420p[b];[b][s]overlay=0:0:format=auto[v0];"
        f"[2:v]zoompan=z='1+0.09*on/{N}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={fw}x{fh}:fps=30,format=yuv420p[z];"
        f"[v0][z]overlay={ox}:{oy}[v1];[v1]{fade_f(N/FPS)},format=yuv420p[v]")
    sh(['ffmpeg','-v','error','-y','-stream_loop','-1','-i',WK+'bg_blu.mp4','-f','concat','-safe','0','-i',lst,'-loop','1','-framerate','30','-i',big,'-filter_complex',fl,'-map','[v]','-t',f'{N/FPS:.4f}']+ENC+[out])
    return out,N/FPS
def approfondimento(n):
    art,tit,call=APPROF[n];vn=f'A{n}';vt=voci.per_voce(voci.VOCI[vn])
    vp,vd,prov=voce(vn,vt);low=vt.lower()
    tv=1.0;D=snap(tv+vd+1.0)
    evs=[]
    for anc,txt in call:
        i=low.find(voci.per_voce(anc).lower())
        evs.append((i/len(vt)*vd if i>=0 else 0,txt))
    evs.sort()
    def layer(k):
        im=blu.layer();blu.intestazione(im);d=ImageDraw.Draw(im)
        d.text((1010,170),'APPROFONDIMENTO',font=fig(30,True),fill=GIALLO,anchor='lm')
        for i,l in enumerate(wrap(d,tit,brico(46),830)):d.text((1010,225+i*56),l,font=brico(46),fill=(255,255,255))
        y=420;tt=[c[1] for c in call]
        vis=range(0,k+1)
        for j in vis:
            h=blu.altezza_riga(tt[j],830,38)
            blu.card_blu(im,1010,y,830,tt[j],'on' if j==k else 'off',38);y+=h+16
        return im
    times=[0]+[tv+e for e,_ in evs]+[D]
    states=[]
    for k in range(-1,len(evs)):
        a,b=times[k+1],times[k+2]
        if b-a>=1/FPS:states.append((png(layer(k),f'{vn}_{k}'),b-a))
    tot=fr(D);acc=0;st2=[]
    for i,(p,d_) in enumerate(states):
        nn=fr(d_) if i<len(states)-1 else tot-acc
        if nn>0:st2.append((p,nn/FPS));acc+=nn
    v,Dd=video_approf(vn,st2,art,(80,170,880,800),D)
    a=audio_pezzo(vn,Dd,[(SND+'trans.wav',0,-6,0,1.0,0),(vp,tv,0,0,None,25)])
    return v,a,Dd
# ---------- copertina e elenco argomenti ----------
ARGT=[a['titolo'] for a in piano.ARGOMENTI]
def cover(parte=1):
    args=ARGT if parte==1 else ARGT[3:]
    num0=1 if parte==1 else 4
    def layer(k):
        im=blu.layer();blu.intestazione(im);d=ImageDraw.Draw(im)
        d.text((960,200),"STORIA DELL'ARTE V"+("" if parte==1 else " · PARTE 2"),font=fig(34,True),fill=GIALLO,anchor='mm')
        d.text((960,340),"Il Neoclassicismo",font=brico(140),fill=(255,255,255),anchor='mm')
        d.rounded_rectangle((900,430,1020,437),3,fill=GIALLO)
        y=520
        for i,t in enumerate(args):
            if i>k:break
            on=(i==k) and parte==1
            blu.card_blu(im,360,y,1200,f'{num0+i}. {t}','on' if on else ('off' if parte==1 else 'neutra' if False else 'off'),40);y+=86
        return im
    if parte==1:
        vt=voci.per_voce(voci.VOCI['INTRO']);vp,vd,prov=voce('INTRO',vt);low=vt.lower()
        anc=["come nasce","l'architettura","piermarini","i teorici","la pittura"]
        ev=[max(0,low.find(a)/len(vt)*vd) for a in anc]
        tv=1.2
        return pezzo_voce('COVER',layer,len(args),ev,tv,vp,vd,jingles=[(SND+'titolo.wav',0,-3,None)],tail=1.5)
    im=layer(len(args)-1);p=png(im,'COVER2');v,D=video_stati('COVER2',[(p,5.0)],bg=True)
    a=audio_pezzo('COVER2',D,[(SND+'trans.wav',0,-6,0,1.6,0),(SND+'titolo.wav',1.3,0,0,None,0)]);return v,a,D
def elenco_argomenti():
    vt=voci.per_voce(voci.VOCI['ARG']);vp,vd,prov=voce('ARG',vt);low=vt.lower()
    def layer(k):
        im=blu.layer();blu.intestazione(im);d=ImageDraw.Draw(im)
        d.text((960,170),'GLI ARGOMENTI DELLA LEZIONE',font=fig(34,True),fill=GIALLO,anchor='mm')
        y=260
        for i,t in enumerate(ARGT):
            if i>k:break
            h=blu.altezza_riga(f'{i+1}. {t}',1400,46)
            blu.card_blu(im,260,y,1400,f'{i+1}. {t}','on' if i==k else 'off',46);y+=h+24
        return im
    anc=["primo:","secondo:","terzo:","quarto:","quinto:"]
    ev=[max(0,low.find(a)/len(vt)*vd) for a in anc]
    return pezzo_voce('ARG',layer,5,ev,1.0,vp,vd,jingles=[(SND+'trans.wav',0,-6,1.6)],tail=1.2)
# ---------- glossario, ripasso finale, spiegone, mappa, verifica, compiti ----------
def glossario():
    ent=voci.GLOSS;vt=voci.per_voce(voci.VOCI['GL']);vp,vd,prov=voce('GL',vt)
    testi=[f"{t}: {d}" for t,d in ent];off=offsets(testi,'Glossario. Le parole da ricordare. ')
    def layer(k):
        im=blu.layer();blu.intestazione(im);d=ImageDraw.Draw(im)
        d.text((960,150),'GLOSSARIO',font=fig(34,True),fill=GIALLO,anchor='mm')
        d.text((960,215),'Le parole da ricordare',font=brico(54),fill=(255,255,255),anchor='mm')
        a=max(0,k-3);y=300
        for j in range(a,k+1):
            h=blu.altezza2(ent[j][0],ent[j][1],1560,40);blu.card_blu2(im,180,y,1560,ent[j][0],ent[j][1],'on' if j==k else 'off',40);y+=h+18
        return im
    ev=[max(0.9,o*vd) if i==0 else o*vd for i,o in enumerate(off)]
    return pezzo_voce('GL',layer,len(ent),ev,1.4,vp,vd,jingles=[(SND+'trans.wav',0,-6,1.6),(SND+'repaso.wav',0.2,-6,1.2)],tail=1.5)
def ripasso_finale():
    R=voci.RFS;vt=voci.per_voce(voci.VOCI['RF']);vp,vd,prov=voce('RF',vt);low=vt.lower()
    def layer(k):
        im=blu.layer();blu.intestazione(im);d=ImageDraw.Draw(im)
        d.text((960,150),'RIPASSO FINALE',font=fig(34,True),fill=GIALLO,anchor='mm')
        for i in range(5):
            x=700+i*130;d.ellipse((x,205,x+26,231),fill=GIALLO if i==k else (255,255,255,90))
        t,x=R[k];d.text((960,310),f'{k+1}. {t}',font=brico(56),fill=(255,255,255),anchor='mm')
        blu.card_blu(im,180,400,1560,x,'on',46)
        return im
    anc=["primo argomento","secondo argomento","terzo argomento","quarto argomento","quinto argomento"]
    ev=[max(0.9,low.find(a)/len(vt)*vd) if i==0 else low.find(a)/len(vt)*vd for i,a in enumerate(anc)]
    return pezzo_voce('RF',layer,5,ev,1.4,vp,vd,jingles=[(SND+'trans.wav',0,-6,1.6),(SND+'repaso.wav',0.2,-6,1.2)],tail=1.5)
SPIMG={0:['goethe','salotto'],1:['newton','pantheon'],2:['scala','palazzo_reale']}
def spiegone():
    vt=voci.per_voce(voci.VOCI['SP']);vp,vd,prov=voce('SP',vt)
    items=[]   # (indice argomento, testo)
    for i,(t,x) in enumerate(voci.SPS[:3]):
        fr_=[s.strip()+'.' for s in re.split(r'(?<=[.!?])\s+',x) if s.strip()]
        for s_ in fr_:items.append((i,s_))
    pre="Prima di continuare, ripassiamo quello che abbiamo visto nella Parte precedente. "
    full=[pre]
    # offsets: ricostruisce il testo della voce
    txt=voci.per_voce(voci.VOCI['SP']);pos=[];cur=len(voci.per_voce(pre))
    labs=['Primo argomento:','Secondo argomento:','Terzo argomento:']
    cur_i=-1;acc=len(voci.per_voce(pre))
    for i,(t,x) in enumerate(voci.SPS[:3]):
        acc+=len(voci.per_voce(f"{labs[i]} {t}. "))
        for s_ in [s.strip() for s in re.split(r'(?<=[.!?])\s+',x) if s.strip()]:
            pos.append(acc/len(txt));acc+=len(voci.per_voce(s_))+1
    def layer(k):
        i,s_=items[k];im=blu.layer();blu.intestazione(im);d=ImageDraw.Draw(im)
        d.text((80,160),'RIPASSO DELLA PARTE PRECEDENTE',font=fig(30,True),fill=GIALLO,anchor='lm')
        t=voci.SPS[i][0]
        for j,l in enumerate(wrap(d,f'{i+1}. {t}',brico(50),920)):d.text((80,215+j*58),l,font=brico(50),fill=(255,255,255))
        # frasi dell'argomento fino a k
        same=[(kk,it[1]) for kk,it in enumerate(items) if it[0]==i and kk<=k][-3:]
        y=400
        for kk,ss in same:
            h=blu.altezza_riga(ss,920,38);blu.card_blu(im,80,y,920,ss,'on' if kk==k else 'off',38);y+=h+16
        # immagini a destra
        ims=SPIMG[i];ys=170;hh=(870-20*(len(ims)-1))//len(ims)
        for j,nm in enumerate(ims):
            a=Image.open(ASSET+nm+'.png').convert('RGBA');a=fit(a,(780,hh))
            x=1060+(780-a.width)//2;y0=ys+j*(hh+20);shadow(im,(x,y0,x+a.width,y0+a.height),r=6,blur=14,off=(0,8),alpha=90);im.alpha_composite(a,(x,y0))
        return im
    ev=[max(0.9,p*vd) if k==0 else p*vd for k,p in enumerate(pos)]
    return pezzo_voce('SP',layer,len(items),ev,1.2,vp,vd,jingles=[(SND+'trans.wav',0,-6,1.6)],tail=1.5)
import mappa_bes as MB
def mappa_finale():
    vt=voci.per_voce(voci.VOCI['MF']);vp,vd,prov=voce('MF',vt);low=vt.lower()
    anc=["il neoclassicismo, arte","è un movimento","nasce in contrasto","il periodo","rinasce l'interesse","grazie alla scoperta","e a winckelmann","l'architettura","rispetto al barocco","gli architetti","la scultura","soggetti idealizzati","con antonio canova","la pittura","temi storici","con jacques"]
    ev=[]
    for a in anc:
        i=low.find(a);ev.append(max(0,i/len(vt)*vd))
    ev[0]=max(ev[0],0.8)
    D=snap(1.0+vd+4.0)
    tv=1.0
    times=[0]+[tv+e for e in ev]+[tv+vd,D]
    states=[]
    # stato 0: mappa vuota (solo titolo e legenda); k nodi
    for k in range(0,len(MB.N)+1):
        a,b=(times[0],times[1]) if k==0 else (times[k],times[k+1] if k<len(MB.N) else times[k+1])
        if k==len(MB.N):
            # ultimo nodo acceso fino a fine voce, poi mappa intera ferma 4 s
            states.append((png(MB.stato(k).convert('RGB').convert('RGBA'),f'MF_{k}'),times[k+1]-times[k]));states.append((png(MB.stato(k,True).convert('RGB').convert('RGBA'),'MF_tutti'),D-times[k+1]));continue
        if b-a>=1/FPS:states.append((png(MB.stato(k).convert('RGB').convert('RGBA'),f'MF_{k}'),b-a))
    tot=fr(D);acc=0;st2=[]
    for i,(p,d_) in enumerate(states):
        nn=fr(d_) if i<len(states)-1 else tot-acc
        if nn>0:st2.append((p,nn/FPS));acc+=nn
    v,Dd=video_stati('MF',st2,fade=(0.35,0.35))
    a=audio_pezzo('MF',Dd,[(SND+'trans.wav',0,-6,0,1.0,0),(vp,tv,0,0,None,25),(SND+'repaso.wav',tv+vd+0.2,-6,0,3.3,0)])
    return v,a,Dd
def verifica_card():
    im=blu.layer();blu.intestazione(im);d=ImageDraw.Draw(im)
    d.text((960,330),'VERIFICA FINALE',font=fig(34,True),fill=GIALLO,anchor='mm')
    d.text((960,470),'10 domande',font=brico(130),fill=(255,255,255),anchor='mm')
    d.text((960,610),'Il Neoclassicismo',font=fig(46),fill=(205,222,250),anchor='mm')
    d.text((960,720),"Per proseguire serve almeno l'80%",font=fig(40,True),fill=(255,255,255),anchor='mm')
    p=png(im,'VER');v,D=video_stati('VER',[(p,5.0)],bg=True)
    a=audio_pezzo('VER',D,[(SND+'trans.wav',0,-12,0,0.45,0),(SND+'quiz.wav',0.5,0,0,None,0)]);return v,a,D
def compiti_intro():
    im=blu.layer();blu.intestazione(im);d=ImageDraw.Draw(im)
    d.text((960,430),'COMPITI',font=brico(170),fill=(255,255,255),anchor='mm')
    d.rounded_rectangle((880,540,1040,548),3,fill=GIALLO)
    d.text((960,640),'Il Neoclassicismo',font=fig(44),fill=(205,222,250),anchor='mm')
    p=png(im,'CI');v,D=video_stati('CI',[(p,3.5)],bg=True)
    a=audio_pezzo('CI',D,[(SND+'trans.wav',0,-6,0,1.0,0),(SND+'titolo.wav',0.6,0,0,None,0)]);return v,a,D
def compiti():
    C=voci.COMPITI;vt=voci.per_voce(voci.VOCI['COMPITI']);vp,vd,prov=voce('COMPITI',vt);low=vt.lower()
    def layer(k):
        im=blu.layer();blu.intestazione(im);d=ImageDraw.Draw(im)
        d.text((960,150),'COMPITI',font=fig(34,True),fill=GIALLO,anchor='mm')
        if k<4:
            d.text((960,225),f'Compito {k+1} di 4',font=brico(60),fill=(255,255,255),anchor='mm')
            blu.card_blu(im,180,310,1560,C[k],'on',40)
        else:
            d.text((960,225),'Ora tocca a te',font=brico(70),fill=(255,255,255),anchor='mm')
            blu.card_blu(im,180,330,1560,voci.CHIUSURA,'on',48)
        return im
    anc=["primo compito","secondo compito","terzo compito","quarto compito","svolgi i compiti"]
    ev=[max(0.9,low.find(a)/len(vt)*vd) if i==0 else low.find(a)/len(vt)*vd for i,a in enumerate(anc)]
    return pezzo_voce('COMP',layer,5,ev,1.2,vp,vd,jingles=[],tail=1.5,fade=(0.35,0.5))
