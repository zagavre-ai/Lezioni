# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 11 · «Il Futurismo e le avanguardie»
**Correzioni 22/11/2026** (sopra la consegna del 17/11). Ramo `revisione-letteratura-V-lez11`. Misurato (M) / stima o lettura a vista (S) / non verificato (NV).

## 1. Numeri sul video finale (M)
| | Valore |
|---|---|
| Durata | **52:57** (3177,27 s), una sola Parte |
| Fotogrammi | **95.318 = durata × 30** |
| Peso | 258,7 MB (< 400) · 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192k 48 kHz |
| Volume | **−15,8 LUFS** integrati (parlato del prof a −16 LUFS ±1); picco vero **−1,6 dBTP** (rimisurati sul file finale) |
| Timbro della voce del prof | rapporto acuti(>4 kHz)/(>100 Hz): originale −16,1 dB · pulito −15,7 dB · video finale −15,5 dB (limite −9…−20: **OK**) |
| Pause > 2,5 s | **0** (`silencedetect` −45 dB, d ≥ 2,5 s) |
| Scatto quiz | **−0,009 / −0,009 / −0,009 / −0,010 s** (limite 0,05) |
| Sincronia labbra/voce (audio finale ↔ originale, 3 punti per pezzo) | **−0,01 s** su tutti i 12 punti nella build precedente; dopo l'ultima ricodifica (audio e video del prof identici, cambiano solo card e dissolvenze) ricontrollato D1 = −0,01 s; D2–D4 non ancora rimisurati (NV) |
| Fermi immagine nel riquadro del prof (`freezedetect` −60 dB, ≥ 1 s) | **0** |
| Controllo severo della master (`controllo_severo.py`) | **IN CORSO al momento della consegna** (lanciato alle 19:09 UTC sul file finale, passo 20 s): l'OCR non era ancora finito. Esito da aggiungere con un commit dopo la consegna; nella build precedente le uniche cose segnalate dall'agente indipendente sono quelle della §7, già corrette |

