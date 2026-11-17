# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 21 · Cesare Pavese · Prof. Giorgio Mazzotti

Chat di revisione 21 · partita il 16/11/2026 · stato: **REVISIONATA — versione finale**

> Per Sara. Scrivo che cosa ho **misurato** (numeri veri letti dai file) e che cosa è una **stima** o una **lettura a occhio dai fotogrammi**. Non ho potuto **ascoltare**: dove scrivo «non verificato all'ascolto» è perché lo strumento qui è solo automatico.

## 1. Verdetto in una riga
La lezione consegnata (58:23, v2 del 15/11) **non è conforme al modello Spagnolo in nessuno degli 11 punti grafici** e ha **3 tagli del prof messi nel punto sbagliato**, **mappe che non sono quelle del prof**, **sottotitoli con molti errori** e **compiti/scheda in formato sbagliato**. Va **rifatta in grafica e rimontata**, non solo ritoccata. Il parlato del prof, le voci degli approfondimenti (verificate sul parlato del prof) e i quiz si riusano.

## 2. Che cosa ho verificato e come
| Controllo | Come | Esito |
|---|---|---|
| File integro | ricomposti i 2 pezzi, sha256 | **OK** (misurato) |
| Parlato di tutta la lezione | trascrizione completa Whisper *small* (italiano) con i tempi, letta riga per riga | fatto (3503 s) |
| Parlato dell'originale del prof | trascrizione con tempi di parola dell'originale (1705 s) | fatto |
| Voci narranti | trascritte tutte (34 file) e confrontate con il copione (SequenceMatcher) | 14 approfondimenti **OK**; **M1, M2, M3, M4 nuove con errori** (vedi §4) |
| Fotogrammi | 1 fotogramma ogni 2 s (1752) + foglio-contatto ogni 30 s, guardati tutti | fatto |
| Sincronia slide ↔ prof | letta la trascrizione contro la slide mostrata | **3 errori** (§3) |
| Volume | misura EBU R128 sui 5 pezzi del prof | −15,6 / −16,2 / −15,9 / −16,4 / −16,0 LUFS (**OK**, misurato); picco −0,3 dBFS in D4 (oltre −1) |
| Rumore | confronto spettro/rumore di fondo con l'originale | passa-alto presente (misurato); **«niente metallico» non verificato all'ascolto** |
| Silenzi > 3 s | silencedetect | 3 casi (§3) |
| Sottotitoli .vtt | 758 cue, nessuna sovrapposizione, max 2 righe (misurato) ma **testo pieno di errori** | da rifare |
| Quiz | 5×5, tutte le risposte «giuste» riscontrate sul parlato del prof | **OK** (1 nota: «Il compagno» 1946 nel parlato/slide, 1947 nella mappa del prof) |
| Verifica finale | confronto cella per cella con «DOMANDE LEZIONE 21.xlsx» | **identica** (10 domande, misurato) |
| Compiti | confronto con «LEZIONE 21.pdf» | **testo identico**, formato JSON sbagliato (§3) |
| Pagine del libro in alta risoluzione | lezione 21 **non è tra quelle con pagine del libro** | **salto B-bis** |

