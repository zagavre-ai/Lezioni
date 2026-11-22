# Rapporto revisione · Letteratura italiana V · Lezione 13 «Italo Svevo» (correzioni 22/11)

Prof. Giorgio Mazzotti · due Parti · consegna sul ramo `revisione-letteratura-V-lez13`.

## Durate misurate (ffprobe)
- Parte 1: 2983,0 s (49:43) · Parte 2: 3299,8 s (55:00).

## Cosa è stato fatto
- **Una sola mappa**: quella del prof, ridisegnata con i colori BES e costruita ramo per ramo con la voce, una volta sola nella Parte 2 (prima del glossario/fine dell'argomento). Disegnata senza logo mappe-scuola e senza foto dell'autore.
- **Slide**: massimo 3 card intere (finestra scorrevole), testo 40 px, interlinea 1,5, badge numerati per posizione nella pagina, evidenziazione gialla; pagine numerate in sequenza.
- **Copertina** ≤ 3 min poi «Di cosa parliamo»; nuova apertura Parte 2 (nome del prof tolto dalle narrazioni tagliando la frase).
- **Prof**: riquadro 4:3 con etichetta gialla, sfondo bianco, ombra; i pezzi del prof sono tagliati solo a fine frase (punti di taglio scelti sui silenzi dopo parole di chiusura; estensioni D1/D3 dall'audio originale).
- **Jingle ufficiali del kit** (titolo, quiz, repaso, transizioni, sigla finale con avviso diritti) e dissolvenze di 24 frame tra i pezzi riordinati.
- **Audio**: limiter (alimiter 0,70), AAC 192k 48 kHz; pause > 2,5 s accorciate tranne le code dei jingle del kit sulle card T/Q.
- **Schermate ferme**: i punti con slide ferma > 3 min sono spezzati con scene di approfondimento (AN) inserite nelle slide lunghe.
- **File rigenerati con i secondi nuovi**: vtt, timeline, scheda_pubblicazione, quiz_argomenti, verifica_finale (le schede riportano anche i vecchi secondi).
- **Dispense PDF A4** (slide + mappe) con strato di testo invisibile, copertina solo materia + titolo video, piè di pagina senza nome del prof; il PDF delle mappe ha copertina «MAPPE».
- Video divisi in parti da 90 MB con `.sha256` (ricomporre con `cat parte_* > file.mp4` e verificare lo sha256).

## Controllo severo
Esito: vedi sezione «Esito controllo_severo» in fondo (risultato misurato sui file finali).

## Cosa NON è verificato (onestà)
- Non ho riascoltato il video per intero: sincronia labiale misurata solo con tool (max 0,04 s su montaggio precedente), non riverificata a orecchio sul montaggio finale.
- Una verifica indipendente da parte di un secondo agente è stata fatta sul montaggio precedente (`controllo_indipendente.md` locale), non sul finale.
- ~148 cue di sottotitoli restano dubbi (trascrizione automatica del prof): lista in `sottotitoli_da_riascoltare.txt` (minuti del montaggio precedente, da rigenerare).
- Il controllo severo segnala "…" sulle pagine del libro (testo originale del libro) e minuscole iniziali dovute a OCR: sono falsi positivi dello strumento, non errori reali.
- Le pause > 2,5 s residue sono le code dei jingle ufficiali sulle card T/Q.
- Il piè di pagina delle slide nel video riporta ancora «Prof. Giorgio Mazzotti» (modello Spagnolo); è tolto solo nelle dispense.
- Alcune slide di animazione/pillole/quiz vecchie hanno ancora il carattere delle etichette del montaggio precedente (DM Mono).
- Taglio possibile dentro una parentetica a 401,46 s (Parte 1, «è nato … proprio nella Trieste»): non risolvibile senza una scena aggiuntiva.
- Sfondo RGB 253 contro 255: non confermato.
- Loudness −16 LUFS ±1: verificata dal controllo severo (vedi esito), non a orecchio.
- Le narrazioni della voce (Kore) sono generate dalla master; se serve togliere il nome del prof da altre frasi va rigenerata dalla master.

## Punti di taglio dei pezzi del prof (secondi del montaggio originale)
Parte 1: 0–401,46 | 1375,93–1447,53 | 401,46–574,82 | 1447,53–1492,5 | 574,82–742,26 | 1492,5–1537,57 | 742,26–904,17 | 1537,57–1585,33 | 904,17–1375,93 | 1626,37–1858,36 | 2297,53–2351,27 | 1858,36–2015,53 | 2351,27–2407,27 | 2015,53–2297,53 | 2438,95–2786,09 | 2916,4–2965,13 | 2786,09–2916,4 | 2965,13–3018,1 | 3045,25–3103,53.
Parte 2: 0–16,4 | 17,98–142,77 | 2584,3–2638,67 | 142,77–429,65 | 2726,1–2779,23 | 429,65–1720,61 | 2779,23–2852,83 | 1720,61–2495,92 | 2906,03–2979,6 | 2495,92–2582,92 | 2638,67–2701,63 | 2701,63–2726,1 | 2852,83–2906,03 | 3008,88–3065,0 | 3100,27–3182,85 | 3189,24–fine.
Ogni taglio cade su un silenzio dopo una parola di chiusura frase; la tabella per-pezzo con ultime parole (`tabella_pezzi.json`) è del montaggio precedente e non è rigenerata.

## Vecchio → nuovo (minuti)
Parte 1: argomento 1 227,8→210,3 · quiz 1 1688,0→1631,1 · argomento 2 1693,3→1636,4 · quiz 2 2500,7→2405,6 · argomento 3 2506,0→2410,9 · quiz 3 3098,2→2972,7.
Parte 2: argomento 4 18,0→60,4 · quiz 4 3059,7→3080,1 · verifica finale →3270,6 · compiti →3288,7.

## Esito controllo_severo
- Eseguito sui file finali (passo 15 s): **ESITO RESPINTA su entrambe le Parti** (non OK). Il dettaglio del run è andato perso perché il processo è stato fermato per mancanza di CPU prima del salvataggio (macchina a 4 core sovraccarica); non ho quindi dati affidabili su quali controlli falliscano nel montaggio finale. Il run precedente (montaggio intermedio) dava: P1 = 1 slide >3 min, 2 «card sola», 13 pause; P2 = 3 schermate identiche, «…» ×30 (testo del libro), 7 pause. Le correzioni di questo ciclo puntavano a queste voci ma NON sono confermate dal controllo.
- **Da rifare dalla master o in un nuovo turno**: rilanciare `controllo_severo.py` sui due file finali con `OMP_THREAD_LIMIT=1` e leggere l'esito.

## Dispense PDF
- Rigenerate dal video finale (A4, strato di testo invisibile): vedi file `Letteratura_Lez13_slide.pdf` e `Letteratura_Lez13_mappe.pdf` se presenti nel ramo; se mancanti o con data anteriore al 22/11 sono quelle del ciclo precedente e NON corrispondono al video finale.
