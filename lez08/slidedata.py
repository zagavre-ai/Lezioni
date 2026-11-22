# testi delle slide del prof (dal PDF), refusi corretti. Una card = una frase intera.
import subprocess,re
SL={ # pagina PDF -> (titolo, [card])
2:("L'Impero tedesco all'inizio del Novecento",[
 "Una potenza globale: nei primi quindici anni del Novecento, l'Impero tedesco domina l'Europa centro-settentrionale dal punto di vista economico e culturale.",
 "Crescita e industrializzazione: grazie alle riforme di Bismarck attive fino al 1890, la produzione d'acciaio supera quella britannica e la popolazione tocca i 67 milioni di abitanti.",
 "I centri dell'avanguardia: Prussia, Baviera e Sassonia ospitano le città più grandi e intellettualmente attive, con Berlino come polo d'attrazione per filosofi, artisti e architetti."]),
3:("Le contraddizioni della metropoli moderna",[
 "Nuovi spazi sociali: la crescita industriale moltiplica i luoghi di aggregazione di massa come cinema, teatri, spazi espositivi e riviste editoriali.",
 "Disagio e alienazione: parallelamente alle energie positive, nel cuore dei grandi centri urbani esplodono conflitti sociali e profonde angosce individuali.",
 "La voce dell'Espressionismo: gli artisti innovatori, in particolare gli espressionisti, si fanno interpreti e specchio di queste tensioni della modernità."]),
4:("Psicologia dello spazio urbano e agorafobia",[
 "Nuove esperienze fisiche: i cittadini si trovano costretti alla vicinanza forzata nei tram o nelle vie affollate, subendo una drastica diminuzione dello spazio personale.",
 "La percezione dell'incommensurabile: il contrasto tra la folla e l'improvviso attraversamento di piazze e viali maestosi genera un senso di smarrimento e blocco fisico.",
 "La fobia degli spazi aperti: è in questo preciso contesto che si sviluppano patologie e nevrosi diffuse come l'agorafobia, cioè la paura delle folle e degli spazi aperti."]),
5:("Il pensiero di Freud e Georg Simmel",[
 "I disegni terapeutici di Freud: a Vienna, Sigmund Freud affronta le fobie dei suoi pazienti disegnando piantine urbane per aiutarli a collegare le reazioni patologiche agli spazi fisici.",
 "L'Esposizione di Dresda (1903): il sociologo Georg Simmel analizza pubblicamente le profonde conseguenze della vita metropolitana sulla mente umana.",
 "L'individuo iperstimolato: Simmel spiega che l'abitante della metropoli gestisce un numero esponenziale di relazioni superficiali senza reale conoscenza reciproca, scivolando nella solitudine."]),
6:("La nascita del design e il ruolo del progettista",[
 "I nuovi compiti della modernità: architetti e ingegneri devono rispondere a esigenze inedite: piani urbanistici per città in espansione, nuove abitazioni e uffici.",
 "Il dibattito sulla macchina: nel settore delle arti e mestieri si apre una riflessione sul superamento del contrasto tradizionale tra produzione manuale e industriale.",
 "Definizione di designer: nasce una figura intellettuale dedicata esclusivamente alla progettazione di oggetti in serie, distinguendosi nettamente dall'artigiano esecutore."]),
7:("Il Deutscher Werkbund (1907)",[
 "La fondazione: l'associazione nasce a Monaco nel 1907 per promuovere la nuova cultura del design attraverso una collaborazione strategica tra arte e industria.",
 "Gli obiettivi: unire le competenze di architetti, artisti e imprenditori per innalzare la qualità estetica, funzionale e la competitività globale dei prodotti tedeschi.",
 "I padri fondatori: l'iniziativa prende vita dal sodalizio tra l'imprenditore Karl Schmidt, il politico Friedrich Naumann e l'architetto Hermann Muthesius.",
 "Il modello inglese: Muthesius introduce le sue ricerche sull'architettura residenziale e sulle arti applicate inglesi, studiate per conto del governo prussiano a Londra."]),
8:("Vienna e la Secessione",[
 "Il declino dell'Impero: Vienna è una metropoli multiculturale di due milioni di abitanti, ma percorsa da un profondo senso di fine impero e crisi dei valori tradizionali.",
 "La crisi dell'io: intellettuali e artisti come Sigmund Freud, Gustav Klimt e Gustav Mahler aprono la strada alle tematiche espressioniste.",
 "La svolta espressionista: gruppi di artisti dissidenti si oppongono alle accademie ufficiali dando vita alle «Secessioni» a Monaco (1892), Vienna (1897) e Berlino (1898)."]),
10:("I precursori dell'Espressionismo: Ensor e Munch",[
 "James Ensor: l'artista belga rappresenta l'angoscia della condizione umana attraverso visioni grottesche, l'uso di maschere e scheletri e una pittura sarcastica.",
 "Edvard Munch: segnato da lutti e vicende personali, esplora i temi della malattia, della follia e della morte tra Oslo, Parigi e Berlino.",
 "Una pittura dell'anima: Munch abbandona il naturalismo a favore di una profonda intensità soggettiva, caricando i colori di forti valenze simboliche e psicologiche."]),
13:("I gruppi tedeschi: Die Brücke e Der Blaue Reiter",[
 "Die Brücke (Il Ponte): fondato a Dresda nel 1905 da studenti di architettura come Ernst Ludwig Kirchner; esprime disagio e ribellione attraverso forme spigolose e colori violenti.",
 "Der Blaue Reiter (Il Cavaliere Azzurro): fondato a Monaco nel 1911 da Vasilij Kandinskij e Franz Marc; punta su una pittura lirica, spirituale e orientata verso l'astrazione.",
 "Due anime diverse: mentre il primo gruppo è dominato dall'angoscia metropolitana, il secondo ricerca una sintesi armonica e spirituale attraverso il colore."]),
18:("L'Espressionismo austriaco: Kokoschka e Schiele",[
 "La specificità austriaca: a Vienna l'Espressionismo mantiene legami con la pittura simbolista e la Secessione, esprimendosi con una forte introspezione psicologica.",
 "Oskar Kokoschka: rappresenta la deformazione della realtà e le tensioni interiori attraverso una pittura tormentata e l'uso di colori pastosi e drammatici.",
 "Egon Schiele: esplora l'erotismo, il nudo e il tormento interiore attraverso un linguaggio lineare tagliente, corpi contorti e figure cariche di una tragica inquietudine."]),
}
# refusi corretti rispetto al PDF del prof (da elencare nel rapporto)
REFUSI=[
 "Slide 4: «Psicologia dello spazio urbano ed agorafobia» → «e agorafobia» (d eufonica non necessaria)",
 "Slide 4: «l'agorafobia (la paura delle folle e degli spazi aperti)» reso con «cioè» per la regola BES delle sigle/termini rispiegati",
 "Slide 13/PDF: «Blaue Reiter» e «Marc»: nel PDF del prof «Marc» (corretto: Franz Marc). Nel mio materiale resta «Franz Marc»",
 "Slide 7/8: «Hermann Muthesius» (nel video il prof dice «Mu Tesius»): nome scritto correttamente",
 "Mappa: «Kandinskij» (ortografia italiana del PDF) mantenuta; «Schmidt-Rottluff» scritto come nella mappa",
]
