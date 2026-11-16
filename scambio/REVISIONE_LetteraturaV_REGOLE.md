# REVISIONE TOTALE · LETTERATURA ITALIANA V · regole uguali per tutte le chat (16/11/2026)

**Escono solo prodotti perfetti** (Sara, 16/11): niente si consegna con un errore noto.
Sara deve poter dire alla direzione: **ogni lezione è stata guardata, ascoltata e letta tutta, e corretta**.
Tu sei una chat di **revisione**: una sola lezione. Lavori sul video già montato; **non rifai la lezione da capo** se non è necessario. Correggi tutto quello che non è perfetto. Parli con Sara in italiano, dandole del tu, frasi brevi; le decisioni tecniche le prendi tu. Scrivi sempre che cosa hai **misurato** e che cosa è una **stima**.

## 00. Il BRIEF APPROVATO è vincolante
Leggi `scambio/BRIEF_videolezioni_APPROVATO.md` (approvato dalla direzione): sigle, transizioni morbide, matrice grafica v3, **sottopancia giallo con il nome del docente**, riquadro come Spagnolo (punto 000), audio pulito del kit, nessun lampeggio, tabelle mai spezzate. Ogni punto del brief va controllato e, se manca, messo.

## 000. MODELLO GRAFICO: IDENTICO A SPAGNOLO LEZ. 1 (decisione di Sara 16/11) — VINCOLANTE
La lezione deve essere **graficamente identica in tutto** alla Lezione 1 di Spagnolo consegnata con il Brief, più le aggiunte successive. Modello e misure: cartella **`kit/modello_spagnolo/`** su main (fotogrammi, slide 1080p, riquadro, dispensa A4, modello mappe) — **aprila e confronta fotogramma per fotogramma**. Dove questo punto è diverso da altre righe di queste regole o del brief, **vale questo punto**.
1. **Sigla** della materia (15 s) → dissolvenza morbida → copertina (nessun lampo).
2. **Copertina:** logo Telesio in alto a sinistra; riga piccola blu in DM Mono «LETTERATURA ITALIANA V · VIDEOLEZIONE»; titolo grande Bricolage Grotesque 800 blu notte con barretta sotto; card «ARGOMENTI» con l'elenco puntato degli argomenti (su due colonne se servono).
3. **Slide:** fondo **bianco**; in alto la riga blu in DM Mono **«01 · NOME DELL'ARGOMENTO»** (01, 02, 03… = **numero dell'argomento** dentro la lezione, mai il numero della lezione); titolo Bricolage 800 + barretta blu; card e tabelle come Spagnolo (intestazione blu notte con testo bianco, celle in grassetto, mai spezzate); giallo solo per evidenziare la parola o la frase in corso.
4. **Piè di pagina** su ogni slide: a sinistra «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» (DM Mono, blu), a destra «Pagina N». Mai il numero della lezione.
5. **Riquadro del prof:** in alto a destra, formato **4:3** (circa **410×308 px** a 1080p, x≈1428 y≈146 — misura sul modello), angoli arrotondati, **ombra grigia morbida, nessun bordo blu** — esattamente come `riquadro_e_nome.png`. Si vedono **tutta la testa e le spalle** (testa mai tagliata). Il ritaglio si rifà dal video originale del prof (release), con la correzione immagine del kit. **Il rettangolo 394×218 e il tondo non si usano più.**
6. **Fascia gialla col nome:** sotto il riquadro, leggermente inclinata (≈ −3°), **due righe**: «Giorgio Mazzotti» (Bricolage 800, grande) e sotto «PROF. DI LETTERATURA ITALIANA» (maiuscolo, più piccolo); inchiostro blu notte. **Sempre visibile** su tutte le slide dove c'è il prof (come Spagnolo).
7. **Slide senza prof** (presentazione, ripassi, glossario, «ora tocca a te»): testo grande, parole chiave evidenziate in giallo, stesso logo e piè di pagina.
8. **Font:** solo **Bricolage Grotesque** (titoli, 800), **Figtree** (testo), **DM Mono** (etichette). Nessun altro font: controlla con l'OCR/a vista confrontando con `slide_1080p_esempio.png`.
9. **Finale:** `kit/sigle/Sigla_finale_5s_con_avviso_diritti.mp4` (5 s, fondo nero, «GRAZIE PER L'ATTENZIONE», logo bianco, avviso dei diritti).
10. **Struttura obbligatoria** (regola ufficiale 7/11, nessun pezzo può mancare): sigla → presentazione (titolo + argomenti, voce di benvenuto) → per ogni argomento: titolo dell'argomento, spiegazione del prof con slide sincronizzate, approfondimenti animati dove servono, **pillola di ripasso** (breve schema animato con voce narrante), **quiz di 5 domande** → **glossario** animato delle parole chiave → **riepilogo finale** argomento per argomento → finale. Fuori dal video: **verifica finale** (10 domande dall'Excel del prof) e **compiti** del prof. Ogni puntata tra 50 e 60 minuti.
11. **Consegna in A4 orizzontale** insieme al video: PDF delle slide **identiche a quelle del video** (senza riquadro e senza nome) e PDF delle mappe del prof (modello `Modello_mappe_BES.pdf` + matrice v3).
Nel rapporto: tabella di confronto con il modello, punto per punto (1–11): OK / corretto / non possibile (perché).

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
2. **Riquadro del prof e fascia col nome: come al punto 000 (5 e 6)** — 4:3 come Spagnolo, ombra grigia morbida, nome su due righe sempre visibile, testa mai tagliata (se è tagliata già nell'originale, scrivilo nel rapporto con il minuto), sincronizzato con la voce (labbra), nessun avanzo di bianco. Correzione immagine del prof (kit): contrasto 1,04, saturazione 1,03, `hqdn3d=1.5:1.5:3:3`, `cas=0.35` sul riquadro già rimpicciolito. **Niente bande laterali blu**: fondo bianco come Spagnolo.
3. Grafica Telesio, niente testo tagliato o sovrapposto, nessuna slide vuota, nessun segnaposto, **mai il numero della lezione** nel video.
4. **Mappe concettuali: sono quelle del prof** (decisione di Sara 16/11: i docenti le hanno già mandate). Si prendono dalla release della materia (Sara le carica; cerca negli asset un file con «mappa/mappe» e il numero della lezione) e si **impaginano con la nostra grafica** (matrice v3), contenuto identico, senza inventare né togliere nulla. Nel video: una per argomento + mappa finale. Se per la tua lezione la mappa del prof non c'è ancora, scrivilo a Sara in una riga e intanto lavori sul resto (non inventarla).

**B-bis · Pagine del libro in alta risoluzione (Letteratura)** — regola del montatore (5/11):
1. Ogni volta che il prof **mostra o legge una pagina del libro** (poesia, brano, analisi), nel video deve esserci la **«fettina» dallo screen HD**, leggibile (rigo ≥ 26–30 px a 1080p), a tempo con la sua voce, con la fettina in corso evidenziata; via intestazioni, numeri di pagina, QR e loghi dell'editore; tagli solo sulle righe bianche; mai deformare.
2. **Lezioni con pagine del libro:** 1, 2, 3, 5, 6, 8, 9, 11, 13, 14, 16, 17, 18 (le altre — 4, 7, 10, 12, 15, 19–26 — non ne hanno: salta questo punto). Gli screen HD sono negli **zip della release** `mazzotti-letteratura-V` (nomi tipo `LezNN_ingrandita*.zip`; Sara li carica il 16/11 sera per tutte le lezioni). Elenca gli asset della release e prendi lo zip della tua lezione. Se per la tua lezione **non c'è**, nella **prima ora** fai l'inventario (minuto, pagina, titolo del brano) e mandalo a Sara in **una** lista; intanto lavori sul resto. Mai usare la versione a bassa risoluzione presa dal video.
3. Nel rapporto: tabella brano · pagina · file HD · minuto.

**C · Testo (testuale)**
1. OCR di tutte le slide: refusi, accenti, nomi, date, titoli di opere → corretti.
2. **Sottotitoli `.vtt`:** riletti tutti e corretti (nomi propri, «letteratura» non «lettatura», niente frasi senza senso), allineati alla voce (±0,3 s), max 2 righe.
3. **Due PDF A4 ORIZZONTALE da consegnare insieme al video** (decisione di Sara 16/11):
   - `…_slide.pdf`: **le slide IDENTICHE a quelle che girano nel video** (stesse pagine, stesso ordine, stesso testo e grafica), una slide per pagina, **senza riquadro del prof e senza sottopancia**; nessun refuso;
   - `…_mappe.pdf`: le mappe concettuali del prof impaginate con la nostra grafica (una per argomento + mappa finale).
   Controllo obbligatorio: confronta ogni pagina del PDF slide con il fotogramma corrispondente del video (devono coincidere); scrivi nel rapporto il numero di pagine e che il confronto è fatto.

**D · Pagina interattiva** (la genera la master; tu prepari i file giusti)
1. Quiz: 5 domande per argomento, solo dal materiale del prof, risposte giuste davvero giuste.
2. **Verifica finale: 10 domande** dall'Excel del prof («DOMANDE LEZIONE N.xlsx», tutti e 26 nello zip `Excel.prova.finale.LETTERATURA.ITALIANA.V.zip`) — obbligatoria.
3. **Compiti: quelli del prof** dal PDF «LEZIONE N.pdf» (sono **tutti e 26** nello zip `LETTERATURA.ITALIANA.V.-20261114T221058Z-1-001.zip` della release; testo identico) in `compiti.json` formato `{"titolo":…, "esercizi":[{"n":1,"tipo":"aperta","testo":…}]}`. Se il PDF non c'è nella release, scrivi `COMPITI_MANCANTI` nel rapporto.
4. `scheda_pubblicazione.json`: titolo **«Letteratura V · Lezione N · Titolo»** (uguale per tutte), descrizione corretta.

## 2. CORREZIONE
Correggi tutto quello che hai trovato. Ricodifica solo i pezzi che cambi quando possibile; video finale 1080p, x264 veryfast CRF 19, AAC 192k, sotto i 400 MB, con `finale_a_pezzi.py`; poi `controllo_finale.py` e `controllo_jingle.py`. **Rifai la verifica A+B+C sul video nuovo** (almeno sui minuti cambiati + 5 punti a caso).

## 3. CONSEGNA
- Ramo nuovo **`revisione-letteratura-V-lezNN`** (non toccare `consegna-…`): video a pezzi + sha256, `.vtt`, **PDF slide A4 orizzontale, PDF mappe A4 orizzontale**, quiz, test/verifica, compiti, scheda, timeline, e **`RAPPORTO_REVISIONE.md`** con:
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
