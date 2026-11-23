# Dati della lezione 18 · Storia dell'arte V · «Postmodernità e globalizzazione»
# Tutti i testi vengono SOLO dal materiale del prof (videolezione, slide PDF, mappe, domande).
import re, json

U = ['zero','uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
T = ['','','venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
def card(n):
    if n < 20: return U[n]
    if n < 100:
        t, u = divmod(n, 10); w = T[t]
        if u in (1, 8): w = w[:-1]
        return w + (U[u] if u else '')
    if n < 1000:
        c, r = divmod(n, 100); w = 'cento' if c == 1 else U[c] + 'cento'
        if r and 80 <= r < 90: w = w[:-1]
        return w + (card(r) if r else '')
    m, r = divmod(n, 1000)
    w = 'mille' if m == 1 else card(m) + 'mila'
    return w + (card(r) if r else '')
def voce(s):
    s = re.sub(r'(\d{4})\s*-\s*(\d{4})', lambda m: card(int(m[1])) + ' e ' + card(int(m[2])), s)
    s = s.replace('XXI secolo', 'ventunesimo secolo')
    s = re.sub(r'\d+', lambda m: card(int(m[0])), s)
    return s

TITOLO = 'Postmodernità e globalizzazione'
MATERIA = "Storia dell'arte V"
MATERIA_MAI = "STORIA DELL'ARTE V"

# Argomenti: (id, titolo, inizio, fine) sulla trascrizione dell'originale; pagine delle slide del prof
ARGOMENTI = [
 ('A1', 'Il contesto globale e la condizione postmoderna'),
 ('A2', 'Il postmoderno nelle arti figurative e la dimensione globale'),
 ('A3', 'Il ritorno alla pittura in Germania e in Italia'),
 ('A4', 'Graffiti e Street Art'),
 ('A5', 'Fotografia, Video Art e nuovi media'),
 ('A6', "L'artista nella società globale: le Artistar"),
 ('A7', "Le ultime tendenze dell'architettura contemporanea"),
]

# Approfondimenti (voce Kore, 40-60 s)
AP = {
'A1': "Come cambia il mondo, e con lui l'arte? Per secoli la società si è retta sull'agricoltura, poi sull'industria, e oggi su un terziario tecnologico: i servizi e lo scambio di dati digitali prevalgono sulla manifattura. È la società dell'informazione, nata dalla rivoluzione informatica e dal World Wide Web, cioè la rete mondiale dei siti. Nel 1989 cade il muro di Berlino e nel 1991 si scioglie l'Unione Sovietica: il mondo non è più bipolare, ma multipolare. Seguono conflitti, minacce terroristiche, come l'attacco alle Twin Towers del 2001, e movimenti di contestazione ecologista e sociale. In questo clima, nel 1979, il filosofo Jean-François Lyotard teorizza la condizione postmoderna: il tramonto delle grandi narrazioni storiche e ideologiche, come il marxismo o l'illuminismo.",
'A2': "Dopo l'arte concettuale e minimalista, il postmoderno torna alla figurazione, alla pittura e alla scultura, in chiave ironica e disincantata. Un orinatoio capovolto diventa un oggetto da museo. Nel 1991 Sherrie Levine, con Fountain, After Marcel Duchamp, riprende la celebre fontana presentata da Duchamp nel 1917. Ma invece di riprodurla fedelmente con un oggetto industriale, la fonde in bronzo lucido: l'oggetto provocatorio e antiestetico diventa un feticcio prezioso, da museo. È l'appropriazionismo: gli artisti si appropriano di opere del passato o di immagini della cultura di massa, per metterne in discussione l'originalità e l'unicità. Così Levine omaggia la nascita dell'arte concettuale e riflette sulla mercificazione dell'arte e sulla perdita dell'aura dell'opera nell'epoca della sua riproducibilità tecnica.",
'A3': "Nomade ed eclettico: così il critico Achille Bonito Oliva definisce, nel 1979, la Transavanguardia italiana. Gli artisti rivendicano la libertà di attraversare tutti gli stili del passato, recuperando il mestiere della pittura e il piacere della narrazione figurativa, al di fuori di ogni dogmatismo concettuale. Sandro Chia, con Gioco di mano, del 1980, è l'anima citazionista del gruppo. Francesco Clemente, nel Cerchio di Milarepa, del 1982, unisce Occidente e Oriente. Mimmo Paladino, con La verità del fornaio in carrozza, del 1981, torna alle radici mitiche del Mediterraneo. In Germania, intanto, il ritorno alla pittura è guidato dal neoespressionismo di Georg Baselitz e Anselm Kiefer, e dal realismo freddo di Gerhard Richter.",
'A4': "Il Tuttomondo di Keith Haring. Nel 1989 l'artista dipinge sulla parete della chiesa di Sant'Antonio, a Pisa, l'ultimo grande lavoro pubblico, prima della sua prematura scomparsa. Trenta figure antropomorfe, stilizzate e concatenate l'una all'altra in un incastro cromatico perfetto, evocano un ritmo vitale ed energico. Ogni figura compie un'azione simbolica: ci sono figure che sconfiggono il male e figure che ne sorreggono altre. È un inno alla vita, alla pace e alla solidarietà globale. Il suo alfabeto visivo trova la sintesi nel Radiant Baby, il bambino radiante, tracciato con il gesso bianco sui pannelli pubblicitari neri della metropolitana di New York: per Haring rappresenta l'innocenza pura e la speranza per il futuro.",
'A5': "Per questo la fotografia contemporanea perde la sua funzione puramente documentaria e diventa uno dei linguaggi dell'arte concettuale. Amazon, 2016, del fotografo tedesco Andreas Gursky, allievo della scuola di Düsseldorf di Bernd e Hilla Becher. Una fotografia digitale monumentale, ad altissima definizione: l'interno sterminato di un centro di distribuzione merci. Prospettiva zenitale, luce diffusa e fredda, accurata post-produzione digitale che corregge le distorsioni e mette a fuoco ogni singolo dettaglio. Lo spazio diventa un pattern geometrico, ipnotico e infinito. I milioni di pacchi perdono la loro individualità e diventano tessere di un mosaico, che visualizza l'iperconsumismo di massa, l'alienazione del lavoro contemporaneo e l'immensità logistica che governa il mondo globale.",
'A6': "Le Artistar sono artisti diventati celebrità globali, capaci di dialogare con l'industria dello spettacolo, la moda e i mercati finanziari. L.O.V.E., di Maurizio Cattelan, 2010. Si trova in Piazza degli Affari, a Milano, di fronte a Palazzo Mezzanotte, sede della Borsa. È un monumentale blocco di marmo bianco di Carrara, alto complessivamente 11 metri, compreso il basamento. Raffigura una mano protesa nel saluto fascista, ma Cattelan tronca tutte le dita, tranne il medio, che svetta verso l'alto. Il titolo è un acronimo ironico: libertà, odio, vendetta, eternità. Collocata in un'architettura di epoca fascista, l'opera è insieme una critica feroce ai totalitarismi del passato e un gesto di aperta ribellione contro il potere economico e le ipocrisie del capitalismo contemporaneo.",
'A7': "Il Centre Georges Pompidou di Parigi, progettato da Renzo Piano e Richard Rogers e inaugurato nel 1977, è il manifesto dell'architettura High-Tech, cioè dell'architettura che mostra la tecnologia. Piano e Rogers svuotano l'interno e portano sulla facciata esterna gli elementi portanti, le tubature e i sistemi di collegamento verticale. I tubi sono dipinti con colori primari, in base alla funzione: blu per l'aria condizionata, giallo per l'elettricità, verde per l'acqua, rosso per gli ascensori e le scale mobili. All'interno restano spazi espositivi immensi, fluidi e privi di pilastri portanti: il museo diventa una macchina culturale aperta, integrata nella vita della città. Nasce così la figura dell'architetto di fama internazionale, l'Archistar.",
}

# Pillole di ripasso: righe (schermo, in cifre); la voce le legge con i numeri in lettere
RIP = {
'A1': ["Dall'industria alla società dell'informazione, con la rivoluzione informatica e il World Wide Web.",
       "La globalizzazione interconnette mercati, culture e popoli.",
       "Nel 1989 cade il muro di Berlino; nel 1991 si scioglie l'Unione Sovietica.",
       "Nel 1979 Jean-François Lyotard teorizza la condizione postmoderna.",
       "Al rigore delle avanguardie si sostituiscono disincanto, ibridazione degli stili, citazione e ironia."],
'A2': ["Il postmoderno torna alla figurazione, in chiave ironica e disincantata.",
       "L'appropriazionismo mette in discussione originalità e unicità dell'opera.",
       "Levine fonde in bronzo lucido la fontana di Duchamp; Mueck crea un ragazzo iperrealista e monumentale.",
       "I fratelli Chapman e Marc Quinn portano sul corpo la provocazione biologica.",
       "Dagli anni Ottanta l'arte si apre alle culture non occidentali: da Les Magiciens de la terre a Fang Lijun e Yinka Shonibare."],
'A3': ["In Germania il neoespressionismo di Georg Baselitz e Anselm Kiefer indaga la memoria storica.",
       "Gerhard Richter esplora il rapporto ambiguo tra pittura e fotografia.",
       "In Italia la Transavanguardia, teorizzata da Achille Bonito Oliva nel 1979, è nomade ed eclettica.",
       "Chia cita la storia della pittura; Clemente unisce Occidente e Oriente.",
       "Mimmo Paladino recupera le radici mitiche del Mediterraneo."],
'A4': ["La graffiti art nasce a New York, sui vagoni dei treni e sui muri.",
       "Keith Haring unisce l'immediatezza della strada alla sensibilità della pop art.",
       "Il Tuttomondo, a Pisa nel 1989, è un inno alla vita, alla pace e alla solidarietà.",
       "Il Radiant Baby, il bambino radiante, simboleggia l'innocenza e la speranza.",
       "Basquiat è il primitivismo metropolitano; Banksy usa lo stencil per opere a sfondo sociale, politico e satirico."],
'A5': ["La fotografia contemporanea perde la funzione documentaria e diventa un linguaggio dell'arte concettuale.",
       "Andreas Gursky fotografa gli spazi del capitalismo globale; Cindy Sherman decostruisce gli stereotipi di genere.",
       "Shirin Neshat indaga la condizione della donna nel mondo musulmano post-rivoluzionario.",
       "La Video Art estende la ricerca allo spazio immersivo e al tempo: Bruce Nauman, Bill Viola, Matthew Barney."],
'A6': ["Nella globalizzazione alcuni artisti diventano celebrità globali: le Artistar.",
       "Jeff Koons eleva il kitsch e gli oggetti di consumo a icone d'arte museale.",
       "Anish Kapoor trasforma la scultura in una lente ottica: Cloud Gate, a Chicago.",
       "Maurizio Cattelan usa ironia e provocazione: La nona ora, del 1999, e L.O.V.E., del 2010, a Milano."],
'A7': ["Il Postmodernismo critica il rigido razionalismo moderno e recupera elementi storici in chiave ironica.",
       "Il Centre Georges Pompidou di Parigi, del 1977, è il manifesto dell'architettura High-Tech.",
       "Il Decostruttivismo frammenta le forme: il Guggenheim di Bilbao, di Frank O. Gehry, 1997, produce l'effetto Bilbao.",
       "Daniel Libeskind crea architetture emotive, come il Museo Ebraico di Berlino.",
       "Zaha Hadid, pioniera dell'architettura parametrica, progetta il MAXXI, il Museo nazionale delle arti del XXI secolo, a Roma."],
}

# Mappe del prof (parole sue; refusi corretti: «Graffity»->Graffiti, «Bansky»->Banksy, «Cyndi»->Cindy)
MAPPE = {
'MAP2': dict(domanda="Che cosa sono i graffiti e la Street Art?",
    nodi=[('top', "Graffiti e Street Art", 'centro'), ('l', "Basquiat: primitivismo metropolitano", 'chiave'), ('r', "Banksy: opere sfondo sociale, politico, satirico", 'chiave')],
    frecce=[(0,1),(0,2)]),
'MAP3': dict(domanda="Come cambiano fotografia, artista e architettura nell'arte globale?",
    nodi=[('a', "Fotografia, Video Art e nuovi media: Cindy Sherman, Shirin Neshat", 'centro'), ('b', "Artistar: artista società globale: Maurizio Cattelan", 'chiave'), ('c', "Archistar: Frank O. Gehry, Zaha Hadid", 'chiave')],
    frecce=[]),
'MAP1': dict(domanda="Che cosa sono la postmodernità e la globalizzazione?",
    nodi=[('top', "Postmodernità e globalizzazione", 'centro'), ('l', "Postmoderno: abbattimento delle barriere tra cultura alta e bassa", 'chiave'), ('c', "Neoespressionismo in Germania, Transavanguardia italiana", 'chiave'), ('r', "L'arte si apre a dimensioni globali non occidentali", 'chiave')],
    frecce=[(0,1),(0,2),(0,3)]),
}
MAPV = {
'MAP2': "Che cosa sono i graffiti e la Street Art? Al centro: Graffiti e Street Art. Da qui partono due rami. Primo ramo: Basquiat, primitivismo metropolitano. Secondo ramo: Banksy, opere a sfondo sociale, politico, satirico.",
'MAP3': "Come cambiano fotografia, artista e architettura nell'arte globale? Primo riquadro: Fotografia, Video Art e nuovi media, con Cindy Sherman e Shirin Neshat. Secondo riquadro: le Artistar, l'artista nella società globale, con Maurizio Cattelan. Terzo riquadro: le Archistar, con Frank O. Gehry e Zaha Hadid.",
'MAP1': "Che cosa sono la postmodernità e la globalizzazione? Al centro: Postmodernità e globalizzazione. Da qui partono tre rami. Primo ramo: il postmoderno, cioè l'abbattimento delle barriere tra cultura alta e bassa. Secondo ramo: il neoespressionismo in Germania e la Transavanguardia italiana. Terzo ramo: l'arte si apre a dimensioni globali, non occidentali.",
}

GLOSS = [
 ("Società postindustriale", "Il passaggio dalla produzione manifatturiera all'economia dei servizi e della società dell'informazione."),
 ("Globalizzazione", "Ha interconnesso mercati, culture e popoli, riducendo le distanze geografiche."),
 ("World Wide Web (WWW)", "La rete mondiale dei siti, che ha trasformato l'informazione nel bene immateriale più prezioso."),
 ("Postmoderno", "Il tramonto delle grandi narrazioni storiche e ideologiche: al loro posto disincanto, ibridazione degli stili, citazione e ironia."),
 ("Appropriazionismo", "Gli artisti si appropriano di opere del passato o di immagini di massa per metterne in discussione l'originalità e l'unicità."),
 ("Transavanguardia", "Movimento italiano teorizzato da Achille Bonito Oliva: un atteggiamento nomade ed eclettico, libero di attraversare tutti gli stili del passato."),
 ("Graffiti art", "Nasce a New York sui vagoni dei treni e sui muri: trasforma lo spazio urbano in espressione visiva e contestazione sociale."),
 ("Video Art", "Estende la ricerca artistica alle dimensioni dello spazio immersivo e del tempo."),
 ("Artistar", "Artisti che diventano celebrità globali, in dialogo con l'industria dello spettacolo, la moda e i mercati finanziari."),
 ("Archistar", "Architetto di fama internazionale."),
 ("High-Tech", "Architettura che porta in primo piano la tecnologia visibile, le strutture ingegneristiche e i materiali industriali lasciati scoperti."),
 ("Decostruttivismo", "Frammentazione delle forme, della simmetria e dei volumi tradizionali."),
 ("Architettura parametrica", "Usa algoritmi informatici complessi per generare forme fluide e continue."),
 ("Effetto Bilbao", "Una grande architettura può riqualificare un'intera città industriale in declino e farne una capitale culturale."),
]
def gloss_voce():
    out = ["Il glossario della lezione."]
    for t, d in GLOSS:
        t2 = t.replace('World Wide Web (WWW)', 'World Wide Web, in sigla WWW')
        out.append(f"{t2}. {d}")
    return ' '.join(out)

RF = [
 ("Il contesto globale", "dall'industria alla società dell'informazione, fino alla condizione postmoderna di Lyotard."),
 ("Arti figurative e dimensione globale", "il ritorno alla figurazione, l'appropriazionismo e l'apertura alle culture non occidentali."),
 ("Pittura in Germania e in Italia", "neoespressionismo tedesco e Transavanguardia italiana."),
 ("Graffiti e Street Art", "Keith Haring, Basquiat e Banksy."),
 ("Fotografia, Video Art e nuovi media", "linguaggi dell'arte concettuale e dello spazio immersivo."),
 ("Le Artistar", "sculture monumentali, ironia e provocazione."),
 ("L'architettura contemporanea", "High-Tech, Decostruttivismo e architettura parametrica delle Archistar."),
]
def rf_voce():
    n = ['Primo','Secondo','Terzo','Quarto','Quinto','Sesto','Settimo']
    return "Ripassiamo la lezione, argomento per argomento. " + ' '.join(f"{n[i]}: {t.lower() if False else t}, {d}" for i, (t, d) in enumerate(RF))

COMPITI = [
 "Analizza le trasformazioni storiche, tecnologiche, geopolitiche e culturali che definiscono la condizione postmoderna e la globalizzazione (dal passaggio alla società postindustriale fino alla caduta del Muro di Berlino e alla nascita del World Wide Web), spiegando come questi cambiamenti abbiano abbattuto le barriere tra cultura alta e bassa e aperto l'arte contemporanea ai mercati e alle culture non occidentali.",
 "Metti a confronto il ritorno alla pittura figurativa in Germania (Neoespressionismo di Georg Baselitz e Anselm Kiefer, e il realismo freddo di Gerhard Richter) con la Transavanguardia italiana teorizzata da Achille Bonito Oliva (soffermandoti sul citazionismo eclettico e sulle opere di Sandro Chia, Francesco Clemente e Mimmo Paladino), illustrando inoltre la nascita e i protagonisti della Street Art metropolitana (Keith Haring, Jean-Michel Basquiat e Banksy).",
 "Esamina l'evoluzione della fotografia concettuale, della Video Art e dei nuovi media tra fine Novecento e Duemila attraverso il lavoro di artisti come Robert Mapplethorpe, Andreas Gursky, Cindy Sherman, Shirin Neshat, Nam June Paik e Bill Viola, spiegando parallelamente il fenomeno delle \"Artistar\" e della spettacolarizzazione dell'arte in figure come Louise Bourgeois, Jeff Koons, Damien Hirst, Maurizio Cattelan e Anish Kapoor.",
 "Descrivi le principali tendenze dell'architettura contemporanea (Postmodernismo, linguaggio High-Tech e Decostruttivismo), illustrando come l'uso della tecnologia ingegneristica e dei software di progettazione digitale abbia trasformato l'edilizia monumentale nelle opere di grandi archistar internazionali quali Renzo Piano, Frank O. Gehry, Daniel Libeskind e Zaha Hadid.",
]
ORD = ['uno','due','tre','quattro']
COMPITI_FINALE = "Svolgi i compiti qui sotto e premi Consegna: arrivano al docente nel tuo quaderno dei compiti."
def compiti_voce():
    return ' '.join(f"Compito {ORD[i]}. {t}" for i, t in enumerate(COMPITI)) + ' ' + COMPITI_FINALE

BENVENUTO = "Benvenuti alla videolezione «Postmodernità e globalizzazione». Oggi ripercorriamo gli ultimi decenni dell'arte in sette argomenti. Il contesto globale e la condizione postmoderna. Il postmoderno nelle arti figurative e la dimensione globale. Il ritorno alla pittura in Germania e in Italia. Graffiti e Street Art. Fotografia, Video Art e nuovi media. L'artista nella società globale, le Artistar. Le ultime tendenze dell'architettura contemporanea. Cominciamo."
VER = "Per concludere, la verifica finale: servono almeno otto risposte giuste su dieci per superarla."

QUIZ = {
'A1': [
 ("Chi ha teorizzato la condizione postmoderna nel 1979?", "Jean-François Lyotard", ["Achille Bonito Oliva","Gerhard Richter","Keith Haring"]),
 ("Quale evento del 1989 segna la fine del mondo bipolare?", "La caduta del muro di Berlino", ["L'attacco alle Torri Gemelle","La nascita della Transavanguardia","Il saggio di Lyotard"]),
 ("In quale anno si scioglie l'Unione Sovietica?", "1991", ["1979","1989","2001"]),
 ("Che cosa sostituisce il rigore delle avanguardie nell'arte postmoderna?", "Il disincanto e l'ibridazione degli stili", ["Il rigore assiomatico e ideologico","La fiducia nel progresso lineare","Le grandi narrazioni"]),
 ("Che cos'è la società postindustriale?", "Una società in cui servizi e scambio di dati digitali prevalgono sulla manifattura", ["Una società basata sull'agricoltura","Una società basata sulla produzione industriale in serie","Una società senza tecnologia"]),
],
'A2': [
 ("Quale opera di Sherrie Levine riprende un'opera di Marcel Duchamp?", "Fountain (After Marcel Duchamp)", ["Untitled (Boy)","Self","Spring"]),
 ("In quale materiale Sherrie Levine fonde la sua Fountain?", "Bronzo lucido", ["Marmo bianco","Resina","Acciaio inossidabile"]),
 ("Chi ha realizzato Self, nel 1991, con il proprio sangue?", "Marc Quinn", ["Ron Mueck","Jake e Dinos Chapman","Fang Lijun"]),
 ("Quale mostra di Parigi, nel 1989, ha messo in dialogo arte occidentale e non occidentale?", "Les Magiciens de la terre", ["Sensation","Made in Heaven","Women of Allah"]),
 ("Che cosa ricostruisce Yinka Shonibare in Scramble for Africa?", "La conferenza di Berlino del 1884-1885, in cui le potenze europee si spartirono l'Africa", ["La caduta del muro di Berlino","La mostra di Parigi del 1989","I fatti di Piazza Tienanmen"]),
],
'A3': [
 ("Quale artista tedesco è noto per i dipinti «capovolti»?", "Georg Baselitz", ["Anselm Kiefer","Gerhard Richter","Sandro Chia"]),
 ("Chi ha teorizzato la Transavanguardia?", "Achille Bonito Oliva", ["Jean-François Lyotard","Francesco Clemente","Mimmo Paladino"]),
 ("Quale atteggiamento caratterizza la Transavanguardia?", "Nomade ed eclettico", ["Rigoroso e concettuale","Minimalista","Dogmatico"]),
 ("Quale opera è di Mimmo Paladino?", "La verità del fornaio in carrozza", ["Gioco di mano","Il cerchio di Milarepa","Fountain"]),
 ("Chi è Milarepa, a cui fa riferimento Francesco Clemente?", "Un asceta e poeta buddista tibetano", ["Un filosofo tedesco","Un critico d'arte italiano","Un pittore cinese"]),
],
'A4': [
 ("Dove nasce il movimento della graffiti art?", "A New York", ["A Pisa","A Parigi","A Berlino"]),
 ("Dove si trova il murale Tuttomondo di Keith Haring?", "A Pisa, sulla parete della chiesa di Sant'Antonio", ["A Milano","A Firenze","A Roma"]),
 ("Quante figure antropomorfe inserisce Haring nel Tuttomondo?", "Trenta", ["Dieci","Quattordici","Centosessantotto"]),
 ("Che cosa rappresenta il Radiant Baby, il bambino radiante?", "L'innocenza pura e la speranza per il futuro", ["La violenza della metropoli","Il potere economico","La memoria storica"]),
 ("Quale tecnica usa Banksy per le sue opere?", "Lo stencil", ["L'affresco","L'incisione","Il mosaico"]),
],
'A5': [
 ("Che cosa fotografa Andreas Gursky in Amazon?", "L'interno di un centro di distribuzione merci", ["Un ritratto in bianco e nero","Una città di notte","Un paesaggio naturale"]),
 ("Quale artista decostruisce gli stereotipi di genere con la serie Untitled Film Stills?", "Cindy Sherman", ["Shirin Neshat","Andreas Gursky","Bill Viola"]),
 ("Con quale scrittura sono ricoperte la pelle del volto nel ritratto di Shirin Neshat?", "Calligrafia farsi, con poesie persiane", ["Caratteri latini","Geroglifici","Graffiti"]),
 ("Chi ha creato l'installazione video Anthro/Socio, con la testa rotante?", "Bruce Nauman", ["Bill Viola","Matthew Barney","Andreas Gursky"]),
 ("Quale artista usa lo slow motion per mostrare un uomo che si tuffa e affonda lentamente?", "Bill Viola", ["Bruce Nauman","Matthew Barney","Cindy Sherman"]),
],
'A6': [
 ("Come si chiamano gli artisti diventati celebrità globali?", "Artistar", ["Archistar","Avanguardie","Appropriazionisti"]),
 ("Di quale materiale è fatta L.O.V.E. di Maurizio Cattelan?", "Marmo bianco di Carrara", ["Bronzo lucido","Acciaio inossidabile","Cera"]),
 ("Che cos'è Balloon Dog di Jeff Koons?", "Un cagnolino di palloncini in acciaio inossidabile con vernice magenta specchiante", ["Un busto in marmo bianco","Un dipinto a olio","Un'installazione video"]),
 ("Come chiamano affettuosamente Cloud Gate i cittadini di Chicago?", "The Bean, il fagiolo", ["The Dog","The Cloud","The Mirror"]),
 ("Chi raffigura La nona ora di Maurizio Cattelan?", "Papa Giovanni Paolo II", ["Un presidente","Un re","Un artista"]),
],
'A7': [
 ("Chi ha progettato il Centre Georges Pompidou di Parigi?", "Renzo Piano e Richard Rogers", ["Frank O. Gehry","Zaha Hadid","Daniel Libeskind"]),
 ("Di quale colore sono le tubature dell'acqua nel Pompidou?", "Verde", ["Blu","Giallo","Rosso"]),
 ("Quale materiale riveste il Museo Guggenheim di Bilbao?", "Lamine di titanio", ["Marmo bianco","Mattoni","Vetro e cemento"]),
 ("Che cos'è l'effetto Bilbao?", "Una grande architettura che riqualifica una città industriale in declino", ["Un software di progettazione","Un colore delle lamine","Un movimento artistico"]),
 ("Chi ha progettato il MAXXI di Roma?", "Zaha Hadid", ["Renzo Piano","Frank O. Gehry","Daniel Libeskind"]),
],
}

def testi_voci():
    L = [("BENVENUTO", BENVENUTO)]
    for a, _ in ARGOMENTI:
        L.append((f"{a}_APPROF", voce(AP[a])))
        L.append((f"{a}_RIPASSO", voce(' '.join(RIP[a]))))
    L += [("MAP2_STREETART", MAPV['MAP2']), ("MAP3_ARTISTAR_ARCHISTAR", MAPV['MAP3']), ("MAP1_FINALE", MAPV['MAP1']),
          ("GLOSSARIO", voce(gloss_voce())), ("RIPASSO_FINALE", voce(rf_voce())), ("VERIFICA", VER), ("COMPITI", voce(compiti_voce()))]
    return [{"nome": n, "testo": t} for n, t in L]

if __name__ == '__main__':
    T = testi_voci()
    for t in T:
        assert not re.search(r'\d', t['testo']), t['nome']
        print(t['nome'], len(t['testo'].split()), 'parole ~%d s' % (len(t['testo'].split()) / 2.6))
    json.dump(T, open('/home/user/w18/testi_voci.json', 'w'), ensure_ascii=False, indent=1)
    print(sum(len(t['testo'].split()) for t in T), 'parole totali')
