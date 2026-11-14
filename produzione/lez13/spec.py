# Specifica approfondimenti Lez 13 (Svevo). Contenuti SOLO da videodispensa, libro (slide) e parole del docente.
import json, os
MAT = "Letteratura italiana"; DOC = "Prof. Giorgio Mazzotti"
def S(titolo, voce, cards=None, **k): return dict(titolo=titolo, voce=voce, cards=cards or [], **k)
def C(k, t, d=""): return dict(k=k, t=t, d=d)
def MP(id, parte, dopo, titolo, intro, rami):
    """rami: (concetto, parola, esempio, voce)"""
    return dict(id=id, parte=parte, dopo=dopo, tipo="mappa",
        mappa=dict(materia=MAT, docente=DOC, titolo=titolo, rami=[dict(concetto=c, parola=p, esempio=e) for c, p, e, v in rami]),
        voci=[intro] + [v for c, p, e, v in rami])
def AN(id, parte, dopo, tipo, titolo, schermate): return dict(id=id, parte=parte, dopo=dopo, tipo=tipo, materia=MAT, titolo=titolo, schermate=schermate)
ANS = []
# ---------------- PARTE 1 ----------------
ANS.append(AN("AN1", 1, 1, "linea", "Italo Svevo: la vita in una linea del tempo", [
 S("Trieste e un nome inventato", "Italo Svevo è uno pseudonimo. Il vero nome è Aron Hector Schmitz. Nasce a Trieste, una città di confine, vivace porto commerciale dell'impero austro-ungarico. La famiglia è di origine ebraica e parla anche italiano. Trieste sarà annessa al Regno d'Italia dopo la prima guerra mondiale. Svevo nasce quindi austriaco e muore italiano.",
   [C("Trieste", "Città di confine", "porto dell'impero austro-ungarico"), C("", "Aron Hector Schmitz", "pseudonimo: Italo Svevo")]),
 S("Un letterato che lavora", "Svevo non è un professore, come Carducci e Pascoli. Ha una formazione commerciale. Il padre lo manda a studiare anche in Germania. Lavora come impiegato di banca, un lavoro che lo annoia. Poi entra nella ditta dei suoceri, la famiglia Veneziani, che produce vernici sottomarine per le navi. Alla fine diventa dirigente industriale.",
   [C("", "Studi commerciali", "anche in Germania"), C("", "Banca e industria", "vernici sottomarine dei suoceri")]),
 S("Il silenzio e la ripresa", "Svevo pubblica due romanzi: Una vita nel milleottocentonovantadue e Senilità nel milleottocentonovantotto. Non hanno successo. Con il matrimonio e il lavoro abbandona la letteratura. Passano molti anni di silenzio. Legge Freud. A Trieste incontra James Joyce, che gli insegna l'inglese, lo corregge e lo spinge a scrivere ancora. Nel millenovecentoventitré esce La coscienza di Zeno.",
   [C("1892", "Una vita", "primo romanzo"), C("1898", "Senilità", "secondo romanzo"), C("1923", "La coscienza di Zeno", "dopo il lungo silenzio")])]))
ANS.append(AN("AN2", 1, 1, "scheda", "Le radici del pensiero sveviano", [
 S("Tre maestri", "La visione del mondo di Svevo si appoggia su tre maestri. Da Schopenhauer prende il pessimismo radicale e la teoria delle illusioni umane. Da Nietzsche, la critica ai valori borghesi e l'idea di un soggetto fatto di forze diverse. Da Darwin, lo studio delle leggi naturali e della lotta per la vita. Svevo però usa Darwin in chiave critica. Chi vince spesso si è solo adattato, ed è più svuotato degli altri.",
   [C("", "Schopenhauer", "pessimismo e illusioni umane"), C("", "Nietzsche", "critica ai valori borghesi"), C("", "Darwin", "lotta per la vita, usata in chiave critica")]),
 S("Freud", "C'è poi Freud. Svevo studia la psicoanalisi, ma non crede che sia una terapia efficace. La ammira come strumento di conoscenza e come motore per la creazione letteraria. Guarda a Balzac, a Flaubert e a Zola, ma sposta l'attenzione sulla psicologia del personaggio e sul tempo interiore.",
   [C("", "Freud", "strumento di indagine, non una cura sicura"), C("", "Dal realismo alla psicologia", "il tempo interiore")])]))
