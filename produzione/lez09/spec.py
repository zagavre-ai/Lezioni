# Specifica approfondimenti Lez 9 (Pascoli). Contenuti SOLO da videodispensa, libro (slide) e parole del docente.
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
ANS.append(AN("AN1", 1, 1, "linea", "Pascoli: la vita in una linea del tempo", [
 S("Le origini", "Mettiamo in ordine le tappe della vita di Pascoli. Nasce nel milleottocentocinquantacinque, a San Mauro di Romagna. La famiglia è della piccola borghesia rurale. Il padre, Ruggero, amministra dei terreni per conto del principe Torlonia. Il bambino cresce in un'infanzia serena. Poi, nel milleottocentosessantasette, tutto cambia. Il dieci agosto il padre viene ucciso con un colpo d'arma da fuoco alle spalle. Pascoli ha undici anni. Il colpevole non verrà mai scoperto. Questo dubbio senza risposta lo accompagnerà per tutta la vita.",
   [C("1855", "Nasce a San Mauro", "Romagna, piccola borghesia rurale"), C("1867", "Ucciso il padre Ruggero", "10 agosto, colpevole mai scoperto")]),
 S("I lutti e gli studi", "Dopo l'omicidio arrivano altri lutti. Muoiono la madre, la sorella maggiore e alcuni fratelli. Restano Giovanni e due sorelle, Ida e Mariù. Pascoli però non si ferma. Grazie a una borsa di studio studia a Firenze e a Bologna. All'università di Bologna ha come professore Giacomo Carducci. Con lui si laurea. Carducci è il suo maestro, ma Pascoli non ne seguirà lo stile solenne.",
   [C("1867 →", "Catena di lutti", "madre, sorella e fratelli"), C("Bologna", "Studia con Carducci", "borsa di studio, laurea")]),
 S("L'impegno politico", "Bologna in quegli anni è una città molto attiva. Si diffonde il socialismo, e Pascoli ne è affascinato. Partecipa alle iniziative dei socialisti locali. Nel milleottocentosettantanove subisce anche un breve arresto. Poi lascia l'attività politica e si dedica all'insegnamento. Insegna nei licei, proprio come aveva fatto Carducci. Il suo mestiere sono le materie classiche, il latino e la letteratura.",
   [C("1879", "Breve arresto", "ideologia socialista"), C("Licei", "Insegna latino", "materie classiche")]),
 S("La cattedra", "L'ultima tappa è l'università. Nel millenovecentocinque Carducci lascia la cattedra di Letteratura italiana a Bologna. Il successore è proprio Pascoli. Una carriera lunga, nata da una vita segnata dal dolore. Per questo la biografia è la chiave per capire la sua poesia. Pascoli morirà nel millenovecentododici.",
   [C("1905", "Cattedra a Bologna", "succede a Carducci"), C("1912", "Muore", "")])]))
ANS.append(MP("AN2", 1, 1, "La vita di Pascoli", "Costruiamo ora la mappa concettuale della vita di Pascoli. Al centro c'è il poeta. Da lui partono cinque rami.", [
 ("Le origini", "famiglia", "San Mauro, 1855", "Primo ramo, le origini. Pascoli nasce nel milleottocentocinquantacinque a San Mauro di Romagna, in una famiglia della piccola borghesia rurale."),
 ("Il trauma", "lutto", "padre ucciso, 1867", "Secondo ramo, il trauma. Il dieci agosto del milleottocentosessantasette viene ucciso il padre Ruggero. Seguono altri lutti in famiglia."),
 ("Gli studi", "Carducci", "Firenze e Bologna", "Terzo ramo, gli studi. Studia a Firenze e a Bologna, e a Bologna ha come maestro Carducci."),
 ("L'impegno politico", "socialismo", "arresto 1879", "Quarto ramo, l'impegno politico. Si avvicina al socialismo e nel milleottocentosettantanove subisce un breve arresto."),
 ("La carriera", "insegnamento", "cattedra 1905", "Quinto ramo, la carriera. Insegna nei licei e nel millenovecentocinque ottiene la cattedra di Letteratura italiana a Bologna, dopo Carducci.")]))
