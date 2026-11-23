# Contenuti della lezione 6 · testi presi dalle slide del prof (LEZIONE 6.pdf) e dai tempi della sua trascrizione
TITOLO = "Simbolismo e Art Nouveau"
ARGOMENTI = [  # (titolo scheda, etichetta slide)
    ("Il Simbolismo e l'Art Nouveau", "Il contesto"),
    ("La stagione in Francia e in Belgio", "Francia e Belgio"),
    ("Vienna e la Secessione di Gustav Klimt", "La Secessione viennese"),
    ("Estetismo inglese, Glasgow e Modernismo catalano", "Gran Bretagna e Spagna"),
    ("Il Liberty in Italia e la Scuola di Chicago", "Italia e Chicago"),
]

# ------ cartelle delle immagini (ritagli) ------
IMG = {  # chiave: (file sorgente nel PDF, riquadro di ritaglio x0,y0,x1,y1 sull'originale, didascalia)
 'brasserie': ('i-001', (16, 2, 748, 432), "Brasserie Bouillon Julien, Parigi, aperta nel 1906, con arredi e decori Art Nouveau."),
 'metro': ('i-008', (11, 3, 483, 393), "Hector Guimard, pensilina della stazione metropolitana Hôtel de Ville, 1900, Parigi (ricollocata in Place des Abbesses nel 1974)."),
 'moreau': ('i-009', (9, 7, 513, 703), "Gustave Moreau, L'apparizione, 1874-76, olio su tela, 142 x 103 cm, Parigi, Musée Gustave Moreau."),
 'tassel': ('i-012', (6, 5, 406, 597), "Victor Horta, Casa Tassel, Bruxelles, scalone interno."),
 'secessione': ('i-015', (0, 3, 546, 366), "Joseph Maria Olbrich, Palazzo della Secessione, 1898, Vienna, esterno e particolare della decorazione sopra l'ingresso."),
 'bacio': ('i-017', (34, 3, 742, 711), "Gustav Klimt, Il bacio, 1907-08, olio su tela, 180 x 180 cm, Vienna, Österreichische Galerie Belvedere."),
 'giuditta': ('i-018', (13, 22, 275, 554), "Gustav Klimt, Giuditta I, 1901, olio e oro su tela, 84 x 42 cm, Vienna, Österreichische Galerie Belvedere."),
 'glasgow': ('i-021', (64, 0, 759, 350), "Charles Rennie Mackintosh, Scuola d'arte, 1897-1909, Glasgow (Regno Unito), esterno e ingresso."),
 'sagrada_aerea': ('i-025', (9, 21, 368, 352), "Antoni Gaudí, Sagrada Família, dal 1883, Barcellona, veduta aerea."),
 'sagrada_facciata': ('i-025', (104, 372, 368, 762), "Antoni Gaudí, Sagrada Família, dal 1883, Barcellona, facciata della Natività."),
 'batllo': ('i-026', (130, 18, 556, 766), "Antoni Gaudí, Casa Batlló, 1904-06, Barcellona."),
 'mila': ('i-027', (13, 2, 770, 599), "Antoni Gaudí, Casa Milà (La Pedrera), Barcellona."),
 'fenoglio': ('i-030', (2, 10, 439, 543), "Pietro Fenoglio, Palazzina Fenoglio (La Fleur), 1902, Torino."),
 'guaranty': ('i-033', (10, 9, 322, 468), "Louis Henry Sullivan, Prudential (Guaranty) Building, 1896, Buffalo (New York)."),
}

# ------ i 5 argomenti: pezzi del prof (tempi nel video originale, secondi) ------
# card: (etichetta, testo, secondo in cui il prof comincia a dirla | None)
C = lambda e, t, h=None: (e, t, h)
SL_INTRO = dict(title="Introduzione al Simbolismo e all'Art Nouveau", kw=["Crisi delle certezze", "Industrializzazione", "Nuova estetica"], cards=[
    C("Il contesto storico", "verso la fine del secolo, lo sviluppo industriale ed economico trasforma le strutture politiche e sociali delle borghesie urbane europee.", 358.2),
    C("La crisi delle certezze", "in questo periodo nasce una profonda crisi culturale legata alla perdita d'identità dei valori tradizionali e del vecchio mondo preindustriale.", 362.7),
    C("Una nuova estetica", "gli artisti e gli intellettuali sentono il bisogno di rinnovare gli ambienti della vita quotidiana e i linguaggi dell'arte, reagendo alle contraddizioni della modernità.", 392.0)])
