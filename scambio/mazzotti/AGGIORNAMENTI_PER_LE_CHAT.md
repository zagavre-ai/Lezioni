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
