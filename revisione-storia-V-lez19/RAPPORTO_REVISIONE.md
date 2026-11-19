# RAPPORTO · Storia V · Lezione 19 · L'Italia dal '68 alla crisi della Prima Repubblica

**Stato: rifatta da zero in 2 Parti** sul video originale del prof. Giorgio Mazzotti (4795,9 s). Della consegna precedente ho riusato le voci Kore già fatte (benvenuto, ripasso Parte 2, glossari, riepiloghi, saluti) e i quiz (8×5) del ramo `voci-storia-V-lez19`; le voci nuove (3 mappe del prof, 8 pillole, 31 righe di schema) le ha fatte la master: 43/43 con esito OK. Ogni affermazione è marcata [misurato], [per costruzione], [stima] o [non verificato].

## 1 · Misure sul video

| | Parte 1 (argomenti 1–4) | Parte 2 (argomenti 5–8) |
|---|---|---|
| Durata | 46:45.6 (2805.6 s) [misurato] | 44:41.3 (2681.3 s) [misurato] |
| Fotogrammi / 30 fps | 84167 = durata×30 [misurato] | 80440 = durata×30 [misurato] |
| Formato | 1920×1080, x264, AAC 192k 48 kHz stereo [misurato] | idem |
| Peso | 380,3 MB (362,7 MiB) [misurato] | 386,3 MB (368,4 MiB) [misurato] |
| Loudness integrata (file finale, ebur128) | −16,5 LUFS [misurato] | −16,6 LUFS [misurato] |
| Picco (true peak, file finale) | −4,1 dBFS [misurato] | −2,9 dBFS [misurato] (limite −1) |
| Parlato del prof (mediana dei pezzi) | −16,4 LUFS [misurato] | −16,1 LUFS [misurato] |
| Scatto `quiz.wav` | 4 quiz a +0,005 s dall'atteso [misurato, controllo_jingle.py] | 4 quiz a +0,005 s [misurato] |
| Fermi immagine del prof ≥ 1 s | nessuno [misurato] | nessuno [misurato] |
| Sfasamento audio/labbra | **non misurato in modo affidabile**: la correlazione tra movimento del viso e inviluppo audio è troppo debole (0,03–0,10; il prof gesticola molto). Audio e video del prof escono dallo stesso istante dell'originale [per costruzione] | idem |
| sha256 | vedi `.sha256`; ricomponendo i `.parte_NN` coincide [misurato] | idem |

Uscita integrale di `controllo_finale.py`:

```
Parte 1
durata 46:45.6 (2805.6 s) | fotogrammi 84167 (attesi 84167) OK | peso 380.3 MB (362.7 MiB) OK | 1920x1080 OK
quiz 4 scatto 0,0 s: OK
fermi immagine nei pezzi del docente: nessuno OK
volume del parlato (mediana dei pezzi del docente): -16.4 LUFS OK
sottotitoli: 656 blocchi, sovrapposti 0, oltre la fine 0, attacco sulla voce entro 0,3 s: 88% di 17 verificabili OK
foglio di miniature: out/Storia_Lez19_Parte1_1080p.mp4.miniature.jpg
ESITO: TUTTO OK

Parte 2
durata 44:41.3 (2681.3 s) | fotogrammi 80440 (attesi 80440) OK | peso 386.3 MB (368.4 MiB) OK | 1920x1080 OK
quiz 4 scatto 0,0 s: OK
fermi immagine nei pezzi del docente: nessuno OK
volume del parlato (mediana dei pezzi del docente): -16.1 LUFS OK
sottotitoli: 632 blocchi, sovrapposti 0, oltre la fine 0, attacco sulla voce entro 0,3 s: 79% di 14 verificabili DA GUARDARE
foglio di miniature: out/Storia_Lez19_Parte2_1080p.mp4.miniature.jpg
ESITO: DA SISTEMARE: sottotitoli
```