SL_LETT_A = dict(title="Il Simbolismo e la letteratura decadente", kw=["Interiorità", "Sogno e fantasia", "Baudelaire", "Verlaine", "Mallarmé"], cards=[
    C("Focus sull'interiorità", "gli artisti rifiutano la semplice riproduzione della realtà per indagare la dimensione nascosta della natura, legata al sogno, alla fantasia e all'immaginario.", 410.7),
    C("Legame con la poesia", "il movimento è strettamente unito alla letteratura decadente di Baudelaire, Verlaine e Mallarmé, che usano la sinestesia per evocare misteriose corrispondenze.", 434.9)])
SL_LETT_B = dict(title="Il Simbolismo e la letteratura decadente", kw=["Ambiguità", "Anti-razionalismo", "Reazione al Positivismo"], cards=[
    C("L'estetica dell'ambiguità", "l'arte simbolista elabora linguaggi ricchi di suggestioni, forme indefinite ed evocatrici con caratteristiche ricercate e preziose.", 439.5),
    C("Reazione al Positivismo", "il Simbolismo si definisce come una reazione idealista, spiritualista e anti-razionalista contro il materialismo della società e della scienza.", 442.8)])
SL_ART = dict(title="L'Art Nouveau e la vita moderna", kw=["Opera d'arte totale", "Omologazione", "Linea sinuosa", "Motivi floreali"], cards=[
    C("Riscatto dall'omologazione", "nasce per qualificare esteticamente ogni aspetto della vita moderna, opponendosi alla bruttezza dei prodotti industriali di massa.", 476.2),
    C("Il concetto di «opera d'arte totale»", "architetti e progettisti non rinunciano ai materiali industriali, ma li integrano in un progetto unitario che coordina la struttura, gli arredi e i decori.", 482.9),
    C("Ispirazione naturale", "lo stile si distingue per l'uso della «linea frustata» o sinuosa, applicando motivi floreali, animali o geometrici astratti a oggetti d'uso e architetture.", 549.0)])

SL_FR_A = dict(title="La stagione in Francia", kw=["Parigi", "Moreau e Redon", "Nabis"], cards=[
    C("Parigi al centro del dibattito", "la capitale francese accoglie le prime generazioni di artisti simbolisti e post-impressionisti che fuggono dalla mondanità urbana.", 562.7),
    C("Gustave Moreau e Odilon Redon", "Moreau indaga il mito della femme fatale e l'erotismo ambiguo con decorazioni preziose; Redon esplora il mondo interno e l'inconscio tramite disegni e incisioni visionarie.", 569.9)])
SL_FR_B = dict(title="La stagione in Francia", kw=["Nabis", "Puvis de Chavannes", "Hector Guimard", "Ghisa"], cards=[
    C("I Nabis e Pierre Puvis de Chavannes", "il gruppo dei Nabis propone una pittura decorativa basata su colori puri e piatti; Puvis de Chavannes influenza la generazione simbolista con la sua pittura murale monumentale.", 582.3),
    C("L'architettura di Hector Guimard", "Guimard applica il nuovo stile alle facciate e ai famosi ingressi della metropolitana parigina, usando forme organiche in ferro battuto ispirate al mondo vegetale e marino.", 603.0)])
SL_BE_A = dict(title="Il Simbolismo e l'Art Nouveau in Belgio", kw=["Bruxelles", "Società dei XX", "Émile Gallé"], cards=[
    C("Bruxelles e la Società dei XX", "la città diventa un centro d'avanguardia dinamico grazie all'attività di gruppi artistici che promuovono le ricerche più innovative.", 878.9),
    C("Le arti applicate", "Émile Gallé sperimenta nel settore del vetro con i suoi vasi fioriti dai colori sfumati, mentre René Lalique crea gioielli fantastici unendo l'oreficeria a forme animali e femminili.", 900.5)])