ANS.append(MP("AN3", 1, 1, "L'inetto e il pensiero sveviano", "Ecco la mappa concettuale dell'inetto e del pensiero di Svevo. Al centro c'è l'inetto. I rami sono cinque.", [
 ("L'inetto", "inadatto", "società borghese", "Primo ramo. L'inetto è incapace di adattarsi alla società borghese e paralizzato dai propri conflitti interiori."),
 ("L'autore", "Trieste", "Aron Hector Schmitz", "Secondo ramo. Italo Svevo, pseudonimo di Aron Hector Schmitz, vive a Trieste, città di confine."),
 ("Formazione", "commercio", "banca e vernici", "Terzo ramo. Unisce cultura letteraria e formazione commerciale: banca e ditta dei suoceri."),
 ("I maestri", "tre pilastri", "Schopenhauer, Nietzsche, Darwin", "Quarto ramo. Schopenhauer, Nietzsche e Darwin sono i pilastri del suo pensiero."),
 ("Psicoanalisi", "Freud", "conoscenza, non cura", "Quinto ramo. Freud è per Svevo uno strumento di indagine più che una terapia.")]))
ANS.append(AN("AN4", 1, 2, "scheda", "Una vita e Senilità", [
 S("Una vita, 1892", "Il primo romanzo è Una vita. Il protagonista è Alfonso Nitti, un giovane intellettuale che lavora come modesto impiegato di banca. Si scontra con il banchiere Maller, simbolo di forza, una figura paterna. Cerca riscatto nella cultura e nel rapporto con Annetta, la figlia del capo. Ma non riesce ad agire, i suoi sogni di gloria letteraria falliscono e si uccide. Il narratore, in terza persona, interviene per giudicare e smascherare le bugie del protagonista.",
   [C("1892", "Alfonso Nitti", "impiegato di banca, finisce per suicidarsi"), C("", "Maller", "il banchiere, figura forte e paterna")]),
 S("Senilità, 1898", "Il secondo romanzo è Senilità. Emilio Brentani ha solo trentacinque anni, ma vive un'esistenza grigia e senile, fatta di rinunce. Si innamora di Angiolina, una ragazza del popolo, e la trasforma in una creatura angelica. Poi si scontra con la realtà del suo tradimento. Il narratore smonta le maschere che Emilio si costruisce. È l'ironia oggettiva.",
   [C("1898", "Emilio Brentani", "35 anni, vita grigia"), C("", "Angiolina", "idealizzata, poi smascherata"), C("", "Le maschere", "alibi contro la realtà")])]))
ANS.append(MP("AN5", 1, 2, "Una vita e Senilità", "Mappa concettuale dei primi due romanzi. Al centro, l'inettitudine.", [
 ("Una vita", "1892", "Alfonso Nitti", "Primo ramo. Una vita racconta di Alfonso Nitti, impiegato di banca, che finisce suicida."),
 ("Il padre", "Maller", "forza e potere", "Secondo ramo. Il banchiere Maller è la figura forte, contrapposta all'inetto."),
 ("Senilità", "1898", "Emilio Brentani", "Terzo ramo. Senilità racconta Emilio Brentani, trentacinquenne già senile."),
 ("L'illusione", "Angiolina", "idealizzata", "Quarto ramo. L'illusione amorosa è smontata dalla realtà."),
 ("Il narratore", "ironia oggettiva", "smaschera le bugie", "Quinto ramo. Il narratore in terza persona giudica e smaschera i protagonisti.")]))
