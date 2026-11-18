# RAPPORTO · Storia V · Lezione 12 · L'Europa e il mondo negli anni Trenta

**Stato: montaggio completo in 2 Parti, fatto da zero** (per la lezione 12 non esisteva nessuna consegna precedente: c'erano solo 52 voci Kore e i quiz nel ramo `voci-storia-V-lez12`, riusati). Ogni affermazione è etichettata **[misurato]**, **[stima]** o **[non verificato]**.

## 1 · Misure sul video

| | Parte 1 (argomenti 1–5) | Parte 2 (argomenti 6–9) |
|---|---|---|
| Durata | 28:58.9 (1738.9 s) [misurato] | 38:38.4 (2318.4 s) [misurato] |
| Fotogrammi / 30 fps | 52166 = durata×30 [misurato] | 69551 = durata×30 [misurato] |
| Formato | 1920×1080, x264 veryfast CRF 19, keyint 60, AAC 192k 48 kHz [misurato] | idem |
| Peso | 225,1 MB [misurato] | 298,2 MB [misurato] |
| Parlato, loudness integrata | −16,7 LUFS [misurato] | −16,8 LUFS [misurato] |
| Picco (true peak, file finale) | −4,1 dBFS [misurato] | −2,2 dBFS [misurato] (limite −1) |
| Scatto `quiz.wav` | 5 quiz a +0,005 s dall'atteso [misurato con controllo_jingle.py] | 4 quiz a +0,005 s [misurato] |
| Fermi immagine del prof ≥ 1 s | nessuno [misurato, freezedetect sul riquadro e controllo_finale.py] | nessuno [misurato] |
| Sfasamento audio/labbra | −15 ms (correlazione dell'inviluppo, 3 punti: min 5, 25, 47) [misurato, limite 40 ms] | idem |
| sha256 | vedi `.sha256` (ricomponendo i `.parte_NN` il sha256 coincide, controllato) [misurato] | idem |

Uscita di `controllo_finale.py` (testo integrale):

```
Parte 1
durata 28:58.9 (1738.9 s) | fotogrammi 52166 (attesi 52166) OK | peso 225.1 MB (214.7 MiB) OK | 1920x1080 OK
quiz 5 scatto 0,0 s: OK
fermi immagine nei pezzi del docente: nessuno OK
volume del parlato (mediana dei pezzi del docente): -16.4 LUFS OK
sottotitoli: 391 blocchi, sovrapposti 0, oltre la fine 0, attacco sulla voce entro 0,3 s: 86% di 21 verificabili OK
foglio di miniature: out/Storia_Lez12_Parte1_1080p.mp4.miniature.jpg
ESITO: TUTTO OK

Parte 2
durata 38:38.4 (2318.4 s) | fotogrammi 69551 (attesi 69551) OK | peso 298.2 MB (284.4 MiB) OK | 1920x1080 OK
quiz 4 scatto 0,0 s: OK
fermi immagine nei pezzi del docente: nessuno OK
volume del parlato (mediana dei pezzi del docente): -16.9 LUFS OK
sottotitoli: 542 blocchi, sovrapposti 0, oltre la fine 0, attacco sulla voce entro 0,3 s: 83% di 18 verificabili OK
foglio di miniature: out/Storia_Lez12_Parte2_1080p.mp4.miniature.jpg
ESITO: TUTTO OK
```

Attacco dei sottotitoli sulla voce (strumento ufficiale, soglia 80%): Parte 1 **86%** di 21 blocchi verificabili, Parte 2 **83%** di 18 [misurato]. Ho dovuto correggere due volte l'allineamento (prima 64–78%): ora i blocchi del prof partono dalla prima parola della trascrizione e le frasi lunghe sono spezzate allineando testo corretto e testo automatico [misurato]. Restano pochi blocchi fuori da ±0,3 s (voci con attacco morbido): vedi controllo.

## 2 · Tabella dei pezzi (sezione C della scheda tecnica)

| Pezzo | Presente | Minuto (Parte) | Durata misurata |
|---|---|---|---|
| 1 · Sigla (P1) | sì | P1 0:00.0 | 15.0 s |
| 3 · Copertina + voce di benvenuto | sì | P1 0:13.6 | 11.8 s |
| 3 · Introduzione del prof sulla copertina (riquadro del prof) | sì | P1 0:25.0 | 195.8 s |
| 4a · Titolo argomento 1 | sì | P1 3:40.4 | 4.0 s |
| 4b · Prof + slide argomento 1 | sì | P1 3:44.0 | 340.7 s |
| 4c · Approfondimenti animati argomento 1 | no (non necessari: il prof copre già tutto; vedi deviazioni) | – | – |
| 4d · Mappa del prof argomento 1 | no (il prof non ha mappa per questo argomento: non inventata) | – | – |
| 4e · Pillola di ripasso (scheda blu) argomento 1 | sì | P1 9:24.3 | 8.2 s |
| 4f · Schema guidato bianco argomento 1 | sì | P1 9:32.1 | 38.2 s |
| 4g · Scheda Quiz 1 | sì | P1 10:09.9 | 5.0 s |
| 4a · Titolo argomento 2 | sì | P1 10:14.5 | 4.0 s |
| 4b · Prof + slide argomento 2 | sì | P1 10:18.1 | 189.6 s |
| 4c · Approfondimenti animati argomento 2 | no (non necessari: il prof copre già tutto; vedi deviazioni) | – | – |
| 4d · Mappa del prof argomento 2 | no (il prof non ha mappa per questo argomento: non inventata) | – | – |
| 4e · Pillola di ripasso (scheda blu) argomento 2 | sì | P1 13:27.3 | 8.3 s |
| 4f · Schema guidato bianco argomento 2 | sì | P1 13:35.3 | 32.6 s |
| 4g · Scheda Quiz 2 | sì | P1 14:07.4 | 5.0 s |
| 4a · Titolo argomento 3 | sì | P1 14:12.0 | 4.0 s |
| 4b · Prof + slide argomento 3 | sì | P1 14:15.6 | 182.4 s |
| 4c · Approfondimenti animati argomento 3 | no (non necessari: il prof copre già tutto; vedi deviazioni) | – | – |
| 4d · Mappa del prof argomento 3 | no (il prof non ha mappa per questo argomento: non inventata) | – | – |
| 4e · Pillola di ripasso (scheda blu) argomento 3 | sì | P1 17:17.6 | 8.3 s |
| 4f · Schema guidato bianco argomento 3 | sì | P1 17:25.6 | 34.7 s |
| 4g · Scheda Quiz 3 | sì | P1 17:59.9 | 5.0 s |
| 4a · Titolo argomento 4 | sì | P1 18:04.5 | 4.0 s |
| 4b · Prof + slide argomento 4 | sì | P1 18:08.1 | 200.5 s |
| 4c · Approfondimenti animati argomento 4 | no (non necessari: il prof copre già tutto; vedi deviazioni) | – | – |
| 4d · Mappa del prof argomento 4 | no (il prof non ha mappa per questo argomento: non inventata) | – | – |
| 4e · Pillola di ripasso (scheda blu) argomento 4 | sì | P1 21:28.2 | 9.0 s |
| 4f · Schema guidato bianco argomento 4 | sì | P1 21:36.8 | 31.9 s |
| 4g · Scheda Quiz 4 | sì | P1 22:08.3 | 5.0 s |
| 4a · Titolo argomento 5 | sì | P1 22:12.9 | 4.0 s |
| 4b · Prof + slide argomento 5 | sì | P1 22:16.5 | 224.1 s |
| 4c · Approfondimenti animati argomento 5 | no (non necessari: il prof copre già tutto; vedi deviazioni) | – | – |
| 4d · Mappa del prof argomento 5 | sì | P1 26:00.2 | 19.9 s |
| 4e · Pillola di ripasso (scheda blu) argomento 5 | sì | P1 26:19.7 | 9.5 s |
| 4f · Schema guidato bianco argomento 5 | sì | P1 26:28.8 | 34.2 s |
| 4g · Scheda Quiz 5 | sì | P1 27:02.6 | 5.0 s |
| 5 · Glossario (P1) | sì | P1 27:07.2 | 54.1 s |
| 6 · Riepilogo finale (P1) + saluto | sì | P1 28:00.9 | 53.4 s |
| 7 · Finale 5 s (P1) | sì | P1 28:53.9 | 5.0 s |
| 1 · Sigla (P2) | sì | P2 0:00.0 | 15.0 s |
| 3 · Copertina + voce di benvenuto + ripasso della Parte 1 | sì | P2 0:13.6 | 48.5 s |
| 4a · Titolo argomento 6 | sì | P2 1:01.7 | 4.0 s |
| 4b · Prof + slide argomento 6 | sì | P2 1:05.3 | 652.1 s |
| 4c · Approfondimenti animati argomento 6 | no (non necessari: il prof copre già tutto; vedi deviazioni) | – | – |
| 4d · Mappa del prof argomento 6 | sì | P2 11:57.0 | 17.5 s |
| 4e · Pillola di ripasso (scheda blu) argomento 6 | sì | P2 12:14.1 | 8.2 s |
| 4f · Schema guidato bianco argomento 6 | sì | P2 12:21.9 | 44.7 s |
| 4g · Scheda Quiz 6 | sì | P2 13:06.1 | 5.0 s |
| 4a · Titolo argomento 7 | sì | P2 13:10.7 | 4.0 s |
| 4b · Prof + slide argomento 7 | sì | P2 13:14.3 | 327.8 s |
| 4c · Approfondimenti animati argomento 7 | no (non necessari: il prof copre già tutto; vedi deviazioni) | – | – |
| 4d · Mappa del prof argomento 7 | no (il prof non ha mappa per questo argomento: non inventata) | – | – |
| 4e · Pillola di ripasso (scheda blu) argomento 7 | sì | P2 18:41.7 | 9.5 s |
| 4f · Schema guidato bianco argomento 7 | sì | P2 18:50.8 | 37.5 s |
| 4g · Scheda Quiz 7 | sì | P2 19:27.9 | 5.0 s |
| 4a · Titolo argomento 8 | sì | P2 19:32.5 | 4.0 s |
| 4b · Prof + slide argomento 8 | sì | P2 19:36.1 | 419.9 s |
| 4c · Approfondimenti animati argomento 8 | no (non necessari: il prof copre già tutto; vedi deviazioni) | – | – |
| 4d · Mappa del prof argomento 8 | sì | P2 26:35.6 | 19.1 s |
| 4e · Pillola di ripasso (scheda blu) argomento 8 | sì | P2 26:54.4 | 10.7 s |
| 4f · Schema guidato bianco argomento 8 | sì | P2 27:04.6 | 39.2 s |
| 4g · Scheda Quiz 8 | sì | P2 27:43.5 | 5.0 s |
| 4a · Titolo argomento 9 | sì | P2 27:48.1 | 4.0 s |
| 4b · Prof + slide argomento 9 | sì | P2 27:51.7 | 500.3 s |
| 4c · Approfondimenti animati argomento 9 | no (non necessari: il prof copre già tutto; vedi deviazioni) | – | – |
| 4d · Mappa del prof argomento 9 | no (il prof non ha mappa per questo argomento: non inventata) | – | – |
| 4e · Pillola di ripasso (scheda blu) argomento 9 | sì | P2 36:11.6 | 11.2 s |
| 4f · Schema guidato bianco argomento 9 | sì | P2 36:22.4 | 38.4 s |
| 4g · Scheda Quiz 9 | sì | P2 37:00.3 | 5.0 s |
| 5 · Glossario (P2) | sì | P2 37:04.9 | 46.3 s |
| 6 · Riepilogo finale (P2) + saluto | sì | P2 37:50.8 | 42.9 s |
| 7 · Finale 5 s (P2) | sì | P2 38:33.4 | 5.0 s |

`trans.wav` + dissolvenza (0,4 s; 1,4 s dopo la sigla) a ogni cambio di pezzo [misurato: la catena xfade ha un confine per pezzo]; `titolo.wav` su ogni titolo, `repaso.wav` su ogni pillola, `quiz.wav` a +0,5 s su ogni quiz, `finale.wav` sul finale [per costruzione; il solo scatto del quiz è stato misurato sul video].

## 3 · Confronto con Spagnolo Lez. 1

Immagine: `confronto_Spagnolo.jpg` (sopra il modello, sotto i nostri fotogrammi). Schede blu fatte SOLO con `schede_spagnolo.py` a scala 1.0 [misurato]. Differenze **dichiarate**:

- Pillola blu: 8–11 s invece di 14 s (le frasi della voce sono brevi); il testo mostrato è la frase della voce, parola per parola.
- Schema guidato: 32–45 s (4–5 righe, 2,5–3 s di pausa dopo ogni riga) invece di ≈46 s.
- Riepilogo finale + saluto: 43–53 s invece di 12–35 s (ho tenuto sulla stessa scheda anche la voce di chiusura, già pronta).
- Pannello «PAROLE CHIAVE» sotto il prof: aggiunta approvata, tenuta.
- Approfondimenti 4c: non fatti.

## 4 · Controlli obbligatori del prompt v3

- **Chip** sotto il titolo: parole chiave vere (persone, luoghi, date, opere), mai il titolo ripetuto: es. «Wall Street · MacDonald · Commonwealth», «Croix de Feu · Léon Blum · 1936», «Horthy · Piłsudski · Metaxas», «Salazar · Estado Novo · Seconda Repubblica», «Vargas · Manciukuò · Lunga marcia», «Franco · Guernica · Brigate internazionali», «Versailles · Renania · Asse Roma-Berlino», «Austria · Sudeti · Cecoslovacchia», «Albania · Patto d'acciaio · Molotov-Ribbentrop» [misurato a vista nel `foglio.png`].
- **Didascalia pillola** = testo della voce Kore parola per parola (preso dal `testi_voci.json`, non dall'OCR) [misurato: vedi `foglio.png`, 2 didascalie per pillola].
- **Argomento lungo** nel quiz: ho corretto i quiz 5, 7, 8, 9 (testo che toccava il pulsante play) con `tfs` più piccolo e verificato a vista il fotogramma finale [misurato]. Il quiz 3 non tocca il pulsante (verificato a vista).
- **Riepilogo finale**: ultimo fotogramma con TUTTE le card (5 in Parte 1, 4 in Parte 2) [misurato a vista].
- **Nomi e titoli** uguali in schede, quiz, compiti e verifica: titoli degli argomenti allineati nei titoli blu, nelle pillole, nei quiz (`quiz_argomenti.json` aggiornato), nella copertina e nelle slide [misurato a vista]. L'argomento 4 si chiama «La penisola iberica» ovunque (titolo blu rifatto).
- **Foglio di controllo**: `foglio.png` (38 fotogrammi: titoli, pillole con 2 didascalie, quiz, riepiloghi).
- **Tempi**: i fotogrammi Quiz cadono ai `quiz_s` della scheda di pubblicazione (+0,005 s, misurato); durata video = durata audio [misurato].

## 5 · Problemi trovati e correzioni

| Minuto | Tipo | Com'era | Correzione |
|---|---|---|---|
| P1 27:02; P2 19:28, 27:43, 37:00 | visivo | Nei quiz 5, 7, 8, 9 il titolo dell'argomento toccava il pulsante play | Rifatti con `tfs` più piccolo (66/56/56/62) |
| P1/P2 mappe del prof | visivo | La scoperta a tempo tagliava a metà i riquadri della mappa | Livelli di scoperta ricalcolati sulle righe vuote tra un livello e l'altro dell'immagine |
| P1 27:07 e P2 37:05 | visivo | Glossario con minuscole sbagliate («franco», «hitler», «italia») e date in lettere | Solo la prima lettera maiuscola, date in cifre («1931», «1936»…) |
| P1 18:04 | visivo | Titolo dell'argomento 4 diverso dal nome nei quiz | Titolo blu rifatto («La penisola / iberica») |
| Tutto | visivo | Titolo lungo della slide del prof («Dittature e autoritarismi in Europa ed extra-Europa») nascosto dal riquadro | Dimensione del titolo adattata alla larghezza |
| Tutto | audio | Mix con voci e jingle: picco +0,5 dBFS | Limiter; picco finale −4,1 / −2,2 dBFS; loudness −16,7 / −16,8 LUFS |
| Tutto il prof | testo | Trascrizione automatica con ~200 segmenti da correggere (nomi: «Piłsudski», «Horthy», «Guernica», «appeasement»…), disturbi («Um», «Mm»), date in lettere | 204 correzioni e 21 righe di disturbo tolte; testo dei sottotitoli corretto (vedi `subs_fix.py` nel ramo di lavoro) |
| Tutto | altro | Il primo montaggio si fermava per memoria sul filtro di sovrapposizione | Metodo rifatto con segmenti a frequenza costante |

## 6 · DA CONFERMARE COL PROF

1. **Sudeti: 1938 o 1939?** Nella mappa del prof il nodo dice «i Sudeti (1939)»; la slide e il parlato dicono settembre 1938 (conferenza di Monaco). Nel video resta ciò che dice la mappa (impaginata invariata) e la voce di lettura dice solo «Invade i Sudeti».
2. **Caduta di Barcellona e Madrid**: il prof dice «il 1 aprile 1936»; la slide dice 1939 (la guerra finisce il 1° aprile 1939). Nei sottotitoli ho lasciato quanto dice il prof [non corretto].
3. «**Croix de Feu, la croce di ferro**»: la Croix de Feu sono le «croci di fuoco»; il prof dice «croce di ferro». Lasciato com'è nei sottotitoli.

## 7 · Cosa NON ho verificato

- I sottotitoli del prof sono corretti sul **testo** della trascrizione automatica: **non** li ho riascoltati uno per uno. Restano 20 segmenti dubbi lasciati come li ha scritti la macchina (indici: 56, 58, 68, 84, 148, 160, 180, 261, 277, 292, 294, 295, 372, 384, 385, 389, 452, 480, 521, 522) [non verificato].
- Immagine del prof: la webcam originale è 184×138 px ingrandita 2,2× a 410×308: **morbida**; la testa è già tagliata in alto nell'originale (limite non risolvibile) [misurato a vista].
- PDF slide: stesse pagine del video senza riquadro e senza fascia col nome (il pannello «PAROLE CHIAVE» è rimasto), generati dallo stesso codice; **non** ho fatto il confronto pixel per pixel pagina per pagina [non verificato]. Pagine: 32 (slide), 3 (mappe) [misurato].
- Quiz e verifica finale: i quiz erano già nel ramo `voci-…` (45 domande, 9×5); li ho riletti contro la trascrizione del prof e li ho trovati coerenti; la verifica finale è l'Excel del prof (10 domande) copiata senza modifiche [misurato].
- Non ho verificato le 3 mappe del prof riga per riga contro la voce di lettura, solo a vista.
- Il suono `trans.wav` ai confini tra i pezzi: verificato per costruzione, non ascoltato [non verificato].

## 8 · Come ho verificato

Trascrizione con `trascrivi.py` (529 segmenti, 7755 parole); cambi slide del video originale con differenza tra fotogrammi; audio del prof rifatto dall'originale con la catena del kit (`aresample 48000, highpass 80, arnndn, loudnorm −16, alimiter`); misure con ffmpeg (`ebur128`, `freezedetect`), `controllo_finale.py` e `controllo_jingle.py` sul video finale; fotogrammi ogni 30 s (`controllo_minuti_Parte1.jpg`, `controllo_minuti_Parte2.jpg`) e fogli di controllo (`foglio.png`, `confronto_Spagnolo.jpg`).

## 9 · Tabella tempi → pagina (secondi nel video nuovo)

**Parte 1** (durata 1738.867 s): arg. 1 «Il Regno Unito negli anni Trenta»: inizio 220.4 s, quiz 609.933 s; arg. 2 «La Francia e il Fronte popolare»: inizio 614.533 s, quiz 847.433 s; arg. 3 «Le dittature dell'Europa orientale»: inizio 852.033 s, quiz 1079.9 s; arg. 4 «La penisola iberica»: inizio 1084.5 s, quiz 1328.333 s; arg. 5 «L'autoritarismo fuori dall'Europa»: inizio 1332.933 s, quiz 1622.6 s

**Parte 2** (durata 2318.367 s): arg. 6 «La guerra civile spagnola»: inizio 61.7 s, quiz 786.133 s; arg. 7 «L'aggressività nazista e l'appeasement»: inizio 790.733 s, quiz 1167.933 s; arg. 8 «L'Anschluss e la conferenza di Monaco»: inizio 1172.533 s, quiz 1663.467 s; arg. 9 «Verso la Seconda guerra mondiale»: inizio 1668.067 s, quiz 2220.333 s

Non esisteva un video precedente per questa lezione: non c'è una tabella «secondo vecchio → secondo nuovo».
