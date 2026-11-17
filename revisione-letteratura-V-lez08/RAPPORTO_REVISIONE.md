# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 8 · Gabriele d'Annunzio (Prof. Giorgio Mazzotti)
Revisione del 17/11/2026. Video: `Letteratura_Lez8_Parte1_1080p.mp4` (a pezzi `.parte_NN`, sha256 nel file `.sha256`). Ogni dato è etichettato **misurato** / **stima** / **non verificato**.

## 1. Misure sul video nuovo
| Controllo | Risultato |
|---|---|
| Formato | misurato: 1920×1080, 30 fps, H.264 (CRF 19–21 veryfast), AAC 192k 48 kHz |
| Durata / fotogrammi | misurato: **4014,003 s = 66:54 · 120 420 fotogrammi = durata × 30 · identici al montaggio precedente**: quiz, verifica e compiti restano agli stessi secondi (Q1 1433,7 · Q2 2259,1 · Q3 2821,2 · Q4 3728,9 · Q5 3902,8 · verifica 3983,0 · compiti 4002,9/4007,7) |
| Peso | misurato: 364,0 MB |
| Volume | misurato: −16,6 LUFS integrato (prima: parlato del prof −16,5); picco −3,0 dBTP |
| Jingle Quiz (`controllo_jingle.py`) | misurato: Q1–Q5 scarto **+0,003 s** (OK, limite 0,05). Jingle presente in titoli (T1–T5), Quiz (Q1–Q5), verifica (VF, aggiunto), compiti (CP, aggiunto); transizione `trans.wav` aggiunta in ogni stacco |
| Fermi immagine del prof | misurato (`freezedetect`, riquadro, ≥ 1 s): **nessuno** in D0–D5 |
| Sincronia labbra/voce | stima: il video del prof è preso dall'originale con lo stesso scarto dell'audio del montaggio precedente (trovato per correlazione audio, 43 tratti a scarto costante); errore di quantizzazione ≤ 0,017 s (1 fotogramma = 0,033 s); **massimo ≈ 0,03 s** con l'incertezza di misura. Un controllo indipendente sul movimento delle labbra **non verificato** (webcam troppo piccola) |
| PDF | slide: **45 pagine** A4 orizzontale (vettoriale); mappe: 1 pagina A4 orizzontale |

## 2. Confronto col modello Spagnolo (punto 000)
| # | Punto | Esito |
|---|---|---|
| 1 | Sigla 15 s → dissolvenza → copertina | OK (sigla invariata; dissolvenza 1,6 s, nessun lampo) |
| 2 | Copertina: logo, «LETTERATURA ITALIANA V · VIDEOLEZIONE», titolo Bricolage, barretta, card ARGOMENTI | **corretto** (era titolo + elenco, con tondo). Durante la voce di benvenuto **niente riquadro del prof** (non parla); il prof compare dalla presentazione parlata |
| 3 | Slide: fondo bianco, «01 · ARGOMENTO», titolo + barretta, card | **corretto** (era fondo azzurrino, riga in DM Mono) |
| 4 | Piè di pagina + «Pagina N» | **corretto**: numeri 1–45, gli stessi del PDF; mai il numero della lezione |
| 5 | Riquadro 4:3, ombra grigia, niente bordo | **corretto**: 412×310 px a x=1428 y=148, angoli r=18, dall'originale con la correzione del kit (contrasto 1,04, saturazione 1,03, hqdn3d, cas 0,35) |
| 6 | Fascia gialla −3°, due righe, sempre visibile | **corretto** («Giorgio Mazzotti» / «PROF. DI LETTERATURA ITALIANA») |
| 7 | Slide senza prof | **corretto**: ripassi, glossario, riepilogo, schede titolo/quiz/verifica/compiti/fine rifatti nel modello |
| 8 | Font | Bricolage Grotesque 800 + Figtree. Etichette in Figtree Bold (DM Mono non usato) |
| 9 | Finale 5 s con avviso diritti | OK, invariato (3996,5–4001,6) |
| 10 | Struttura | OK: sigla, presentazione, 5 argomenti con ripasso e quiz, glossario, riepilogo, verifica, finale, compiti |
| 11 | PDF slide + mappe | consegnati; confronto: i PDF sono generati dallo **stesso HTML** delle slide del video (stato «tutte le card normali»), 45 pagine = 45 slide diverse del video; confronto fotogramma per fotogramma **non fatto una per una** (stima) |
Card «in corso» e ombre (aggiornamenti 01:30): bordo giallo sottile, numero su pallino giallo, fondo bianco, ombre grigie morbide ovunque (misurato a vista su fotogrammi di controllo).