ANS.append(AN("AN6", 1, 3, "scheda", "La coscienza di Zeno: struttura e narratore", [
 S("Un diario per lo psicoanalista", "La coscienza di Zeno esce nel millenovecentoventitré. È l'autobiografia di Zeno Cosini, scritta su invito del suo psicoanalista, il Dottor S. Il racconto è in prima persona. Autore e personaggio si avvicinano. Il tempo non è lineare, ma misto: segue il flusso della memoria, per gruppi di temi. Il dottore pubblica le memorie per vendetta, perché Zeno ha interrotto la cura. Lo scopriamo nella prefazione.",
   [C("1923", "Autobiografia di Zeno", "scritta per il Dottor S."), C("", "Tempo misto", "segue la memoria, non il calendario")]),
 S("Un narratore inattendibile", "Zeno è un narratore di cui non ci si può fidare. Le sue memorie sono piene di bugie inconsce e di autogiustificazioni. Lo fa per sentirsi innocente. Non sapremo mai quale sia la vera vita di Zeno. I temi chiave sono la nevrosi, il vizio del fumo, con il continuo rinvio dell'ultima sigaretta, e il rapporto di amore e odio con il padre.",
   [C("", "Narratore inattendibile", "bugie inconsce e alibi"), C("", "Temi chiave", "nevrosi, fumo, il padre")])]))
ANS.append(MP("AN7", 1, 3, "La coscienza di Zeno", "Mappa concettuale della coscienza di Zeno. Al centro, Zeno Cosini.", [
 ("La cornice", "Dottor S.", "prefazione", "Primo ramo. Zeno scrive su invito del Dottor S., che pubblica le memorie per vendetta."),
 ("Il tempo", "misto", "per temi", "Secondo ramo. Il tempo è misto e segue il flusso della memoria."),
 ("Il narratore", "inattendibile", "bugie inconsce", "Terzo ramo. Zeno mente a se stesso e al lettore."),
 ("I temi", "nevrosi", "ultima sigaretta", "Quarto ramo. Nevrosi, fumo e rapporto con il padre."),
 ("Il finale", "guarigione?", "profezia", "Quinto ramo. Il romanzo si chiude con una profezia, senza dirci se Zeno sia guarito.")]))
ANS.append(MP("MF1", 1, 99, "Italo Svevo · Parte 1", "Ripassiamo con la mappa concettuale di tutta la prima parte. Al centro c'è Italo Svevo.", [
 ("L'inetto", "inadatto", "società borghese", "Primo ramo. L'inetto non si adatta alla società borghese."),
 ("L'autore", "Trieste", "Aron Hector Schmitz", "Secondo ramo. Un uomo di Trieste, che unisce commercio e letteratura."),
 ("I maestri", "Freud", "Schopenhauer, Nietzsche, Darwin", "Terzo ramo. Tre maestri e la psicoanalisi come strumento di conoscenza."),
 ("I primi romanzi", "inettitudine", "Una vita, Senilità", "Quarto ramo. Una vita e Senilità mostrano due inetti sconfitti dalla realtà."),
 ("Zeno", "narratore", "1923", "Quinto ramo. La coscienza di Zeno è l'autobiografia di un narratore inattendibile.")]))
# ---------------- PARTE 2 ----------------
ANS.append(AN("AN1", 2, 4, "scheda", "Il fumo e la morte del padre", [
 S("L'ultima sigaretta", "Cinque nuclei narrativi dominano La coscienza di Zeno. Il primo è il fumo. Zeno si racconta da una vita che quella sarà l'ultima sigaretta. Ma non lo sarà mai, perché non vuole che lo sia. Si inventa una malattia e le dà la colpa di tutto. In realtà è un alibi. Il fumo è il sintomo dell'inettitudine, e dietro il fumo c'è il padre. Da ragazzo Zeno rubava gli spiccioli dal panciotto del padre.",
   [C("", "Il fumo", "sintomo dell'inettitudine"), C("", "L'alibi", "la malattia come scusa")]),
 S("Lo schiaffo", "Il secondo nucleo è la morte del padre. Il padre di Zeno è un uomo solido e privo di dubbi, che vede il figlio come un irresponsabile. Sul letto di morte, ormai in agonia, lo colpisce con uno schiaffo e spira. Non è un gesto voluto. Ma Zeno lo vive come una condanna e come una punizione. Il senso di colpa, nascosto da una devozione filiale ostentata, tormenta Zeno anche da morto.",
   [C("", "Il padre", "solido, vede il figlio come irresponsabile"), C("", "Lo schiaffo", "involontario, vissuto come condanna")])]))
