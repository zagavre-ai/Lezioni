# RAPPORTO · Storia V · Lezione 7 · Gli Stati Uniti dal boom economico al New Deal

**Stato: rifatta da zero e poi corretta con le note della master del 19/11 (03:40, 05:10, 05:25)**, in 1 Parte unica, sul video originale del prof. Giorgio Mazzotti (2180,2 s). Voci Kore e quiz (5×5) già approvati nel ramo `voci-storia-V-lez07`: nessuna voce nuova generata. Ogni affermazione è marcata [misurato], [per costruzione], [stima] o [non verificato].

## 1 · Misure sul video

| | Parte unica (argomenti 1–5) |
|---|---|
| Durata | 50:11.5 (3011.5 s) [misurato] |
| Fotogrammi / 30 fps | 90344 = durata×30 [misurato] |
| Formato | 1920×1080, x264, AAC 192k 48 kHz stereo [misurato] |
| Peso | 388.2 MB [misurato] |
| Loudness integrata (file finale, ebur128) | -16,8 LUFS [misurato] |
| Picco (true peak, file finale) | -3,9 dBFS [misurato] (limite −1) |
| Parlato del prof (mediana dei pezzi) | -16,4 LUFS [misurato] |
| Scatto `quiz.wav` | OK +0.005; OK +0.005; OK +0.005; OK +0.005; OK +0.005 [misurato, controllo_jingle.py] |
| Fermi immagine del prof ≥ 1 s | vedi uscita del controllo [misurato] |
| Sfasamento audio/labbra | **non misurato in modo affidabile** (la correlazione viso/audio è troppo debole perché il prof gesticola); audio e video del prof escono dallo stesso istante dell'originale [per costruzione] |
| sha256 | vedi `.sha256`; ricomponendo i `.parte_NN` coincide [misurato] |

Uscita integrale di `controllo_finale.py`:

```
durata 50:11.5 (3011.5 s) | fotogrammi 90344 (attesi 90344) OK | peso 388.2 MB (370.2 MiB) OK | 1920x1080 OK
quiz 5 scatto 0,0 s: OK
fermi immagine nei pezzi del docente: nessuno OK
volume del parlato (mediana dei pezzi del docente): -16.4 LUFS OK
sottotitoli: 684 blocchi, sovrapposti 0, oltre la fine 0, attacco sulla voce entro 0,3 s: 67% di 18 verificabili DA GUARDARE
foglio di miniature: out/Storia_Lez7_Parte1_1080p.mp4.miniature.jpg
ESITO: DA SISTEMARE: sottotitoli
```