**Sottotitoli, attacco sulla voce (soglia 80%)**: Parte 1 **88%** di 17 blocchi verificabili (OK); Parte 2 **79%** di 14 (lo strumento dice DA SISTEMARE) [misurato]. Come ci sono arrivato: prime misure 76% e 81%; ho migliorato l'allineamento (inizio dei blocchi portato all'attacco di energia misurato, cercando fino a 2 s in avanti). I 3 blocchi che restano fuori nella Parte 2 (2:32, 3:19, 10:19 circa) li ho guardati uno per uno: l'energia del parlato parte entro 0,05 s dall'inizio del blocco, ma lo strumento trova un breve rumore (respiro/coda della parola precedente) 0,8 s prima e lo scambia per attacco. Quindi per me sono artefatti della misura, **non** errori reali [stima dopo controllo a mano, non riascoltati]; lo dichiaro comunque perché il verdetto automatico resta DA SISTEMARE.

## 2 · Tabella dei pezzi (sezione C della scheda tecnica)

| Pezzo | Presente | Minuto (Parte) | Durata misurata |
|---|---|---|---|
| 1 · Sigla (P1) | sì | P1 0:00.0 | 15.0 s |
| 3 · Copertina + voce di benvenuto | sì | P1 0:13.6 | 21.6 s |
| 3 · Introduzione del prof sulla copertina | sì | P1 0:34.8 | 288.3 s |
| 4a · Titolo argomento 1 | sì | P1 5:22.6 | 4.0 s |
| 4b · Prof + slide argomento 1 | sì | P1 5:26.2 | 718.9 s |
| 4c · Approfondimenti animati argomento 1 | no (non necessari: il prof copre già tutto) | – | – |
| 4d · Mappa del prof argomento 1 | no (il prof non ha mappa per questo argomento: non inventata) | – | – |
| 4e · Pillola di ripasso argomento 1 | sì | P1 17:24.7 | 10.3 s |
| 4f · Schema guidato argomento 1 | sì | P1 17:34.6 | 30.1 s |
| 4g · Scheda Quiz 1 | sì | P1 18:04.3 | 5.0 s |
| 4a · Titolo argomento 2 | sì | P1 18:08.9 | 4.0 s |
| 4b · Prof + slide argomento 2 | sì | P1 18:12.5 | 325.3 s |
| 4c · Approfondimenti animati argomento 2 | no (non necessari: il prof copre già tutto) | – | – |
| 4d · Mappa del prof argomento 2 | no (il prof non ha mappa per questo argomento: non inventata) | – | – |
| 4e · Pillola di ripasso argomento 2 | sì | P1 23:37.4 | 9.1 s |
| 4f · Schema guidato argomento 2 | sì | P1 23:46.1 | 23.1 s |
| 4g · Scheda Quiz 2 | sì | P1 24:08.7 | 5.0 s |
| 4a · Titolo argomento 3 | sì | P1 24:13.3 | 4.0 s |
| 4b · Prof + slide argomento 3 | sì | P1 24:16.9 | 694.8 s |
| 4c · Approfondimenti animati argomento 3 | no (non necessari: il prof copre già tutto) | – | – |
| 4d · Mappa del prof argomento 3 | sì | P1 35:51.3 | 25.1 s |
| 4e · Pillola di ripasso argomento 3 | sì | P1 36:16.0 | 9.3 s |
| 4f · Schema guidato argomento 3 | sì | P1 36:24.9 | 36.6 s |
| 4g · Scheda Quiz 3 | sì | P1 37:01.2 | 5.0 s |
| 4a · Titolo argomento 4 | sì | P1 37:05.8 | 4.0 s |
| 4b · Prof + slide argomento 4 | sì | P1 37:09.4 | 441.4 s |
| 4c · Approfondimenti animati argomento 4 | no (non necessari: il prof copre già tutto) | – | – |
| 4d · Mappa del prof argomento 4 | sì | P1 44:30.4 | 22.1 s |
| 4e · Pillola di ripasso argomento 4 | sì | P1 44:52.1 | 10.1 s |
| 4f · Schema guidato argomento 4 | sì | P1 45:01.8 | 34.0 s |
| 4g · Scheda Quiz 4 | sì | P1 45:35.5 | 5.0 s |
| 5 · Glossario (P1) | sì | P1 45:40.1 | 33.5 s |
| 6 · Riepilogo finale (P1) + saluto | sì | P1 46:13.2 | 27.8 s |
| 7 · Finale 5 s (P1) | sì | P1 46:40.6 | 5.0 s |
| 1 · Sigla (P2) | sì | P2 0:00.0 | 15.0 s |
| 3 · Copertina + voce di benvenuto (ripasso della Parte 1) | sì | P2 0:13.6 | 20.6 s |
| 4a · Titolo argomento 5 | sì | P2 0:33.8 | 4.0 s |
| 4b · Prof + slide argomento 5 | sì | P2 0:37.4 | 442.9 s |
| 4c · Approfondimenti animati argomento 5 | no (non necessari: il prof copre già tutto) | – | – |
| 4d · Mappa del prof argomento 5 | no (il prof non ha mappa per questo argomento: non inventata) | – | – |
| 4e · Pillola di ripasso argomento 5 | sì | P2 7:60.0 | 9.6 s |
| 4f · Schema guidato argomento 5 | sì | P2 8:09.2 | 44.2 s |
| 4g · Scheda Quiz 5 | sì | P2 8:53.0 | 5.0 s |
| 4a · Titolo argomento 6 | sì | P2 8:57.6 | 4.0 s |
| 4b · Prof + slide argomento 6 | sì | P2 9:01.2 | 980.2 s |
| 4c · Approfondimenti animati argomento 6 | no (non necessari: il prof copre già tutto) | – | – |
| 4d · Mappa del prof argomento 6 | no (il prof non ha mappa per questo argomento: non inventata) | – | – |
| 4e · Pillola di ripasso argomento 6 | sì | P2 25:21.0 | 10.3 s |
| 4f · Schema guidato argomento 6 | sì | P2 25:30.9 | 42.4 s |
| 4g · Scheda Quiz 6 | sì | P2 26:12.9 | 5.0 s |
| 4a · Titolo argomento 7 | sì | P2 26:17.5 | 4.0 s |
| 4b · Prof + slide argomento 7 | sì | P2 26:21.1 | 683.2 s |
| 4c · Approfondimenti animati argomento 7 | no (non necessari: il prof copre già tutto) | – | – |
| 4d · Mappa del prof argomento 7 | sì | P2 37:43.9 | 25.5 s |
| 4e · Pillola di ripasso argomento 7 | sì | P2 38:09.0 | 9.3 s |
| 4f · Schema guidato argomento 7 | sì | P2 38:18.0 | 34.6 s |
| 4g · Scheda Quiz 7 | sì | P2 38:52.2 | 5.0 s |
| 4a · Titolo argomento 8 | sì | P2 38:56.8 | 4.0 s |
| 4b · Prof + slide argomento 8 | sì | P2 39:00.4 | 227.0 s |
| 4c · Approfondimenti animati argomento 8 | no (non necessari: il prof copre già tutto) | – | – |
| 4d · Mappa del prof argomento 8 | no (il prof non ha mappa per questo argomento: non inventata) | – | – |
| 4e · Pillola di ripasso argomento 8 | sì | P2 42:47.0 | 9.2 s |
| 4f · Schema guidato argomento 8 | sì | P2 42:55.8 | 34.6 s |
| 4g · Scheda Quiz 8 | sì | P2 43:30.0 | 5.0 s |
| 5 · Glossario (P2) | sì | P2 43:34.6 | 33.5 s |
| 6 · Riepilogo finale (P2) + saluto | sì | P2 44:07.7 | 29.0 s |
| 7 · Finale 5 s (P2) | sì | P2 44:36.3 | 5.0 s |

