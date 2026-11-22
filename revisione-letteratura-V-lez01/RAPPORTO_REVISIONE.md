# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 1 · L'età del Naturalismo e del Decadentismo
Correzioni del 22/11/2026 (prima consegna 16–17/11) · stato: **REVISIONATA, «correzioni 22/11 fatte»** · durata misurata 59:19,4
Video: `Letteratura_Lez1_Parte1_1080p.mp4` (a pezzi `.parte_00…`, sha256 nel file `.sha256`).
Etichette: **misurato** = con uno strumento · **stima** = dedotto · **non verificato** = non ho potuto.

## 1. Cosa ho cambiato il 22/11
- **Testo delle slide a 40 px** (interlinea 1,5) in tutte le slide del docente, approfondimenti, ripassi, glossario, riepilogo; mai sotto. Dove tre card non entrano la slide si divide. Titoli, etichette e piè come prima.
- **Al massimo 3 card per slide, ogni card una frase intera** (iniziale maiuscola, niente «…»); le frasi lunghe delle slide del docente sono state spezzate **al punto** (es. «Economia e divario Nord-Sud…» / «La successiva svolta protezionistica…»), parole identiche. Le card sono nell'ordine in cui il docente le dice (nell'argomento 1 «Politica estera» viene detta prima di «L'involuzione di fine secolo»; nel 3 «L'editoria» prima di «Scuola»).
- **Nessuna slide ferma oltre 3 minuti**: ogni pagina dura al massimo ≈ 2,7 minuti (numero di pagina diverso); dove il docente parla a lungo prima della prima card (argomenti 2 e 5) c'è una slide «In questo argomento» invece della card sola. Bordo giallo all'inizio della frase (±1 s, **stima** dai tempi della trascrizione).
- **Una sola mappa, quella del docente** (`MAPPE/LEZIONE 1.pdf`, su Baudelaire), ridisegnata nel modello BES approvato: 12 riquadri, colori del disciplinare con legenda in alto a destra (pesca = concetto centrale, celeste = date, paglierino = parole chiave, menta = opere ed esempi, lilla = conseguenze), testo 35–50 px, frecce blu notte, costruita **ramo per ramo** con la voce Kore (`R10`), riquadro in giallo finché la voce parla, mappa intera ferma 4 secondi. Sta alla fine dell'argomento 5 (prima del ripasso), una volta sola. **Ridisegnata senza il marchio di mappe-scuola.com e senza la fotografia** (decisione di Sara). Le parole sono del docente ma **condensate** per stare in 12 riquadri a 35–50 px (come nel modello Gadda): nel riquadro del Realismo non ci sono «le persone sono miseri e tristi» (refuso del docente: accordo) e «Parigi di quell'epoca». Nel PDF `…_mappe.pdf` c'è la stessa mappa.
- Le 6 mappe nostre sono già state tolte il 17/11.
- Copertina: titolo esatto «L'età del Naturalismo e del Decadentismo»; la copertina compare per 167 s (introduzione animata senza riquadro del docente + il docente che si presenta, 2:12): sotto i 180 s.
- **Dispensa A4 slide e PDF mappe** rifatti identici al video, **con strato di testo invisibile** (selezionabile e leggibile dalla sintesi vocale); copertina solo con materia e titolo (per le mappe in più «MAPPE»), piè di pagina solo con la materia e il numero di pagina, niente nome del docente.
- Sottotitoli, `timeline.json`, `scheda_pubblicazione.json`, `quiz_argomenti.json`, `verifica_finale.json`, `compiti.json` rigenerati sul video finale con i secondi nuovi.

