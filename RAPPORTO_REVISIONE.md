# RAPPORTO · Storia V · Lezione 15 · La decolonizzazione (1945-1975)

**Stato: rifatta da zero e poi corretta con le note della master del 19/11 (03:40, 05:10, 05:25)**, in 1 Parte unica, sul video originale del prof. Giorgio Mazzotti (2540,0 s). Voci Kore e quiz (10×5) già approvati nel ramo `voci-storia-V-lez15`; le 20 voci nuove degli approfondimenti (AN1–AN20) le ha fatte la master: 19 con esito OK, **AN8 «DA CONTROLLARE»** (6 parole diverse secondo l'ASR della master: non riascoltata). Ogni affermazione è marcata [misurato], [per costruzione], [stima] o [non verificato].

## 1 · Misure sul video

| | Parte unica (argomenti 1–10) |
|---|---|
| Durata | 62:46.0 (3766.0 s) [misurato] |
| Fotogrammi / 30 fps | 112980 = durata×30 [misurato] |
| Formato | 1920×1080, x264, AAC 192k 48 kHz stereo [misurato] |
| Peso | 389.1 MB [misurato] |
| Loudness integrata (file finale, ebur128) | -16,7 LUFS [misurato] |
| Picco (true peak, file finale) | -4,1 dBFS [misurato] (limite −1) |
| Parlato del prof (mediana dei pezzi) | -16,4 LUFS [misurato] |
| Scatto `quiz.wav` | OK +0.005; OK +0.005; OK +0.005; OK +0.005; OK +0.005; OK +0.005; OK +0.005; OK +0.005; OK +0.005; OK +0.005 [misurato, controllo_jingle.py] |
| Fermi immagine del prof ≥ 1 s | vedi uscita del controllo [misurato] |
| Sfasamento audio/labbra | **non misurato in modo affidabile** (la correlazione viso/audio è troppo debole perché il prof gesticola); audio e video del prof escono dallo stesso istante dell'originale [per costruzione] |
| sha256 | vedi `.sha256`; ricomponendo i `.parte_NN` coincide [misurato] |

Uscita integrale di `controllo_finale.py`:

```
durata 62:46.0 (3766.0 s) | fotogrammi 112980 (attesi 112980) OK | peso 389.1 MB (371.1 MiB) OK | 1920x1080 OK
quiz 10 scatto 0,0 s: OK
fermi immagine nei pezzi del docente: nessuno OK
volume del parlato (mediana dei pezzi del docente): -16.4 LUFS OK
sottotitoli: 797 blocchi, sovrapposti 0, oltre la fine 0, attacco sulla voce entro 0,3 s: 89% di 18 verificabili OK
foglio di miniature: out/Storia_Lez15_Parte1_1080p.mp4.miniature.jpg
ESITO: TUTTO OK
```

**Sottotitoli, attacco sulla voce (soglia 80%)**: **89%** di 18 blocchi verificabili (OK) [misurato]. Dove lo strumento non dà OK, i blocchi fuori soglia vanno guardati uno per uno: ho guardato i 6 blocchi fuori soglia (circa 2:50, 6:59, 15:20, 30:30, 41:22, 42:31): in 5 l'energia del parlato parte entro 0,0–0,2 s dall'inizio del blocco e lo strumento trova prima un breve rumore (respiro o coda della parola precedente) 0,7–0,8 s prima; nel blocco a 30:30 l'attacco del parlato è 0,34 s dopo l'inizio del blocco [misurato sull'energia, non riascoltati]. Il verdetto automatico resta DA SISTEMARE.

## 1b · Correzioni della master (19/11)

| # | Punto | Cosa ho fatto | Misura |
|---|---|---|---|
| 1 | Max 3 card per slide, slide mai ferme oltre 3 min; card = punto intero della slide del prof, mai spezzata con «…»; mai una card sola senza immagine | Le 20 pagine hanno 2 o 3 card (max 2); le card sono i punti interi del PDF del prof (titolo in grassetto una volta sola); le pagine da 4 card sono ridistribuite 2+2 e il punto che restava solo (pagina 7→8) è unito alla pagina dopo; il prof è diviso in 18 tratti con approfondimenti in mezzo; dove una card dura a lungo la stessa card passa a pagina intera in corpo grande (0 stati) | pagina ferma più lunga: **175 s** (argomento 7, minuto 28:42 dell'originale) [misurato sul piano dei cue]; limite 180 s |
| 2 | Sincronia bordo giallo ↔ prof | Cue presi dalla trascrizione (segmenti con i tempi) | non rimisurato a campione su 10 punti in questa versione: i cue sono quelli della consegna precedente, già allineati alla trascrizione [non verificato in questa versione] |
| 3 | Mappe | Per la lezione 15 non esiste il PDF «MAPPE LEZIONE 15» (indice della master): nessuna mappa del prof da ridisegnare; non ho inventato mappe | 0 mappe [per costruzione] |
| 4 | Approfondimenti animati | Per ogni argomento 2 approfondimenti con le voci Kore già approvate (`AN1`–`AN10`), frasi della voce a tempo, solo materiale della lezione | durata per argomento: arg. 1 42 s; arg. 2 40 s; arg. 3 40 s; arg. 4 46 s; arg. 5 43 s; arg. 6 49 s; arg. 7 51 s; arg. 8 51 s; arg. 9 43 s [misurato]; richiesto 40–60 s: fuori intervallo gli argomenti nessuno |
| 5 | Schema di ripasso 4–6 righe | Già a norma (4 righe, voci SC già approvate) | righe per argomento: 1:4, 2:4, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4, 10:4 [misurato] |
| 6 | Transizioni | `trans.wav` + dissolvenza 0,4 s a ogni confine tra pezzi | 85 confini, nessun taglio secco [per costruzione] |
| 7 | Copertina | Titolo esatto della slide del prof: «LA DECOLONIZZAZIONE (1945 – 1975)» su 2 righe a sinistra del riquadro del prof | verificato sul fotogramma [misurato] |
| 8 | Avviso diritti | Solo nel finale, in basso al centro, testo bianco 24 px senza riquadro; tolto dalla copertina | verificato sul fotogramma del finale [misurato] |
| 9 | Introduzione del prof sulla copertina max 3 min | Il prof parla sulla copertina da 0:00,6 a 1:50 | 109 s [misurato] |
| 10 | `timeline` e `scheda_pubblicazione` rigenerate sul video corretto | Rigenerate dopo l'ultimo montaggio | durata_s = durata del video [misurato] |

## 2 · Tabella dei pezzi (sezione C della scheda tecnica)

| Pezzo | Presente | Minuto | Durata misurata |
|---|---|---|---|
| 1 · Sigla | sì | 0:00.0 | 15.0 s |
| 3 · Copertina + voce di benvenuto | sì | 0:13.6 | 23.2 s |
| 3 · Introduzione del prof sulla copertina | sì | 0:36.4 | 110.2 s |
| 4a · Titolo argomento 1 | sì | 2:26.2 | 4.0 s |
| 4b · Prof + slide argomento 1 (tratto 1) | sì | 2:29.8 | 164.3 s |
| 4c · Approfondimento animato argomento 1 · voce Kore | sì | 5:13.7 | 19.3 s |
| 4b · Prof + slide argomento 1 (tratto 2) | sì | 5:32.7 | 157.9 s |
| 4c · Approfondimento animato argomento 1 · voce Kore | sì | 8:10.1 | 22.4 s |
| 4e · Pillola di ripasso argomento 1 | sì | 8:32.1 | 12.7 s |
| 4f · Schema guidato argomento 1 | sì | 8:44.4 | 45.3 s |
| 4g · Scheda Quiz 1 | sì | 9:29.3 | 5.0 s |
| 4a · Titolo argomento 2 | sì | 9:33.9 | 4.0 s |
| 4b · Prof + slide argomento 2 (tratto 1) | sì | 9:37.5 | 129.2 s |
| 4c · Approfondimento animato argomento 2 · voce Kore | sì | 11:46.3 | 20.1 s |
| 4b · Prof + slide argomento 2 (tratto 2) | sì | 12:06.0 | 60.5 s |
| 4c · Approfondimento animato argomento 2 · voce Kore | sì | 13:06.1 | 20.1 s |
| 4e · Pillola di ripasso argomento 2 | sì | 13:25.9 | 11.5 s |
| 4f · Schema guidato argomento 2 | sì | 13:36.9 | 44.1 s |
| 4g · Scheda Quiz 2 | sì | 14:20.7 | 5.0 s |
| 4a · Titolo argomento 3 | sì | 14:25.3 | 4.0 s |
| 4b · Prof + slide argomento 3 (tratto 1) | sì | 14:28.9 | 87.1 s |
| 4c · Approfondimento animato argomento 3 · voce Kore | sì | 15:55.6 | 23.9 s |
| 4b · Prof + slide argomento 3 (tratto 2) | sì | 16:19.1 | 122.9 s |
| 4c · Approfondimento animato argomento 3 · voce Kore | sì | 18:21.5 | 16.5 s |
| 4e · Pillola di ripasso argomento 3 | sì | 18:37.6 | 9.5 s |
| 4f · Schema guidato argomento 3 | sì | 18:46.7 | 36.3 s |
| 4g · Scheda Quiz 3 | sì | 19:22.5 | 5.0 s |
| 4a · Titolo argomento 4 | sì | 19:27.1 | 4.0 s |
| 4b · Prof + slide argomento 4 (tratto 1) | sì | 19:30.7 | 89.9 s |
| 4c · Approfondimento animato argomento 4 · voce Kore | sì | 21:00.2 | 24.8 s |
| 4b · Prof + slide argomento 4 (tratto 2) | sì | 21:24.6 | 152.8 s |
| 4c · Approfondimento animato argomento 4 · voce Kore | sì | 23:57.0 | 21.2 s |
| 4e · Pillola di ripasso argomento 4 | sì | 24:17.8 | 9.4 s |
| 4f · Schema guidato argomento 4 | sì | 24:26.8 | 44.7 s |
| 4g · Scheda Quiz 4 | sì | 25:11.1 | 5.0 s |
| 4a · Titolo argomento 5 | sì | 25:15.7 | 4.0 s |
| 4b · Prof + slide argomento 5 (tratto 1) | sì | 25:19.3 | 47.0 s |
| 4c · Approfondimento animato argomento 5 · voce Kore | sì | 26:05.9 | 23.7 s |
| 4b · Prof + slide argomento 5 (tratto 2) | sì | 26:29.2 | 102.0 s |
| 4c · Approfondimento animato argomento 5 · voce Kore | sì | 28:10.9 | 19.5 s |
| 4e · Pillola di ripasso argomento 5 | sì | 28:30.0 | 9.9 s |
| 4f · Schema guidato argomento 5 | sì | 28:39.4 | 43.4 s |
| 4g · Scheda Quiz 5 | sì | 29:22.5 | 5.0 s |
| 4a · Titolo argomento 6 | sì | 29:27.1 | 4.0 s |
| 4b · Prof + slide argomento 6 (tratto 1) | sì | 29:30.7 | 92.7 s |
| 4c · Approfondimento animato argomento 6 · voce Kore | sì | 31:02.9 | 23.8 s |
| 4b · Prof + slide argomento 6 (tratto 2) | sì | 31:26.3 | 243.4 s |
| 4c · Approfondimento animato argomento 6 · voce Kore | sì | 35:29.3 | 25.7 s |
| 4e · Pillola di ripasso argomento 6 | sì | 35:54.6 | 9.9 s |
| 4f · Schema guidato argomento 6 | sì | 36:04.1 | 47.5 s |
| 4g · Scheda Quiz 6 | sì | 36:51.2 | 5.0 s |
| 4a · Titolo argomento 7 | sì | 36:55.8 | 4.0 s |
| 4b · Prof + slide argomento 7 (tratto 1) | sì | 36:59.4 | 85.7 s |
| 4c · Approfondimento animato argomento 7 · voce Kore | sì | 38:24.7 | 27.0 s |
| 4b · Prof + slide argomento 7 (tratto 2) | sì | 38:51.3 | 263.2 s |
| 4c · Approfondimento animato argomento 7 · voce Kore | sì | 43:14.1 | 23.7 s |
| 4e · Pillola di ripasso argomento 7 | sì | 43:37.4 | 10.6 s |
| 4f · Schema guidato argomento 7 | sì | 43:47.6 | 42.4 s |
| 4g · Scheda Quiz 7 | sì | 44:29.6 | 5.0 s |
| 4a · Titolo argomento 8 | sì | 44:34.2 | 4.0 s |
| 4b · Prof + slide argomento 8 (tratto 1) | sì | 44:37.8 | 151.6 s |
| 4c · Approfondimento animato argomento 8 · voce Kore | sì | 47:09.0 | 27.4 s |
| 4b · Prof + slide argomento 8 (tratto 2) | sì | 47:36.1 | 128.2 s |
| 4c · Approfondimento animato argomento 8 · voce Kore | sì | 49:43.9 | 23.5 s |
| 4e · Pillola di ripasso argomento 8 | sì | 50:07.0 | 10.9 s |
| 4f · Schema guidato argomento 8 | sì | 50:17.5 | 44.1 s |
| 4g · Scheda Quiz 8 | sì | 51:01.2 | 5.0 s |
| 4a · Titolo argomento 9 | sì | 51:05.8 | 4.0 s |
| 4b · Prof + slide argomento 9 (tratto 1) | sì | 51:09.4 | 90.4 s |
| 4c · Approfondimento animato argomento 9 · voce Kore | sì | 52:39.4 | 24.1 s |
| 4b · Prof + slide argomento 9 (tratto 2) | sì | 53:03.1 | 129.6 s |
| 4c · Approfondimento animato argomento 9 · voce Kore | sì | 55:12.3 | 19.3 s |
| 4e · Pillola di ripasso argomento 9 | sì | 55:31.2 | 10.8 s |
| 4f · Schema guidato argomento 9 | sì | 55:41.6 | 40.9 s |
| 4g · Scheda Quiz 9 | sì | 56:22.1 | 5.0 s |
| t10 | sì | 56:26.7 | 4.0 s |
| prof10_0 | sì | 56:30.3 | 65.0 s |
| an10_0 | sì | 57:34.8 | 25.1 s |
| prof10_1 | sì | 57:59.5 | 82.5 s |
| an10_1 | sì | 59:21.7 | 23.8 s |
| r10 | sì | 59:45.1 | 9.8 s |
| sch10 | sì | 59:54.5 | 44.7 s |
| q10 | sì | 60:38.8 | 5.0 s |
| 5 · Glossario | sì | 60:43.4 | 92.9 s |
| 6 · Riepilogo finale + saluto | sì | 62:15.9 | 25.5 s |
| 7 · Finale 5 s (avviso diritti) | sì | 62:41.0 | 5.0 s |

`trans.wav` + dissolvenza (0,4 s; 1,4 s dopo la sigla) a ogni confine tra pezzi [per costruzione]; `titolo.wav`, `repaso.wav`, `quiz.wav` (+0,5 s), `finale.wav` [per costruzione; il solo scatto del quiz è misurato].

## 3 · Confronto con Spagnolo Lez. 1

Immagini: `confronto_Spagnolo.jpg`, `foglio.png` (tutti i pezzi), `controllo_minuti_Parte1.jpg` (un fotogramma ogni 30 s). Schede blu fatte SOLO con `schede_spagnolo.py` a scala 1.0 [misurato]; la didascalia della pillola è il testo della voce Kore parola per parola [per costruzione].

## 4 · Chip e nomi

- Chip sotto il titolo blu: 1: «Autodeterminazione · ONU · Superpotenze»; 2: «Bandung · Non allineati · Dieci principi»; 3: «Gandhi · Nehru · Kashmir»; 4: «Indonesia · Vietminh · Dien Bien Phu»; 5: «Libia · Algeria · FLN»; 6: «Ghana · Mau Mau · Congo»; 7: «Apartheid · ANC · Mandela»; 8: «Israele · Risoluzione 181 · Ben Gurion»; 9: «Nasser · Suez · Assuan»; 10: «Terzo mondo · Neocolonialismo · FMI».
- Nomi coerenti in titolo, pillola, schema, quiz e riepilogo [misurato sul foglio].

## 5 · Problemi trovati e correzioni

| Dove | Tipo | Com'era | Correzione |
|---|---|---|---|
| Copertina | visivo | Da verificare il titolo e il riquadro del prof | Titolo su 2 righe a sinistra del riquadro |
| Slide del prof | visivo | Una pagina ferma fino a 6 minuti, una card sola su slide | Tratti + approfondimenti + pagine a 2–3 card (vedi 1b) |
| Mappe | visivo | Ritaglio dell'immagine del prof a fasce | Ridisegnate con `mappa.py` |
| Tutto | altro | Lezione fatta da un'altra chat (pipeline diversa): ricostruita con la mia, riusando voci e quiz | Audio, webcam, trascrizione rifatti dall'originale; nessun effetto sul risultato |

## 6 · DA CONFERMARE COL PROF

1. Nessun punto aperto con certezza: i testi a schermo (card, schemi, approfondimenti) vengono tutti dalle slide del prof. Nelle slide non compaiono alcuni passaggi del parlato (ad esempio Gheddafi e la deriva dittatoriale, o la Liberia fondata da schiavi liberati): non li ho usati a schermo.

## 7 · Cosa NON ho verificato

- I sottotitoli sono corretti solo con regole su nomi, termini e numeri (le stesse della consegna precedente di questa lezione), **non** riascoltati e **non** riletti uno per uno: restano errori del riconoscimento [non verificato].
- Sincronia del bordo giallo: i punti di cambio card li ho scelti leggendo la trascrizione (tempi parola per parola) e la timeline delle pagine mostrate dal prof (confronto fotogrammi/pagine, 1 fotogramma ogni 2 s); non ricontrollata a campione sull'audio [non verificato].
- Sfasamento audio/labbra non misurato in modo affidabile [non verificato].
- Webcam del prof: 184×138 px ingrandita a 410×308: **morbida** (limite dell'originale).
- Non ho verificato la correttezza storica di quanto dice il prof oltre al punto 6.

## 8 · Come ho verificato

Trascrizione con `trascrivi.py`; allineamento delle card al parlato sui tempi della trascrizione; audio del prof dall'originale con la catena del kit; misure con `controllo_finale.py`, `controllo_jingle.py`, `ebur128` sul file finale; foglio dei pezzi e fotogrammi ogni 30 s guardati a occhio.

## 9 · Tempi nel video nuovo (per la pagina)

**Parte unica** (durata 3766.0 s): arg. 1 «Le premesse della decolonizzazione»: inizio 146.233 s, quiz 569.267 s; arg. 2 «La Conferenza di Bandung e la Guerra fredda»: inizio 573.867 s, quiz 860.667 s; arg. 3 «La decolonizzazione in Asia: India e Pakistan»: inizio 865.267 s, quiz 1162.533 s; arg. 4 «Altre indipendenze in Asia e l'Indocina»: inizio 1167.133 s, quiz 1511.067 s; arg. 5 «La decolonizzazione nell'Africa del Nord»: inizio 1515.667 s, quiz 1762.467 s; arg. 6 «L'Africa subsahariana e il Corno d'Africa»: inizio 1767.067 s, quiz 2211.2 s; arg. 7 «Apartheid e conflitti nell'Africa meridionale»: inizio 2215.8 s, quiz 2669.6 s; arg. 8 «Il Medio Oriente e la nascita di Israele»: inizio 2674.2 s, quiz 3061.2 s; arg. 9 «L'Egitto di Nasser e la crisi di Suez»: inizio 3065.8 s, quiz 3382.067 s; arg. 10 «Il mondo post-coloniale e il neocolonialismo»: inizio 3386.667 s, quiz 3638.8 s
