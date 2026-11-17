# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 2 · La Scapigliatura
**Consegna 17/11/2026 (seconda versione, 17:45) · stato: REVISIONATA (con i limiti scritti in §5)** · ogni dato è etichettato *misurato* / *stima* / *non verificato*.

## 1. Misure sul video nuovo (`Letteratura_Lez2_Parte1_1080p.mp4`)
| Voce | Valore | Tipo |
|---|---|---|
| Durata / fotogrammi | 55:26,8 · 99 803 (attesi 99 803) · 1920×1080 · 30 fps · 266,1 MB | misurato |
| Vecchio video | 59:17,1 · 106 712 fotogrammi (la durata è cambiata: vedi §3, tabella secondi) | misurato |
| Volume | integrato −15,2 LUFS (include sigle e jingle); parlato del prof −16,0 LUFS sul file pulito (catena kit: aresample 48000, highpass 80, arnndn `sh.rnnn`, loudnorm −16); voci Kore portate a −16 LUFS | misurato |
| Picco reale | **−1,2 dBTP** (limite −1) | misurato |
| Jingle Quiz (`controllo_jingle.py`, `quiz.wav`) | 7/7 a +0,005 s (rifatto sul file finale) dall'inizio scheda + 0,5 s: OK | misurato |
| Altri jingle del kit | `titolo.wav` su ogni titolo di argomento (già presente), `repaso.wav` su ogni ripasso (**aggiunto**, mancava), `finale.wav` su «Fine della lezione» (**aggiunto**), schede Verifica/Compiti con jingle (**aggiunto**) | misurato (correlazione) |
| Silenzi > 3 s | **nessuno** (`silencedetect` −45 dB, 3 s); i più lunghi sono ≈ 2,9 s dopo il jingle di titoli e Quiz | misurato |
| Fermo immagine del riquadro del prof ≥ 1 s (`freezedetect` sul riquadro) | **nessuno** dentro i pezzi del prof (rifatto anche dopo la seconda passata su D3, D4, D5) | misurato |
| **Sincronia audio/video dei pezzi del prof** (correlazione audio del file finale con l'originale; scarto dei fotogrammi del riquadro con la webcam originale; 5 punti per pezzo) | audio **−20 ms** costanti (ritardo di codifica AAC), video **0 ms** su D1–D7: massimo 20 ms (limite 40 ms) | misurato |
| Sottotitoli | 934 blocchi, nessuna sovrapposizione, tempi dalla trascrizione Parakeet; testo del docente da trascrizione automatica con correzioni di nomi | misurato / **non riletti per intero** |

## 2. Confronto col modello Spagnolo (punto 000)
| # | Esito |
|---|---|
| 1 Sigla → dissolvenza → copertina | OK (sigla 15 s del kit; dissolvenza di 0,2 s su ogni giunzione tra pezzi, tranne sigle) |
| 2 Copertina | **corretto**: titolo, card ARGOMENTI su 2 colonne, riga «LETTERATURA ITALIANA V · VIDEOLEZIONE» |
| 3 Slide (fondo bianco, «0N · ARGOMENTO», barretta blu, tabelle intestazione blu notte) | **corretto** (tutte rifatte da testo del pptx del prof) |
| 4 Piè di pagina «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» + «Pagina N» | **corretto** (Figtree Bold) |
| 5 Riquadro 4:3 (412×310, x 1428 y 148, ombra grigia morbida, niente bordo) | **corretto**; ritaglio dalla webcam dell'originale 184×138 ingrandito 2,24× con correzione kit (hqdn3d, cas, contrasto 1,04, sat. 1,03): **morbido**, limite della sorgente |
| 6 Fascia gialla −3°, due righe, sempre visibile | **corretto** |
| 7 Slide senza prof | OK (ripassi, schemi, parole difficili, glossario, riepilogo) |
| 8 Font | solo Bricolage 800 / Figtree / (DM Mono non usato) |
| 9 Finale kit `Sigla_finale_5s_con_avviso_diritti.mp4` | **corretto** (prima: testo tagliato e 8 s di silenzio) |
| 10 Struttura | presente: sigla, presentazione, 7 argomenti (prof, ripasso con voce, schema, quiz 5 domande), approfondimenti, glossario, riepilogo, mappa del prof, finale |
| 11 PDF A4 orizzontale | `Letteratura_Lez2_slide.pdf` (62 pagine = slide del video senza riquadro e fascia; vettoriale) e `Letteratura_Lez2_mappe.pdf` (mappa del prof). **Confronto pagina per pagina con i fotogrammi: NON fatto** (stesso generatore per video e PDF) |

## 3. Problemi trovati e correzioni
| Minuto (vecchio video) | Tipo | Com'era | Correzione |
|---|---|---|---|
| tutta la lezione | audio/visivo | **Audio in anticipo sul video in modo progressivo**: scarto 0,03 s sul primo argomento fino a ≈ 1 s sul settimo (offset del prof rispetto all'originale: D1 0,03 · D3 0,25 · D5 0,57 · D7 0,97 s; jingle Quiz 7 a −1,24 s dall'attesa; voci Kore che partono fino a 0,6 s prima della scheda) | audio rifatto da zero con i file originali (prof dall'originale pulito, voci Kore dai `.wav`, jingle del kit) agganciato ai fotogrammi |
| tutti i pezzi del prof | visivo | prof nel tondo, nome su una riga | riquadro 4:3 + fascia gialla |
| tutte le slide | visivo | modello diverso da Spagnolo (fondo grigio, barretta gialla, etichetta senza «0N ·») | rifatte nel modello |
| fine D5 (orig. 1324 s) | audio | pezzo del prof tagliato a metà frase («…preludio di Emilio» / «Prague») | fine spostata dopo la frase |
| fine D6 (orig. 1816 s) | audio | tagliato a metà frase («…la noia e»…) | fine spostata a 1820,74 s dell'originale |
| fine D4 (orig. 1223 s) | audio | fine di «…a leggere» sul bordo | spostata dopo «…almeno alcune di queste.» (1226,58 s) |
| 58:51–59:17 | visivo+audio | finale con «GRAZIE PER L'ATTENZI» tagliato, senza logo, 8 s di silenzio | sigla finale del kit |
| 3300 s e dintorni | audio | schede Verifica/Compiti e ripasso senza jingle | jingle aggiunti |
| Preludio/Dualismo | pagina | pagina intera rimpicciolita, riga tagliata in fondo | 26 fettine dagli screen HD (vedi §4) |
| card 3 («significato letterale»), 309 s | visivo | evidenziata 12 s prima della frase del prof (321,6 s) | evidenziazione dai tempi parola per parola |
| mappe | contenuto | 7 mappe + 1 finale **fatte da noi**, non del prof (il prof ne ha una sola) | tolte; nel video la **mappa del prof** (voce nuova `RM1`, 108 s); mappa nel PDF |
| ripassi/schemi | visivo/testo | voci scritte alla pronuncia («Bodlèr», «Òffman», «boemièn», «Gòete», «Anjambmàn») anche sullo schermo | sullo schermo ortografia corretta (Baudelaire, Hoffmann, bohémien, Goethe, enjambement) |

### Tabella secondo vecchio → nuovo (la durata è cambiata: scheda_pubblicazione.json e timeline.json già aggiornati)
| Pezzo | vecchio (s) | nuovo (s) |
|---|---|---|
| Q1 | 529.1 | 491.0 |
| Q2 | 740.5 | 668.5 |
| Q3 | 1133.9 | 1028.9 |
| Q4 | 1710.2 | 1545.1 |
| Q5 | 1896.4 | 1696.8 |
| Q6 | 2570.7 | 2332.6 |
| Q7 | 3295.6 | 3006.8 |
| VERIFICA | 3538.4 | 3308.1 |
| COMPITI | 3552.0 | 3321.7 |

### Inizio e fine di ogni pezzo del prof (ultime parole dalla trascrizione, *stima*)
| pezzo | inizio | prime parole | fine | ultime parole | frase finita |
|---|---|---|---|---|---|
| D1 | 0:50.8 | Buongiorno e benvenuti alla lezione sulla | 7:10.3 | organizzato. con manifestazioni teoriche o manifesti codificati. | sì |
| D2 | 8:20.0 | Tra un bel po' di lezioni, | 10:19.3 | tra gli autori, i bersagli della polemica. | sì |
| D3 | 11:17.5 | Ecco, proviamo a parlare di questo | 16:15.3 | sempre uguali, a leggere cose sempre tranquille. | sì |
| D4 | 17:17.9 | Noi vogliom la barriera, ecco, capite | 24:27.8 | andiamo a leggere. almeno alcune di queste. | sì |
| D5 | 25:54.1 | Allora, parliamo di Emilio Praga, come | 27:32.3 | mistero. Vediamo quindi preludio di Emilio Prague. | sì |
| D6 | 28:25.8 | Allora, questa è, come potete vedere, | 36:41.8 | disperazione, e torna ovviamente su questo Podler. | sì |
| D7 | 39:01.6 | Arrigo Boito, dualismo. Come vedete, 1863, | 47:59.8 | e lo capite anche voi. a risolversi. | sì |

**Tagli corretti:** tutti i pezzi del prof finiscono e iniziano a frase finita. In una seconda passata ho spostato i tagli D3/D4 (796,66 s dell'originale, dopo «…cose sempre tranquille.») e D4/D5 (1226,58 s, dopo «…almeno alcune di queste.»); i tagli D1/D2, D2/D3, D5/D6 (dopo «Emilio Prague.») e D6/D7 (dopo «…questo Podler.») cadono già in una pausa (energia minima). Nei primi secondi di D3 e D4 le slide mostrano ancora quella del tema precedente finché il prof non passa al nuovo.

## 4. Pagine del libro in HD (fettine)
Sorgente: `Lez02_ingrandita.1.zip` → `Lez02/screen/Lez02_p038, 039, 041, 042, 043, 044.png`. Ogni fettina inizia e finisce su una riga bianca, prende solo la colonna del brano, senza intestazioni, numeri di pagina o riquadri; il rigo è ≈ 26 px o più a 1080p (scala ≥ 1,16 sulla sorgente HD). Le note a piè di pagina non sono state mostrate (spiegate dagli approfondimenti con voce). Foglio dei fotogrammi: `controllo_fettine.jpg` (un fotogramma a metà intervallo per ogni fettina, controllati a vista: nessuna riga tagliata).
| Fettina | Pagina | File (rettangolo in pixel) | Minuto video |
|---|---|---|---|
| A1 | p. 38 | Lez02/screen/Lez02_p038.png (334,235)-(875,507) | 28:41.6 |
| A2 | p. 38 | Lez02/screen/Lez02_p038.png (503,512)-(1593,731) | 29:41.3 |
| D | p. 38 | Lez02/screen/Lez02_p038.png (845,940)-(1602,1184) | 30:32.6 |
| E | p. 38 | Lez02/screen/Lez02_p038.png (839,1221)-(1573,1462) | 30:47.6 |
| F | p. 38 | Lez02/screen/Lez02_p038.png (761,1502)-(1592,1746) | 31:02.6 |
| G | p. 38 | Lez02/screen/Lez02_p038.png (760,1785)-(1694,2024) | 31:18.6 |
| H | p. 39 | Lez02/screen/Lez02_p039.png (740,232)-(1586,475) | 31:36.1 |
| I | p. 39 | Lez02/screen/Lez02_p039.png (830,511)-(1695,759) | 31:50.6 |
| J | p. 39 | Lez02/screen/Lez02_p039.png (740,794)-(1627,1046) | 32:01.1 |
| K | p. 39 | Lez02/screen/Lez02_p039.png (740,1078)-(1671,1317) | 32:40.6 |
| A2 | p. 38 | Lez02/screen/Lez02_p038.png (503,512)-(1593,731) | 33:33.1 |
| D | p. 38 | Lez02/screen/Lez02_p038.png (845,940)-(1602,1184) | 33:59.6 |
| G | p. 38 | Lez02/screen/Lez02_p038.png (760,1785)-(1694,2024) | 34:47.1 |
| H | p. 39 | Lez02/screen/Lez02_p039.png (740,232)-(1586,475) | 35:33.6 |
| K | p. 39 | Lez02/screen/Lez02_p039.png (740,1078)-(1671,1317) | 36:11.4 |
| S1 | p. 41 | Lez02/screen/Lez02_p041.png (272,1762)-(880,2109) | 39:13.7 |
| S2 | p. 41 | Lez02/screen/Lez02_p041.png (438,2356)-(1113,2765) | 39:43.3 |
| S3 | p. 42 | Lez02/screen/Lez02_p042.png (424,230)-(1047,642) | 40:08.3 |
| S4 | p. 42 | Lez02/screen/Lez02_p042.png (419,680)-(1047,1096) | 40:24.8 |
| S5 | p. 42 | Lez02/screen/Lez02_p042.png (417,1133)-(1011,1543) | 40:41.3 |
| S6 | p. 42 | Lez02/screen/Lez02_p042.png (419,1580)-(1098,1994) | 40:59.8 |
| S7 | p. 42 | Lez02/screen/Lez02_p042.png (418,2034)-(1066,2448) | 41:31.3 |
| S8 | p. 43 | Lez02/screen/Lez02_p043.png (414,232)-(1003,644) | 41:57.3 |
| S9 | p. 43 | Lez02/screen/Lez02_p043.png (414,685)-(1046,1106) | 42:11.3 |
| S10 | p. 43 | Lez02/screen/Lez02_p043.png (417,1143)-(1003,1555) | 42:26.3 |
| S11 | p. 43 | Lez02/screen/Lez02_p043.png (416,1601)-(1073,2013) | 42:39.3 |
| S12 | p. 43 | Lez02/screen/Lez02_p043.png (415,2051)-(1072,2473) | 42:57.8 |
| S13 | p. 43 | Lez02/screen/Lez02_p043.png (417,2507)-(1146,2927) | 43:16.3 |
| S14 | p. 44 | Lez02/screen/Lez02_p044.png (419,218)-(1060,629) | 43:28.8 |
| S15 | p. 44 | Lez02/screen/Lez02_p044.png (421,670)-(1085,1081) | 43:42.3 |
| S16 | p. 44 | Lez02/screen/Lez02_p044.png (402,1122)-(1058,1536) | 43:56.8 |
| S17 | p. 44 | Lez02/screen/Lez02_p044.png (408,1568)-(1074,1982) | 44:12.8 |
| S2 | p. 41 | Lez02/screen/Lez02_p041.png (438,2356)-(1113,2765) | 45:27.8 |
| S6 | p. 42 | Lez02/screen/Lez02_p042.png (419,1580)-(1098,1994) | 47:05.3 |
| S17 | p. 44 | Lez02/screen/Lez02_p044.png (408,1568)-(1074,1982) | 47:48.3 |

## 5. Cosa NON ho verificato / limiti noti
- **Ascolto**: nessun ascolto umano. Pronuncia delle voci Kore controllata solo confrontando la trascrizione automatica col testo: da ascoltare «Manzonismo» (resa «mansonismo» in S3 e glossario), «Igino Ugo» (resa «Gino Ugo» in R5/S5/riepilogo), «svolazziam» (approfondimento Preludio). Non ho rigenerato voci.
- **Rumore** del prof (fruscio/ronzio/metallico): applicata la catena del kit ma non ascoltata.
- **Sincronia labbra/voce**: misurata con la correlazione (audio −20 ms, video 0 ms); non ho guardato le labbra a occhio.
- **Evidenziazioni** (card in corso): tempi dalla trascrizione ma con sovrapposizioni stimate: *stima* ±1,5 s; per ripassi/schemi/glossario/riepilogo i tempi sono corretti sullo scarto medio (*stima*).
- **Testo delle slide**: preso dal pptx del prof (nessun OCR del video finale). Sottotitoli non riletti per intero; possibili errori residui di nomi.
- **Webcam**: 244×138 px nell'originale, ingrandita ×2,24: morbida; in alcuni punti la testa tocca il bordo alto già nell'originale (es. orig. 100 s, 1700 s).
- **Mappa del prof nel video**: schermata fissa di 108 s con voce RM1 (nessuna comparsa progressiva dei nodi). Una sola mappa per lezione (il prof non ne ha mandata una per argomento).
- **Dissolvenze**: 0,2 s verso il bianco su ogni giunzione; `trans.wav` usato solo sulla scheda Compiti. Non c'è un effetto sonoro di transizione tra tutti i pezzi.
- Slide extra «Avanguardia e ritardo italiano» (D4, 1077–1223 s dell'originale): il prof parla di cose che non sono sulle sue slide; schede scritte con le sue parole.

## DA CONFERMARE COL PROF
- Slide extra «Avanguardia e ritardo italiano» (frasi: «Manzoni è ancora vivo: morirà nel 1873», «anticipa i temi della letteratura decadente: mistero, crudeltà, bellezza malata»).
- Nome «Igino Ugo Tarchetti» (slide) pronunciato «Gino Ugo» dal prof.
- Data «il 6 febbraio» (pptx e Excel concordano; il prof dice «nel 1862»).

## 6. Come ho verificato
Ricomposizione e sha256 del video vecchio; trascrizione `trascrivi.py` (Parakeet) di video vecchio e originale; fotogrammi ogni 60/30 s; allineamento audio-originale (correlazione) dei pezzi del prof; slide dal pptx del prof; fettine dalle 6 pagine HD con coordinate OCR (rapidocr); `controllo_jingle.py`; `ebur128`, `silencedetect`, `freezedetect` (ffmpeg); confronto compiti (identici al PDF del prof) ed Excel (identico byte per byte). Video: piano di montaggio per pezzi (47 pezzi), una codifica x264 veryfast CRF 19, AAC 192k.