## 2. Cosa ho cambiato in questa tornata
1. **Testo a 40 px** (mai sotto 36), interlinea 1,5, in tutte le card; **al massimo 3 card per slide, ogni card una frase intera**, alta quanto il testo (misurata col font vero). Quando 3 card non entrano la slide si divide (da 64 a 99 pagine). Nessuna card resta sola per oltre 60 s (M).
2. **Copertina**: il prof sopra la copertina parla per 150 s (< 3 min), poi slide «Di cosa parliamo» con i 4 argomenti, che si accendono quando il prof li nomina. L'introduzione animata (voce di benvenuto) **non ha il riquadro del prof, nemmeno vuoto**.
3. **Nessuna schermata identica oltre 3 minuti** (M, dalla composizione delle scene): il fotogramma identico più lungo è la copertina con il prof (150 s); la stessa slide con evidenziazione che cambia al massimo 150,6 s (D1, «Un'arte nuova»); nessuna card sola oltre 45 s fuori dalla copertina.
4. **Una sola mappa, quella del prof** (`MAPPE/LEZIONE 11.pdf`, 1 sola mappa sul Futurismo), **ridisegnata nel modello BES approvato** (stesse parole, stessa struttura a 5 rami): 5 colori con legenda in alto a destra, testo 34–50 px, **costruita ramo per ramo** mentre la voce Kore la legge (box in giallo finché parla), poi la mappa intera resta ferma 4 s. Posta alla fine dell'argomento 2, prima della pillola, **una volta sola**. L'originale non ha marchio di mappe-scuola né foto dell'autore: nessun marchio da togliere. Assegnazione dei colori (mia, S): pesca = concetto centrale; celeste = Marinetti e il manifesto (origine); paglierino = parole chiave (Paroliberismo, Esaltava, «Scrivono eliminando…»); menta = esempi (punteggiatura/infinito, modernità, coraggio, guerra, esponenti); lilla = conseguenze (volevano distruggere il passato; polemici sulla donna). Le due mappe inventate da noi sono già tolte dal 17/11.
5. **Schede blu scuro** (titolo argomento, pillola di ripasso, quiz, verifica, riepilogo, compiti) come Spagnolo; le righe della pillola e del riepilogo si accendono con la voce.
6. **Verifica di sbarramento e compiti dentro il video**: scheda «Verifica finale» (10 domande, soglia 80%), sigla finale del kit con avviso diritti, intro «Compiti» con jingle e i 4 compiti del prof (testo identico al suo PDF) letti dalla voce Kore (CP1–CP4), una card per volta.
7. **Pausa del prof > 2,5 s accorciata**: una sola, orig. 1571,9–1574,7 (2,75 s) → 1 s, tra due frasi, con la slide che non cambia (taglio sia nel video che nell'audio del prof).
8. **Card riallineate al parlato** (bordo giallo all'inizio della frase): ho confrontato ogni card con la trascrizione e spostato le 5 che erano fuori oltre 1 s e ben identificabili (D1 p.2 card 1, D1 p.4 card 2, D2 p.11 card 3, D4 p.22 card 2, D4 p.24 card 1).
9. **Nome del docente mai detto né scritto nelle animazioni**: tolto dal piè di pagina di tutte le slide senza il prof e dalla voce di benvenuto (nuova voce **INTRO2**: «Il professore ci guida…»). Resta solo nella fascia gialla e nel piè di pagina delle slide col prof.
10. **Dispensa A4 e PDF mappe rifatti** (§5).
11. File rigenerati sul video finale: `.vtt`, `timeline.json`, `scheda_pubblicazione.json` (titolo «Letteratura V · Lezione 11 · Il Futurismo e le avanguardie»), `quiz_argomenti.json` (con `inizio_s`), `verifica_finale.json` (10 domande dall'Excel del prof, con `inizio_s`).
Mantenuti: trascrizione, tagli del prof, fettine HD del libro (9, già approvate), sigla, voci Kore, quiz, compiti, jingle del kit, transizioni (dissolvenza + `trans.wav` in uscita dai pezzi del prof), audio del prof pulito (highpass 80, rnnoise, loudnorm −16, alimiter).

## 3. Secondi vecchio → nuovo (la pagina Vimeo va rigenerata)
| Elemento | consegna 17/11 (s) | consegna 22/11 (s) |
|---|---|---|
| T1 | 46.3 (0:46) | 43.4 (0:43) |
| D1 | 49.2 (0:49) | 46.3 (0:46) |
| Q1 | 1029.4 (17:09) | 1026.5 (17:06) |
| T2 | 1034.3 (17:14) | 1030.7 (17:10) |
| D2 | 1037.2 (17:17) | 1033.6 (17:13) |
| Q2 | 1828.8 (30:28) | 1829.2 (30:29) |
| T3 | 1833.7 (30:33) | 1833.4 (30:33) |
| D3 | 1836.6 (30:36) | 1836.3 (30:36) |
| Q3 | 2511.9 (41:51) | 2509.9 (41:49) |
| T4 | 2516.8 (41:56) | 2514.1 (41:54) |
| D4 | 2519.7 (41:59) | 2517.0 (41:56) |
| Q4 | 3017.7 (50:17) | 3015.0 (50:14) |
| GL1 | 3022.6 (50:22) | 3019.2 (50:19) |
| RF1 | 3064.4 (51:04) | 3060.9 (51:00) |
| VF | — | 3095.6 (51:35) |
| SIGF | 3099.0 (51:38) | 3099.1 (51:39) |
| CMPI | — | 3104.1 (51:44) |
| CMP | — | 3107.6 (51:47) |
| Durata totale | 3104,0 | 3177.3 |

## 4. Mai il prof tagliato a metà frase (M, su trascrizione dell'originale pulito)
| Pezzo | Inizio (orig. s) | Prime parole | Fine (orig. s) | Ultime parole | Frase intera |
|---|---|---|---|---|---|
| D1 | 0,0 | «Buongiorno e benvenuti alla lezione sul Futurismo» | 721,9 | «…chiedono il Futurismo italiano, d'accordo?» | sì |
| D2 | 721,9 | «il Futurismo di Marinetti. Noi dobbiamo affrontare…» | 1201,9 | «…agli occhi della società borghese, quella che produce.» | sì |
| D3 | 1203,0 | «però sempre più… In Marinetti, questo è Palazzeschi…» | 1648,15 | «…ecco questo a seconda del programma, va bene.» | sì |
| D4 | 1648,15 | «chiudiamo con altre esperienze sempre d'avanguardia…» | 1984,0 | «…segnerà l'inizio della letteratura.» | sì (fine originale) |
I tagli cadono nelle pause (0,15 s o più prima della frase che segue); le dissolvenze tra pezzi cadono nel silenzio.

## 5. Dispensa e PDF mappe
- `Letteratura_Lez11_slide.pdf`: A4 orizzontale, **99 pagine** = le slide del video (una per slide, stato finale, senza riquadro, fascia e nome del docente), **testo vero e selezionabile** (PDF vettoriale: `pdftotext` lo legge; nessuno strato invisibile necessario), testo a 40 px come il video. Copertina con **solo materia e titolo**; piè di pagina «LETTERATURA ITALIANA V» + pagina, **senza nome del docente**. Confronto di tutte le 99 pagine con il fotogramma corrispondente: **scarto medio massimo 2,0/255** (M).
- `Letteratura_Lez11_mappe.pdf`: copertina identica con la scritta **MAPPE**, poi la mappa del prof nel modello BES (colori e legenda).

## 6. Voci (M/NV)
Nuove voci Kore generate dalla master: MPD1 (mappa), INTRO2 (benvenuto senza nome), CP1–CP4 (compiti). Tutte trascritte con `trascrivi.py` e confrontate con il testo: parole e numeri coincidono (gli anni sono scritti in lettere nel testo: «millenovecentonove»); **bordi**: ampiezza negli ultimi 50 ms tra 0,0006 e 0,0021 (< 0,03); dissolvenza 20–40 ms. Nomi propri letti correttamente nelle trascrizioni (Marinetti, Palazzeschi, Govoni, Joyce, Molly). **NV**: non ho ascoltato a orecchio le voci (ho solo la trascrizione automatica).

## 7. Verifica indipendente (§11)
Un agente separato (che non ha montato la lezione) ha controllato il video e la dispensa sull'elenco del §11 (campionando fotogrammi, trascrizione, OCR su 139 fotogrammi, PDF). Esito e che cosa ho fatto:
| Punto | Esito dell'agente | Azione |
|---|---|---|
| Introduzione/copertina ≤ 3 min, nessun riquadro nell'intro animata | OK (copertina col prof 150,7 s; nessun riquadro nemmeno vuoto) | – |
| Max 3 card per slide | NO: «Gli argomenti di oggi» e il riepilogo avevano 4 card | **Corretto**: «Di cosa parliamo» ora in 2 slide da 2 card; riepilogo in 2 slide |
| Card intere, 40 px | OK (passo riga 60 px) | – |
| Nessuna schermata identica > 3 min | OK (max 150 s) | – |
| Nessuna card sola > 60 s | NO sulle fettine del Manifesto (91 s e 67 s): sono fettine del libro, una alla volta a tempo con la voce (approvate dalla master) | Lasciate; segnalo |
| Bordo giallo a inizio frase (20 punti) | 14/20 entro ±1 s; fuori: D1 4:53, D1 10:49, D2 22:55, D4 43:35, D4 43:52, D2 18:16 | **Corretti i 5 con scarto misurato** (card anticipate di 14,0 / 1,0 / 1,6 / 2,2 / 2,2 s); D2 18:16 («La prima avanguardia italiana…») non ha una frase corrispondente nella trascrizione: lasciata, da riascoltare |
| Prof mai tagliato a metà frase | OK; dubbi: giunzioni D1/D2 («…d'accordo? Uh see, so») e D3 (inizia con «però sempre più») | Il «so» è un'esitazione trascritta dal riconoscimento: da riascoltare (NV) |
| Nome del docente nelle animazioni | OK (OCR: 0 occorrenze; voce INTRO2 senza nome) | – |
| Mappa del prof | parole identiche all'originale; struttura ad albero invece che radiale | Lasciata (stessi rami e stesse parole; colori BES); segnalo |
| Quiz e verifica | domande giuste; `verifica_finale.json` = Excel del prof; nel video solo le schede (le domande sono nel player) | – |
| Dispensa/PDF | OK (testo selezionabile, niente nome del docente, pagine = fotogrammi). Copertina dispensa senza card «ARGOMENTI» (come da §9: solo materia e titolo) | **Aggiunta la scritta MAPPE grande** nella copertina dei PDF mappe |
| Transizioni | dissolvenze bianco↔blu di 0,17 s e VF→sigla finale a taglio secco | **Corretto**: dissolvenze di 10 fotogrammi (0,33 s) in tutto il video, dissolvenza a nero da VF al finale e dal finale a «Compiti» |
| Ordine apertura | scheda «Argomento 1» prima dell'introduzione del prof | Lasciata (la scheda titolo precede sempre l'argomento; il pezzo del prof non si spezza) |


## 8. Refusi e anomalie nel materiale del prof
Nessun refuso da correggere oltre alla doppia punteggiatura «divertire!.» (→ «divertire!»). Nessun numero che non torni. Nella voce del prof (non toccata) compaiono errori di dizione tipici del parlato: restano come li dice lui.

## 9. Cosa NON ho verificato
Ascolto a orecchio (fruscio, ronzio, metallico, labbra); i sottotitoli frase per frase (trascrizione automatica con correzione di nomi e termini; circa 15 frammenti senza senso tolti); l'accensione giallo/frase su ogni singolo cambio (verificati 20 punti con la trascrizione, ±1 s); riquadro del prof: la sorgente è la webcam in miniatura dello schermo registrato (247×138 px), quindi il 4:3 è morbido e la testa è al limite alto dell'inquadratura già nell'originale.

## 10. File consegnati
Video a pezzi da 90 MB + `.sha256`, `.vtt`, `timeline.json`, `scheda_pubblicazione.json`, `quiz_argomenti.json`, `verifica_finale.json`, `Quiz_Letteratura_Lez11.txt`, `Test_Letteratura_Lez11.xlsx`, `compiti.json`, `testo_youtube.txt`, `Letteratura_Lez11_slide.pdf`, `Letteratura_Lez11_mappe.pdf`, `controllo_minuti.jpg`, `controllo_fettine.jpg`, questo rapporto. Voci nuove sul ramo `voci-letteratura-V-lez11`.
