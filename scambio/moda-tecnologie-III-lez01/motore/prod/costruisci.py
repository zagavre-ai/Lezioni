# Costruisce le scene di lez01 dalle voci (vere o finte) e dai contenuti. Cache per scena (.ok).
import sys,os,json,re,subprocess,hashlib
sys.path.insert(0,'/home/user/lav/tools');sys.path.insert(0,'/home/user/lav/prod');sys.path.insert(0,'/home/user/lav/lez01/cont')
from scene import video,audio,dur
from sync import sync as sync_voce
from build_voci import carica,ordina_opz,vopz,nodi_mappa,LET
import build_voci2 as B2
P='/home/user/lav/prod/';L='/home/user/lav/lez01/'
VOX=os.environ.get('VOX',L+'vox/')           # cartella delle voci .wav (NOME.wav)
IMG=os.environ.get('IMG',L+'img/')
SC=L+'scene/'
FOOT='Tecnologie dei materiali e dei processi produttivi e organizzativi della moda · Tecnico Sistema Moda · III anno'
MAT='Tecnologie dei materiali e dei processi produttivi e organizzativi della moda'
RINOMINA={'A09_APPROF':'A09_APPROF_V2','A09_MAPPA':'A09_MAPPA_V2'}
def vox(n):return f'{VOX}{RINOMINA.get(n,n)}.wav'
def sy(nome,testi):
    """sincronia con cache"""
    f=f'{SC}sync_{nome}.json';w=vox(nome);key=hashlib.md5((open(w,'rb').read()[:200000]+json.dumps(testi).encode())).hexdigest()
    if os.path.exists(f):
        j=json.load(open(f))
        if j['key']==key:return j['st'],j['d']
    st,d=sync_voce(w,testi);os.makedirs(SC,exist_ok=True);json.dump(dict(key=key,st=st,d=d),open(f,'w'));return st,d
def fatto(nome):
    return os.path.exists(f'{SC}{nome}.ok')
def chiudi(nome,v,a,trans=True):
    open(f'{SC}{nome}.ok','w').write('1');return dict(v=v,a=a,trans=trans,nome=nome)
def clip(nome):
    return dict(v=f'{SC}{nome}.mp4',a=f'{SC}{nome}.wav',trans=json.load(open(f'{SC}{nome}.meta'))['trans'],nome=nome)
def salva(nome,v,a,trans=True):
    json.dump(dict(trans=trans),open(f'{SC}{nome}.meta','w'));open(f'{SC}{nome}.ok','w').write('1')
# ---------------- scene -----------------
def titolo(nome,kick,t,f,D=5.4,jing=[('titolo.wav',1.9)],trans=True):
    if fatto(nome):return clip(nome)
    v=video(P+'titolo.html',dict(k=kick,t=t,f=f),[],D,SC,nome);a=audio([],D,f'{SC}{nome}.wav',jing);salva(nome,v,a,trans);return clip(nome)
def approf(n):
    nome=f'A{n:02d}_approf'
    if fatto(nome):return clip(nome)
    from approf import AP
    A=carica(n);voice=A['approf']['voce'];fr=[s.strip() for s in re.split(r'(?<=[.?!])\s+',voice) if s.strip()]
    st,d=sy(f'A{n:02d}_APPROF',fr);lead=0.8
    box=AP[n]['box'];idx=sorted(box);steps=[[st[i][0]+lead,st[i][1]] for i in idx]
    img=None
    if AP[n]['img'] and os.path.exists(f"{IMG}{AP[n]['img']}.png"):img=f"{IMG}{AP[n]['img']}.png"
    D=lead+d+1.6
    v=video(P+'approf.html',dict(titolo=A['approf']['titolo'],img=img,box=[box[i] for i in idx],foot=FOOT),steps,D,SC,nome)
    a=audio([(vox(f'A{n:02d}_APPROF'),lead)],D,f'{SC}{nome}.wav');salva(nome,v,a);return clip(nome)
