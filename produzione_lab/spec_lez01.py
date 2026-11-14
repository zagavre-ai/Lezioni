# -*- coding: utf-8 -*-
# Lezione 1 · Modellistica · Prof.ssa Piera Caputi. Contenuti SOLO dal materiale del docente (PDF + video).
TAG='moda-laboratori-III-IV-lez01'
MATERIA='Laboratori tecnologici · Tecnico Sistema Moda'
DOCENTE='Prof.ssa Piera Caputi'
TITOLO='Modellistica'
FILE='Modellistica_Lez1'   # nome base file consegna
SRC='Lezione.1.-.Modellistica.mp4'
CAM=(810,437,34)           # cerchio del docente nel video originale: centro x,y, raggio
# t0 = inizio argomento nel video del docente (s); agganciato poi alla pausa più vicina
ARGS=[
dict(n=1,t0=0,titolo='Il modellista e le sue competenze',
 slides=[
  dict(t='Il ruolo del modellista',c=['Interpreta gli schizzi dello stilista','Li traduce nel modello: l\'insieme dei pezzi del capo','Unisce il reparto creativo e quello produttivo']),
  dict(t='Che cosa deve sapere',c=['Sensibilità per forme e colori','Misure anatomiche, merceologia tessile, assemblaggio','Matematica e geometria per i tracciati']),
  dict(t='Il modellista oggi',c=['Tracciati base, trasformazioni, sviluppo taglie, piazzamenti','Basi sartoriali e sistemi CAD','Una figura integrata: assorbe compiti di più esperti']),
  dict(t='Le capacità del profilo',c=['Leggere linee e volumi del figurino','Rilevare misure e usare le tabelle industriali','Tracciato, sviluppo taglie, piazzamento, scheda tecnica']),
  dict(t='Industriale e sartoriale',c=['Industriale: soggetti standard, sviluppo taglie, piazzamenti','Sartoriale: il singolo cliente, capi su misura','Per entrambi: leggere il figurino e misurare con precisione']),
 ],
 an=dict(t='Il modellista in tre mosse',items=[('1','Legge il figurino','L\'idea dello stilista diventa un progetto da costruire.'),('2','Costruisce il modello','I pezzi del capo, con le misure e il tracciato.'),('3','Collega i reparti','Fa dialogare creatività e produzione.')]),
 mappa=dict(titolo='Il modellista',rami=[('Ruolo','interpretare','dal figurino al modello'),('Competenze','geometria','misure e tessuti'),('Oggi','CAD','figura integrata'),('Contesto','industriale','o sartoriale')]),
 ripasso='Il modellista interpreta gli schizzi dello stilista e li traduce nel modello, unendo creatività e produzione. Oggi lavora con basi sartoriali e con il CAD, in contesto industriale o sartoriale.',
 quiz=[
  ('Qual è il compito fondamentale del modellista?','Interpretare gli schizzi dello stilista e tradurli nel modello',['Disegnare soltanto figurini di tendenza','Gestire le spedizioni dei capi finiti','Produrre le fibre tessili'],'Il modellista traduce gli schizzi in un modello: l\'insieme dei pezzi che comporranno il capo.'),
  ('Che cos\'è il modello?','L\'insieme di tutti i pezzi che comporranno il capo finale',['Un disegno artistico di moda','Il manichino su cui si prova il capo','Un campione di tessuto'],'Il modello è l\'insieme dei pezzi del capo finale.'),
  ('Quali basi servono al modellista per progettare i tracciati?','Matematica e geometria',['Solo conoscenze di marketing','Solo abilità di disegno artistico','Nozioni di logistica'],'Per progettare tracciati adeguati servono solide basi di matematica e geometria.'),
  ('Che cosa distingue il modellista sartoriale da quello industriale?','Lavora sul singolo cliente correggendo il modello sulla sua conformazione',['Lavora solo al computer','Non legge mai il figurino','Si occupa solo di piazzamenti'],'Il sartoriale opera sul singolo cliente; l\'industriale lavora su soggetti standard.'),
  ('A quale sistema informatico si lega oggi la figura del modellista?','Ai sistemi CAD',['Ai programmi di contabilità','Ai sistemi di posta elettronica','Ai software di montaggio video'],'L\'evoluzione tecnologica ha legato il modellista ai sistemi CAD.')]),
dict(n=2,t0=345,titolo='Il figurino',
 slides=[
  dict(t='Che cos\'è il figurino',c=['L\'espressione grafica di un\'idea','È la base per costruire ogni modello','Lo disegna lo stilista, un aiutante o il modellista']),
  dict(t='Le tre tipologie',c=['Figurino di tendenza o sketch','Figurino tecnico o plat','Figurino intermedio o ibrido']),
  dict(t='Il figurino di tendenza',c=['Evoca atmosfere e temi stagionali','Dettagli costruttivi in secondo piano','Proporzioni alterate; spesso con campioni di tessuto']),
  dict(t='Il figurino tecnico o plat',c=['Il capo in piano, con precisione tecnica','Maglieria: linee rigide e forme stilizzate','Tessuti a navetta: linee più morbide, con il volume del corpo']),
  dict(t='Il figurino ibrido',c=['Senza colore, usato dai professionisti interni','Bilancia gusto estetico e produzione','Si ritrova su etichette, cartellini e imballaggi']),
  dict(t='Dall\'ispirazione al figurino',c=['Ritagli di giornale e contenuti web','Colletti, lunghezze, stampe da armonizzare','Un\'immagine globale: figure geometriche, lettere, stili storici']),
 ],
 an=dict(t='Tre figurini a confronto',items=[('Tendenza','Emozione','Evoca atmosfere e temi stagionali.'),('Tecnico','Precisione','Il capo in piano, con linee precise.'),('Ibrido','Equilibrio','Unisce estetica ed esigenze produttive.')]),
 mappa=dict(titolo='Il figurino',rami=[('Tendenza','sketch','atmosfere stagionali'),('Tecnico','plat','capo in piano'),('Ibrido','senza colore','etichette e cartellini'),('Ispirazione','giornali e web','immagine globale')]),
 ripasso='Il figurino è l\'espressione grafica di un\'idea. Può essere di tendenza, tecnico o ibrido, e da lui parte la costruzione del modello.',
 quiz=[
  ('Che cosa rappresenta il figurino?','L\'espressione grafica di un\'idea, base di ogni modello',['Il tessuto scelto per la collezione','La taglia base dell\'azienda','Il listino prezzi del capo'],'Il figurino è la base di partenza per la costruzione di ogni modello.'),
  ('Quali sono le tre tipologie di figurino?','Di tendenza, tecnico e intermedio o ibrido',['Solo maschile, femminile e infantile','Di seta, di lana e di cotone','Primaverile, estivo e invernale'],'Le tipologie sono: figurino di tendenza, tecnico o plat, intermedio o ibrido.'),
  ('Che cosa caratterizza il figurino tecnico o plat?','Una rappresentazione del capo in piano con precisione tecnica',['Uno schizzo che comunica emozioni','Proporzioni anatomiche alterate','Campioni di tessuto e pizzi applicati'],'Il plat mostra il capo in piano, con linee precise.'),
  ('Come sono le linee del plat per la maglieria?','Rigide, con forme geometriche molto stilizzate',['Morbide, con il volume del corpo','Sempre colorate','Tracciate solo a mano libera'],'Per la maglieria le linee sono rigide; per i tessuti a navetta sono più morbide.'),
  ('Dove si ritrova spesso il figurino ibrido?','Su etichette, cartellini e imballaggi',['Solo nelle riviste di moda','Solo nei cataloghi dei tessuti','Solo nei registri di magazzino'],'Il figurino ibrido dà al consumatore indicazioni sui volumi e sulla linea del capo.')]),
dict(n=3,t0=650,titolo='Gli strumenti del modellista',
 slides=[
  dict(t='Misurare e verificare',c=['Metro a nastro flessibile da 150 cm','Metro rigido per l\'altezza; bilancia per la massa','Manichino: prova la caduta dei tessuti']),
  dict(t='Disegno tecnico e basi',c=['Mine e portamine ad alta precisione','Righe, squadre e curvilinei','Carta da modello e cartoncino']),
  dict(t='Utensili di marcatura',c=['Forbici per cartone e spilli','Segnatacche e punteruolo','Trapanino per tasche e pinces']),
  dict(t='Gli strumenti digitali',c=['Computer con software CAD','Mouse, penne ottiche, plotter in scala reale','Sistemi CAM per le macchine di taglio']),
  dict(t='Digitale e manualità',c=['Il CAD velocizza piazzamenti e precisione','La manualità resta centrale, come nel moulage','Il piazzamento riduce il consumo di materia prima']),
 ],
 an=dict(t='Dal manuale al digitale',items=[('Misurare','Metro e manichino','Il rilievo delle misure e la prova del capo.'),('Tracciare','Matite, righe, curvilinei','Il disegno tecnico su carta e cartoncino.'),('Digitalizzare','CAD, plotter, CAM','Tracciati e piazzamenti al computer.')]),
 mappa=dict(titolo='Gli strumenti',rami=[('Misura','metro','nastro, rigido, bilancia'),('Disegno','mine e squadre','curvilinei'),('Marcatura','segnatacche','spilli, punteruolo'),('Digitale','CAD e CAM','plotter')]),
 ripasso='Gli strumenti del modellista servono a misurare, disegnare, marcare e digitalizzare. Il CAD velocizza il lavoro, ma la manualità resta centrale.',
 quiz=[
  ('Quale strumento serve per rilevare le circonferenze?','Il metro a nastro flessibile da 150 cm',['Il metro rigido','La bilancia','Il plotter'],'Il metro a nastro flessibile si usa per le circonferenze; quello rigido per l\'altezza.'),
  ('A che cosa serve il segnatacche?','Ad asportare piccoli lembi di cartoncino nei punti di giuntura',['A stampare i modelli in scala reale','A pesare il tessuto','A tagliare il tessuto in serie'],'Il segnatacche segna i punti di giuntura delle cuciture.'),
  ('Che cosa si usa per stampare i modelli in scala reale?','Il plotter',['Il punteruolo','Il trapanino','Il curvilineo'],'Il plotter stampa in scala reale i tracciati digitali.'),
  ('A che cosa servono i sistemi CAM?','A interfacciarsi direttamente con i macchinari di taglio industriale',['A misurare l\'altezza del soggetto','A disegnare i figurini di tendenza','A cucire i capi'],'I sistemi CAM collegano il lavoro ai macchinari di taglio industriale.'),
  ('Che cosa permette il piazzamento al CAD?','Di ridurre il consumo di materia prima',['Di eliminare i modelli','Di scegliere i colori della collezione','Di sostituire il manichino'],'Visualizzare le sagome insieme riduce drasticamente lo spreco di tessuto.')]),
dict(n=4,t0=905,titolo='Come si costruisce un modello',
 slides=[
  dict(t='I tre sistemi',c=['Tracciato geometrico','Trasformazione di un modello base','Tecnica del moulage']),
  dict(t='Il tracciato geometrico',c=['Parte dall\'analisi del figurino','Si aggiungono misure anatomiche e vestibilità','Diretto: sartoria · Proporzionale: industria']),
  dict(t='Il modello base',c=['Tracciati standard già testati','Si variano lunghezze, tagli e linee','Adatta il prodotto alle tendenze in modo rapido']),
  dict(t='Il moulage',c=['Il tessuto si modella sul manichino','Spilli e tacche di riferimento','Poi i pezzi passano su carta o su tessuto']),
  dict(t='Il CAD',c=['Tutto il ciclo al computer','Modifiche con pochi clic; cuciture e asole','Sviluppo taglie e piazzamenti veloci']),
 ],
 an=dict(t='Tre strade per il modello',items=[('Geometrico','Dalle misure al tracciato','Diretto in sartoria, proporzionale in industria.'),('Modello base','Si trasforma','Tracciati standard adattati alle tendenze.'),('Moulage','Sul manichino','Il tessuto prende forma senza calcoli preventivi.')]),
 mappa=dict(titolo='Costruire un modello',rami=[('Geometrico','misure','diretto o proporzionale'),('Modello base','trasformazione','standard testati'),('Moulage','manichino','tessuto e spilli'),('CAD','computer','ciclo digitale')]),
 ripasso='Il modello si costruisce con il tracciato geometrico, con la trasformazione di un modello base o con il moulage. Il CAD porta tutto al computer.',
 quiz=[
  ('Quali sono i tre sistemi per realizzare un modello?','Tracciato geometrico, modello base e moulage',['Cucito, stiro e taglio','Disegno, pittura e collage','Filatura, tessitura e tintura'],'I sistemi fondamentali sono tracciato geometrico, trasformazione di un modello base e moulage.'),
  ('Quale metodo si usa soprattutto in sartoria nel tracciato geometrico?','Il metodo diretto',['Il metodo proporzionale','Il metodo industriale','Il metodo CAD'],'Il metodo diretto riporta fedelmente le misure di una persona specifica.'),
  ('Su che cosa si basa il metodo proporzionale?','Su rapporti armonici del corpo umano',['Sulle misure di un solo cliente','Sul peso del tessuto','Sul prezzo del capo'],'È fondamentale per l\'industria e punta a una buona vestibilità per un pubblico ampio.'),
  ('Quale metodologia genera il modello modellando il tessuto sul manichino?','Il moulage',['Il metodo proporzionale','Il modello base','Il piazzamento'],'Con il moulage il modello nasce direttamente sul manichino, senza calcoli preventivi.'),
  ('Che cosa permette il CAD nella costruzione del modello?','Eseguire l\'intero ciclo di lavoro al computer',['Eliminare le misure anatomiche','Sostituire il docente','Produrre le fibre'],'Con il CAD non servono modelli fisici in carta o cartoncino.')]),
dict(n=5,t0=1290,titolo='Proporzioni e misure del corpo',
 slides=[
  dict(t='La proporzione aurea',c=['Rapporto altezza totale e distanza ombelico-terra','Policleto, V secolo a.C.: il corpo in 8 parti uguali','Vitruvio e Leonardo: l\'Uomo vitruviano']),
  dict(t='Le unità antropometriche',c=['8 parti uguali: unità antropometriche (U.A.)','Dalla testa alla vita: 3 parti','Dalla vita ai piedi: 5 parti']),
  dict(t='Come si rileva la misura',c=['Altezza: metro rigido, soggetto scalzo a piedi uniti','Altre misure: metro a nastro, soggetto eretto','Poco vestito, per non falsare i valori']),
  dict(t='Le tipologie di misure',c=['Larghezza: torace, seno, vita, bacino','Lunghezza o livelli: ascella, vita, bacino, ginocchio','Arti e misure accessorie o di controllo']),
 ],
 an=dict(t='Il corpo in 8 parti',items=[('8','Parti uguali','Il canone di Policleto: unità antropometriche.'),('3','Parti sopra','Dalla sommità del capo alla linea della vita.'),('5','Parti sotto','Dalla vita ai piedi.')]),
 mappa=dict(titolo='Le misure del corpo',rami=[('Proporzione','Policleto','8 unità'),('Rilievo','metro','soggetto scalzo'),('Larghezze','circonferenze','torace e vita'),('Lunghezze','livelli','ascella, vita, bacino')]),
 ripasso='Il canone di Policleto divide il corpo in otto parti uguali. Le misure si rilevano con il metro e si distinguono in larghezze, lunghezze, arti e misure accessorie.',
 quiz=[
  ('Secondo il canone di Policleto, in quante parti uguali si divide il corpo ideale?','In 8 parti, dette unità antropometriche',['In 10 parti','In 6 parti','In 12 parti'],'Il canone risale al V secolo a.C.: 3 parti dal capo alla vita e 5 dalla vita ai piedi.'),
  ('Con che cosa si rileva l\'altezza?','Con un metro rigido, con il soggetto scalzo e a piedi uniti',['Con un metro a nastro, in poltrona','Con una bilancia','Con un plotter'],'Le altre misure si rilevano con il metro a nastro flessibile.'),
  ('Quali sono misure di larghezza?','Le circonferenze di torace, seno, vita e bacino',['Il livello ascella e il livello ginocchio','La lunghezza del braccio','La massa corporea'],'Le misure di larghezza sono circonferenze.'),
  ('Che cosa indicano i livelli?','Le distanze verticali dal girocollo verso il basso',['Le circonferenze del busto','Il peso del soggetto','La taglia del capo'],'Esempi di livelli: ascella, vita, bacino, inforcatura, ginocchio e caviglia.'),
  ('Perché il soggetto deve essere poco vestito durante la misurazione?','Per evitare che lo spessore degli indumenti falsi i valori',['Per stirare meglio il capo','Per scegliere il colore','Per ridurre il tempo di taglio'],'Gli indumenti spessi alterano le misure rilevate.')]),
dict(n=6,t0=1576,titolo='Le taglie e il normotipo',
 slides=[
  dict(t='Le tabelle di misure',c=['Nell\'industria non si misura ogni cliente','Si usano tabelle standardizzate','Basate sulle dimensioni più comuni della clientela']),
  dict(t='Il grado di vestibilità',c=['Spazio aggiunto o sottratto alle misure del corpo','Si indica in gradi (v.v.): 1 grado = 1 cm','Dipende dal disegno e dal tipo di tessuto']),
  dict(t='La taglia in Italia',c=['La taglia è la semicirconferenza del torace, in centimetri','Torace 84 cm: taglia 42','Ogni taglia: +2 cm sulla semicirconferenza']),
  dict(t='La taglia 42 come base',c=['Semicirconferenza seno: taglia + 3 cm','Vita: taglia − 8 cm · Bacino: taglia + 5 cm','La differenza di 8 cm è il drop 8']),
  dict(t='Il normotipo',c=['Taglia 42: statura media di 168 cm','Larghezze: ampio accordo; altezze: opinioni diverse','Le unità antropometriche calcolano le misure mancanti']),
 ],
 an=dict(t='Le misure della taglia 42',items=[('84','Torace','La semicirconferenza indica la taglia 42.'),('−8','Vita','La differenza di 8 cm si chiama drop 8.'),('+5','Bacino','Semicirconferenza del bacino: taglia più 5 centimetri.')]),
 mappa=dict(titolo='Taglie e normotipo',rami=[('Taglia','semicirconferenza','torace 84 cm = 42'),('Passo','2 cm','tra una taglia e l\'altra'),('Drop 8','vita','taglia meno 8'),('Normotipo','168 cm','taglia 42'),('Vestibilità','gradi v.v.','1 grado = 1 cm')]),
 ripasso='In Italia la taglia è la semicirconferenza del torace: 84 centimetri sono la taglia 42. La vita è taglia meno 8, il drop 8, e il normotipo è alto 168 centimetri.',
 quiz=[
  ('In Italia a quale misura corrisponde la taglia?','Alla semicirconferenza del torace, in centimetri',['All\'altezza totale','Al peso corporeo','Alla lunghezza della gamba'],'Una circonferenza di 84 cm identifica la taglia 42.'),
  ('Che cos\'è il drop 8?','La differenza di 8 cm tra semicirconferenza del torace e della vita',['Un tipo di armatura del tessuto','La riduzione dei tessuti in lana','L\'altezza della cimosa'],'La semicirconferenza della vita è pari alla taglia meno 8 cm.'),
  ('Di quanto varia la semicirconferenza tra una taglia e la successiva?','Di 2 centimetri',['Di 8 centimetri','Di 5 centimetri','Di 10 centimetri'],'Ogni taglia superiore o inferiore varia in modo progressivo di 2 cm.'),
  ('Quale statura media ha il normotipo femminile della taglia 42?','168 cm',['150 cm','180 cm','190 cm'],'Per la taglia 42 italiana il normotipo ha statura media di 168 cm.'),
  ('Che cos\'è la vestibilità nel tracciato del modello?','Lo spazio aggiuntivo, in gradi, sommato o sottratto alle misure del corpo',['Il colore del tessuto','Il prezzo della taglia','La lunghezza del rotolo'],'Un grado di vestibilità (v.v.) corrisponde a 1 centimetro.')]),
dict(n=7,t0=2126,titolo='La norma EN 13402 e il rilievo delle misure',
 slides=[
  dict(t='Perché serve una norma',c=['Sistemi di misura diversi creano confusione','Con lo shopping on-line i resi arrivano vicini al 30%','L\'Unione Europea promuove la norma EN 13402']),
  dict(t='I requisiti della norma',c=['Misure anatomiche reali, in centimetri: via i pollici','Larghezze come circonferenze intere','Dati sotto forma di intervalli (range)']),
  dict(t='Primarie, secondarie e pittogrammi',c=['Primarie: mai omesse in etichetta','Secondarie: informazioni utili, facoltative','Pittogrammi: figura stilizzata con le misure']),
  dict(t='Come si rilevano le circonferenze',c=['Testa: sezione massima sopra le orecchie','Collo: 2 cm sotto il pomo d\'Adamo','Torace, seno, vita, anca: respiro normale, posizione eretta']),
  dict(t='Lunghezze e massa',c=['Altezza: dalla testa alla pianta dei piedi','Gamba interna: dal cavallo ai piedi · braccio: scapola-polso','Piede, mano e massa corporea in chilogrammi']),
  dict(t='La misura primaria per prodotto',c=['Camicia: collo (uomo) o seno (donna) · calzini: piede','Cappello: testa · giacche e felpe: torace o seno','Pantaloni e gonne: vita o anca']),
  dict(t='Vestibilità e tessuto',c=['Molto elastico: −2 v.v. · jersey: −1 v.v.','Peso medio non elastico: +1 v.v.','Lana pesante: +2 v.v.']),
 ],
 an=dict(t='L\'etichetta secondo la norma',items=[('cm','Solo centimetri','Via i pollici: le misure sono espresse in centimetri.'),('1','Primarie','I dati essenziali, mai omessi in etichetta.'),('2','Secondarie','Informazioni utili, indicate a discrezione del produttore.')]),
 mappa=dict(titolo='La norma EN 13402',rami=[('Scopo','meno resi','uniformità'),('Unità','centimetri','niente pollici'),('Larghezze','circonferenze','intere'),('Dati','intervalli','range di misure'),('Misure','primarie','secondarie facoltative'),('Pittogrammi','figura umana','misure indicate')]),
 ripasso='La norma EN 13402 uniforma le misure: centimetri, circonferenze intere e intervalli. Le misure primarie sono obbligatorie in etichetta, le secondarie facoltative.',
 quiz=[
  ('Come devono essere indicate le misure secondo la norma EN 13402?','Esclusivamente in centimetri, abolendo i pollici',['In pollici','In millimetri','Con codici come S, M, L e XL'],'La norma stabilisce l\'uso dei centimetri e l\'abolizione dei pollici.'),
  ('Come devono essere indicate le larghezze?','Come circonferenze intere, non semicirconferenze',['Come semicirconferenze','Solo come altezze','Come pesi'],'Le larghezze si indicano come circonferenze intere.'),
  ('Che cosa sono le misure primarie?','I dati essenziali che non possono mai essere omessi in etichetta',['Informazioni facoltative','Le misure del manichino','Le misure del tessuto'],'Le secondarie sono utili, ma l\'indicazione resta facoltativa.'),
  ('Qual è la misura primaria di un cappello?','La circonferenza della testa',['La lunghezza del piede','La circonferenza del bacino','La lunghezza del braccio'],'Per i calzini è la lunghezza del piede; per pantaloni e gonne vita o anca.'),
  ('Quale correzione di vestibilità si applica ai tessuti molto elasticizzati?','Una riduzione di 2 gradi (−2 v.v.)',['Un aumento di 2 gradi','Nessuna correzione','Un aumento di 1 grado'],'La lana pesante richiede invece un aumento di 2 gradi.')]),
dict(n=8,t0=2709,titolo='Le fibre tessili',
 slides=[
  dict(t='Che cos\'è una fibra',c=['L\'unità elementare della materia prima','Flessibile, fine, molto più lunga che larga','Filata, diventa filato e poi tessuto']),
  dict(t='Come si classificano',c=['Naturali: dal mondo vegetale o animale','Chimiche o man-made: prodotte dall\'uomo','In mischia: materiali diversi mescolati in filatura']),
  dict(t='Le fibre naturali',c=['Animali: proteine, come lana e seta','Vegetali: cellulosa, come cotone e lino','Lana: morbida ed elastica · seta: non aderisce al corpo']),
  dict(t='Le fibre chimiche',c=['Artificiali: da polimeri naturali, come viscosa e modal','Sintetiche: da sintesi chimica, come poliestere e acrilico','Elastan: la fibra del movimento, allungamento 400-600%']),
  dict(t='Fibre e vestibilità',c=['Con l\'elastan si può usare vestibilità zero','Le chimiche sono più flessibili e drappeggiabili','Le nobilitazioni possono limitare l\'elasticità']),
 ],
 an=dict(t='La famiglia delle fibre',items=[('Naturali','Animali e vegetali','Lana e seta · cotone e lino.'),('Artificiali','Da polimeri naturali','Viscosa e modal, dalla cellulosa.'),('Sintetiche','Da sintesi chimica','Poliestere, acrilico ed elastan.')]),
 mappa=dict(titolo='Le fibre tessili',rami=[('Naturali','animali o vegetali','lana, seta, cotone, lino'),('Artificiali','polimeri naturali','viscosa, modal'),('Sintetiche','sintesi chimica','poliestere, elastan'),('In mischia','filatura','proprietà combinate'),('Vestibilità','elastan','v.v. zero')]),
 ripasso='Le fibre si dividono in naturali, animali o vegetali, e chimiche, artificiali o sintetiche. L\'elastan migliora la vestibilità e permette la vestibilità zero.',
 quiz=[
  ('Come si dividono le fibre naturali?','In animali, come lana e seta, e vegetali, come cotone e lino',['In artificiali e sintetiche','In filati e tessuti','In cimose e ordito'],'Le fibre animali sono proteine, quelle vegetali cellulosa.'),
  ('Che cosa sono le fibre in mischia?','Materiali di natura diversa mescolati durante la filatura',['Fibre di un solo materiale','Fibre prodotte solo in laboratorio','Fibre senza filatura'],'La mischia combina e ottimizza le proprietà di ciascun materiale.'),
  ('Quali sono esempi di fibre artificiali?','Modal e viscosa',['Poliestere e acrilico','Lana e seta','Cotone e lino'],'Le artificiali derivano da polimeri naturali preesistenti, come la cellulosa.'),
  ('Quale fibra è definita «fibra del movimento»?','L\'elastan, che si allunga dal 400% al 600%',['Il lino','La seta','Il cotone'],'Anche in piccole percentuali migliora sensibilmente la vestibilità.'),
  ('Che cosa permette un tessuto con elastan nel tracciato?','Una vestibilità zero',['Un aumento di 2 gradi','Di non usare le misure','Di eliminare il piazzamento'],'L\'elasticità consente al capo di adattarsi senza aggiungere agio.')]),
dict(n=9,t0=3143,titolo='I tessuti e le loro caratteristiche',
 slides=[
  dict(t='Le quattro famiglie',c=['Tessuti a navetta (ortogonali)','Tessuti a maglia e a rete','Tessuti non tessuti: feltro e TNT']),
  dict(t='Il tessuto a navetta',c=['Ordito: fili verticali, la lunghezza','Trama: fili perpendicolari, la larghezza','Armature: tela, saia, raso']),
  dict(t='Maglia, rete e non tessuti',c=['Maglia: elasticità e comfort','Rete: celle vuote, come il tulle','Non tessuti: né filatura né tessitura']),
  dict(t='Le cimose e l\'altezza utile',c=['Cimose: bordi laterali contro lo sfilacciamento','Basse < 7 mm · medie 7-14 mm · alte > 14 mm','Altezza utile: la misura tra le due cimose']),
  dict(t='Diritto, rovescio e verso',c=['Diritto: più lucido, liscio e curato','Rovescio: meno rifiniture, colore più tenue','Verso: indifferente, obbligato o semi obbligato']),
  dict(t='Diritto filo, sbieco, nobilitazioni',c=['Diritto filo: parallelo all\'ordito','Sbieco: 45 gradi rispetto a trama e ordito','Nobilitazioni: possono limitare l\'elasticità']),
  dict(t='La vestibilità è moda',c=['Aderente, semilenta o lenta','Dipende da fibre, intreccio, spessore e peso','1 grado = 1 cm da aggiungere o togliere']),
 ],
 an=dict(t='Ordito e trama',items=[('Ordito','Fili verticali','Definiscono la lunghezza del tessuto.'),('Trama','Fili perpendicolari','Formano la larghezza.'),('Armature','Tela, saia, raso','Dall\'intreccio nascono le armature fondamentali.')]),
 mappa=dict(titolo='I tessuti',rami=[('Navetta','ordito e trama','tela, saia, raso'),('Maglia','elasticità','comfort'),('Rete','celle vuote','tulle'),('Cimose','bordi','basse, medie, alte'),('Verso','diritto e rovescio','indifferente o obbligato'),('Vestibilità','nobilitazioni','gradi v.v.')]),
 ripasso='I tessuti si dividono in navetta, maglia, rete e non tessuti. Il modellista guarda cimose, diritto e rovescio, verso e diritto filo per un buon piazzamento.',
 quiz=[
  ('Che cosa sono le cimose?','I bordi laterali del tessuto che lo proteggono dagli sfilacciamenti',['I fili verticali del tessuto','Le celle vuote del tulle','Le armature diagonali'],'Si classificano in basse, medie e alte secondo l\'altezza.'),
  ('Quali sono le armature fondamentali dei tessuti a navetta?','Tela, saia e raso',['Maglia, rete e feltro','Ordito, trama e verso','Diritto, rovescio e sbieco'],'La tela è semplice e compatta, la saia diagonale, il raso lucido e liscio.'),
  ('Come viene definito il diritto filo?','Il segmento parallelo alla lunghezza del tessuto, cioè all\'ordito',['Una linea a 45 gradi','Il lato meno rifinito','La tacca sul cartamodello'],'Lo sbieco è invece la linea a 45 gradi rispetto a trama e ordito.'),
  ('Come appare di solito il diritto del tessuto?','Più lucido, liscio e curato',['Con colore più tenue','Con più difetti','Sempre uguale al rovescio'],'Il rovescio presenta meno rifiniture e colore più tenue.'),
  ('Che cosa è il tulle?','Un esempio di tessuto a rete, con celle vuote',['Un tessuto non tessuto','Una fibra animale','Un tipo di cimosa'],'I tessuti a rete si caratterizzano per le celle vuote.')]),
]
GLOSSARIO=[('Modello','l\'insieme dei pezzi che compongono il capo finale'),('Figurino','l\'espressione grafica di un\'idea, base di ogni modello'),('Plat','il figurino tecnico, il capo in piano'),('Moulage','la tecnica che modella il tessuto sul manichino'),('Taglia','in Italia, la semicirconferenza del torace in centimetri'),('Drop 8','la differenza di 8 centimetri tra torace e vita'),('Vestibilità','lo spazio aggiunto o sottratto alle misure, in gradi'),('Cimosa','il bordo laterale del tessuto'),('Diritto filo','la direzione parallela ai fili di ordito'),('Sbieco','la linea a 45 gradi rispetto a trama e ordito')]
MAPPA_FINALE=dict(titolo='Modellistica',rami=[('Il modellista','ruolo','figura integrata'),('Il figurino','tre tipologie','dal disegno al modello'),('Il modello','geometrico, base, moulage','strumenti e CAD'),('Taglie','semicirconferenza','norma EN 13402'),('Fibre','naturali e chimiche','elastan'),('Tessuti','navetta, maglia, rete','cimose e verso')])
INTRO='Benvenuti alla lezione di Laboratori tecnologici, con la professoressa Piera Caputi. Oggi parliamo di modellistica: il ruolo del modellista, il figurino, gli strumenti, le misure, le fibre e i tessuti.'
FIN='Fine della lezione. Grazie per l\'attenzione, e buono studio.'
COMPITI='Ora passa ai compiti.'