ANS.append(AN("AN2", 2, 4, "scheda", "Augusta, Guido e la profezia", [
 S("La salute malata", "Il terzo nucleo è il matrimonio. Dopo il rifiuto di Ada e Alberta, Zeno sposa Augusta, la più brutta delle sorelle, ma anche la più solida. Per lui è il perfetto campione della salute borghese. Zeno la guarda con ammirazione e ironia, e la chiama salute malata. Sposandola, spera di guarire dalla propria inettitudine.",
   [C("", "Augusta", "campione di normalità borghese"), C("", "Salute malata", "ammirazione e ironia")]),
 S("Un affare disastroso", "Il quarto nucleo è l'affare con Guido Speyer, il cognato. Guido sembra l'uomo sicuro di sé e destinato al successo. Rovina invece l'azienda con una speculazione in borsa, e finge un suicidio che poi riesce davvero. Zeno, l'inetto, riesce a salvare il patrimonio della famiglia. Ma si sente in colpa del trionfo sul rivale.",
   [C("", "Guido Speyer", "sicuro, ma fallisce"), C("", "Zeno", "si salva, ma ha il senso di colpa")]),
 S("La profezia", "Il quinto nucleo è la profezia finale. Zeno si dichiara guarito, non grazie alla psicoanalisi, ma grazie ai successi commerciali in guerra. Capisce che la vita è inquinata alle radici. Un giorno un uomo inventerà un ordigno fuori dal comune. Ci sarà una catastrofe, la terra tornerà una nebulosa, e con l'uomo sparirà ogni malattia.",
   [C("", "Zeno guarito?", "dopo la guerra e il commercio"), C("", "Apocalisse cosmica", "un ordigno incomparabile")])]))
ANS.append(AN("AN3", 2, 4, "parole", "Parole chiave dei testi di Zeno", [
 S("Alibi, colpa, inettitudine", "Tre parole per leggere i testi. La prima è alibi. Zeno trova scuse per non affrontare la vita: la malattia, il padre, il fumo. La seconda è senso di colpa. Lo tormenta per la morte del padre e per il trionfo su Guido. La terza è inettitudine. Non è solo debolezza individuale. È una nuova idea di uomo, in divenire, mai definitivo.",
   [C("", "Alibi", "una scusa per non vivere"), C("", "Senso di colpa", "il padre, il rivale"), C("", "Inettitudine", "un uomo in divenire")])]))
ANS.append(MP("AN4", 2, 4, "Testi da La coscienza di Zeno", "Mappa concettuale dei cinque testi. Al centro, La coscienza di Zeno. Ricordiamo i cinque nuclei.", [
 ("Il fumo", "ultima sigaretta", "il panciotto", "Primo ramo. Il fumo è il sintomo e l'alibi di Zeno."),
 ("La morte del padre", "schiaffo", "senso di colpa", "Secondo ramo. Lo schiaffo del padre morente alimenta il senso di colpa."),
 ("Augusta", "salute malata", "ironia", "Terzo ramo. Augusta è la normalità borghese, ammirata con ironia."),
 ("L'affare con Guido", "rivalità", "speculazione in borsa", "Quarto ramo. Guido fallisce, e Zeno si salva con il senso di colpa."),
 ("La profezia", "apocalisse", "ordigno", "Quinto ramo. La profezia di una catastrofe cosmica chiude il romanzo.")]))
ANS.append(MP("MF2", 2, 99, "Svevo · tutta la lezione", "Concludiamo con la mappa concettuale di tutta la lezione. Al centro c'è Italo Svevo.", [
 ("La vita", "Trieste", "commercio e letteratura", "Primo ramo. Un uomo di Trieste, tra banca, industria e letteratura."),
 ("L'inetto", "nuova idea di uomo", "alibi", "Secondo ramo. L'inetto, in divenire, non si adatta alla società borghese."),
 ("Il pensiero", "Freud", "Schopenhauer, Nietzsche, Darwin", "Terzo ramo. Tre maestri filosofici e scientifici, più Freud."),
 ("I romanzi", "1892, 1898, 1923", "Una vita, Senilità, Zeno", "Quarto ramo. Tre romanzi, fino al capolavoro del millenovecentoventitré."),
 ("I testi di Zeno", "fumo e padre", "Augusta, Guido", "Quinto ramo. Il fumo, il padre, Augusta, l'affare con Guido."),
 ("La profezia", "apocalisse", "ordigno", "Sesto ramo. Un'apocalisse cosmica chiude il romanzo con una domanda aperta.")]))

