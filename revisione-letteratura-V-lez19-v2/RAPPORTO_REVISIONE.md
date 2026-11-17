# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 19 · «Dal secondo dopoguerra a oggi» (Prof. Giorgio Mazzotti)
Versione 17/11/2026 · stato: REVISIONATA (da riguardare dalla master) · ramo `revisione-letteratura-V-lez19`.

> **Attenzione: seconda revisione (v2) della lezione 19, fatta in una chat parallela.** Sul ramo `revisione-letteratura-V-lez19` esiste già una revisione consegnata il 17/11 alle 08:35 UTC (50:25, REVISIONATA). Questa cartella è alternativa e **non** l'ha sostituita: Sara o la master scelgono quale caricare.

Etichette: **M** = misurato, **S** = stima / lettura a vista, **NV** = non verificato.

## 1. Risultato in numeri (M)
| | Prima (consegna) | Dopo (revisione) |
|---|---|---|
| Durata | 53:44,2 (3224,17 s) | **50:09,47 (3009,47 s)** |
| Fotogrammi | 96.725 | **90.284 = durata × 30** (controllato) |
| Peso | 185,3 MB | **307,3 MB** (< 400), 4 pezzi + `.sha256` (ricomposto e controllato) |
| Formato | 1920×1080 | 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192k 48 kHz |
| Volume | −16,5 LUFS, picco −0,4 dBFS (oltre il limite) | **−16,2 LUFS integrati, picco vero −1,4 dBFS** (`ebur128 peak=true`) |
| Silenzi > 3 s | 8 (1290, 1295, 2089, 2146, 2992, 3053 s: 3,0–3,6 s; 3192–3200 e 3215–3224 s: 8,3 e 8,9 s) | **0** (nessun silenzio > 2,5 s) |
| Scatto jingle Quiz (`controllo_jingle.py`) | +0,000 / +0,002 / +0,035 s | **+0,005 / +0,005 / +0,005 s** (limite 0,05) |
| Fermi immagine ≥ 1 s nel riquadro del prof (`freezedetect`) | – | **0** nei 4 pezzi del prof |
| Scarto audio/video del prof (12 punti) | – | audio vs originale **−0,02 s**; video vs originale **0 fotogrammi** (energia di movimento, correlazione 0,98–0,99 dove il prof si muove; dove sta fermo la misura non è significativa) → scarto massimo **0,02 s** (limite 0,04) |