`trans.wav` + dissolvenza (0,4 s; 1,4 s dopo la sigla) a ogni cambio di pezzo [per costruzione]; `titolo.wav`, `repaso.wav`, `quiz.wav` (+0,5 s), `finale.wav` [per costruzione; il solo scatto del quiz è misurato].

## 3 · Confronto con Spagnolo Lez. 1

Immagine: `confronto_Spagnolo.jpg` (sopra il modello, sotto i nostri fotogrammi); foglio di tutti i pezzi: `foglio.png`; un fotogramma ogni 30 s: `controllo_minuti_Parte1/2.jpg`. Schede blu fatte SOLO con `schede_spagnolo.py` a scala 1.0 [misurato]. Differenze dichiarate: pillola blu di 9,1–10,3 s invece di 14 s (frasi brevi); la didascalia è il testo della voce Kore parola per parola [per costruzione]; schermata slide a pagina intera con riquadro del prof; le tre mappe del prof compaiono a livelli, sincronizzate alle frasi della voce.

## 4 · Controlli obbligatori del prompt v3

- **Chip** sotto il titolo blu (2–3 parole chiave vere): 1: «Sessantotto · Vietnam · Studenti»; 2: «Statuto dei lavoratori · Regioni · 1970»; 3: «Piazza Fontana · Brigate Rosse · Bologna 1980»; 4: «Aldo Moro · Via Fani · Berlinguer»; 5: «Divorzio · Aborto · Crisi del petrolio»; 6: «Riflusso · Craxi · Loggia P2»; 7: «Mani pulite · Di Pietro · Capaci»; 8: «Referendum 1993 · Mattarella · Ciampi».
- Nomi coerenti in tutto il video (titolo, pillola, schema, quiz, riepilogo) [misurato sul foglio].
- Titoli lunghi: corpo ridotto (`tfs`) per non toccare il tasto play [misurato sul foglio].
- Riepilogo finale con tutti gli argomenti della Parte (4 + 4) [misurato sul foglio]. `foglio.png` fatto.
- Quiz: scatto del jingle +0,005 s su tutti e 8 [misurato].
- Mappe del prof: riquadro sotto il titolo, nessuna parte nascosta a fine animazione [misurato sui fotogrammi]; il titolo della mappa 7 («Cosa accade negli anni Novanta?») l'ho scritto io perché nel PDF delle mappe non c'è una domanda; le mappe 3 e 4 hanno la domanda originale del prof.

