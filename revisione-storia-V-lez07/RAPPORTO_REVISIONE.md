# RAPPORTO · Storia V · Lezione 7 · Gli Stati Uniti dal boom economico al New Deal

**Stato: rifatta da zero, Parte unica** sul video originale del prof. Della consegna precedente ho riusato solo le voci Kore già fatte (benvenuto, glossario, riepilogo e saluto) e i quiz (5×5). Ogni affermazione è etichettata **[misurato]**, **[stima]** o **[non verificato]**.

## 1 · Misure sul video

| | Parte unica (argomenti 1–5) |
|---|---|
| Durata | 45:02.0 (2702.0 s): sotto i 50 minuti perché il prof dura 36 minuti [misurato] |
| Fotogrammi / 30 fps | 81061 = durata×30 [misurato] |
| Formato | 1920×1080, x264 veryfast CRF 19, keyint 60, AAC 192k 48 kHz [misurato] |
| Peso | 365,6 MB [misurato] |
| Loudness integrata (file finale) | −16,7 LUFS [misurato] |
| Picco (true peak, file finale) | −4,2 dBFS [misurato] (limite −1) |
| Parlato del prof (mediana dei pezzi) | −16,6 LUFS [misurato] |
| Scatto `quiz.wav` | 5 quiz a +0,005 s dall'atteso [misurato, controllo_jingle.py] |
| Fermi immagine del prof ≥ 1 s | nessuno [misurato, controllo_finale.py] |
| Sfasamento audio/labbra | −15 ms (correlazione dell'inviluppo, 3 punti: min 5, 20, 33) [misurato, limite 40 ms] |
| sha256 | vedi `.sha256`; ricomponendo i `.parte_NN` coincide [misurato] |

Uscita integrale di `controllo_finale.py`:

```
durata 45:02.0 (2702.0 s) | fotogrammi 81061 (attesi 81061) OK | peso 365.6 MB (348.7 MiB) OK | 1920x1080 OK
quiz 5 scatto 0,0 s: OK
fermi immagine nei pezzi del docente: nessuno OK
volume del parlato (mediana dei pezzi del docente): -16.6 LUFS OK
sottotitoli: 619 blocchi, sovrapposti 0, oltre la fine 0, attacco sulla voce entro 0,3 s: 75% di 12 verificabili DA GUARDARE
foglio di miniature: out/Storia_Lez7_Parte1_1080p.mp4.miniature.jpg
ESITO: DA SISTEMARE: sottotitoli
```

**Sottotitoli: lo strumento dà «DA SISTEMARE».** L'attacco dei sottotitoli sulla voce entro 0,3 s risulta **75% di 12 blocchi verificabili** (soglia 80%) [misurato]. I 3 blocchi che lo strumento segna fuori (a 2:33,6, 17:48,7 e 30:20,2) li ho controllati a mano sul profilo di energia dell'audio: il parlato comincia esattamente all'attacco del blocco (differenza < 0,1 s); lo scarto di −0,8 s dello strumento è causato da un picco della parola precedente all'inizio della sua finestra. Non l'ho nascosto: l'esito automatico resta «DA SISTEMARE» [misurato a mano].

## 2 · Tabella dei pezzi (sezione C della scheda tecnica)

| Pezzo | Presente | Minuto | Durata misurata |
|---|---|---|---|
| 1 · Sigla | sì | 0:00.0 | 15.0 s |
| 3 · Copertina + voce di benvenuto | sì | 0:13.6 | 15.2 s |
| 3 · Introduzione del prof sulla copertina (riquadro del prof) | sì | 0:28.4 | 109.2 s |
| 4a · Titolo argomento 1 | sì | 2:17.2 | 4.0 s |
| 4b · Prof + slide argomento 1 | sì | 2:20.8 | 559.0 s |
| 4c · Approfondimenti animati argomento 1 | no (non necessari: il prof copre già tutto) | – | – |
| 4d · Mappa del prof argomento 1 | no (il prof non ha mappa per questo argomento: non inventata) | – | – |
| 4e · Pillola di ripasso argomento 1 | sì | 11:39.4 | 9.5 s |
| 4f · Schema guidato argomento 1 | sì | 11:48.4 | 41.8 s |
| 4g · Scheda Quiz 1 | sì | 12:29.9 | 5.0 s |
| 4a · Titolo argomento 2 | sì | 12:34.5 | 4.0 s |
| 4b · Prof + slide argomento 2 | sì | 12:38.1 | 186.0 s |
| 4c · Approfondimenti animati argomento 2 | no (non necessari: il prof copre già tutto) | – | – |
| 4d · Mappa del prof argomento 2 | no (il prof non ha mappa per questo argomento: non inventata) | – | – |
| 4e · Pillola di ripasso argomento 2 | sì | 15:43.7 | 12.0 s |
| 4f · Schema guidato argomento 2 | sì | 15:55.3 | 38.2 s |
| 4g · Scheda Quiz 2 | sì | 16:33.0 | 5.0 s |
| 4a · Titolo argomento 3 | sì | 16:37.6 | 4.0 s |
| 4b · Prof + slide argomento 3 | sì | 16:41.2 | 485.7 s |
| 4c · Approfondimenti animati argomento 3 | no (non necessari: il prof copre già tutto) | – | – |
| 4d · Mappa del prof argomento 3 | sì | 24:46.5 | 34.0 s |
| 4e · Pillola di ripasso argomento 3 | sì | 25:20.1 | 10.5 s |
| 4f · Schema guidato argomento 3 | sì | 25:30.3 | 45.7 s |
| 4g · Scheda Quiz 3 | sì | 26:15.5 | 5.0 s |
| 4a · Titolo argomento 4 | sì | 26:20.1 | 4.0 s |
| 4b · Prof + slide argomento 4 | sì | 26:23.7 | 387.3 s |
| 4c · Approfondimenti animati argomento 4 | no (non necessari: il prof copre già tutto) | – | – |
| 4d · Mappa del prof argomento 4 | sì | 32:50.6 | 27.6 s |
| 4e · Pillola di ripasso argomento 4 | sì | 33:17.9 | 11.2 s |
| 4f · Schema guidato argomento 4 | sì | 33:28.7 | 44.4 s |
| 4g · Scheda Quiz 4 | sì | 34:12.6 | 5.0 s |
| 4a · Titolo argomento 5 | sì | 34:17.2 | 4.0 s |
| 4b · Prof + slide argomento 5 | sì | 34:20.8 | 453.4 s |
| 4c · Approfondimenti animati argomento 5 | no (non necessari: il prof copre già tutto) | – | – |
| 4d · Mappa del prof argomento 5 | sì | 41:53.8 | 23.8 s |
| 4e · Pillola di ripasso argomento 5 | sì | 42:17.2 | 9.3 s |
| 4f · Schema guidato argomento 5 | sì | 42:26.1 | 46.2 s |
| 4g · Scheda Quiz 5 | sì | 43:11.9 | 5.0 s |
| 5 · Glossario | sì | 43:16.5 | 54.0 s |
| 6 · Riepilogo finale + saluto | sì | 44:10.1 | 47.3 s |
| 7 · Finale 5 s | sì | 44:57.0 | 5.0 s |

`trans.wav` + dissolvenza (0,4 s; 1,4 s dopo la sigla) a ogni cambio di pezzo [per costruzione]; `titolo.wav`, `repaso.wav`, `quiz.wav` (+0,5 s), `finale.wav` [per costruzione; il solo scatto del quiz è misurato].

## 3 · Confronto con Spagnolo Lez. 1

Immagine: `confronto_Spagnolo.jpg`. Schede blu fatte SOLO con `schede_spagnolo.py` a scala 1.0 [misurato]. Differenze dichiarate:

- Pillola blu: 9–12 s invece di 14 s; il testo mostrato è la frase della voce, parola per parola (nella pillola 4 la voce dice le date in lettere, e così è mostrata).
- Schema guidato: 30–45 s invece di ≈46 s.
- Riepilogo finale + saluto: 47 s invece di 12–35 s (sulla stessa scheda ho tenuto la voce di chiusura già pronta).
- Pannello «PAROLE CHIAVE»: aggiunta approvata, tenuta. Approfondimenti 4c: non fatti.
- Mappe del prof: 3 (argomenti 3, 4, 5) su 5 argomenti; per gli argomenti 1 e 2 il prof non ne ha mandate.

## 4 · Controlli obbligatori del prompt v3

- **Chip**: «Fordismo · Jazz · Sogno americano», «Suffragio · Flappers · Charleston», «Harding · Ku Klux Klan · Al Capone», «Wall Street · Hoover · 14 milioni», «Roosevelt · Keynes · Social Security Act» [misurato a vista nel `foglio.png`].
- **Didascalia pillola** = testo della voce Kore parola per parola (da `testi_voci.json`, non da OCR) [misurato: `foglio.png`, 2 didascalie per pillola].
- **Argomento lungo** nel quiz: `tfs` ricalcolato sulla lunghezza: nessun titolo tocca il pulsante play [misurato a vista nel `foglio.png`].
- **Riepilogo finale**: ultimo fotogramma con TUTTE e 5 le card [misurato a vista].
- **Nomi e titoli** uguali in schede, quiz (`quiz_argomenti.json` aggiornato), copertina, slide [misurato a vista].
- **Foglio di controllo**: `foglio.png`. **Tempi**: i Quiz cadono ai `quiz_s` della scheda di pubblicazione (+0,005 s) [misurato].

## 5 · Problemi trovati e correzioni

| Minuto | Tipo | Com'era | Correzione |
|---|---|---|---|
| Tutto | testo | Trascrizione automatica con errori su nomi e parole («Coover», «Flectors», «Ku Klux Clan», «tailorista», «sog americano»…) e disturbi | 111 segmenti corretti a mano, correzioni globali, 22 righe di disturbo tolte (`subs_fix_sottotitoli.py`) |
| P1 6:49–9:00 | visivo | Il prof parla del «sogno americano» (slide 3) prima del jazz | Card accese nell'ordine del parlato, non della slide |
| P1 12:40–14:00 | altro | Nell'argomento 2 il prof passa ~100 s sulle disuguaglianze (salari bassi, crisi agricola) senza una card dedicata | Resta accesa l'ultima card: nessuna card inventata |
| Tutto | altro | Container riavviato a metà lavoro | Ripresi i file conservati; nessun effetto sul risultato |

## 6 · DA CONFERMARE COL PROF

1. «**Giovedì nero 24 ottobre / martedì nero 29**» nel parlato; la slide scrive «il 14 e il 29 ottobre»: il «14» sembra un errore di battitura della slide (il Giovedì nero è il 24). Nelle schede e nei sottotitoli ho tenuto quanto dice il prof (24 e 29).
2. Nella voce di ripasso dell'argomento 2 è riportato il suffragio del 1920 come dice la slide.

## 7 · Cosa NON ho verificato

- Sottotitoli corretti sul **testo**, **non** riascoltati uno per uno; 60 segmenti dubbi lasciati come li scrive la macchina (lista `DUBBI` nel file) [non verificato].
- Webcam: 184×138 px ingrandita 2,2×: **morbida**; testa tagliata in alto nell'originale [misurato a vista].
- PDF slide (24 pagine) e mappe (3 pagine): stessa grafica del video senza riquadro (il pannello «PAROLE CHIAVE» resta); **non** ho confrontato pagina per pagina con i fotogrammi [non verificato].
- Quiz: i 25 quesiti erano nel ramo `voci-…`; riletti solo a campione [non verificato]. Verifica = Excel del prof (10 domande) invariato; compiti = PDF del prof (4 domande) invariato [misurato].
- Suono `trans.wav` ai confini: per costruzione, non ascoltato [non verificato].

## 8 · Come ho verificato

Trascrizione con `trascrivi.py` (355 segmenti); allineamento delle card al parlato con confronto automatico di parole chiave e controllo sul testo; audio del prof rifatto dall'originale con la catena del kit; `controllo_finale.py`, `controllo_jingle.py`, ebur128; fotogrammi ogni 30 s (`controllo_minuti_Parte1.jpg`), `foglio.png`, `confronto_Spagnolo.jpg`.

## 9 · Tempi nel video nuovo

Durata 2702.033 s: arg. 1 «I ruggenti anni Venti»: inizio 137.167 s, quiz 749.867 s; arg. 2 «Le donne e le flappers»: inizio 754.467 s, quiz 993.033 s; arg. 3 «Isolazionismo, razzismo e proibizionismo»: inizio 997.633 s, quiz 1575.533 s; arg. 4 «Il crollo del 1929 e la Grande Depressione»: inizio 1580.133 s, quiz 2052.633 s; arg. 5 «Il New Deal di Roosevelt»: inizio 2057.233 s, quiz 2591.933 s

La durata è cambiata rispetto alla consegna precedente (53 minuti): i secondi vecchi non valgono più.
