# RAPPORTO REVISIONE · Letteratura V · Lezione 5 · Giovanni Verga — 17/11/2026
Video rifatto nel modello Spagnolo. Etichette: **M** misurato · **S** stima · **NV** non verificato. File in questa cartella; video a pezzi `.parte_00…04` + `.sha256` (sha256 dei pezzi ricomposti verificato: M).

## 1. Misure sul video nuovo (M)
| Controllo | Risultato |
|---|---|
| Formato | 1920×1080, 30 fps, x264 veryfast (prof CRF 22, schede CRF 19), AAC 192k 48 kHz |
| Durata / fotogrammi | 56:57,73 · **102 532 fotogrammi = identici al montaggio precedente** (sigla 450, finale 150). Quiz, verifica e compiti restano agli stessi secondi, **tranne** il quiz 4 e l'inizio dell'argomento 5, spostati di **+1,03 s** (vedi §3): `scheda_pubblicazione.json` e `testo_youtube.txt` aggiornati (quiz 4 a 2649,7 s; argomento 5 a 2654,7 s) |
| Peso | 391,0 MB (sotto i 400) |
| Volume | −16,8 LUFS integrato, LRA 6,1; picco vero **−1,6 dBTP** (era −1,0: abbassato di 0,8 dB) |
| Jingle quiz (`controllo_jingle.py`) | Q1–Q5 scarto **+0,000 s**, tutti OK (jingle del kit `quiz.wav`, già presenti nell'audio) |
| Fermi immagine del prof (`freezedetect`, 0,6 s) | **nessuno** nei 5 pezzi del prof |
| Sincronia labbra/voce | video del prof preso dall'originale con scarto in fotogrammi interi uguale a quello dell'audio: scarto audio/originale misurato per correlazione −0,0066 / −0,0100 / −0,0099 / +0,0068 / −0,0099 s (max 0,010 s, limite 0,04): M. Guardata a occhio: NV |
| PDF | slide: **87 pagine** A4 orizzontale (una per slide, senza riquadro, senza fascia, senza evidenziazione); mappe: 1 pagina |

## 2. Confronto col modello Spagnolo (punto 000)
| # | Punto | Esito |
|---|---|---|
| 1 | Sigla → dissolvenza → copertina | OK: sigla del kit (450 fotogrammi), dissolvenza di 12 fotogrammi |
| 2 | Copertina | **corretto**: logo, «LETTERATURA ITALIANA V · VIDEOLEZIONE», titolo, barretta, card ARGOMENTI (una colonna, 5 voci) |
| 3 | Slide | **corretto**: fondo bianco, «01 · ARGOMENTO», titolo Bricolage 800 + barretta, card con bordo grigio; card in corso = bordo giallo + pallino giallo |
| 4 | Piè di pagina | **corretto**: «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» + «Pagina N» (nelle schede di servizio senza numero, come il modello) |
| 5 | Riquadro 4:3 | **corretto**: 412×309 px a x=1428 y=148, angoli r=18, ombra grigia, niente bordo; ritaglio 184×138 dalla webcam dell'originale, correzione immagine del kit (contrasto 1,04, saturazione 1,03, hqdn3d, cas 0,35) |
| 6 | Fascia gialla | **corretto**: −3°, «Giorgio Mazzotti» / «PROF. DI LETTERATURA ITALIANA», sempre visibile con il prof |
| 7 | Slide senza prof | **corrette**: ripassi, glossario, riepilogo, quiz, fine, verifica, compiti, «Ora tocca a te» senza riquadro (nessun riquadro fermo in presentazione: il prof compare solo quando parla davvero) |
| 8 | Font | Bricolage Grotesque 800, Figtree (Regular/SemiBold/Bold); etichette e piè in Figtree Bold; DM Mono non usato; onda audio decorativa eliminata |
| 9 | Finale | **OK**: `Sigla_finale_5s_con_avviso_diritti.mp4` (150 fotogrammi) |
| 10 | Struttura | sigla, presentazione, 5 argomenti con titolo + prof + ripasso + quiz, glossario, riepilogo, finale; seguono le schede Fine / Verifica finale / Compiti / «Ora tocca a te» |
| 11 | PDF slide + mappe | consegnati; confronto pagina per pagina col video: **NV** (le pagine sono generate dagli stessi file HTML delle slide del video, senza evidenziazione) |

## 3. Problemi trovati e correzioni
| Minuto | Tipo | Com'era | Correzione |
|---|---|---|---|
| tutto | visivo | prof nel tondo, fondo azzurrino, grafica diversa dal modello, copertina senza card | tutto rifatto (punti 2–7) |
| 43:23 circa | audio/montaggio | **il pezzo 4 del prof finiva a metà frase** («…ciclo dei Vinti,» | quiz e ripasso | «il primo romanzo.») | spostato il taglio di 31 fotogrammi: ora finisce a «…il primo romanzo.» (frase intera) e il pezzo 5 parte da «A seguire vi sarebbe…». Audio riordinato campione per campione, continuità verificata per correlazione 0,83–0,89 sull'originale. Durata totale invariata |
| 0:00–57:00 | visivo | slide del prof a passi regolari, evidenziazioni scelte a occhio | sequenza slide ricostruita sulle fasi **visibili nell'originale del prof** (slide di testo / pagine del libro) + abbinamento parlato↔testo; evidenziazione delle card dal parlato (S) |
| 0:00 | visivo | fotogramma fermo del prof in presentazione | presentazione senza riquadro; il prof compare dal «Buongiorno» |
| ripassi/glossario/riepilogo | testo | refusi, onda audio, etichette tra parentesi | testi riletti e corretti (accenti, apostrofi), «SCHEMA DI RIPASSO» senza parentesi |
| vtt | testo | 649 cue con errori gravi | rifatto dalla trascrizione del video finale (1084 cue, max 2 righe, tempi seguono il riordino audio). **Non riletto da una persona**: restano errori di trascrizione (es. «Foyer»); dizionario applicato (Zola, Dumas, Mastro-don Gesualdo, Verismo, Malavoglia) |
| fettine | pagina | pagine intere piccole, QR dell'editore visibili | usate le fettine del prof (immagini a risoluzione piena); **QR di 9 fettine coperti** (p6, 22, 38, 49, 60, 66, 78, 97, 112). Restano in alcune fettine i bottoni «ANALISI INTERATTIVA / ENTRA NEL TESTO» e un frammento «AUDIOLETTURA»/«IMMERSIVA» (NV controllo 100%) |
| audio | audio | picco −1,0 dBTP | −0,8 dB |
| fine | consegna | mancavano verifica, compiti, PDF | prodotti (§1) |
| scheda | testo | titolo «Giovanni Verga · Parte 1» | «Letteratura V · Lezione 5 · Giovanni Verga» |

## 4. Pagine del libro (B-bis)
Le fettine sono quelle della videodispensa del prof (`Letteratura_Lez5_videodispensa.pptx`): ritagli identici al libro a risoluzione piena (verificato su p12: identica alla pagina HD di `Lez05_ingrandita.zip`). **Non ho rifatto i tagli dagli screen HD**: pagina e file HD per fettina **NV**. Scala di visualizzazione 0,49–0,80 (mediana 0,66); altezza riga (box OCR) a 1080p su 5 campioni: 21–32 px → **per le strisce a due colonne il rigo può essere sotto i 26–30 px richiesti**. Ogni fettina ha bordo giallo quando è in corso; `controllo_fettine.jpg` mostra un fotogramma per ogni intervallo (68). Sincronia fettina↔voce: **S** (abbinamento lessicale parlato↔testo, ±10 s; il prof spesso commenta senza leggere).

| Brano | File (fettina n. della videodispensa del prof) | Minuto |
|---|---|---|
| T3 Rosso Malpelo | p6.png | 16:40–16:55 |
| T3 Rosso Malpelo | p7.png | 16:55–17:08 |
| T3 Rosso Malpelo | p6.png | 19:56–20:54 |
| T3 Rosso Malpelo | p7.png | 20:54–21:04 |
| T3 Rosso Malpelo | p8.png | 21:04–21:20 |
| T3 Rosso Malpelo | p9.png | 21:20–21:30 |
| T3 Rosso Malpelo | p10.png | 21:30–21:42 |
| T3 Rosso Malpelo | p11.png | 21:42–21:56 |
| T3 Rosso Malpelo | p12.png | 21:56–22:06 |
| T3 Rosso Malpelo | p13.png | 22:06–22:18 |
| T3 Rosso Malpelo | p14.png | 22:18–22:36 |
| T3 Rosso Malpelo | p15.png | 22:36–22:50 |
| T3 Rosso Malpelo | p16.png | 22:50–23:00 |
| T3 Rosso Malpelo | p17.png | 23:00–23:16 |
| T3 Rosso Malpelo | p18.png | 23:16–23:26 |
| T3 Rosso Malpelo | p19.png | 23:26–23:36 |
| T3 Rosso Malpelo | p20.png | 23:36–23:48 |
| T3 Rosso Malpelo | p21.png | 23:48–24:28 |
| T3 Rosso Malpelo | p22.png | 24:28–24:38 |
| T3 Rosso Malpelo | p23.png | 24:38–24:48 |
| T3 Rosso Malpelo | p24.png | 24:48–24:58 |
| T3 Rosso Malpelo | p25.png | 24:58–25:08 |
| T3 Rosso Malpelo | p26.png | 25:08–25:18 |
| T3 Rosso Malpelo | p27.png | 25:18–25:28 |
| T3 Rosso Malpelo | p28.png | 25:28–25:38 |
| T3 Rosso Malpelo | p29.png | 25:38–25:52 |
| T3 Rosso Malpelo | p30.png | 25:52–26:02 |
| T3 Rosso Malpelo | p31.png | 26:02–26:12 |
| T3 Rosso Malpelo | p32.png | 26:12–26:22 |
| T3 Rosso Malpelo | p33.png | 26:22–26:32 |
| T3 Rosso Malpelo | p34.png | 26:32–26:42 |
| T3 Rosso Malpelo | p35.png | 26:42–26:52 |
| T3 Rosso Malpelo | p36.png | 26:52–27:03 |
| T4 I «vinti» e la «fiumana del progresso» | p38.png | 32:05–32:17 |
| T4 I «vinti» e la «fiumana del progresso» | p39.png | 32:17–32:30 |
| T4 I «vinti» e la «fiumana del progresso» | p40.png | 32:30–32:43 |
| T5 Il mondo arcaico e l’irruzione della storia | p49.png | 40:36–40:48 |
| T5 Il mondo arcaico e l’irruzione della storia | p53.png | 40:48–41:02 |
| T7 I Malavoglia e la dimensione economica | p59.png | 41:02–42:02 |
| T7 I Malavoglia e la dimensione economica | p61.png | 42:02–42:26 |
| T7 I Malavoglia e la dimensione economica | p64.png | 42:26–42:36 |
| T8 La conclusione del romanzo e la partenza di ’Ntoni | p66.png | 42:36–42:50 |
| T8 La conclusione del romanzo e la partenza di ’Ntoni | p70.png | 42:50–43:18 |
| T8 La conclusione del romanzo e la partenza di ’Ntoni | p71.png | 43:18–43:24 |
| T8 La conclusione del romanzo e la partenza di ’Ntoni | p71.png | 44:18–44:26 |
| T12 La morte di mastro-don Gesualdo | p114.png | 44:26–45:06 |
| T12 La morte di mastro-don Gesualdo | p117.png | 45:06–45:30 |
| T12 La morte di mastro-don Gesualdo | p121.png | 45:30–45:42 |
| T12 La morte di mastro-don Gesualdo | p122.png | 45:42–45:58 |
| T12 La morte di mastro-don Gesualdo | p125.png | 45:58–46:10 |
| T12 La morte di mastro-don Gesualdo | p126.png | 46:10–46:30 |
| T12 La morte di mastro-don Gesualdo | p129.png | 46:30–47:20 |
| T12 La morte di mastro-don Gesualdo | p130.png | 47:20–47:30 |
| T12 La morte di mastro-don Gesualdo | p132.png | 47:30–47:40 |
| T12 La morte di mastro-don Gesualdo | p133.png | 47:40–48:40 |
| T9 La roba | p78.png | 48:40–48:58 |
| T9 La roba | p79.png | 48:58–49:08 |
| T9 La roba | p81.png | 49:08–49:18 |
| T9 La roba | p87.png | 49:18–49:40 |
| T9 La roba | p88.png | 49:40–50:12 |
| T9 La roba | p89.png | 50:12–50:24 |
| T9 La roba | p90.png | 50:24–50:42 |
| T9 La roba | p92.png | 50:42–50:54 |
| T9 La roba | p94.png | 50:54–51:40 |
| T10 Libertà | p96.png | 51:40–52:40 |
| T10 Libertà | p97.png | 52:40–53:06 |
| T10 Libertà | p100.png | 53:06–53:16 |
| T10 Libertà | p106.png | 53:16–53:26 |

## 5. COSA NON HO VERIFICATO
- Ascolto integrale (voce Kore: pronunce di nomi; «ecco/guarda/vedete» a 1:05, 14:41, 19:43, 20:30, 28:56, 30:35, 35:13, 50:44: non controllato che l'immagine nominata sia sullo schermo).
- Pulizia del rumore del prof: **non rifatta dall'originale con `arnndn`** (modello non disponibile qui); resta l'audio del montaggio precedente (correlazione 0,9 con l'originale). Fruscio/ronzio/metallico: NV.
- Transizioni: dissolvenze video di 12 fotogrammi nei cambi di scheda; `trans.wav` e gli altri jingle sono quelli già nell'audio: **non ho aggiunto né verificato** i suoni di transizione e il jingle di titolo/ripasso.
- Slide ferme > 60 s: 3 (227 s), 4 (290 s), 5 (356 s e 168 s), 37 (190 s), 47 (423 s). Coincidono con l'originale (il prof tiene a schermo la stessa slide di testo, verificato sulle fasi visibili); le card sono evidenziate dal parlato. L'ordine delle pagine nell'ultimo tratto (T5…T10) è **S**.
- Testa tagliata: nell'originale la webcam taglia già la testa in alto (es. 2:00, 29:10, 48:20 circa); non risolvibile. Webcam 184×138 ingrandita 2,2×: immagine morbida.
- OCR di tutti i fotogrammi del video nuovo; refusi nelle fettine (testo del libro): NV.
- Mappe: **non ridisegnate**, nella nostra cornice; il logo «MAPPE per la SCUOLA» è stato coperto; decide Sara sui diritti.
- Il confronto fotogramma-per-pagina del PDF slide col video non è stato fatto a mano.

## DA CONFERMARE COL PROF
La mappa dà «La Roba 1882», «La Lupa 1880», «Cavalleria rusticana 1880»; la slide T9 dice «pubblicata nel dicembre 1880, raccolta nel 1883». Non modificato.

## 6. Come ho verificato
Trascrizione completa (`trascrivi.py`) di originale e montato; correlazione audio per gli scarti; `ebur128` (volume, picco vero); `controllo_jingle.py`; `freezedetect`; contact sheet ogni 30 s (`controllo_minuti.jpg`) e per ogni fettina; fotogrammi a campione guardati; conteggio fotogrammi con ffprobe.
