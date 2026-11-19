# RAPPORTO REVISIONE · Laboratori tecnologici ed esercitazione · Lezione 2 «Sartoria» (Prof.ssa Piera Caputi)

Tag `moda-laboratori-III-IV-lez02`, modello nuovo (Spagnolo Lez. 1). Voci: solo Kore, tutte reali dalla master (165 già esistenti + 63 degli schemi SC consegnate sul branch `voci-moda-laboratori-III-IV-lez02` il 19/11 alle 05:05 UTC). Nessuna voce generata da me, nessun segnaposto nel video finale (una prima versione con segnaposto è stata scartata e ricostruita con le voci vere, rimisurata da capo).

## 1. Durate e divisione in Parti (misurate sui file finali)

| | Durata | Peso | Fotogrammi | LUFS integrato | Picco | Silenzi > 3 s | sha256 |
|---|---|---|---|---|---|---|---|
| Parte 1 (argomenti 1-6) | 2757,5 s = 45:57 | 247,9 MB | 82724 letti (video 2757,47 s x 30) | -16,3 | -1,7 dBFS | 0 | `4c0834fa5597dff4b46c75b5a4696a6e353169adac032e194b279d29d87e3142` |
| Parte 2 (ripasso Parte 1 + argomenti 7-10 + glossario + riepilogo) | 2687,7 s = 44:48 | 241,2 MB | 80631 (= 2687,70 x 30) | -15,8 | -1,5 dBFS | 0 | `3f7bc7307003c02cbb1ff4df89829ecf02fadbcf3f3bedc4e638e669875dc9d0` |

Parte 1: voce del docente 34:48, approfondimenti 2:04, pillole 1:31, schemi 4:34, titoli 0:24, quiz 0:30. Parte 2: docente 36:44, approfondimenti 1:19, pillole 1:00, schemi 3:11, titoli 0:16, quiz 0:20.

Motivo delle durate sotto i 50 minuti: il video del docente dura 71:52 (4312 s), una lettura continua del PDF senza pause lunghe; con approfondimenti, pillole, schemi e quiz la lezione fa in tutto 90:45. Non raggiunge 50-60 minuti per ciascuna Parte e non ho aggiunto riempitivi. La divisione cade a fine argomento 6, alla fine di un tema (cucitura/elementi del capo), ed è la più bilanciata (scarto 69 s). La Parte 2 si apre con il ripasso animato della Parte 1 (pezzo RCP, voci RPR2).

Video 1920x1080, 30 fps, H.264 High (x264 veryfast crf 19, keyint 60, scenecut 0), AAC LC 48 kHz 160 kbit/s. Durata video = durata audio (mux con -shortest). Nel video non compare il numero della lezione né la parola «youtube». Font solo Bricolage Grotesque 800 e Figtree.

## 2. Controlli (strumenti del kit: controllo_finale.py, controllo_jingle.py, ffmpeg)