ANS.append(AN("AN1b", 1, 1, "scheda", "Che cos'è l'inetto", [
 S("Una nuova idea di uomo", "Al centro del pensiero di Svevo c'è l'inetto. È un uomo incapace di adattarsi alla società borghese, basata sul commercio, sul guadagno, sul successo. È bloccato da una perenne insoddisfazione. Sostituisce l'azione con una complessa autoanalisi. Fa un progetto, poi pensa a tutto quello che potrebbe andare storto, e resta fermo. Per Svevo non è una semplice debolezza individuale.",
   [C("", "Società borghese", "commercio, guadagno, successo"), C("", "Autoanalisi", "pensa invece di agire")]),
 S("Un uomo in divenire", "L'inetto è l'espressione di una nuova idea di uomo. Non è ancora cristallizzato in una forma definitiva. Non ha ancora un ruolo. Per questo è aperto a infinite possibilità di sviluppo. Chi ha successo, invece, spesso è solo adattato alla realtà e più svuotato degli altri. L'inetto sembra sconfitto, ma può essere più autentico.",
   [C("", "In divenire", "non ancora un ruolo definitivo"), C("", "Più autentico", "gli adattati sono più svuotati")])]))
ANS.append(AN("AN1c", 1, 1, "scheda", "Dalla vita di Svevo ai suoi romanzi", [
 S("Lavoro e frustrazione", "La biografia di Svevo torna nei romanzi. La noia e la frustrazione per il lavoro in banca diventano Una vita. Svevo spera che il lavoro nell'azienda dei suoceri migliori la sua condizione mentale, ma non è così. Questa esperienza non gli permette di sentirsi pienamente vivo. Il lavoro, il denaro e la società borghese diventano il suo mondo narrativo.",
   [C("", "La banca", "noia e frustrazione"), C("", "Il matrimonio", "ingresso nella famiglia Veneziani")]),
 S("Il padre e il rapporto con gli altri", "Svevo ebbe un rapporto duro con il padre, che voleva formarlo per il mondo del lavoro. Lui, un po' intellettuale, non riusciva a uniformarsi alle regole e ai ritmi di quel mondo. Questo rapporto irrisolto tornerà in tutti e tre i romanzi. Ritornano anche le difficoltà nelle relazioni sentimentali. Sono elementi autobiografici che nella Coscienza di Zeno vengono esasperati.",
   [C("", "Il padre", "rapporto duro e irrisolto"), C("", "Le relazioni", "difficoltà sentimentali dei protagonisti")])]))
ANS.append(AN("AN4b", 1, 2, "scheda", "Tre temi comuni ai primi due romanzi", [
 S("Padre, lavoro, amore", "Una vita e Senilità raccontano storie diverse, ma i temi sono simili. Il primo è il rapporto non risolto con il padre, o con una figura che lo rappresenta, come il banchiere Maller. Il secondo è il conflitto con il mondo del lavoro. Il terzo è la difficoltà nelle relazioni sentimentali, vissute con illusioni e maschere. In tutti e due i casi il protagonista non riesce a prendere in mano la propria vita.",
   [C("", "Il padre", "rapporto non risolto"), C("", "Il lavoro", "conflitto con il mondo degli impiegati"), C("", "L'amore", "illusioni e maschere")]),
 S("Un'ironia che smaschera", "In tutti e due i romanzi il narratore è in terza persona, ma non si limita a raccontare. Interviene per giudicare, correggere e smascherare le bugie dei protagonisti. Alfonso Nitti e Emilio Brentani si raccontano mille storie per giustificarsi. Il narratore le smonta. Qui nasce il tema della maschera, che ritroveremo in Pirandello. Il successo con il pubblico però non arriva: Svevo scrive in italiano a Trieste, in un impero austro-ungarico, e si rivolge a una nicchia.",
   [C("", "Narratore in terza persona", "giudica e smaschera"), C("", "Maschera", "nasconde il fallimento esistenziale")])]))
