# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 3 · Giosuè Carducci
Revisione del 16/11/2026. Video corretto: `Letteratura_Lez3_Parte1_1080p.mp4` (a pezzi `.parte_00…04`, sha256 nel file `.sha256`).
Regola: sotto, **misurato** = misurato con uno strumento; **stima** = dedotto; **non verificato** = non ho potuto.

## 1. Misure sul video nuovo (misurato)
| Controllo | Risultato |
|---|---|
| Formato | 1920×1080, 30 fps, x264 veryfast, AAC 192k (prima: 2560×1440) |
| Durata / fotogrammi (misurato, file finale) | 62:12,93 · 111 988 fotogrammi = durata × 30 · **identici al montaggio precedente**: quiz, verifica e compiti restano agli stessi secondi |
| Peso | 393,3 MB (375 MiB), sotto i 400 MB. Tratti col prof a CRF 22, il resto CRF 19 |
| Volume | −16,4 LUFS integrato (LRA 7,1). Picco (true peak) **−1,3 dBTP** (misurato sul file finale; prima era −0,8): ora ≤ −1 dBTP |
| Fermi immagine | Misurato sul file finale (riquadro, 45 s–59:49): nessun fermo ≥ 2 s mentre il prof parla; i soli fermi ≥ 2 s (8) cadono su schede senza prof (ripassi 11:13, 29:19, 45:59, schede quiz). Unico fermo del prof: 0:17–0:45 (voce narrante di benvenuto, foto-fotogramma), come prima |
| PDF | slide: 44 pagine A4 orizzontale (una per fettina e per slide); mappe: 1 pagina A4 orizzontale |

