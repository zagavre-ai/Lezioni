import json
P={
"P1":["Avanguardia viene dal francese avant-garde: le truppe d'avanscoperta dell'esercito.",
"Gli artisti d'avanguardia si oppongono ai canoni delle accademie e al gusto della borghesia.",
"Partono dal Postimpressionismo e dal Simbolismo e subiscono il fascino del primitivismo dell'Africa e dell'Asia.",
"Sono influenzati dalle scoperte scientifiche, dalla psicoanalisi, dal cinema, dal movimento e dalla velocità.",
"Parigi, nel millenovecento, è la capitale della Belle Époque e il centro dell'arte mondiale."],
"P2":["Nel millenovecentocinque un gruppo di artisti espone al Salon d'Automne di Parigi e scatena forti polemiche.",
"Il critico Louis Vauxcelles esclama: Donatello in mezzo alle belve! E nasce il nome Fauves.",
"I Fauves abbandonano la prospettiva e il chiaroscuro e usano colori antinaturalistici.",
"Il capolavoro è La felicità di vivere di Henri Matisse, del millenovecentocinque, millenovecentosei.",
"Nel gruppo spiccano anche Maurice de Vlaminck e André Derain."],
"P3":["Nel millenovecentotto Matisse scrive che l'arte non deve imitare la realtà.",
"L'arte esprime il sentimento intimo del pittore, attraverso l'armonia interiore del quadro.",
"La Danza è commissionata dal collezionista Shchukin: cinque corpi nudi danzano in cerchio su un fondo blu e verde.",
"Dopo i viaggi in Nord Africa nascono le odalische e gli interni dai motivi complessi.",
"Negli ultimi anni Matisse inventa i papiers découpés: carte colorate ritagliate a forbice."],
"P4":["Picasso attraversa il periodo blu, sulla miseria e l'emarginazione, e il periodo rosa, legato al circo.",
"Les Demoiselles d'Avignon, del millenovecentosette, segnano la nascita del Cubismo.",
"Cinque figure femminili sono scomposte in piani geometrici taglienti.",
"I volti delle figure di destra sono ricalcati sulle maschere africane.",
"Dal millenovecentotto Picasso e Georges Braque lavorano insieme alla scomposizione della realtà."],
"P5":["Il Protocubismo, dal millenovecentosette al millenovecentonove, usa volumi geometrici puri: cubi, cilindri e sfere.",
"Il Cubismo Analitico, dal millenovecentonove al millenovecentododici, frammenta gli oggetti e li vede da più punti di vista.",
"La tavolozza è monocroma: grigi, ocra, marroni e neri.",
"Il Cubismo Sintetico, dal millenovecentododici al millenovecentoquattordici, ricompone l'oggetto in forme più leggibili.",
"Con i papiers collés Braque e Picasso incollano nel quadro ritagli di giornale, spartiti e paglia."],
"P6":["Léger e Gris diffondono il Cubismo nelle grandi mostre pubbliche.",
"Robert Delaunay, con l'Orfismo, studia la luce pura e i contrasti simultanei di colore.",
"La scultura cubista introduce il vuoto come elemento plastico.",
"Picasso inventa gli assemblages, con materiali poveri: legno, cartone e corda.",
"Brâncuși cerca la forma pura e originaria, senza dettagli superflui."],
"P7":["A Montparnasse lavorano artisti che non aderiscono a nessun manifesto teorico.",
"Henri Rousseau, detto il Doganiere, è un autodidatta: la sua pittura naïf è bidimensionale e sognante.",
"Marc Chagall unisce scomposizione cubista e colore fauve alle tradizioni ebraiche della sua infanzia in Russia.",
"Amedeo Modigliani costruisce il suo stile sulla purezza della linea.",
"I suoi ritratti e i suoi nudi hanno figure allungate e occhi enigmatici, privi di pupilla."],
}
M={
"MAP_FAUVES":"Chi sono i Fauves? I Fauves, le belve, millenovecentocinque, millenovecentosette. Il termine fu utilizzato per sottolineare, in senso spregiativo, l'uso selvaggio del colore. Movimento pittorico francese: fu il primo dei grandi movimenti d'avanguardia dell'arte europea nel periodo di sperimentazione. Caratteristiche principali. La prospettiva viene ignorata, e il senso della profondità è prodotto dalla visione di scorcio su un piano unico e dal contrasto cromatico. Semplificazione delle forme, l'immediatezza e il colore. Si dipinge in relazione al sentire interiore e non all'impressione. Il colore è svincolato dalla realtà: alberi viola e figure umane rosse, scelti e accostati liberamente, secondo esclusivamente l'armonia della composizione. La pittura è istintiva e immediata. Espressionismo, millenovecentocinque, millenovecentoventicinque. Maggiori esponenti: André Derain, Henri Matisse, Maurice de Vlaminck, Albert Marquet, Georges Braque. I punti di riferimento: Cézanne, per la smaterializzazione e ricomposizione delle forme; Gauguin e Van Gogh, per i colori impiegati puri, con violenza.",
"MAP_CUBISMO":"Che cos'è il Cubismo? Cubismo. È un movimento di avanguardia. Nasce nel millenovecentosette a Parigi. Principali protagonisti: Picasso, Braque, Gris. Raffigura simultaneamente un oggetto da vari punti di vista. Si supera il metodo prospettico tradizionale. Deriva dalle ricerche di Cézanne e dalla scultura primitiva. Il termine nasce nel millenovecentootto, in senso dispregiativo. L'oggetto subisce una scomposizione e una ricomposizione sulla tela. I soggetti non sono innovativi. Vedono non solo con gli occhi, ma anche con la mente. Le fasi del Cubismo sono tre. Il Cubismo formativo: le caratteristiche sono forme semplificate, volumi puri, influenza dell'arte primitiva. Il Cubismo analitico: spezza le forme in piccoli piani, il soggetto diventa quasi indecifrabile, il colore è quasi assente. Il Cubismo sintetico: semplifica la scomposizione, usa piani larghi e colorati, usa il collage polimaterico, l'opera diventa un soggetto autonomo.",
"MAP_FINALE":"Che cosa sono le Avanguardie? Avanguardie, arte. Il periodo: primo Novecento. Che cos'è: un movimento artistico-culturale nato in Europa. L'Espressionismo esprime il mondo interiore: paura, angoscia. Tra gli Espressionisti, i Fauves: colori molto forti. Munch, Nolde e Matisse. Il Cubismo: forme geometriche. Picasso, Gris, Braque. Il Futurismo: movimento e velocità; auto e treni; sport. Severini, Boccioni, Russolo. L'Astrattismo esprime il mondo interiore, con colori puri. Kandinskij, Mondrian. Il Dadaismo esprime la libertà dell'artista. Duchamp, Schwitters, Man Ray. La Scuola di Parigi: interesse per l'arte primitiva. Modigliani, Chagall. Il Surrealismo: l'inconscio, sogno e fantasia. Miró, Dalí, Ernst, Magritte. La Metafisica: atmosfere irreali, mistero. De Chirico.",
}
out=[{"nome":k,"testo":" ".join(v)} for k,v in P.items()]+[{"nome":k,"testo":v} for k,v in M.items()]
json.dump(out,open('/tmp/claude-0/w/build/nuove_voci.json','w'),ensure_ascii=False,indent=1)
json.dump(P,open('/tmp/claude-0/w/build/pillole.json','w'),ensure_ascii=False,indent=1)
print(len(out),sum(len(o['testo'].split()) for o in out))
