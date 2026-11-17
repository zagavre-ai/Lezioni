# Aggiornamenti per tutte le chat di produzione (leggere a ogni nuova lezione)

## 14/11 sera
- **TRASCRIZIONE (Whisper):** Hugging Face è bloccato (403) e il servizio Gemini ha un tetto di 100 richieste: **non usarlo**. Il modello Whisper «base» (sherpa-onnx int8) è sul ramo `modelli-whisper-base` di questo repository: leggi `LEGGIMI.md` di quel ramo (git fetch, ricomponi il decoder, `pip install sherpa-onnx`).
- **Storia V · compiti del prof (lezioni 1–21):** release `mazzotti-storia-V`, zip `STORIA.V.-20261114T220649Z-1-001.zip`, file «LEZIONE N.pdf». Inseriscili nella scheda «Compiti» e in `compiti.json` della consegna. Per le lezioni già consegnate: aggiungi `compiti.json` sul ramo `consegna-<tag>` (nessuna ricodifica).
- **Storia V · test finali (lezioni 1–21):** zip `STORIA.V-20261114T194325Z-1-001.zip`, file «DOMANDE LEZIONE N.xlsx».
- **Letteratura V · compiti del prof (lezioni 1–26):** release `mazzotti-letteratura-V`, zip `LETTERATURA.ITALIANA.V.-20261114T221058Z-1-001.zip`, file «LEZIONE N.pdf». Stessa cosa: scheda «Compiti» + `compiti.json` (per le già consegnate, solo `compiti.json` sul ramo di consegna).
- **Mappe:** strumento `kit/tools/mappa.py` su main (obbligatorio). Se nella release ci sono mappe del docente, partire da quelle.
- **Velocità:** nessuna anteprima intera, una sola codifica finale 1080p veryfast CRF 19, lavoro a catena (mentre codifica, prepari la lezione dopo).

