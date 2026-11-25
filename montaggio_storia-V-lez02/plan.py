import sys,os,json,glob
sys.path.insert(0,'/tmp/w/b')
from kinds2 import *
import kinds2
QZ=json.load(open('/tmp/w/old/consegna-storia-V-lez02/quiz_argomenti.json'))
B=json.load(open('/tmp/w/B.json'))
TITLE="Il mondo agli inizi del XX secolo e l'imperialismo"
TIT={1:"La competizione imperialista",2:"Il Regno Unito e l'Impero britannico",3:"La Francia tra nazionalismo e antisemitismo",4:"La Germania di Guglielmo II",5:"L'Austria-Ungheria e i Balcani",
     6:"L'Impero russo: autocrazia e rivoluzione",7:"L'Estremo Oriente: Giappone e Cina",8:"Gli Stati Uniti come nuova potenza",9:"L'America Latina e la rivoluzione messicana"}
KW={1:['Imperialismo','Conferenza di Berlino','Sfere di influenza','Revanscismo','Superiorità razziale'],2:['Età vittoriana','Parliament Act','Home Rule','Dominions','Guerra anglo-boera'],
    3:['Caso Dreyfus','Dreyfusardi','Fashoda','Entente cordiale','Santa Sede'],4:['Weltpolitik','Guglielmo II','Piano Tirpitz','Riarmo navale','Herero'],
    5:['Compromesso del 1867','Bosnia Erzegovina','Panslavismo','Trialismo','Francesco Ferdinando'],6:['Autocrazia','Transiberiana','Bolscevichi','Domenica di sangue','Soviet e Duma'],
    7:['Era Meiji','Guerre dell\'oppio','Rivolta dei Boxer','Sun Yat-sen','Yuan Shikai'],8:['Sherman Act','Theodore Roosevelt','Big Stick','Guerra contro la Spagna','Pacifico'],
    9:['Porfirio Díaz','Latifondisti','Madero','Zapata e Villa','Costituzione del 1917']}
AN={n:[f'AN{2*n-1}',f'AN{2*n}'] for n in range(1,10)}
MAP={3:('MAPD1','MAPD1'),6:('MAPD2','MAPD2'),9:('MAPD3','MAPD3')}
PARTS={1:dict(args=[1,2,3],gl='GL1',rf='RF1',fin='FIN1'),2:dict(args=[4,5,6,7,8,9],gl='GL2',rf='RF2',fin='FIN2')}
ARGLIST=[TIT[i] for i in range(1,4)]
def have(v): return os.path.exists(VOX+v+'.wav')
def copertina_img(prof,reveal,items):
    im=Image.new('RGB',(W,H),WHITE);d=ImageDraw.Draw(im)
    im.paste(LOGO_B,(56,34),LOGO_B)
    d.text((64,170),'STORIA · VIDEOLEZIONE',font=font(FIGB,28),fill=BLUE)
    f=font(BRI,92);y=225
    for l in wrap(d,TITLE,f,1300): d.text((60,y),l,font=f,fill=NAVY);y+=112
    d.rectangle((64,y+10,224,y+20),fill=BLUE)
    y+=60
    shadow_rect(im,(60,y,1330,y+80+len(items)*66),r=22,blur=10,off=(0,6),alpha=40)
    d.rounded_rectangle((60,y,1330,y+80+len(items)*66),22,fill=(247,249,253),outline=(222,228,238),width=2)
    d.text((96,y+22),'ARGOMENTI',font=font(FIGB,26),fill=BLUE)
    yy=y+70
    for i,it in enumerate(items[:reveal]):
        d.ellipse((100,yy+14,118,yy+32),fill=YEL,outline=BLUE,width=3)
        d.text((140,yy),it,font=font(FIGM,40),fill=NAVY);yy+=66
    d.text((56,1030),MAT,font=font(FIGB,20),fill=BLUE)
    if prof:
        x,y0=1428,148
        shadow_rect(im,(x,y0,x+412,y0+309+78),r=6,blur=12)
        d.rectangle((x,y0,x+412,y0+309),fill=(235,238,244));d.rectangle((x,y0+309,x+412,y0+309+78),fill=YEL)
        d.text((x+20,y0+309+12),'Giorgio Mazzotti',font=font(BRI,34),fill=NAVY);d.text((x+20,y0+309+52),'PROF. DI STORIA',font=font(FIGB,20),fill=NAVY)
    return im
