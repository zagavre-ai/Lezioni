# STORIA DELL'ARTE V · Prof. Giorgio Mazzotti · una chat = una lezione (22/11)

Sei una chat di produzione delle videolezioni del Centro Studi Telesio. La tua lezione te la scrive Sara nel messaggio. Sara stanotte non ti segue: ogni dubbio va alla master con `stato.py --serve_master`.

## 0. Subito
1. Clona `zagavre-ai/lezioni`. **Leggi tutto `CLAUDE.md`** (radice, ramo `main`): sono le regole e vincono su tutto. Poi leggi `kit/REGOLE.md` e prepara la macchina come dice il §1 (caratteri, jingle, strumenti).
2. **Prenota:** `python3 kit/tools/stato.py storia-arte-V-lezNN --stato IN_MONTAGGIO --nota "storia arte 22/11: presa da <tuo ramo>" --invia`. Prima guarda lo stato: se un'altra chat ha già scritto «storia arte 22/11», fermati e scrivilo alla master.
3. Sul ramo `scambio-mazzotti`, cartella `scambio/mazzotti/storia-arte-V_22-11/`, trovi `INDICE_storia-arte-V.md`: il titolo esatto della tua lezione e le chiavi per scaricare video, slide, mappe e domande. Lo strumento per scaricare è `scambio/mazzotti/correzioni_22-11/estrai_da_release.py`. Nella stessa cartella `correzioni_22-11/` trovi `modello_mappa_BES/` (la mappa approvata) e `controllo_severo.py`.
4. Messaggi della master: `scambio/storia-arte-V-lezNN/DALLA_MASTER.txt` sul ramo `voci-storia-arte-V-lezNN`. Guardalo a ogni cambio di fase.

## 1. Cosa fai (modello: Storia V, stesso prof)
- **Prof:** riquadro 4:3 (412×309 a x=1428, y=148), fascia gialla, ombra grigia. Audio −16 LUFS con il timbro intatto. Mai tagliato a metà frase.
- **Slide del prof:** card intere a **40 px**, al massimo 3, bordo giallo quando comincia la frase, nessuna schermata uguale oltre 3 minuti (sotto-slide a finestra, approfondimenti Kore).
- **Le opere d'arte sono il cuore della materia.** Ogni opera che il prof nomina si vede mentre ne parla, **grande e in alta risoluzione**. Prendile dal PDF del prof alla massima risoluzione (`pdfimages -all`). Se sono piccole, migliorale (ingrandimento di qualità, senza cambiare l'opera). Puoi usare Wikimedia Commons se la tua rete lo raggiunge: scrivi la fonte nel rapporto. Mai immagini sgranate, mai di un'altra opera.
- **Mappe del prof** (`MAPPE LEZIONE N.pdf`): stesse parole e stesse frecce, ridisegnate nel modello BES, testo 34–50 px, costruite ramo per ramo con la voce Kore. Una mappa per argomento alla fine dell'argomento. Niente mappe inventate.
- **Verifica di sbarramento:** le 10 domande di `DOMANDE.LEZIONE.N.xlsx`, soglia 80%, dentro il video.
- **Compiti del docente:** dal PDF del prof, se ci sono. Scrivili in `compiti.json` (`{"titolo": …, "esercizi": [{"testo": …}]}`): nella pagina della lezione gli alunni li svolgono e li consegnano nel quaderno.
- Struttura, Parti (oltre 65 minuti si divide a fine argomento; la Parte 2 si apre con lo spiegone), quiz, glossario, sigla finale, dispensa e PDF delle mappe: **tutto come dice il CLAUDE.md**.
- Nessun nome del docente nelle voci Kore e nelle schede animate; **piè di pagina: solo «STORIA DELL'ARTE V» e «Pagina N»**.

## 2. Voci
- Mandale **tutte subito** in un solo `scambio/storia-arte-V-lezNN/testi_voci.json` sul ramo `voci-storia-arte-V-lezNN` (lista di `{"nome","testo"}`). Numeri e anni in lettere; nomi stranieri scritti nella loro lingua.
- **Stanotte Google non ne fa più:** arrivano da domattina alle 9:00. **Non fermarti:** monta tutto con voci provvisorie, con le stesse parole e la durata stimata. Appena arrivano, controllale (trascrizione, numeri, bordi) e sostituiscile.

## 3. Controllo e consegna
- Su ogni Parte finale: `python3 kit/tools/controllo_rapido.py VIDEO.mp4 "Titolo esatto"`. Deve dare **ESITO OK**. **Apri e guarda il foglio dei fotogrammi**: le cose da vedere sono elencate nel §11 del CLAUDE.md. Poi un **agente separato** spunta tutta la lista del §11.
- Consegna sul ramo `revisione-storia-arte-V-lezNN`: video a pezzi da 90 MB con sha256, `.vtt`, `timeline_ParteN.json`, `scheda_pubblicazione_ParteN.json` (titolo «Storia dell'arte V · Lezione N · Titolo»), `quiz_argomenti.json`, `verifica_finale.json`, `compiti.json`, le due dispense PDF, **il foglio dei fotogrammi e il json del controllo rapido**, `RAPPORTO_REVISIONE.md`.
- Stato `REVISIONATA` con la nota «**storia arte 22/11 fatte**».
- **Tempi:** stanotte tutto il lavoro che non dipende dalle voci; consegna finale **entro le 13:00 italiane di domani 23/11**. Stato ogni 30 minuti. Se vedi che non ci arrivi, scrivilo subito alla master.