- Parlato (mediana dei pezzi D del controllo_finale): -16,2 LUFS (Parte 1), -16,0 LUFS (Parte 2). Integrato di tutto il file: -16,3 / -15,8 LUFS (intervallo -16 ±2: OK). Picco vero -1,7 / -1,5 dBFS (≤ -1: OK). Guadagno docente +5,5 dB, limitatore a -3,3 dBFS.
- Scatto jingle del Quiz (controllo_jingle): tutte le schede Q a +0,003 s dall'atteso (Parte 1: Q1-Q6, Parte 2: Q7-Q10), OK.
- Transizioni: ad ogni cambio di pezzo dissolvenza di 12 fotogrammi (0,4 s) con suono `trans` allineato (40 cambi in Parte 1, 29 in Parte 2); la scheda blu del titolo con suono `titolo`, la pillola con `repaso`, il Quiz con `quiz`.
- Silenzi (silencedetect -50 dB, 3 s): nessuno in entrambe le Parti.
- Fermi immagine: il rilevatore del controllo_finale (a fotogramma intero) segna 219 (Parte 1) e 147 (Parte 2) intervalli in D*: sono falsi positivi, perché a tutto schermo il solo tondo della docente (124 px) cambia meno della soglia. Misurato sul solo tondo (ritaglio 124x124 a 1594,154, freezedetect n=0,00005 d=1,0) in tutti i pezzi D: 0 fermi di 1 s o più nel tondo della docente (Parte 1: l'unico intervallo segnalato, 15,0 s per 16,7 s, è la copertina con la voce di benvenuto, in cui il tondo non è ancora presente; Parte 2: nessuno). Nessun taglio a metà frase della docente (le Parti e i pezzi D iniziano e finiscono su pause misurate).
- Sottotitoli (`.vtt`): riletti davvero. Controllati inizio e fine del file (Parte 1: primo blocco 00:00:16,055 sulla voce di benvenuto, ultimo 45:50 «Sesto: gli elementi del capo»; Parte 2: ultimo 44:40 «lo stiro e la scheda anagrafica»), nessun blocco sovrapposto, nessuno oltre la fine del video, e lettura a campione di 40 blocchi per Parte. Corretti nel parlato riconosciuto automaticamente circa 70 errori sistematici (cuscitura/cusitura→cucitura, imbassitura→imbastitura, lago→ago, siro/stilo→stiro, esagome→sagome, curicino→cucirino, croquet→crochet, sopragitto→sopraggitto, dispettatura→sdifettatura e simili). Possono restare errori isolati di riconoscimento su parole rare. Attacco dei blocchi sulla voce entro 0,3 s: il controllo_finale dà 78 % su 23 blocchi (Parte 1) e 76 % su 21 (Parte 2), sotto la soglia del 80 %: DA GUARDARE. Il controllo usa una soglia energetica globale che il rumore di fondo della stanza della docente sposta; verifica indipendente su 60 blocchi a campione della Parte 1: scarto mediano tra inizio del blocco e inizio del parlato -0,02 s; i blocchi fuori da 0,3 s sono casi in cui nella finestra cade la coda della frase precedente.
- Slide PDF A4: una pagina per ogni slide mostrata nel video, stessa grafica (Parte 1: 52 pagine, Parte 2: 57), costruita dagli stessi fotogrammi di stato usati nel video, quindi PDF = video.

## 3. Tabella dei pezzi (tutti presenti; nessuna mappa del prof nella release, nessun compito)
SIG = sigla `Sigla_Laboratori_moda_15s.mp4`; COV = copertina con card ARGOMENTI + voce di benvenuto; T = titolo blu; D = prof con slide sincronizzate (card in corso gialla, webcam a tondo con striscia gialla nome e materia); AN = approfondimento animato con voce; P = pillola di ripasso (intro blu); SC = schema bianco guidato; Q = scheda Quiz (5 domande, soglia 80 %); GLO = glossario; RIE = riepilogo finale; FIN = sigla finale 5 s con avviso diritti.
Ordine di ogni argomento: titolo blu, prof+slide con card gialla, approfondimento, pillola blu + schema bianco, quiz. Mappa del prof: non presente, quindi nessun pezzo e nessun PDF mappe. Compiti: nessuno.

### Parte 1

| Pezzo | Presente | Inizio (min) | Durata misurata (s) |
|---|---|---|---|
| SIG | sì | 0.00 | 15.0 |
| COV | sì | 0.25 | 36.5 |
| T1 | sì | 0.86 | 4.0 |
| D1 | sì | 0.93 | 448.1 |
| AN1 | sì | 8.39 | 22.0 |
| P1 | sì | 8.76 | 16.5 |
| SC1 | sì | 9.03 | 43.0 |
| Q1 | sì | 9.75 | 5.0 |
| T2 | sì | 9.84 | 4.0 |
| D2 | sì | 9.90 | 188.8 |
| AN2 | sì | 13.05 | 21.0 |
| P2 | sì | 13.40 | 15.8 |
| SC2 | sì | 13.66 | 54.4 |
| Q2 | sì | 14.57 | 5.0 |
| T3 | sì | 14.65 | 4.0 |
| D3 | sì | 14.72 | 232.9 |
| AN3 | sì | 18.60 | 21.2 |
| P3 | sì | 18.95 | 15.0 |
| SC3 | sì | 19.20 | 32.4 |
| Q3 | sì | 19.74 | 5.0 |
| T4 | sì | 19.83 | 4.0 |
| D4 | sì | 19.89 | 575.1 |
| AN4 | sì | 29.48 | 20.8 |
| P4 | sì | 29.83 | 15.6 |
| SC4 | sì | 30.08 | 56.4 |
| Q4 | sì | 31.02 | 5.0 |
| T5 | sì | 31.11 | 4.0 |
| D5 | sì | 31.17 | 241.8 |
| AN5 | sì | 35.20 | 17.8 |
| P5 | sì | 35.50 | 13.4 |
| SC5 | sì | 35.73 | 40.1 |
| Q5 | sì | 36.39 | 5.0 |
| T6 | sì | 36.48 | 4.0 |
| D6 | sì | 36.54 | 401.7 |
| AN6 | sì | 43.24 | 20.8 |
| P6 | sì | 43.59 | 14.9 |
| SC6 | sì | 43.83 | 47.4 |
| Q6 | sì | 44.62 | 5.0 |
| GLO | sì | 44.71 | 43.7 |
| RIE | sì | 45.44 | 26.3 |
| FIN | sì | 45.88 | 5.0 |

### Parte 2

| Pezzo | Presente | Inizio (min) | Durata misurata (s) |
|---|---|---|---|
| SIG | sì | 0.00 | 15.0 |
| COV | sì | 0.25 | 14.0 |
| RCP | sì | 0.48 | 27.4 |
| T7 | sì | 0.94 | 4.0 |
| D7 | sì | 1.01 | 283.2 |
| AN7 | sì | 5.73 | 20.6 |
| P7 | sì | 6.07 | 13.4 |
| SC7 | sì | 6.29 | 48.9 |
| Q7 | sì | 7.11 | 5.0 |
| T8 | sì | 7.19 | 4.0 |
| D8 | sì | 7.26 | 544.9 |
| AN8 | sì | 16.34 | 21.4 |
| P8 | sì | 16.70 | 15.5 |
| SC8 | sì | 16.95 | 49.8 |
| Q8 | sì | 17.79 | 5.0 |
| T9 | sì | 17.87 | 4.0 |
| D9 | sì | 17.93 | 862.6 |
| AN9 | sì | 32.31 | 20.4 |
| P9 | sì | 32.65 | 14.8 |
| SC9 | sì | 32.90 | 49.4 |
| Q9 | sì | 33.72 | 5.0 |
| T10 | sì | 33.80 | 4.0 |
| D10 | sì | 33.87 | 513.5 |
| AN10 | sì | 42.43 | 16.3 |
| P10 | sì | 42.70 | 16.1 |
| SC10 | sì | 42.97 | 42.7 |
| Q10 | sì | 43.68 | 5.0 |
| GLO | sì | 43.76 | 38.6 |
| RIE | sì | 44.41 | 18.3 |
| FIN | sì | 44.71 | 5.0 |

## 4. Cartamodelli e figure (ridisegno vettoriale)

- `diag_cintura.svg` (+ `confronto_cartamodelli_cintura_originale_vs_vettoriale.png`): figura «cintura» di p. 10 (tre gruppi: verde 1, rosa 2, azzurro 3, con la cucitura d'unione sul fianco). Ridisegnata su misure prese a mano sul fotogramma del video (mediana di 8 fotogrammi, rialzata 4x), scritte riscritte come testo vero in Figtree con testo identico alla docente. Controllo 4x sulla figura intera: forme, tacche delle pinces, posizione dei numeri e didascalie coincidono; scarto residuo: curve dei fianchi della gonna azzurra e della gonna rosa approssimate a mano (differenze di pochi pixel a 4x), pieghe a fruncio della cintura verde stilizzate. Difetti dell'originale non riprodotti: bordi sfocati e artefatti di compressione nel video; nel PDF le sagome sfumano a destra (macchie bianche).
- `diag_piegatura.svg` (+ confronto piegatura): sigle di piegatura 1A, 1B, 2A, 2B, 2C (p. 8), tabella come nell'originale, quadro «La piegatura del tessuto», evidenziazione gialla della sigla letta. Residuo: il motivo floreale è semplificato (stessi colori e disposizione, non ogni petalo), la piega 2C è schematica.
- Le foto dei punti a mano (p. 19-23: fili lenti, imbastitura rettilinea/diagonale/filza, sella, indietro, impuntura, sopraffilo, mosca, occhiello, resca, sottopunto, cieco) sono fotografie, non disegni tecnici: usate come immagini ritagliate dal PDF a 288 dpi, accanto alla scheda gialla del punto che la docente sta leggendo. Non vettorializzate.

## 5. Criticalità e residui (nessun contatto con la docente: tutto segnalato qui)

1. **Figura di p. 10 diversa tra video e PDF.** Nel video la docente mostra tre gruppi di cintura (con il terzo, azzurro, con cucitura sul fianco e la frase «Cintura che segue il diritto filo d'ordito e sul capo, la rigatura si presenta orizzontale con cucitura d'unione sul fianco»), il PDF rilasciato ne ha due. Ho seguito il video (immagini = quello che la docente dice in quel momento); il PDF andrebbe aggiornato dalla docente. La frase del terzo gruppo, assente dal PDF, è una scheda virtuale ricostruita dal parlato.
2. **Pagina 34 del PDF non letta nel video** (il video segue 33 pagine). Non è nel video né nelle slide.
3. **Paragrafi non letti dalla docente** (restano visibili sulla slide, ma non vengono mai evidenziati): «Le sagome così ottenute vengono infine…», «Il segno del gessetto è ideale…», «Durante il processo possono verificarsi…», rottura dell'ago, rottura del cucirino, cucitura non riuscita, problemi nella tensione. Alcuni paragrafi sono ripetuti o letti fuori ordine; ho ancorato le schede ai tempi del parlato misurato.
4. **Riconoscimento del parlato impreciso** (voce con rumore di stanza, qualche termine improvvisato). Sottotitoli corretti come in §2; possibili refusi residui su parole rare. Nel parlato la docente usa «a verso»/«avverso» per tessuto a verso, «tagliasnella»/«taglieforte» per taglie snelle e forti: nei sottotitoli ho sistemato i casi evidenti.
5. **Webcam a bassa risoluzione**: la sorgente è 852x480 con la docente in un cerchio di 62 px; il tondo è ritagliato e ingrandito a 124 px (circa 2x), pulito con maschera circolare e striscia gialla nome e materia. Non migliorabile senza la sorgente originale.
6. **Direttive europee** (etichettatura e composizione, scheda anagrafica/cartellino): nella scheda e nel parlato compare un richiamo normativo la cui formulazione (riferimento alla direttiva 2014/108/CE) andrebbe verificata dalla docente; l'ho lasciato come lei lo legge.
7. **Parti sotto i 50 minuti** (45:57 e 44:48): vedi §1, nessun riempitivo.
8. **Didascalia della pillola 1 (P1)**: la didascalia sotto la pillola è su tre righe e scende fino al bordo inferiore del fotogramma; leggibile, ma è il caso più stretto. Le altre pillole hanno una o due righe.
9. Mappa concettuale del docente: assente nella release (nessun pezzo MP nel video). I testi MP8_* ecc. presenti sul branch voci non sono montati.

## 6. File consegnati (cartella `revisione-moda-laboratori-III-IV-lez02/`)

`Laboratori_Lez2_Parte1_1080p.mp4.parte_00..02` e `Parte2` (da 90.000.000 byte, ricomporre con `cat`), `*.sha256` (hash del file intero), `Laboratori_Lez2_Parte1.vtt` e `Parte2.vtt`, `scheda_pubblicazione_Parte1.json` e `Parte2.json`, `quiz_Parte1.txt` e `quiz_Parte2.txt`, `verifica_finale.json` (12 domande da lez2.xlsx, 3 risposte sbagliate + 2 extra ciascuna), `timeline.json`, `Slide_Laboratori_Lez2_Parte1_A4.pdf` e `Parte2`, `foglio.png`, `confronto_cartamodelli_*.png`, `diag_*.svg`, i `controllo.txt` degli strumenti.
