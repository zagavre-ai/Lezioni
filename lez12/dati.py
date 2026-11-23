import json, openpyxl
D = '/home/user/Lezioni/lavoro/consegna/'
def q(p, a, w, e): return {'p': p, 'a': a, 'w': w, 'e': e}
Q = {
'Q1': {'title': 'Quiz 1 · I folli anni Venti', 'items': [
 q("Perché negli Stati Uniti, dopo la prima guerra mondiale, non c'era nulla da ricostruire?", "Perché avevano combattuto poco tempo e non sul loro suolo", ["Perché non avevano partecipato alla guerra", "Perché erano usciti sconfitti dal conflitto", "Perché avevano già ricostruito durante la guerra"], "hanno combattuto per circa un anno e non hanno conosciuto la guerra sul suolo americano."),
 q("Che cosa caratterizza i cosiddetti «folli anni Venti»?", "Divertimento, nuovi gusti e nuovi stili artistici e musicali", ["Una forte ripresa dell'ideologia borghese", "La chiusura delle gallerie d'arte", "Il ritorno ai canoni accademici"], "è l'età del jazz, che dagli Stati Uniti arriva poi in Europa."),
 q("Quale quartiere di Parigi diventa il punto di ritrovo di intellettuali, poeti, filosofi, musicisti e scrittori internazionali?", "Montparnasse, sulla Rive Gauche", ["Montmartre, sulla riva destra", "Il quartiere del Louvre", "Il quartiere degli sventramenti di Haussmann"], "Montparnasse e la zona della Rive Gauche, dove ci sono l'università e il quartiere latino."),
 q("Contro che cosa si contrappongono, in aperta rottura, i nuovi movimenti artistici?", "Contro l'ideologia borghese e capitalista che aveva portato alla guerra", ["Contro l'arte del Rinascimento", "Contro la scoperta della psicoanalisi", "Contro l'uso del jazz nei locali"], "rifiutano il senso comune che aveva portato alla guerra."),
 q("Quali luoghi diventano i nuovi punti di ritrovo degli artisti anticonformisti?", "I caffè, i club e i locali della vita notturna", ["Le gallerie tradizionali", "I saloni ufficiali delle secessioni", "Le aule delle accademie"], "rifiutano gallerie e collezionisti speculatori e cercano canali alternativi."),
]},
'Q2': {'title': 'Quiz 2 · Il Dadaismo e Marcel Duchamp', 'items': [
 q("Che cosa significa il nome «Dada»?", "È una parola senza senso, scoperta per caso sul dizionario", ["È il nome del locale di Zurigo", "Significa «pronto all'uso»", "È il cognome del fondatore del movimento"], "è stata scelta proprio per valorizzare il nonsenso e l'irrazionalità."),
 q("Qual è l'unica regola del Dadaismo?", "Non avere regole", ["Usare solo la pittura a olio", "Rispettare la prospettiva", "Rappresentare il sogno"], "il movimento rifiuta ogni valore precostituito."),
 q("Come compone i suoi collage Jean Arp?", "Affidandosi alla casualità, strappando e lasciando cadere i pezzi di carta", ["Seguendo un disegno tecnico preciso", "Copiando opere di altri artisti", "Usando solo ritagli di giornale"], "è la legge del caso."),
 q("Che cos'è il fotomontaggio dadaista?", "Una tecnica che combina ritagli di giornali e foto per svelare in modo ironico le contraddizioni della società", ["Una tecnica di pittura a olio", "Un modo di fotografare i paesaggi", "Una tecnica di scultura in ferro"], "è stato inventato dai dadaisti tedeschi, in un clima di satira e contestazione sociale."),
 q("Che cosa significa Ready-Made e in che cosa consiste?", "«Pronto all'uso»: un oggetto comune sottratto al suo contesto ed esposto come opera d'arte", ["«Fatto a mano»: un oggetto creato dall'artista", "«Fatto a caso»: un collage di carta", "«Nonsenso»: una parola inventata"], "il valore si sposta dall'abilità manuale al pensiero."),
]},
'Q3': {'title': 'Quiz 3 · Il Surrealismo e gli oggetti surrealisti', 'items': [
 q("Dove e con quale testo nasce ufficialmente il Surrealismo?", "A Parigi, nel 1924, con il Manifesto di André Breton", ["A Zurigo, nel 1916, con il Manifesto di Tristan Tzara", "A New York, nel 1924, con il Manifesto di Duchamp", "A Berlino, nel 1916, con il Manifesto di Arp"], "il Surrealismo si sviluppa a Parigi in virtù di questo manifesto."),
 q("A quale teoria si ispira il Surrealismo?", "Alla psicoanalisi di Freud", ["Al positivismo", "Al marxismo", "Al futurismo"], "mette al centro il sogno, l'irrazionalità e l'esplorazione dell'inconscio."),
 q("Che cos'è l'automatismo psichico?", "Una tecnica per esprimere il pensiero puro, libero dal controllo della ragione o da freni morali", ["Una tecnica di stampa meccanica", "Un metodo per copiare la realtà", "Un modo di fotografare i sogni"], "può essere usato nella scrittura, nel disegno e nella pittura."),
 q("Che cosa si intende per Surrealtà?", "Una realtà superiore, nata dalla fusione armonica tra sogno e veglia", ["Una realtà che copia fedelmente la natura", "Una realtà senza regole né significato", "Una realtà nata dalla guerra"], "è un concetto fondamentale del Surrealismo."),
 q("Quale effetto producono gli oggetti surrealisti sullo spettatore?", "Un effetto perturbante, di shock e profondo disagio", ["Un effetto di quiete e di armonia", "Un effetto di noia e distacco", "Un effetto di calma e di silenzio"], "gli accostamenti insoliti e contrari alla logica attivano desideri o impulsi nascosti."),
]},
'Q4': {'title': 'Quiz 4 · Ernst, Miró, Dalí e Magritte', 'items': [
 q("Quale opera di Max Ernst mostra una figura mostruosa, biomorfa e vagamente antropomorfa?", "L'angelo del focolare", ["La persistenza della memoria", "La condizione umana", "Il tradimento delle immagini"], "il titolo stride con la rappresentazione: più che un angelo sembra un demonio."),
 q("Da che cosa si ispira Joan Miró nella serie delle Costellazioni?", "Dal fascino del cielo stellato", ["Dalla pittura accademica", "Dalle fotografie di giornale", "Dagli oggetti di uso quotidiano"], "crea un repertorio di pittogrammi e segni semplici."),
 q("Su che cosa si basa il metodo paranoico-critico di Dalí?", "Sulla razionalizzazione guidata di immagini deliranti, illusioni ottiche e ossessioni profonde", ["Sull'uso del caso nei collage", "Sullo sfregamento di grafite su carta", "Sulla fotografia di oggetti comuni"], "ne La persistenza della memoria si vedono orologi deformati."),
 q("Che cosa simboleggiano gli orologi molli de La persistenza della memoria?", "La relatività del tempo e la deformazione psicologica della sua durata", ["La rigidità del tempo meccanico", "La velocità della vita moderna", "Il passaggio delle stagioni"], "il tempo si scioglie e cambia, in contrapposizione al tempo meccanico."),
 q("Che cosa vuole ricordare Magritte con «Ceci n'est pas une pipe»?", "Che l'immagine di una pipa non è l'oggetto reale", ["Che la pipa è un oggetto da collezione", "Che la pittura deve copiare la natura", "Che la pipa si può fumare"], "il dipinto è soltanto una rappresentazione grafica bidimensionale."),
]},
}
def verifica():
    ws = openpyxl.load_workbook('/home/user/Lezioni/lavoro/in/DOMANDE.LEZIONE.12.xlsx').active; rows = list(ws.iter_rows(values_only=True))[1:]
    return {'titolo': 'Storia dell\'arte V · Lezione 12 · Verifica finale', 'domande': [{'n': i + 1, 'p': r[0], 'a': r[1], 'w': [r[2], r[3], r[4]]} for i, r in enumerate(rows)]}
COMP = {'titolo': 'Compiti · Storia dell\'arte V · Lezione 12', 'esercizi': [{'testo': t} for t in __import__('run_comp').CT]}
if __name__ == '__main__':
    json.dump(Q, open(D + 'quiz_argomenti.json', 'w'), ensure_ascii=False, indent=1)
    json.dump(verifica(), open(D + 'verifica_finale.json', 'w'), ensure_ascii=False, indent=1)
    print(len(Q), len(verifica()['domande']))
