# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 22 · Elsa Morante · VERSIONE 2 (17/11, dopo il rifiuto di Sara)
Video: `Letteratura_Lez22_Parte1_1080p.mp4` (a pezzi `.parte_00…03`, sha256 nel file `.sha256`, ricomponi con `cat FILE.mp4.parte_* > FILE.mp4`).
Etichette: **misurato** = misurato con uno strumento · **stima** = dedotto · **non verificato** = non ho potuto.
Le regole seguite sono quelle fino all'aggiornamento delle 08:45 del 17/11. (Gli aggiornamenti dopo le 08:45 sono per altre lezioni.)

## 0. Cosa non andava e cosa ho cambiato (rifiuto di Sara)
| Difetto indicato | Causa trovata | Correzione |
|---|---|---|
| Riquadro del prof **fermo** nella presentazione | l'introduzione (0:15–0:49, voce narrante) mostrava la foto del prof nel riquadro | **tolto**: nell'introduzione non c'è né riquadro né fascia. Il riquadro compare solo dove il prof parla davvero (video vivo) |
| **Niente jingle** | nel video vecchio c'erano solo `quiz.wav` e `titolo.wav`; mancavano `repaso.wav`, `trans.wav`, `finale.wav` | aggiunti come nel modello Spagnolo (vedi §1, jingle) |
| **Niente transizioni** | tagli secchi fra i pezzi | ogni passaggio fra due pezzi ha ora una **dissolvenza di 0,8 s con `trans.wav`** (61 transizioni). Dove il prof è coinvolto la dissolvenza usa il suo video vero prima/dopo il taglio (non un fermo) |
| **Audio e video sfasati** | misurato: l'audio del prof era in ritardo di **+0,020 s** (ritardo del filtro `arnndn`) e il video in anticipo di **1–2 fotogrammi** (0,03–0,07 s) su D2, D4, D5: insieme 0,05–0,09 s | audio compensato (−960 campioni); video rifatto con taglio **esatto al fotogramma** (`trim=start_frame`). Misura finale in §1 |
| Silenzi > 3 s | cartelli di argomento (3,5 s di silenzio), schede Quiz (3,0 s) e «Compiti» | cartelli 5,0→3,0 s, Quiz 5,3→4,5 s, Compiti 5,0→4,2 s; nessun silenzio > 3 s |
| «Aracoeli» si legge «Aracèli» (aggiornamento 08:45) | — | testi voce con «Aracèli», **9 voci nuove** (RA01–RA09) generate dalla master e rimontate: introduzione, approfondimenti 5a e 5c, mappa del ramo Aracèli, ripasso/schema/approfondimento 5, mappa finale, riepilogo. A schermo e nei sottotitoli resta «Aracoeli» |
| Card in corso | bordo blu e ombra bluastra | bordo **giallo** sottile + numero su pallino giallo, fondo bianco, ombre grigie morbide; le altre card con bordo grigio chiaro |