SL_BE_B = dict(title="Il Simbolismo e l'Art Nouveau in Belgio", kw=["Victor Horta", "Casa Tassel", "Ferro e ghisa a vista"], cards=[
    C("Le innovazioni di Victor Horta", "Horta rivoluziona l'architettura residenziale con capolavori come Casa Tassel, dove integra ferro e ghisa a vista per creare scaloni aerei e decorazioni sinuose.", 917.9)])
CARD_LUCE = C("La luce e lo spazio", "nei progetti di Horta, la luce naturale penetra attraverso lucernari e ampie vetrate, valorizzando la continuità visiva tra interni ed esterni.", 963.3)

SL_VI_A = dict(title="Vienna e la Secessione di Gustav Klimt", kw=["Secessione", "1897", "Gustav Klimt"], cards=[
    C("La rottura del 1897", "un gruppo di artisti guidati da Klimt si separa dalle istituzioni ufficiali per rinnovare la cultura austriaca e collegarsi alle avanguardie europee.", 1117.9)])
SL_HO_A = dict(title="Hoffmann, Palazzo Stoclet e la reazione di Loos", kw=["Wiener Werkstätte", "Hoffmann e Moser", "Palazzo Stoclet", "Opera d'arte totale"], cards=[
    C("Le Officine viennesi", "fondate da Hoffmann e Moser nel 1903, producono arredi e gioielli che uniscono la tradizione artigianale all'uso dei macchinari industriali.", 1153.6),
    C("Palazzo Stoclet a Bruxelles", "considerato il capolavoro della cultura secessionista, è un'opera d'arte totale in cui ogni dettaglio, dalle luci ai mosaici di Klimt nella sala da pranzo, è coordinato.", 1197.5)])
SL_HO_B = dict(title="Hoffmann, Palazzo Stoclet e la reazione di Loos", kw=["Adolf Loos", "Ornamento", "Villa Steiner", "Funzionalità"], cards=[
    C("Adolf Loos e l'architettura pura", "in netta opposizione alla Secessione, Loos sostiene che l'ornamento sia un inutile spreco di forza lavoro e denaro.", 1241.2),
    C("La funzionalità", "con opere come Villa Steiner, Loos anticipa l'architettura moderna, eliminando le decorazioni dalle facciate per concentrarsi sui volumi e sulla qualità dei materiali.", 1259.8)])
CARD_SECESS = C("Il Palazzo della Secessione", "progettato da Joseph Maria Olbrich, l'edificio è un blocco squadrato sormontato da una cupola di foglie di alloro in bronzo, simbolo del movimento.", 1330.0)
SL_VI_B = dict(title="Vienna e la Secessione di Gustav Klimt", kw=["Fregio di Beethoven", "Figure femminili", "Giuditta I", "Il bacio"], cards=[
    C("Il Fregio di Beethoven", "realizzato da Klimt all'interno del Palazzo, rappresenta il percorso dell'umanità verso la felicità attraverso l'arte e la musica, con l'uso di ricchi inserti dorati.", 1388.2),
    C("Le figure femminili", "nella pittura di Klimt, come in «Giuditta I» e nel «Ritratto di Adele Bloch-Bauer», domina la donna tra erotismo e rigore geometrico-decorativo, azzerando la profondità dello spazio.", 1418.6)])

SL_GL_A = dict(title="L'Estetismo inglese e la Scuola di Glasgow", kw=["Estetismo", "Arts and Crafts", "Aubrey Beardsley", "Stampe giapponesi"], cards=[
    C("Il culto della bellezza", "in Inghilterra l'estetismo e il movimento «Arts and Crafts» cercano la bellezza pura come antidoto all'alienazione della moderna vita industriale.", 1639.5),
    C("La grafica di Aubrey Beardsley", "personaggio emblematico del Decadentismo, realizza illustrazioni lineari e stilizzate in bianco e nero, fortemente influenzate dalle stampe giapponesi.", 1655.9)])