**Sottotitoli, attacco sulla voce (soglia 80%)**: **67%** di 18 blocchi verificabili (DA) [misurato]. Dove lo strumento non dà OK, i blocchi fuori soglia vanno guardati uno per uno: ho guardato i 6 blocchi fuori soglia (circa 2:50, 6:59, 15:20, 30:30, 41:22, 42:31): in 5 l'energia del parlato parte entro 0,0–0,2 s dall'inizio del blocco e lo strumento trova prima un breve rumore (respiro o coda della parola precedente) 0,7–0,8 s prima; nel blocco a 30:30 l'attacco del parlato è 0,34 s dopo l'inizio del blocco [misurato sull'energia, non riascoltati]. Il verdetto automatico resta DA SISTEMARE.

## 1b · Correzioni della master (19/11)

| # | Punto | Cosa ho fatto | Misura |
|---|---|---|---|
| 1 | Max 3 card per slide, slide mai ferme oltre 3 min; card = punto intero della slide del prof, mai spezzata con «…»; mai una card sola senza immagine | Le 13 pagine hanno 2 o 3 card (max 3); le card sono i punti interi del PDF del prof (titolo in grassetto una volta sola); le pagine da 4 card sono ridistribuite 2+2 e il punto che restava solo (pagina 7→8) è unito alla pagina dopo; il prof è diviso in 13 tratti con approfondimenti in mezzo; dove una card dura a lungo la stessa card passa a pagina intera in corpo grande (3 stati) | pagina ferma più lunga: **172 s** (argomento 3, minuto 15:47 dell'originale) [misurato sul piano dei cue]; limite 180 s |
| 2 | Sincronia bordo giallo ↔ prof | Cue presi dalla trascrizione (segmenti con i tempi) | non rimisurato a campione su 10 punti in questa versione: i cue sono quelli della consegna precedente, già allineati alla trascrizione [non verificato in questa versione] |
| 3 | Mappe | Le 3 mappe del PDF «MAPPE LEZIONE 7» ridisegnate con `kit/tools/mappa.py` (testi del prof; rami a tempo con la voce Kore) | 3 mappe (argomenti 3, 4, 5), un ramo alla volta [misurato sui fotogrammi] |
| 4 | Approfondimenti animati | Per ogni argomento 2 approfondimenti con le voci Kore già approvate (`AN1`–`AN10`), frasi della voce a tempo, solo materiale della lezione | durata per argomento: arg. 1 62 s; arg. 2 50 s; arg. 3 75 s; arg. 4 58 s; arg. 5 62 s [misurato]; richiesto 40–60 s: fuori intervallo gli argomenti 1, 3, 5 |
| 5 | Schema di ripasso 4–6 righe | Già a norma | righe per argomento: 1:4, 2:4, 3:5, 4:5, 5:5 [misurato] |
| 6 | Transizioni | `trans.wav` + dissolvenza 0,4 s a ogni confine tra pezzi | 51 confini, nessun taglio secco [per costruzione] |
| 7 | Copertina | Titolo esatto della slide del prof: «GLI STATI UNITI: DAL BOOM ECONOMICO AL NEW DEAL» su 2 righe a sinistra del riquadro del prof; la consegna precedente aveva per errore il titolo della lezione 5 | verificato sul fotogramma [misurato] |
| 8 | Avviso diritti | Solo nel finale, in basso al centro, testo bianco 24 px senza riquadro; tolto dalla copertina | verificato sul fotogramma del finale [misurato] |
| 9 | Introduzione del prof sulla copertina max 3 min | Il prof parla sulla copertina da 0:00,6 a 1:49 | 108 s [misurato] |
| 10 | `timeline` e `scheda_pubblicazione` rigenerate sul video corretto | Rigenerate dopo l'ultimo montaggio | durata_s = durata del video [misurato] |

## 2 · Tabella dei pezzi (sezione C della scheda tecnica)

| Pezzo | Presente | Minuto | Durata misurata |
|---|---|---|---|
| 1 · Sigla | sì | 0:00.0 | 15.0 s |
| 3 · Copertina + voce di benvenuto | sì | 0:13.6 | 15.2 s |
| 3 · Introduzione del prof sulla copertina | sì | 0:28.4 | 109.4 s |
| 4a · Titolo argomento 1 | sì | 2:17.4 | 4.0 s |
| 4b · Prof + slide argomento 1 (tratto 1) | sì | 2:21.0 | 184.9 s |
| 4c · Approfondimento animato argomento 1 · voce Kore | sì | 5:25.5 | 27.9 s |
| 4b · Prof + slide argomento 1 (tratto 2) | sì | 5:53.0 | 294.4 s |
| 4c · Approfondimento animato argomento 1 · voce Kore | sì | 10:47.0 | 33.7 s |
| 4b · Prof + slide argomento 1 (tratto 3) | sì | 11:20.2 | 81.4 s |
| 4e · Pillola di ripasso argomento 1 | sì | 12:41.2 | 9.5 s |
| 4f · Schema guidato argomento 1 | sì | 12:50.3 | 41.8 s |
| 4g · Scheda Quiz 1 | sì | 13:31.7 | 5.0 s |
| 4a · Titolo argomento 2 | sì | 13:36.3 | 4.0 s |
| 4b · Prof + slide argomento 2 (tratto 1) | sì | 13:39.9 | 186.0 s |
| 4c · Approfondimento animato argomento 2 · voce Kore | sì | 16:45.5 | 24.9 s |
| 4c · Approfondimento animato argomento 2 · voce Kore | sì | 17:10.1 | 24.6 s |
| 4e · Pillola di ripasso argomento 2 | sì | 17:34.3 | 12.0 s |
| 4f · Schema guidato argomento 2 | sì | 17:45.9 | 38.2 s |
| 4g · Scheda Quiz 2 | sì | 18:23.7 | 5.0 s |
| 4a · Titolo argomento 3 | sì | 18:28.3 | 4.0 s |
| 4b · Prof + slide argomento 3 (tratto 1) | sì | 18:31.9 | 172.5 s |
| 4c · Approfondimento animato argomento 3 · voce Kore | sì | 21:24.0 | 35.1 s |
| 4b · Prof + slide argomento 3 (tratto 2) | sì | 21:58.7 | 156.3 s |
| 4c · Approfondimento animato argomento 3 · voce Kore | sì | 24:34.6 | 39.8 s |
| 4b · Prof + slide argomento 3 (tratto 3) | sì | 25:14.0 | 158.6 s |
| 4d · Mappa del prof argomento 3 (mappa.py, voce Kore) | sì | 27:52.2 | 35.1 s |
| 4e · Pillola di ripasso argomento 3 | sì | 28:26.9 | 10.5 s |
| 4f · Schema guidato argomento 3 | sì | 28:37.0 | 45.7 s |
| 4g · Scheda Quiz 3 | sì | 29:22.3 | 5.0 s |
| 4a · Titolo argomento 4 | sì | 29:26.9 | 4.0 s |
| 4b · Prof + slide argomento 4 (tratto 1) | sì | 29:30.5 | 109.3 s |
| 4c · Approfondimento animato argomento 4 · voce Kore | sì | 31:19.4 | 26.5 s |
| 4b · Prof + slide argomento 4 (tratto 2) | sì | 31:45.5 | 172.1 s |
| 4c · Approfondimento animato argomento 4 · voce Kore | sì | 34:37.2 | 31.7 s |
| 4b · Prof + slide argomento 4 (tratto 3) | sì | 35:08.5 | 107.6 s |
| 4d · Mappa del prof argomento 4 (mappa.py, voce Kore) | sì | 36:55.7 | 28.7 s |
| 4e · Pillola di ripasso argomento 4 | sì | 37:24.0 | 11.2 s |
| 4f · Schema guidato argomento 4 | sì | 37:34.8 | 44.4 s |
| 4g · Scheda Quiz 4 | sì | 38:18.8 | 5.0 s |
| 4a · Titolo argomento 5 | sì | 38:23.4 | 4.0 s |
| 4b · Prof + slide argomento 5 (tratto 1) | sì | 38:27.0 | 155.0 s |
| 4c · Approfondimento animato argomento 5 · voce Kore | sì | 41:01.6 | 26.5 s |
| 4b · Prof + slide argomento 5 (tratto 2) | sì | 41:27.7 | 198.7 s |
| 4c · Approfondimento animato argomento 5 · voce Kore | sì | 44:46.0 | 35.6 s |
| 4b · Prof + slide argomento 5 (tratto 3) | sì | 45:21.2 | 101.4 s |
| 4d · Mappa del prof argomento 5 (mappa.py, voce Kore) | sì | 47:02.2 | 24.9 s |
| 4e · Pillola di ripasso argomento 5 | sì | 47:26.6 | 9.3 s |
| 4f · Schema guidato argomento 5 | sì | 47:35.6 | 46.2 s |
| 4g · Scheda Quiz 5 | sì | 48:21.4 | 5.0 s |
| 5 · Glossario | sì | 48:26.0 | 54.0 s |
| 6 · Riepilogo finale + saluto | sì | 49:19.5 | 47.3 s |
| 7 · Finale 5 s (avviso diritti) | sì | 50:06.5 | 5.0 s |

`trans.wav` + dissolvenza (0,4 s; 1,4 s dopo la sigla) a ogni confine tra pezzi [per costruzione]; `titolo.wav`, `repaso.wav`, `quiz.wav` (+0,5 s), `finale.wav` [per costruzione; il solo scatto del quiz è misurato].

## 3 · Confronto con Spagnolo Lez. 1

Immagini: `confronto_Spagnolo.jpg`, `foglio.png` (tutti i pezzi), `controllo_minuti_Parte1.jpg` (un fotogramma ogni 30 s). Schede blu fatte SOLO con `schede_spagnolo.py` a scala 1.0 [misurato]; la didascalia della pillola è il testo della voce Kore parola per parola [per costruzione].

## 4 · Chip e nomi

- Chip sotto il titolo blu: 1: «Fordismo · Jazz · Sogno americano»; 2: «Suffragio · Flappers · Charleston»; 3: «Harding · Ku Klux Klan · Al Capone»; 4: «Wall Street · Hoover · 14 milioni»; 5: «Roosevelt · Keynes · Social Security Act».
- Nomi coerenti in titolo, pillola, schema, quiz e riepilogo [misurato sul foglio].

## 5 · Problemi trovati e correzioni

| Dove | Tipo | Com'era | Correzione |
|---|---|---|---|
| Copertina | visivo | Titolo della lezione 5 («La Rivoluzione russa…») al posto di quello della lezione 7 (errore mio nella consegna del 18/11) | Titolo esatto: «Gli Stati Uniti: dal boom economico al New Deal» |
| Slide del prof | visivo | Una pagina ferma fino a 6 minuti, una card sola su slide | Tratti + approfondimenti + pagine a 2–3 card (vedi 1b) |
| Mappe | visivo | Ritaglio dell'immagine del prof a fasce | Ridisegnate con `mappa.py` |
| Tutto | altro | Container riavviato a metà lavoro | Audio, webcam, trascrizione rifatti dall'originale; nessun effetto sul risultato |

## 6 · DA CONFERMARE COL PROF

1. «**Giovedì nero 24 ottobre / martedì nero 29**» nel parlato; la slide scrive «il 14 e il 29 ottobre»: il «14» sembra un errore di battitura della slide (il Giovedì nero è il 24). Nelle schede e nei sottotitoli ho tenuto quanto dice il prof (24 e 29).
2. Il suffragio femminile del 1920 è riportato come dice la slide.

## 7 · Cosa NON ho verificato

- I sottotitoli sono corretti sul **testo** della trascrizione, **non** riascoltati; i 60 segmenti dubbi (indici trascrizione: 10, 29, 31, 68, 71, 84, 87, 89, 96, 97, 102, 121, 122, 129, 130, 146, 148, 160, 161, 165, 166, 172, 176, 185, 186, 189, 192, 193, 206, 207, 210, 212, 233, 237, 239, 243, 250, 252, 253, 260, 261, 262, 264, 273, 280, 281, 291, 292, 295, 296, 300, 302, 309, 310, 313, 318, 324, 325, 331, 335) restano con la mia migliore lettura [non verificato].
- Sincronia del bordo giallo non ricontrollata a campione in questa versione [non verificato].
- Sfasamento audio/labbra non misurato in modo affidabile [non verificato].
- Webcam del prof: 184×138 px ingrandita a 410×308: **morbida** (limite dell'originale).
- Non ho verificato la correttezza storica di quanto dice il prof oltre al punto 6.

## 8 · Come ho verificato

Trascrizione con `trascrivi.py`; allineamento delle card al parlato sui tempi della trascrizione; audio del prof dall'originale con la catena del kit; misure con `controllo_finale.py`, `controllo_jingle.py`, `ebur128` sul file finale; foglio dei pezzi e fotogrammi ogni 30 s guardati a occhio.

## 9 · Tempi nel video nuovo (per la pagina)

**Parte unica** (durata 3011.467 s): arg. 1 «I ruggenti anni Venti»: inizio 137.367 s, quiz 811.733 s; arg. 2 «Le donne e le flappers»: inizio 816.333 s, quiz 1103.667 s; arg. 3 «Isolazionismo, razzismo e proibizionismo»: inizio 1108.267 s, quiz 1762.3 s; arg. 4 «Il crollo del 1929 e la Grande Depressione»: inizio 1766.9 s, quiz 2298.8 s; arg. 5 «Il New Deal di Roosevelt»: inizio 2303.4 s, quiz 2901.367 s
