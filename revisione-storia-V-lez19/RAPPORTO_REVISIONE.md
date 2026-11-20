# RAPPORTO · Storia V · Lezione 19 · L'Italia dal '68 alla crisi della Prima Repubblica

**Stato: rifatta da zero in 2 Parti e poi corretta con gli 8 punti della master del 19/11 (03:40)** sul video originale del prof. Giorgio Mazzotti (4795,9 s). Della consegna precedente ho riusato le voci Kore già fatte (benvenuto, ripasso Parte 2, glossari, riepiloghi, saluti) e i quiz (8×5) del ramo `voci-storia-V-lez19`; le voci nuove (3 mappe del prof, 8 pillole, 31 righe di schema) le ha fatte la master: 43/43 con esito OK. Ogni affermazione è marcata [misurato], [per costruzione], [stima] o [non verificato].

## 1 · Misure sul video

| | Parte 1 (argomenti 1–4) | Parte 2 (argomenti 5–8) |
|---|---|---|
| Durata | 51:03.6 (3063.6 s) [misurato] | 48:30.7 (2910.7 s) [misurato] |
| Fotogrammi / 30 fps | 91908 = durata×30 [misurato] | 87320 = durata×30 [misurato] |
| Formato | 1920×1080, x264, AAC 192k 48 kHz stereo [misurato] | idem |
| Peso | 387.5 MB [misurato] | 359.5 MB [misurato] |
| Loudness integrata (file finale, ebur128) | -16,6 LUFS [misurato] | -16,7 LUFS [misurato] |
| Picco (true peak, file finale) | -4,0 dBFS [misurato] | -4,0 dBFS [misurato] (limite −1) |
| Parlato del prof (mediana dei pezzi) | -16,4 LUFS [misurato] | -16,5 LUFS [misurato] |
| Scatto `quiz.wav` | 4 quiz a +0,005 s dall'atteso [misurato, controllo_jingle.py] | 4 quiz a +0,005 s [misurato] |
| Fermi immagine del prof ≥ 1 s | nessuno [misurato] | nessuno [misurato] |
| Sfasamento audio/labbra | **non misurato in modo affidabile** (correlazione viso/audio 0,03–0,10: il prof gesticola molto). Audio e video del prof escono dallo stesso istante dell'originale [per costruzione] | idem |
| sha256 | vedi `.sha256`; ricomponendo i `.parte_NN` coincide [misurato] | idem |

Uscita integrale di `controllo_finale.py`:

```
Parte 1
durata 51:03.6 (3063.6 s) | fotogrammi 91908 (attesi 91908) OK | peso 387.5 MB (369.5 MiB) OK | 1920x1080 OK
quiz 4 scatto 0,0 s: OK
fermi immagine nei pezzi del docente: nessuno OK
volume del parlato (mediana dei pezzi del docente): -16.4 LUFS OK
sottotitoli: 700 blocchi, sovrapposti 0, oltre la fine 0, attacco sulla voce entro 0,3 s: 87% di 15 verificabili OK
foglio di miniature: out/Storia_Lez19_Parte1_1080p.mp4.miniature.jpg
ESITO: TUTTO OK

Parte 2
durata 48:30.7 (2910.7 s) | fotogrammi 87320 (attesi 87320) OK | peso 359.5 MB (342.9 MiB) OK | 1920x1080 OK
quiz 4 scatto 0,0 s: OK
fermi immagine nei pezzi del docente: nessuno OK
volume del parlato (mediana dei pezzi del docente): -16.5 LUFS OK
sottotitoli: 674 blocchi, sovrapposti 0, oltre la fine 0, attacco sulla voce entro 0,3 s: 88% di 17 verificabili OK
foglio di miniature: out/Storia_Lez19_Parte2_1080p.mp4.miniature.jpg
ESITO: TUTTO OK
```

