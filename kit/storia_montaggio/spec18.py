# Dati della lezione 18 (L'Italia repubblicana): argomenti, scene di approfondimento, mappe
TITOLO="L'Italia repubblicana"
ARGS=[ # (titolo scheda, esempio sotto il titolo, quiz)
 ("Un Paese da ricostruire","bombardamenti · mercato nero · violenza"),
 ("La nascita della Repubblica","partiti di massa · amnistia · referendum"),
 ("La Costituzione","madri costituenti · tre poteri · 1948"),
 ("Il Centrismo (1948-1953)","elezioni del 1948 · riforme · blocco occidentale"),
 ("Il miracolo economico","boom · consumi · migrazioni"),
 ("Il Centrosinistra (1953-1963)","Fanfani e Moro · ENEL · scuola media unica"),
]
def T(c,h,s='',**k):
    d=dict(cue=c,h=h,s=s);d.update(k);return d
AN={
'AN1a':dict(kick='Un Paese da ricostruire',title="L'Italia alla fine della guerra",items=[
  T('Primo:','Bombardamenti e rappresaglie','soprattutto al Nord · decimazioni: 10 italiani per 1 tedesco'),
  T('Secondo:','Economia ferma','strade e ferrovie saltate · produzione di guerra da riconvertire'),
  T('Terzo:','La vita di ogni giorno','inflazione galoppante · cibo scarso · mercato nero'),
  T('Il Nord, dove','Il Nord è il più colpito','qui c\'è davvero tutto da rifare')]),
'AN1b':dict(kick='Un Paese da ricostruire',title="L'ordine pubblico è precario",items=[
  T('Nel Centro-Nord','Centro-Nord','regolamenti di conti contro gli ex fascisti'),
  T('Nel Sud','Sud','lotte contadine: occupazione dei latifondi'),
  T('Lo Stato è fragile','Stato fragile','la forza pubblica reprime le proteste'),
  T('Il clima sociale','Conflitti di classe','un Paese sfiduciato dopo la guerra perduta')]),
'AN1c':dict(kick='Un Paese da ricostruire',title='Dalla guerra alla ricostruzione',layout='timeline',items=[
  T('Nel giugno del millenovecentoquarantaquattro','giugno 1944','i tedeschi lasciano Roma',lab='giugno 1944'),
  T('Ma il Nord','primavera 1945','il Nord resta difeso dai tedeschi',lab='fino al 1945'),
  T('Quando la guerra finisce','Fine della guerra','riconvertire la produzione, ricostruire',lab='dopo la guerra')]),
'AN2a':dict(kick='La nascita della Repubblica',title='Dalla fine della guerra alla Repubblica',layout='timeline',items=[
  T('Nel giugno del millenovecentoquarantacinque','Governo Parri','molto radicale, dura pochi mesi',lab='giugno 1945'),
  T('A dicembre','Primo governo De Gasperi','unità nazionale con tutti i partiti antifascisti',lab='dicembre 1945'),
  T('Il due giugno','Referendum','gli italiani scelgono tra Monarchia e Repubblica',lab='2 giugno 1946'),
  T('Nello stesso anno nasce','Assemblea Costituente','scrive la nuova Costituzione',lab='1946')]),
'AN2b':dict(kick='La nascita della Repubblica',title='I tre leader dei partiti di massa',img='p4',items=[
  T('Alcide De Gasperi guida','De Gasperi','Democrazia Cristiana · ultimo premier del Regno, primo della Repubblica'),
  T('Palmiro Togliatti','Togliatti','Partito comunista · amnistia per i reati politici'),
  T('Pietro Nenni','Nenni','Partito socialista italiano'),
  T('Accanto a questi','Partiti minori','Azione · repubblicani · liberali · monarchici')]),
'AN2c':dict(kick='La nascita della Repubblica',title='I numeri del referendum',items=[
  T('Circa dodici','12 milioni','scelgono la Repubblica',big=1),
  T('Circa dieci','10 milioni','votano per la Monarchia',big=1),
  T('Per la prima volta','Votano le donne','per la prima volta',),
  T('Il re Umberto','Re Umberto II','parte per l\'esilio, in Portogallo')]),
'AN3a':dict(kick='La Costituzione',title='I tratti della nuova Costituzione',items=[
  T('Tra i cinquecentocinquantasei','556 membri','tra loro 21 donne: le madri costituenti'),
  T('La Costituzione entra','1° gennaio 1948','repubblica democratica fondata sul lavoro'),
  T('Il potere legislativo','Tre poteri','Parlamento · Governo · Magistratura'),
  T('E nella Repubblica','La fiducia','il Governo deve chiederla al Parlamento')]),
'AN3b':dict(kick='La Costituzione',title="Che cosa cambia rispetto al Regno d'Italia",items=[
  T('Fino a poco prima','Il Regno','Statuto del Regno di Sardegna e d\'Italia'),
  T('Il Parlamento resta','Due Camere','Camera dei deputati e Senato'),
  T('Ma nel Regno','Il Governo','nel Regno incaricato dal re · nella Repubblica chiede la fiducia'),
  T('Dopo le elezioni','1948','prima legislatura repubblicana: dura cinque anni')]),
'AN3c':dict(kick='La Costituzione',title='Chi scrive davvero la Costituzione',items=[
  T('Il primo partito','La DC','circa 35% · con socialisti e comunisti ha la maggioranza'),
  T('Tra le ventuno','21 donne','democristiane, comuniste, socialiste, liberali, Uomo Qualunque'),
  T('Anche la tutela','La famiglia','scritta soprattutto dai cattolici'),
  T('Poi la Costituzione','Entra in vigore','firmata dal presidente provvisorio, governo De Gasperi')]),
'AN4a':dict(kick='Il Centrismo',title="L'Italia dopo la pace di Parigi",img='p5',items=[
  T('Con la pace','Pace di Parigi','febbraio 1947 · l\'Italia paga la guerra fascista'),
  T('Perde le colonie','Le perdite','colonie, territori e alcune località di frontiera'),
  T('Ma, a differenza','Non viene divisa','a differenza della Germania'),
  T('La città di Trieste','Trieste','zona A angloamericana · zona B jugoslava')]),
'AN4b':dict(kick='Il Centrismo',title='Le elezioni del 1948',items=[
  T('La Democrazia Cristiana, sostenuta','DC 48%','con Chiesa e Stati Uniti: quasi la maggioranza assoluta'),
  T('Dall\'altra parte','Fronte popolare','comunisti e socialisti, legati all\'URSS'),
  T('Nel luglio','Luglio 1948','attentato a Togliatti: Paese sull\'orlo della guerra civile'),
  T('Ma la Democrazia Cristiana ha bisogno','51% dei seggi','alleanza con repubblicani, liberali, socialdemocratici')]),
'AN4c':dict(kick='Il Centrismo',title='Le scelte dei governi De Gasperi',items=[
  T('Prima la linea','Economia','liberista · Einaudi · aiuti americani'),
  T('Poi le riforme','Riforme','riforma agraria · Cassa per il Mezzogiorno'),
  T('Infine la politica estera','Politica estera','Piano Marshall · NATO (aprile 1949) · CECA'),
  T('Con questi interventi','Anni Cinquanta','normalità e tranquillità, ma ancora senza vera crescita')]),
'AN5a':dict(kick='Il miracolo economico',title='Il boom del 1958-1963',items=[
  T('Il boom economico è','1958-1963','il quinquennio del boom'),
  T('In questi anni','+6% all\'anno','crescita del prodotto interno lordo',big=1),
  T('Un Paese essenzialmente','Da agricolo a industriale','il simbolo: la Fiat Cinquecento'),
  T('Il debito pubblico','Debito contenuto','onda lunga del Piano Marshall')]),
'AN5b':dict(kick='Il miracolo economico',title='Le due facce del boom',img='p8',items=[
  T('Da un lato','Nuovi consumi','elettrodomestici, auto, televisione, vacanze'),
  T('Dall\'altro','Nord e Sud','divario e migrazione interna'),
  T('Le grandi città','Città caotiche','periferie povere · cementificazione'),
  T('Torino, per esempio','Torino','operai dal Sud in periferie costruite in fretta')]),
'AN5c':dict(kick='Il miracolo economico',title="La nuova struttura dell'economia",items=[
  T('Il settore primario','Primario','l\'agricoltura perde peso'),
  T('Nel settore secondario','Secondario','industria: una crescita che nessuno si aspettava'),
  T('Cresce anche il terziario','Terziario','servizi e trasporti'),
  T('E con le ferie','Ferie retribuite','la vacanza al mare entra nelle famiglie')]),
'AN6a':dict(kick='Il Centrosinistra',title='Le tappe verso il centrosinistra',layout='timeline',items=[
  T('Nel millenovecentocinquantasei','Fatti d\'Ungheria','il PCI verso l\'autonomia dall\'URSS',lab='1956'),
  T('Nel millenovecentosessantadue','Centrosinistra','governi con Fanfani e i socialisti',lab='1962'),
  T('Nel millenovecentosessantatré','Governo Moro','il primo governo organico',lab='1963'),
  T('Nel millenovecentosessantaquattro muore','Muore Togliatti','prima crisi economica · Piano Solo',lab='1964')]),
'AN6b':dict(kick='Il Centrosinistra',title='Le riforme del centrosinistra',img='p11',items=[
  T("L'ENEL nasce",'ENEL','nazionalizzazione dell\'energia elettrica'),
  T('La scuola media unica','Scuola media unica','obbligatoria fino a quattordici anni'),
  T('Dietro queste riforme','Dialogo con i socialisti','voluto da Fanfani e da Moro')]),
'AN6c':dict(kick='Il Centrosinistra',title='Luci e ombre',items=[
  T('Le luci sono','Luci','riforme sociali · papa Giovanni XXIII · Concilio Vaticano II'),
  T('Le ombre sono','Ombre','tensioni con i conservatori · Piano Solo'),
  T('Secondo il Piano Solo','Piano Solo','carabinieri del generale De Lorenzo: un colpo di stato?'),
  T('Il generale lasciò','Dopo','De Lorenzo diventa parlamentare')]),
}
# mappe concettuali (rami nell'ordine in cui la voce li nomina; cue = frase della voce)
def R(c,p,e,cue,s=None):
    d=dict(concetto=c,parola=p,esempio=e,cue=cue)
    if s:d['sotto']=s
    return d
