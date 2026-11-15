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