## 3. Problemi trovati (minuti = video consegnato v2)
| # | Minuto | Tipo | Com'era | Come lo correggo |
|---|---|---|---|---|
| 1 | 9:02–10:03 | sincronia | il prof parla di armistizio 1943, Resistenza e Casale Monferrato (è il punto 1 della slide dopo) mentre sullo schermo c'è «La delusione amorosa» | taglio spostato a fine frase («…figure femminili.»): l'argomento 2 parte da «Dopo l'armistizio…» con la slide 2, punto 1 evidenziato |
| 2 | 21:53–22:15 | audio | l'argomento 3 si apre con «E così l'abbiamo delineato… vedrete anche voi», che è la chiusura dell'argomento 2, dopo il quiz 2 | la chiusura resta alla fine dell'argomento 2; l'argomento 3 parte da «Allora, addentrandoci nella sua poetica» |
| 3 | 40:31 → 46:26 | audio | frase spezzata: «Ma soprattutto, come dicevo,» in fondo all'argomento 4, «il capolavoro…» in testa al 5, con 6 minuti di approfondimenti e quiz in mezzo | la frase resta intera in testa all'argomento 5 |
| 4 | 55:05, 58:05, 58:15 | audio | silenzi di 3,1 s, 4,7 s e 7,9 s (ultimo = cartello finale muto) | cartelli con suono; finale del kit (5 s) |
| 5 | scatti Q3, Q4, Q5 | audio | scatto del jingle +0,068 s (soglia 0,05), già segnalato dalla chat precedente | pezzi rifatti, controllo_jingle sul file nuovo |
| 6 | pezzo D4 | audio | picco −0,3 dBFS | alimiter −1 dB nella catena del kit |
| 7 | 56:30 | contenuto | Glossario: «Neorealismo: la letteratura del dopoguerra che racconta la realtà sociale» — non è del prof (per lui è la produzione promossa dal partito, che esalta il mito della povertà) | nuova voce GL2 con le parole del prof |
| 8 | 13:36, 20:27, 31:51, 44:32, 53:34, 55:02 | contenuto | le 6 «mappe» sono **inventate** dalla chat precedente (parole chiave «memoria, introversione, colpa…») | sostituite con la **mappa del prof** (una per argomento + finale), voci nuove M1–M5, MF |
| 9 | tutto il video | visivo | prof nel **tondo**, senza ombra morbida e **senza fascia gialla col nome** | riquadro **4:3 410×308**, angoli 18, ombra grigia morbida; fascia gialla −3° su due righe sempre visibile |
| 10 | tutto il video | visivo | fondo grigio-azzurro, schede blu a gradiente, «Fine della lezione»/«Quiz»/«Compiti» in blu scuro | fondo **bianco** come Spagnolo; stesse card e tabelle |
| 11 | 0:16–0:40 | visivo | copertina con «QUINTO ANNO» e «GLI ARGOMENTI DI OGGI» | «LETTERATURA ITALIANA V · VIDEOLEZIONE», titolo grande, card ARGOMENTI su 2 colonne |
| 12 | tutto il video | visivo | piè di pagina a destra «Introduzione», «Ripasso», «Approfondimento» o «Pagina n» non coerente col PDF | «Pagina N» progressivo, uguale al PDF slide |
| 13 | arg. 1–5 | visivo | slide del prof mostrate **2 punti su 4** per volta, testo abbreviato (es. manca «ma si isola nella letteratura» e «(affidatigli dalla donna amata, Tina Pizzardo)») | **4 punti col testo integrale delle slide del prof**; evidenziato quello detto (±1,5 s) |
| 14 | arg. 1–5 | visivo | schede non attive in grigio chiarissimo (poco leggibili per BES) | tutte nere su bianco |
| 15 | ≈11:30, ≈31:00, ≈53:00 | visivo | schede degli approfondimenti **tagliate dal piè di pagina** (AN1b, AN3c, AN5c) | tabelle in stile Spagnolo, mai spezzate, nessuna sbordata (verificato: bordo ≤ 968 px su 1080) |
| 16 | 13:36, 20:27, 31:51… | visivo | mappa ferma per 2–6 s con solo il nodo centrale | nodi che entrano a tempo con la voce |
| 17 | 0:34–0:40 | audio | titolo argomento 1 sopra le prime parole del prof | titolo con suono prima del prof |
| 18 | tutto il video | testo | sottotitoli fatti con Whisper *base*: es. «lezione succesare Pavese», «Una autore», «notici pari troppo», «sede disame» | **tutti i sottotitoli del prof riletti e corretti a mano** (357 cue); voci da copione |
| 19 | file | dati | `compiti.json` non nel formato richiesto | `{titolo, esercizi:[{n,tipo,testo}]}`, testo identico al PDF del prof |
| 20 | file | dati | scheda: titolo «Cesare Pavese · Parte 1» | «Letteratura V · Lezione 21 · Cesare Pavese» |
| 21 | file | dati | dispensa unica con mappe inventate | due PDF A4 orizzontali: `…_slide.pdf` (33 pagine = le slide del video, senza riquadro e senza nome) e `…_mappe.pdf` (6 pagine, mappa del prof) |