ANS.append(AN("AN7b", 1, 3, "scheda", "Zeno, il Dottor S. e la psicoanalisi", [
 S("Il dottore e il paziente", "Nella cornice di La coscienza di Zeno c'è il Dottor S. Non sappiamo se la S voglia alludere a Sigmund Freud. Il dottore compare soltanto nella prefazione. Zeno ne parla con tono scettico e polemico, come probabilmente faceva lo stesso Svevo con la psicoanalisi. Zeno interrompe la terapia. Il dottore pubblica allora le memorie, per vendetta.",
   [C("", "Il Dottor S.", "compare solo nella prefazione"), C("", "La terapia interrotta", "Zeno non si fida fino in fondo")]),
 S("Bugie e ricordi", "Zeno scrive per capire perché soffre di quella che chiama la sua malattia. Ma i ricordi riaffiorano e lui li maschera. Mente a se stesso. Per questo la terapia non funziona. Anche il medico lo dice nella prefazione: il paziente falsifica i ricordi. Il lettore non saprà mai se Zeno è sincero. Il romanzo, con il suo tempo misto e la sua prima persona, è molto vicino alla letteratura psicologica e al flusso di coscienza.",
   [C("", "Ricordi alterati", "li mente e li maschera"), C("", "Lettore ingannato", "non sappiamo mai la verità")])]))
ANS.append(AN("AN1b", 2, 4, "scheda", "Il fumo: gli indizi nel testo", [
 S("La scatola di sigarette", "Il dottore chiede a Zeno di scrivere una storia del suo vizio. Zeno scrive al tavolo, non sul divano. Ricorda le prime sigarette: quelle austro-ungariche, con il marchio dell'aquila. Ricorda un fratello, Giuseppe, un anno più giovane. E sospetta che il padre gli desse più denaro per le sigarette. Zeno non ricorda bene, e noi non possiamo fidarci. Siamo davanti a un sospetto di inferiorità.",
   [C("", "Il dottore", "scrivi la storia del tuo vizio"), C("", "Le prime sigarette", "marchio austro-ungarico")]),
 S("Il panciotto", "Poi arrivano il panciotto e i bottoni. Il padre lascia il panciotto su una sedia, con degli spiccioli nel taschino. Zeno li prende per comprare le sigarette e fuma di nascosto. Il padre lo sorprende e ride. Forse così nasce il vizio: voleva assomigliare al padre, fumare come lui. Dietro al fumo c'è il rapporto con il padre. Con il fumo, Zeno cercava di sentirsi forte.",
   [C("", "Il furto degli spiccioli", "dal panciotto del padre"), C("", "Fumare come il padre", "volersi sentire forte")])]))
ANS.append(AN("AN2b", 2, 4, "scheda", "La morte del padre: tre momenti", [
 S("La madre e il padre", "Zeno perde la madre prima dei quindici anni. Scrive delle poesie per onorarla. Il dolore lo spinge a una vita più seria. Invece la morte del padre è una vera catastrofe. Zeno ha trent'anni, e dice di sentirsi un uomo finito. Perché? Perché il padre era il punto di riferimento. Senza di lui, non c'è più nessuno a cui dimostrare qualcosa.",
   [C("", "La madre", "dolore che spinge alla serietà"), C("", "Il padre", "una vera catastrofe")]),
 S("La sera del tentativo", "Il padre si ammala e viene assistito da un infermiere. Zeno vuole tenerlo a letto, come ordina il medico. Il padre si ribella, si alza e con un ultimo sforzo lascia cadere la mano sulla guancia del figlio. Poi muore. Zeno non può più dimostrare la propria innocenza. Sente che il padre lo ha punito per l'ultima volta. Ma, dice il docente, non era uno schiaffo voluto.",
   [C("", "Il padre malato", "vuole alzarsi dal letto"), C("", "Lo schiaffo", "Zeno lo vive come una punizione")]),
 S("Il padre idealizzato", "Anche dopo la morte, il padre torna nei pensieri di Zeno. Zeno costruisce un'immagine di figlio buono, con una memoria paterna idealizzata. Era cattivo, ma non mi ha capito. È il tentativo di sfuggire a un giudizio terribile e inappellabile. In realtà il padre era preoccupato per il figlio. Voleva che fosse in grado di cavarsela, perché la vita è dura.",
   [C("", "Senso di colpa", "nascosto da una devozione ostentata"), C("", "Un padre preoccupato", "non un nemico")])]))
