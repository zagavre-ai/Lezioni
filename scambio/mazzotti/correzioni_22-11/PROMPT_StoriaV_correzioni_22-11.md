# STORIA V · CORREZIONI FINALI DEL 22/11 · Prof. Giorgio Mazzotti (una chat = una lezione)

Sei una chat di produzione delle videolezioni del Centro Studi Telesio. La tua lezione te la scrive Sara nel messaggio. **Leggi tutto `CLAUDE.md`** (radice del repository, ramo main): sono le regole e vincono su ogni nota vecchia. Poi leggi `kit/REGOLE.md` per strumenti, stato e consegna. Sara oggi non ti segue: ogni dubbio va alla master con `stato.py --serve_master`.

Nella cartella `scambio/mazzotti/correzioni_22-11/` del ramo **`scambio-mazzotti`** trovi:
- `controllo_severo.py`: il controllo severo della master;
- `modello_mappa_BES/`: la mappa approvata, con `mappa.html`, `render.py` e il video di prova;
- `estrai_da_release.py`: scarica dalla release solo i file che servono, anche dentro gli zip.

L'indice dei materiali di Storia V è `scambio/mazzotti/INDICE_storia-V.md`, sullo stesso ramo.

## 0. Subito
1. Clona `zagavre-ai/lezioni`. Prepara la macchina come dice `kit/REGOLE.md` §1: caratteri, jingle, strumenti.
2. **Prenota:** `python3 kit/tools/stato.py storia-V-lezNN --stato IN_REVISIONE --nota "correzioni 22/11: presa da <tuo ramo>" --invia`. Se lo stato ha già «correzioni 22/11» scritto da un'altra chat, fermati e scrivilo alla master.
3. **Riparti dall'ultima consegna**, sul ramo `revisione-storia-V-lezNN`: video, timeline, voci, quiz, mappe. Il video originale del prof è nella release `mazzotti-storia-V` (vedi l'indice). Lancia `controllo_severo.py` sul video attuale: l'elenco degli errori è la tua lista di lavoro, insieme a quella qui sotto.

## 1. Cosa rifai (tutte le regole sono nel CLAUDE.md)
1. **Mappe del prof**, dal PDF «MAPPE LEZIONE N» della release.
   - Stessa struttura, stesse frecce, **stesse parole**. Una mappa per ogni argomento che ne ha una, alla fine dell'argomento. Mai il ritaglio dell'immagine.
   - Ridisegnate nel **modello BES approvato**: pesca, celeste, paglierino, menta e lilla, con la legenda; testo in maiuscolo e minuscolo, 34–50 px.
   - **Costruite ramo per ramo con la voce Kore.** Se una mappa a 34 px non entra in una schermata, si divide in 2–3 schermate seguendo i rami principali del prof («Mappa · 1 di 2»).
   - Togli tutte le mappe inventate o ristrutturate da noi.
   - Se per una lezione il PDF delle mappe non c'è (vedi l'indice), scrivilo alla master e **non inventare mappe**.
2. **Slide del prof**:
   - testo delle card a **40 px** (mai sotto 36), interlinea 1,5;
   - al massimo 3 card intere, mai «…»;
   - bordo giallo quando il prof comincia la frase;
   - nessuna schermata identica oltre 3 minuti: si usano sotto-slide «a finestra» e, dove il prof resta a lungo sullo stesso concetto, al massimo 2–3 approfondimenti Kore;
   - riquadro 4:3 del prof.
3. **Introduzione animata senza riquadro del docente** (nemmeno vuoto). **Il nome del docente non si dice mai nelle voci Kore** e non si scrive nelle schede animate: le voci che lo dicono si rifanno.
4. **Copertina** con il titolo esatto. L'introduzione del prof sopra la copertina dura al massimo 3 minuti, poi «Di cosa parliamo».
5. **Lezioni in più Parti:** ogni Parte dopo la prima si apre con lo **spiegone** della Parte precedente.
6. **Refusi** delle slide del prof corretti nelle nostre slide e dispense, ed elencati nel rapporto.
7. **Audio:** −16 LUFS, pause oltre 2,5 s accorciate a circa 1 s, **timbro intatto** (tra −9 e −20 dB). **Lezioni 4 e 6:** l'audio del prof va rifatto dall'originale, perché la versione su Vimeo ha la voce rovinata («grugnito»): solo pulizia leggera, mai filtri che cambiano il timbro.
8. **Dispensa** identica al video, con lo strato di testo invisibile. Copertina con solo materia e titolo. PDF delle mappe a parte, con la copertina «MAPPE».
9. **Lezione 18:** non è mai stata montata. Si fa da zero nel modello, partendo dai materiali del ramo `lavoro-storia-V-lez18`.

## 2. Voci
- Mandale **tutte subito**, in un solo `testi_voci.json` sul ramo `voci-storia-V-lezNN`: mappe, introduzioni senza nome, spiegoni, approfondimenti nuovi.
- **Stasera Google ci limita il numero di voci.** Le tue arrivano da domattina alle 9:00 italiane, prima se ne avanzano.
- **Non fermarti ad aspettarle:** monta tutto con voci provvisorie, delle stesse parole e durata stimata. Appena arrivano, controlla ogni voce (trascrizione, numeri, bordi) e sostituiscila.

## 3. Controllo e consegna
- `controllo_severo.py` con esito OK su ogni Parte. Poi un **agente separato** spunta tutta la lista del §11 del CLAUDE.md.
- Consegna sul ramo `revisione-storia-V-lezNN`. Stato `REVISIONATA` con la nota «**correzioni 22/11 fatte**».
- **Scadenza:**
  - stasera tutto il lavoro che non dipende dalle voci;
  - **consegna finale entro le 11:00 italiane di domani 23/11** (10:00 UTC).
  - Stato ogni 30 minuti. Se vedi che non ci arrivi, scrivilo subito alla master.
