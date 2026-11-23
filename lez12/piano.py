# Piano di montaggio Storia dell'arte V · Lezione 12 · «Dadaismo e Surrealismo»
# Tempi (secondi) = originale del docente, presi dalla trascrizione (taglio sempre a fine frase).
TITOLO = "Dadaismo e Surrealismo"
OPERE = '/home/user/Lezioni/lavoro/opere_hd/'
ARGO = {1: "I folli anni Venti", 2: "Il Dadaismo e Marcel Duchamp", 3: "Il Surrealismo e gli oggetti surrealisti", 4: "Ernst, Miró, Dalí e Magritte"}
EYEB = {0: '', 1: '01 · I folli anni Venti', 2: '02 · Il Dadaismo e Marcel Duchamp', 3: '03 · Il Surrealismo', 4: '04 · Ernst, Miró, Dalí e Magritte'}
# ---------------- slide di testo del docente (card = frasi intere, refusi corretti) ----------------
def B(a, b): return f'<b>{a}</b>: {b}'
SL = {
 'S1a': (1, 'Il contesto dei “folli anni Venti”', [
    B('Nascita dei movimenti', 'si sviluppano nel Primo Dopoguerra tra Zurigo, Parigi e New York.'),
    B('Spirito di rottura', "nascono in aperta contrapposizione all'ideologia borghese e capitalista che aveva portato alla guerra.")],
    ['Primo Dopoguerra', 'Zurigo, Parigi, New York', 'Spirito di rottura']),
 'S1b': (1, 'Il contesto dei “folli anni Venti”', [
    B("Contro il mercato dell'arte", 'rifiutano le gallerie tradizionali e i collezionisti “speculatori”, cercando canali alternativi e indipendenti.'),
    B('Nuovi spazi culturali', 'la vita notturna si sposta in locali anticonformisti, caffè e club, che diventano i nuovi punti di ritrovo per gli artisti.')],
    ["Mercato dell'arte", 'Caffè e club', 'Vita notturna']),
 'S2a': (2, 'La Rivoluzione del Dadaismo', [
    B("L'unica regola", 'la regola fondamentale è non avere regole e rifiutare ogni valore precostituito.'),
    B('La nascita a Zurigo', 'il movimento decolla nel 1916 al Cabaret Voltaire per iniziativa di intellettuali rifugiati in Svizzera.')],
    ['Zurigo 1916', 'Cabaret Voltaire', 'Nessuna regola']),
 'S2b': (2, 'La Rivoluzione del Dadaismo', [
    B('Il nome <i>“Dada”</i>', 'una parola senza senso, scoperta per caso sul dizionario, scelta proprio per valorizzare il nonsenso e l’irrazionalità.'),
    B('Il Manifesto di Tzara', "spiega che Dada non significa nulla e che l'arte deve essere un atto di indipendenza e rivolta.")],
    ['Dada', 'Tristan Tzara', 'Irrazionalità']),
 'S3': (2, 'Le tecniche dadaiste e il caso', [
    B('La legge del caso', 'Jean Arp affida la composizione dei suoi collage alla casualità, strappando e lasciando cadere i pezzi di carta.'),
    B('Dada in Germania', "a Berlino il movimento assume un forte tono politico, diventando uno strumento di satira e contestazione sociale."),
    B('Il fotomontaggio', 'inventato dai dadaisti tedeschi, combina ritagli di giornali e foto per svelare in modo ironico le contraddizioni della società.')],
    ['Jean Arp', 'Legge del caso', 'Fotomontaggio']),
 'S4a': (2, 'Marcel Duchamp e i Ready-Made', [
    B('Provocazione totale', "Duchamp distrugge l'estetica tradizionale dimostrando che l'arte è prima di tutto un'operazione mentale."),
    B('Il concetto di <i>Ready-Made</i>', 'significa “pronto all’uso” e consiste nel sottrarre un oggetto comune dal suo contesto quotidiano per esporlo come opera d’arte.')],
    ['Ready-Made', 'Operazione mentale']),
 'S4b': (2, 'Marcel Duchamp e i Ready-Made', [
    B("Il valore dell'idea", "l'artista non crea l'oggetto con le proprie mani, ma lo “sceglie”, spostando il valore dall'abilità manuale al pensiero."),
    B('Opere simbolo', 'lo <i>Scolabottiglie</i> (arte allo stato puro) e la celebre <i>Fontana</i>, un orinatoio capovolto firmato con uno pseudonimo.')],
    ['Scolabottiglie', 'Fontana']),
 'S5a': (3, "Il Surrealismo e l'Inconscio", [
    B('La fondazione', 'nasce ufficialmente a Parigi nel 1924 con la pubblicazione del Manifesto scritto da André Breton.'),
    B('La teoria di base', "si ispira alla psicoanalisi di Freud, mettendo al centro il sogno, l'irrazionalità e l'esplorazione dell'inconscio.")],
    ['Parigi 1924', 'André Breton', 'Freud']),
 'S5b': (3, "Il Surrealismo e l'Inconscio", [
    B("L'automatismo psichico", 'una tecnica (usata anche nella scrittura) per esprimere il pensiero puro, libero dal controllo della ragione o di freni morali.'),
    B('La Surrealtà', 'definita come una realtà superiore, nata dalla fusione armonica tra la dimensione del sogno e quella della veglia.')],
    ['Automatismo psichico', 'Surrealtà']),
 'S6': (3, 'Gli oggetti surrealisti', [
    B('Funzionamento simbolico', 'sono oggetti quotidiani scelti, modificati e assemblati per attivare desideri o impulsi nascosti.'),
    B("L'effetto perturbante", 'gli accostamenti insoliti e contrari alla logica creano nello spettatore un senso di shock e profondo disagio.'),
    B('Esempi iconici', 'il <i>Telefono aragosta</i> di Salvador Dalí e la celebre tazza rivestita di pelliccia (<i>Colazione in pelliccia</i>) di Meret Oppenheim.')],
    ['Oggetti surrealisti', 'Effetto perturbante', 'Telefono aragosta']),
 'S7': (4, "L'immaginario di Max Ernst e Joan Miró", [
    B('Il frottage di Ernst', 'tecnica dello sfregamento (es. grafite su carta sopra una superficie ruvida) usata per stimolare immagini allucinatorie e inconsce.'),
    B("L'elefante di Celebes", "un'opera di Ernst in cui la tecnica del collage viene portata in pittura, creando un mostruoso e assurdo incrocio tra una bestia e una macchina."),
    B('Il biomorfismo di Miró', 'un linguaggio fantastico popolato da forme geometriche e organiche, che sembrano fluttuare liberamente nello spazio.')],
    ['Frottage', 'Biomorfismo', 'Max Ernst', 'Joan Miró']),
 'S8': (4, 'Il metodo paranoico-critico di Dalí', [
    B('Il metodo', 'una tecnica basata sulla razionalizzazione guidata di immagini deliranti, illusioni ottiche e ossessioni profonde.'),
    B('La persistenza della memoria', 'celebre dipinto ambientato in un paesaggio deserto e surreale, dominato dalla presenza di orologi deformati.'),
    B('Gli orologi molli', 'diventano il simbolo della relatività del tempo e della deformazione psicologica della durata delle cose.')],
    ['Metodo paranoico-critico', 'Orologi molli']),
 'S9': (4, 'René Magritte: parole e illusioni', [
    B('Convenzionalità del linguaggio', 'Magritte indaga sul rapporto ambiguo tra le parole, le immagini dipinte e gli oggetti reali.'),
    B('Il tradimento delle immagini', "nel quadro <i>Ceci n'est pas une pipe</i>, l'artista ricorda che l'immagine di una pipa non è l'oggetto reale che si può fumare."),
    B('La condizione umana', 'gioco concettuale del “quadro nel quadro” applicato a una finestra, dove la finzione dipinta e la realtà coincidono perfettamente, dimostrando che ciò che consideriamo realtà è solo una nostra rappresentazione interna.')],
    ['Parole e immagini', 'Quadro nel quadro']),
}
# ---------------- schermate con le opere: (argo, titolo, [(file, x,y,w,h, didascalia)]) ----------------
def C(a, b=''): return f'<b>{a}</b>' + (f'<small>{b}</small>' if b else '')
IM = {
 'I_duch': (2, 'Opere dadaiste di Marcel Duchamp', [
    (OPERE+'duchamp_ruota.png', 80, 330, 300, 420, ''), (OPERE+'scolabottiglie.png', 410, 330, 280, 420, ''),
    (OPERE+'fontana.png', 720, 330, 420, 420, ''), (OPERE+'monnalisa.png', 1170, 330, 215, 420, '')]),
 'I_ruota': (2, 'Ruota di bicicletta', [(OPERE+'duchamp_ruota.png', 80, 310, 1305, 520, C('Marcel Duchamp · Ruota di bicicletta', '1913 · ready-made rettificato'))]),
 'I_lhooq': (2, 'L.H.O.O.Q.', [(OPERE+'monnalisa.png', 80, 310, 1305, 520, C('Marcel Duchamp · L.H.O.O.Q.', 'Le cinque lettere, lette in francese, formano un gioco di parole · 1919'))]),
 'I_scola': (2, 'Scolabottiglie', [(OPERE+'scolabottiglie.png', 80, 310, 1305, 520, C('Marcel Duchamp · Scolabottiglie', '1914 · ready-made allo stato puro'))]),
 'I_fontana': (2, 'Fontana', [(OPERE+'fontana.png', 80, 310, 1305, 520, C('Marcel Duchamp · Fontana', '1917 · firmata con lo pseudonimo R. Mutt'))]),
 'I_telaz': (3, 'Gli oggetti surrealisti', [
    (OPERE+'telefono.png', 80, 330, 620, 480, C('Salvador Dalí · Telefono aragosta')), (OPERE+'tazza.png', 740, 330, 620, 480, C('Meret Oppenheim · Colazione in pelliccia'))]),
 'I_tel': (3, 'Telefono aragosta', [(OPERE+'telefono.png', 80, 310, 1305, 520, C('Salvador Dalí · Telefono aragosta', 'Materiali vari · Londra, Tate Modern'))]),
 'I_taz': (3, 'Colazione in pelliccia', [(OPERE+'tazza.png', 80, 310, 1305, 520, C('Meret Oppenheim · Colazione in pelliccia', 'Pelliccia, tazza, piattino e cucchiaio · New York, Museum of Modern Art'))]),
 'I_angelo': (4, "L'angelo del focolare", [(OPERE+'angelo.png', 80, 310, 1305, 520, C('Max Ernst · L’angelo del focolare', '1937 · olio su tela, 114 × 146 cm · Collezione privata'))]),
 'I_miro': (4, 'Joan Miró · Costellazioni', [
    (OPERE+'miro_a.png', 80, 320, 420, 480, C('Figure di notte guidate da tracce fosforescenti di lumache', '1940')),
    (OPERE+'miro_b.png', 520, 320, 380, 480, C('Risveglio all’alba', '1941')), (OPERE+'miro_c.png', 920, 320, 460, 480, C('La scala della fuga', '1940'))]),
 'I_pers': (4, 'La persistenza della memoria', [(OPERE+'persistenza.png', 80, 310, 1305, 520, C('Salvador Dalí · La persistenza della memoria', '1931'))]),
 'I_sogni': (4, 'La chiave dei sogni', [(OPERE+'chiave_sogni.png', 80, 310, 1305, 520, C('René Magritte · La chiave dei sogni'))]),
 'I_pipa': (4, 'Il tradimento delle immagini', [(OPERE+'pipa.png', 80, 310, 1305, 520, C('René Magritte · Il tradimento delle immagini', '1929 · olio su tela, 60 × 81 cm · Los Angeles County Museum of Art'))]),
 'I_aff': (4, 'Le affinità elettive', [(OPERE+'afflitta.png', 80, 310, 1305, 520, C('René Magritte · Le affinità elettive', '1933'))]),
 'I_cond': (4, 'La condizione umana', [(OPERE+'condizione.png', 80, 310, 1305, 520, C('René Magritte · La condizione umana', '1933 · olio su tela, 100 × 81 cm · Washington, National Gallery of Art'))]),
 'I_campi': (4, 'La chiave dei campi', [(OPERE+'chiave_campi.png', 80, 310, 1305, 520, C('René Magritte · La chiave dei campi', '1933 · olio su tela, 80 × 60 cm · Madrid, Museo Nacional Thyssen-Bornemisza'))]),
}
# ---------------- pezzi del docente ----------------
# (id, argo, t0, t1, stati[(t, chiave, card_accesa)])  t0 = inizio prima frase, t1 = fine ultima frase
P = [
 ('D0', 0, 0.7, 77.6, [(0.7, 'COVERP', None)]),
 ('D1a', 1, 78.4, 187.0, [(78.4, 'S1a', 0)]),
 ('D1b', 1, 188.3, 390.2, [(188.3, 'S1a', 0)]),
 ('D1c', 1, 390.9, 747.8, [(390.9, 'S1a', 0), (489.5, 'S1a', 1), (631.7, 'S1a', 0), (643.8, 'S1b', 0), (720.0, 'S1b', 1)]),
 ('D2a', 2, 748.2, 1004.3, [(748.2, 'S2a', None), (771.3, 'S2a', 1), (894.1, 'S2a', 0)]),
 ('D2b', 2, 1004.7, 1349.9, [(1004.7, 'S2a', 0), (1040.9, 'S4a', None), (1047.8, 'S4a', 1), (1064.9, 'S4a', 0), (1069.8, 'S4a', 1),
        (1097.9, 'S2a', 0), (1103.7, 'S2a', 1), (1114.3, 'S2b', 0), (1146.6, 'S2b', 1), (1155.8, 'S3', 0), (1199.5, 'S3', 1), (1204.1, 'S3', 2),
        (1213.6, 'S4a', 0), (1218.9, 'S4b', 0), (1220.7, 'S4b', 1), (1226.4, 'I_duch', None), (1263.6, 'I_ruota', None)]),
 ('D2c', 2, 1354.0, 1705.1, [(1354.0, 'I_lhooq', None), (1516.7, 'I_scola', None), (1572.0, 'I_fontana', None)]),
 ('D3a', 3, 1705.4, 1882.85, [(1705.4, 'S5a', 0), (1734.1, 'S5a', 1), (1802.4, 'S5b', 0), (1838.6, 'S5b', 1), (1848.2, 'S6', 0)]),
 ('D3b', 3, 1884.9, 2066.5, [(1884.9, 'S6', 2), (1892.3, 'I_telaz', None), (1933.9, 'I_tel', None), (2015.0, 'I_taz', None), (2058.1, 'S6', 1)]),
 ('D4a', 4, 2067.1, 2351.4, [(2067.1, 'S7', None), (2084.4, 'I_angelo', None), (2259.8, 'I_miro', None)]),
 ('D4b', 4, 2352.2, 2802.3, [(2352.2, 'S8', None), (2385.8, 'S8', 0), (2398.8, 'I_pers', None), (2503.9, 'S9', 0), (2531.2, 'I_sogni', None),
        (2646.4, 'I_pipa', None), (2748.4, 'I_aff', None)]),
 ('D4c', 4, 2804.2, 2971.9, [(2804.2, 'I_cond', None), (2873.5, 'I_campi', None)]),
]
# sequenza finale delle scene (nome -> pezzo del docente o scheda)
SEQ = ['SIG', 'COVER', 'D0',
  'T1', 'D1a', 'AN1A', 'D1b', 'AN1B', 'D1c', 'PILL1', 'Q1',
  'T2', 'D2a', 'AN2A', 'D2b', 'AN2B', 'D2c', 'MAPPA', 'PILL2', 'Q2',
  'T3', 'D3a', 'AN3A', 'D3b', 'PILL3', 'Q3',
  'T4', 'D4a', 'AN4A', 'D4b', 'AN4B', 'D4c', 'PILL4', 'Q4',
  'GLOSS', 'RF', 'VF', 'SF', 'CI', 'COMPITI']