## 1-bis. Controllo di un agente separato (22/11) e correzioni
Un agente che non ha montato la lezione ha controllato la lista del §11 e ha trovato i difetti sotto: **corretti** salvo dove scritto.
| Difetto trovato | Correzione |
|---|---|
| Il nome del docente era detto e sottotitolato nella voce di benvenuto | voce rifatta (`R11`), nome tolto anche dal sottotitolo |
| 23 silenzi ≥ 3 s e schede titolo/quiz/verifica/compiti mute | schede titolo 3,4 s con `titolo.wav`, quiz 3,6 s con `quiz.wav`, verifica e compiti con `titolo.wav`; code delle voci accorciate; nessun silenzio oltre 2,5 s (max 2,43 s) |
| Due pagine identiche per oltre 3 minuti (argomenti 3 e 5) | pagine ricomposte (ordine card diverso, bordo giallo che cambia): nessuna schermata uguale oltre 3 minuti |
| Evidenziazioni fuori ±1 s (1ª, 2ª card dell'arg. 1, 4ª card, «I fiori del male») | tempi corretti (134,0 · 219,0 · 358,1 · 1873,5 s dell'originale) |
| Sigla di 17,9 s | sigla del kit di 15,0 s |
| Falsa partenza del docente ripetuta all'inizio dell'argomento 3 («Ancora una volta, proviamo a…») | tolta (2,45 s, in pausa) |
| Intercalari («eh», «ehm») nei sottotitoli | tolti |
| Finale senza dissolvenza | dissolvenza verso il bianco |
| Quiz/verifica/compiti non mostrano le domande nel video | **non cambiato**: le schede sono le stesse di Spagnolo, le domande le mostra la pagina interattiva (file `quiz_argomenti.json`, `verifica_finale.json`, `compiti.json`) |
| Pagine del manuale in carattere con grazie e a cambio rapido (52:40) | **non cambiato**: sono le pagine del libro del docente e cambiano quando le cambia lui (1–2,9 s); un solo pagina alla volta, nessun lampo |
| Verifica finale: «rifiuto … contro la cultura borghese» ha come giusto Giosuè Carducci mentre la slide dice che il rifiuto estetizzante è del Decadentismo | domanda del docente (`DOMANDE LEZIONE 1.xlsx`), **non modificata**: da confermare col prof |

## 2. Esito del controllo severo (`controllo_severo.py`, 22/11)
**ESITO: OK, zero errori** (`controllo_severo.py`, passo 15 s, 238 fotogrammi): copertina trovata e titolo intero («L'età del Naturalismo e del Decadentismo»), copertina 165 s (< 180); nessuna slide con lo stesso titolo/pagina oltre 3 min; nessuna schermata identica oltre 3 min; nessun «…»; nessuna card con iniziale minuscola; nessuna card sola oltre 60 s; loudness −16,4 LUFS; pause oltre 2,5 s: 0; durata 59,3 min; voce: tono 145–168 Hz e chiarezza 1244–1510 Hz sui 6 campioni (voce non alterata). Il controllo usa un OCR di sostituzione (tesseract non installabile: `apt-get` non lo trova): ho verificato a parte che legge i numeri di pagina (con una prima versione dell'OCR che non leggeva le cifre singole il controllo segnalava due falsi allarmi sul titolo; corretto lo strumento, non il video). File: `controllo_severo.json`.