ANS.append(AN("AN3", 1, 2, "scheda", "La teoria del «nido»", [
 S("Un rifugio e una ferita", "Entriamo meglio nella teoria del nido. Il nido è il rifugio protettivo della famiglia. Fuori c'è un mondo che Pascoli sente minaccioso e violento. Dopo la morte del padre e degli altri familiari, Pascoli cerca soprattutto una cosa, la stabilità domestica. Appena riesce a mantenersi, vuole ricostruire la famiglia perduta. Lo ripete il docente: senza il dieci agosto del milleottocentosessantasette non si capisce Pascoli.",
   [C("", "Il nido", "rifugio protettivo dal mondo esterno, minaccioso e violento"), C("", "Il trauma", "il lutto cerca stabilità domestica")]),
 S("Le sorelle", "Pascoli resta l'unico maschio della famiglia. Si sente in dovere di prendersi cura delle sorelle. Le sorelle erano state ospitate in collegio. Appena può, vuole riunirle. Va a vivere con Ida e Mariù a Castelvecchio di Barga. Qui ricostruisce, a lungo, il nucleo originario della famiglia. Il nido ritorna spesso anche nelle sue poesie.",
   [C("", "Ida e Mariù", "con lui a Castelvecchio di Barga"), C("", "Un nido ricostruito", "il nucleo originario della famiglia")]),
 S("La fragilità", "Questo legame è profondo ed esclusivo. Mostra una fragilità psicologica. Pascoli non si sposa e ha difficoltà a creare relazioni mature fuori dal nido. Le relazioni esterne, soprattutto con il mondo femminile, sono vissute come una minaccia. Una sorella resterà con lui per tutta la vita. L'altra si sposerà, e lui ne soffrirà. Ricordiamolo: è un profilo psicologico, utile per capire i temi delle sue poesie.",
   [C("", "Fragilità", "difficoltà nelle relazioni esterne al nido"), C("", "Nessuna famiglia propria", "non si sposa mai")])]))
ANS.append(MP("AN4", 1, 2, "Il «nido»", "Ecco la mappa concettuale del nido. Al centro c'è il nido familiare. I rami sono quattro.", [
 ("Il rifugio", "protezione", "dal mondo violento", "Primo ramo, il rifugio. Il nido protegge dal mondo esterno, percepito come minaccioso e violento."),
 ("La ferita", "lutti", "10 agosto 1867", "Secondo ramo, la ferita. Nasce dal trauma dell'uccisione del padre e dai lutti familiari."),
 ("Le sorelle", "Ida e Mariù", "Castelvecchio di Barga", "Terzo ramo, le sorelle. Pascoli vive con Ida e Mariù per ricostruire il nucleo originario."),
 ("La fragilità", "isolamento", "difficoltà nelle relazioni", "Quarto ramo, la fragilità. Il trauma genera una difficoltà a stabilire relazioni mature fuori dal nido.")]))
ANS.append(AN("AN5", 1, 3, "scheda", "Il fanciullino: il saggio del 1897", [
 S("Il saggio", "Il fanciullino è il saggio in cui Pascoli spiega la sua idea di poesia. Una parte uscì nel milleottocentonovantasette sulla rivista Il Marzocco, con il titolo Pensieri sull'arte poetica. Nello stesso anno uscivano la prima edizione dei Poemetti e la quarta di Myricae. Nella versione definitiva il testo fu poi ripubblicato nel millenovecentotré, nella raccolta di prose Miei pensieri di varia umanità. Il libro propone alcuni passi fondamentali, in cui la poetica pascoliana si delinea con chiarezza.",
   [C("1897", "Pensieri sull'arte poetica", "rivista Il Marzocco"), C("1903", "Miei pensieri di varia umanità", "raccolta di prose, versione definitiva")]),
 S("Il fanciullino che è in noi", "Che cosa dice il testo? In ogni uomo vive una parte fanciullesca. È il fanciullino. Guarda il mondo con meraviglia, come fa un bambino. Cresciamo, ma il fanciullino resta piccolo. La sua voce è come un tintinnio di campanello, che gli adulti, presi dai loro affari, non ascoltano. Il poeta è chi sa ascoltarlo e dargli voce. Per questo il poeta conosce le cose in modo intuitivo, non con la logica.",
   [C("", "Meraviglia", "sguardo ingenuo sulle cose"), C("", "Intuizione", "non la logica, ma le corrispondenze segrete")]),
 S("Le piccole cose", "Il libro indica quattro temi principali del testo. La conoscenza immaginosa del poeta fanciullino. L'utilità morale e sociale della poesia. Le corrispondenze segrete tra le cose. La poetica delle piccole cose. Per Pascoli la poesia è pura, cioè libera da scopi morali, pedagogici o politici diretti. Proprio per questo unisce gli uomini e li rende più buoni.",
   [C("", "Poesia pura", "senza scopi politici o morali diretti"), C("", "Utilità sociale", "unisce gli uomini e induce alla bontà")])]))