def args_slide(page):
    cards=[ "In questa prima parte: "+"; ".join(t.lower() if i else t for i,t in enumerate(ARGLIST))+"." ]
    return None
def build(spec):
    k=spec[0]
    if k=='sigla': return p_media(spec[1],KIT+'sigle/Sigla_Storia_15s.mp4')
    if k=='sfin': return p_media(spec[1],KIT+'sigle/Sigla_finale_5s_con_avviso_diritti.mp4')
    if k=='copert':
        v='BENV1'
        units=["Benvenuti alla lezione «Il mondo agli inizi del ventesimo secolo e l'imperialismo».","In questa prima parte vedremo tre argomenti:","la competizione imperialista;","il Regno Unito e l'Impero britannico;","la Francia tra nazionalismo e antisemitismo.","Cominciamo."]
        al,vdur,r=align(v,units);lead=1.0;tot=lead+vdur+0.8
        fr=[(copertina_img(False,0,ARGLIST),lead+al[2][0])]
        for i in range(3):
            s=lead+al[2+i][0];e=lead+(al[3+i][0] if i<2 else vdur+0.8)
            fr.append((copertina_img(False,i+1,ARGLIST),e-s))
        pc=piece('COPERT',fr,tot,[(TRANS,0.0,-8,'fx'),(vpath(v),lead,vgain(vpath(v)),'voice')]);pc['cues']=[(lead+a,lead+b,u) for (a,b),u in zip(al,units)];return pc,r
    if k=='d0':
        a,b=0.0,B[0];fr=[]
        fr.append((copertina_img(True,3,ARGLIST),50.0))
        pk=[(t,x) for t,x in [(0,'')]]
        # second state: slide degli argomenti
        im=white_frame('Gli argomenti','In questa parte vedremo',1,True,None);d=ImageDraw.Draw(im);y=300
        for i,t in enumerate(ARGLIST):
            y=draw_card(im,60,y,f'{i+1}. {t}',False if i else True)+22
        fr.append((im,b-a-50.0))
        return p_teacher('D0',a,b,fr)
    if k=='title': return p_title(spec[1],spec[2],spec[3])
    if k=='quiz': return p_quiz(spec[1],spec[2],spec[3],spec[4] if len(spec)>4 else False)
    if k=='teach':
        n,pg=spec[1],spec[2]
        a,b=B[n-1],B[n];pk=slide_pick(a,b,n)
        fr,info,nxt=teacher_states(a,b,f'Argomento {n}',TIT[n],pk,KW[n],pg,n)
        r=p_teacher(f'D{n}',a,b,fr);r['info']=info;r['picks']=pk;r['next']=nxt;return r
    if k=='an':
        v=spec[1];us=split_sentences(TXT[v]);title=us[0].rstrip('.')
        return cards_piece(spec[2],'Approfondimento',title,us[1:],v,lead=1.0,tail=0.8,maxvis=4,fs=42,tsize=74,align_units=us)[0]
    if k=='map': return p_map(spec[1],spec[2],spec[3])[0]
    if k=='ripasso':
        v=spec[1];us=split_sentences(TXT[v])
        return cards_piece(spec[2],'Ripasso',spec[3],us[1:],v,jingle=JR,lead=2.0,tail=1.9,trans_end=True,maxvis=6,fs=42,align_units=us)[0]
    if k=='cards':
        v=spec[1];us=split_sentences(TXT[v])
        return cards_piece(spec[2],spec[3],spec[4],us[1:],v,lead=1.0,tail=0.8,maxvis=6,fs=42,gl=spec[5] if len(spec)>5 else False,align_units=us)[0]
    raise KeyError(k)