## 1. Misure sul video nuovo (misurato)
| Controllo | Risultato |
|---|---|
| Formato | 1920×1080, 30 fps, x264 veryfast (schede CRF 18, pezzi col prof CRF 20), AAC 192k 48 kHz |
| Durata / fotogrammi | **51:38,6 (3098,6 s)**, 92 957 fotogrammi = durata × 30. Peso **291,0 MB** |
| Volume | −16,4 LUFS integrato (LRA 6,0 LU). Picco (true peak) **−1,5 dBTP** (richiesto ≤ −1) |
| **Sincronia prof, per ogni pezzo** | audio dell'originale ↔ video finale (correlazione su finestre di 30 s ogni 40 s): **D1 0,0001 s · D2 0,0001 s · D3 0,0000 s · D4 0,0001 s · D5 0,0001 s**. Video (movimento del riquadro vs. originale): **0 fotogrammi** su tutti e 5. Scarto massimo audio/video: **0,0001 s ≤ 0,04 s** |
| Fermi immagine del prof | `freezedetect` (≥ 1 s) sul riquadro, 51 minuti: 56 fermi, **nessuno dentro D1–D5**: i fermi sono tutti sulle slide senza prof, dove il riquadro non c'è |
| Silenzi | `silencedetect` (−45 dB, ≥ 2,5 s): un solo silenzio, 2,7 s alla fine della scheda «Verifica finale»; **nessuno > 3 s** |
| **Jingle** (correlazione col file del kit) | `quiz.wav` sulle schede Quiz Q1–Q5 e Verifica: attacco a **+0,5 s dall'inizio, scarto 0,000 s** con `controllo_jingle.py` (Q1 695,9 · Q2 1306,3 · Q3 2008,5 · Q4 2574,7 · Q5 2950,7 s); correlazione 0,93–0,99. `titolo.wav` su T1–T5 (0,98–0,99) e su «Compiti» (1,00). `repaso.wav` sui 5 ripassi a +0,4 s (correlazione 0,36–0,46: è sotto la voce, per costruzione come nel modello). `trans.wav` all'inizio di approfondimenti, mappe, glossario e riepilogo, e in ogni transizione; `finale.wav` su «Fine». **Il livello di `trans.wav` sotto la voce non l'ho potuto misurare per correlazione** (misurato solo che l'energia nei primi 0,8 s c'è: RMS 225–368 contro 0 del video vecchio) |
| Controllo jingle | `controllo_jingle.py` con `quiz.wav` del kit (`Telesio_kit_produzione_v1/v5…zip`, `home/claude/v5/snd/`): 5/5 OK |
| PDF | slide: 85 pagine A4 orizzontale; mappe: 1 pagina |
| Sottotitoli | 828 cue, max 2 righe, nessuna sovrapposizione; scarto mediano 0,25 s (90° percentile 0,36 s) su 770 cue |

## 2. Confronto col modello Spagnolo (punto 000)
| # | Punto | Esito |
|---|---|---|
| 1 | Sigla 15 s → dissolvenza → copertina | **OK**: sigla del kit + dissolvenza di 0,8 s con suono |
| 2 | Copertina (logo, riga «LETTERATURA ITALIANA V · VIDEOLEZIONE», titolo, card ARGOMENTI a 2 colonne) | OK. Nell'introduzione **senza riquadro**; con riquadro solo quando il prof parla (inizio D1) |
| 3 | Slide: fondo bianco, «01 · ARGOMENTO», titolo + barretta, card | OK |
| 4 | Piè «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» + «Pagina N» | OK |
| 5 | Riquadro 4:3 con ombra grigia, niente bordo | OK: 412×309 px, x=1428 y=148, angoli r=18 |
| 6 | Fascia gialla −3°, due righe | OK, sempre visibile dove c'è il prof |
| 7 | Slide senza prof | OK, giallo solo per la card o la frase in corso |
| 8 | Font | Bricolage Grotesque 800, Figtree (etichette in Figtree Bold maiuscolo spaziato). DM Mono non usato |
| 9 | Finale 5 s con avviso diritti | OK, file del kit |
| 10 | Struttura | OK (vedi sotto per la durata) |
| 11 | PDF slide + mappe A4 orizzontale | consegnati; confronto PDF↔video su 10 pagine: differenza media 1,8–4,5/255 (solo la card in corso) |