MAPS={
'MAP1':dict(titolo='Un Paese da ricostruire',rami=[
  R('Le distruzioni','bombardamenti','fabbriche e strade','Primo ramo'),
  R("L'economia",'produzione ferma','mercato nero','Secondo ramo'),
  R('La popolazione','disoccupazione','reduci e sfollati','Terzo ramo'),
  R('Centro-Nord','violenza','regolamenti di conti','Quarto ramo'),
  R('Il Sud','lotte contadine','terre dei latifondisti','Quinto ramo')]),
'MAP2':dict(titolo='La nascita della Repubblica',rami=[
  R('Partiti di massa','DC, PCI, PSI','De Gasperi, Togliatti, Nenni','Primo ramo'),
  R('Pacificazione','amnistia','promossa da Togliatti','Secondo ramo'),
  R('Referendum','2 giugno 1946','votano anche le donne','Terzo ramo'),
  R('Il risultato','Repubblica','12 milioni contro 10','Quarto ramo'),
  R('Assemblea Costituente','1946','scrive la Costituzione','Quinto ramo')]),
'MAP3':dict(titolo='La Costituzione',rami=[
  R('Madri costituenti','21 donne','Iotti, Merlin, Mattei','Primo ramo'),
  R('Entrata in vigore','1° gennaio 1948','repubblica fondata sul lavoro','Secondo ramo'),
  R('Parlamento','potere legislativo','fa le leggi','Terzo ramo'),
  R('Governo','potere esecutivo','chiede la fiducia','Quarto ramo'),
  R('Magistratura','potere giudiziario','giudica','Quinto ramo')]),
'MAP4':dict(titolo='Il Centrismo',rami=[
  R('Elezioni 1948','vittoria DC','contro il Fronte popolare','Primo ramo'),
  R('Pace di Parigi','perdite','Trieste divisa','Secondo ramo'),
  R('Linea economica','liberista','De Gasperi ed Einaudi','Terzo ramo'),
  R('Riforme','riforma agraria','Cassa per il Mezzogiorno','Quarto ramo'),
  R('Politica estera','blocco occidentale','Marshall, NATO, CECA','Quinto ramo')]),
'MAP5':dict(titolo='Il miracolo economico',rami=[
  R('Le cause','blocco occidentale','CEE, lavoro a basso costo','Primo ramo'),
  R('Settori trainanti','industria','auto, siderurgia, chimica','Secondo ramo'),
  R('I consumi','nuovi stili di vita','TV, auto, elettrodomestici','Terzo ramo'),
  R('Le migrazioni','Sud verso Nord','dalle campagne alle città','Quarto ramo'),
  R('Le criticità','divario Nord-Sud','periferie, cementificazione','Quinto ramo')]),
'MAP6':dict(titolo='Il Centrosinistra',rami=[
  R('Fanfani e Moro','sinistra DC','guidano i governi','Primo ramo'),
  R('Alleanza','Partito socialista','Nenni','Secondo ramo'),
  R('Governi','dal 1962','centrosinistra','Terzo ramo'),
  R('ENEL','nazionalizzazione','energia elettrica','Quarto ramo'),
  R('Scuola media unica','obbligo a 14 anni','fine dell\'avviamento','Quinto ramo'),
  R('Partito comunista','autonomia','dopo l\'Ungheria del 1956','Sesto ramo')]),
'MAPF1':dict(titolo='Italia repubblicana · parte 1',rami=[
  R('Le macerie','mercato nero','violenza','Dalle macerie'),
  R('Partiti di massa','DC, PCI, PSI','','Alla scena politica'),
  R('Referendum','2 giugno 1946','vince la Repubblica','Fino al referendum'),
  R('Assemblea Costituente','21 madri costituenti','','Poi l\'Assemblea'),
  R('Costituzione','1° gennaio 1948','tre poteri separati','Infine la Costituzione')]),
'MAPF2':dict(titolo='Italia repubblicana · parte 2',rami=[
  R('Il Centrismo','DC al governo','vittoria del 1948','Il Centrismo'),
  R('Governi De Gasperi','riforma agraria','Cassa, Patto Atlantico','Le scelte'),
  R('Miracolo economico','1958-1963','Fiat Cinquecento','Il miracolo'),
  R('Le criticità','divario Nord-Sud','migrazioni, periferie','Le sue criticità'),
  R('Centrosinistra','DC e socialisti','ENEL, scuola media','Infine il centrosinistra')]),
}