ANS.append(AN("AN3b", 2, 4, "confronto", "Zeno e Guido: due modi di essere", [
 S("L'uomo sicuro e l'inetto", "Guido Speyer, il marito di Ada, appare come l'uomo che ce la fa. È sicuro di sé, forse più bello. Zeno lo ammira e lo odia insieme: è un rapporto di amore e odio. È il maschio che ce la fa, come il padre. Zeno si sente inferiore, ma invece di lavorare su questo continua ad auto limitarsi e a odiarlo. Con Guido finge un rapporto di amicizia solido.",
   [C("Guido", "Sicuro di sé", "l'uomo che sembra destinato al successo"), C("Zeno", "Inferiore?", "amore e odio per il rivale")]),
 S("Il ribaltamento", "Il ribaltamento arriva con l'affare commerciale. Guido gestisce male l'attività e provoca una catastrofica speculazione in borsa. Zeno si muove con la sua apparente inettitudine, ma salva il patrimonio della famiglia. Guido simula un suicidio e muore davvero. Zeno non è così inetto come dice di essere. E ha pure un senso di colpa: durante il funerale sbaglia corteo. Un celebre errore.",
   [C("Guido", "Fallisce", "la sicurezza era apparente"), C("Zeno", "Si salva", "ma si sente in colpa")])]))
ANS.append(AN("AN4b", 2, 4, "scheda", "La profezia finale, lettura guidata", [
 S("La vita come malattia", "Siamo nell'ultimo capitolo. Zeno scrive che la vita somiglia un poco alla malattia: procede per crisi e lisi, con giornalieri miglioramenti e peggioramenti. A differenza delle altre malattie, la vita è sempre mortale. La vita attuale, dice, è inquinata alle radici. L'uomo ha messo gli ordigni al posto degli alberi e delle bestie.",
   [C("", "La vita", "somiglia a una malattia, sempre mortale"), C("", "Un mondo inquinato", "alle radici")]),
 S("Gli ordigni", "Gli animali, spiega Zeno, si adattano cambiando il proprio corpo. La rondinella sviluppa i muscoli delle ali. La talpa si scava. L'uomo invece inventa ordigni fuori dal suo corpo. All'inizio erano prolungamenti del braccio, come la lancia. Ora l'ordigno non ha più relazione con il corpo. Così l'uomo diventa sempre più furbo e sempre più debole.",
   [C("", "Gli animali", "cambiano il proprio corpo"), C("", "L'uomo", "inventa ordigni fuori dal corpo")]),
 S("Una domanda aperta", "La profezia continua. Un uomo, anche lui malato, inventerà un esplosivo incomparabile. Un altro lo userà. Ci sarà un'esplosione enorme che nessuno udrà, e la terra tornerà una nebulosa, libera da parassiti e malattie. Zeno è meno malato di chi guida il mondo. Il romanzo si chiude con questa domanda: Zeno è guarito? Il lettore resta con l'amaro in bocca.",
   [C("", "L'esplosione", "la terra torna una nebulosa"), C("", "Guarito?", "la domanda resta aperta")])]))

def voce_testo(a):
    return " ".join(a["voci"]) if a["tipo"] == "mappa" else " ".join(s["voce"] for s in a["schermate"])
if __name__ == "__main__":
    for p, a0 in ((1, 43.15), (2, 45.68)):
        w = sum(len(voce_testo(a).split()) for a in ANS if a["parte"] == p)
        m = w / 2.24 / 60
        print("Parte", p, "parole", w, "+min", round(m, 1), "totale atteso", round(a0 + m, 1))