SL_GL_B = dict(title="L'Estetismo inglese e la Scuola di Glasgow", kw=["I Quattro di Glasgow", "Mackintosh", "Scuola d'arte", "Linee geometriche"], cards=[
    C("I Quattro di Glasgow", "in Scozia, il gruppo guidato da Charles Rennie Mackintosh e Margaret Macdonald introduce una nuova qualità estetica geometrica negli ambienti urbani.", 1672.7),
    C("La Scuola d'arte di Glasgow", "progettata da Mackintosh, la scuola unisce rigore geometrico e funzionalità, con arredi in legno dominati da linee semplici e decorazioni incise.", 1690.0)])
SL_GA_A = dict(title="Il Modernismo catalano e Antoni Gaudí", kw=["Modernismo catalano", "Barcellona", "Antoni Gaudí", "Forme organiche"], cards=[
    C("Il Rinascimento catalano", "Barcellona vive una forte crescita economica e culturale, manifestando il desiderio di autonomia da Madrid attraverso l'architettura modernista.", 1808.6),
    C("Antoni Gaudí e la genialità delle forme", "Gaudí unisce il fervore religioso a una straordinaria carica espressiva, creando forme curve e scheletri strutturali complessi.", 1833.1)])
CARD_SAGRADA = C("La Sagrada Família", "un cantiere infinito iniziato nel 1883, concepito come una cattedrale gotica ripensata attraverso una complessa rete di archi parabolici e sculture organiche.", 1858.0)
CARD_RESID = C("Le residenze urbane", "opere come Casa Batlló e Casa Milà si distinguono per le facciate mosse da balaustre metalliche, tetti coperti da scaglie ceramiche e l'assenza di linee rette negli interni.", 1977.8)

SL_IT_A = dict(title="Il Simbolismo e lo Stile Liberty in Italia", kw=["Liberty", "Stile floreale", "Torino 1902", "Segantini"], cards=[
    C("Il Liberty italiano", "conosciuto anche come stile floreale, si afferma a livello nazionale trovando un momento di massima visibilità nell'Esposizione internazionale di Torino del 1902.", 2149.0),
    C("Giovanni Segantini e il Divisionismo", "nel campo della pittura, Segantini unisce la tecnica divisionista a visioni simboliste, trattando temi universali e spirituali legati alla natura e alla maternità.", 2168.7)])
SL_IT_B = dict(title="Il Simbolismo e lo Stile Liberty in Italia", kw=["Sommaruga", "Palazzo Castiglioni", "Ernesto Basile", "Villa Igea"], cards=[
    C("Milano e Torino protagoniste", "Giuseppe Sommaruga progetta Palazzo Castiglioni a Milano con decorazioni esuberanti e finestre a nastro, mentre a Torino si distingue la Palazzina Fenoglio-Lafleur.", 2195.0),
    C("Ernesto Basile a Palermo", "l'architetto esprime lo stile Liberty nel Sud Italia attraverso opere come Villa Igea, unendo il gusto floreale a un linguaggio eclettico e mediterraneo.", 2205.8)])
SL_CH_A = dict(title="La Scuola di Chicago e la nascita del grattacielo", kw=["Incendio del 1871", "Gabbia metallica", "Ascensore"], cards=[
    C("Il contesto americano", "Chicago viene colpita da un devastante incendio nel 1871; la ricostruzione e la crescita urbana portano alla nascita di una nuova tipologia edilizia: il grattacielo.", 2316.0),
    C("Struttura tecnologica", "utilizzo di una gabbia metallica interna in ferro e cemento, ascensori elettrici e ampie superfici vetrate.", 2329.3)])
