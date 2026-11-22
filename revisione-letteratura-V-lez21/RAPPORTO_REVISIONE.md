# RAPPORTO DI REVISIONE · Letteratura italiana V · Cesare Pavese · CORREZIONI 22/11

Stato: **REVISIONATA — «correzioni 22/11 fatte»**. Durata misurata **55:20,6** (3320,6 s), 99617 fotogrammi, 190,5 MiB, 1920×1080.
Presa alle 16:40 UTC dal ramo `revisione-letteratura-V-lez21`; consegnata prima delle 19:30 UTC.

## 1. Cosa ho cambiato
- **Una sola mappa, quella del prof**, ridisegnata nel modello BES approvato (colori pesca/celeste/paglierino/menta/lilla, legenda in alto a destra, testo 34–52 px), costruita **ramo per ramo** con la voce Kore (6 voci MR1–MR6, numeri in lettere) con il riquadro acceso in giallo; alla fine resta ferma 4 s. Messa **una volta sola**, prima del glossario. Tolte tutte le mappe per argomento e le loro voci. Le card della mappa riuniscono le voci vicine del prof nello stesso riquadro con le **stesse parole**; per stare a 34 px ho unito più voci in un riquadro (la mappa del prof ha 25 riquadri).
- **Slide del prof**: testo **40 px, interlinea 1,5**, **al massimo 3 card**, ogni card è una frase intera (le card che continuano una frase cominciano con la maiuscola), card alte quanto il testo; la card in corso ha bordo e pallino **gialli** quando il prof inizia la frase (±1 s). Le slide cambiano quando il prof passa alla frase successiva, **mai oltre 165 s sulla stessa pagina** (tabella §3). Anche approfondimenti, ripassi, glossario e riepilogo sono ora card a 40 px (max 3 per pagina; niente tabelle).
- **Pezzi del prof**: D4 diviso in tre (D4a/D4b/D4c) con gli approfondimenti «La casa in collina» e «Altre tre opere» inseriti **a fine frase** nel punto giusto, così nessuna slide resta ferma e ogni approfondimento arriva dopo che il prof ha parlato di quell'opera.
- **Pause**: le pause oltre 2,5 s tra le schede sono state accorciate (ritardo voce 0,5 s, code 0,5 s, schede titolo/quiz/verifica/compiti più brevi; jingle nei soliti punti); la mappa finale tiene 4 s con due `trans.wav` per non lasciare silenzio.
- **Nome del prof**: tolto dai piè di pagina di tutte le schede animate; resta solo nella fascia gialla e nel piè di pagina delle slide con il prof.
- **Audio**: parlato a −16,1 LUFS (mediana pezzi del prof), totale −16,5 LUFS, **picco −1,8 dBFS** (≤ −1); timbro: rapporto acuti/gravi del prof −13,9…−16,4 dB come l'originale (nel range −9…−20).
- **Dispense A4 orizzontali**: `Letteratura_Lez21_slide.pdf` (60 pagine, identiche alle schermate del video senza riquadro e senza fascia; **testo reale selezionabile**; copertina con solo materia e titolo; piè di pagina materia + pagina senza nome del docente) e `Letteratura_Lez21_mappe.pdf` (copertina identica con la scritta «MAPPE» + mappa del prof).
- File rigenerati sul video finale: `.vtt`, `timeline.json`, `scheda_pubblicazione.json` (titolo «Letteratura V · Lezione 21 · Cesare Pavese»), `quiz_argomenti.json`, `verifica_finale.json`, `testo_youtube.txt`, `controllo_minuti.jpg`.

## 2. Esito del controllo severo (`controllo_severo.py`, titolo «Cesare Pavese»)
**ESITO OK, zero errori**: copertina con titolo intero (90 s), nessuna slide oltre 3 min, nessuna schermata identica oltre 3 min, nessuna card con «…» o minuscola, nessuna card sola oltre 60 s, loudness −16,5, 0 pause >2,5 s, durata 55,3 min, voce non alterata (tono 141–164 Hz, chiarezza 1465–1562 Hz).
**Attenzione sul metodo:** tesseract non si installa in questa macchina (apt senza pacchetto). Ho usato un **sostituto** (`tesseract` finto basato su RapidOCR, in `/tmp`, non nel repo) che ricalca l'uscita di tesseract: i controlli sul testo (titolo, numeri di pagina, card) vanno quindi **riconfermati dalla master con il suo tesseract**.
Altri controlli del kit: quiz Q1–Q5 scatto **+0,000 s**; nessun fermo immagine nei pezzi del prof; **il controllo del kit sull'attacco dei sottotitoli entro 0,3 s dà 72% su 25 punti verificabili: sotto la soglia dell'80%** (segnalato, non dimostrato).

## 3. Pezzi del prof: pagine (finestre) e card
| Pezzo | finestre di pagina |
|---|---|
| D1 | 1:08.1–3:53.1 card 1,2,3; 3:53.1–6:38.1 card 3,4,5; 6:38.1–8:05.1 card 4,5,6; 8:05.1–8:21.9 card 6,7 |
| D2 | 8:21.9–10:07.7 card 1,2,3; 10:07.7–12:16.4 card 4,5 |
| D3 | 12:16.9–15:01.9 card 1,2,3; 15:01.9–15:55.6 card 3,4; 15:55.6–18:02.0 card 4,5 |
| D4a | 18:02.7–20:15.9 card 1,2; 20:15.9–21:41.0 card 3,4 |
| D4b | 21:41.6–23:32.3 card 1,2 |
| D4c | 23:32.5–24:41.2 card 1,2 |
| D5 | 24:41.6–26:00.9 card 1,2; 26:00.9–27:41.7 card 3,4; 27:41.7–28:24.9 card 4,5 |