ANS.append(AN("AN6", 1, 3, "confronto", "Pascoli e D'Annunzio a confronto", [
 S("Due poeti, un'epoca", "Pascoli e D'Annunzio nascono entrambi dal Decadentismo e dal simbolismo, ma sono molto diversi. Il docente li confronta spesso, per capire le differenze. Cominciamo dal modo di intendere il poeta. Per D'Annunzio il poeta è una figura pubblica, un personaggio che fa parlare di sé. Per Pascoli il poeta è il fanciullino, che dà voce al mondo interiore. Pascoli sta dietro le quinte. Odiava quel mondo.",
   [C("Pascoli", "Il fanciullino", "poesia pura, nessun interesse pubblico"), C("D'Annunzio", "Il personaggio", "figura pubblica che fa parlare di sé")]),
 S("Lo stile e il mondo", "Lo stile è un altro punto di differenza. Pascoli rompe i ponti con la tradizione classicista. Preferisce frasi brevi affiancate, uno stile nominale e vocaboli quotidiani. Usa termini precisi della botanica e dell'ornitologia. Non c'è estetismo e non c'è seduzione. L'uomo e la natura dialogano. D'Annunzio invece cerca l'estetismo, il fascino, il gesto che si fa notare.",
   [C("Pascoli", "Piccole cose", "paratassi, termini di botanica e di uccelli"), C("D'Annunzio", "Estetismo", "seduzione e immagine pubblica")]),
 S("Che cosa li unisce", "Qualcosa li unisce. Tutti e due sono figli del Decadentismo e del simbolismo. Tutti e due sentono la crisi del Positivismo. Ma le strade sono diverse. Per Pascoli la poesia pura induce alla fratellanza e consola dalla sofferenza umana. Per questo, dice il docente, possiamo capire meglio ciascuno solo confrontandoli.",
   [C("Insieme", "Decadentismo e simbolismo", "crisi del Positivismo"), C("Pascoli", "Fratellanza", "la poesia pura consola")])]))
ANS.append(MP("AN7", 1, 3, "Il fanciullino", "Ora la mappa concettuale della poetica del fanciullino. Al centro c'è il fanciullino. I rami sono cinque.", [
 ("Il saggio", "1897", "Il Marzocco", "Primo ramo, il saggio. Il fanciullino esce nel milleottocentonovantasette e poi nei Miei pensieri di varia umanità."),
 ("Il fanciullino", "meraviglia", "sguardo del bambino", "Secondo ramo, il fanciullino. In ogni uomo c'è una parte infantile che guarda il mondo con meraviglia."),
 ("Il poeta", "intuizione", "non la logica", "Terzo ramo, il poeta. Dà voce al fanciullino e conosce le cose per intuizione, non con il ragionamento."),
 ("La poesia pura", "autonomia", "niente morale o politica", "Quarto ramo, la poesia pura. La poesia non ha scopi morali, pedagogici o politici diretti."),
 ("L'utilità sociale", "fratellanza", "unisce gli uomini", "Quinto ramo, l'utilità sociale. Proprio per la sua purezza, la poesia unisce gli uomini e induce alla bontà.")]))
