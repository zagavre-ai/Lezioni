import json,sys,os,subprocess,re
sys.path.insert(0,'/tmp/w14');sys.path.insert(0,'/tmp/w14/build')
import gen
gen.PROFON=False
E=gen.E
D={
(1,'AN01'):('La vita di Pirandello',[("La nascita","Girgenti","Oggi Agrigento: famiglia agiata, borghese."),("Il disastro","Le miniere di zolfo","La ricchezza di famiglia e la dote della moglie vanno perse."),("La famiglia","La moglie Antonietta","Una malattia mentale, anche con ricoveri."),("Gli studi","Roma e la Germania","Cultura internazionale, contatti che durano nel tempo."),("Il lavoro","Scrittore e professore","Insegna all'università."),("La politica","Il fascismo","Aderisce al regime, forse per paura.")]),
(1,'AN02'):('Le basi del pensiero di Pirandello',[("La vita","Un flusso continuo","Non si riesce mai a fissarlo: siamo destinati a fallire."),("Le influenze","Bergson e Binet","Il vitalismo del filosofo francese; la psicologia."),("La crisi dell'io","Identità in frantumi","L'io non è unico: è un prisma di tante sfumature.")]),
(1,'AN05'):('La trappola sociale',[("La maschera","L'io frantumato","L'identità si riduce a una maschera imposta dalle convenzioni."),("La trappola","Famiglia e lavoro","Le istituzioni sociali imprigionano l'uomo in una condizione infelice."),("La via di fuga","Follia, immaginazione, natura","Il rifiuto del sociale, per sfuggire all'oppressione.")]),
(1,'AN04'):("L'umorismo di Pirandello",[("Il comico","Avvertimento del contrario","Nasce dalla percezione di una situazione ridicola."),("La riflessione","Qualcosa di più","Ci si chiede perché: dietro il ridicolo c'è qualcosa di triste."),("Il tragico","Sentimento del contrario","La scomposizione della realtà porta alla comprensione.")]),
(1,'AN07'):('Il fu Mattia Pascal',[("La trama","Creduto morto","Un piccolo borghese tenta di costruirsi una nuova identità: Adriano Meis."),("Il fallimento","Nessun legame legale","Senza identità non può stabilire legami sociali."),("La conclusione","Il forestiere della vita","Narratore inattendibile della propria storia.")]),
(1,'AN08'):('Quaderni di Serafino Gubbio operatore',[("Il tema","La critica alle macchine","Tecnologia e industria portano all'alienazione dell'uomo."),("La conseguenza","Sentimenti cancellati","Le macchine sono i nuovi padroni: l'uomo è loro schiavo."),("La fine","Il silenzio","Dopo un delitto reale, il protagonista si chiude nel mutismo.")]),
(1,'AN10'):('Uno, nessuno e centomila',[("L'approdo","La parabola pirandelliana","L'evoluzione estrema della critica all'identità."),("Dall'angoscia alla libertà","Vitangelo Moscarda","Accetta la perdita d'identità come condizione positiva."),("La natura","Via il proprio nome","Morire e rinascere in ogni istante, nel flusso della vita.")]),
(2,'AN01'):('Il teatro grottesco e Il giuoco delle parti',[("Il periodo grottesco","Oltre il dramma borghese","Deformazione e assurdo superano il dramma naturalistico."),("Il protagonista","Leone Gala","Un «filosofo» che guarda la vita dall'alto, con l'intelletto."),("La sconfitta","La maschera cade","Le passioni represse esplodono e generano la tragedia.")]),
(2,'AN03'):("Sei personaggi in cerca d'autore",[("La forma","Il teatro nel teatro","Si rompe la finzione scenica e l'illusione realistica."),("La trama","Sei personaggi rifiutati","Cercano di far recitare la propria verità ad attori mediocri."),("Il risultato","La verità deformata","Gli attori la deformano: impossibile comunicare."),("Lo stile","Comico e tragico","Si fondono: rispecchiano la frammentazione della psiche.")]),
(2,'AN05'):('Enrico IV: la follia come salvezza',[("La finzione cosciente","Un uomo si crede imperatore","Guarito, sceglie di continuare a fingere la pazzia."),("La maschera","Una protezione","La follia è l'unico strumento di difesa contro la società."),("La condanna","Pazzo per sempre","Dopo la vendetta sul rivale, non può più tornare indietro.")]),
(2,'AN07'):("L'ultima produzione e le ultime novelle",[("Il pirandellismo","Una ripetizione stanca","Cerebralismo e forme artificiose."),("Anni Trenta","Verso il mito","Dimensione mitica, fantastica e simbolica."),("Incompiuto","I giganti della montagna","Il ruolo dell'arte nella società industriale."),("Le novelle","Il ritorno al profondo","Gli impulsi più oscuri dell'inconscio."),("Il clima","Allucinato e surreale","Lontano dal realismo borghese iniziale."),("Esempi","Una giornata; Di sera, un geranio","La morte e il rapido scorrere del tempo.")]),
(2,'AN09'):('Ciàula scopre la luna',[("L'ambiente","Le miniere di zolfo","Un contesto di ritmi disumani e di sfruttamento."),("Il protagonista","Ciàula","Un caruso quasi privo di coscienza di sé."),("L'unica paura","Il buio della notte","Nata dopo un'esplosione che ferì il padrone."),("Il momento centrale","L'uscita dalla miniera","La luna risplende nel cielo, inattesa."),("L'epifania","Un risveglio","Una rivelazione interiore: Ciàula piange."),("Il senso","Una rinascita","Recupera dignità e un legame con la natura.")]),
(2,'AN11'):('Il treno ha fischiato',[("La struttura","Un'inchiesta","Prima i colleghi, poi il narratore testimone."),("La trappola","Casa e ufficio","Un inferno familiare e un lavoro di angherie."),("La svolta","Il fischio del treno","Parole senza senso: tutti lo credono pazzo."),("L'umorismo","La ragione dietro la follia","Il fischio ridesta la coscienza del mondo esterno."),("Il finale","La routine riprende","Con una nuova consapevolezza, è una fuga solo immaginata.")]),
}
def html(title,cards,k,pag):
    g=(k-1)//3 if k>0 else 0;sub=list(range(g*3,min(k,g*3+3)))
    body=f'<div style="position:absolute;left:80px;top:146px;width:1760px"><div class="lab">APPROFONDIMENTO</div><div class="tit" style="margin-top:34px;font-size:{56 if len(title)>44 else 64}px">{E(title)}</div><div class="bar"></div>'
    body+='<div style="margin-top:40px;display:flex;flex-direction:column;gap:20px">'
    for i in sub:
        l,t,b=cards[i];on=' on' if i==k-1 else ''
        body+=f'<div class="card nc{on}" style="padding:20px 34px;font-size:40px;line-height:1.5"><div class="n">{i+1}</div><div><div class="lab" style="font-size:18px;letter-spacing:2.5px">{E(l)}</div><div style="font:800 40px/1.2 Bric;margin:6px 0 4px;color:#0B1530">{E(t)}</div><div style="font:500 36px/1.4 Fig;color:#0B1530">{E(b)}</div></div></div>'
    body+='</div></div>'
    return gen.page(body,(pag+g) if pag else None,prof=False)