## 3. Problemi trovati e correzioni (tutti)
| Minuto (video nuovo) | Tipo | Com'era | Correzione |
|---|---|---|---|
| 0:15–0:49 | visivo | riquadro del prof fermo nella presentazione | tolto (vedi §0) |
| tutto | audio | jingle mancanti; transizioni a taglio secco | vedi §0 e §1 |
| D1–D5 | sincronia | audio +0,020 s, video −1/−2 fotogrammi | vedi §0 |
| 6:41 → 11:44 | **audio** | pezzo del prof interrotto a metà frase: «lei continua [stacco] a scrivere. Il debutto…» | D1 finisce dopo «a scrivere.»; D2 parte da «Il debutto…» |
| 10:30 e simili | contenuto | mappe disegnate da noi | mappa del prof, nodi identici; voci nuove dedicate |
| T1–T5, Quiz, Compiti | audio | silenzi 3–3,5 s | schede accorciate (§0) |
| tutta la lezione | pronuncia | «Aracoeli» letto male | voci RA01–RA09; a schermo/sottotitoli «Aracoeli» |
| tutta la lezione | visivo | tondo, fondo azzurrino, ombre e card diverse dal modello | rifatto nel modello |
| D1–D5 | sincronia slide | evidenziazione card «a occhio»; pagine in ritardo fino a 33 s | pagine e card dal **parlato** del prof (±1,5 s, stima) |
| vtt | testo | 606 cue con errori («una belle poche scrittrici», «El Samorante», «Aracivi», «Guseppe», «le lotto operai»…) | 828 cue riscritti, ≈60 correzioni di nomi e termini; tempi riallineati sul video nuovo |
| audio prof | audio | non pulito | rifatto dall'originale (`aresample 48000, highpass 80, arnndn, loudnorm, alimiter`), −16,4 LUFS, picco −1,5 dBTP |
| consegna | file | mancavano `verifica_finale.json`; `compiti.json` nel formato sbagliato; titolo scheda | creati/corretti; compiti identici al PDF del prof (4/4) |

### Fine e inizio di ogni pezzo del prof (tabella richiesta dall'aggiornamento 01:25) — misurato su trascrizione e originale
| Pezzo | Inizio (video) | Prime parole | Fine (video) | Ultime parole | Frase finita |
|---|---|---|---|---|---|
| D1 | 0:54,30 | «Buongiorno e benvenuti alla lezione su…» | 6:41,20 | «…esattamente poco. Nel frattempo lei continua a scrivere.» | sì |
| D2 | 11:44,50 | «Il debutto, anzi il primo grande…» | 17:30,90 | «…personaggi agiscono come guidati da una fatalità magica.» | sì |
| D3 | 21:54,93 | «Nel 1957 la scrittrice…» | 28:21,70 | «…gli autori un po' più noti.» | sì |
| D4 | 33:37,10 | «Comunque noi affrontiamo serenamente tutto…» | 38:03,67 | «…questo fantasticare, questo andare oltre.» | sì |
| D5 | 43:03,33 | «Ecco. Terminiamo analizzando anche la trama…» | 45:39,70 | «…che sono, a mio giudizio, molto interessanti.» | sì |
Nessuna parola mozzata in partenza: i tagli cadono nelle pause fra frasi (la pausa prima della prima parola è ≥ 0,08 s in D2, ≥ 0,2 s negli altri).
(I tempi di questa tabella sono quelli del video nuovo; la durata è cambiata, vedi sotto.)

### Secondi vecchio → nuovo (la durata è cambiata: ogni transizione ha 0,8 s, le schede sono più corte)
La master rigenera la pagina. Aggiornati `scheda_pubblicazione.json` (`inizio_s`, `quiz_s`, `t_verifica`, `t_compiti`, `durata_s`, approfondimenti) e `testo_youtube.txt`. `quiz_argomenti.json` non contiene tempi.
| Punto | Vecchio | Nuovo | Differenza |
|---|---|---|---|
| Titolo argomento 1 | 48,9 s (0:48,9) | 50,5 s (0:50,5) | +1,6 s |
| Quiz 1 | 687,5 s (11:27,5) | 695,4 s (11:35,4) | +7,9 s |
| Titolo argomento 2 | 692,8 s (11:32,8) | 700,7 s (11:40,7) | +7,9 s |
| Quiz 2 | 1293,8 s (21:33,8) | 1305,8 s (21:45,8) | +12,0 s |
| Titolo argomento 3 | 1299,1 s (21:39,1) | 1311,1 s (21:51,1) | +12,0 s |
| Quiz 3 | 1990,0 s (33:10,0) | 2008,0 s (33:28,0) | +18,0 s |
| Titolo argomento 4 | 1995,3 s (33:15,3) | 2013,3 s (33:33,3) | +18,0 s |
| Quiz 4 | 2550,2 s (42:30,2) | 2574,2 s (42:54,2) | +24,0 s |
| Titolo argomento 5 | 2555,5 s (42:35,5) | 2579,5 s (42:59,5) | +24,0 s |
| Quiz 5 | 2921,0 s (48:41,0) | 2950,2 s (49:10,2) | +29,2 s |
| Verifica finale | 3040,1 s (50:40,1) | 3071,7 s (51:11,7) | +31,6 s |
| Compiti | 3059,6 s (50:59,6) | 3094,4 s (51:34,4) | +34,8 s |
| Durata totale | 3064,6 s | 3098,6 s | +34,0 s |
(Lo scatto del jingle del Quiz cade 0,5 s dopo questi inizi.)