ANS.append(AN("AN8", 1, 4, "parole", "Parole chiave dello stile di Pascoli", [
 S("Suoni e analogie", "Quattro parole chiave per capire lo stile di Myricae e dei Canti di Castelvecchio. La prima è onomatopea. È una parola che riproduce un suono, come scrivere brum per il rumore di una moto. Pascoli la usa di continuo, per riprodurre i suoni della natura. La seconda è fonosimbolismo. Qui i suoni delle parole hanno un significato simbolico. Sono impressioni acustiche che vogliono evocare il significato profondo e misterioso delle cose.",
   [C("", "Onomatopea", "parola che imita un suono"), C("", "Fonosimbolismo", "i suoni hanno un significato simbolico")]),
 S("Linguaggio e sintassi", "La terza parola è linguaggio analogico. Pascoli accosta le cose per somiglianze nascoste, senza spiegare. La quarta è sintassi frantumata. Le frasi sono spezzettate, coordinate, spesso nominali, e il ritmo diventa discontinuo. Aggiungiamo il lessico: termini precisi della botanica e dell'ornitologia, mescolati a parole quotidiane. Sono scelte formali che fanno della poesia pascoliana una poesia molto moderna.",
   [C("", "Linguaggio analogico", "accosta le cose per somiglianza"), C("", "Sintassi frantumata", "frasi spezzate, ritmo discontinuo")]),
 S("Le piccole cose", "Torniamo infine al titolo della prima raccolta. Myricae, con la y, è latino e significa tamerici. Sono piante basse. Il riferimento è a un verso del poeta latino Virgilio, che dice: mi piacciono gli arbusti e le basse tamerici. Pascoli annuncia così che canterà le piccole cose. Il muschio, l'arbusto, e non il pino, la sequoia o le grandi piante di cui parlano tutti.",
   [C("1891", "Myricae", "prima raccolta, vita campestre"), C("1903", "Canti di Castelvecchio", "stessi temi, toni più inquieti")])]))
ANS.append(MP("AN9", 1, 4, "Myricae e Canti di Castelvecchio", "Mappa concettuale delle due raccolte. Al centro, la poesia delle piccole cose.", [
 ("Myricae", "1891", "tamerici", "Primo ramo. Myricae è la prima raccolta, del milleottocentonovantuno. Il titolo richiama le basse tamerici."),
 ("Canti di Castelvecchio", "1903", "toni inquieti", "Secondo ramo. I Canti di Castelvecchio, del millenovecentotré, continuano Myricae con una misura lirica più inquieta."),
 ("Temi", "morte e lutto", "vita campestre", "Terzo ramo. La vita campestre è carica di simboli legati alla morte e al dramma familiare."),
 ("Suoni", "fonosimbolismo", "onomatopee", "Quarto ramo. Onomatopee e fonosimbolismo riproducono il significato profondo dei suoni."),
 ("Lingua", "sintassi frantumata", "linguaggio analogico", "Quinto ramo. Il linguaggio è analogico e la sintassi è frantumata.")]))
ANS.append(MP("MF1", 1, 99, "Pascoli · Parte 1", "Per finire, la mappa concettuale di tutta la prima parte. Al centro c'è Giovanni Pascoli. Ripassiamo i quattro rami.", [
 ("La vita", "trauma", "1867", "Primo ramo, la vita. Nasce nel milleottocentocinquantacinque, nel milleottocentosessantasette perde il padre, ucciso, e studia con Carducci."),
 ("Il nido", "famiglia", "Ida e Mariù", "Secondo ramo, il nido. Pascoli cerca di ricostruire la famiglia perduta con le sorelle, a Castelvecchio di Barga."),
 ("Il fanciullino", "meraviglia", "poesia pura", "Terzo ramo, il fanciullino. La poesia dà voce alla parte infantile che è in ogni uomo, con intuizione e meraviglia."),
 ("Le raccolte", "Myricae", "Canti di Castelvecchio", "Quarto ramo, le raccolte. Myricae e Canti di Castelvecchio cantano le piccole cose con onomatopee, fonosimbolismo e sintassi frantumata.")]))
