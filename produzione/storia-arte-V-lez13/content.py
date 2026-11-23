# contenuti della lezione 13 (solo dal materiale del prof): immagini, mappe, quiz, argomenti
W='/tmp/claude-0/w/prod';IM=W+'/im/'
ARG=[("L'Italia fascista e il controllo delle arti",["Fasci","Marcia su Roma","Podestà","Sventramenti"]),
     ("L'architettura tra tradizione classica e Razionalismo",["Razionalismo","Muzio","Terragni","Piacentini","EUR"]),
     ("Il ritorno all'ordine e la Metafisica",["Ritorno all'ordine","de Chirico","Carrà","Morandi"]),
     ("Il Novecento italiano e l'opposizione",["Sarfatti","Sironi","Corrente"])]
LAB=["01 · L'Italia fascista","02 · L'architettura del ventennio","03 · Ritorno all'ordine e Metafisica","04 · Il Novecento italiano"]
# nome -> (titolo, [file], didascalia, parole chiave)
IMG={
 'vittoria':("Piazza della Vittoria, Brescia",['vittoria'],"Marcello Piacentini, Piazza della Vittoria, 1927-32, Brescia, fotografia d'epoca",['Brescia','Piacentini','1927-1932','Razionalismo']),
 'conc_dopo':("Via della Conciliazione, Roma",['conc_dopo'],"Veduta di piazza San Pietro dopo l'apertura di via della Conciliazione, Roma",['Via della Conciliazione','San Pietro','Sventramenti']),
 'conc_2':("Piazza San Pietro prima e dopo",['conc_prima','conc_dopo'],"Piazza San Pietro prima e dopo l'apertura di via della Conciliazione (1936-1950)",['Spina di Borgo','Patti Lateranensi','1936-1950']),
 'casa_facciata':("Casa del Fascio, Como",['casa_facciata'],"Giuseppe Terragni, Casa del Fascio (ex), 1932-36, Como, facciata principale",['Terragni','Como','1932-1936','Razionalismo']),
 'casa_pianta':("Casa del Fascio: la pianta",['casa_pianta'],"Casa del Fascio (ex): pianta del piano terra (in verde, la corte centrale)",['Quadrato perfetto','Corte centrale','Cemento armato']),
 'casa_int':("Casa del Fascio: gli interni",['casa_corte','casa_sala'],"Casa del Fascio (ex): la corte centrale e la sala del Direttorio",['Corte centrale','Vetrocemento']),
 'palazzo':("Palazzo della Civiltà Italiana, EUR",['palazzo'],"Guerrini, La Padula, Romano, Palazzo della Civiltà, 1938-53, Roma (EUR)",['Colosseo quadrato','Archi a tutto sesto','Travertino']),
 'e42':("Esposizione Universale di Roma",['e42'],"Marcello Piacentini, Planimetria generale del sito dell'Esposizione Universale di Roma, 1938",['EUR','E42','Piacentini','Asse centrale']),
 'canto':("Giorgio de Chirico, Canto d'amore",['canto'],"Giorgio de Chirico, Canto d'amore, 1914",['Metafisica','Apollo del Belvedere','Guanto di gomma','Palla verde']),
 'muse':("Giorgio de Chirico, Le muse inquietanti",['muse'],"Giorgio de Chirico, Le muse inquietanti, 1918",['Ferrara','Manichini','Castello estense']),
 'carra':("Carlo Carrà, La musa metafisica",['carra'],"Carlo Carrà, La musa metafisica, 1917",['Carrà','Realismo mitico','Istria']),
 'morandi':("Giorgio Morandi, Natura morta metafisica",['morandi'],"Giorgio Morandi, Natura morta metafisica con la squadra",['Morandi','Oggetti quotidiani','Volumi geometrici']),
}
# pagine del prof a card: (pagina pdf) -> raggruppamento in sotto-slide
PACK={3:[[0,1],[2]],5:[[0,1],[2,3]],7:[[0,1],[2]],10:[[0,1],[2]],11:[[0,1],[2]],12:[[0,1],[2,3]]}
KW={(3,0):['Biennio rosso','Fasci','Marcia su Roma'],(3,1):['Italianità','Impero romano','Podestà'],(3,2):['Tradizione','Modernità'],
    (5,0):['Avanguardie','Futurismo','Tradizione'],(5,1):['De Chirico','Antimoderno','Enigma'],(5,2):['Spazio sospeso','Ombre lunghe'],(5,3):['Manichini','Alienazione'],
    (7,0):['Le muse inquietanti','Ferrara'],(7,1):['Savinio','Carrà','Realismo mitico'],(7,2):['Morandi','Nature morte'],
    (10,0):['Sarfatti','Novecento','Sironi'],(10,1):['Sironi','Solitudini urbane'],(10,2):['Corrente','Via Cavour','Sei di Torino'],
    (11,0):['Pluralità di stili','Classicismo','Razionalismo'],(11,1):['Muzio','Via Principe Umberto'],(11,2):['Terragni','Casa del Fascio','Cemento armato'],
    (12,0):['Sventramenti','Via della Conciliazione'],(12,1):['Piacentini','Sintesi di regime'],(12,2):['EUR','Esposizione 1942'],(12,3):['Colosseo quadrato']}