## 4. Pagine del libro in alta risoluzione
La lezione 22 non ne ha: non applicabile.

## 5. Cosa NON ho verificato / limiti
- **Non ho ascoltato nulla.** Non verificati all'orecchio: fruscio/ronzio/«metallico» dopo la pulizia; **la pronuncia di «Aracèli»** (la trascrizione automatica le sente come «Araceli» in INTRO, AP5a, AP5c, MP5, R5, S5, RF1, e come «Arachali» in AN5 e «Aracelli» in MPF: coerente ma **non è una prova**); il volume del `trans.wav` sotto le voci (misurato solo che c'è); il gusto delle dissolvenze. Da ascoltare: 0:49, 11:35, 12:30 (transizioni), 10:40 e 49:10 (mappe), 44:00 (Aracèli).
- **Mappa del prof**: ne ha data una sola per la lezione; i 5 rami per argomento mostrano la stessa mappa con i nodi relativi in evidenza (come da decisione 00:40 «mappe solo del prof»).
- **Testa tagliata:** la webcam originale (247×139) è ritagliata in 4:3 e ingrandita 2,2×: immagine morbida. Nell'originale i capelli toccano il bordo alto (es. orig. 1:40, 4:00): non risolvibile.
- **Evidenziazioni delle card** (±1–2 s) e **testi degli approfondimenti** (letti con OCR dal video vecchio e riletti a vista solo in parte): non ricontrollati card per card all'ascolto.
- **Sottotitoli del prof**: testo fedele al parlato (esitazioni «Mm/Um» tolte), non riletto cue per cue all'ascolto. Cue dubbi lasciati: 6:34 «passano insieme velità» (forse «vent'anni»), 6:07 «è rimando… corso di storia», 23:35 «in un'isolita», 34:47 «Roma diata», 35:54 «Tupro», 37:40 «questa effecta», 42:46 «il coe».
- **Trasformazione del tempo:** la lezione dura 34 s in più del vecchio: la master aggiorna la pagina con la tabella sopra.

### DA CONFERMARE COL PROF
- **Separazione da Moravia:** parlato e linea del tempo dicono 1962, la **mappa** del prof dice 1961. Lasciati entrambi come sono.
- **«Pro o contro la bomba atomica»:** nel parlato «volume postumo del 1987»; nelle slide il 1965 è l'anno dell'intervento (non in conflitto, ma la card può farlo credere).

## 6. Come ho verificato
Trascrizione (Parakeet TDT, `trascrivi.py`) dell'originale e del video nuovo; correlazione audio originale↔finale su finestre di 30 s; correlazione del movimento nel riquadro originale↔finale (ritardi −6…+6 fotogrammi); `freezedetect`, `silencedetect`, `ebur128`; `controllo_jingle.py`; confronto PDF↔video su 10 pagine; 100 fotogrammi a 1/30 s (`controllo_minuti.jpg`); controllo energia del segnale ai punti di taglio.