# ---------------- PARTE 2 ----------------
v = ["San Lorenzo, io lo so perché tanto", "di stelle per l'aria tranquilla", "arde e cade, perché sì gran pianto", "nel concavo cielo sfavilla."]
v2 = ["Anche un uomo tornava al suo nido:", "l'uccisero: disse: Perdono;", "e restò negli aperti occhi un grido:", "portava due bambole in dono..."]
v3 = ["Ora là, nella casa romita,", "lo aspettano, aspettano in vano:", "egli immobile, attonito, addita", "le bambole al cielo lontano."]
ANS.append(AN("AN1", 2, 1, "testo", "X Agosto · lettura guidata", [
 dict(titolo="Il cielo piange", versi=v, evid=[0, 1, 2, 3], note=["Il testo si apre con San Lorenzo, la notte del dieci agosto.", "Le stelle cadenti arrivano da un'aria tranquilla.", "Il cielo sembra piangere: un pianto, dice Pascoli.", "È il pianto del cielo sulla terra."],
   voce="Leggiamo insieme alcuni versi di X Agosto. La poesia è tratta da Myricae. Ricorda l'uccisione del padre, avvenuta il dieci agosto del milleottocentosessantasette, giorno di San Lorenzo. Il metro è fatto di quartine di decasillabi e novenari alternati, con rime abab. Il primo verso nomina San Lorenzo. Le stelle cadenti attraversano un'aria tranquilla. Ma questo pianto di stelle, dice Pascoli, ha una ragione. Il cielo sfavilla, e sembra piangere."),
 dict(titolo="Il padre", versi=v2, evid=[0, 1, 2, 3], note=["Il nido dell'uomo è un nido, non un tetto come quello della rondine.", "Nel morire la vittima perdona: è un motivo ricorrente della retorica pascoliana.", "Gli occhi sbarrati esprimono il grido che il padre non poté emettere.", "Il dono per le figlie: due bambole."],
   voce="Nella quarta quartina il padre prende il posto della rondine. Anche un uomo tornava al suo nido. Il libro nota lo scambio dal forte valore simbolico: quello dell'animale è un tetto, quello dell'uomo è un nido. L'uccisero. E il padre disse: Perdono. Nel morire, la vittima perdona gli assassini. Negli occhi aperti resta un grido, quello che il padre non poté emettere. Portava due bambole in dono."),
 dict(titolo="La casa vuota", versi=v3, evid=[0, 1, 2, 3], note=["Romita: solitaria, desolata per l'assenza del padre.", "Lo aspettano invano: il nido è vuoto.", "Attonito: sbigottito dalla malvagità umana.", "Le bambole al cielo: è il parallelismo con la rondine."],
   voce="Poi lo sguardo passa alla casa. Ora là, nella casa romita, cioè solitaria e desolata. Lo aspettano, ma aspettano invano. Lui è immobile e attonito, sbigottito dalla malvagità umana. E addita le bambole al cielo lontano. Il parallelismo con la rondine è evidente. La rondine che tende il verme al cielo, e l'uomo che addita le bambole al cielo. Il dolore di una famiglia diventa il dolore del mondo. Alla fine Pascoli chiama il Cielo e lo invita a inondare di stelle questo atomo opaco del Male: la terra.")]))
ANS.append(MP("AN2", 2, 1, "X Agosto", "Mappa concettuale di X Agosto. Al centro, il dieci agosto del milleottocentosessantasette.", [
 ("La notte", "San Lorenzo", "stelle cadenti", "Primo ramo, la notte. È San Lorenzo, la notte delle stelle cadenti."),
 ("La rondine", "il nido", "il verme ai piccoli", "Secondo ramo, la rondine. Torna al tetto con il cibo per i rondinini, ma cade uccisa."),
 ("Il padre", "perdono", "due bambole in dono", "Terzo ramo, il padre. Torna al suo nido portando due bambole. Lo uccidono, e muore perdonando."),
 ("Il parallelismo", "natura e uomo", "rondine e padre", "Quarto ramo, il parallelismo. La sorte della rondine e quella del padre si rispecchiano."),
 ("Il cielo", "il Male", "atomo opaco", "Quinto ramo, il cielo. Le stelle sono un pianto che inonda la terra, atomo opaco del Male.")]))
ANS.append(AN("AN3", 2, 2, "scheda", "L'assiuolo e Temporale", [
 S("L'assiuolo", "Passiamo a due poesie di Myricae. La prima è L'assiuolo. Fu pubblicata sulla rivista Il Marzocco il tre gennaio del milleottocentonovantasette, e poi nella quarta edizione di Myricae. L'assiuolo è un piccolo uccello rapace notturno, simile al gufo. Emette un verso monotono e malinconico, che sembra un lamento. Il libro indica due temi: l'angoscia della morte e il linguaggio allusivo.",
   [C("1897", "L'assiuolo", "Il Marzocco, poi Myricae"), C("", "Angoscia della morte", "linguaggio allusivo")]),
 S("Temporale", "La seconda è Temporale. Come si ricava da un quaderno manoscritto, fu concepita nell'agosto del milleottocentonovantadue. Fu pubblicata nella terza edizione di Myricae, nel milleottocentonovantaquattro. È una ballata minima di settenari. I temi indicati dal libro sono tre: l'annullamento dei legami logico-sintattici, il linguaggio analogico e allusivo, il simbolismo. Sono tre caratteristiche tipiche della poesia pascoliana.",
   [C("1892", "Temporale", "terza edizione di Myricae, 1894"), C("", "Linguaggio analogico", "annullamento dei legami logico-sintattici")])]))