SL_CH_B = dict(title="La Scuola di Chicago e la nascita del grattacielo", kw=["Louis Sullivan", "La forma segue la funzione", "Terracotta"], cards=[
    C("Louis Sullivan", "architetto chiave che teorizza che «la forma segue la funzione», integrando la struttura geometrica dell'edificio con decorazioni geometriche e naturalistiche in terracotta (es. «Guaranty Building» e «Prudential Building»).", 2347.6)])

# scene: ('cards', slide, t_inizio) | ('img', [chiavi], t_inizio, card|None) ; t in secondi del video originale
PEZZI_PROF = {
 'T1': dict(c0=254.1, c1=557.95, s0=254.7, s1=557.7, label="01 · Il contesto", scene=[('img', ['brasserie'], 254.7, None), ('cards', SL_INTRO, 355.0), ('cards', SL_LETT_A, 408.0), ('cards', SL_LETT_B, 439.0), ('cards', SL_ART, 475.7)]),
 'T2': dict(c0=558.2, c1=1047.6, s0=558.6, s1=1047.1, label="02 · Francia e Belgio", scene=[('cards', SL_FR_A, 558.6), ('cards', SL_FR_B, 582.0), ('img', ['moreau'], 619.1, None), ('img', ['metro'], 712.0, None), ('cards', SL_BE_A, 831.0), ('cards', SL_BE_B, 917.0), ('img', ['tassel'], 945.2, CARD_LUCE)]),
 'T3': dict(c0=1047.65, c1=1629.6, s0=1048.3, s1=1629.2, label="03 · La Secessione viennese", scene=[('cards', SL_VI_A, 1048.3), ('cards', SL_HO_A, 1153.4), ('cards', SL_HO_B, 1241.0), ('img', ['secessione'], 1291.3, CARD_SECESS), ('cards', SL_VI_B, 1386.0), ('img', ['bacio'], 1439.0, None), ('img', ['giuditta'], 1530.0, None)]),
 'T4': dict(c0=1629.35, c1=2140.9, s0=1629.9, s1=2140.4, label="04 · Gran Bretagna e Spagna", scene=[('cards', SL_GL_A, 1629.9), ('cards', SL_GL_B, 1672.0), ('img', ['glasgow'], 1693.9, None), ('cards', SL_GA_A, 1773.0), ('img', ['sagrada_aerea', 'sagrada_facciata'], 1855.0, CARD_SAGRADA), ('img', ['batllo'], 1977.0, CARD_RESID), ('img', ['mila'], 2056.0, None)]),
 'T5': dict(c0=2141.45, c1=2472.3, s0=2142.0, s1=2471.8, label="05 · Italia e Chicago", scene=[('cards', SL_IT_A, 2142.0), ('cards', SL_IT_B, 2189.0), ('img', ['fenoglio'], 2217.0, None), ('cards', SL_CH_A, 2300.5), ('cards', SL_CH_B, 2345.0), ('img', ['guaranty'], 2365.5, None)]),
}
KW_NOTE = "parole chiave: massimo 5"

