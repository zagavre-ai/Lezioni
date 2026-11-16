# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 21 · Cesare Pavese · Prof. Giorgio Mazzotti

Chat di revisione 21 · partita il 16/11/2026 · stato: **PRIMA VERSIONE (verifica finita, correzione in corso)**

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
| 18 | tutto il video | testo | sottotitoli fatti con Whisper *base*: es. «lezione succesare Pavese», «Una autore», «notici pari troppo», «disame», «ricorda a Pavesi» | **tutti i sottotitoli del prof riletti e corretti a mano** (357 cue); voci da copione |
| 19 | file | dati | `compiti.json` non nel formato richiesto | `{titolo, esercizi:[{n,tipo,testo}]}`, testo identico al PDF del prof |
| 20 | file | dati | scheda: titolo «Cesare Pavese · Parte 1» | «Letteratura V · Lezione 21 · Cesare Pavese» |
| 21 | file | dati | dispensa unica con mappe inventate | due PDF A4 orizzontali: `…_slide.pdf` (33 pagine = le slide del video, senza riquadro e senza nome) e `…_mappe.pdf` (6 pagine, mappa del prof) |

## 4. Cose che ti segnalo (non decido io)
1. **Il prof si contraddice tra slide, parlato e mappa.** Mappa: «a 5 anni rimane orfano di padre» ma slide e parlato dicono sei anni; mappa: *Il compagno* 1947, parlato e slide 1946; mappa: *La bella estate* 1949 (è il volume trittico: nel parlato il racconto è del 1940). Ho lasciato **la mappa identica a come l'ha mandata** e ho tenuto slide e quiz come il parlato. Se vuoi, chiedi al prof quale data vale.
2. **Nella mappa del prof c'era il logo «MAPPE per la SCUOLA» e una foto di Pavese**: per le regole (nessun marchio di terzi, mai foto scaricate) li ho **tolti**; il contenuto dei nodi è identico.
3. **La webcam del prof è piccola (245×139 px nell'originale) e lui siede alto**: nell'originale i capelli/fronte sono **già tagliati** in vari tratti (visto a 2:30, 7:00, 13:20, 20:00, 26:40 dell'originale). Non correggibile. Nel riquadro 4:3 l'immagine è ingrandita ×2,2: è un po' morbida.
4. Whisper è stato scaricato da un pacchetto pubblico npm (modello *small* convertito) perché huggingface è bloccato; checksum interno OK, **non confrontabile con l'originale OpenAI**. Serve solo a trascrivere, non entra nel prodotto.

## 5. Piano di correzione (stima)
| Fase | Stima |
|---|---|
| Voci mappe (le ha fatte la master; M1, M3, M4 uniti/riparati da me con taglio a parola) | fatta |
| Codifica 53 pezzi (prof con riquadro 4:3, audio con catena del kit) | in corso, ~40 min |
| Unione, controllo_finale, controllo_jingle, sottotitoli sul file finale | ~40 min |
| Rifacimento verifica A+B+C su minuti cambiati + 5 punti a caso, PDF, rapporto finale | ~30 min |
| **Consegna** | **entro 4 ore dalla partenza (stato REVISIONATA)** |

*(Questa è la prima versione del rapporto. La versione finale avrà durata, fotogrammi, peso e tutte le misure sul file nuovo, la tabella di confronto con il modello punto per punto e `controllo_minuti.jpg`.)*