## 15/11 notte (03:40 ora italiana) · SVEGLIA: RIPARTITE TUTTE
- **Perché molte lezioni sono FERMA:** la quota giornaliera di Google per le voci Kore è finita su tutti i modelli. **Riparte da sola alle 09:00 italiane**; il servizio della master è acceso e riprova ogni 20 minuti. Le richieste già sui rami `voci-*` restano in coda: **non rifarle, non cambiare i nomi**.
- **Non stare ferma ad aspettare le voci.** Fai adesso tutto il resto: approfondimenti animati e mappe (con voci SEGNAPOSTO della durata stimata), quiz, sottotitoli del docente, dispensa A4 con le mappe, compiti del prof, testo YouTube, timeline. Quando le voci arrivano in `vox/` sostituisci i segnaposto e fai l'UNICA codifica finale.
- **Stato:** non `FERMA` per le voci: scrivi `IN_MONTAGGIO` con nota «pronta, attende voci Kore». `FERMA` solo per un problema vero, con il motivo scritto nel campo `nota`.
- **Controllo prima di PRONTA (è quello che la circolare alle famiglie promette):**
  1. ogni Parte **50–60 minuti** (le lezioni di Letteratura rifatte sotto i 50 minuti NON sono PRONTA);
  2. **quiz di 5 domande** dopo ogni argomento;
  3. **verifica finale** = test Excel del prof, scheda «Verifica finale» con `t_verifica` esatto (il video riparte solo con almeno l'80%);
  4. **compiti del prof dentro il video** (intro + scheda «Compiti» con `t_compiti`) e `compiti.json`;
  5. **mappe concettuali**: una per argomento + mappa finale, anche nella dispensa;
  6. **bande blu** sopra e sotto in pausa, verifica e compiti;
  7. **slide sincronizzate** con la voce del docente (±1,5 s) e nessun residuo grafico del video originale (logo, bordi) sotto il riquadro del docente;
  8. mai il numero della lezione nel video; 1080p, < 400 MB, `controllo_finale.py` e `controllo_jingle.py` superati.
## 15/11 notte (03:55) · DECISIONE DI SARA SULLA DURATA (sostituisce il punto 1 della lista di controllo)
- Gli approfondimenti animati si fanno **solo con il materiale della lezione stessa** (videodispensa, slide, libro, prove del prof di QUELLA lezione). **Mai anticipare argomenti delle lezioni successive** per allungare: la direzione non lo vuole.
- Se con il materiale della lezione non si arriva a 50 minuti, **va bene così**: la lezione è PRONTA con la durata misurata (scrivila nello stato). Non si inventa e non si allunga. Le lezioni brevi le compensa Sara assegnandone di più nel piano di studi.
- Resta obbligatorio tutto il resto: approfondimenti e mappe per ogni argomento (dal materiale della lezione), quiz, verifica 80%, compiti nel video, bande blu, slide sincronizzate.

## 15/11 mattina (09:45) · CORREZIONE SULLE VOCI
- Le voci Kore **non** ripartono da sole: il blocco non è la quota giornaliera ma il **tetto di spesa mensile** del progetto Google, che è stato raggiunto. Le voci ripartono solo quando Sara alza il tetto (decisione sua). Il servizio della master è acceso e genera appena si sblocca.
- Intanto vale tutto quello scritto nella voce «15/11 notte»: lavora con le voci segnaposto, chiudi tutto il resto, prepara le lezioni successive, stato `IN_MONTAGGIO` «pronta, attende voci Kore». Non `FERMA` per le voci.

## 15/11 pomeriggio (15:05) · LEZIONI FERME SENZA MOTIVO
- **Letteratura V 14, 16, 25** e **Storia V 6** risultano `FERMA` senza nessun motivo scritto. La chat che le ha nella sua lista le riprende **subito** (le voci ora arrivano regolarmente: se le tue non ci sono ancora, chiedile sul ramo `voci-<tag>` e intanto lavora con i segnaposto).
- Da ora: **mai `FERMA` senza il motivo** nel campo `nota` dello stato (una riga: cosa manca, cosa serve).

## 15/11 pomeriggio (17:05) · LE VOCI SONO RIPARTITE: CHIUDETE LE LEZIONI
- Sara ha sistemato il credito Google: **dalle 16:04 le voci Kore funzionano di nuovo**. Il servizio della master le sta generando con priorità **Storia dell'arte V → Letteratura V → Storia V**.
- Già caricate sui rami `voci-*` (cartella `vox/`): **Storia dell'arte V 1, 7, 11, 15 · Letteratura V 16, 25 · Storia V 3**; in corso Storia V 6, poi le altre in coda. Fate `git fetch` del vostro ramo `voci-<tag>`.
- **Chi aveva una lezione «pronta, attende voci Kore»:** sostituisci i segnaposto, fai l'unica codifica finale, controlli, consegna e stato `PRONTA` con la durata misurata.
- **Storia V lezioni 4, 8, 10:** Sara sta caricando adesso i video del docente nella release `mazzotti-storia-V`. Le chat di Storia V: appena compaiono, partite.
- **Non stare ferme:** se la tua lezione è consegnata, passa subito alla successiva della tua lista nel prompt.
- Ogni voce segnata «da controllare» nel log del servizio va ascoltata prima della codifica finale.

## 15/11 sera (19:15) · DECISIONE DI SARA SULLE MAPPE (vale per TUTTE le lezioni)
- Le **mappe concettuali restano nel video** in tutte le lezioni: il modello deve essere uguale per tutte.
- In più ogni lezione consegna le mappe anche come **file PDF a parte**: `Mappe_<tag>.pdf`, **A4 orizzontale**, una mappa per pagina (una per argomento + mappa finale), stessa grafica del video. Va sul ramo `consegna-<tag>` insieme agli altri file.
- Le mappe **NON vanno nella dispensa**: la dispensa resta senza mappe, le mappe sono solo nel file a parte.
- **Lezioni già consegnate:** se hanno le mappe nel video, aggiungete solo `Mappe_<tag>.pdf` sul ramo di consegna (nessuna ricodifica). Se NON hanno le mappe nel video, scrivetelo in PER_LA_MASTER / nello stato («senza mappe nel video») così la master fa l elenco per Sara.


## 15/11 sera (19:35) · CONTROLLO DELLA MASTER PRIMA DI PUBBLICARE: DA SISTEMARE STASERA (la direzione le vuole domani)
Controllate dai file di consegna. Sistemare **senza rifare il montaggio**:
- **Mappe mancanti nel video → «Ripasso con le mappe» inserito SUBITO PRIMA della verifica finale** (decisione di Sara): codifica solo del pezzo nuovo con gli stessi parametri, concatenazione, aggiornare `t_verifica` e `t_compiti` (slittano della durata del pezzo), sottotitoli e capitoli. Voci delle mappe con richiesta sul ramo `voci-<tag>` (il servizio è acceso). Più il file `Mappe_<tag>.pdf` A4 orizzontale.
  - **Letteratura V 3, 5, 8, 17** (chat che le ha consegnate). Letteratura 3 anche: dispensa e `compiti.json` mancanti.
- **Compiti del prof non trovati nel video:** Letteratura V **20** e **25**; Storia V **1**. Aggiungere intro + scheda «Compiti» prima della chiusura (stesso metodo: solo il pezzo nuovo) + `compiti.json`.
- **Storia V 9:** non trovo né la verifica finale né i compiti nei file di consegna. Controllare e sistemare.
- **`compiti.json` mancante** (solo il file, nessuna ricodifica): Storia V 1, 2, 11, 14, 16, 17, 19, 21; Letteratura V 8, 17.
- **Letteratura V 1 e 2:** non c'è il ramo `consegna-<tag>` nel formato nuovo. Chi le ha fatte: consegna sul ramo con tutti i file.
- Finito: stato `PRONTA` e scrivete nella nota «sistemata per controllo 15/11».

## 15/11 sera (19:50) · VOCI: LIMITE GIORNALIERO DI GOOGLE RAGGIUNTO (100 per modello)
- Fino alle **09:00 di domani** non si generano voci nuove. Le richieste già sui rami `voci-*` restano in coda: **non rifarle, non cambiare nomi**. Alle 9 il servizio riparte da solo, con priorità alle correzioni del controllo 15/11 e alle lezioni di Storia V, Letteratura V e Storia dell arte.
- **Non fermatevi:** fate tutto il resto con le voci SEGNAPOSTO (pezzi nuovi, mappe, compiti nel video, `compiti.json`, PDF delle mappe, sottotitoli, testi YouTube). Stato `IN_MONTAGGIO` con nota «pronta, attende voci Kore».
- Le lezioni che hanno già tutte le voci: chiudetele e consegnatele stanotte.


## 15/11 sera (19:52) · CORREZIONE: LE VOCI FUNZIONANO
- Il blocco era solo sul modello «lite». Il servizio ora usa l altro modello e **le voci stanno arrivando di nuovo**. Priorità: correzioni del controllo 15/11 (Letteratura 3, 5, 8, 17, 20, 25; Storia V 1, 9), poi Storia dell arte, Storia V, Letteratura V.


## 16/11 notte (00:30) · INGLESE AFM TRIENNIO DALLA LEZIONE 6: TORNA ALLA MASTER (decisione di Sara)
- Claude 2 è quasi al limite settimanale: le sue chat di Inglese AFM si fermano. Le lezioni **6, 7, 8, …** le fa la **chat della master «Inglese AFM» (E1, quella delle lezioni 4–5)**, in ordine, partendo dalla 6.
- Materiali: release unica `inglese-afm-triennio` (video, dispense, `ENG_Amm_LezN_Verifica.xlsx`, `ENG_Amm_LezN_Compiti.pdf`). Se i file di una lezione mancano, passa alla successiva e scrivilo nello stato.
- Prima di partire controlla `PER_LA_MASTER.txt` sul ramo `scambio-claude2`: se una chat di Claude 2 ha già iniziato la 6 o la 7, riprendi da lì (stesso tag `afm-inglese-triennio-lezNN`).
- Stesse regole delle lezioni 4–5 (narratore Kore in inglese B1, parole chiave tradotte), mappe nel video + `Mappe_<tag>.pdf` A4 orizzontale, quiz, verifica 80% con l'Excel, compiti nel video + compiti.json. Voci: dalle 9 di domattina.

## 16/11 notte (01:00) · CHIMICA MODA PASSA ALLA MASTER (decisione di Sara)
- Le chat di Claude 2 (limite settimanale all'87%) NON continuano Moda III+IV · Chimica applicata (`moda-chimica-III-IV-lezNN`).
- La riprende una chat della master, partendo dal lavoro già sui rami: lez02 PRONTA; lez01, 03, 04, 05, 06, 07, 09, 11 IN_MONTAGGIO (leggere stato-<tag> e scambio/claude2/PER_LA_MASTER.txt prima di toccare qualcosa; non rifare ciò che è fatto); lez08 e lez10 da iniziare.
- Regole: quelle delle voci del 15/11 17:25 (scambio-claude2/DALLA_MASTER.txt) + mappe nel video e `Mappe_<tag>.pdf` A4 orizzontale.
- Alimentazione 1-3: le controlla la master; lezione 1 resta UNA Parte (Sara).

## 16/11 07:55 · STOP PUSH PER 20 MINUTI (cambio nome GitHub)
- Da adesso fino a nuovo avviso NON fate git push. Continuate a lavorare in locale. Il repository passa da zagavre-ai/Lezioni a centrostuditelesio/Lezioni: dopo, aggiornate il remote con `git remote set-url origin https://github.com/centrostuditelesio/Lezioni.git` (vi avviso qui).

## 16/11 08:05 · ANNULLATO: potete fare git push normalmente
- Il nome di GitHub NON cambia per ora. Repository e indirizzi restano quelli di sempre (zagavre-ai/Lezioni). Riprendete i push.

## 16/11 08:20 · NUOVE CHAT DI PRODUZIONE (aperte da Claude Code con il repository) · CHI FA COSA
Molti stati `IN_MONTAGGIO` sono vecchi (chat spostate su altro il 15/11). Regola: se lo stato di una lezione non è aggiornato da **più di 2 ore**, la lezione è libera: scrivi il tuo nome nello stato e prendila; se è aggiornato da meno di 2 ore, saltala.
- **Letteratura V · chat F:** 18, 20, 6
- **Letteratura V · chat G:** 9, 15, 10
- **Letteratura V · chat H:** 11, 13, 22, 23, 24
- **Storia V · chat S5:** 3, 7, 12, 13, poi 4, 8, 10 (appena il video è nell'indice)
- **Storia dell'arte V · chat A5:** 1, 2, 4, 5, 7, 11, 15 (controlla prima gli stati delle chat A1–A4)
Voci Kore: dalle 9 (prima usa i segnaposto e fai tutto il resto: montaggio, slide sincronizzate, animazioni, mappe nel video + `Mappe_<tag>.pdf`, quiz, verifica, compiti). Consegna su `consegna-<tag>` a pezzi da 90 MB + sha256, stato PRONTA. Commit senza firma.

## 16/11 11:30 · LETTERATURA V LEZIONI 1 E 2: PRIORITÀ MASSIMA (servono per far partire il corso)
- I video del prof sono nella release `mazzotti-letteratura-V`: `Letteratura_Lez1.mp4` (805 MB) e `Letteratura_Lez2.mp4` (751 MB), caricati da Sara stamattina. Pagine del libro: `Lez01_ingrandita.1.zip`, `Lez02_ingrandita.1.zip`.
- Le versioni dell'8/11 sono andate perse (mandate solo in chat): **si rifanno da capo** con le regole di adesso (1080p, approfondimenti animati con voce Kore, mappe nel video + `Mappe_<tag>.pdf`, quiz, verifica 80% con l'Excel del prof, compiti nel video + compiti.json, dispensa A4, testo YouTube). Tag: `letteratura-V-lez01`, `letteratura-V-lez02`. Le vecchie voci su `voci-letteratura-V-lez01/02` si possono riusare se i testi coincidono.
- **Chat F**: appena finita la lezione che ha in mano, prende la **1**. **Chat G**: prende la **2**. Se una delle due è ferma da più di 2 ore, l'altra le fa entrambe. Scrivete subito il vostro nome nello stato.

## 16/11 12:30 · REGOLA (Sara): IL PROF SEMPRE NEL RETTANGOLO, MAI NEL CERCHIO
- Il riquadro del docente è **rettangolare** (come nelle lezioni 9, 12, 14, 18, 20, 23, 25: rettangolo nella fascia scura a destra, oppure riquadro rettangolare accanto al testo). **Niente foto o video del prof dentro un cerchio**, in nessuna scheda: introduzione, argomenti, ripassi.
- Controllo fatto sui video consegnati (5 fotogrammi per lezione): **cerchio presente in Letteratura V lezioni 3, 5, 6, 8, 10, 11, 13, 15, 17, 19, 21, 22, 26**. Da rimontare con il rettangolo: **stesso montaggio, stesse voci, stessi tempi** (quiz, verifica e compiti devono restare agli stessi secondi, altrimenti le pagine Vimeo si sfasano). Consegna sullo stesso ramo, stato PRONTA, nota «v3 rettangolo».
- Chi le rifà: ciascuna chat le lezioni che ha consegnato lei (vedi lo stato). Se la chat non c'è più: **F** → 3, 5, 6, 8; **G** → 10, 11, 13, 15; **H** → 17, 19, 21, 22, 26. Prima le lezioni 1 e 2 (priorità), poi queste.
- Anche le lezioni nuove (1, 2 e le altre materie) solo con il rettangolo.

## 16/11 12:45 · ANNULLATO IL RIMONTAGGIO DEL TONDO
- Le 13 lezioni col prof nel tondo (3, 5, 6, 8, 10, 11, 13, 15, 17, 19, 21, 22, 26) le corregge **la master** direttamente sui video finiti. **Le chat NON le rifanno.** Continuate con le lezioni 1 e 2 e con il vostro elenco.
- Regola che resta: nelle lezioni nuove il prof va **solo nel rettangolo 394×218** (come 9 e 14), mai nel tondo (il tondo è solo per la prof. Caputi).

## 16/11 13:10 · STORIA V: LEZIONI 12, 15, 18, 20 A DUE CHAT NUOVE
- Le lezioni 12, 15, 18, 20 erano IN_MONTAGGIO dal 14–15/11 e abbandonate. Le fanno due chat nuove: **S6 → 12, 15**; **S7 → 18, 20** (prompt in `scambio/prompt/`). Le altre chat non le toccano.
- Lezioni 3, 4, 8, 10, 13: Sara sta caricando i video del prof. La 3 resta alla chat S5; la 4, 8, 10, 13 alla S5 appena arrivano i video.

## 16/11 13:15 · STORIA V: VIDEO DELLE LEZIONI 3, 8, 10, 13 PRESENTI · SIGLA E INTRODUZIONE OBBLIGATORIE
- L'indice è vecchio: nella release `mazzotti-storia-V` ci sono come file singoli i video delle lezioni **3** (`LEZIONE.3.L.ITALIA.DI.GIOLITTI.mp4`), **8**, **10** e **13** (in 4 file `Storia.V.Lez.13-1…4.mp4`, da unire in ordine). Manca ancora solo la **4**.
- Chi le fa: **S5 → 3, 13** · **S6 → 12, 15** · **S7 → 18, 20** · **S8 (nuova) → 8, 10**.
- **Ogni lezione di Storia ha la SIGLA di Storia (15 s) e l'INTRODUZIONE** (cartello «Benvenuta e benvenuto» + argomenti, voce Kore, come la lezione 7). La sigla `kit/sigle/Sigla_Storia_15s.mp4` la prepara la master oggi: fino ad allora 15 s di segnaposto.


## 16/11 · 17:45 · STOP QUALITÀ (Sara) — vale per TUTTE le chat, anche S5, S6, S7, S8
- **Escono solo prodotti perfetti.** Prima di consegnare, ogni lezione passa la verifica di `scambio/REVISIONE_StoriaV_REGOLE.md` (Storia) / `scambio/REVISIONE_LetteraturaV_REGOLE.md` (Letteratura): ascolto, visione, testo, pagina — con `RAPPORTO_REVISIONE.md`.
- **Il brief approvato è vincolante:** `scambio/BRIEF_videolezioni_APPROVATO.md`.
- Prof nel rettangolo **stile Spagnolo** (ombra blu, bordo sottile) con **sottopancia giallo e nome ben leggibile**; **testa mai tagliata**; **audio del prof pulito** (highpass 80, arnndn, loudnorm −16, alimiter).
- Strumenti per il rettangolo: `kit/tools/rettangolo/` su main.

## 16/11 ore 10:15 · GRAFICA IDENTICA A SPAGNOLO LEZ. 1 (vale per TUTTE le chat, anche S5, S6, S8)
Decisione di Sara: ogni videolezione deve essere **graficamente identica** alla Lezione 1 di Spagnolo consegnata con il Brief. Modello: `kit/modello_spagnolo/` su main. Regole complete: punto **000** di `scambio/REVISIONE_StoriaV_REGOLE.md` (e LetteraturaV).
- Riquadro del prof **4:3** (circa 410×308 a 1080p, in alto a destra), ombra grigia morbida, niente bordo blu; **il rettangolo 394×218 non si usa più**; testa mai tagliata.
- Fascia gialla col nome **su due righe** («Giorgio Mazzotti» / «PROF. DI STORIA»), sempre visibile.
- Fondo bianco, niente bande laterali blu. Font solo Bricolage Grotesque / Figtree / DM Mono.
- Piè di pagina «STORIA V · Prof. Giorgio Mazzotti» + «Pagina N». «01 · ARGOMENTO» = numero dell'argomento.
- Finale: `kit/sigle/Sigla_finale_5s_con_avviso_diritti.mp4`.
- Consegna anche **PDF slide A4 orizzontale identiche al video** e **PDF mappe del prof** A4 orizzontale.

## 16/11 ore 10:30 · TRASCRIZIONE E SORGENTI (per tutte le chat di revisione)
- HuggingFace è bloccato: per la trascrizione usa **`kit/tools/trascrivi.py`** su main (scarica il modello da GitHub da solo, tempi parola per parola, 1 ora ≈ 10 min). Uso: `python3 trascrivi.py VIDEO.mp4 uscita`.
- Se mancano i sorgenti del montaggio (slide HTML, timeline) **non fermarti**: slide dal `_videodispensa.pptx` del prof (release) + OCR dei fotogrammi del video montato, grafica del modello Spagnolo; timeline dalla trascrizione e dai cambi slide. Chat della lezione 3: riparti da qui (stato da FERMA a IN_REVISIONE).

## 16/11 ore 12:30 PT · BLOCCHI RISOLTI (vale per TUTTE le chat di revisione, Letteratura e Storia)
Dai primi rapporti risultano tre blocchi. **Sono tutti risolti: non scrivere più «bloccato» e non chiedere consensi, procedi.**
1. **Trascrizione / «Whisper non scaricabile» (huggingface bloccato).** Usa `kit/tools/trascrivi.py` su main: `python3 trascrivi.py VIDEO.mp4 uscita`. Scarica il modello da GitHub da solo (nessun consenso necessario), 1 ora di audio ≈ 10 minuti, tempi parola per parola. Fai l'ascolto A completo (trascrizione, «ecco/guarda…», silenzi, parole tagliate, sincronia), non limitarti al `.vtt`.
2. **«Il generatore delle slide non è nel repository».** Sì che c'è: nella cartella principale del repo (main e scambio-mazzotti) ci sono `Telesio_kit_produzione_v1.zip` e `…_v2…v5_aggiunta.zip` (programmi di produzione, tra cui `build_slides.py`, `build_blocks.py`, `GUIDA_MONTATORE.md`). Scaricali con l'API REST e leggi le guide. **Esempio completo già funzionante:** la lezione 3 ha rifatto tutta la grafica nel modello Spagnolo in circa 2 ore — guarda il suo ramo `revisione-letteratura-V-lez03` e il suo `RAPPORTO_REVISIONE.md`.
3. **Mappe concettuali.** Le mappe sono **quelle del prof** (cartella `MAPPE/` nella release, `LEZIONE N.pdf`). Le lezioni 7 e 13 hanno trovato mappe nel video **inventate da noi**: vanno rifatte con i nodi del prof, nella nostra grafica, senza aggiungere né togliere nulla.
- **Tempi:** Sara ha detto che si può andare oltre le 4 ore: **l'importante è finire bene**. Non accorciare la qualità; scrivi a Sara in una riga solo se prevedi di superare le 6 ore.
- **Voci nuove (R1, R2…):** aggiungile a `testi_voci.json` e fai push: il servizio della master le genera in 10–30 minuti.

## 16/11 ore 14:30 · METODO DELLA LEZIONE 3 (IN PROVA sulla lezione 19 con obiettivo 2 ore; per le altre chat è una lista di controllo: i tempi restano quelli già dati, se il metodo funziona diventerà uguale per tutte)
La lezione 3 è la rifatta meglio (tutta nel modello Spagnolo in ~2 ore). Nei file `REVISIONE_*_REGOLE.md` c'è ora la **sezione 5 «METODO COLLAUDATO»**: ordine di lavoro, struttura del rapporto, cose da chiudere meglio. Punti da non perdere:
- **Stessa durata e stessi fotogrammi del video vecchio** (somma dei pezzi = fotogrammi totali): i quiz, la verifica e i compiti restano agli stessi secondi su Vimeo.
- Trascrizione + fotogrammi a 1/s + OCR **prima** di toccare qualsiasi cosa; evidenziazioni dal parlato del prof, non a occhio.
- Rapporto con sezione **«Cosa NON ho verificato»** e ogni dato etichettato misurato / stima / non verificato.
- Voci Kore sbagliate: aggiungi `R1`, `R2`… e rimonta. Schede finali «Quiz / Verifica / Compiti» nel modello. Picco audio ≤ −1 dBTP. Date che non coincidono: lista «DA CONFERMARE COL PROF».
- Se sei già oltre questi punti, non rifare: controlla solo di non aver saltato nulla dell'elenco.

## 16/11 ore 15:00 PT · FETTINE DEL LIBRO: CONTROLLO OBBLIGATORIO (Letteratura)
Il controllo della master sulla lezione 3 ha trovato fettine **sbagliate**: righe tagliate a metà, pezzi di colonne accanto tagliati a sinistra, frammenti estranei. Da adesso (sezione 5 delle regole): per ogni fettina un fotogramma, tutti in `controllo_fettine.jpg` nel rapporto; la fettina inizia e finisce su una riga bianca e prende **solo** la colonna del brano. Con anche un solo difetto la lezione non è consegnabile. **Chat della lezione 3: rifai le fettine (tabella §4 del tuo rapporto) e riconsegna.**

## 16/11 ore 15:10 PT · FONT DELLE ETICHETTE: Figtree Bold, NON DM Mono (correzione della master)
Nelle regole c'era scritto «DM Mono» per la riga «01 · ARGOMENTO», la riga della copertina e il piè di pagina: **era sbagliato**. Nel video Spagnolo (il modello) quelle righe sono in **Figtree Bold maiuscolo spaziato**. Tutte le lezioni devono essere uguali: chi ha usato DM Mono (es. lezione 11) lo cambia. Controllo: confronta la tua slide con `kit/modello_spagnolo/slide_1080p_esempio.png`.
**Audio:** picco massimo −1 dBTP (misuralo con `ebur128=peak=true`): la lezione 11 è a 0,0 dB, la 3 a −0,8. Correggete prima di consegnare.

## 17/11 ore 00:40 (ora italiana) · DECISIONE DI SARA: MAPPE SOLO DEL PROF, LA DURATA PUÒ CAMBIARE (vale per TUTTE)
- **Nel video entrano solo le mappe del prof** (`MAPPE/LEZIONE N.pdf` nella release), impaginate nella nostra grafica, con una voce nuova `R…` che le legge. Le mappe fatte da noi (e la loro voce) si tolgono.
- **La durata può cambiare.** Togli anche i silenzi > 3 s e le frasi della voce narrante senza immagine. Poi aggiorna i secondi in `scheda_pubblicazione.json` (`inizio_s`, `quiz_s`, `durata_s`) e `quiz_argomenti.json`; nel rapporto la tabella secondo vecchio → secondo nuovo. La master rigenera la pagina.
- Annullata la regola «stessa durata e stessi fotogrammi del video vecchio».
- **Chat 20:** rifai così (le 7 mappe nostre → mappa del prof; via i 12 silenzi di 3–4 s) e riconsegna.


## 17/11 ore 01:00 (ora italiana) · LEZIONE DI RIFERIMENTO APPROVATA DA SARA: la 11 (Futurismo)
Sara ha guardato la lezione 11 e ha detto: «tutte così devono essere». Guardala (ramo `revisione-letteratura-V-lez11`, pagina `videolezioni/letteratura-V-lez11-p1/?rev=1`): pagine del libro intere e leggibili, una fettina per volta a tempo con la voce del prof, slide pulite nel modello. Per il font delle etichette vale l'aggiornamento delle 15:10 (Figtree Bold, non DM Mono) e per il volume il picco ≤ −1 dBTP.

## 17/11 ore 01:20 (ora italiana) · JINGLE OBBLIGATORI COME SPAGNOLO (Sara: «la 15 non ha i jingle»)
La master ha misurato il jingle del Quiz nelle lezioni consegnate: c'è in tutte le schede Quiz solo nella **21**; nella 22 in 3 su 5; nella 20 in 1 su 6; **manca** in 3, 11, 15, 26.
- I jingle sono nel kit: `Telesio_kit_produzione_v1.zip` (cartella principale del repo) → `home/claude/v5/snd/`: `quiz.wav` (scheda Quiz), `titolo.wav` (titolo dell'argomento), `repaso.wav` (pillola di ripasso), `trans.wav` (transizioni), `finale.wav`. Sono quelli del video Spagnolo Lez. 1: usali negli stessi punti.
- **Scheda Quiz:** lo scatto di `quiz.wav` deve cadere a 0,0 s (inizio scheda + 0,5 s): controlla con `kit/tools/controllo_jingle.py` (copia `quiz.wav` in `/home/claude/v5/snd/` se lo strumento non lo trova) e metti l'esito nel rapporto.
- Nessuna scheda Quiz o di passaggio in silenzio.

## 17/11 ore 01:25 (ora italiana) · MAI IL PROF TAGLIATO A METÀ FRASE (trovato da Sara nella 15 a 14:18)
Nella lezione 15 il pezzo del prof finisce a metà frase («…con la guerra, il regime non sarebbe…») e parte la voce narrante. **Controllo obbligatorio per tutte:** nel rapporto una tabella con la **fine di ogni pezzo del prof**: minuto · ultime 6–8 parole dette · frase finita sì/no. Ogni pezzo deve finire alla fine di una frase del prof (si allunga il pezzo; la durata può cambiare, poi si aggiornano i secondi nella scheda). Stesso controllo per l'**inizio** di ogni pezzo: niente parole mozzate in partenza.

## 17/11 ore 01:30 (ora italiana) · OMBRE E CARD «IN CORSO» COME SPAGNOLO (Sara, lezione 15 a 34:17)
Nella 15 la card in corso ha **bordo nero spesso e ombra nera netta spostata in basso a destra**: Sara dice «le ombre sono nere», non va. Come Spagnolo (e come la lezione 3):
- **ombre sempre grigie e morbide** (sfocate, poco scure), mai nere e mai «a blocco» spostate;
- **card in corso:** bordo **giallo** sottile + numero su pallino giallo, fondo bianco; le altre card con bordo grigio chiaro;
- riquadro del prof e foto: ombra grigia morbida, niente bordi neri.
Controlla tutte le slide (anche ripassi, schede opera, linee del tempo) e il PDF slide.

## 17/11 ore 08:15 (ora italiana) · DIFETTI GRAVI: LA LEZIONE NON SI CONSEGNA (lezione 22 respinta da Sara)
La 22 è stata respinta: riquadro del prof con **immagine ferma** nella presentazione, **niente jingle**, **niente transizioni**, **audio/video sfasati**. Prima di consegnare controlla e scrivi nel rapporto, con il minuto:
1. **Mai immagine ferma del prof**: in copertina/presentazione il riquadro del prof c'è solo se il prof parla davvero in quel momento (video vivo); altrimenti niente riquadro. Nessun fermo immagine ≥ 1 s nei pezzi del prof (`freezedetect`).
2. **Jingle** come Spagnolo (aggiornamento 01:20) e **transizioni** tra un pezzo e l'altro (`trans.wav` + dissolvenza breve), mai taglio secco.
3. **Sincronia labbra/voce**: per ogni pezzo del prof misura lo scarto audio/video sull'originale (es. correlazione dell'audio col file originale) e scrivilo; scarto massimo 0,04 s.
4. Font Figtree (15:10), ombre grigie morbide e card in corso gialla (01:30), mappe del prof (00:40), fettine intere (15:00), prof mai tagliato a metà frase (01:25).

## 17/11 ore 08:45 (ora italiana) · PRONUNCIA: «Aracoeli» si legge «Aracèli» (Sara)
È latino: «Aracoeli» (romanzo di Elsa Morante) si pronuncia **«Aracèli»**. Nei testi per la voce Kore (`testi_voci.json`) scrivi **«Aracèli»** così Kore lo dice giusto; sullo schermo e nei sottotitoli resta scritto **«Aracoeli»**. Stessa regola per ogni nome latino o straniero: nel testo della voce si scrive come si pronuncia, a schermo come si scrive. Ascolta ogni voce nuova che contiene nomi propri e rigenerala (R…) se è sbagliata.

## 17/11 09:27 — solo per la chat della lezione 15
La lezione 15 è online (verificata e caricata alle 09:10). Resta un difetto: la **copertina iniziale** (fotogramma a 25 s) ha ancora etichetta e piè di pagina in DM Mono. Rifai solo la copertina in Figtree Bold come nel resto della lezione, ricodifica il pezzo, ricontrolla sha e sync, e consegna sullo stesso ramo `revisione-letteratura-V-lez15`. Nient'altro da cambiare.

## 17/11 10:15 — solo per la chat della lezione 7
La lezione 7 è online (verificata e caricata). Resta un difetto: nelle slide «Il tema del "doppio" e la Prefazione a "Dorian Gray"» (pagina 19, intorno a 23:20-24:30) il **titolo finisce sotto il riquadro del prof** e si legge «Dorian Gra». Il titolo deve stare a sinistra del riquadro: mandalo a capo su due righe o accorcialo («Il "doppio" e la Prefazione a "Dorian Gray"»). Controlla tutte le slide della lezione con lo stesso problema, ricodifica, consegna sullo stesso ramo.
