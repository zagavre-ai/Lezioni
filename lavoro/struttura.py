# Struttura della lezione: argomenti, card (testo del prof) e istanti d'accensione (secondi nell'originale).
def T(s):
    m,x=s.split(':');return int(m)*60+float(x)
def C(lead,testo,lit): return dict(lead=lead,testo=testo,lit=T(lit) if isinstance(lit,str) else lit)
ARG=[
 dict(n=1,titolo='La Repubblica di Weimar e gli anni Venti',slide='Le speranze della Repubblica di Weimar (anni Venti)',ini=239.88,
  kw=['Repubblica di Weimar','Accordi di Locarno','Società delle Nazioni','Patto Briand-Kellogg'],
  cards=[
   C('La ripresa post-crisi:','La ripresa post-crisi: dopo una forte instabilità economica e politica nel Dopoguerra, la seconda metà degli anni Venti registrò un periodo di normalizzazione e ripresa economica.','6:21.4'),
   C('Gli accordi di Locarno (1925):',"Gli accordi di Locarno (1925): firmati da Germania, Regno Unito, Francia, Belgio e Italia per stabilizzare l'Europa. La Germania accettò i confini occidentali e rinunciò alla guerra per risolvere le controversie.",'8:15.1'),
   C('Società delle Nazioni:','Società delle Nazioni: nel 1926 la Germania entrò a farne parte, simboleggiando il ritorno allo status di Stato sovrano e libero.','8:54.0'),
   C('Fiducia sul futuro:','Fiducia sul futuro: tra il 1925 e il 1929 la produzione industriale tedesca aumentò del 46%, la ricchezza pro capite crebbe del 12% e la disoccupazione si ridusse nettamente.','12:01.0'),
   C('Patto Briand-Kellogg (1928):','Patto Briand-Kellogg (1928): accordo internazionale firmato anche dalla Germania per rinunciare alla guerra come mezzo di risoluzione dei conflitti.','16:15.1')]),
 dict(n=2,titolo='La crisi del 1929 e il collasso della Germania',slide="L'impatto della crisi del 1929",ini=1039.13,
  kw=['Crollo di Wall Street','Iperinflazione','Disoccupazione','Partiti estremi'],
  cards=[
   C('Il crollo di Wall Street:',"Il crollo di Wall Street: nel 1929 le banche americane ritirarono i prestiti concessi alla Germania, provocando il rapido collasso dell'economia tedesca.",'19:32.8'),
   C('Conseguenze sociali:',"Conseguenze sociali: si verificarono l'iperinflazione, il dimezzamento dei flussi di credito, il crollo degli stipendi del 40% e una disoccupazione reale al 10%, alimentando il consenso per i partiti estremisti.",'20:37.3')]),
 dict(n=3,titolo='Il partito nazista e la sua ideologia',slide="L'ascesa del nazismo",ini=1676.09,
  kw=['NSDAP = partito nazista','Popolo omogeneo','Nazionalismo','Antisemitismo','Antibolscevismo'],
  cards=[
   C('La nascita del Partito Nazista (NSDAP):','La nascita del Partito Nazista (NSDAP): fondato nel 1920, mise al centro del programma l\'idea di un popolo omogeneo basato sulla purezza del sangue germanico ("razza ariana").','27:56.1'),
   C('Tratti ideologici fondamentali:','Tratti ideologici fondamentali:','35:18.3'),
   C('Nazionalismo esasperato','Nazionalismo esasperato e totale cancellazione del trattato di Versailles.','35:26.2'),
   C('Razzismo e antisemitismo radicato','Razzismo e antisemitismo radicato, identificando gli ebrei come responsabili della crisi economica.','35:54.8'),
   C('Antibolscevismo feroce','Antibolscevismo feroce, considerando comunisti e socialisti come rivali e minacce interne.','38:48.1')],
  immagini=[dict(file='s-004.png',lit='39:19.9',fine='40:59.2',titolo='Lo stemma nazista',did="L'immagine riproduce una spilla con la croce uncinata.")]),
 dict(n=4,titolo='Hitler, le SA e il putsch di Monaco',slide='La personalità di Hitler',ini=2462.37,
  kw=['Putsch di Monaco','Mein Kampf','SA = squadre d\'assalto','SS = squadre di protezione'],
  cards=[
   C('Il colpo di Stato fallito (1923):','Il colpo di Stato fallito (1923): dopo il fallimento del putsch di Monaco, Hitler fu arrestato e usò il processo per ottenere celebrità nazionale.','45:36.4'),
   C('Il "Mein Kampf":','Il "Mein Kampf": scritto in prigione, divenne il manifesto dell\'ideologia nazista, delineando gli obiettivi di distruzione del comunismo e di espansione territoriale per lo "spazio vitale" (Lebensraum).','46:05.2'),
   C('Le milizie paramilitari:','Le milizie paramilitari: la nascita delle SA (squadre d\'assalto) e successivamente delle SS (squadre di protezione), unità di combattimento fedeli a Hitler impiegate per violenze e intimidazioni politiche.','43:15.8')]),
 dict(n=5,titolo='Dalle elezioni alla nomina di Hitler',slide='La conquista del potere',ini=3169.78,
  kw=['Elezioni del 1930 e del 1932','Hindenburg','Hitler cancelliere','Reich = Stato'],
  cards=[
   C('Le elezioni del 1930 e del 1932:','Le elezioni del 1930 e del 1932: sfruttando la crisi e una propaganda aggressiva, la NSDAP divenne prima il secondo partito del Reich (1930) e poi il primo partito assoluto (1932).','52:49.8'),
   C('Hitler cancelliere:','Hitler cancelliere: il 30 gennaio 1933, dopo forti pressioni da parte di industriali e militari, il presidente Hindenburg nominò Hitler capo del governo.','61:30.2')],
  immagini=[dict(file='s-007.png',lit='62:01.8',fine='62:47.1',titolo='Le sfilate militari',did='La fotografia del 1926 ritrae Hitler mentre saluta la parata di un gruppo di SA (squadre d\'assalto).'),
            dict(file='s-009.png',lit='62:47.1',fine='63:04.5',titolo='Un poster di propaganda nazista',did="Il manifesto invita a votare la lista 9 della NSDAP (partito nazista) alle elezioni del 1930. Un pugnale trafigge la testa di un serpente, sulla quale è disegnato l'emblema della stella giudea.")]),
 dict(n=6,titolo='La costruzione dello Stato totalitario',slide='La costruzione dello Stato totalitario',ini=3784.93,
  kw=['Reichstag = il Parlamento tedesco','Pieni poteri','Partito unico','Führer = guida','Notte dei lunghi coltelli'],
  cards=[
   C("L'incendio del Reichstag (febbraio 1933):","L'incendio del Reichstag (febbraio 1933): usato come pretesto per emanare decreti d'emergenza che sospesero le libertà di stampa, parola e associazione.",'64:14.6'),
   C('La legge sui pieni poteri (marzo 1933):',"La legge sui pieni poteri (marzo 1933): approvata dal Parlamento sotto intimidazione, assegnò il potere legislativo all'esecutivo, eliminando il controllo dei deputati.",'68:25.7'),
   C('Dittatura a partito unico:','Dittatura a partito unico: nel giro di poche settimane vennero sciolti tutti gli altri partiti e a Dachau fu aperto il primo campo di concentramento per gli oppositori politici.','69:23.6'),
   C('Accentramento totale (1934):','Accentramento totale (1934): alla morte di Hindenburg, una legge unificò le cariche di capo del governo e capo dello Stato nella nuova figura del Führer.','73:43.5'),
   C('La Notte dei lunghi coltelli (1934):',"La Notte dei lunghi coltelli (1934): eliminazione violenta dell'ala radicale delle SA guidata da Ernst Röhm per azzerare ogni dissenso interno al partito.",'71:17.4')]),
 dict(n=7,titolo='Controllo della società ed economia',slide='Repressione e controllo della società ("nazificazione")',ini=4550.69,
  kw=['Gestapo = polizia segreta','SS = squadre di protezione','Gleichschaltung = allineamento','Gioventù hitleriana','Goebbels'],
  cards=[
   C('Apparato repressivo:','Apparato repressivo: affidato alla Gestapo (polizia segreta) e alle SS sotto la guida di Heinrich Himmler e Reinhard Heydrich per perseguitare oppositori, ebrei, rom e omosessuali.','75:50.7'),
   C('Gleichschaltung (Allineamento):','Gleichschaltung (Allineamento): sottomissione forzata di ogni aspetto della vita pubblica e privata alle direttive del partito. Sindacati e associazioni tradizionali vennero sciolti e sostituiti da istituzioni naziste (es. Fronte del lavoro tedesco).','77:40.7'),
   C('Inquadramento delle masse:','Inquadramento delle masse:','78:57.0'),
   C('Giovani:','Giovani: educazione scolastica riscritta su principi di razzismo e militarismo; obbligo di iscrizione alla "Gioventù hitleriana".','79:01.5'),
   C('Donne:','Donne: reintrodotte al ruolo primario di madri prolifiche per la patria, sebbene impiegate anche come ausiliarie o nel volontariato aziendale.','80:08.1'),
   C('Propaganda e censura:','Propaganda e censura: il ministero guidato da Joseph Goebbels controllò radio, cinema e giornali. Nel maggio 1933 vennero organizzati i celebri "roghi dei libri" per eliminare le opere considerate degenerate o contrarie all\'ideologia del regime.','81:06.6'),
   C('Dirigismo economico:','Dirigismo economico: forte intervento dello Stato nell\'economia attraverso grandi lavori pubblici (infrastrutture e autostrade) per assorbire la disoccupazione.','84:36.4'),
   C('Politica di riarmo:','Politica di riarmo: massicci investimenti statali nell\'industria pesante e bellica sotto la direzione di Hermann Göring (dal 1936) per preparare il paese alla conquista dello "spazio vitale".','86:26.6')],
  immagini=[dict(file='s-012.png',lit='79:48.3',fine='80:01.8',titolo='Joseph Goebbels',did='Il ministro della Propaganda Joseph Goebbels durante un comizio pubblico verso la metà degli anni Trenta.')]),
 dict(n=8,titolo='La politica razzista e antisemita',slide='Politica razzista e antisemita',ini=5355.72,
  kw=['Eugenetica = selezione dei "migliori"','Aktion T4','Leggi di Norimberga','Notte dei cristalli'],
  cards=[
   C('Politiche eugenetiche (1933):','Politiche eugenetiche (1933): introduzione della sterilizzazione forzata per persone affette da patologie mentali o fisiche, sfociata poi nel programma "Aktion T4" per l\'eliminazione dei disabili.','89:15.7'),
   C('Le Leggi di Norimberga (1935):','Le Leggi di Norimberga (1935): esclusione degli ebrei dalla cittadinanza tedesca, dai pubblici impieghi, dalle università e divieto di matrimoni misti.','90:49.3'),
   C('La Notte dei cristalli (novembre 1938):',"La Notte dei cristalli (novembre 1938): pogrom nazionale con la devastazione di sinagoghe, negozi e abitazioni ebraiche, culminato con l'arresto e la deportazione di circa 20.000 ebrei.",'91:28.8')]),
]
FINE_SRC=5786.18
# confini
INTRO_FINE=180.3   # fine della prima parte d'introduzione (frase intera, vedi controllo)
PARTE1=[1,2,3,4]; PARTE2=[5,6,7,8]
for _a in ARG:
    for _im in _a.get('immagini',[]):
        _im['lit']=T(_im['lit']) if isinstance(_im['lit'],str) else _im['lit']
        _im['fine']=T(_im['fine']) if isinstance(_im['fine'],str) else _im['fine']