def mappa(n):
    nome=f'A{n:02d}_mappa'
    if fatto(nome):return clip(nome)
    A=carica(n);m=A['mappa'];testi=nodi_mappa(m);st,d=sy(f'A{n:02d}_MAPPA',testi);lead=0.8
    steps=[[a+lead,b] for a,b in st];D=steps[-1][0]+steps[-1][1]+4.0
    data=dict(kicker='MAPPA · '+A['titolo'].upper(),titolo=m['titolo'],centro=m['centro'],rami=[dict(t=r['t'],c=r['c'],f=[dict(t=f['t'],c=f['c']) for f in r['f']]) for r in m['rami']],foot=FOOT)
    v=video(P+'mappa.html',data,steps,D,SC,nome);a=audio([(vox(f'A{n:02d}_MAPPA'),lead)],D,f'{SC}{nome}.wav');salva(nome,v,a);return clip(nome)
def pillola_gen(nome,voce,kick,titolo_,righe_html,righe_voce,prefisso='Ripasso.',lead=3.9,tail=2.6):
    if fatto(nome):return clip(nome)
    st,d=sy(voce,[prefisso]+righe_voce);st=st[1:]
    steps=[[a+lead,b] for a,b in st];D=lead+d+tail
    v=video(P+'pillola.html',dict(kicker=kick,titolo=titolo_,righe=righe_html,foot=FOOT),steps,D,SC,nome)
    a=audio([(vox(voce),lead)],D,f'{SC}{nome}.wav',[('repaso.wav',1.9)]);salva(nome,v,a);return clip(nome)
def pillola(n):
    A=carica(n);return pillola_gen(f'A{n:02d}_ripasso',f'A{n:02d}_RIPASSO','RIPASSO',A['titolo'],[h for h,_ in A['ripasso']],[v for _,v in A['ripasso']])
def quiz_intro(n,tot=5):
    nome=f'A{n:02d}_quizintro' if n else 'TEST_intro'
    return titolo(nome,'METTITI ALLA PROVA','Quiz',f'{tot} domande · per continuare serve almeno l\'80%',D=4.6,jing=[('quiz.wav',0.5)],trans=False)
def quizq(nome,tag,d,opz,ok,spieg,voce_d,voce_r,testi_d,pensa=5.0):
    if fatto(nome):return clip(nome)
    st,dd=sy(voce_d,testi_d);lead=0.7
    q=st[0][0]+lead;o=[x[0]+lead for x in st[1:]]
    tend=lead+dd+0.4;th=[tend,tend+pensa];tr=th[1]+0.2;dr=dur(vox(voce_r));D=tr+dr+1.8
    v=video(P+'quizq.html',dict(tag=tag,domanda=d,opz=opz,ok=ok,spieg=spieg,foot=FOOT),dict(q=q,o=o,r=tr,think=th),D,SC,nome)
    a=audio([(vox(voce_d),lead),(vox(voce_r),tr)],D,f'{SC}{nome}.wav');salva(nome,v,a);return clip(nome)
def quiz(n):
    A=carica(n);out=[quiz_intro(n)]
    for qi,q in enumerate(A['quiz'],1):
        o,pos=ordina_opz(n,qi,q)
        dv=f"Domanda {['uno','due','tre','quattro','cinque'][qi-1]}. {q['dv']}"
        testi=[dv]+[f"Risposta {LET[i]}: {vopz(x)}." for i,x in enumerate(o)]
        out.append(quizq(f'A{n:02d}_q{qi}',f'QUIZ · DOMANDA {qi} DI 5',q['d'],o,pos,q['s'],f'A{n:02d}_Q{qi}_D',f'A{n:02d}_Q{qi}_R',testi))
    return out

