# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 1 · L'età del Naturalismo e del Decadentismo
Prof. Giorgio Mazzotti · revisione del 16–17/11/2026 · stato: **REVISIONATA** (la master la guarda prima di sostituire il video su Vimeo)
Video: `Letteratura_Lez1_Parte1_1080p.mp4` (a pezzi `.parte_00…`, sha256 nel file `.sha256`).
Etichette: **misurato** = misurato con uno strumento · **stima** = dedotto · **non verificato** = non ho potuto.

## 1. Misure sul video nuovo
| Controllo | Risultato |
|---|---|
| Formato | 1920×1080, 30 fps, x264 veryfast (CRF 19 schede, CRF 21 tratti col prof), AAC 192k 48 kHz — **misurato** |
| Durata / fotogrammi | 59:38,1 · 107342 fotogrammi = durata × 30 (vecchio: 63:53,8). **La durata è cambiata** (via le 6 mappe non del docente e le voci senza immagine): vedi tabella vecchio → nuovo in §6 — **misurato** |
| Peso | 239.8 MB (228.7 MiB) — **misurato** |
| Volume | parlato del docente −16,2 LUFS (mediana dei pezzi col docente); integrato −16,3 LUFS, LRA 6,0 LU — **misurato** |
| Picco | true peak **−1,4 dBTP** (obiettivo ≤ −1 dBTP) — **misurato** |
| Rumore del docente | originale: fondo −47,4 dBFS, parlato mediano −25,6 dBFS, **picco 1,000 (clipping)**; dopo la catena del kit: fondo −50,4 dBFS, parlato −20,9 dBFS, picco 0,803 — **misurato**. Ascolto a orecchio di fruscio/ronzio/«metallico»: **non fatto** (non verificato) |
| Fermi immagine del docente | nessun fermo ≥ 1 s nei 7 pezzi col docente (riquadro sempre con video vivo; copertina senza riquadro mentre parla la voce) — **misurato** (`freezedetect`, soglia 1 s, solo sui pezzi col docente) |
| Scatto dei Quiz (jingle) | 6 su 6 a 0,0 s (scarto +0,002 s) — **misurato** (`controllo_jingle.py`) |
| Altri jingoli del kit | `titolo.wav` ×6 (inizio titolo +0,5 s), `repaso.wav` ×6 (prima di ogni ripasso), `quiz.wav` ×6; `trans.wav` messa ai passaggi (approfondimenti, mappa, glossario, riepilogo) ma **non rilevabile** per correlazione perché sotto la voce (non verificato) — **misurato** (correlazione con `titolo.wav`, `repaso.wav`, `trans.wav`) |
| Sincronia audio/video del docente | audio: scarto 0,000 ± 0,0001 s su 21 punti (7 pezzi × 3, correlazione con l'originale); video: scarto ≤ 1 fotogramma (0,033 s) su 21 punti, nessun trend; massimo 0,033 s (< 0,04) — **misurato** |
| Sottotitoli | 952 blocchi, sovrapposti 0, oltre la fine 0, max 2 righe; attacco sulla voce entro 0,3 s: **68% di 22 verificabili** (il controllo chiede ≥ 80%): scarti senza trend (mediana ≈ 0), gli errori grandi coincidono con blocchi che iniziano dopo jingle/passaggi; **da guardare** — **misurato** |
| PDF | `…_slide.pdf`: **35 pagine** A4 orizzontale, senza riquadro e fascia; `…_mappe.pdf`: **1 pagina** — **misurato** |

## 2. Confronto col modello Spagnolo (punto 000)
| # | Punto | Esito |
|---|---|---|
| 1 | Sigla 15 s → dissolvenza → copertina | **corretto**: sigla del kit invariata; dissolvenza morbida (0,37 s) alla copertina bianca; nessun lampo |
| 2 | Copertina (logo, «LETTERATURA ITALIANA V · VIDEOLEZIONE», titolo, card ARGOMENTI su due colonne) | **corretto** (prima mancavano gli argomenti, il titolo restava fermo da 0:56 a 2:15). Durante la voce di benvenuto **nessun riquadro del docente** (prima immagine ferma); il riquadro entra quando il docente parla davvero |
| 3 | Slide: fondo bianco, «01 · ARGOMENTO», titolo + barretta, card | **corretto** |
| 4 | Piè di pagina + «Pagina N» | **corretto** (numerazione 1–35 uguale nel PDF) |
| 5 | Riquadro 4:3, ombra grigia, niente bordo | **corretto**: 412×310 px a x=1428, y=148, angoli r=18, ombra grigia morbida (prima 16:9 in banda blu). **Limite**: i capelli toccano il bordo alto già nell'originale (webcam 245×137 px, ingrandita ≈ 2,3×: immagine morbida) |
| 6 | Fascia gialla −3°, due righe | **corretto** (prima: nome piccolo bianco, illeggibile) |
| 7 | Slide senza prof | **corretto**; card **in corso: bordo giallo sottile, numero su pallino giallo, fondo bianco**; le altre bordo grigio chiaro; ombre grigie morbide ovunque (aggiornamento 01:30) |
| 8 | Font | Bricolage Grotesque 800, Figtree (etichette e piè **Figtree Bold**, DM Mono non usato) |
| 9 | Finale | `Sigla_finale_5s_con_avviso_diritti.mp4` (prima «GRAZIE PER L'ATTENZION» tagliato) |
| 10 | Struttura | sigla → presentazione → 6 argomenti (titolo, docente, approfondimento animato, [mappa del docente nel 5], ripasso con voce, quiz 5 domande) → glossario → riepilogo → finale; verifica e compiti dopo |
| 11 | PDF A4 | consegnati, §7 |

## 3. Problemi trovati e correzioni
Minuti del video **vecchio**, salvo indicato.
| Minuto | Tipo | Com'era | Correzione |
|---|---|---|---|
| tutto | visivo | grafica diversa dal modello | tutta la lezione rifatta nel modello (35 slide) |
| 0:17–2:15 | visivo | presentazione: solo la slide del titolo (come segnalato); poi slide avanti sul parlato | copertina con card ARGOMENTI; slide in sincronia (§5) |
| 0:17–0:55 | visivo | riquadro del docente **fermo** durante la voce di benvenuto | niente riquadro finché non parla il docente |
| 2:15 | audio | taglio dentro la frase «Siamo in letteratura» | tutti i tagli nelle pause (tabella §4) |
| 19:12 | audio | «Bene.» ripetuto (fine arg. 2 e inizio arg. 3) | un solo «Bene.» |
| 26:00 / 28:34 | audio | arg. 4 inizia 1,4 s prima, poi riparte a metà frase | taglio nella pausa |
| 44:17 / 46:50 | audio | fine arg. 5 tagliata a 0,4 s dalla fine della frase; arg. 6 riparte a metà frase | taglio nella pausa |
| 56:30 | video | 1,6 s oltre la fine dell'originale | fine = fine dell'originale |
| 36:00–62:30 | testo | «Bodlèr», «Splin», «dèndi», «boemièn» sulle schede e nel .vtt | Baudelaire, Spleen, dandy, bohémien ovunque |
| 9:00, 17:30, 45:00, 59:30 | visivo | titolo «MAPPA CONCETTUALE» tagliato | — |
| 8:49, 17:21, 26:57, 35:11, 57:55 e mappa finale | contenuto | 6 mappe **fatte da noi**, non del docente | **tolte** (decisione di Sara 17/11); voce e silenzi collegati tolti |
| 45:00 | contenuto | mappa di Baudelaire inventata | sostituita dalla **mappa del docente** (`MAPPE/LEZIONE 1.pdf`), con voce nuova R7 che la legge |
| 8:30 · 17:10 | audio | in fondo agli approfondimenti la voce dice «Ecco la mappa…» e passa alla mappa | tagliata prima di «Ecco la mappa» |
| 58:20 | audio | voce mappa finale saltava il primo ramo | scheda tolta con la mappa |
| 63:37 | visivo | «GRAZIE PER L'ATTENZION» tagliato | finale del kit |
| quiz, titoli, ripassi | audio | jingle del quiz e del titolo presenti, **mancavano** quelli di ripasso e le transizioni | `repaso.wav` prima di ogni ripasso, `trans.wav` ai passaggi, `titolo.wav` ai titoli, `quiz.wav` ai quiz (come Spagnolo) |
| .vtt | testo | 788 blocchi con errori («lettatura», «ben umale il metesimo», «le tà del naturalismo»…) | **rifatto** sulla trascrizione: 952 cue |
| 40:18–42:30 orig. | pagina | pagine del manuale piccole prese dal video | fettine HD (§4) |

## 4. Fine e inizio di ogni pezzo del docente (aggiornamento 01:25)
Misurato sulla trascrizione (tempi parola per parola). Ogni pezzo inizia e finisce **nelle pause**, tra una frase e l'altra; nessuna parola mozzata o ripetuta.
| Pezzo | Inizio (video) | Prime parole | Fine (video) | Ultime parole dette | Frase finita |
|---|---|---|---|---|---|
| D0 | 0:52 | «Buongiorno e benvenuti al corso di letteratura» (pausa prima: 0.0 s; parola non mozzata: sì) | 3:04 | «…di questi contenuti, quindi meno male ci siamo.» (pausa dopo: 0.54 s) | sì |
| D1 | 3:09 | «Il Regno d'Italia Lo ricordo, nacque ufficialmente» (pausa prima: 0.84 s; parola non mozzata: sì) | 7:55 | «…ottocento, soprattutto italiano. fino alle soglie del Novecento.» (pausa dopo: 0.61 s) | sì |
| D2 | 9:53 | «dobbiamo parlare però come vedete anche di» (pausa prima: 0.65 s; parola non mozzata: sì) | 15:30 | «…repubblicano-democratiche. Quindi lo schieramento un po' questo. Bene.» (pausa dopo: 0.53 s) | sì |
| D3 | 17:34 | «Ancora una volta, proviamo a... Ancora una» (pausa prima: 0.46 s; parola non mozzata: sì) | 24:17 | «…altri paesi europei. Quelli avanzati, chiaramente, quelli avanzati.» (pausa dopo: 1.22 s) | sì |
| D4 | 26:09 | «Dicevamo, storia della lingua, anche questo è» (pausa prima: 1.25 s; parola non mozzata: sì) | 31:45 | «…mirato, comprendendo tutte le parti. che ci interessano.» (pausa dopo: 0.14 s) | sì |
| D5 | 33:40 | «Ma adesso Per così dire, stacchiamo dalla» (pausa prima: 0.19 s; parola non mozzata: sì) | 41:20 | «…incarna e che lui incarna è Cochle Baudelaire.» (pausa dopo: 1.05 s) | sì |
| D6 | 43:47 | «E quindi, insomma, capite che i contenuti» (pausa prima: 1.09 s; parola non mozzata: sì) | 53:22 | «…e la prima lezione si può concludere qui.» (pausa dopo: 8999997471.0 s) | sì |

## 5. Pagine del libro e mappe
**Pagine HD** (`Lez01_ingrandita.1.zip`: p. 24, 26, 28, 30, 31). Taglio solo sulle righe bianche, solo la colonna del brano, senza intestazioni, numeri di pagina, QR, loghi. Fettina in corso con bordo giallo. Tempi = quelli in cui il docente cambia pagina (rilevati nell'originale, misurato).
| Brano | Pagina | File HD | Minuto (video nuovo) |
|---|---|---|---|
| Corrispondenze (da I fiori del male) | 24 | Lez01_p024.png · fettina 1 | 51:43–51:50 |
| Corrispondenze (da I fiori del male) | 24 | Lez01_p024.png · fettina 2 | 51:50–51:57 |
| L'albatro | 26 | Lez01_p026.png · fettina 1 | 51:57–51:58 |
| Spleen | 28 | Lez01_p028.png · fettina 1 | 51:58–51:59 |
| Perdita d'aureola (Lo spleen di Parigi) | 30 | Lez01_p030.png · fettina 1 | 51:59–52:01 |
| Perdita d'aureola (testo) | 31 | Lez01_p031.png · fettina 1 | 52:01–52:04 |
| Spleen | 28 | Lez01_p028.png · fettina 1 | 52:04–52:05 |
| Perdita d'aureola (testo) | 31 | Lez01_p031.png · fettina 1 | 52:05–52:40 |

Il docente non legge i versi: mostra le pagine alla fine («trovate i testi, li ho aggiunti in slide»). Rigo più piccolo: prosa di p. 31, interlinea ≈ 34 px a 1080p. Foglio di controllo: `controllo_fettine.jpg`.
**Mappa.** `MAPPE/LEZIONE 1.pdf` ha **una sola pagina, su Baudelaire**. Impaginata senza cambiare né togliere nessun nodo (nel PDF c'erano il logo di un sito e una fotografia: non riportati). Per gli altri argomenti il docente non ha mandato mappe: non ce ne sono nel video.
**Sincronia delle evidenziazioni:** card accesa quando il docente comincia a parlarne (parola chiave nella trascrizione); ripassi/approfondimenti sull'inizio delle frasi della voce. Scarto atteso ±1 s (**stima**).

## 6. Tabella vecchio → nuovo (secondi)
Serve alla master per rigenerare la pagina. Aggiornati `scheda_pubblicazione.json` (`inizio_s`, `quiz_s`, `durata_s`) e `timeline.json`.
| Punto | Vecchio | Nuovo |
|---|---|---|
| Quiz 1 | 632.7 | 585.3 |
| Quiz 2 | 1142.6 | 1048.3 |
| Quiz 3 | 1704.0 | 1564.8 |
| Quiz 4 | 2191.0 | 2017.5 |
| Quiz 5 | 2799.9 | 2628.9 |
| Quiz 6 | 3550.4 | 3330.6 |
| Verifica finale | 3808.7 | 3553.0 |
| Compiti | 3821.9 | 3566.2 |
| Durata totale | 3833.8 | 3578.1 |

## 7. PDF e consegne
- `…_slide.pdf`: 35 pagine, generate dallo stesso HTML delle slide del video; confronto con 15 fotogrammi del video: tutti uguali (scarto medio ≈ 2/255 = compressione) sulle 15 pagine senza docente; le 20 pagine col docente sono la stessa grafica senza riquadro e fascia (non confrontate a una a una).
- `verifica_finale.json` + `.xlsx`: le **10 domande del docente** (`DOMANDE LEZIONE 1.xlsx`). `compiti.json`: **4 esercizi** del docente (`LEZIONE 1.pdf`). `quiz_argomenti.json`, `Quiz_Letteratura_Lez1.txt`, `scheda_pubblicazione.json` (titolo «Letteratura V · Lezione 1 · L'età del Naturalismo e del Decadentismo»), `testo_youtube.txt`, `timeline.json`.

## 8. Cosa NON ho verificato
Ascolto del rumore (fruscio, ronzio, «metallico»); sottotitoli riletti ascoltando (sono la trascrizione con ≈ 90 correzioni: restano frasi del docente rese male: «I fiori del mare… del male» (≈ 31:12 orig.), «Dogali/Adua» (≈ 5:41), «Podler/Baudelaire» e nomi propri nelle spiegazioni a braccio); pronuncia delle voci Kore GL/S/RF (solo trascritte); OCR su tutti i fotogrammi (verificate le immagini delle slide, non i 107342 fotogrammi); funzionamento dei file sulla pagina interattiva.

## 9. DA CONFERMARE COL PROF / SARA
1. Mappa del docente: «le persone sono **miseri** e tristi» riportato identico.
2. Il docente dice «I fiori del **mare**… del male» (≈ 31:12 orig.): lapsus, nei sottotitoli «I fiori del male».
3. Il docente dice «1887/1896: Dogali e Adua»; Adua è del 1896, Dogali del 1887: nei sottotitoli «Adua, 1896» come dice dopo.
4. Voci Kore di S, GL, RF non riascoltate: controllare a orecchio.

## 10. Tempi
Primo rapporto: 01:00 italiane (16–17/11). Consegna: 09:30 (ora italiana).