**Sottotitoli, attacco sulla voce (soglia 80%)**: Parte 1 **87%** di 15 blocchi verificabili (OK); Parte 2 **88%** di 17 (OK) [misurato, controllo_finale.py]. L'allineamento l'ho migliorato rispetto alla prima versione (inizio dei blocchi portato all'attacco di energia misurato, cercando fino a 2 s in avanti). Dove lo strumento non dà OK, i blocchi fuori soglia li ho guardati uno per uno: l'energia del parlato parte quasi all'inizio del blocco, ma lo strumento trova prima un breve rumore (respiro/coda della parola precedente) e lo scambia per attacco: per me sono artefatti della misura, non errori reali [stima dopo controllo a mano, non riascoltati].

## 1b · Correzioni 19/11 (gli 8 punti della master)

| # | Punto | Cosa ho fatto | Misura |
|---|---|---|---|
| 1 | Max 3 card per slide, nessuna slide ferma oltre 3 minuti | Le 18 pagine di testo hanno 2 o 3 card (max 3); il prof è diviso in tratti (22 pezzi) con approfondimenti in mezzo; quando una card dura a lungo la stessa card passa a pagina intera in corpo grande (6 slide «in primo piano», solo il testo della card, niente di nuovo) | pagina ferma più lunga: **176 s** (argomento 1, minuto 13:51 dell'originale) [misurato sul piano dei cue]; limite 180 s |
| 2 | Sincronia bordo giallo ↔ prof | Cue presi dalla trascrizione parola per parola; controllo su 10 punti a caso | scarto (cue − inizio della frase del prof): 455 s −0,2; 1166 s −0,1; 1531 s −0,4; 2131 s −0,6; 2465 s −0,7; 2532 s −0,1; 2773 s −0,7; 2917 s −0,3; 4041 s −0,5; 4580 s −0,3 → tutti entro ±1 s, la card si accende fino a 0,7 s PRIMA della frase [misurato sulla trascrizione, non riascoltato] |
| 3 | Mappe | Le 3 mappe del PDF «MAPPE LEZIONE 19» ridisegnate con `kit/tools/mappa.py` (nostra grafica, testi del prof; nodi a tempo con la voce Kore, rami che compaiono quando la voce li nomina); niente più ritaglio dell'immagine | 3 mappe (arg. 3, 4, 7), un ramo alla volta [misurato sui fotogrammi]; le frasi lunghe del prof («il ruolo di garante della posizione internazionale del paese») eccedono il limite di 6 parole di `mappa.py` ma sono tenute intere per non cambiare il testo |
| 4 | Approfondimenti animati (4c) | Per ogni argomento 2 approfondimenti con le voci Kore già fatte dalla master (`AN*`), frasi della voce che compaiono a tempo, con la foto della slide del prof dove c'è: solo materiale della lezione | durata per argomento: arg. 1 62 s; arg. 2 56 s; arg. 3 68 s; arg. 4 52 s; arg. 5 58 s; arg. 6 68 s; arg. 7 48 s; arg. 8 54 s [misurato]; richiesto 40–60 s: **fuori intervallo** gli argomenti 3, 6 (tolleranza 65 s) |
| 5 | Schema di ripasso 4–6 righe | Aggiunta una riga agli argomenti 1 e 2 (voci nuove SC1_4, SC2_4) | righe per argomento: 1:4, 2:4, 3:4, 4:4, 5:5, 6:5, 7:4, 8:4 [misurato] |
| 6 | Transizioni | `trans.wav` + dissolvenza 0,4 s a ogni confine tra pezzi, anche prof → approfondimento → prof e prof → mappa → pillola | 82 confini, nessun taglio secco [per costruzione] |
| 7 | Copertina | Titolo esatto della slide del prof: «L'ITALIA DAL '68 ALLA CRISI DELLA PRIMA REPUBBLICA» su 2 righe; la card ARGOMENTI scende sotto il titolo senza sovrapporsi | verificato sul fotogramma [misurato] |
| 8 | Avviso diritti | Tolto dalla copertina (il riquadro scuro copriva il piè di pagina e il testo bianco su fondo bianco non si legge); resta nel **finale 5 s** in basso al centro, testo bianco 24 px, **senza riquadro** | verificato sul fotogramma del finale [misurato]; **da confermare con la master** se lo vuole anche sulla copertina |

## 2 · Tabella dei pezzi (sezione C della scheda tecnica)

| Pezzo | Presente | Minuto (Parte) | Durata misurata |
|---|---|---|---|
| 1 · Sigla | sì | P1 0:00.0 | 15.0 s |
| 3 · Copertina + voce di benvenuto | sì | P1 0:13.6 | 21.6 s |
| 3 · Introduzione del prof sulla copertina | sì | P1 0:34.8 | 288.3 s |
| 4a · Titolo argomento 1 | sì | P1 5:22.6 | 4.0 s |
| 4b · Prof + slide argomento 1 (tratto 1) | sì | P1 5:26.2 | 181.2 s |
| 4c · Approfondimento animato argomento 1 (1) · voce Kore | sì | P1 8:27.0 | 34.7 s |
| 4b · Prof + slide argomento 1 (tratto 2) | sì | P1 9:01.3 | 362.7 s |
| 4c · Approfondimento animato argomento 1 (2) · voce Kore | sì | P1 15:03.6 | 27.8 s |
| 4b · Prof + slide argomento 1 (tratto 3) | sì | P1 15:31.0 | 176.8 s |
| 4e · Pillola di ripasso argomento 1 | sì | P1 18:27.4 | 10.3 s |
| 4f · Schema guidato argomento 1 | sì | P1 18:37.2 | 39.3 s |
| 4g · Scheda Quiz 1 | sì | P1 19:16.1 | 5.0 s |
| 4a · Titolo argomento 2 | sì | P1 19:20.7 | 4.0 s |
| 4b · Prof + slide argomento 2 (tratto 1) | sì | P1 19:24.3 | 180.9 s |
| 4c · Approfondimento animato argomento 2 (1) · voce Kore | sì | P1 22:24.8 | 27.3 s |
| 4b · Prof + slide argomento 2 (tratto 2) | sì | P1 22:51.6 | 145.2 s |
| 4c · Approfondimento animato argomento 2 (2) · voce Kore | sì | P1 25:16.5 | 28.5 s |
| 4e · Pillola di ripasso argomento 2 | sì | P1 25:44.5 | 9.1 s |
| 4f · Schema guidato argomento 2 | sì | P1 25:53.2 | 31.1 s |
| 4g · Scheda Quiz 2 | sì | P1 26:23.9 | 5.0 s |
| 4a · Titolo argomento 3 | sì | P1 26:28.5 | 4.0 s |
| 4b · Prof + slide argomento 3 (tratto 1) | sì | P1 26:32.1 | 339.2 s |
| 4c · Approfondimento animato argomento 3 (1) · voce Kore | sì | P1 32:10.9 | 47.1 s |
| 4b · Prof + slide argomento 3 (tratto 2) | sì | P1 32:57.6 | 148.9 s |
| 4c · Approfondimento animato argomento 3 (2) · voce Kore | sì | P1 35:26.2 | 20.9 s |
| 4b · Prof + slide argomento 3 (tratto 3) | sì | P1 35:46.6 | 208.3 s |
| 4d · Mappa del prof argomento 3 (mappa.py, voce Kore) | sì | P1 39:14.6 | 26.2 s |
| 4e · Pillola di ripasso argomento 3 | sì | P1 39:40.3 | 9.3 s |
| 4f · Schema guidato argomento 3 | sì | P1 39:49.3 | 36.6 s |
| 4g · Scheda Quiz 3 | sì | P1 40:25.5 | 5.0 s |
| 4a · Titolo argomento 4 | sì | P1 40:30.1 | 4.0 s |
| 4b · Prof + slide argomento 4 (tratto 1) | sì | P1 40:33.7 | 124.2 s |
| 4c · Approfondimento animato argomento 4 (1) · voce Kore | sì | P1 42:37.5 | 30.5 s |
| 4b · Prof + slide argomento 4 (tratto 2) | sì | P1 43:07.7 | 105.8 s |
| 4c · Approfondimento animato argomento 4 (2) · voce Kore | sì | P1 44:53.1 | 22.0 s |
| 4b · Prof + slide argomento 4 (tratto 3) | sì | P1 45:14.6 | 213.1 s |
| 4d · Mappa del prof argomento 4 (mappa.py, voce Kore) | sì | P1 48:47.3 | 23.2 s |
| 4e · Pillola di ripasso argomento 4 | sì | P1 49:10.1 | 10.1 s |
| 4f · Schema guidato argomento 4 | sì | P1 49:19.9 | 34.0 s |
| 4g · Scheda Quiz 4 | sì | P1 49:53.5 | 5.0 s |
| 5 · Glossario P1 | sì | P1 49:58.1 | 33.5 s |
| 6 · Riepilogo finale P1 + saluto | sì | P1 50:31.2 | 27.8 s |
| 7 · Finale 5 s (avviso diritti) | sì | P1 50:58.6 | 5.0 s |
| 1 · Sigla | sì | P2 0:00.0 | 15.0 s |
| 3 · Copertina + ripasso della Parte 1 | sì | P2 0:13.6 | 20.6 s |
| 4a · Titolo argomento 5 | sì | P2 0:33.8 | 4.0 s |
| 4b · Prof + slide argomento 5 (tratto 1) | sì | P2 0:37.4 | 172.5 s |
| 4c · Approfondimento animato argomento 5 (1) · voce Kore | sì | P2 3:29.5 | 31.3 s |
| 4b · Prof + slide argomento 5 (tratto 2) | sì | P2 4:00.4 | 83.7 s |
| 4c · Approfondimento animato argomento 5 (2) · voce Kore | sì | P2 5:23.7 | 26.9 s |
| 4b · Prof + slide argomento 5 (tratto 3) | sì | P2 5:50.2 | 188.5 s |
| 4e · Pillola di ripasso argomento 5 | sì | P2 8:58.2 | 9.6 s |
| 4f · Schema guidato argomento 5 | sì | P2 9:07.4 | 44.2 s |
| 4g · Scheda Quiz 5 | sì | P2 9:51.2 | 5.0 s |
| 4a · Titolo argomento 6 | sì | P2 9:55.8 | 4.0 s |
| 4b · Prof + slide argomento 6 (tratto 1) | sì | P2 9:59.4 | 533.8 s |
| 4c · Approfondimento animato argomento 6 (1) · voce Kore | sì | P2 18:52.8 | 23.7 s |
| 4b · Prof + slide argomento 6 (tratto 2) | sì | P2 19:16.1 | 304.8 s |
| 4c · Approfondimento animato argomento 6 (2) · voce Kore | sì | P2 24:20.5 | 44.3 s |
| 4b · Prof + slide argomento 6 (tratto 3) | sì | P2 25:04.4 | 143.3 s |
| 4e · Pillola di ripasso argomento 6 | sì | P2 27:27.3 | 10.3 s |
| 4f · Schema guidato argomento 6 | sì | P2 27:37.2 | 42.4 s |
| 4g · Scheda Quiz 6 | sì | P2 28:19.2 | 5.0 s |
| 4a · Titolo argomento 7 | sì | P2 28:23.8 | 4.0 s |
| 4b · Prof + slide argomento 7 (tratto 1) | sì | P2 28:27.4 | 155.5 s |
| 4c · Approfondimento animato argomento 7 (1) · voce Kore | sì | P2 31:02.5 | 27.7 s |
| 4b · Prof + slide argomento 7 (tratto 2) | sì | P2 31:29.9 | 288.8 s |
| 4c · Approfondimento animato argomento 7 (2) · voce Kore | sì | P2 36:18.2 | 20.5 s |
| 4b · Prof + slide argomento 7 (tratto 3) | sì | P2 36:38.3 | 240.6 s |
| 4d · Mappa del prof argomento 7 (mappa.py, voce Kore) | sì | P2 40:38.5 | 26.6 s |
| 4e · Pillola di ripasso argomento 7 | sì | P2 41:04.8 | 9.3 s |
| 4f · Schema guidato argomento 7 | sì | P2 41:13.7 | 34.6 s |
| 4g · Scheda Quiz 7 | sì | P2 41:47.9 | 5.0 s |
| 4a · Titolo argomento 8 | sì | P2 41:52.5 | 4.0 s |
| 4b · Prof + slide argomento 8 (tratto 1) | sì | P2 41:56.1 | 104.0 s |
| 4c · Approfondimento animato argomento 8 (1) · voce Kore | sì | P2 43:39.7 | 25.3 s |
| 4b · Prof + slide argomento 8 (tratto 2) | sì | P2 44:04.7 | 123.9 s |
| 4c · Approfondimento animato argomento 8 (2) · voce Kore | sì | P2 46:08.1 | 28.6 s |
| 4e · Pillola di ripasso argomento 8 | sì | P2 46:36.4 | 9.2 s |
| 4f · Schema guidato argomento 8 | sì | P2 46:45.2 | 34.6 s |
| 4g · Scheda Quiz 8 | sì | P2 47:19.4 | 5.0 s |
| 5 · Glossario P2 | sì | P2 47:24.0 | 33.5 s |
| 6 · Riepilogo finale P2 + saluto | sì | P2 47:57.1 | 29.0 s |
| 7 · Finale 5 s (avviso diritti) | sì | P2 48:25.7 | 5.0 s |

`trans.wav` + dissolvenza (0,4 s; 1,4 s dopo la sigla) a ogni confine tra pezzi, compresi prof → approfondimento → prof, prof → mappa e mappa → pillola: 82 confini [per costruzione: un confine per pezzo]; `titolo.wav`, `repaso.wav`, `quiz.wav` (+0,5 s), `finale.wav` [per costruzione; il solo scatto del quiz è misurato].

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
| Tutto | visivo | Una pagina per argomento ferma 8–16 minuti, mappe a fasce gialle, nessun approfondimento (prima consegna di stanotte) | Corretti i punti 1–8 della master del 19/11 (sezione 1b) |
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
- Negli approfondimenti animati le date compaiono scritte in lettere («millenovecentosessantanove»), perché il testo a schermo è quello della voce Kore parola per parola; in una versione futura si possono scrivere in cifre [limite noto].
- Webcam del prof: 184×138 px ingrandita a 410×308: **morbida** (limite dell'originale) [misurato sul fotogramma].
- Non ho verificato la correttezza storica di quanto dice il prof oltre ai punti della sezione 6.

## 8 · Come ho verificato

Trascrizione con `trascrivi.py` (715 segmenti); allineamento delle card al parlato leggendo la trascrizione e scegliendo a mano i punti di cambio; audio del prof dall'originale con la catena del kit (denoise rnnn, loudnorm, aresample 48k, limiter); misure con `controllo_finale.py`, `controllo_jingle.py`, `ebur128` (loudness, true peak) sul file finale; foglio di tutti i pezzi, un fotogramma ogni 30 s e le tre mappe viste a occhio; correlazione audio/video per lo sfasamento (inconcludente).

## 9 · Tempi nel video nuovo (per la pagina)

**Parte 1** (durata 3063.6 s): arg. 1 «Il Sessantotto e la protesta studentesca»: inizio 322.633 s, quiz 1156.1 s; arg. 2 «L'Autunno caldo e le riforme»: inizio 1160.7 s, quiz 1583.9 s; arg. 3 «Gli anni di piombo e lo stragismo»: inizio 1588.5 s, quiz 2425.5 s; arg. 4 «Il caso Moro e la solidarietà nazionale»: inizio 2430.1 s, quiz 2993.5 s

**Parte 2** (durata 2910.667 s): arg. 5 «Conquiste sociali e crisi energetica»: inizio 33.833 s, quiz 591.233 s; arg. 6 «Gli anni Ottanta: riflusso e Pentapartito»: inizio 595.833 s, quiz 1699.2 s; arg. 7 «Tangentopoli e il crollo dei partiti»: inizio 1703.8 s, quiz 2507.933 s; arg. 8 «La transizione e i governi tecnici»: inizio 2512.533 s, quiz 2839.367 s

La scheda di pubblicazione ha i secondi nuovi; quelli della consegna precedente non valgono più.

## 10 · Correzioni del 20/11 (note della master 05:25)

- **Introduzione del prof sulla copertina max 3 minuti** [misurato]: la Parte 1 aveva il prof sulla copertina per 4,8 minuti. Ora resta sulla copertina da 0:35 a 2:44 (129 s); poi 3 slide «Di cosa parliamo» con gli 8 argomenti in card (3 + 3 + 2, ognuna 45–60 s), con il bordo giallo acceso quando il prof dice «si apre con il 68» (argomento 1) e «anni di piombo» (argomento 3). Nelle altre slide «Di cosa parliamo» non c'è bordo giallo perché il prof non nomina gli argomenti.
- **Come ho fatto la sostituzione** [per costruzione]: ho sostituito solo i fotogrammi del tratto di introduzione (stessa durata, 288,3 s); audio, sottotitoli e tutti gli altri pezzi sono invariati. Il video è stato ricodificato una volta (x264 CRF 18): peso 387,5 MB; durata, fotogrammi, loudness (−16,6 LUFS), picco (−4,0 dBFS) e scatto dei Quiz (+0,005 s) rimisurati, `controllo_finale` TUTTO OK.
- **`timeline_Parte1.json` e `timeline_Parte2.json` rigenerate** [misurato]: nella consegna del 19/11 erano quelle della versione precedente (2805,6 s e 2681,3 s); ora l'ultimo pezzo finisce a 3063,6 s e 2910,7 s, uguali alle durate dei video. `scheda_pubblicazione_Parte1/2.json` avevano già i tempi nuovi (durata_s 3063,567 e 2910,667).
