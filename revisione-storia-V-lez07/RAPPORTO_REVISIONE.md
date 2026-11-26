# RAPPORTO DI REVISIONE · Storia · «Gli Stati Uniti: dal boom economico al New Deal» · Parte 1 (tag storia-V-lez07)

Correzioni 22/11 fatte. Una sola Parte (53 min 17 s). Consegna dopo le 10:00 UTC previste: le voci Kore sono arrivate in ritardo e le schede che le usano sono state rifatte con quelle vere.

## Misure sul video finale `Storia_Lez7_Parte1_1080p.mp4`
- Durata 53:17,4 (3197,37 s) · fotogrammi 95 921 = durata × 30 · 1920×1080 · 30 fps · x264 · AAC 192k 48 kHz · peso 312,6 MB (una sola codifica; consegnato in 4 pezzi da 90 MB, sha256 nel file `.sha256`).
- Volume −16,3 LUFS · picco vero −1,5 dBFS.
- Scatto dei 5 quiz (jingle) a +0,009…+0,014 s dall'inizio della scheda (file `jingle.txt`): non esattamente 0,0 s, ma entro 15 ms (meno di un fotogramma).
- `controllo_rapido.py`: **ESITO OK** (nessun errore: nessuna pausa muta oltre 2,5 s, nessun nome del docente nel piè di pagina, nessuna scheda con fasce, nessuna schermata identica oltre 3 minuti, titolo in copertina 8/8 parole). Foglio dei fotogrammi e json in consegna.
- `controllo_finale.py`: **TUTTO OK** (durata, fotogrammi, peso 312,6 MB = 298,2 MiB, formato, quiz a 0,0 s, nessun fermo immagine del docente, volume del parlato −15,5 LUFS, sottotitoli: 856 blocchi, nessuna sovrapposizione, attacco sulla voce entro 0,3 s nell'83% dei verificabili). Esito in `controllo_finale.txt`, miniature in `miniature_per_pezzo.jpg`. I sottotitoli sono stati agganciati all'attacco reale della voce sul video finale.
- Timbro della voce del docente (acuti > 4 kHz meno 100 Hz–1 kHz, confronto con l'originale su tutti i 15 pezzi del docente, fino a 30 s ciascuno): finale da −14,4 a −19,5 dB (dentro −9…−20), differenza dall'originale al massimo 0,9 dB. Il pezzo più vicino al limite è Dprof5_1 (−19,5).

## Tagli del docente (tabella in `tagli.md`)
16 pezzi del docente. Ogni pezzo comincia e finisce su frase intera, con il taglio 0,15 s prima della frase che segue (margini in tabella).
- Un solo caso segnato «NO» dal programma: fine di Dprof3_0 (19:54,7) «…a favore dei ricchi, sono i repubblicani». La frase è conclusa a voce; la trascrizione automatica non mette il punto e sente «sono di repubblicani». Da riascoltare dalla master.

## Sincronia labbra/voce
Misura a campione su 64 punti: scarto mediano 0 fotogrammi; 6 campioni fuori ±1 fotogramma (−2…+4 fotogrammi, cioè fino a 0,13 s) in Dintro, Dprof2_0, Dprof3_0, Dprof4_2, Dprof5_2. Probabile errore di campionamento della misura (il mediano per pezzo è 0), **ma non verificato a mano**: va riguardato da chi controlla.

## Struttura e regole
- Ordine: sigla · copertina con titolo esatto e voce di benvenuto · introduzione del docente (170 s sopra la copertina, meno di 3 minuti; la copertina cambia evidenziazione per non restare identica) · «Di cosa parliamo» · 5 argomenti, ciascuno con titolo + jingle, docente con slide a card (massimo 3, frase intera, bordo giallo all'inizio della frase), 2 approfondimenti animati con voce Kore, pillola o schema di ripasso, quiz da 5 domande (soglia 80%, testo «Rispondi · premi Controlla · poi Continua») · glossario · ripasso finale · verifica di sbarramento (Excel del docente, soglia 80%) · sigla finale con avviso diritti · intro «Compiti» con jingle e compiti del docente letti con voce Kore (voci CP1, CP2).
- **Mappe:** solo quelle del prof (3). Mappa 1 «Qual è la situazione economica e sociale degli Stati Uniti dopo la guerra?» cade a fine argomento 3 perché il prof la presenta lì; mappa 2 «Quali sono le cause e gli effetti della Grande depressione?»; **mappa 3 senza domanda come titolo: titolo scritto da me «Che cosa prevede il New Deal?» con parole del prof (approvato dalla master, voce M3_0_R2)**. Nessuna mappa finale (il prof non ne ha fatta una di tutta la lezione). Nessuna mappa inventata. Ogni mappa compare una sola volta.
- Nessuna Parte precedente: **nessuno «spiegone»** (lezione di una sola Parte).
- **Immagini:** Wikimedia Commons è bloccato dal proxy (403): nessuna immagine esterna, solo grafica e slide del prof (come approvato dalla master). Nessuna foto di persone reali aggiunta.
- Piè di pagina di slide, schede, dispensa e mappe: materia e «Pagina N», senza nome del docente. Nome del docente solo nella fascia gialla.
- Dispensa: 57 pagine A4 orizzontali, identiche al video, con strato di testo invisibile. PDF mappe a parte con copertina «MAPPE».
- File: `quiz_argomenti.json`, `verifica_finale.json`, `compiti.json`, `Storia_Lez7_verifica_finale.xlsx`, `Storia_Lez7_compiti_docente.pdf`, `scheda_pubblicazione_Parte1.json`, `timeline_Parte1.json`, `.vtt` (856 blocchi, fatto con i termini corretti dal materiale del prof; spento all'avvio).

## Refusi e anomalie nel materiale del docente
- Refusi nelle nostre slide: nessuno da correggere trovato (nomi propri e termini già corretti nelle slide: Herbert Hoover, Ku Klux Klan, Sacco e Vanzetti, Fitzgerald, Hemingway, Steinbeck).
- Anomalie lasciate come le dice il docente (da portare a Sara):
  - nelle slide «14 e 29 ottobre» (crollo di Wall Street), a voce «24 e 29»;
  - proibizionismo «introdotto nel 1919»: a voce e nelle slide è così, la data va ricontrollata;
  - leggi sull'immigrazione «tra il 1921 e il 1934»;
  - John Steinbeck citato tra gli autori della «generazione perduta» (è associato di solito agli anni Trenta).
- SC5_3_R2 (voce che spiega AAA e NIRA): la voce Kore è lenta (8,8 caratteri/s, scandisce le sigle); il controllo voci dice «durata fuori misura»; il testo è corretto e le sigle sono rispiegate.

## Cosa NON è stato verificato
- Ascolto umano di tutte le voci Kore con nomi stranieri (Ku Klux Klan, Hoover, Keynes, Tennessee Valley Authority, Agricultural Adjustment Act, National Industrial Recovery Act): controllate solo con la trascrizione automatica (`ESITI_2.txt`).
- Sincronia labbra a mano (vedi sopra).
- Bordi delle voci Kore nuove (ampiezza negli ultimi 50 ms sotto 0,03): non rimisurati sulle voci arrivate stamattina; il limitatore e le dissolvenze di montaggio sono quelli del resto del video.
- Sottotitoli: non riletti a mano sul video finale.
- Il controllo dell'agente separato del §11: vedi sezione sotto.

## Controllo dell'agente separato (§11)
Eseguito da un agente separato su foglio, json e file di consegna (non ha riascoltato il video). Esito iniziale: NON consegnabile per: (1) fine di Dprof3_0 a 19:54,7 da riascoltare (la frase è conclusa a voce; l'«inizio NO» di Dprof3_1 è un effetto della stessa trascrizione automatica, non un taglio a metà); (2) sincronia a campione non verificata a mano; (3) «LEZIONE 7» nel PDF dei compiti — **corretto**: PDF rifatto dal `compiti.json` senza numero di lezione né nome del docente; (4) timbro su soli 3 pezzi — **corretto**: ora tutti i 15; (5) peso 312,6 MB (MB) contro 298 (MiB) — stessa misura, chiarito; (6) sottotitoli agganciati alla voce — **corretto**, controllo_finale TUTTO OK. Restano aperti, dichiarati: punto 19:54,7, sincronia labbra a mano, pronuncia dei nomi stranieri nelle voci Kore (non ascoltata), bordi delle voci nuove, SC5_3_R2 lenta.


## Correzione del 26/11 (elenco DIFETTI_Storia_V_25-11-2026, lez07 Parte 1)
- **Difetto confermato sul video (misurato, fotogramma):** a 51:42–51:47 la scheda «Verifica di sbarramento» aveva il titolo su due righe che copriva il testo «10 domande · per superarla serve almeno l'80%…».
- **Correzione:** rifatta solo quella scheda (4,4 s) con lo stesso programma delle schede blu: «Verifica finale», etichetta «VERIFICA DI SBARRAMENTO», titolo su una riga, testo e «Rispondi · premi Controlla · poi Continua» senza sovrapposizioni. Sostituita da 51:41 a 51:49 (dissolvenze comprese); audio e tutto il resto del video non toccati.
- **Misure sul file nuovo (M):** durata 3197,43 s (prima 3197,37: +0,06 s, una frame in più alla giunzione); quiz e inizio argomenti invariati (tutti prima del punto modificato); i tempi dei pezzi dopo la verifica (FIN1, sigla finale, compiti) sono spostati di +0,055 s in `timeline_Parte1.json` (approssimato). `controllo_rapido.py`: ESITO OK (LUFS −16,3, picco −1,5 dBTP, nessuna pausa muta, nessun nome del docente nel piè di pagina, titolo in copertina 8/8). Foglio e json aggiornati.
- **NV (non verificato):** non ho riascoltato la lezione; il resto del video è identico al precedente (copia dei pezzi senza ricodifica, salvo gli 8 s della giunzione 51:39–51:56 ricodificati a CRF 19).
- Rimane da decidere alla master: il glossario a 47:44 mostra 2 card nel fotogramma del foglio (non ho aperto il resto del pezzo).