def comp_piece(name):
    v='COMPITI';us=split_sentences(TXT[v])
    al,vdur,r=align(v,us)
    pdf=[
     "Spiega che cos'è l'imperialismo e in che modo si differenzia dal vecchio colonialismo, indicando le principali motivazioni economiche e ideologiche che spinsero le potenze europee alla spartizione dell'Africa sancita dalla conferenza di Berlino.",
     "Analizza le principali tensioni politiche e sociali delle grandi potenze europee agli inizi del Novecento, soffermandoti sulla questione irlandese e sull'amministrazione dell'Impero britannico, sul caso Dreyfus in Francia e sulla politica aggressiva della Weltpolitik nella Germania di Guglielmo II.",
     "Ricostruisci la crisi dell'Impero russo all'inizio del XX secolo, illustrando le cause della guerra russo-giapponese e gli eventi della rivoluzione del 1905, fino alla nascita dei primi soviet e alla concessione della Duma.",
     "Descrivi l'ascesa degli Stati Uniti come nuova potenza mondiale durante la presidenza di Theodore Roosevelt, spiegando la politica estera del Big Stick, la guerra contro la Spagna e gli esiti dell'espansionismo statunitense nell'oceano Pacifico e in America Latina.",
     "Svolgi i compiti qui sotto e premi Consegna: arrivano al docente nel tuo quaderno dei compiti."]
    disp=[f'Compito {i+1}. '+t for i,t in enumerate(pdf[:4])]+[pdf[4]]
    starts=[al[0][0],al[2][0],al[4][0],al[6][0],al[8][0]]
    lead=1.0;tail=2.0;total=lead+vdur+tail
    fr=[(cards_state(0,'Compiti','I compiti di questa lezione',disp,-1,44,1780,False,1),lead+starts[0])]
    for i in range(5):
        s=lead+starts[i];e=lead+(starts[i+1] if i<4 else vdur+tail)
        fr.append((cards_state(s,'Compiti','I compiti di questa lezione',disp,i,44,1780,False,1,0.5),0.12))
        t=s+0.12
        while t<e-0.01:
            nx=min(e,t+1.0);fr.append((cards_state(t,'Compiti','I compiti di questa lezione',disp,i,44,1780,False,1),nx-t));t=nx
    pc=piece(name,fr,total,[(TRANS,0.0,-8,'fx'),(vpath(v),lead,vgain(vpath(v)),'voice')]);pc['cues']=[(lead+starts[i],lead+(starts[i+1] if i<4 else vdur),disp[i]) for i in range(5)];return pc
def cintro_piece(name):
    fr=[]
    for k in range(7):
        im=blue_frame(k*0.5,footer=False);d=ImageDraw.Draw(im)
        d.text((64,400),'Compiti',font=font(BRI,170),fill=WHITE);d.rectangle((68,600,300,614),fill=YEL)
        fr.append((im,0.5))
    return piece(name,fr,3.5,[(JT,0.3,0,'fx')])
def part_seq(p):
    P=PARTS[p];seq=[];pg=3 if p==1 else 1
    seq.append(('sigla',f'P{p}_SIGLA'))
    if p==1:
        seq.append(('copert',));seq.append(('d0',))
    else:
        seq.append(('cards','RIP2','P2_RIP2','Ripasso','Prima di continuare: la prima parte'))
    for n in P['args']:
        seq.append(('title',f'T{n}',n,TIT[n]))
        seq.append(('teach',n,None))
        for v in AN[n]: seq.append(('an',v,f'AN_{v}'))
        if n in MAP: seq.append(('map',f'MAP_{n}',MAP[n][0],MAP[n][1]))
        seq.append(('ripasso',f'R{n}',f'R_{n}',TIT[n]))
        seq.append(('quiz',f'Q{n}',n,TIT[n]))
    seq.append(('cards',P['gl'],f'P{p}_GL','Glossario','Le parole chiave',True))
    seq.append(('cards',P['rf'],f'P{p}_RF','Ripasso finale','Ripasso finale della parte'))
    seq.append(('cards',P['fin'],f'P{p}_FIN','Fine della parte','A presto'))
    seq.append(('quiz',f'P{p}_VER',0,'',True))
    seq.append(('sfin',f'P{p}_SFIN'))
    seq.append(('cintro',f'P{p}_CINTRO'))
    seq.append(('comp',f'P{p}_COMP'))
    return seq
def spec_name(sp):
    k=sp[0]
    return {'copert':'COPERT','d0':'D0'}.get(k) or (f'D{sp[1]}' if k=='teach' else (sp[1] if k in('sigla','sfin','cintro','comp') else sp[2] if k in('an','ripasso','cards') else sp[1] if k=='map' else sp[1]))
def spec_voices(sp):
    k=sp[0]
    if k=='copert': return ['BENV1']
    if k in('an','ripasso','cards'): return [sp[1]]
    if k=='map': return [sp[3]]
    if k=='comp': return ['COMPITI']
    return []
def build_any(sp):
    k=sp[0]
    if k=='cintro': return cintro_piece(sp[1])
    if k=='comp': return comp_piece(sp[1])
    r=build(sp)
    return r[0] if isinstance(r,tuple) else r
