# REVISIONE TOTALE · LETTERATURA ITALIANA V · regole uguali per tutte le chat (16/11/2026)

**Escono solo prodotti perfetti** (Sara, 16/11): niente si consegna con un errore noto.
Sara deve poter dire alla direzione: **ogni lezione è stata guardata, ascoltata e letta tutta, e corretta**.
Tu sei una chat di **revisione**: una sola lezione. Lavori sul video già montato; **non rifai la lezione da capo** se non è necessario. Correggi tutto quello che non è perfetto. Parli con Sara in italiano, dandole del tu, frasi brevi; le decisioni tecniche le prendi tu. Scrivi sempre che cosa hai **misurato** e che cosa è una **stima**.

## 00. Il BRIEF APPROVATO è vincolante
Leggi `scambio/BRIEF_videolezioni_APPROVATO.md` (approvato dalla direzione): sigle, transizioni morbide, matrice grafica v3, **sottopancia giallo con il nome del docente**, riquadro con ombra blu, audio pulito del kit, nessun lampeggio, tabelle mai spezzate. Ogni punto del brief va controllato e, se manca, messo.

## 0. Da dove si parte (tutto c'è già)
- **Video montato e materiali:** ramo `consegna-letteratura-V-lezNN` (video a pezzi `.parte_N` + `.sha256`, `.vtt`, dispensa, quiz, test, compiti, timeline se c'è, scheda_pubblicazione, testo_youtube).
- **Video originale del prof, slide del prof (`_videodispensa.pptx`), PDF dei compiti, Excel delle domande:** release `mazzotti-letteratura-V` (download con l'API REST, vedi `kit/REGOLE.md`).
- **Voci Kore già fatte:** ramo `voci-letteratura-V-lezNN`, cartella `scambio/letteratura-V-lezNN/vox/`. **Si riusano.** Solo per frasi nuove o da correggere aggiungi oggetti nuovi (nomi nuovi, es. `R1`, `R2`…) allo **stesso** `testi_voci.json` e fai push: il servizio della master le genera (10–30 min). Intanto lavori sul resto.
- Regole di produzione: `kit/REGOLE.md` su main. Strumenti: `kit/tools/` (mappa.py, finale_a_pezzi.py, controllo_finale.py, controllo_jingle.py, stato.py).

## 1. VERIFICA (la fai tutta, poi scrivi il rapporto)
Scarica il video montato, ricomponi i pezzi, controlla lo sha256.

**A · Ascolto (testuale-uditivo)** — trascrivi TUTTO l'audio (Whisper `small`, lingua it) con i tempi.
1. Ogni frase della **voce narrante** corrisponde a quello che si vede in quel momento. Cerca in particolare: «ecco», «guarda/guardate», «in questa foto/immagine/ritratto/mappa/carta/schema/tabella», «come vedete»: in quel momento **l'immagine nominata deve essere sullo schermo** (±3 s). Se l'immagine c'è nei materiali del prof (slide, dispensa, screen HD) la metti; **se non c'è, tagli quella frase della voce narrante e metti una transizione morbida** (decisione di Sara 16/11). Si taglia solo la voce narrante, **mai il prof**.
2. Nessuna parola tagliata, nessuna frase ripetuta, nessun silenzio > 3 s, nessun salto di audio, volume del parlato -16 LUFS ±2.
3. Nei pezzi del **prof**: niente tagli dentro le frasi.
4. **Rumore (decisione di Sara 16/11):** l'audio del prof va **pulito** come nel kit: `aresample=48000, highpass=f=80, arnndn` (modello del kit) `, loudnorm=I=-16, alimiter`. Controlla all'ascolto 3 punti: niente fruscio, niente ronzio, niente «metallico». Se il video montato non l'ha, rifai l'audio dei pezzi del prof dall'originale con questa catena.

**B · Visione (visiva)** — fotogrammi ogni 2 s (contact sheet per minuto) + OCR del testo delle slide.
1. **Sincronia slide–prof:** mentre il prof parla, la slide mostra quello di cui sta parlando; la card gialla evidenziata è quella della frase che sta dicendo (±1,5 s). Nessuna slide ferma > 60 s se il prof è passato ad altro (es. lezione 10: evidenziazione ferma sul punto 1 da 23:02 a 28:30 → errore). Se il prof presenta il corso o gli argomenti, sullo schermo ci sono **gli argomenti** (non il solo titolo).
2. **Prof nel RETTANGOLO** 394×218, angoli arrotondati (raggio 14), in alto a destra, **stile delle lezioni di Spagnolo** (decisione di Sara 16/11): ombra netta blu Telesio #2060AF e bordo sottile blu notte #0B1530; **sotto il riquadro la fascia gialla #FFE600 con il nome** «Prof. Giorgio Mazzotti» (Bricolage Grotesque 800, ≥ 30 px, inchiostro #0B1530) e la materia in DM Mono — **il nome si deve leggere bene** a 1080p e anche sul telefono. **Mai il tondo**; nessun avanzo di bianco; sincronizzato con la voce (labbra).
   - **La testa del prof non deve mai essere tagliata:** nel rettangolo si vede tutta la testa con un po' di margine sopra. Se l'inquadratura dell'originale la taglia, allarga il ritaglio (rimpicciolisci, non deformare); se è tagliata già nell'originale, scrivilo nel rapporto con il minuto.
   - **Correzione immagine del prof** (kit): contrasto 1,04, saturazione 1,03, `hqdn3d=1.5:1.5:3:3`, `cas=0.35` sul riquadro già rimpicciolito.
   - Le lezioni con la **banda laterale blu** restano con la banda blu, ma riquadro e nome vanno come sopra.
3. Grafica Telesio, niente testo tagliato o sovrapposto, nessuna slide vuota, nessun segnaposto, **mai il numero della lezione** nel video.
4. Mappe concettuali presenti (una per argomento + mappa finale) — se mancano le aggiungi con `kit/tools/mappa.py`.

**B-bis · Pagine del libro in alta risoluzione (Letteratura)** — regola del montatore (5/11):
1. Ogni volta che il prof **mostra o legge una pagina del libro** (poesia, brano, analisi), nel video deve esserci la **«fettina» dallo screen HD**, leggibile (rigo ≥ 26–30 px a 1080p), a tempo con la sua voce, con la fettina in corso evidenziata; via intestazioni, numeri di pagina, QR e loghi dell'editore; tagli solo sulle righe bianche; mai deformare.
2. Gli screen HD sono nella release: `Lez01_ingrandita.1.zip`, `Lez02_ingrandita.1.zip`, `Lez03_ingrandita.1.zip`, `Lez04_ingrandita.1.zip` (solo `Lez04_docente.pdf`), `Lez05_ingrandita.zip`. **Per le lezioni 6–26 non ci sono:** nella **prima ora** fai l'inventario (minuto, pagina, titolo del brano) e scrivilo a Sara in **una** lista, così li carica lei; intanto lavori sul resto. Mai usare la versione a bassa risoluzione presa dal video.
3. Nel rapporto: tabella brano · pagina · file HD · minuto.

**C · Testo (testuale)**
1. OCR di tutte le slide: refusi, accenti, nomi, date, titoli di opere → corretti.
2. **Sottotitoli `.vtt`:** riletti tutti e corretti (nomi propri, «letteratura» non «lettatura», niente frasi senza senso), allineati alla voce (±0,3 s), max 2 righe.
3. Dispensa A4: stessi contenuti delle slide, mappe dentro, nessun refuso.

**D · Pagina interattiva** (la genera la master; tu prepari i file giusti)
1. Quiz: 5 domande per argomento, solo dal materiale del prof, risposte giuste davvero giuste.
2. **Verifica finale: 10 domande** dall'Excel del prof («DOMANDE LEZIONE N.xlsx», tutti e 26 nello zip `Excel.prova.finale.LETTERATURA.ITALIANA.V.zip`) — obbligatoria.
3. **Compiti: quelli del prof** dal PDF «LEZIONE N.pdf» (sono **tutti e 26** nello zip `LETTERATURA.ITALIANA.V.-20261114T221058Z-1-001.zip` della release; testo identico) in `compiti.json` formato `{"titolo":…, "esercizi":[{"n":1,"tipo":"aperta","testo":…}]}`. Se il PDF non c'è nella release, scrivi `COMPITI_MANCANTI` nel rapporto.
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
