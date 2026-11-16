# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 3 · Giosuè Carducci
Revisione del 16/11/2026. Video corretto: `Letteratura_Lez3_Parte1_1080p.mp4` (a pezzi `.parte_00…04`, sha256 nel file `.sha256`).
Regola: sotto, **misurato** = misurato con uno strumento; **stima** = dedotto; **non verificato** = non ho potuto.

## 1. Misure sul video nuovo (misurato)
| Controllo | Risultato |
|---|---|
| Formato | 1920×1080, 30 fps, x264 veryfast, AAC 192k (prima: 2560×1440) |
| Durata / fotogrammi | 62:12,93 · 111 988 fotogrammi = durata × 30 · **identici al montaggio precedente**: quiz, verifica e compiti restano agli stessi secondi |
| Peso | 414,4 MB (395 MiB). Tratti col prof a CRF 22, il resto CRF 19 |
| Volume | −16,1 LUFS integrato (LRA 7,1). Picco (true peak) −0,8 dBTP: 0,2 dB sopra il −1 dBTP chiesto per le sigle; non l'ho abbassato |
| Fermi immagine | Nessun fermo ≥ 2 s del riquadro mentre il prof parla. Unico fermo: 0:17–0:45 (voce narrante di benvenuto) con la foto-fotogramma del prof, come prima |
| PDF | slide: 34 pagine A4 orizzontale; mappe: 1 pagina A4 orizzontale |

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
| 10:30–15:00 · 36:00–46:00 | pagina | pagine del libro prese dal video, piccole e illeggibili | fettine dagli screen HD (tabella §4), rigo ≈ 27 px |
| vtt | testo | circa 60 errori: «Giosuèè», «Giambie ed epoti», «Giambi e ipodi», «le ho di barbare», «Leodi Barbare», «Gibaldina», «Giacomino», «rocci», «Cartucci», «Plumbeo» → «l'umbe», versi di Pianto antico, San Petronio, Alla stazione | corretti (800 cue, max 2 righe). Tempi invariati |
| audio | audio | parlato del prof non pulito con la catena del kit (non dimostrabile dall'ascolto) | rifatto dall'originale con `aresample 48000, highpass 80, arnndn (sh.rnnn), loudnorm −16, alimiter`, −1 dB di margine; stessi offset del video |
| fine | consegna | mancavano verifica finale, compiti, PDF slide, PDF mappe | prodotti: `verifica_finale.json` + xlsx del prof (10 domande), `compiti.json` (4 esercizi), `…_slide.pdf`, `…_mappe.pdf` |
| scheda | testo | titolo «Giosuè Carducci · Parte 1» | «Letteratura V · Lezione 3 · Giosuè Carducci» |

## 4. Pagine del libro in alta risoluzione (B-bis)
Zip `Lez03_ingrandita.1.zip`: pagine 50, 51, 53, 54, 56, 57, 58. Taglio solo sulle righe bianche, senza intestazioni, numeri di pagina, QR, margini. Fettina in corso con bordo giallo. **L'abbinamento fettina → voce è automatico (stima, ±8 s)**: va riguardato all'ascolto.
| Brano | Pagina | File HD | Minuto |
|---|---|---|---|
| Pianto antico (Rime nuove) | 50 | Lez03_p050.png · fettina 4 | 37:37–37:47 |
| Pianto antico (Rime nuove) | 50 | Lez03_p050.png · fettina 3 | 37:47–38:07 |
| Pianto antico (Rime nuove) | 50 | Lez03_p050.png · fettina 4 | 38:07–38:23 |
| Pianto antico (Rime nuove) | 51 | Lez03_p051.png · fettina 1 | 38:23–38:45 |
| Pianto antico (Rime nuove) | 50 | Lez03_p050.png · fettina 1 | 38:45–39:01 |
| Pianto antico (Rime nuove) | 50 | Lez03_p050.png · fettina 3 | 39:01–39:25 |
| Pianto antico (Rime nuove) | 50 | Lez03_p050.png · fettina 1 | 39:25–40:23 |
| Pianto antico (Rime nuove) | 51 | Lez03_p051.png · fettina 3 | 40:23–40:35 |
| Pianto antico (Rime nuove) | 50 | Lez03_p050.png · fettina 4 | 40:35–43:19 |
| Pianto antico (Rime nuove) | 51 | Lez03_p051.png · fettina 1 | 43:19–43:59 |
| Pianto antico (Rime nuove) | 51 | Lez03_p051.png · fettina 3 | 43:59–44:19 |
| Pianto antico (Rime nuove) | 51 | Lez03_p051.png · fettina 1 | 44:19–44:47 |
| Pianto antico (Rime nuove) | 50 | Lez03_p050.png · fettina 4 | 44:47–45:05 |
| Pianto antico (Rime nuove) | 51 | Lez03_p051.png · fettina 1 | 45:05–45:21 |
| Pianto antico (Rime nuove) | 51 | Lez03_p051.png · fettina 3 | 45:21–45:52 |
| Nella piazza di San Petronio | 53 | Lez03_p053.png · fettina 1 | 47:51–48:17 |
| Nella piazza di San Petronio | 53 | Lez03_p053.png · fettina 2 | 48:17–49:09 |
| Nella piazza di San Petronio | 53 | Lez03_p053.png · fettina 3 | 49:09–49:51 |
| Nella piazza di San Petronio | 54 | Lez03_p054.png · fettina 1 | 49:51–50:09 |
| Nella piazza di San Petronio | 54 | Lez03_p054.png · fettina 2 | 50:09–50:41 |
| Nella piazza di San Petronio | 54 | Lez03_p054.png · fettina 4 | 50:41–51:03 |
| Nella piazza di San Petronio | 54 | Lez03_p054.png · fettina 3 | 51:03–51:19 |
| Nella piazza di San Petronio | 54 | Lez03_p054.png · fettina 2 | 51:19–51:37 |
| Nella piazza di San Petronio | 53 | Lez03_p053.png · fettina 1 | 51:37–51:51 |
| Nella piazza di San Petronio | 53 | Lez03_p053.png · fettina 2 | 51:51–52:03 |
| Alla stazione in una mattina d'autunno | 56 | Lez03_p056.png · fettina 1 | 52:03–52:25 |
| Alla stazione in una mattina d'autunno | 56 | Lez03_p056.png · fettina 2 | 52:25–53:05 |
| Alla stazione in una mattina d'autunno | 56 | Lez03_p056.png · fettina 3 | 53:05–53:25 |
| Alla stazione in una mattina d'autunno | 57 | Lez03_p057.png · fettina 1 | 53:25–54:13 |
| Alla stazione in una mattina d'autunno | 57 | Lez03_p057.png · fettina 2 | 54:13–54:45 |
| Alla stazione in una mattina d'autunno | 58 | Lez03_p058.png · fettina 1 | 54:45–55:25 |
| Alla stazione in una mattina d'autunno | 58 | Lez03_p058.png · fettina 2 | 55:25–55:49 |
| Alla stazione in una mattina d'autunno | 57 | Lez03_p057.png · fettina 2 | 55:49–56:01 |
| Alla stazione in una mattina d'autunno | 56 | Lez03_p056.png · fettina 3 | 56:01–56:15 |
| Alla stazione in una mattina d'autunno | 56 | Lez03_p056.png · fettina 1 | 56:15–56:53 |
| Alla stazione in una mattina d'autunno | 56 | Lez03_p056.png · fettina 3 | 56:53–57:21 |
| Alla stazione in una mattina d'autunno | 58 | Lez03_p058.png · fettina 3 | 57:21–57:35 |
| Alla stazione in una mattina d'autunno | 56 | Lez03_p056.png · fettina 3 | 57:35–57:47 |

## 5. Cosa NON ho verificato / limiti
- **Sincronia labbra:** il montaggio usa lo stesso offset per audio e video (misurato per correlazione audio, punteggio ≥ 0,55). Una verifica indipendente sul movimento della bocca non è conclusiva (webcam troppo piccola). **Non verificato.**
- **Ascolto umano:** non ho ascoltato fruscio/ronzio/metallico dopo la pulizia. Non verificato.
- **Evidenziazioni e fettine:** calcolate con la trascrizione automatica (Parakeet, ±8 s); da controllare in almeno 4 punti da chi guarda.
- **Voce narrante Kore:** nei ripassi pronuncia male «Levia Gravia» (45:56), «Giambi ed Epodi» e, nel riepilogo, «Le Odi barbare» (61:37, «Leo di barbare»). Non posso rigenerarla: serve il servizio della master (testi `R1…` da aggiungere a `testi_voci.json`). **Non corretto.**
- **Sottotitoli — da riascoltare:** 18:18 «alla Cereberi ma regina» e 22:31 «cantore italilo»: parola non decifrabile, lasciata com'è. Il resto del testo è stato riletto solo per le parole sospette (confronto con la trascrizione automatica), non cue per cue.
- **Mappa del prof:** impaginata in 1 pagina A4 con la nostra grafica, contenuto identico; tolti il logo di terzi (mappe-scuola.com) e le immagini (ritratto e frontespizio). **Non inserita nel video**: cambierebbe i tempi e i quiz si sfaserebbero su Vimeo. Decisione a Sara/master.
- **Date da confermare col prof (la mappa e le slide non coincidono):** mappa «Odi barbare 1889», «Rime e ritmi 1897», «Giambi ed Epodi 1879»; slide e voce «Odi barbare dal 1877», «Rime e ritmi 1899». Nella mappa ho lasciato le date del prof.
- **Quiz:** riletti contro il testo delle slide del prof: domande e risposte giuste coerenti. Invariati.
- **Controllo dei Quiz a 0,0 s (`controllo_jingle.py`):** non rieseguito (manca il file del jingle); il video dei quiz e il loro audio sono rimasti identici e ai secondi di prima.
- Schede di servizio «Quiz», «Verifica finale» e «Compiti» (stile diverso dal modello): non toccate.

## 6. Come ho verificato
Trascrizione completa (Parakeet TDT via `trascrivi.py`, 816 segmenti), OCR dei fotogrammi, 3733 fotogrammi a 1/s sul video vecchio, 124 fotogrammi a 1/30 s sul nuovo (`controllo_minuti.jpg`), controllo contiguità del piano (35 pezzi = 111 988 fotogrammi).