# ---------------- scene di apertura/chiusura -----------------
def copertina(part,voce,voci_lista,img='IMG_COPERTINA_lana_seta'):
    nome=f'P{part}_copertina'
    if fatto(nome):return clip(nome)
    testo=json.load(open(L+'testi_voci_completo.json'));T={v['nome']:v['testo'] for v in testo}[voce]
    # l'ultima parte del testo elenca gli argomenti separati da ';'
    pre=T.split('vedremo:')[0]+'vedremo:';resto=T.split('vedremo:')[1]
    items=[x.strip().rstrip('.') for x in re.split(r';',resto.split('. Alla fine')[0])]
    st,d=sy(voce,[pre]+items);st=st[1:];lead=0.8
    steps=[[a+lead,b] for a,b in st];D=lead+d+2.0
    img_p=f'{IMG}{img}.png' if os.path.exists(f'{IMG}{img}.png') else None
    v=video(P+'copertina.html',dict(kicker=MAT.upper(),titolo='Preparazione',sub='Tecnico Sistema Moda · III anno',voci=[i[0].upper()+i[1:] for i in voci_lista],img=img_p,foot=FOOT),steps,D,SC,nome)
    a=audio([(vox(voce),lead)],D,f'{SC}{nome}.wav');salva(nome,v,a);return clip(nome)
def glossario(voce='P2_GLOSSARIO'):
    nome='P3_glossario'
    if fatto(nome):return clip(nome)
    testi=['Glossario.']+[B2.gl_voce(a,b) for a,b in B2.GLOS];st,d=sy(voce,testi);st=st[1:];lead=0.8
    steps=[[a+lead,b] for a,b in st];D=lead+d+2.0
    v=video(P+'glossario.html',dict(kicker='GLOSSARIO',titolo='Le parole della lezione',termini=[[a,b] for a,b in B2.GLOS],foot=FOOT,per=10),steps,D,SC,nome)
    a=audio([(vox(voce),lead)],D,f'{SC}{nome}.wav');salva(nome,v,a);return clip(nome)
def mappa_finale(voce='P2_MAPPA_FINALE'):
    nome='P3_mappafinale'
    if fatto(nome):return clip(nome)
    testi=['La mappa della lezione.']+[v for _,v in B2.MAPF];st,d=sy(voce,testi);lead=0.8
    steps=[[a+lead,b] for a,b in st];D=steps[-1][0]+steps[-1][1]+4.0
    data=dict(kicker='MAPPA DELLA LEZIONE · PREPARAZIONE',titolo='Che cosa abbiamo imparato sulle fibre di origine animale?',centro='Fibre naturali di origine animale',rami=[dict(t=t,c='pag',f=[]) for t,_ in B2.MAPF],foot=FOOT)
    v=video(P+'mappa.html',data,steps,D,SC,nome);a=audio([(vox(voce),lead)],D,f'{SC}{nome}.wav');salva(nome,v,a);return clip(nome)
def ripasso_finale(voce='P2_RIPASSO_FINALE'):
    righe=[f"<b>{t.split(':')[0] if False else ''}</b>{h}" for h,t in zip(RIGHE_FIN(),B2.RIPF)]
    return pillola_gen('P3_ripassofinale',voce,'RIPASSO FINALE','Argomento per argomento',RIGHE_FIN(),B2.RIPF,prefisso='Ripasso finale, argomento per argomento.',lead=3.9)