## 2. Confronto con il modello Spagnolo Lez. 1 (punto 000), punto per punto
| # | Punto | Esito |
|---|---|---|
| 1 | Sigla 15 s → dissolvenza → copertina | **corretto**: `Sigla_Letteratura_15s.mp4` del kit, poi copertina con dissolvenza da nero di 1 s (nessun lampo) |
| 2 | Copertina | **corretto**: logo, riga «LETTERATURA ITALIANA V · VIDEOLEZIONE», titolo Bricolage 800 con barretta, card «ARGOMENTI» (3 argomenti). Copertina senza prof mentre parla la voce; con riquadro e fascia solo quando il prof parla davvero |
| 3 | Slide su fondo bianco, «01 · ARGOMENTO», titolo + barretta | **corretto**: tutte le slide rifatte su fondo bianco (prima: schede, approfondimenti, ripassi, quiz, glossario su fondo blu scuro/grigio). Numero = numero dell'argomento, mai della lezione |
| 4 | Piè di pagina | **corretto**: «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» + «Pagina N» (N progressivo 1–37 nell'ordine del video) in Figtree Bold spaziato |
| 5 | Riquadro del prof 4:3 ~410×308, ombra morbida, niente bordo | **corretto**: 412×310 px a x=1428, y=148, angoli arrotondati r=22, ombra grigia; ritaglio 4:3 (185×139 px) dall'**originale** del prof con correzione del kit (contrasto 1,04, saturazione 1,03, `hqdn3d=1.5:1.5:3:3`, `cas=0.35`). Il tondo non c'è più |
| 6 | Fascia gialla col nome | **corretto**: due righe, −3°, «Giorgio Mazzotti» / «PROF. DI LETTERATURA ITALIANA», visibile in tutti i pezzi con il prof |
| 7 | Slide senza prof | **corretto**: testo grande (card 40 px, 27–34 px), card in corso con bordo giallo e numero su pallino giallo, le altre grigio chiaro, stesso logo e piè di pagina |
| 8 | Font | **corretto**: Bricolage Grotesque 800, Figtree (incl. Figtree Bold spaziato per le etichette). Nessun DM Mono. Confronto a vista con `slide_1080p_esempio.png` (S) |
| 9 | Finale | **corretto**: `Sigla_finale_5s_con_avviso_diritti.mp4` del kit. Tolti «Fine della lezione», scheda Verifica finale e schede Compiti |
| 10 | Struttura | **OK**: sigla → presentazione → per argomento: titolo (jingle), prof, approfondimenti con voce, ripasso con voce (jingle), schema, quiz (jingle) → mappa del prof → glossario → riepilogo → finale. Verifica finale e compiti fuori dal video |
| 11 | PDF A4 orizzontale | **fatti**: `…_slide.pdf` (37 pagine) e `…_mappe.pdf` (1 pagina: il prof ha mandato una sola mappa per tutta la lezione) |

## 3. Problemi trovati e corretti
| Minuto (video vecchio) | Tipo | Com'era | Come l'ho corretto |
|---|---|---|---|
| tutto | visivo | prof nel tondo, nessuna fascia gialla, fondo grigio/blu scuro, stile diverso da Spagnolo | tutta la grafica rifatta nel modello Spagnolo (punti 1–11 sopra) |
| 13:35 → 21:38 (fine D1 / inizio D2) | audio (prof) | **prof tagliato a metà frase**: il pezzo finiva con «…la pluralità, la ricchezza.» e il pezzo dopo ripartiva con «L'incredibile vastità di argomenti…» (stessa frase, interrotta da 8 minuti di approfondimenti) | pezzo allungato fino a fine frase («…della persona è fondamentale.»): ora il confine cade nella pausa dopo la frase |
| 35:46 → 35:53 (fine D2 / inizio D3) | audio (prof) | **prof tagliato a metà frase**: finiva con «Gio Caproni, Alda Merini» e il pezzo dopo iniziava con «Patrizia Cavalli, vedete… e Patrizia Valduga» (stessa frase, divisa tra argomento 2 e 3) | confine spostato dopo «…e Patrizia Valduga.», prima di «I maestri della narrativa» |
| tutti i pezzi del prof | audio | i pezzi del prof erano stati accorciati rispetto all'originale di circa 16 s in totale (pause tolte all'interno dei pezzi; S, dall'allineamento delle parole: 3 s in D1, 9 s in D2, 4 s in D3) | pezzi rifatti **dall'originale intero e continuo** (nessun taglio interno) |
| 0:32 | audio (voce) | l'introduzione diceva «La storia e la società?» come primo argomento, ma l'argomento è «L'Italia dal dopoguerra a oggi» | introduzione rifatta con la voce RV1 (già pronta sul ramo voci), **tagliata dopo i primi 16,45 s: RV1 contiene all'inizio le istruzioni di regia lette per errore** («…per studenti BES e DSA, dizione italiana cristallina, timbro luminoso…»). Nessuna voce nuova necessaria |
| 30:59 | voce | la scheda Caproni diceva «capace di svelare il senso ultimo dell'esistenza»; il prof dice «incapace» | voce RV2 (corretta, già sul ramo voci) al posto di AN2b |
| 47:17 | voce | scheda Fenoglio/Lampedusa/Ginzburg: «priva di **ascensioni** liriche» (il prof dice «accensioni») | voce RV3 (corretta) al posto di AN3b |
| 48:22 | voce | «**Donne** in guerra» (il titolo è «Donna in guerra») | voce RV4 (corretta) al posto di AN3c; a schermo «Donna in guerra» |
| 19:15–20:30, 33:45–35:15, 48:45–50:15, 51:00–52:00 | contenuto | **4 mappe concettuali inventate da noi** (una per argomento + finale) | tolte (insieme alle loro voci). Resta **solo la mappa del prof** (`MAPPE/LEZIONE 19.pdf`, una sola, per tutta la lezione), nella nostra grafica, con testi identici (maiuscolo del prof), letta dalla voce RV5 con evidenziazione a tempo, dopo il Quiz 3 |
| 21:30 e altri | visivo | transizione con macchia blu scura tra ripasso e argomento 2; schede animate su fondo scuro | sostituite da schede bianche e dissolvenza breve (0,3 s) tra ogni pezzo |
| 1290–1298, 2089–2092, 2145–2149, 2992–2995, 3052–3056 s | audio | 6 silenzi di 3,0–3,6 s tra schede | nessun silenzio > 2,5 s |
| 3191–3224 s | audio/struttura | 2 code silenziose di 8,3 e 8,9 s; slide «Fine»; schede Verifica finale e Compiti dentro il video | tolte; finale del kit (5 s) |
| fine | audio | picco −0,4 dBFS | limitatore: picco vero −1,4 dBFS |
| prof nelle schede | visivo | evidenziazione ferma sulla prima card all'inizio mentre il prof parlava in generale (es. 3:00–6:40 vecchio) | nessuna card in corso quando il prof non sta leggendo una card; card in corso agganciata alla prima parola della card letta dal prof (tempi dalla trascrizione, vedi §4) |
| `compiti.json` | dati | formato `compiti: [testi]` | formato `{"titolo", "esercizi":[{"n","tipo":"aperta","testo"}]}`; 4 compiti, testo identico a `LEZIONE 19.pdf` (controllato) |
| `scheda_pubblicazione.json` | dati | titolo «Dal secondo dopoguerra a oggi», secondi vecchi, `t_verifica`/`t_compiti` | titolo «Letteratura V · Lezione 19 · Dal secondo dopoguerra a oggi», secondi nuovi (vedi §5), tolti i campi delle schede esterne |
| Quiz 3 domanda 5 | quiz | «Che cosa unisce Dacia Maraini?» (poco chiara) | «Che cosa unisce Dacia Maraini nelle sue opere?» |
| `.vtt` | testo | 706 cue con errori di riconoscimento («dopo guerra», «statisolati», «sudannuzio», «Aldamerini»…) | rifatto da zero sull'originale: 455 cue ≤ 2 righe, tolti i frammenti senza senso (Uh, Mm, «Kill easy», «The name»…), corretti nomi propri (Alda Merini, Natalia Ginzburg, Tomasi di Lampedusa, Gattopardo, Fenoglio, Mani pulite, Dacia Maraini, Valduga, Cavalli) |

## 4. Verifica (che cosa ho fatto davvero)
- **A · Ascolto (M):** trascrizione completa con `trascrivi.py` (Parakeet) del video vecchio, dell'originale del prof (29:34) e di tutte le voci Kore (clip pulite). Cercati «ecco / guarda / in questa… / come vedete / vedete / questa slide»: «Ecco i punti da ricordare» (S1, S2) cade con lo schema sullo schermo; «Fermati un momento a guardare la mappa» (RV5) con la mappa; «lo vedete anche in slide» (prof, 17:04 orig.) con la card di Caproni. Nessuna frase della voce nomina immagini assenti. Silenzi: nessuno > 2,5 s. Frasi tagliate o ripetute nei pezzi del prof: nessuna (pezzi continui dall'originale).
- **Audio del prof (M/S):** rifatto dall'originale con la catena del kit (`aresample 48000, highpass 80, arnndn` con `sh.rnnn` del kit, `loudnorm −16`, `alimiter`). Le voci sono normalizzate a −16 LUFS ciascuna; jingle `quiz/titolo/repaso/trans` del kit negli stessi punti di Spagnolo (quiz a +0,5 s dalla scheda).
- **Fine e inizio di ogni pezzo del prof (M, regola 01:25):**

