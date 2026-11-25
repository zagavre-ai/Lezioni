import sys,os,json,glob
sys.path.insert(0,'/tmp/w/b')
from kinds2 import *
import kinds2
QZ=json.load(open('/tmp/w/old/quiz_argomenti.json'))
B=[121.3,1132.24,1635.79,2184.37,2365.14,2795.25,3276.62,3636.43,4071.02,4524.5,4650.61,5070.4]
TIT={1:"Belle Époque: luci e ombre",2:"Trasporti e comunicazioni",3:"Medicina e società di massa",4:"Urbanizzazione e grandi città",5:"La società dei consumi",
     6:"Tempo libero, taylorismo e fordismo",7:"Trust, crisi agraria e migrazioni",8:"Politica di massa e socialismo",9:"La Chiesa e i movimenti femministi",10:"La crisi del Positivismo",11:"Razzismo, antisemitismo e nazionalismo"}
KW={1:['Belle Époque','Borghesia','Esposizioni Universali','Tour Eiffel','Disuguaglianze'],2:['Elettricità','Motore a scoppio','Aeroplano','Radio','Cinema'],
    3:['Louis Pasteur','Robert Koch','Vaccini','Mortalità infantile','Società di massa'],4:['Urbanizzazione','Londra','Parigi','Metropolitana','Acquedotti'],
    5:['Società dei consumi','Beni secondari','Grandi magazzini','Pubblicità','Mass media'],6:['Tempo libero','Taylorismo','Catena di montaggio','Henry Ford','Omologazione'],
    7:['Trust','Monopolio','Crisi agraria','Ellis Island','Emigrazione'],8:['Suffragio universale','Partiti di massa','Sindacati','Riformisti','Rivoluzionari'],
    9:['Rerum Novarum','Leone XIII','Modernismo cattolico','Suffragiste','Emmeline Pankhurst'],10:['Positivismo','Max Planck','Albert Einstein','Friedrich Nietzsche','Sigmund Freud'],
    11:['Darwinismo sociale','Razzismo','Antisemitismo','Sionismo','Nazionalismo']}
AN={1:['AN10'],2:['AN1'],3:['AN11'],4:['AN2'],5:['AN12'],6:['AN3'],7:['AN6'],8:['AN4_R2'],9:['AN5'],10:['AN7'],11:['AN9','AN8']}
MAP={3:('MAPPA1','MAPPA1'),7:('MAPPA2','MAPPA2'),9:('MAPPA3','MAPPA3')}
PARTS={1:dict(args=[1,2,3,4,5],gl='GL1',rf='RF1',fin='FIN1'),2:dict(args=[6,7,8,9,10,11],gl='GL2',rf='RF2',fin='FIN2')}
ARGLIST=[TIT[i] for i in range(1,6)]
def have(v): return os.path.exists(VOX+v+'.wav')
def copertina_img(prof,reveal,items):
    im=Image.new('RGB',(W,H),WHITE);d=ImageDraw.Draw(im)
    im.paste(LOGO_B,(56,34),LOGO_B)
    d.text((64,170),'STORIA · VIDEOLEZIONE',font=font(FIGB,28),fill=BLUE)
    f=font(BRI,100);y=225
    for l in wrap(d,'Il Novecento, il secolo delle masse',f,1300): d.text((60,y),l,font=f,fill=NAVY);y+=112
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
        units=["Benvenuti alla lezione «Il Novecento, il secolo delle masse».","In questa prima parte vedremo cinque argomenti:","la Belle Époque, tra luci e ombre;","i trasporti e le comunicazioni;","la medicina e la società di massa;","l'urbanizzazione e le grandi città;","la società dei consumi.","Cominciamo."]
        al,vdur,r=align(v,units);lead=1.0;tot=lead+vdur+0.8
        fr=[(copertina_img(False,0,ARGLIST),lead+al[2][0])]
        for i in range(5):
            s=lead+al[2+i][0];e=lead+(al[3+i][0] if i<4 else vdur+0.8)
            fr.append((copertina_img(False,i+1,ARGLIST),e-s))
        pc=piece('COPERT',fr,tot,[(TRANS,0.0,-8,'fx'),(vpath(v),lead,vgain(vpath(v)),'voice')]);pc['cues']=[(lead+a,lead+b,u) for (a,b),u in zip(al,units)];return pc,r
    if k=='d0':
        a,b=0.0,B[0];fr=[]
        fr.append((copertina_img(True,5,ARGLIST),50.0))
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
        a,b=B[n-1],B[n];pk=pick(a,b)
        fr,info,nxt=teacher_states(a,b,f'Argomento {n}',TIT[n],pk,KW[n],pg)
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
     "Analizza le luci e le ombre della Belle Époque, spiegando da un lato i fattori che alimentarono l'ottimismo della borghesia e dall'altro le profonde contraddizioni sociali e ideologiche che caratterizzarono questo periodo.",
     "Descrivi le caratteristiche principali del Taylorismo e del Fordismo, illustrando sia i vantaggi economici legati alla produzione di massa sia le conseguenze sociali negative per gli operai e per i consumatori.",
     "Spiega come si trasforma la partecipazione politica all'inizio del Novecento attraverso la nascita dei partiti di massa e dei sindacati, confrontando la posizione delle diverse correnti del Socialismo con l'intervento della Chiesa cattolica (enciclica Rerum Novarum) e con le lotte dei movimenti suffragisti.",
     "Analizza la crisi delle certezze positivistiche tra la fine dell'Ottocento e l'inizio del Novecento (citando i contributi della fisica e della psicoanalisi) e spiega in che modo le teorie del Darwinismo sociale e dell'antisemitismo alimentarono il razzismo e il nazionalismo aggressivo in Europa.",
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
        seq.append(('ripasso',f'R{n}' if n!=8 else 'R8_R2',f'R_{n}',TIT[n]))
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
