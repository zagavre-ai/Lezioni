# RAPPORTO · Storia V · Lezione 5 · La Rivoluzione russa e la nascita dell'URSS (1917-1922)

**Stato: rifatta da zero in 2 Parti** sul video originale del prof. Della consegna precedente ho riusato solo le voci Kore già fatte (ripasso della Parte 1, glossario, riepilogo e saluti) e i quiz (9×5) del ramo `voci-storia-V-lez05`. Ogni affermazione è etichettata **[misurato]**, **[stima]** o **[non verificato]**.

## 1 · Misure sul video

| | Parte 1 (argomenti 1–4) | Parte 2 (argomenti 5–9) |
|---|---|---|
| Durata | 41:26.9 (2486.9 s) [misurato] | 30:41.4 (1841.4 s) [misurato] |
| Fotogrammi / 30 fps | 74608 = durata×30 [misurato] | 55242 = durata×30 [misurato] |
| Formato | 1920×1080, x264 veryfast CRF 19, keyint 60, AAC 192k 48 kHz [misurato] | idem |
| Peso | 333,6 MB [misurato] | 233,6 MB [misurato] |
| Loudness integrata (file finale) | −16,6 LUFS [misurato] | −17,0 LUFS [misurato] |
| Picco (true peak, file finale) | −4,1 dBFS [misurato] | −4,1 dBFS [misurato] (limite −1) |
| Parlato del prof (mediana dei pezzi) | −16,3 LUFS [misurato] | −16,7 LUFS [misurato] |
| Scatto `quiz.wav` | 4 quiz a +0,005 s dall'atteso [misurato, controllo_jingle.py] | 5 quiz a +0,005 s [misurato] |
| Fermi immagine del prof ≥ 1 s | nessuno [misurato, controllo_finale.py] | nessuno [misurato] |
| Sfasamento audio/labbra | −15 ms (correlazione dell'inviluppo, 3 punti: min 5, 25, 50) [misurato, limite 40 ms] | idem |
| sha256 | vedi `.sha256`; ricomponendo i `.parte_NN` coincide [misurato] | idem |

Uscita integrale di `controllo_finale.py`:

```
Parte 1
durata 41:26.9 (2486.9 s) | fotogrammi 74608 (attesi 74608) OK | peso 333.6 MB (318.1 MiB) OK | 1920x1080 OK
quiz 4 scatto 0,0 s: OK
fermi immagine nei pezzi del docente: nessuno OK
volume del parlato (mediana dei pezzi del docente): -16.3 LUFS OK
sottotitoli: 585 blocchi, sovrapposti 0, oltre la fine 0, attacco sulla voce entro 0,3 s: 86% di 14 verificabili OK
foglio di miniature: out/Storia_Lez5_Parte1_1080p.mp4.miniature.jpg
ESITO: TUTTO OK

Parte 2
durata 30:41.4 (1841.4 s) | fotogrammi 55242 (attesi 55242) OK | peso 233.6 MB (222.8 MiB) OK | 1920x1080 OK
quiz 5 scatto 0,0 s: OK
fermi immagine nei pezzi del docente: nessuno OK
volume del parlato (mediana dei pezzi del docente): -16.7 LUFS OK
sottotitoli: 398 blocchi, sovrapposti 0, oltre la fine 0, attacco sulla voce entro 0,3 s: 87% di 23 verificabili OK
foglio di miniature: out/Storia_Lez5_Parte2_1080p.mp4.miniature.jpg
ESITO: TUTTO OK
```

Attacco dei sottotitoli sulla voce (soglia 80%): Parte 1 **86%** di 14 blocchi verificabili, Parte 2 **87%** di 23 [misurato]. Ho dovuto correggere l'allineamento dopo le prime misure (65% e 64%): l'inizio dei blocchi che seguono una pausa è allineato all'attacco misurato del parlato [misurato].

## 2 · Tabella dei pezzi (sezione C della scheda tecnica)

| Pezzo | Presente | Minuto (Parte) | Durata misurata |
|---|---|---|---|
| 1 · Sigla (P1) | sì | P1 0:00.0 | 15.0 s |
| 3 · Copertina + voce di benvenuto | sì | P1 0:13.6 | 13.5 s |
| 3 · Introduzione del prof sulla copertina (riquadro del prof) | sì | P1 0:26.7 | 193.9 s |
| 4a · Titolo argomento 1 | sì | P1 3:40.2 | 4.0 s |
| 4b · Prof + slide argomento 1 | sì | P1 3:43.8 | 344.0 s |
| 4c · Approfondimenti animati argomento 1 | no (non necessari: il prof copre già tutto) | – | – |
| 4d · Mappa del prof argomento 1 | no (il prof non ha mappa per questo argomento: non inventata) | – | – |
| 4e · Pillola di ripasso argomento 1 | sì | P1 9:27.4 | 8.6 s |
| 4f · Schema guidato argomento 1 | sì | P1 9:35.6 | 33.1 s |
| 4g · Scheda Quiz 1 | sì | P1 10:08.4 | 5.0 s |
| 4a · Titolo argomento 2 | sì | P1 10:13.0 | 4.0 s |
| 4b · Prof + slide argomento 2 | sì | P1 10:16.6 | 553.7 s |
| 4c · Approfondimenti animati argomento 2 | no (non necessari: il prof copre già tutto) | – | – |
| 4d · Mappa del prof argomento 2 | sì | P1 19:29.9 | 27.6 s |
| 4e · Pillola di ripasso argomento 2 | sì | P1 19:57.1 | 8.6 s |
| 4f · Schema guidato argomento 2 | sì | P1 20:05.3 | 31.0 s |
| 4g · Scheda Quiz 2 | sì | P1 20:35.9 | 5.0 s |
| 4a · Titolo argomento 3 | sì | P1 20:40.5 | 4.0 s |
| 4b · Prof + slide argomento 3 | sì | P1 20:44.1 | 469.4 s |
| 4c · Approfondimenti animati argomento 3 | no (non necessari: il prof copre già tutto) | – | – |
| 4d · Mappa del prof argomento 3 | no (il prof non ha mappa per questo argomento: non inventata) | – | – |
| 4e · Pillola di ripasso argomento 3 | sì | P1 28:33.1 | 9.6 s |
| 4f · Schema guidato argomento 3 | sì | P1 28:42.3 | 34.8 s |
| 4g · Scheda Quiz 3 | sì | P1 29:16.7 | 5.0 s |
| 4a · Titolo argomento 4 | sì | P1 29:21.3 | 4.0 s |
| 4b · Prof + slide argomento 4 | sì | P1 29:24.9 | 548.8 s |
| 4c · Approfondimenti animati argomento 4 | no (non necessari: il prof copre già tutto) | – | – |
| 4d · Mappa del prof argomento 4 | sì | P1 38:33.3 | 18.5 s |
| 4e · Pillola di ripasso argomento 4 | sì | P1 38:51.4 | 10.3 s |
| 4f · Schema guidato argomento 4 | sì | P1 39:01.3 | 31.1 s |
| 4g · Scheda Quiz 4 | sì | P1 39:32.0 | 5.0 s |
| 5 · Glossario (P1) | sì | P1 39:36.6 | 56.9 s |
| 6 · Riepilogo finale (P1) + saluto | sì | P1 40:33.1 | 49.2 s |
| 7 · Finale 5 s (P1) | sì | P1 41:21.9 | 5.0 s |
| 1 · Sigla (P2) | sì | P2 0:00.0 | 15.0 s |
| 3 · Copertina + voce di benvenuto + ripasso della Parte 1 | sì | P2 0:13.6 | 71.4 s |
| 4a · Titolo argomento 5 | sì | P2 1:24.6 | 4.0 s |
| 4b · Prof + slide argomento 5 | sì | P2 1:28.2 | 276.6 s |
| 4c · Approfondimenti animati argomento 5 | no (non necessari: il prof copre già tutto) | – | – |
| 4d · Mappa del prof argomento 5 | no (il prof non ha mappa per questo argomento: non inventata) | – | – |
| 4e · Pillola di ripasso argomento 5 | sì | P2 6:04.4 | 8.7 s |
| 4f · Schema guidato argomento 5 | sì | P2 6:12.7 | 33.0 s |
| 4g · Scheda Quiz 5 | sì | P2 6:45.3 | 5.0 s |
| 4a · Titolo argomento 6 | sì | P2 6:49.9 | 4.0 s |
| 4b · Prof + slide argomento 6 | sì | P2 6:53.5 | 381.9 s |
| 4c · Approfondimenti animati argomento 6 | no (non necessari: il prof copre già tutto) | – | – |
| 4d · Mappa del prof argomento 6 | sì | P2 13:15.0 | 26.4 s |
| 4e · Pillola di ripasso argomento 6 | sì | P2 13:41.1 | 9.7 s |
| 4f · Schema guidato argomento 6 | sì | P2 13:50.4 | 34.0 s |
| 4g · Scheda Quiz 6 | sì | P2 14:24.0 | 5.0 s |
| 4a · Titolo argomento 7 | sì | P2 14:28.6 | 4.0 s |
| 4b · Prof + slide argomento 7 | sì | P2 14:32.2 | 109.0 s |
| 4c · Approfondimenti animati argomento 7 | no (non necessari: il prof copre già tutto) | – | – |
| 4d · Mappa del prof argomento 7 | no (il prof non ha mappa per questo argomento: non inventata) | – | – |
| 4e · Pillola di ripasso argomento 7 | sì | P2 16:20.8 | 8.5 s |
| 4f · Schema guidato argomento 7 | sì | P2 16:28.9 | 36.7 s |
| 4g · Scheda Quiz 7 | sì | P2 17:05.2 | 5.0 s |
| 4a · Titolo argomento 8 | sì | P2 17:09.8 | 4.0 s |
| 4b · Prof + slide argomento 8 | sì | P2 17:13.4 | 279.4 s |
| 4c · Approfondimenti animati argomento 8 | no (non necessari: il prof copre già tutto) | – | – |
| 4d · Mappa del prof argomento 8 | sì | P2 21:52.4 | 22.7 s |
| 4e · Pillola di ripasso argomento 8 | sì | P2 22:14.7 | 8.5 s |
| 4f · Schema guidato argomento 8 | sì | P2 22:22.8 | 32.7 s |
| 4g · Scheda Quiz 8 | sì | P2 22:55.1 | 5.0 s |
| 4a · Titolo argomento 9 | sì | P2 22:59.7 | 4.0 s |
| 4b · Prof + slide argomento 9 | sì | P2 23:03.3 | 269.7 s |
| 4c · Approfondimenti animati argomento 9 | no (non necessari: il prof copre già tutto) | – | – |
| 4d · Mappa del prof argomento 9 | no (il prof non ha mappa per questo argomento: non inventata) | – | – |
| 4e · Pillola di ripasso argomento 9 | sì | P2 27:32.6 | 10.1 s |
| 4f · Schema guidato argomento 9 | sì | P2 27:42.4 | 33.3 s |
| 4g · Scheda Quiz 9 | sì | P2 28:15.3 | 5.0 s |
| 5 · Glossario (P2) | sì | P2 28:19.9 | 72.8 s |
| 6 · Riepilogo finale (P2) + saluto | sì | P2 29:32.3 | 64.5 s |
| 7 · Finale 5 s (P2) | sì | P2 30:36.4 | 5.0 s |

`trans.wav` + dissolvenza (0,4 s; 1,4 s dopo la sigla) a ogni cambio di pezzo [per costruzione: un confine per pezzo]; `titolo.wav`, `repaso.wav`, `quiz.wav` (+0,5 s), `finale.wav` [per costruzione; il solo scatto del quiz è misurato].

## 3 · Confronto con Spagnolo Lez. 1

Immagine: `confronto_Spagnolo.jpg` (sopra il modello, sotto i nostri fotogrammi). Schede blu fatte SOLO con `schede_spagnolo.py` a scala 1.0 [misurato]. Differenze dichiarate:

- Pillola blu: 8,5–10,3 s invece di 14 s (frasi brevi); il testo mostrato è la frase della voce, parola per parola.
- Schema guidato: circa 30–40 s (4–5 righe, 3 s di pausa dopo ogni riga) invece di ≈46 s.
- Riepilogo finale + saluto: 49 s (Parte 1) e 65 s (Parte 2) invece di 12–35 s: sulla stessa scheda ho tenuto anche la voce di chiusura già pronta.
- Pannello «PAROLE CHIAVE» sotto il prof: aggiunta approvata, tenuta.
- Approfondimenti 4c: non fatti.
- Mappe del prof: 4 (argomenti 2, 4, 6, 8) su 9 argomenti; per gli altri il prof non ne ha mandate: non le ho inventate.

## 4 · Controlli obbligatori del prompt v3

- **Chip** sotto il titolo blu: parole chiave vere (persone, luoghi, date): «Nicola II · Duma · Rasputin», «Pietrogrado · Nicola II · L'vov», «Soviet · Lenin · Tesi di aprile», «Kerenskij · Kornilov · Palazzo d'Inverno», «Čeka · Politburo · Costituente», «Trockij · Armata rossa · Ekaterinburg», «Requisizioni · Mercato nero · Armata rossa», «Kronstadt · Lenin · NEP», «20 dicembre 1922 · Mosca · Stalin» [misurato a vista nel `foglio.png`].
- **Didascalia della pillola** = testo della voce Kore parola per parola (dal `testi_voci.json`, non dall'OCR) [misurato: `foglio.png`, 2 didascalie per pillola].
- **Argomento lungo** nel quiz: formula `tfs` ricalcolata per tutti i quiz: nessun titolo tocca il pulsante play [misurato a vista nel `foglio.png`].
- **Riepilogo finale**: ultimo fotogramma con TUTTE le card (4 in Parte 1, 5 in Parte 2) [misurato a vista].
- **Nomi e titoli** uguali in schede, quiz, compiti e verifica: i titoli degli argomenti sono quelli di titolo blu, pillola, quiz (`quiz_argomenti.json` aggiornato), copertina e slide [misurato a vista].
- **Foglio di controllo**: `foglio.png` (38 fotogrammi). **Tempi**: i Quiz cadono ai `quiz_s` della scheda di pubblicazione (+0,005 s) e durata video = durata audio [misurato].

## 5 · Problemi trovati e correzioni

| Minuto | Tipo | Com'era | Correzione |
|---|---|---|---|
| Tutto | testo | Trascrizione automatica con molti errori sui nomi e sulle date («Rash Putin», «L'ov», «Trozki», «Gresnitovsk», «millenoventosedici»…) e disturbi («Um», «Mm») | 185 segmenti corretti a mano, correzioni globali dei nomi, 32 righe di disturbo tolte (`subs_fix_sottotitoli.py`) |
| Tutto | testo | Sottotitoli che attaccavano in anticipo sulla voce (65%/64% sul controllo) | Inizio dei blocchi allineato all'attacco misurato: 86%/87% |
| P2 2:58 circa | visivo | Card «Diritti di genere» della slide 9 spiegata dal prof durante l'argomento 5 | Pagina dedicata nell'argomento 5, card accesa quando il prof ne parla |
| Tutto | visivo | Slide con 5 card troppo alte per la pagina | Pagine spezzate in a/b (≤4 card per pagina, testo ≥ 28 px) |
| Tutto | altro | Disco pieno a metà lavoro (repository scaricato per intero) | Ripuliti i miei file di lavoro; nessun effetto sulla consegna |

## 6 · DA CONFERMARE COL PROF

1. **Nascita dell'URSS: 20 o 30 dicembre 1922?** La slide del prof (pagina «La nascita dell'URSS e la successione») dice «20 dicembre 1922»; nel parlato il prof dice «30 dicembre 1922» (che è la data storica). Le nostre schede (chip, schema, voce) riportano **20 dicembre** come la slide; i sottotitoli riportano **30 dicembre** come il parlato. Da uniformare dopo la risposta del prof [non corretto].
2. Nomi e date nei sottotitoli: corretti dove evidente; restano 48 segmenti dubbi (elenco in `subs_fix_sottotitoli.py`, lista `DUBBI`).

## 7 · Cosa NON ho verificato

- I sottotitoli sono corretti sul **testo** della trascrizione, **non** riascoltati uno per uno; i 48 segmenti dubbi sono lasciati come li scrive la macchina [non verificato].
- Webcam del prof: 184×138 px ingrandita 2,2× a 410×308: **morbida**; testa già tagliata in alto nell'originale (limite non risolvibile) [misurato a vista].
- PDF slide (38 pagine) e mappe (4 pagine): stessa grafica del video, senza riquadro e fascia col nome (il pannello «PAROLE CHIAVE» resta); **non** ho fatto il confronto pagina per pagina con i fotogrammi [non verificato].
- Quiz: i 45 quesiti erano nel ramo `voci-…`; li ho riletti contro la trascrizione solo a campione [non verificato]. Verifica finale = Excel del prof (10 domande) copiato senza modifiche; compiti = PDF del prof (4 domande) con testo invariato [misurato].
- Le card «Il reclutamento forzato al lavoro» e «La conclusione dei conflitti» (comunismo di guerra) non sono mai accese: il prof non le tratta in quel punto [misurato sulla trascrizione]. Idem la card «Diritti di genere» nell'argomento 6 (trattata nell'argomento 5).
- Suono `trans.wav` ai confini: verificato per costruzione, non ascoltato [non verificato].

## 8 · Come ho verificato

Trascrizione con `trascrivi.py` (562 segmenti); allineamento delle card al parlato con un confronto automatico di parole chiave e controllo a mano sul testo; audio del prof rifatto dall'originale con la catena del kit (`aresample 48000, highpass 80, arnndn, loudnorm −16, alimiter`); `controllo_finale.py` e `controllo_jingle.py` sul video finale; ebur128 per loudness e picco; fotogrammi ogni 30 s (`controllo_minuti_Parte1.jpg`, `_Parte2.jpg`), `foglio.png`, `confronto_Spagnolo.jpg`.

## 9 · Tempi nel video nuovo (per la pagina)

**Parte 1** (durata 2486.933 s): arg. 1 «La crisi della Russia zarista»: inizio 220.233 s, quiz 608.367 s; arg. 2 «La Rivoluzione di Febbraio (1917)»: inizio 612.967 s, quiz 1235.933 s; arg. 3 «Dualismo di potere e Lenin»: inizio 1240.533 s, quiz 1756.733 s; arg. 4 «Dalle giornate di luglio a Ottobre»: inizio 1761.333 s, quiz 2372.0 s

**Parte 2** (durata 1841.4 s): arg. 5 «I primi provvedimenti bolscevichi»: inizio 84.633 s, quiz 405.333 s; arg. 6 «Brest-Litovsk e la guerra civile»: inizio 409.933 s, quiz 863.967 s; arg. 7 «Il «Comunismo di guerra»»: inizio 868.567 s, quiz 1025.167 s; arg. 8 «La Nuova Politica Economica (NEP)»: inizio 1029.767 s, quiz 1375.133 s; arg. 9 «La nascita dell'URSS e la successione»: inizio 1379.733 s, quiz 1695.3 s

La durata è cambiata rispetto alla consegna precedente (che aveva 53+51 minuti): i secondi vecchi non valgono più, la scheda di pubblicazione ha quelli nuovi.