## 5 · Problemi trovati e correzioni

| Minuto | Tipo | Com'era | Correzione |
|---|---|---|---|
| Tutto | testo | Trascrizione automatica (715 segmenti) con errori su nomi/date e molti riempitivi («Um», «Mm», «Republika»…) | 281 segmenti corretti a mano, 35 frammenti/riempitivi tolti, correzioni globali dei nomi (Craxi, D'Amelio, URSS…) |
| Tutto | testo | Sottotitoli che attaccavano in anticipo sulla voce dopo le pause (76% / 81% sul controllo) | Inizio dei blocchi allineato all'attacco misurato: 79% / 88% (vedi sezione 1) |
| Slide 3,5,7,11,13,15,16 | visivo | Pagine-immagine del prof senza card | Pagine immagine dedicate nell'argomento giusto, accese quando il prof ne parla; la pagina 5 (Piazza Fontana + Berlinguer/Moro) compare due volte, nell'arg. 3 e nell'arg. 4 |
| Slide 2 | visivo | Una sola pagina con 4 card che copre due argomenti (Sessantotto e Autunno caldo) | Divisa in due pagine: card 1–2 nell'arg. 1, card 3–4 nell'arg. 2 |
| Mappa 3 (PDF) | visivo | Ritaglio troncato dell'albero «Negli anni Novanta» | Ricavato di nuovo dal render a 110 dpi: albero intero |
| Parte 2 inizio | audio | Il prof entra a metà di un discorso (argomento 5) | Taglio alla pausa più lunga entro 2,5 s dal punto scelto; nessuna parola tagliata [stima, non riascoltato] |
| Tutto | altro | Le voci nuove servono prima di poter montare pillole, schemi e mappe | Richieste alla master subito dopo la prenotazione; nel frattempo preparate slide, schede titolo/quiz e pezzi del prof |

## 6 · DA CONFERMARE COL PROF

1. **Corpo ritrovato di Moro**: il prof dice «Fiat rossa» (al minuto 35:46 dell'originale); storicamente è una Renault 4 rossa. Sottotitolo lasciato come detto.
2. **Treno Italicus**: il prof dice che l'attentato portò alla morte di «tutti i passeggeri» (27:17 dell'originale); storicamente furono 12 morti. Sottotitolo lasciato come detto.
3. **Legge Mattarella**: nel parlato il prof parla di «premio di maggioranza … 25% o 65%» (77:34 dell'originale), mentre la sua slide (e il nostro schema e quiz) dicono sistema misto 75% maggioritario / 25% proporzionale. Nel video il parlato e la slide non coincidono.
4. **Governo Craxi**: nel parlato «dal 1983 al 1986» (55:09 dell'originale); nella slide «dal 1983 al 1987». Nelle schede abbiamo usato la slide (1983-1987).
5. **Verifica finale, domanda 1** («Quale ateneo fu occupato per primo alla fine del 1967?» → Università Cattolica di Milano): nel parlato il prof cita le «Tesi della Sapienza» del '67 come inizio del movimento universitario e la Cattolica per la protesta sulle tasse; chiedere se la risposta giusta è davvero la Cattolica.
6. **Quiz 4, domanda 2** («Che ruolo ha Aldo Moro quando viene rapito?» → Presidente della Democrazia Cristiana): vale per la slide; il prof nel parlato dice solo «più volte presidente del Consiglio, all'epoca senza cariche di governo».
7. **Nomi nei sottotitoli scritti da me, da confermare**: «Donat-Cattin» (ministro del lavoro), «Edilnord», «Standa», «Černobyl», «Icmesa», «Mara Cagol».

## 7 · Cosa NON ho verificato

- I sottotitoli sono corretti sul **testo** della trascrizione, **non** riascoltati uno per uno; i 42 segmenti dubbi (indici trascrizione: 0, 13, 81, 84, 110, 113, 132, 139, 141, 142, 189, 195, 242, 246, 258, 266, 272, 286, 341, 343, 346, 362, 369, 377, 440, 456, 466, 485, 508, 519, 545, 549, 576, 606, 626, 628, 639, 648, 652, 666, 689, 693) sono lasciati con la mia migliore lettura [non verificato].
- Sfasamento audio/labbra non misurato in modo affidabile (sezione 1) [non verificato].
- Voci Kore nuove: l'ASR della master segnala 1–2 «parole diverse vere» su MD1, MD3, P1, P4, P5, SC1_2, SC5_5, SC6_5, SC7_3; **non le ho riascoltate** [non verificato].
- Webcam del prof: 184×138 px ingrandita a 410×308: **morbida** (limite dell'originale) [misurato sul fotogramma].
- Non ho verificato la correttezza storica di quanto dice il prof oltre ai punti della sezione 6.

## 8 · Come ho verificato

Trascrizione con `trascrivi.py` (715 segmenti); allineamento delle card al parlato leggendo la trascrizione e scegliendo a mano i punti di cambio; audio del prof dall'originale con la catena del kit (denoise rnnn, loudnorm, aresample 48k, limiter); misure con `controllo_finale.py`, `controllo_jingle.py`, `ebur128` (loudness, true peak) sul file finale; foglio di tutti i pezzi, un fotogramma ogni 30 s e le tre mappe viste a occhio; correlazione audio/video per lo sfasamento (inconcludente).

## 9 · Tempi nel video nuovo (per la pagina)

**Parte 1** (durata 2805.567 s): arg. 1 «Il Sessantotto e la protesta studentesca»: inizio 322.633 s, quiz 1084.333 s; arg. 2 «L'Autunno caldo e le riforme»: inizio 1088.933 s, quiz 1448.733 s; arg. 3 «Gli anni di piombo e lo stragismo»: inizio 1453.333 s, quiz 2221.167 s; arg. 4 «Il caso Moro e la solidarietà nazionale»: inizio 2225.767 s, quiz 2735.467 s

**Parte 2** (durata 2681.333 s): arg. 5 «Conquiste sociali e crisi energetica»: inizio 33.833 s, quiz 532.967 s; arg. 6 «Gli anni Ottanta: riflusso e Pentapartito»: inizio 537.567 s, quiz 1572.867 s; arg. 7 «Tangentopoli e il crollo dei partiti»: inizio 1577.467 s, quiz 2332.2 s; arg. 8 «La transizione e i governi tecnici»: inizio 2336.8 s, quiz 2610.033 s

La scheda di pubblicazione ha i secondi nuovi; quelli della consegna precedente non valgono più.