## 2. Confronto col modello Spagnolo (punto 000)
| # | Punto | Esito |
|---|---|---|
| 1 | Sigla 15 s → dissolvenza → copertina | OK (sigla invariata; dissolvenza rifatta) |
| 2 | Copertina (logo, riga «LETTERATURA ITALIANA V · VIDEOLEZIONE», titolo, card ARGOMENTI su 2 colonne) | **corretto** (era titolo + elenco senza card) |
| 3 | Slide: fondo bianco, «01 · ARGOMENTO», titolo + barretta, card | **corretto** (era fondo azzurrino, titolo e card diversi) |
| 4 | Piè di pagina «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» + «Pagina N» | **corretto**; ripassi/glossario avevano «Ripasso» al posto del numero |
| 5 | Riquadro 4:3, ombra grigia, niente bordo | **corretto**: 412×309 px a x=1428, y=148, angoli arrotondati r=18 (era un tondo) |
| 6 | Fascia gialla −3°, due righe | **corretto**: «Giorgio Mazzotti» / «PROF. DI LETTERATURA ITALIANA», sempre visibile |
| 7 | Slide senza prof | **corretto**: ripassi, glossario, riepilogo rifatti nel modello |
| 8 | Font | Bricolage Grotesque 800, Figtree. Etichette e piè in Figtree Bold come nel modello (DM Mono non usato: nel modello non c'è) |
| 9 | Finale 5 s con avviso diritti | OK (già presente, 61:57–62:02). Seguono le schede «Verifica finale» e «Compiti», che non ho toccato |
| 10 | Struttura | OK: sigla, presentazione, 4 argomenti con ripasso e quiz, glossario, riepilogo, finale |
| 11 | PDF slide + mappe | consegnati (vedi sotto) |

**Testa nel riquadro:** il taglio 4:3 prende la webcam dell'originale (184×138 px, ingrandita 2,2×: l'immagine è morbida perché l'originale è piccola). In diversi punti i capelli toccano il bordo alto già nell'originale (es. 0:05, 5:00, 28:20 dell'originale): non è risolvibile.

## 3. Problemi trovati e correzioni
| Minuto | Tipo | Com'era | Correzione |
|---|---|---|---|
| tutto | visivo | prof nel tondo, fondo azzurrino, grafica diversa dal modello | tutto rifatto: 22 slide + pagine del libro, riquadro 4:3, fascia (punti 000) |
| 3:43–4:36 | sincronia | slide «La vita e la giovinezza»: la card 2 (infanzia) non veniva mai evidenziata mentre il prof ne parlava; nessuna evidenziazione per 53 s | card 2 accesa a 3:43 |
| 8:12–9:12 | sincronia | slide «La carriera…»: card 2 (vita da studioso) mai evidenziata (nessuna card per 80 s) | card 2 accesa a 8:12 |
| tutte le slide | sincronia | evidenziazioni scelte a occhio | rifatte dal parlato del prof (stima, vedi §5) |
| 59:52–60:30 (ripasso 4) | testo | scheda 5: «Rime e ritmi, è del **1890nove**» | «è del 1899» |
| 61:13–61:50 (riepilogo) | testo | schede 3 e 4 senza titolo, testo in grassetto con «Tre,» e «Quattro,» | titoli come le schede 1 e 2, testo corretto |
| ripassi, glossario | grafica | piè «Ripasso», senza numero di pagina; sfondo azzurrino | modello Spagnolo, onda animata sulla voce |
| 37:37–45:52 · 47:51–57:47 | pagina | **16/11 (controllo master): fettine sbagliate.** Righe tagliate a metà in basso («…i versi han-» a 45:50), pezzi della colonna accanto tagliati a sinistra («del viale della stazione», «ROLE», «rosso cupo.»), «ALISI DEL TESTO» tagliato, «precedenti?» in alto. Causa: tagli su tutta la larghezza della pagina, con ripiego a 900 px quando non c'era una riga bianca | **rifatte tutte**: una colonna per volta, tagli solo su righe bianche, bordi su colonne bianche, controllo automatico dei 4 bordi (nessuna riga né colonna tagliata) e foglio `controllo_fettine.jpg` con un fotogramma per fettina (38) |
| vtt | testo | circa 60 errori: «Giosuèè», «Giambie ed epoti», «Giambi e ipodi», «le ho di barbare», «Leodi Barbare», «Gibaldina», «Giacomino», «rocci», «Cartucci», «Plumbeo» → «l'umbe», versi di Pianto antico, San Petronio, Alla stazione | corretti (800 cue, max 2 righe). Tempi invariati |
| audio | audio | parlato del prof non pulito con la catena del kit (non dimostrabile dall'ascolto) | rifatto dall'originale con `aresample 48000, highpass 80, arnndn (sh.rnnn), loudnorm −16, alimiter`, poi −0,3 dB: picco −1,3 dBTP, −16,4 LUFS; stessi offset del video |
| fine | consegna | mancavano verifica finale, compiti, PDF slide, PDF mappe | prodotti: `verifica_finale.json` + xlsx del prof (10 domande), `compiti.json` (4 esercizi), `…_slide.pdf`, `…_mappe.pdf` |
| scheda | testo | titolo «Giosuè Carducci · Parte 1» | «Letteratura V · Lezione 3 · Giosuè Carducci» |

## 4. Pagine del libro in alta risoluzione (B-bis) — fettine rifatte il 16/11
Zip `Lez03_ingrandita.1.zip`: pagine 50, 51, 53, 54, 56, 57, 58. **Regole applicate (misurato con un controllo automatico su ogni fettina):** una sola colonna per fettina (versi, note a sinistra/al centro/a destra, testata, «Temi principali», «Analisi del testo»); inizio e fine su una riga bianca; i quattro bordi senza inchiostro di testo; niente intestazioni, numeri di pagina, QR, etichette laterali, esercizi di comprensione né il quadro a p. 58. Le tabelle non si spezzano. Le fettine larghe («Analisi del testo») hanno il titoletto sempre unito al suo paragrafo. Fettina in corso con bordo giallo, dentro un riquadro con margine bianco (nulla è tagliato dalla cornice). Fotogrammi di controllo di tutte le 38 righe in `controllo_fettine.jpg` (fotogramma preso a metà intervallo dal video finale).
**Abbinamento fettina → voce: fatto a mano leggendo la trascrizione (parola per parola), non in automatico.** È comunque una **stima di ±3 s** (misurato: nessuna verifica all'ascolto).
| # | Brano | Pagina | Parte | File HD e ritaglio (px) | Minuto |
|---|---|---|---|---|---|
| 1 | Pianto antico (Rime nuove) | 50 | testata del brano | `Lez03_p050.png` x 330–1650, y 1927–2385 | 37:37–38:06 |
| 2 | Pianto antico (Rime nuove) | 50 | versi | `Lez03_p050.png` x 444–969, y 2463–2965 | 38:06–38:24 |
| 3 | Pianto antico (Rime nuove) | 51 | versi | `Lez03_p051.png` x 427–966, y 237–750 | 38:24–38:42 |
| 4 | Pianto antico (Rime nuove) | 50 | testata del brano | `Lez03_p050.png` x 330–1650, y 1927–2385 | 38:42–39:59 |
| 5 | Pianto antico (Rime nuove) | 50 | riquadro «Temi principali» | `Lez03_p050.png` x 1680–2197, y 1930–2165 | 39:59–40:34 |
| 6 | Pianto antico (Rime nuove) | 50 | versi | `Lez03_p050.png` x 444–969, y 2463–2965 | 40:34–40:50 |
| 7 | Pianto antico (Rime nuove) | 50 | note | `Lez03_p050.png` x 1385–2195, y 2472–2969 | 40:50–42:31 |
| 8 | Pianto antico (Rime nuove) | 51 | note, colonna sinistra | `Lez03_p051.png` x 170–830, y 819–944 | 42:31–43:19 |
| 9 | Pianto antico (Rime nuove) | 51 | versi | `Lez03_p051.png` x 427–966, y 237–750 | 43:19–43:40 |
| 10 | Pianto antico (Rime nuove) | 51 | note, colonna centrale | `Lez03_p051.png` x 850–1511, y 816–947 | 43:40–44:12 |
| 11 | Pianto antico (Rime nuove) | 51 | note, colonna destra | `Lez03_p051.png` x 1532–2192, y 496–951 | 44:12–44:44 |
| 12 | Pianto antico (Rime nuove) | 51 | versi | `Lez03_p051.png` x 427–966, y 237–750 | 44:44–45:18 |
| 13 | Pianto antico (Rime nuove) | 51 | «Analisi del testo» | `Lez03_p051.png` x 507–2192, y 1315–2134 | 45:18–45:52 |
| 14 | Nella piazza di San Petronio | 53 | testata del brano | `Lez03_p053.png` x 330–1630, y 1238–1593 | 47:51–48:22 |
| 15 | Nella piazza di San Petronio | 53 | riquadro «Temi principali» | `Lez03_p053.png` x 1640–2193, y 1240–1519 | 48:22–48:31 |
| 16 | Nella piazza di San Petronio | 53 | testata del brano | `Lez03_p053.png` x 330–1630, y 1238–1593 | 48:31–48:57 |
| 17 | Nella piazza di San Petronio | 53 | metro | `Lez03_p053.png` x 506–2191, y 1612–1797 | 48:57–49:13 |
| 18 | Nella piazza di San Petronio | 53 | versi | `Lez03_p053.png` x 427–1474, y 1866–2312 | 49:13–49:36 |
| 19 | Nella piazza di San Petronio | 53 | versi | `Lez03_p053.png` x 427–1474, y 2312–2607 | 49:36–49:54 |
| 20 | Nella piazza di San Petronio | 54 | versi | `Lez03_p054.png` x 425–1454, y 241–690 | 49:54–50:13 |
| 21 | Nella piazza di San Petronio | 54 | versi | `Lez03_p054.png` x 425–1454, y 690–1056 | 50:13–50:33 |
| 22 | Nella piazza di San Petronio | 54 | «Analisi del testo» | `Lez03_p054.png` x 505–2192, y 1579–1961 | 50:33–51:13 |
| 23 | Nella piazza di San Petronio | 54 | «Analisi del testo» | `Lez03_p054.png` x 505–2192, y 2664–2965 | 51:13–52:03 |
| 24 | Alla stazione in una mattina d'autunno | 56 | testata del brano | `Lez03_p056.png` x 260–1720, y 240–512 | 52:03–52:06 |
| 25 | Alla stazione in una mattina d'autunno | 56 | introduzione | `Lez03_p056.png` x 507–1659, y 538–684 | 52:06–52:19 |
| 26 | Alla stazione in una mattina d'autunno | 56 | metro | `Lez03_p056.png` x 507–1656, y 703–802 | 52:19–52:31 |
| 27 | Alla stazione in una mattina d'autunno | 56 | versi | `Lez03_p056.png` x 428–1397, y 902–1440 | 52:31–52:55 |
| 28 | Alla stazione in una mattina d'autunno | 56 | versi | `Lez03_p056.png` x 428–1397, y 1440–1979 | 52:55–53:25 |
| 29 | Alla stazione in una mattina d'autunno | 57 | versi | `Lez03_p057.png` x 421–1365, y 241–771 | 53:25–53:45 |
| 30 | Alla stazione in una mattina d'autunno | 57 | versi | `Lez03_p057.png` x 421–1365, y 771–1324 | 53:45–54:25 |
| 31 | Alla stazione in una mattina d'autunno | 57 | versi | `Lez03_p057.png` x 421–1365, y 1324–1854 | 54:25–54:48 |
| 32 | Alla stazione in una mattina d'autunno | 58 | versi | `Lez03_p058.png` x 424–1349, y 238–769 | 54:48–55:11 |
| 33 | Alla stazione in una mattina d'autunno | 58 | versi | `Lez03_p058.png` x 424–1349, y 769–1321 | 55:11–55:36 |
| 34 | Alla stazione in una mattina d'autunno | 58 | versi | `Lez03_p058.png` x 424–1349, y 1321–1650 | 55:36–55:54 |
| 35 | Alla stazione in una mattina d'autunno | 56 | testata del brano | `Lez03_p056.png` x 260–1720, y 240–512 | 55:54–56:20 |
| 36 | Alla stazione in una mattina d'autunno | 56 | metro | `Lez03_p056.png` x 507–1656, y 703–802 | 56:20–56:37 |
| 37 | Alla stazione in una mattina d'autunno | 56 | riquadro «Temi principali» | `Lez03_p056.png` x 1740–2194, y 242–513 | 56:37–57:38 |
| 38 | Alla stazione in una mattina d'autunno | 56 | testata del brano | `Lez03_p056.png` x 260–1720, y 240–512 | 57:38–57:47 |

## 5. Cosa NON ho verificato / limiti
- **Sincronia labbra:** il montaggio usa lo stesso offset per audio e video (misurato per correlazione audio, punteggio ≥ 0,55). Una verifica indipendente sul movimento della bocca non è conclusiva (webcam troppo piccola). **Non verificato.**
- **Ascolto umano:** non ho ascoltato fruscio/ronzio/metallico dopo la pulizia. Non verificato.
- **Evidenziazioni delle card:** calcolate con la trascrizione automatica (Parakeet, ±8 s); da controllare in almeno 4 punti da chi guarda. **Fettine:** abbinamento scritto a mano dalla trascrizione (±3 s, stima); ritagli verificati col controllo automatico dei bordi e a vista sul foglio `controllo_fettine.jpg`. In diversi punti (es. «Analisi del testo» a 45:18, 50:33, «Pesare le parole») il prof non legge la fettina: l'abbinamento è per argomento. **Non verificato all'ascolto.**
- **Testo piccolo:** le fettine larghe («Analisi del testo», «Metro») sono scalate a ≈ 0,8×: righe a ≈ 31–42 px a 1080p. Le fettine strette sono ingrandite fino a 1,5×.
- **Cose non fatte in questa riconsegna:** voci Kore da rigenerare (`R…` in `testi_voci.json`), schede finali «Quiz / Verifica / Compiti» nel modello, `controllo_jingle.py`: restano come nel rapporto precedente.
- **Voce narrante Kore:** nei ripassi pronuncia male «Levia Gravia» (45:56), «Giambi ed Epodi» e, nel riepilogo, «Le Odi barbare» (61:37, «Leo di barbare»). Non posso rigenerarla: serve il servizio della master (testi `R1…` da aggiungere a `testi_voci.json`). **Non corretto.**
- **Sottotitoli — da riascoltare:** 18:18 «alla Cereberi ma regina» e 22:31 «cantore italilo»: parola non decifrabile, lasciata com'è. Il resto del testo è stato riletto solo per le parole sospette (confronto con la trascrizione automatica), non cue per cue.
- **Mappa del prof:** impaginata in 1 pagina A4 con la nostra grafica, contenuto identico; tolti il logo di terzi (mappe-scuola.com) e le immagini (ritratto e frontespizio). **Non inserita nel video**: cambierebbe i tempi e i quiz si sfaserebbero su Vimeo. Decisione a Sara/master.
- **Date da confermare col prof (la mappa e le slide non coincidono):** mappa «Odi barbare 1889», «Rime e ritmi 1897», «Giambi ed Epodi 1879»; slide e voce «Odi barbare dal 1877», «Rime e ritmi 1899». Nella mappa ho lasciato le date del prof.
- **Quiz:** riletti contro il testo delle slide del prof: domande e risposte giuste coerenti. Invariati.
- **Controllo dei Quiz a 0,0 s (`controllo_jingle.py`):** non rieseguito (manca il file del jingle); il video dei quiz e il loro audio sono rimasti identici e ai secondi di prima.
- Schede di servizio «Quiz», «Verifica finale» e «Compiti» (stile diverso dal modello): non toccate.

## 6. Come ho verificato
Trascrizione completa (Parakeet TDT via `trascrivi.py`, 816 segmenti), OCR dei fotogrammi, 3733 fotogrammi a 1/s sul video vecchio, 124 fotogrammi a 1/30 s sul nuovo (`controllo_minuti.jpg`), controllo contiguità del piano (35 pezzi = 111 988 fotogrammi).