ANS.append(MP("AN4", 2, 2, "L'assiuolo e Temporale", "Mappa concettuale dei due testi. Al centro, due poesie di Myricae.", [
 ("L'assiuolo", "1897", "uccello notturno", "Primo ramo. L'assiuolo è un piccolo uccello rapace notturno, simile al gufo."),
 ("Il verso", "lamento", "monotono e malinconico", "Secondo ramo. Il suo verso è monotono e malinconico, e sembra un lamento."),
 ("Il tema", "morte", "angoscia", "Terzo ramo. Il tema è l'angoscia della morte, espressa con un linguaggio allusivo."),
 ("Temporale", "1892", "ballata minima", "Quarto ramo. Temporale è una ballata minima di settenari, concepita nell'agosto del milleottocentonovantadue."),
 ("Lo stile", "simbolismo", "analogia", "Quinto ramo. I legami logici si annullano, e domina il linguaggio analogico e simbolico.")]))
ANS.append(AN("AN5", 2, 3, "scheda", "Novembre, Il lampo, Il gelsomino notturno", [
 S("Novembre", "Tre poesie, tre schede. La prima è Novembre. Fu abbozzata ed elaborata nel milleottocentonovanta e pubblicata sulla rivista Vita Nuova nel febbraio del milleottocentonovantuno. Entrò poi nella prima edizione di Myricae. I temi: la realtà frutto dell'immaginazione, l'immagine simbolica della morte, la frantumazione dei versi.",
   [C("1891", "Novembre", "rivista Vita Nuova, poi Myricae"), C("", "Immaginazione e morte", "versi frantumati")]),
 S("Il lampo", "La seconda è Il lampo. Fu composta negli anni milleottocentonovantadue e novantatré e pubblicata nella terza edizione di Myricae, nel milleottocentonovantaquattro. Il tema indicato dal libro è la rappresentazione simbolica di un dolore tragico: la morte del padre. Anche qui torna il trauma che ha segnato la vita di Pascoli.",
   [C("1892-93", "Il lampo", "terza edizione di Myricae"), C("", "Dolore tragico", "la morte del padre")]),
 S("Il gelsomino notturno", "La terza è Il gelsomino notturno. Fu composta per le nozze dell'amico Gabriele Briganti, e uscì come opuscolo nel millenovecentouno. Fu poi raccolta nei Canti di Castelvecchio, nel millenovecentotré. Il metro è fatto di quartine di novenari a rime alternate, abab. Tema centrale è il rapporto tormentato di Pascoli con l'amore. Il poeta resta fuori dalla casa nuziale. Il libro indica l'opposizione tra la casa nuziale e il nido, e l'esclusione dalle gioie familiari.",
   [C("1901", "Il gelsomino notturno", "nozze di Gabriele Briganti, poi Canti di Castelvecchio"), C("", "Casa e nido", "il poeta escluso dalle gioie familiari")])]))
ANS.append(MP("AN6", 2, 3, "Tre poesie, tre temi", "Mappa concettuale dei tre testi. Al centro, i temi principali.", [
 ("Novembre", "immaginazione", "morte simbolica", "Primo ramo. Novembre mostra una realtà frutto dell'immaginazione e un'immagine simbolica della morte."),
 ("Il lampo", "dolore tragico", "morte del padre", "Secondo ramo. Il lampo rappresenta in modo simbolico un dolore tragico, la morte del padre."),
 ("Il gelsomino notturno", "eros", "nozze di Briganti", "Terzo ramo. Il gelsomino notturno è scritto per le nozze di un amico. Il tema è l'eros e il suo mistero."),
 ("Il poeta escluso", "nido", "fuori dalla casa", "Quarto ramo. Pascoli osserva da fuori. Si oppone la casa nuziale al nido dei morti."),
 ("La forma", "versi frantumati", "analogia", "Quinto ramo. La forma è spezzata, con versi frantumati e linguaggio analogico.")]))