## 3. Problemi trovati e correzioni
| Minuto | Tipo | Com'era | Correzione |
|---|---|---|---|
| tutta la lezione | visivo | prof nel **tondo**, fondo azzurrino, senza logo, senza fascia gialla | tutto rifatto nel modello (punti 1–8) |
| 3:30–3:38 | visivo/sync | il prof dice «Questa è una fotografia del d'Annunzio» ma sullo schermo c'era la slide 3 | mostrata la foto (slide 2 del prof) 3:29–3:38 |
| 12:48–13:26 | visivo/sync | il prof descrive la fotografia «lui che legge… il dolce divano», la foto non c'era | mostrata la foto (slide 5 del prof) 12:48–13:26 |
| 38:58–44:26 (argomento 3) | sincronia | card 3 «L'impianto del romanzo psicologico» accesa per **328 s** (2338–2666) mentre il prof parla del *Piacere* (card 2) | card 2 riaccesa da 39:56 |
| 44:01 | pagina | il prof dice «potete vedere degli estratti» e non c'era nulla | mostrato l'estratto T3 (p. 239) 44:01–44:04 |
| 3194–3330 s (53:14–55:30) | sincronia | pagina del libro ferma per 165 s mentre il prof commenta la poesia (panismo, Alcyone) | tornano le card «Alcyone» e «Il panismo» |
| 3536–3682 s (58:56–61:22) | sincronia | ultima pagina T7 ferma 146 s mentre il prof riassume la *Pioggia nel pineto* | card «Esempi significativi» / «Il panismo» |
| T6/T7 | pagina | pagine intere dal video (illeggibili), fettine non allineate | fettine HD (ritagli esatti dello screen HD, verificato: corrispondenza 1,00) in ordine di lettura; tempi dal parlato (stima ±8 s) |
| gruppo di card | sincronia | card «impegno politico» e «PGM/Fiume» raggruppate diversamente dal PPTX del prof | gruppi uguali al PPTX del prof, ordine di lezione |
| consegna | testo | mancava `compiti.json`; mancavano i PDF slide e mappe | prodotti (4 compiti del prof, testo identico; PDF da 45 e 1 pagina) |
| audio | audio | parlato −16,5 LUFS, non pulito | `highpass 80, arnndn (sh.rnnn), −16 LUFS`, partendo dal parlato del montaggio (stessi tagli) |
| audio | audio | **nessuna transizione sonora**, scheda Verifica e Compiti senza suono | `trans.wav` ad ogni stacco; jingle sulla Verifica e sui Compiti; jingle Quiz riallineati (erano a −0,082 s) |
| sottotitoli | testo | `.vtt` con errori («letturatura», «troppo 900», «tard 800») | rifatto dalla trascrizione (Parakeet) con correzioni sistematiche dei nomi (d'Annunzio, Alcyone, Nietzsche, Baudelaire…) e dei riempitivi; 948 cue, max 2 righe |
| scheda | testo | titolo «Gabriele d'Annunzio» | «Letteratura V · Lezione 8 · Gabriele d'Annunzio» |

## 4. Pagine del libro in alta risoluzione (B-bis)
Fonte: `Lez08_ingrandita.zip` (screen HD p. 239, 240, 258, 259, 262–265). Le fettine del PPTX del prof sono **ritagli esatti** degli screen HD (misurato sulle fettine 13–26: corrispondenza 1,00 a scala 1:1; le altre non misurate). **Non ritagliate di nuovo**: contengono ancora, dove il libro li ha, QR e riquadri «analisi interattiva» (es. fettine 13, 23, 31): **non risolto**.
Non compaiono le fettine T3 14–19 (il prof le accenna soltanto) e T6 30 (annotazioni, non lette).
| Brano | Pagina | File HD | Minuto |
|---|---|---|---|
| T3 · Un ritratto allo specchio (Il piacere) | 239 | Lez08_p239.png · fettina 13 (pptx) | 44:01.0–44:04.5 |
| T6 · La sera fiesolana | 258 | Lez08_p258.png · fettina 23 (pptx) | 49:54.0–50:14.0 |
| T6 · La sera fiesolana | 258 | Lez08_p258.png · fettina 24 (pptx) | 50:14.0–50:56.0 |
| T6 · La sera fiesolana | 258 | Lez08_p258.png · fettina 25 (pptx) | 50:56.0–51:32.0 |
| T6 · La sera fiesolana | 258 | Lez08_p258.png · fettina 26 (pptx) | 51:32.0–51:48.0 |
| T6 · La sera fiesolana | 259 | Lez08_p259.png · fettina 27 (pptx) | 51:48.0–52:14.0 |
| T6 · La sera fiesolana | 259 | Lez08_p259.png · fettina 28 (pptx) | 52:14.0–52:45.0 |
| T6 · La sera fiesolana | 259 | Lez08_p259.png · fettina 29 (pptx) | 52:45.0–53:14.5 |
| T7 · La pioggia nel pineto | 262 | Lez08_p262.png · fettina 31 (pptx) | 55:31.0–55:39.0 |
| T7 · La pioggia nel pineto | 262 | Lez08_p262.png · fettina 32 (pptx) | 55:39.0–56:08.0 |
| T7 · La pioggia nel pineto | 262 | Lez08_p262.png · fettina 33 (pptx) | 56:08.0–56:22.0 |
| T7 · La pioggia nel pineto | 263 | Lez08_p263.png · fettina 34 (pptx) | 56:22.0–56:42.0 |
| T7 · La pioggia nel pineto | 263 | Lez08_p263.png · fettina 35 (pptx) | 56:42.0–57:00.0 |
| T7 · La pioggia nel pineto | 263 | Lez08_p263.png · fettina 36 (pptx) | 57:00.0–57:10.0 |
| T7 · La pioggia nel pineto | 264 | Lez08_p264.png · fettina 37 (pptx) | 57:10.0–57:32.0 |
| T7 · La pioggia nel pineto | 264 | Lez08_p264.png · fettina 38 (pptx) | 57:32.0–57:52.0 |
| T7 · La pioggia nel pineto | 264 | Lez08_p264.png · fettina 39 (pptx) | 57:52.0–58:04.0 |
| T7 · La pioggia nel pineto | 264 | Lez08_p264.png · fettina 40 (pptx) | 58:04.0–58:16.0 |
| T7 · La pioggia nel pineto | 265 | Lez08_p265.png · fettina 41 (pptx) | 58:16.0–58:38.0 |
| T7 · La pioggia nel pineto | 265 | Lez08_p265.png · fettina 42 (pptx) | 58:38.0–59:00.5 |

## 5. Inizio e fine di ogni pezzo del prof (aggiornamento 01:25)
| Pezzo | Fine (min) | Ultime parole (trascrizione) | Frase finita? | Prime parole del pezzo |
|---|---|---|---|---|
| D0 | 3:23.0 | …si tratterà non tanto di letture. altro ti. | sì | «Buongiorno e benvenuti alla lezione su…» |
| D1 | 22:39.1 | …avrà anche altre donne in realtà in parallelo. | sì | «Questa è una fotografia del d'annunzio.…» |
| D2 | 36:29.4 | …Allora, adesso... nel millecentrentotto. | sì | «Nonostante il disprezzo ostentato per l'esistenza…» |
| D3 | 45:52.8 | …pastorale Metato nell'Arabruzzo, primitivo e magico dei pastori. | sì | «Dobbiamo assolutamente parlare, in questa seconda…» |
| D4 | 61:22.1 | …testo, diciamo così, piuttosto noto, insieme al piacere. | sì | «Ecco.…» |
| D5 | 64:20.7 | …Che appunto caratterizza il corpus, come dicevo. annunciare | NO: l’originale del prof finisce qui (3533,7 s) | «Per concludere il periodo del notturno.…» |
Nessuna parola mozzata in partenza (misurato su trascrizione).

## 6. Cosa NON ho verificato / limiti
- **Ascolto umano**: non ho ascoltato fruscio, ronzio, «metallico» dopo la pulizia, né la pronuncia della voce Kore (la trascrizione automatica ha sentito «Alcione/Alzione» per *Alcyone*: serve un ascolto; il testo voce è «Alcyone»). Non rigenerata nessuna voce.
- **Sottotitoli**: generati con correzioni automatiche; **non riletti cue per cue**. Restano errori di riconoscimento (es. 1:03 «C», 1:13 «A cavallo tra 8 e 9 e 100» per «tra Otto e Novecento», «Metato nell'Arabruzzo»): serve una rilettura umana. Le voci narranti non sono sottotitolate (come prima).
- **Evidenziazioni**: le card sono quelle del montaggio precedente, corrette dove il parlato le contraddiceva (tabella §3); le fettine dal parlato per allineamento (±8 s). Non ho riguardato ogni singola card con l'audio.
- **Mappe del prof**: il prof ne ha mandata **una sola** (mappa finale): rifatta nella nostra grafica (stesso contenuto, tolti logo di terzi e immagini). **Non inserita nel video** (cambierebbe i tempi); mancano le mappe per argomento: da chiedere a Sara.
- **Testa nel riquadro**: la webcam originale è 246×138; il 4:3 ne usa 185×139, ingrandita 2,2× (immagine morbida). Il prof è a volte vicino al bordo alto ma non tagliato nei fotogrammi guardati.
- **Fine D5 (64:20)**: l'originale del prof termina a 3533,7 s con la frase non conclusa («…come dicevo. d'Annunzio»): non allungabile.
- **Durata** 66:54: oltre i 65 minuti tollerati (regola 8/11).
- **Date da confermare col prof**: mappa «1898 va a vivere vicino Firenze con Eleonora Duse», slide/voce «Capponcina» senza anno; mappa «Laudi 1903-12» vs slide «Alcyone 1903».
- Il PDF slide è stato controllato a vista su 2 pagine, non una per una.

## 7. Come ho verificato
Trascrizione completa (`trascrivi.py`, 839 segmenti), allineamento audio vecchio↔originale (43 tratti), 1 fotogramma ogni 2 s del video vecchio (OCR e rilevazione evidenziazioni), fotogramma ogni 30 s del nuovo (`controllo_minuti.jpg`), `controllo_jingle.py`, `freezedetect`, ebur128, conteggio fotogrammi.