| Pezzo | Inizio nel video | Prime parole | Ultime 8 parole dette | Frase finita? |
|---|---|---|---|---|
| D0 | 0:44,2 | «Buongiorno e benvenuti alla lezione Dal secondo dopoguerra…» | «…c'è anche la parte di teatro. Bene, allora.» | **sì** |
| D1 | 2:51,5 | «Vediamo di dare delle coordinate storiche, ancora una…» | «…ruolo, come dico sempre, della persona è fondamentale.» | **sì** (prima: no) |
| D2 | 20:39,0 | «Quale tipo di poeta? quale tipo di letterato?» | «…vedete, la conformismo più totale, e Patrizia Valduga.» | **sì** (prima: no) |
| D3 | 33:59,7 | «I maestri della narrativa. C'è anche la narrativa,…» | «…costituiscono magari materiale già più. Come dire. D'esame.» | **sì** (fine dell'originale) |

  Gli inizi: ogni pezzo parte in una pausa (≥ 0,5 s prima della prima parola), nessuna parola mozzata.
- **B · Visione (M/S):** 1 fotogramma ogni 30 s (`controllo_minuti.jpg`, 100 fotogrammi) e fotogrammi mirati; la sincronia card–parlato è **dalla trascrizione**: ogni card si illumina sulla prima parola con cui il prof inizia a leggerla (tempi sull'originale, in secondi: quadro 335,4 / 346,6 / 359,3 / 393,8; bipolarismo 418,7 / 441,5 / 464,4; trasformazioni 513,4 / 551,4 / 609,4; media 659,4 / 702,4 / 725,4; dibattito 804,4 / 825,4 / 842,4; poesia 896,4 / 948,4 / 1027,4 / 1099,4; narrativa 1 1257,7 / 1297,4 / 1347,4; narrativa 2 1421,4 / 1486,4 / 1533,4; saggistica 1581,7 / 1628,7). La card **non** si illumina mentre il prof parla in generale. Negli approfondimenti, schemi, glossario e mappa lo stato cambia sull'inizio della frase della voce corrispondente (tempi dalla trascrizione di ogni voce). **(S: dopo il montaggio non ho rifatto un controllo indipendente su ogni cambio; ho guardato solo i fotogrammi del contact sheet.)**
- **C · Testo (M/S):** testi delle slide presi dalla dispensa (22 pagine lette per intero); le slide nuove le ho guardate a campione (copertina, 5 slide con il prof, 10 approfondimenti, schema, quiz, mappa, glossario, riepilogo): accenti e nomi controllati su quel campione (S), non su ogni stato. **PDF slide: 37 pagine.** 28 pagine sono state confrontate con il fotogramma corrispondente del video (scarto medio massimo 1,0/255, solo compressione): **coincidono**. Le altre 9 sono le slide con il prof (pagine 3–6, 16–17, 26–28): stesso codice di impaginazione delle slide del video, senza riquadro, fascia né card in corso (scelta voluta: in pagina nessuna evidenziazione). Controllate a vista nel contact sheet. **PDF mappe: 1 pagina.**
- **D · Dati (M):** `Test_Letteratura_Lez19.xlsx` = 10 domande, identiche a `DOMANDE LEZIONE 19.xlsx` del prof (controllato cella per cella). Quiz: 3×5 domande dal materiale del prof (una riga corretta); compiti = PDF del prof.

## 5. Tabella dei secondi (vecchio → nuovo)
| Elemento | Vecchio | Nuovo |
|---|---|---|
| Argomento 1 (inizio, T1) | 171,9 s | **167,9 s** |
| Quiz 1 | 1287,9 s | **1231,4 s** |
| Argomento 2 (inizio, T2) | 1292,9 s | **1235,4 s** |
| Quiz 2 | 2143,6 s | **2032,1 s** |
| Argomento 3 (inizio, T3) | 2148,6 s | **2036,1 s** |
| Quiz 3 | 3050,5 s | **2880,7 s** |
| Durata | 3224,1 s | **3009,5 s** |
(`inizio_s` in `scheda_pubblicazione.json` = inizio della scheda titolo − 0,35 s, come nella consegna precedente; la master rigenera la pagina.) Schede titolo T = 3,6 s con jingle titolo; schede Quiz Q = 4,0 s con jingle quiz a +0,5 s.

## 6. Pagine del libro (B-bis)
La lezione 19 **non ha pagine del libro** (è nell'elenco 4, 7, 10, 12, 15, 19–26): punto saltato come da regole. Nessuna tabella fettine.

## 7. Limiti e cose da sapere (da dire a Sara)
1. **Riquadro del prof:** l'originale è una registrazione dello schermo 1092×614 in cui il prof sta in un riquadro di **247×139 px**; il ritaglio 4:3 è 185×139 px ingrandito ×2,2: **più morbido del modello Spagnolo**, non si può fare meglio senza la sola webcam. **La testa tocca il bordo alto già nell'originale** (capelli) per tutta la lezione.
2. **Foto di Eco e Maraini:** nell'originale, a 27:56–29:35 (orig.), il prof mostra una slide con le due fotografie; non sono nei materiali che ho (manca il `_videodispensa.pptx` della lezione 19 nella release) e non uso foto prese altrove: nel video resta la slide con la card di Maraini. **Se Sara carica il pptx, si possono aggiungere.**
3. **Voce introduttiva RV1:** usata solo dopo il taglio dei primi 16,45 s (istruzioni di regia lette per errore). **Da riascoltare dalla master** (nella clip tagliata non compaiono né «BES/DSA» né istruzioni di regia; il nome del prof compare, correttamente, nella presentazione).
4. **Sottotitoli:** generati dalla trascrizione automatica sull'originale + correzione sistematica dei nomi: il prof parla in modo colloquiale e **alcune frasi restano approssimative** («la conformismo più totale» nella frase su Cavalli: parola riconosciuta male dal parlato, a schermo non compare). Da controllare a campione.
5. **Date da confermare col prof:** nessuna data dubbia trovata nelle slide.
6. Il confronto delle slide-PDF con i fotogrammi è automatico (§4 C); la lettura a vista di ogni slide **non** è fatta pagina per pagina da un secondo lettore.
7. Gli strumenti `finale_a_pezzi.py` / `controllo_finale.py` usano percorsi della macchina della master: non girano qui. Ho fatto la codifica a pezzi di 45 s (x264 veryfast CRF 19, un solo AAC 192k), unione senza ricomprimere; controlli equivalenti nelle tabelle (§1).

## Cosa NON ho verificato
- **Ascolto a orecchio** (fruscio, ronzio, «metallico», sincronia delle labbra a vista): non possibile qui; ho solo le misure di §1.
- La correttezza di **ogni** riga dei sottotitoli e di ogni slide letta a occhio da una seconda persona.
- La sincronia di **ogni** cambio card e il bordo di ogni schermata (nessun controllo indipendente dopo il montaggio).
- Le pronunce Kore dei nomi propri (ascolto non possibile): la trascrizione automatica delle voci riporta Mani pulite, Caproni, Merini, Lampedusa, Gattopardo, Fenoglio, Maraini correttamente; «Aracoeli» non compare in questa lezione.

## 8. File consegnati (cartella `revisione-letteratura-V-lez19/`)
`Letteratura_Lez19_Parte1_1080p.mp4.parte_00…03` + `.sha256`, `Letteratura_Lez19_Parte1.vtt`, `Letteratura_Lez19_slide.pdf` (A4 orizz., 37 pp.), `Letteratura_Lez19_mappe.pdf` (A4 orizz.), `quiz_argomenti.json`, `Quiz_Letteratura_Lez19.txt`, `Test_Letteratura_Lez19.xlsx`, `compiti.json`, `scheda_pubblicazione.json`, `testo_youtube.txt`, `timeline.json`, `controllo_minuti.jpg`, questo rapporto. **Voci nuove: nessuna** (RV1c, RV2, RV3, RV4, RV5 erano già sul ramo `voci-letteratura-V-lez19`).