ANS.append(AN("AN7", 2, 4, "scheda", "Poemetti, Poemi conviviali, Carmina e idee politiche", [
 S("I Poemetti", "Dopo le poesie brevi, le raccolte più ampie. I Poemetti si dividono in Primi poemetti e Nuovi poemetti. Hanno un taglio più narrativo e ampio. Celebrano la campagna: il mondo contadino è custode di affetti, tradizioni e valori fondamentali. Ma emerge anche il contrasto tra civiltà rurale e modernità industriale. Compare il dramma dell'emigrazione, come nella lirica Italy.",
   [C("", "Poemetti", "Primi e Nuovi poemetti, taglio narrativo"), C("", "Campagna e modernità", "contrasto, emigrazione: Italy")]),
 S("Le ultime raccolte", "Nell'ultima fase Pascoli scrive i Poemi conviviali, dedicati a personaggi e miti del mondo antico. Scrive i Carmina, in lingua latina, che ottengono riconoscimenti internazionali. E scrive saggi critici, soprattutto su Dante. Sono prove di un grande latinista e di uno studioso molto attivo.",
   [C("", "Poemi conviviali", "miti del mondo antico"), C("", "Carmina e saggi", "latino, e studi su Dante")]),
 S("Le idee politiche", "Resta il pensiero politico. Pascoli si era avvicinato al socialismo. Con il tempo rifiuta la lotta di classe e la rivoluzione. Il suo diventa un socialismo umanitario, una fede nella fratellanza universale. Il docente lo definisce una religione laica. Il nazionalismo pascoliano difende la piccola proprietà e la patria. Arriva a giustificare le guerre coloniali, come la guerra di Libia, per dare terra ai lavoratori italiani. Pascoli morirà nel millenovecentododici.",
   [C("", "Socialismo umanitario", "fratellanza, no lotta di classe"), C("", "Nazionalismo", "la patria, la guerra di Libia")])]))
ANS.append(MP("AN8", 2, 4, "Poemetti e ultime raccolte", "Mappa concettuale delle raccolte più tarde. Al centro, i Poemetti e le ultime raccolte.", [
 ("I Poemetti", "narrativi", "Primi e Nuovi", "Primo ramo. I Poemetti hanno un taglio narrativo e ampio."),
 ("La campagna", "valori", "tradizioni e affetti", "Secondo ramo. Il mondo contadino custodisce affetti, tradizioni e valori."),
 ("L'emigrazione", "modernità", "Italy", "Terzo ramo. Il conflitto con la modernità porta al dramma dell'emigrazione, come in Italy."),
 ("Poemi e Carmina", "mondo antico", "latino", "Quarto ramo. I Poemi conviviali e i Carmina guardano al mondo antico."),
 ("I saggi", "Dante", "critica", "Quinto ramo. L'attività di studioso culmina nei saggi su Dante."),
 ("Le idee politiche", "umanitarismo", "guerra di Libia", "Sesto ramo. Socialismo umanitario e nazionalismo, fino alla guerra di Libia.")]))
ANS.append(MP("MF2", 2, 99, "Pascoli · tutta la lezione", "Concludiamo con la mappa concettuale di tutta la lezione su Pascoli. Al centro c'è il poeta. Ripassiamo sei rami.", [
 ("La vita", "trauma", "1867", "Primo ramo, la vita. Il padre ucciso nel milleottocentosessantasette, gli studi con Carducci, la cattedra a Bologna."),
 ("Il nido", "famiglia", "Ida e Mariù", "Secondo ramo, il nido. La ricerca di stabilità con le sorelle, a Castelvecchio di Barga."),
 ("Il fanciullino", "poesia pura", "1897", "Terzo ramo, il fanciullino. La poetica della meraviglia e delle piccole cose."),
 ("Myricae e Canti", "simbolismo", "X Agosto", "Quarto ramo. Le raccolte brevi: X Agosto, L'assiuolo, Temporale, Novembre, Il lampo, Il gelsomino notturno."),
 ("Lo stile", "onomatopee", "sintassi frantumata", "Quinto ramo, lo stile. Onomatopee, fonosimbolismo, linguaggio analogico e sintassi frantumata."),
 ("Le ultime raccolte", "Poemetti", "Carmina", "Sesto ramo. Poemetti, Poemi conviviali, Carmina e le idee politiche tra umanitarismo e nazionalismo.")]))

def voce_testo(a):
    return " ".join(a["voci"]) if a["tipo"] == "mappa" else " ".join(s["voce"] for s in a["schermate"])
if __name__ == "__main__":
    out = os.path.dirname(os.path.abspath(__file__))
    for p in (1, 2):
        w = 0
        for a in ANS:
            if a["parte"] == p: w += len(voce_testo(a).split())
        print("Parte", p, "parole", w, "≈ min", round(w / 2.5 / 60, 1))
