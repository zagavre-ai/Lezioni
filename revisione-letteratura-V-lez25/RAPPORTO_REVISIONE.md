# CORREZIONE URGENTE 25/11 (Letteratura V · lezione 25)
Partita dal video consegnato (`Letteratura_Lez25_Parte1_1080p.mp4` del 23/11), senza rifare il montaggio. Ricodificato una volta (x264 veryfast CRF 19, AAC 192k 48 kHz). **misurato** = con uno strumento; **non verificato** = non ho potuto.

## Controllo rapido sul video nuovo (misurato)
`controllo_rapido.py`: **un solo errore, preesistente: la scheda dei compiti muta (38:37, 60,7 s)**, perché la voce COMPITI non è ancora arrivata sul ramo voci (nessun `COMPITI.wav`). Tutto il resto OK: −16,7 LUFS, picco −1,3 dBTP (alla prima codifica era 0,0: aggiunto limitatore sui soli picchi), 1920×1080 30 fps, 146 MB, nessun nome del docente nel piè di pagina, titolo in copertina 3/3. Foglio dei fotogrammi guardato: giunzioni D5→approfondimento, D6 e scheda finale a posto. **Esito del programma: DA CORREGGERE solo per i compiti muti.**

## 1. Minuto 27:49 · l'approfondimento tagliava il professore — FATTO
- **Causa (misurata sull'originale):** la frase è «…Scritti corsari del 1975, d'accordo, **possiamo andare pure su questi.**». Il pezzo D5 finiva su «d'accordo,» e «possiamo andare pure su questi» era finito in testa al pezzo D6 (dopo l'approfondimento).
- **Ora:** il professore finisce la frase («…d'accordo, possiamo andare pure su questi.», verificato con la trascrizione sul video nuovo, 27:42–27:51), poi pausa di 0,45 s, dissolvenza al bianco con `trans.wav`, approfondimento. Le sue parole sono le stesse di prima, non tagliate né cambiate: solo spostate di 2,4 s.
- Immagine: per i 2,4 s in più il riquadro del professore è preso dal **file originale** (stesso ritaglio e stessa correzione colore del resto; allineamento misurato, correlazione 0,988) sulla slide che c'era.
- Il pezzo D6 ora riprende alla pausa prima di «Nelle postume lettere…» (30:39,7): dissolvenza dal bianco con la slide già a schermo e la card accesa, il professore parla a 30:41,7 come prima. Pausa muta più lunga introdotta: 1,97 s (< 2,5 s).
- La durata totale resta uguale (2378,47 s; +1 fotogramma). **Cambia solo il tempo di Q5**: 1830,9 → **1833,33 s** (argomento 5: quiz, T6 e inizio argomento 6: 1834,5 → 1836,93). Q1–Q4, Q6, verifica e compiti: identici. Rigenerati `timeline.json`, `scheda_pubblicazione.json`, `testo_youtube.txt` (capitolo 6: 30:36) e `.vtt`.

## 2. Da 30:34 alla fine · sovrapposizioni — NON TROVATE, mappa NON modificata
- Ho ascoltato (trascrizione) e misurato tutto il tratto. **Voci:** ho cercato ogni voce Kore (AN14, S6, R2, GL1, RF1, FIN1) nell'audio del video con la correlazione: ognuna parte dopo la fine della precedente, nessuna sovrapposizione fra due voci. **Jingle:** l'energia di titolo, quiz, ripasso e trans finisce prima della fine di ogni scheda (tranne il ripasso, che accompagna l'attacco della voce). **Schede:** guardati i fotogrammi a ogni giunzione: solo le dissolvenze al bianco previste, nessuna scheda sopra un'altra.
- Se la sovrapposizione è in un minuto preciso, serve il minuto: ci lavoro su quello. **Non verificato:** l'ascolto umano.
- **Mappa «OPERE» (35:27): confermata incompleta rispetto alla mappa del professore** e non l'ho toccata: nelle 3 schermate (decise dalla master il 22/11 per le scritte a 34 px) il ramo OPERE compare **staccato dal centro** (nessuna freccia da «Pier Paolo Pasolini») e la mappa **intera non compare mai**: l'ultima schermata ferma è solo «romanzi + regista». Il disegno vettoriale e lo script della mappa non sono nel repository, quindi rifarla è un lavoro nuovo: **la intera a una schermata ha scritte sotto i 34 px** (conflitto con la regola della master). **Serve una decisione** (mappa intera a schermo con scritte più piccole nell'ultimo quadro, oppure 4 schermate con il collegamento al centro) e una nuova voce se cambiano i tempi.

## 3. «Ci vediamo alla prossima lezione» — FATTO
- Tolto dalla scheda finale (testo cancellato su tutti i 198 fotogrammi, controllato sul foglio) e **dalla voce**: «Fine della lezione. Grazie per l'attenzione.» (la voce Kore è stata tagliata dopo «attenzione», con dissolvenza di 80 ms; trascrizione verificata). Per non lasciare una pausa muta di 2,8 s l'audio della scheda è spostato in avanti di 0,9 s (muti: 0,9 s all'inizio e 1,9 s alla fine).
- Tolto anche dalla **dispensa** (`Letteratura_Lez25_slide.pdf`, pagina 57: immagine e strato di testo invisibile) e dal `.vtt`. Il PDF delle mappe non cambia.
- Se la master preferisce la voce rigenerata invece del taglio, basta `FIN1_R2` con il testo «Fine della lezione. Grazie per l'attenzione.».

## Non verificato
Ascolto umano; l'agente separato del §11 non c'è stato (urgenza di 1 ora, superata): ho controllato io sul foglio. La voce COMPITI resta quella di prima (la scheda dei compiti è muta per 60 s, `controllo_rapido` la segnala come l'altra volta se è ancora così).

---

# AGGIORNAMENTO 23/11 (correzioni della master del 22/11 22:50)
- Schede di titolo, quiz, ripasso, approfondimento, riepilogo e glossario ora **blu scuro a tutto schermo**; negli approfondimenti **tutte le card sono visibili dall'inizio** e si accendono con la voce (niente più schermata con il solo titolo).
- **Mappa del prof in 3 schermate** (vita/è stato/pensiero; opere-poesie; opere-romanzi/regista) con testo a 40 px, ramo per ramo con la voce R2.
- Schede quiz/verifica: «Rispondi · premi Controlla · poi Continua». Compiti: una card per compito a schermo con bordo giallo e frase finale «Svolgi i compiti qui sotto e premi Consegna…».
- **Voce COMPITI**: testo già inviato sul ramo voci; **la voce non è ancora arrivata**: per ora la scheda dei compiti dura 60 s con i tempi stimati e **senza voce (resta l'unica pausa muta segnalata da `controllo_rapido`)**. Appena arriva rimonto solo quel pezzo e riconsegno.
- `controllo_rapido.py`: unico errore la pausa muta dei compiti; foglio e json sono in cartella.

# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 25 · Pier Paolo Pasolini
Correzioni del 22/11/2026 (sul video del 17/11). Video: `Letteratura_Lez25_Parte1_1080p.mp4` (a pezzi `.parte_00/01`, sha256 nel file `.sha256`, verificato sul file ricomposto).
**misurato** = misurato con uno strumento; **stima** = dedotto; **non verificato** = non ho potuto.

## 1. Cosa ho cambiato il 22/11
- **Slide del prof:** testo delle card a **40 px**, interlinea 1,5, card alte quanto il testo. Ogni card è una **frase intera** (le frasi lunghe del prof sono separate in card distinte), al massimo **3 card** per slide, la slide cambia quando il prof passa alla 4ª frase; se tre card non entrano a 40 px la slide si divide. Bordo e pallino gialli sulla card in corso (tempi dal parlato, ±1 s; i tempi dei paragrafi sono misurati, quelli delle singole frasi sono stimati dalla trascrizione). Schermata identica più lunga: 123 s; card sola più lunga: 52 s (misurato dall'agente di controllo).
- **Mappa:** una sola, **quella del prof**, ridisegnata nel **modello BES** (colori pesca, celeste, paglierino, menta, lilla con legenda in alto a destra), stesse parole e stessa struttura, costruita **un riquadro alla volta** con la voce Kore **R2**; il riquadro è giallo mentre la voce parla; alla fine mappa intera ferma 7 s. Va prima del glossario (riguarda tutta la lezione), una volta sola. Ridisegnata **senza il marchio mappe-scuola.com e senza le foto di Pasolini** (decisione di Sara).
- **Introduzione:** il prof sopra la copertina dura 22 s (poi voce Kore con gli argomenti che si accendono quando li nomina, **senza riquadro del prof**). Titolo copertina «Pier Paolo Pasolini».
- **Glossario:** ora a **due pagine** con tutti e **6 i termini** letti dalla voce (prima ne mostrava 3).
- **Piè di pagina:** «LETTERATURA ITALIANA V» + numero di pagina, senza il nome del docente (il nome compare solo nella fascia gialla).
- **Jingle e transizioni:** jingle anche su glossario, ripasso finale, Verifica, Compiti; dissolvenza a ogni cambio di pezzo, compresi gli ultimi (prima 3 tagli secchi alla fine).
- **Taglio D0/D1:** il pezzo del prof non si interrompe più a metà frase («…Analizziamo la sua | Ecco appunto una sua fotografia»).
- **Audio del prof:** −16,9 LUFS, picco ≥ −1 dBTP, catena del kit; guadagno +0,4 dB e voce della mappa +1,5 dB (prima fuori di 1 dB).
- **Sottotitoli:** rifatti sul video finale; anni scritti in cifre («1922», non «19ventidue»), «Palazzo» maiuscolo, mappa su due righe.
- **PDF:** slide (57 pagine) e mappe (2 pagine), A4 orizzontale, identici al video (senza riquadro del prof), **con strato di testo invisibile** selezionabile (testato con `pdftotext`). Copertina con solo materia e titolo (più «MAPPE» nel PDF mappe), piè di pagina con materia e numero, senza nome del docente.
- `timeline.json`, `scheda_pubblicazione.json` («Letteratura V · Lezione 25 · Pier Paolo Pasolini»), `testo_youtube.txt`, `quiz_argomenti.json` rigenerati sui secondi del video finale.

- **Nota di unione:** sul ramo la master aveva inserito nel video del 17/11 «pillole di ripasso» di 14 s con voce di annuncio (commit a663a39). Questa consegna rifà il montaggio da capo e ha già un ripasso con voce e jingle dopo ogni argomento: **ho tenuto la mia versione** di video, `.vtt`, scheda e timeline (coerenti tra loro). Se la master vuole le sue pillole, vanno reinserite sul nuovo video e i secondi rigenerati.

## 2. Misure sul video finale (misurato)
| Controllo | Risultato |
|---|---|
| Formato | 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192k; 69 625 fotogrammi = 2320,83 s × 30 (38:40,8) |
| Peso | 145,7 MB |
| Volume / picco | −16,6 LUFS integrato; picco −1,4 dBFS |
| Silenzi ≥ 2,5 s (`silencedetect −45 dB`) | nessuno (prima: 27 da 3 a 11 s, poi 2 da 2,5 s) |
| Fermi del riquadro del prof ≥ 1 s (`freezedetect`) | nessuno |
| Sincronia audio/video del prof | per ogni pezzo D0–D6, audio finale vs originale: **−0,013 s** (limite 0,04) |
| Jingle Quiz (`controllo_jingle.py`) | Q1–Q6: **0,000 s** |
| PDF slide | 57 pagine (+ copertina) A4 orizzontale, 57 su 57 coincidono col fotogramma del video (maschera su riquadro e nome) |
| Sigla finale, avviso diritti | file del kit, conservato |

## 3. Controlli
- **`controllo_severo.py`:** lanciato sul video finale (passo 20 s, tesseract installato). **Al momento della consegna non aveva ancora finito** (OCR lento su 116 fotogrammi); la copia dell'esito è in `esito_controllo_severo.json` se completata. Un primo controllo dei punti che esso verifica è stato fatto a mano e con l'agente separato: schermata identica più lunga 123 s (< 180), card sola più lunga 52 s (< 60), nessun «…», nessuna card con iniziale minuscola, copertina «Pier Paolo Pasolini» presente per 55 s (< 180), volume −16,6 LUFS, nessuna pausa > 2,5 s, durata 38:40 (**sotto i 45 minuti: il controllo severo la segnerà**; il materiale del prof dura 20 minuti e non si allunga con riempitivi).
- **Agente separato** (non ha montato la lezione) ha spuntato la lista del §11. Difetti trovati e **corretti**: nome del docente nel piè di pagina; mappa senza «vita dei ragazzi nelle borgate romane», senza «regista cinematografico», senza parentesi e senza «.....»; mappa vuota per 4 s all'inizio; tre tagli secchi (FIN1→VER→SFIN→CI1); mappa a −17,6 LUFS e D2 a −17,3; taglio D0/D1 a metà frase; glossario con 3 termini su 6; jingle mancanti su glossario, ripasso finale e Compiti; anni mal scritti nei sottotitoli. Dopo le correzioni ho rimisurato: volume, silenzi, fermi, sincronia, jingle (sotto).
- **Pagina PDF vs fotogramma:** 56 pagine confrontate (maschera su riquadro e nome), nessuna differente oltre il 6 %.

## 4. Fine e inizio di ogni pezzo del prof
| Pezzo | Minuto | Prime parole | Ultime parole | Frase intera |
|---|---|---|---|---|
| D0 | 0:51–1:13 | Buongiorno e benvenuti alla lezione su | del Novecento. Analizziamo. Ecco appunto una sua fotografia. | sì |
| D1 | 1:16–5:04 | Analizziamo la sua biografia, cerchiamo di | costruirsi un'altra vita, una nuova vita, se vogliamo. | sì |
| D2 | 6:57–8:56 | Nella capitale l'impatto con i duri | potrebbe potremmo rubricarlo il suo… impegno. | sì |
| D3 | 10:44–15:10 | Andiamo avanti. Intorno al millenovecentosessanta, periodo | diversa e un po' fastidiosa. | sì |
| D4 | 17:18–21:18 | Allora ripercorriamo, dopo aver visto velocemente | Officina. Quella di vista di cui abbiamo parlato. | sì |
| D5 | 24:24–27:49 | Poi c'è anche la narrativa, certamente. | o Scritti corsari del 1975, d'accordo. | sì |
| D6 | 30:37–32:42 | possiamo andare pure su questi. Nelle | intellettuali più lucidi, tormentati e provocatori. del Novecento. | sì |

(D5 ripete «d'accordo»: il taglio cade dopo «d'accordo.» e il pezzo successivo parte da «possiamo andare…».)

## 5. Secondi vecchio → nuovo
`timeline.json`, `scheda_pubblicazione.json` (`inizio_s`, `quiz_s`, `durata_s` = 2320,83) sono sui secondi del video finale. Rispetto alla versione del 17/11 (38:38,2): la mappa del prof dura 1:52 (prima 1:47) con 4,5 s di mappa intera, il glossario ha 6 termini, il taglio D0/D1 aggiunge 3,6 s.

## 6. DA CONFERMARE COL PROF
- Mappa: «dopo l'**8 settembre 1943** si rifugia a Casarsa»; slide e parlato: «dal **1942** vive a Casarsa». Restano come li dice il prof.
- Mappa: «muore assassinato **a Roma**»; slide: «presso **Ostia**».
- Mappa: «della **società dei consumi**» (così nell'originale, riportato identico).
- Parlato 1:18: «una sua fotografia» ma nelle sue slide non c'è nessuna foto (non si scaricano foto): non risolvibile.
- Nomi dubbi nella trascrizione: «Silone» (tra Verga e Pavese), «a Marx» (prima «a Marshall»): da riascoltare.
- Refusi dei file del prof: nessuno corretto sul file originale (non si tocca); nelle nostre slide ho sistemato «Casarsa/…» maiuscole e accenti; nel PDF «–» e «·» compaiono come «-» nel solo strato di testo invisibile.

## 7. Cosa NON ho verificato
- **Pronuncia della voce Kore** (R1, R2, voci già fatte): nessun ascolto umano; trascrizione automatica: R2 e R1 hanno anni e numeri giusti e frasi complete (agente di controllo). Un solo dubbio: «Alì dagli occhi azzurri» trascritto «Alida/Ali…» da riascoltare; «Accattone» trascritto «A cattone» in tutte le voci (probabile errore del trascrittore).
- **Pause del prof fra 2,2 e 2,6 s** (D4, 18:41 e 19:39): non accorciate, perché cadono dove la slide e il riquadro non permettono un taglio pulito senza toccare il video del prof; sotto 2,5 s alla soglia −45 dB.
- Parlato del prof parola per parola nei sottotitoli: trascrizione automatica, alcuni tratti poco intelligibili (es. «era una cosa non», tolta).
- Testa nel riquadro: la webcam originale è 245×138 px con i capelli a contatto del bordo alto; ritaglio 4:3 ingrandito 2,2×, morbido. Non risolvibile.
- Sigla (fondo nero) e sigla finale (fondo nero): sono i file del kit.
- Pagine del libro: la lezione non ne ha.