## 3. Misure sul video finale
| Controllo | Risultato |
|---|---|
| Formato | 1920×1080, 30 fps, x264 veryfast (CRF 19 schede, CRF 21 tratti col docente), AAC 192k 48 kHz — misurato |
| Durata / fotogrammi | 59:19,4 · 106781 fotogrammi = durata × 30 — misurato |
| Peso | 235.6 MB — misurato |
| Volume | parlato del docente −16,2 LUFS; integrato −16,4 LUFS; picco −1,4 dBTP — misurato |
| Timbro della voce del docente | rapporto energia sopra 4 kHz / sopra 100 Hz, originale vs dopo la pulizia: −15,5/−15,6, −17,3/−17,5, −19,0/−16,9, −10,9/−11,4, −17,1/−17,4, −12,7/−12,8, −17,4/−19,0 dB (7 punti): sempre tra −9 e −20 dB, il timbro non è cambiato — misurato |
| Fermi immagine del docente | nessun fermo ≥ 0,7 s nel riquadro del docente in nessuno dei 7 pezzi (freezedetect sul ritaglio del riquadro) — misurato |
| Scatto dei Quiz | 6 su 6 a +0,5 s dall'inizio della scheda, scarto −0,015 s (limite 0,05); jingle titolo ×6, ripasso ×6, titolo anche sulle schede «Verifica» e «Compiti» — misurato |
| Sincronia labbra/voce | audio: scarto 0,0001 s su 21 punti (correlazione con l'originale); video: ≤ 1 fotogramma (0,033 s), nessun trend; massimo audio+video 0,033 s — misurato |
| Pause > 2,5 s | silenzi sotto −45 dB più lunghi di 2 s: 4 (52,8 s, 587,1 s, 3548,2 s, 3557,2 s), il più lungo 2,43 s: nessuna pausa oltre 2,5 s — misurato |
| Sottotitoli | 960 cue, max 2 righe, nessuna sovrapposizione; intercalari («eh», «ehm») e nome del docente tolti; nomi corretti (Baudelaire, Spleen, D'Annunzio) — misurato |
| PDF | dispensa 63 pagine A4 orizzontale con testo invisibile selezionabile (pdftotext); mappe 2 pagine (copertina «MAPPE» + mappa) — misurato |

## 4. Pezzi del docente: inizio e fine (frase intera sì/no)
| Pezzo | Inizio (video) | Prime parole | Fine (video) | Ultime parole dette | Frase finita |
|---|---|---|---|---|---|
| D0 | 0:54 | «Buongiorno e benvenuti al corso di letteratura» (pausa prima: 0.0 s; parola non mozzata: sì) | 3:06 | «…di questi contenuti, quindi meno male ci siamo.» (pausa dopo: 0.54 s) | sì |
| D1 | 3:09 | «Il Regno d'Italia Lo ricordo, nacque ufficialmente» (pausa prima: 0.84 s; parola non mozzata: sì) | 7:55 | «…ottocento, soprattutto italiano. fino alle soglie del Novecento.» (pausa dopo: 0.61 s) | sì |
| D2 | 9:48 | «dobbiamo parlare però come vedete anche di» (pausa prima: 0.65 s; parola non mozzata: sì) | 15:25 | «…repubblicano-democratiche. Quindi lo schieramento un po' questo. Bene.» (pausa dopo: 0.53 s) | sì |
| D3 | 17:24 | «Ancora una volta a parlare di storie,» (pausa prima: 0.16 s; parola non mozzata: sì) | 24:04 | «…altri paesi europei. Quelli avanzati, chiaramente, quelli avanzati.» (pausa dopo: 1.2 s) | sì |
| D4 | 25:51 | «Dicevamo, storia della lingua, anche questo è» (pausa prima: 1.25 s; parola non mozzata: sì) | 31:27 | «…mirato, comprendendo tutte le parti. che ci interessano.» (pausa dopo: 0.14 s) | sì |
| D5 | 33:16 | «Ma adesso Per così dire, stacchiamo dalla» (pausa prima: 0.19 s; parola non mozzata: sì) | 40:56 | «…incarna e che lui incarna è Cochle Baudelaire.» (pausa dopo: 1.05 s) | sì |
| D6 | 44:10 | «E quindi, insomma, capite che i contenuti» (pausa prima: 1.09 s; parola non mozzata: sì) | 53:44 | «…e la prima lezione si può concludere qui.» (pausa dopo: 8999997471.0 s) | sì |

Tutti i tagli cadono nelle pause tra due frasi. **Pause lunghe:** l'unica pausa del docente oltre 2,5 s in mezzo a una frase (≈ 17:04, «…come link. [3,9 s] lista del corso») non sta sotto −45 dB (rumore di fondo) e non l'ho accorciata: se la master vuole accorciarla va fatto con un taglio del video del docente.

## 5. Voci Kore: confronto trascrizione ↔ schermo
Le card sullo schermo sono più brevi di quello che dice la voce (rapporto parole uguali 0,6–0,94: la voce spiega, la card riassume con le stesse parole). Ogni voce è stata trascritta e confrontata con il testo sullo schermo (rapporto parole uguali; numeri e anni **identici** in tutte).
| Voce | Parole uguali | Numeri uguali |
|---|---|---|
| AP1 | 0.88 | sì |
| S1 | 0.93 | sì |
| AP2 | 0.6 | sì |
| S2 | 0.91 | sì |
| AP3 | 0.73 | sì |
| S3 | 0.92 | sì |
| AP4 | 0.77 | sì (nella prima trascrizione la frase era tagliata a «settant…»; sul file intero `AP4a.wav` la voce dice «settantotto per cento») |
| S4 | 0.94 | sì |
| AP5 | 0.76 | sì |
| S5 | 0.82 | sì |
| AP6 | 0.79 | sì |
| S6 | 0.88 | sì |
| GL | 0.78 | sì |
| RF | 0.92 | sì |
| R11 (benvenuto) | trascritta: nessun nome del docente; «Charles Baudelaire» detto | — |
| R10 (mappa) | trascritta riga per riga: 19 segmenti, testo uguale riga per riga, anni 1821·1845·1848·1857·1867 giusti | sì |
Bordi delle voci: ho applicato 30 ms di dissolvenza a ogni voce nel montaggio. Sui file di origine alcune voci hanno ampiezza oltre 0,03 negli ultimi 50 ms (AP1a, AP6a, S1, S2, R1): la dissolvenza copre il punto. Pronuncia: «Baudelaire» scritto come si pronuncia nel testo voce (Bodlèr); R10 trascritta: «Quarto ramo» riconosciuto male dal riconoscimento («Toro le opere»), ma la durata è giusta: **non verificato a orecchio**.

## 6. Pagine del libro (fettine HD) e fonti
| Brano | Pagina | File HD | Minuto |
|---|---|---|---|
| Corrispondenze (da I fiori del male) | 24 | Lez01_p024.png · fettina 1 | 51:54–52:01 |
| Corrispondenze (da I fiori del male) | 24 | Lez01_p024.png · fettina 2 | 52:01–52:08 |
| L'albatro | 26 | Lez01_p026.png · fettina 1 | 52:08–52:09 |
| Spleen | 28 | Lez01_p028.png · fettina 1 | 52:09–52:11 |
| Perdita d'aureola (Lo spleen di Parigi) | 30 | Lez01_p030.png · fettina 1 | 52:11–52:12 |
| Perdita d'aureola (testo) | 31 | Lez01_p031.png · fettina 1 | 52:12–52:15 |
| Spleen | 28 | Lez01_p028.png · fettina 1 | 52:15–52:16 |
| Perdita d'aureola (testo) | 31 | Lez01_p031.png · fettina 1 | 52:16–52:51 |

Pagine dal file `Lez01_ingrandita.1.zip` (p. 24, 26, 28, 30, 31), taglio su righe bianche, solo la colonna del brano; foglio `controllo_fettine.jpg`.

## 7. Tabella vecchio → nuovo (secondi)
| Punto | Prima del 22/11 (consegna 17/11) | Ora |
|---|---|---|
| Quiz 1 | 632.7 | 581.6 |
| Quiz 2 | 1142.6 | 1037.3 |
| Quiz 3 | 1704.0 | 1544.5 |
| Quiz 4 | 2191.0 | 1989.7 |
| Quiz 5 | 2799.9 | 2643.9 |
| Quiz 6 | 3550.4 | 3337.7 |
| Verifica finale | 3808.7 | 3546.4 |
| Compiti | 3821.9 | 3555.4 |
| Durata totale | 3833.8 (prima consegna 16/11: 3833,8) | 3559.4 |

## 8. Cosa NON ho verificato
ascolto a orecchio di rumore, pronuncia e timbro delle voci (le trascrizioni sono fatte, l'ascolto no); sincronia delle evidenziazioni di ripassi e glossario (±1 s è una stima sui tempi della voce); pagina interattiva (quiz, verifica, compiti: la generano la master e il lettore); OCR di tutti i fotogrammi (il controllo severo ne campiona uno ogni 15 s)

## 9. Da confermare col prof / Sara
1. Mappa: «le persone sono **miseri** e tristi» (accordo): nel video non compare in questa forma.
2. «I fiori del **mare**… del male» (≈ 31:12 dell'originale): lapsus, nei sottotitoli «I fiori del male».
3. Dogali (1887) e Adua (1896): il docente le dice in sequenza; sottotitoli «Adua, 1896».
4. Le card di slide, ripassi e glossario derivano dal testo delle slide del docente, spezzato in frasi intere: confermare che la spezzatura va bene.