# ------ approfondimenti Kore: immagine + punti che compaiono con la frase ------
APPROF = {
 'A1': dict(voce='A1_APPROF', titolo="L'opera d'arte totale", img=['brasserie'], punti=[
    ("Struttura, arredi e decori in un unico progetto coerente", 3), ("Il contrario della fabbrica: non si riproduce in serie per le masse", 4),
    ("Brasserie Bouillon Julien, Parigi, 1906", 5), ("Architetti, ebanisti del legno e artigiani collaborano", 6), ("Linea sinuosa e motivi floreali, animali o geometrici", 8)]),
 'A2': dict(voce='A2_APPROF', titolo="Casa Tassel, Bruxelles", img=['tassel'], punti=[
    ("Victor Horta, 1893, lotto stretto e profondo", 2), ("Bovindo vetrato: la luce entra negli interni", 3), ("Ferro a vista, non nascosto nei muri", 4),
    ("Architettura e ornamento fusi nello scalone", 5), ("Colonna in ghisa: prima volta in una casa borghese", 6), ("Balaustra in ferro battuto a colpo di frusta", 7)]),
 'A3': dict(voce='A3_APPROF', titolo="Il bacio, di Gustav Klimt", img=['bacio'], punti=[
    ("1907-1908, periodo d'oro dell'artista", 2), ("Fondo oro di memoria bizantina", 3), ("Prato fiorito, come negli arazzi tardo medievali", 4),
    ("Lui: rettangoli bianchi e neri. Lei: cerchi e fiori", 5), ("Tempo assoluto: Simbolismo con elementi Art Nouveau", 7)]),
 'A4': dict(voce='A4_APPROF', titolo="La Sagrada Família, Barcellona", img=['sagrada_facciata'], punti=[
    ("Antoni Gaudí la dirige dal 1883", 2), ("Croce latina, cinque navate", 4), ("Tre facciate e dodici torri: una per ogni apostolo", 4),
    ("Facciata della Natività: rocce, stalattiti, fondali marini", 5), ("Albero della vita in pietra, con colombe bianche", 6), ("Navata alta 45 metri, pilastri come rami di foresta", 7)]),
 'A5': dict(voce='A5_APPROF', titolo="Il Guaranty Building, Buffalo", img=['guaranty'], punti=[
    ("1896: la forma segue la funzione", 1), ("Scomposizione tripartita", 2), ("Basamento con vetrate: negozi e pubblico", 3),
    ("Corpo centrale: piani identici, uffici", 4), ("Cornicione: impianti tecnici", 5), ("Terracotta con cerchi, quadrati e foglie d'acanto", 6)]),
}

# ------ pillole di ripasso: 1 frase di schermo per ogni frase della voce ------
PILLOLE = {
 'R1': dict(voce='R1_RIPASSO', titolo="Il contesto", righe=["Il Simbolismo reagisce al Positivismo.", "Guarda all'interiorità, al sogno e all'immaginario.", "È legato alla poesia di Baudelaire, Verlaine e Mallarmé.", "L'Art Nouveau vuole riscattare ogni aspetto della vita quotidiana.", "Il suo ideale è l'opera d'arte totale."]),
 'R2': dict(voce='R2_RIPASSO', titolo="Francia e Belgio", righe=["Parigi accoglie i primi simbolisti: Moreau, Redon e i Nabis.", "Guimard disegna le entrate della metropolitana di Parigi, in ghisa e con forme floreali.", "A Bruxelles, Horta porta ferro e ghisa a vista nelle case borghesi.", "Casa Tassel è il manifesto della sua architettura.", "La linea a colpo di frusta unisce architettura e ornamento."]),
 'R3': dict(voce='R3_RIPASSO', titolo="La Secessione viennese", righe=["Nel 1897 un gruppo di artisti guidato da Klimt fonda la Secessione viennese.", "Il Palazzo della Secessione è opera di Olbrich.", "Hoffmann e Moser fondano nel 1903 le Wiener Werkstätte.", "Klimt unisce Simbolismo e Art Nouveau, come nel Bacio e in Giuditta.", "Loos, con Villa Steiner, rifiuta l'ornamento."]),
 'R4': dict(voce='R4_RIPASSO', titolo="Gran Bretagna e Spagna", righe=["L'estetismo inglese cerca la bellezza pura, contro l'alienazione della vita industriale.", "Aubrey Beardsley disegna in bianco e nero, con linee sinuose.", "Mackintosh guida i Quattro di Glasgow e progetta la Scuola d'arte di Glasgow.", "In Catalogna, Gaudí crea forme curve e organiche.", "Sagrada Família, Casa Batlló e Casa Milà sono le sue opere."]),
 'R5': dict(voce='R5_RIPASSO', titolo="Italia e Chicago", righe=["In Italia l'Art Nouveau si chiama Liberty, o stile floreale.", "Segantini e Previati sono i pittori del Divisionismo.", "Sommaruga, Basile e Fenoglio progettano Palazzo Castiglioni, Villa Igea e la Palazzina Fenoglio-Lafleur.", "A Chicago, dopo l'incendio del 1871, nasce il grattacielo.", "Per Sullivan, la forma segue la funzione."]),
}