ENC=['-c:v','libx264','-preset','veryfast','-crf','19','-pix_fmt','yuv420p','-r','30','-an','-x264-params','keyint=60:scenecut=0','-threads','2']
made=[];PG=json.load(open('/tmp/w14/pg_next.json'));PAG={1:PG['1'],2:PG['2']}
for (P,n),(title,cards) in D.items():
    TL=json.load(open(f'/tmp/w14/tl{P}.json'));a,d=[(a,d) for nn,a,d in TL if nn==n][0]
    nf=round((a+d)*30)-round(a*30);N=len(cards)
    starts=[0]+[round(nf*(0.06+0.84*i/N)) for i in range(N)]+[nf]
    parts=[]
    for k in range(N+1):
        nm=f'an_{P}_{n}_{k}';gen.scrivi(nm,html(title,cards,k,PAG[P]));parts.append((nm,starts[k+1]-starts[k]))
    made.append((P,n,parts));PAG[P]+=max(1,-(-N//3))
subprocess.run(['node','/tmp/w14/build/render.js','/tmp/w14/build/html','/tmp/w14/build/png'],check=True)
for P,n,parts in made:
    out=f'/tmp/w14/new{P}/{n}.mp4';segs=[]
    for i,(nm,k) in enumerate(parts):
        if k<=0: continue
        po=f'/tmp/w14/build/an_{P}_{n}_{i}.mp4'
        subprocess.run(['ffmpeg','-v','error','-y','-loop','1','-framerate','30','-t',f'{k/30:.4f}','-i',f'/tmp/w14/build/png/{nm}.png','-frames:v',str(k),*ENC,po],check=True);segs.append(po)
    L=f'/tmp/w14/build/lan_{P}_{n}.txt';open(L,'w').write(''.join(f"file '{s}'\n" for s in segs))
    subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',L,'-c','copy',out],check=True);print(P,n,sum(k for _,k in parts),flush=True)
