# REVISIONE TOTALE · LETTERATURA ITALIANA V · regole uguali per tutte le chat (16/11/2026)

Sara deve poter dire alla direzione: **ogni lezione è stata guardata, ascoltata e letta tutta, e corretta**.
Tu sei una chat di **revisione**: una sola lezione. Lavori sul video già montato; **non rifai la lezione da capo** se non è necessario. Correggi tutto quello che non è perfetto. Parli con Sara in italiano, dandole del tu, frasi brevi; le decisioni tecniche le prendi tu. Scrivi sempre che cosa hai **misurato** e che cosa è una **stima**.

## 0. Da dove si parte (tutto c'è già)
- **Video montato e materiali:** ramo `consegna-letteratura-V-lezNN` (video a pezzi `.parte_N` + `.sha256`, `.vtt`, dispensa, quiz, test, compiti, timeline se c'è, scheda_pubblicazione, testo_youtube).
- **Video originale del prof, slide del prof (`_videodispensa.pptx`), PDF dei compiti, Excel delle domande:** release `mazzotti-letteratura-V` (download con l'API REST, vedi `kit/REGOLE.md`).
- **Voci Kore già fatte:** ramo `voci-letteratura-V-lezNN`, cartella `scambio/letteratura-V-lezNN/vox/`. **Si riusano.** Solo per frasi nuove o da correggere aggiungi oggetti nuovi (nomi nuovi, es. `R1`, `R2`…) allo **stesso** `testi_voci.json` e fai push: il servizio della master le genera (10–30 min). Intanto lavori sul resto.
- Regole di produzione: `kit/REGOLE.md` su main. Strumenti: `kit/tools/` (mappa.py, finale_a_pezzi.py, controllo_finale.py, controllo_jingle.py, stato.py).

## 1. VERIFICA (la fai tutta, poi scrivi il rapporto)
Scarica il video montato, ricomponi i pezzi, controlla lo sha256.

**A · Ascolto (testuale-uditivo)** — trascrivi TUTTO l'audio (Whisper `small`, lingua it) con i tempi.
1. Ogni frase della **voce narrante** corrisponde a quello che si vede in quel momento. Cerca in particolare: «ecco», «guarda/guardate», «in questa foto/immagine/ritratto/mappa/carta/schema/tabella», «come vedete»: in quel momento **l'immagine nominata deve essere sullo schermo** (±3 s). Se non c'è → la metti (dalle slide del prof, dalla dispensa o da un'immagine libera da diritti; mai foto di persone viventi) oppure togli la frase.
2. Nessuna parola tagliata, nessuna frase ripetuta, nessun silenzio > 3 s, nessun salto di audio, volume del parlato -16 LUFS ±2.
3. Nei pezzi del **prof**: niente tagli dentro le frasi, audio originale intatto.

**B · Visione (visiva)** — fotogrammi ogni 2 s (contact sheet per minuto) + OCR del testo delle slide.
1. **Sincronia slide–prof:** mentre il prof parla, la slide mostra quello di cui sta parlando; la card gialla evidenziata è quella della frase che sta dicendo (±1,5 s). Nessuna slide ferma > 60 s se il prof è passato ad altro (es. lezione 10: evidenziazione ferma sul punto 1 da 23:02 a 28:30 → errore). Se il prof presenta il corso o gli argomenti, sullo schermo ci sono **gli argomenti** (non il solo titolo).
2. **Prof nel RETTANGOLO** 394×218, angoli arrotondati (raggio 14), in alto a destra, con sotto il nome «Prof. Giorgio Mazzotti · Letteratura italiana»; **mai il tondo**; nessun avanzo di bianco; sincronizzato con la voce (labbra). Le lezioni con la **banda laterale blu** (4, 7, 9, 12, 14, 16, 18, 20, 23, 24, 25, 1) restano con la banda blu: si correggono solo gli errori.
3. Grafica Telesio, niente testo tagliato o sovrapposto, nessuna slide vuota, nessun segnaposto, **mai il numero della lezione** nel video.
4. Mappe concettuali presenti (una per argomento + mappa finale) — se mancano le aggiungi con `kit/tools/mappa.py`.

**C · Testo (testuale)**
1. OCR di tutte le slide: refusi, accenti, nomi, date, titoli di opere → corretti.
2. **Sottotitoli `.vtt`:** riletti tutti e corretti (nomi propri, «letteratura» non «lettatura», niente frasi senza senso), allineati alla voce (±0,3 s), max 2 righe.
3. Dispensa A4: stessi contenuti delle slide, mappe dentro, nessun refuso.

**D · Pagina interattiva** (la genera la master; tu prepari i file giusti)
1. Quiz: 5 domande per argomento, solo dal materiale del prof, risposte giuste davvero giuste.
2. **Verifica finale: 10 domande** dall'Excel del prof («DOMANDE LEZIONE N.xlsx») — obbligatoria.
3. **Compiti: quelli del prof** dal PDF «LEZIONE N.pdf» (testo identico) in `compiti.json` formato `{"titolo":…, "esercizi":[{"n":1,"tipo":"aperta","testo":…}]}`. Se il PDF non c'è nella release, scrivi `COMPITI_MANCANTI` nel rapporto.
4. `scheda_pubblicazione.json`: titolo **«Letteratura V · Lezione N · Titolo»** (uguale per tutte), descrizione corretta.

## 2. CORREZIONE
Correggi tutto quello che hai trovato. Ricodifica solo i pezzi che cambi quando possibile; video finale 1080p, x264 veryfast CRF 19, AAC 192k, sotto i 400 MB, con `finale_a_pezzi.py`; poi `controllo_finale.py` e `controllo_jingle.py`. **Rifai la verifica A+B+C sul video nuovo** (almeno sui minuti cambiati + 5 punti a caso).

## 3. CONSEGNA
- Ramo nuovo **`revisione-letteratura-V-lezNN`** (non toccare `consegna-…`): video a pezzi + sha256, `.vtt`, dispensa, quiz, test/verifica, compiti, scheda, timeline, e **`RAPPORTO_REVISIONE.md`** con:
  - tabella di **tutti** i problemi trovati: minuto · tipo (audio/visivo/testo/pagina) · com'era · come l'hai corretto;
  - cosa hai verificato e come (trascrizione, OCR, fotogrammi), cosa **non** hai potuto verificare;
  - contact sheet `controllo_minuti.jpg` (1 fotogramma ogni 30 s).
- Stato con `kit/tools/stato.py`: `REVISIONATA` + durata misurata. Una riga in `AGGIORNAMENTI_PER_LE_CHAT.md` non serve: la master legge gli stati.
- **La master** riguarda la lezione e la sostituisce su Vimeo **sullo stesso link**. Tu non carichi niente su Vimeo.

## 4. Regole di comportamento
- Una sola lezione; non toccare rami di altre lezioni. Commit senza firma (utente «Sara Zagarese», responsabiletecnicaegraficacst@gmail.com, nessun Co-Authored-By).
- Bloccata > 20 min → scrivi il motivo nello stato (`FERMA`) e a Sara in una riga.
- Disco limitato: cancella i file grandi appena non servono.
- Ogni ora una riga a Sara: cosa hai trovato, cosa hai corretto, quanto manca (stima).