GLOSSARIO = [  # (termine, definizione) nell'ordine della voce
 ("Simbolismo", "Reazione idealista, spiritualista e anti-razionalista al materialismo positivista: cerca la dimensione nascosta della natura, legata al sogno e alla fantasia."),
 ("Art Nouveau (arte nuova)", "Movimento che vuole riscattare ogni aspetto della vita quotidiana, con linee curve e motivi floreali."),
 ("Opera d'arte totale", "Un progetto unitario che coordina la struttura, gli arredi e i decori."),
 ("Arts and Crafts", "Movimento inglese che cerca di conciliare la produzione industriale con l'arte."),
 ("Secessione", "La rottura del 1897: un gruppo di artisti guidato da Klimt si separa dalle istituzioni ufficiali."),
 ("Femme fatale", "La donna alla quale non si può sfuggire, per la sua bellezza."),
 ("Liberty", "Il nome italiano dell'Art Nouveau, detto anche stile floreale."),
 ("Divisionismo", "Tecnica a filamenti colorati, usata da Segantini e da Previati."),
 ("Grattacielo", "Edificio alto, con una gabbia metallica in ferro e cemento e l'ascensore di sicurezza."),
 ("Linea a colpo di frusta", "L'andamento sinuoso dei ferri battuti, tipico di Horta."),
]
GLOSS_FRASI = ["Glossario.", "Simbolismo", "Art Nouveau", "Opera d'arte totale", "Arts and Crafts", "Secessione", "Femme fatale", "Liberty", "Divisionismo", "Grattacielo", "Linea a colpo di frusta"]
RIPASSO_FINALE = [  # (titolo, testo) per ogni argomento, ordine della voce
 ("Il contesto", "Il Simbolismo reagisce al Positivismo e guarda al sogno e all'interiorità. L'Art Nouveau vuole l'opera d'arte totale."),
 ("Francia e Belgio", "In Francia, Guimard disegna la metropolitana di Parigi. In Belgio, Horta costruisce Casa Tassel, con il ferro a vista."),
 ("La Secessione viennese", "A Vienna, nel 1897, nasce la Secessione di Gustav Klimt. Hoffmann realizza Palazzo Stoclet, mentre Loos rifiuta l'ornamento."),
 ("Gran Bretagna e Spagna", "In Gran Bretagna ci sono Beardsley e Mackintosh. In Spagna, Gaudí firma la Sagrada Família, Casa Batlló e Casa Milà."),
 ("Italia e Chicago", "In Italia nasce lo stile Liberty. A Chicago nasce il grattacielo, e per Sullivan la forma segue la funzione."),
]
COMPITI = [
 "Analizza il contesto storico e culturale di fine Ottocento in cui si sviluppano il Simbolismo e l'Art Nouveau, spiegando i caratteri della reazione simbolista al Positivismo (inclusi il legame con la letteratura decadente e i principali esponenti francesi come Moreau, Redon e i Nabis) e il significato del concetto di «opera d'arte totale» nell'Art Nouveau.",
 "Confronta le diverse interpretazioni dell'Art Nouveau in Europa attraverso l'opera dei suoi maggiori protagonisti: Hector Guimard in Francia, Victor Horta e gli artisti delle arti applicate in Belgio, Charles Rennie Mackintosh nella Scuola di Glasgow e Antoni Gaudí nel Modernismo catalano.",
 "Illustra la nascita e gli sviluppi della Secessione viennese guidata da Gustav Klimt, soffermandoti sull'architettura del Palazzo della Secessione, sulle caratteristiche stilistiche e simboliche dei suoi dipinti, sulla realizzazione di Palazzo Stoclet e sulla successiva reazione anti-ornamentale di Adolf Loos.",
 "Esamina la diffusione dello Stile Liberty e del Simbolismo in Italia (tra pittura divisionista e architettura a Torino, Milano e Palermo) e metti a confronto l'estetica floreale europea con la nascita del grattacielo nella Scuola di Chicago, spiegando le innovazioni tecnologiche e il principio teorico formulato da Louis Sullivan.",
]