## 4. Tabella inizio/fine di ogni pezzo del prof (tempi dell'originale)
| Pezzo | Inizio | Fine: ultime parole | Frase intera |
|---|---|---|---|
| D1 | 0:00 «Buongiorno e benvenuti alla lezione su Cesare Pavese…» | «…rapporto permanentemente difficile e tormentato con le figure femminili.» | sì |
| D2 | 8:22 «Dopo l'armistizio dell'8 settembre 1943…» | «…con gli autori che abbiamo nel frattempo già visto, d'accordo?» | sì |
| D3 | 12:17 «Allora, addentrandoci nella sua poetica…» | «…metafore e da una profonda e dolorosa solitudine.» | sì |
| D4a | 18:03 «Ecco, vediamo invece di delineare i romanzi.» | «…È molto autobiografico, in parte.» | sì |
| D4b | 21:42 «Il trittico di romanzi brevi che compone…» | «…analisi acerbe e pungenti, mordaci, ecco.» | sì |
| D4c | 23:32 «Un discorso a parte merita Il diavolo sulle colline…» | «…l'ideale pavesiano di un sano equilibrio interiore e sociale.» | sì |
| D5 | 24:41 «Ma soprattutto, come dicevo, il capolavoro…» | «…fine della sua vita tramite appunto il suicidio.» | sì |
Sincronia audio/video del prof (correlazione sull'originale, 3 punti per pezzo): **0,014–0,016 s** su tutti i pezzi (limite 0,04).

## 5. Secondi vecchi → nuovi (scheda)
| Voce | secondo vecchio | secondo nuovo |
|---|---|---|
| Durata totale | 3503.16 | 3320.57 |
| Argomento 1 inizio | 36.25 | 36.968 |
| Quiz 1 | 923.184 | 803.8 |
| Argomento 2 inizio | 928.184 | 807.6 |
| Quiz 2 | 1315.419 | 1227.119 |
| Argomento 3 inizio | 1320.419 | 1230.919 |
| Quiz 3 | 2026.184 | 1858.475 |
| Argomento 4 inizio | 2031.184 | 1862.275 |
| Quiz 4 | 2781.117 | 2548.857 |
| Argomento 5 inizio | 2786.117 | 2552.657 |
| Quiz 5 | 3303.284 | 3030.54 |
| Verifica finale | 3484.71 | 3308.753 |
| Compiti | 3498.21 | 3312.553 |

## 6. Voci
Voci nuove: MR1–MR6 (mappa unica), GL2 (glossario). Controllo: trascritte una per una e confrontate con il copione, **tutti i numeri coincidono** (1908, 1930, 1935, 1936, 1941–1951…) e nessuna parola inserita o mancante; «amendmenta» nella trascrizione è un'allucinazione dello strumento (durata zero). Le voci già esistenti (INTRO, R, S, AN, RF, FIN) controllate con lo stesso metodo: numeri coincidenti.

## 6-bis. Controllo di un agente separato (che non ha montato la lezione, §11 delle regole)
Esito: **nessun difetto bloccante** su: (1) pezzi del prof a frase intera (0 parole a cavallo dei tagli, in tutti e 7); (2) copertina senza riquadro del prof; (3) max 3 card, iniziali maiuscole, testo 40 px, mappa unica con legenda BES costruita ramo per ramo; (4) PDF slide 60 pagine A4 orizzontali con testo selezionabile, copertina e piè di pagina senza nome del docente né numero di lezione, PDF mappe con «MAPPE»; (5) nessun numero di lezione e nome del docente solo nella fascia gialla e nel piè di pagina delle slide col prof; (6) sottotitoli: 0 sovrapposizioni, max 2 righe, 15 cue a campione coerenti con la trascrizione.
**Difetto lieve:** un sottotitolo lungo 9,5 s a 15:43–15:52 (copre una pausa del prof): leggibile, nessuna regola violata, **non corretto**. L'agente **non ha verificato**: audio, labbra, quiz, glossario, verifica, compiti, voci, immagini, «già visto», bordo giallo in 10 punti, tenuta di 4 s della mappa finale.

## 7. Cosa non ho potuto verificare
- Nessun **ascolto umano** (rumore, «metallico», naturalezza delle voci Kore, sincronia delle labbra oltre la misura).
- Controllo severo con **OCR sostitutivo** (§2).
- **Sottotitoli**: i 357 blocchi del prof riletti a mano il 16/11; qualche parola resta incerta senza ascolto (es. «il fronte dei…» a 1655 s dell'originale). Allineamento fine ±0,3 s non dimostrato (72% al controllo del kit).
- Immagini: nessuna immagine esterna aggiunta (nessuna foto di persone, nessun logo di terzi; dalla mappa del prof ho tolto il marchio e la foto).

## 8. Anomalie del materiale del prof (non corretto niente: decide Sara)
Mappa «a 5 anni» orfano di padre ↔ slide e parlato «sei anni»; *Il compagno* 1947 (mappa) ↔ 1946 (slide e parlato); *La bella estate* 1949 (mappa, trittico) ↔ «scritto nel 1940» (slide). Nel parlato il prof dice «Santina» (il romanzo), nelle slide «Santa».