## 4. Cose che ti segnalo (non decido io)
1. **Il prof si contraddice tra slide, parlato e mappa.** Mappa: «a 5 anni rimane orfano di padre» ma slide e parlato dicono sei anni; mappa: *Il compagno* 1947, parlato e slide 1946; mappa: *La bella estate* 1949 (è il volume trittico: nel parlato il racconto è del 1940). Ho lasciato **la mappa identica a come l'ha mandata** e ho tenuto slide e quiz come il parlato. Se vuoi, chiedi al prof quale data vale.
2. **Nella mappa del prof c'era il logo «MAPPE per la SCUOLA» e una foto di Pavese**: per le regole (nessun marchio di terzi, mai foto scaricate) li ho **tolti**; il contenuto dei nodi è identico.
3. **La webcam del prof è piccola (245×139 px nell'originale) e lui siede alto**: nell'originale i capelli/fronte sono **già tagliati** in vari tratti (visto a 2:30, 7:00, 13:20, 20:00, 26:40 dell'originale). Non correggibile. Nel riquadro 4:3 l'immagine è ingrandita ×2,2: è un po' morbida.
4. Whisper è stato scaricato da un pacchetto pubblico npm (modello *small* convertito) perché huggingface è bloccato; checksum interno OK, **non confrontabile con l'originale OpenAI**. Serve solo a trascrivere, non entra nel prodotto.

## 5. Esito sul video nuovo (misurato sul file finale)
| Misura | Valore |
|---|---|
| Durata | **57:23,3** (3443,3 s) — tra 50 e 60 min |
| Fotogrammi | 103299 = durata × 30 (**OK**) |
| Peso | 210,5 MB (200,7 MiB), 1920×1080, x264 veryfast CRF 19, AAC 192k |
| Scatto quiz (controllo_jingle) | Q1–Q5 **+0,000 s** (OK) |
| Fermi immagine nei pezzi del prof | nessuno |
| Parlato del prof | mediana **−16,1 LUFS** (OK, ±2); catena del kit: 48 kHz, passa-alto 80, arnndn, loudnorm −16 a due passaggi, alimiter |
| **Picco audio (ebur128 peak, tutto il file)** | **−2,0 dBTP** (≤ −1, OK; prima −0,1) |
| Sincronia audio prof (correlazione col file originale, 3 punti per pezzo) | D1–D5 **0,015 s** (D5 fino a 0,016) → **≤ 0,04 OK** |
| Slide nel video = slide progettate | 67 confronti fotogramma↔slide, differenza media ≤ **3,7 su 255** (solo compressione; eccezione: la dissolvenza a nero del cartello Compiti) |
| PDF slide | **33 pagine** A4 orizzontale, stesse pagine e stesso ordine delle slide del video, senza riquadro e senza nome; numerazione «Pagina N» uguale al video (**confronto fatto**; le schede senza contenuto — titoli argomento, quiz, verifica, compiti, sigle — non hanno numero né pagina) |
| PDF mappe | 6 pagine A4 orizzontale (una per argomento + finale), mappa del prof con la nostra grafica |
| Sottotitoli | 812 blocchi, 0 sovrapposti, 0 oltre la fine, max 2 righe; **357 cue del prof riletti e corretti a mano**, voci da copione. Verifica sulla trascrizione automatica del video finale: **94,6 %** dei blocchi ritrovati nella finestra ±0,8 s (misura grossolana, per segmento); il controllo del kit sull'attacco entro 0,3 s dà **50 % su 16 punti verificabili → non raggiunge la soglia**, quindi **lo segnalo: l'allineamento fine ±0,3 s non è dimostrato**. Non ho potuto riascoltare |
| Font etichette (richiesta master 17/11) | «01 · ARGOMENTO», riga copertina e piè di pagina in **Figtree Bold maiuscolo spaziato** come `slide_1080p_esempio.png`, anche nel PDF slide (rifatto) |
| Titolo copertina | «Cesare Pavese» (non più tutto maiuscolo) |
| Card in corso | bordo giallo sottile, pallino numerato giallo, altre card con bordo grigio; ombre sempre grigie e morbide, anche nel PDF |
| Jingle | `titolo.wav` sui titoli argomento, `repaso.wav` sui ripassi, `trans.wav` sugli approfondimenti, `quiz.wav` su Quiz 1–5 (scatto +0,000 s) e su Verifica; `titolo.wav` su Compiti: nessuna scheda in silenzio |
| Transizioni | dissolvenza tra tutti i pezzi (bianco 0,35 s; da/verso nero 2 s per sigle) |
| Prof mai fermo | `freezedetect` sui pezzi del prof: nessun fermo; il riquadro c'è solo dove il prof parla davvero (copertina con prof = video vivo; copertina con voce di benvenuto senza riquadro) |
| Mai il numero della lezione nel video | OK (a vista sul foglio minuti) |

### Inizio e fine di ogni pezzo del prof (aggiornamento 01:25)
| Pezzo | Inizio | Fine: ultime parole | Frase finita |
|---|---|---|---|
| D1 | «Buongiorno e benvenuti alla lezione su…» | «…rapporto permanentemente difficile e tormentato con le figure femminili.» | **sì** |
| D2 | «Dopo l'armistizio dell'8 settembre…» | «…con gli autori che abbiamo nel frattempo già visto, d'accordo?» | **sì** |
| D3 | «Allora, addentrandoci nella sua poetica…» | «…metafore e da una profonda e dolorosa solitudine.» | **sì** |
| D4 | «Ecco, vediamo invece di delineare i romanzi.» | «…l'ideale pavesiano di un sano equilibrio interiore e sociale.» | **sì** |
| D5 | «Ma soprattutto, come dicevo, il capolavoro…» | «…fine della sua vita tramite appunto il suicidio.» | **sì** |
(Parole dalla trascrizione con tempi di parola dell'originale; tagli nelle pause tra frasi, nessuna parola mozzata in partenza.)

### Ritocchi del 17/11 ore 10:19 (aggiornamento per la lezione 21)
- «SCHEMA DI RIPASSO» senza parentesi quadre (5 slide, video e PDF slide).
- «MAPPA CONCETTUALE» in alto a sinistra sopra il titolo, in tutte le 6 slide-mappa (video, PDF slide e PDF mappe).
- Ricodificati solo i pezzi toccati (S1–S5, M1–M5, MF) e rifatto il video finale: **durata 57:23,3, 103299 fotogrammi, timeline identica** (secondi di scheda invariati); picco −2,0 dBTP, quiz +0,000 s. Verificato a vista sul video finale (ripasso 1 a 14:05; mappa finale a 54:52).

## 6. Tabella di confronto col modello Spagnolo (punto 000)
| # | Punto | Esito |
|---|---|---|
| 1 | Sigla 15 s → dissolvenza morbida → copertina | **corretto**: sigla del kit, poi dissolvenza da nero di 2 s (nessun lampo) |
| 2 | Copertina | **corretto**: logo, «LETTERATURA ITALIANA V · VIDEOLEZIONE», titolo grande, barretta, card ARGOMENTI su 2 colonne |
| 3 | Slide: fondo bianco, «01 · ARGOMENTO», titolo+barretta, tabelle | **corretto** (numero = argomento, mai la lezione) |
| 4 | Piè di pagina | **corretto**: «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» + «Pagina N» |
| 5 | Riquadro 4:3 410×308 (412×310), x 1428 y 148, angoli 18, ombra grigia, testa | **corretto** (testa tagliata dall'originale in vari tratti: §4) |
| 6 | Fascia gialla −3° su due righe, sempre visibile | **corretto** |
| 7 | Slide senza prof | **corretto**: Fine lezione, Verifica finale, Compiti in stile «Ora tocca a te» |
| 8 | Font | **OK**: solo Bricolage 800, Figtree, DM Mono |
| 9 | Finale | **corretto**: `Sigla_finale_5s_con_avviso_diritti.mp4` del kit |
| 10 | Struttura | **OK**: sigla → presentazione → 5×(titolo, prof, 3–4 approfondimenti animati, mappa del prof, ripasso, quiz) → mappa finale → glossario → riepilogo → fine → verifica → compiti → finale |
| 11 | PDF A4 slide + mappe | **fatto** (§5) |

## 7. Non verificato / limiti
- **Ascolto**: nessun ascolto umano. Rumore/«metallico», qualità delle voci Kore e sincronia labbra non verificati all'ascolto (solo misure).
- Sottotitoli: allineamento fine ±0,3 s non dimostrato (§5). Poche parole del prof restano incerte senza ascolto (es. attorno a 1660 s dell'originale, «il fronte dei…»).
- Le voci delle mappe M1–M4 sono state unite/tagliate da me a livello di parola (M2 conteneva istruzioni lette a voce, tagliate): **vanno riascoltate dalla master**.
- Mappa e slide del prof non coincidono su alcune date (§4).
- Webcam del prof a bassa risoluzione ingrandita ×2,2.

## 8. Consegna
Ramo `revisione-letteratura-V-lez21`: video a pezzi + sha256, `.vtt`, PDF slide, PDF mappe, quiz, verifica, compiti, scheda, testo YouTube, `controllo_minuti.jpg`, `timeline.json`. Durata misurata 57:23,3 (invariata), 103299 fotogrammi → stato `REVISIONATA`. La master riguarda e sostituisce su Vimeo.