# mappe del prof (stesse parole, ridisegnate): boxes, arrows, passi (id box, frase iniziale nella voce)
MAPPE={
'arch':dict(voce='MAPPA_ARCH',titolo="Come risponde l'architettura dell'Italia fascista al regime?",
 boxes=[('c','l1',545,160,830,120,"Architettura Italia fascista"),
  ('a','pag',60,400,700,220,"L'architettura deve rispondere ai requisiti del regime"),
  ('b','pag',60,700,640,300,"Monumentalità<br>Tradizione storica<br>Modernità industriale<br>Romanità"),
  ('p','men',1040,400,820,340,"Architetto di punta del regime: Marcello Piacentini<br>- Rigore geometrico<br>- Razionalismo<br>- Grandiosità monumentale"),
  ('v','men',1040,830,820,150,"Via della Conciliazione<br>E42")],
 arrows=[('1',720,290,540,390,'a'),('2',1290,290,1420,390,'p'),('3',730,850,1020,640,'b'),('4',1450,750,1450,820,'v')],
 passi=[('c','Architettura Italia fascista.'),('a',"L'architettura deve"),('b','Monumentalità.'),('p','Architetto di punta'),('v','Via della Conciliazione.')]),
'meta':dict(voce='MAPPA_META',titolo="Che cos'è la metafisica?",
 boxes=[('c','l1',545,160,830,120,"La metafisica"),
  ('a','pag',60,400,780,240,"Avanguardia: superare il Futurismo e tornare alla tradizione figurativa"),
  ('o','pag',1040,400,820,360,"Le opere della metafisica hanno:<br>atmosfere sospese<br>ombre lunghe<br>staticità<br>piazze deserte<br>assenza umana"),
  ('e','men',60,730,860,300,"Esponenti:<br>Giorgio de Chirico<br>Carlo Carrà<br>Alberto Savinio<br>Giorgio Morandi")],
 arrows=[('1',740,290,520,390,'a'),('2',1290,290,1420,390,'o'),('3',860,520,1020,560,'o'),('4',1100,780,930,850,'e')],
 passi=[('c','La metafisica.'),('a','Avanguardia:'),('o','Le opere della'),('e','Esponenti:')]),
}
QUIZ={
 'Q1':("Quiz 1 · L'Italia fascista e il controllo delle arti",[
  ("In quale anno Mussolini fonda i Fasci italiani di combattimento?","1919",["1912","1922","1925"],"I Fasci italiani di combattimento sono fondati da Benito Mussolini nel 1919."),
  ("Quale evento del 1922 porta il re a incaricare Mussolini di formare il governo?","La Marcia su Roma",["Il Biennio rosso","L'assassinio di Matteotti","I Patti Lateranensi"],"In seguito alla Marcia su Roma dell'ottobre 1922 il re incarica Mussolini di formare il governo."),
  ("Che cosa accade all'inizio del 1925?","Mussolini si proclama Duce e sopprime le libertà di stampa e di associazione",["Nasce il Partito Comunista Italiano","Mussolini lascia il governo","Si firmano i Patti Lateranensi"],"Nel 1925 Mussolini si proclama Duce, sopprimendo le libertà di stampa e di associazione."),
  ("Che cosa sono gli «sventramenti»?","Demolizioni di quartieri storici medievali o barocchi per aprire nuove strade",["Restauri dei monumenti antichi","Nuovi quartieri di campagna","Mostre d'arte del regime"],"Sventramenti: operazioni di demolizione dei tessuti storici medievali o barocchi."),
  ("Quale piazza di Brescia fu progettata da Marcello Piacentini tra il 1927 e il 1932?","Piazza della Vittoria",["Piazza della Loggia","Piazza San Pietro","Piazza del Popolo"],"Piazza della Vittoria, a Brescia, è stata realizzata tra il 1927 e il 1932.")]),
 'Q2':("Quiz 2 · L'architettura tra tradizione classica e Razionalismo",[
  ("Chi progetta la Casa del Fascio di Como?","Giuseppe Terragni",["Marcello Piacentini","Giovanni Muzio","Mario Sironi"],"Giuseppe Terragni progetta la Casa del Fascio di Como, tra il 1932 e il 1936."),
  ("Che forma ha la pianta della Casa del Fascio di Como?","Un quadrato perfetto",["Un cerchio","Un rettangolo molto allungato","Una croce"],"La pianta dell'edificio è un quadrato perfetto."),
  ("Che cosa significa la sigla EUR?","Esposizione Universale di Roma",["Esposizione Urbana Romana","Edificio Unico Razionalista","Ente Urbanistico di Roma"],"EUR: Esposizione Universale di Roma, detta anche E42."),
  ("Con quale soprannome è noto il Palazzo della Civiltà Italiana?","Colosseo quadrato",["Casa del Fascio","Ca' Brutta","Palazzo del Duce"],"Il palazzo è noto come «Colosseo quadrato»."),
  ("Quale architetto, architetto di punta del regime, unisce il rigore razionalista alla monumentalità?","Marcello Piacentini",["Giuseppe Terragni","Giovanni Muzio","Giovanni Guerrini"],"Piacentini coniuga il rigore geometrico del razionalismo con la grandiosità monumentale.")]),
 'Q3':("Quiz 3 · Il ritorno all'ordine e la Metafisica",[
  ("Chi è l'ideatore della pittura metafisica?","Giorgio de Chirico",["Carlo Carrà","Mario Sironi","Felice Casorati"],"Giorgio de Chirico è l'ideatore della pittura metafisica."),
  ("In quale città si sviluppa la pittura metafisica dal 1917?","Ferrara",["Milano","Torino","Roma"],"La pittura metafisica si sviluppa a Ferrara dal 1917."),
  ("Quale oggetto color mattone è inchiodato al muro in «Canto d'amore»?","Un guanto di gomma",["Una squadra da disegno","Un manichino da sarto","Una palla verde"],"In «Canto d'amore» c'è un grande guanto di gomma color mattone inchiodato al muro."),
  ("Quale caratteristica appartiene alla pittura metafisica?","Scene sospese, prive di tempo, con ombre lunghe",["Pennellate rapide e colori puri","Soggetti dinamici e velocissimi","Scomposizione cubista delle forme"],"Scene sospese, prive di tempo, con prospettive deformate e ombre lunghe."),
  ("A quale approdo artistico arriva Carlo Carrà dopo il Futurismo?","A un personale «realismo mitico»",["All'Impressionismo","Al Dadaismo","Alla pittura murale monumentale"],"Carrà passa dal Futurismo alla Metafisica, approdando a un personale «realismo mitico».")]),
 'Q4':("Quiz 4 · Il Novecento italiano e l'opposizione",[
  ("In quale anno nasce a Milano il gruppo del Novecento Italiano?","1922",["1910","1919","1925"],"Il Gruppo del Novecento è fondato a Milano nel 1922."),
  ("Quale critica d'arte guida il Gruppo del Novecento?","Margherita Sarfatti",["Maria Gironi","Silvana Cenni","Alberto Savinio"],"Il gruppo è guidato dalla critica d'arte Margherita Sarfatti."),
  ("Chi dipinge le cupe periferie urbane e le solitudini delle città moderne?","Mario Sironi",["Arturo Martini","Giorgio Morandi","Felice Casorati"],"Sironi traduce lo spirito del tempo in paesaggi urbani cupi e monumentali."),
  ("Quale movimento milanese, fondato da Ernesto Treccani, va contro la mentalità fascista?","Corrente",["Futurismo","Novecento","Scuola di via Cavour"],"A Milano si forma il movimento Corrente, fondato da Ernesto Treccani."),
  ("Che cos'è la scuola di via Cavour?","Un gruppo di Roma contrario alla retorica monumentale del fascismo",["Una scuola di architettura di Milano","Un gruppo di pittori di Torino","Il gruppo di Margherita Sarfatti"],"A Roma si sviluppa la scuola di via Cavour, contraria alla retorica monumentale del fascismo.")])}