def RIGHE_FIN():
    return ["Una <b>fibra tessile</b> è lunga, flessibile e sottile. Le fibre sono <b>naturali</b> (vegetali o animali) o <b>chimiche</b> (artificiali o sintetiche).",
     "Le proprietà sono <b>morfologiche</b>, <b>chimiche</b>, <b>fisico-meccaniche</b> e <b>fisiologiche</b>.",
     "Le fibre naturali sono il <b>37%</b> della produzione; le chimiche il <b>63%</b> del consumo.",
     "La lana è fatta di <b>cheratina</b> (80%); le lane migliori vengono da <b>spalle e fianchi</b>.",
     "Il valore della lana: <b>razza</b>, <b>finezza in micron</b>, <b>filabilità</b>, morbidezza, lunghezza, colore.",
     "Trattamenti della lana: <b>chimici</b> e <b>meccanici</b> (ZIRPRO, follatura, superwash).",
     "La lana è <b>ingualcibile</b>, <b>ignifuga</b>, idrorepellente e <b>igroscopica</b> (fino al 30% del peso).",
     "Lane speciali: la <b>vigogna</b> è la più fine e costosa; a pelo fine corrisponde il prezzo più elevato.",
     "La seta è l'unica fibra naturale <b>continua</b>: <b>trattura</b> e <b>sgommatura</b> danno seta cruda, mezza cotta e cotta.",
     "La seta è <b>resistente</b> e <b>termoisolante</b> ma delicata: lavaggio tiepido, stiro a rovescio, senza vapore diretto."]
def test_finale():
    T=json.load(open(L+'test.json'));out=[quiz_intro(0,tot=20)]
    for i,q in enumerate(T,1):
        testi=[f"Domanda {B2.conv(str(i))}. {B2.vq(q['d'])}"]
        # le opzioni restano a schermo: la voce legge solo la domanda -> sincronia: domanda sola
        nome=f'T{i:02d}'
        if fatto(nome):out.append(clip(nome));continue
        st,dd=sy(f'T{i:02d}_D',testi);lead=0.7;qq=st[0][0]+lead
        o=[lead+dd*0.0+0.9+0.35*k+dd for k in range(4)]
        tend=lead+dd+2.0;th=[tend,tend+6.0];tr=th[1]+0.2;dr=dur(vox(f'T{i:02d}_R'));D=tr+dr+1.6
        v=video(P+'quizq.html',dict(tag=f'VERIFICA FINALE · DOMANDA {i} DI 20',domanda=q['d'],opz=q['o'],ok=q['ok'],spieg='',foot=FOOT),dict(q=qq,o=o,r=tr,think=th),D,SC,nome,extra="document.getElementById('sp').style.display='none'")
        a=audio([(vox(f'T{i:02d}_D'),lead),(vox(f'T{i:02d}_R'),tr)],D,f'{SC}{nome}.wav');salva(nome,v,a);out.append(clip(nome))
    return out
def compiti():
    out=[titolo('P3_compitiintro','COMPITI','Compiti',MAT,D=3.6,jing=[('titolo.wav',0.6)])]
    nome='P3_compiti'
    if fatto(nome):out.append(clip(nome));return out
    C=json.load(open(L+'compiti.json'));lead=0.8;t=lead;steps=[];vv=[]
    vv.append((vox('P2_COMPITI_INTRO'),t));t+=dur(vox('P2_COMPITI_INTRO'))+0.6
    for i in range(1,len(C)+1):
        d=dur(vox(f'C{i}_D'));steps.append([t,d]);vv.append((vox(f'C{i}_D'),t));t+=d+0.8
    D=t+4.0
    v=video(P+'compiti.html',dict(kicker='COMPITI · PREPARAZIONE',titolo='Rispondi alle seguenti domande',domande=C,foot=FOOT),steps,D,SC,nome)
    a=audio(vv,D,f'{SC}{nome}.wav');salva(nome,v,a);out.append(clip(nome));return out
def chiusura(nome,voce,testo_schermo):
    if fatto(nome):return clip(nome)
    lead=0.8;d=dur(vox(voce));D=lead+d+2.0
    v=video(P+'titolo.html',dict(k='PER OGGI È TUTTO' if 'P2_CHIUSURA'==voce else 'FINE DELLA PARTE',t=testo_schermo,f=MAT),[],D,SC,nome)
    a=audio([(vox(voce),lead)],D,f'{SC}{nome}.wav');salva(nome,v,a);return clip(nome)
