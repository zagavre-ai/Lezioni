# LETTERATURA ITALIANA V · CORREZIONI FINALI DEL 22/11 (vale per tutte le 26 lezioni)

La tua lezione è già montata, ma **non va online così com'è**. Il controllo severo della master del 22/11 ha trovato gli stessi difetti di Storia V:
- slide ferme 5–7 minuti;
- card spezzate o che cominciano in minuscolo;
- una card sola per minuti;
- introduzione del prof sopra la copertina oltre 3 minuti;
- volume fuori misura;
- mappe sbagliate.

Sara vuole ogni lezione «**pura come l'acqua**»: non c'è più tempo per un secondo giro di correzioni.

Tutto quello che serve è sul ramo **`scambio-mazzotti`**, cartella `scambio/mazzotti/correzioni_22-11/`:
- `REGOLE_BLINDATE.md`: tutte le regole decise da Sara. **Leggilo tutto: vale più di ogni regola vecchia.**
- `controllo_severo.py`: lo stesso controllo che usa la master.
- `modello_mappa_BES/`: la mappa approvata da Sara (Gadda, lezione 20): `mappa.html`, `render.py`, il video di prova e la mappa originale del prof.
- `estrai_da_release.py`: scarica dalla release solo i file che servono, anche dentro gli zip.

## 0. Subito
1. La tua macchina probabilmente è stata chiusa: **riclona** `zagavre-ai/lezioni` e prendi tutto da GitHub. Ti servono il ramo `revisione-letteratura-V-lezNN` (la tua ultima consegna), i rami `consegna-`, `voci-` e `lavoro-` della lezione se ci sono, e la release `mazzotti-letteratura-V`.
2. **Prenota:** `python3 kit/tools/stato.py letteratura-V-lezNN --stato IN_REVISIONE --nota "correzioni 22/11: presa da <tuo ramo>" --invia`. Prima controlla lo stato: se un'altra chat ha già scritto «correzioni 22/11», **non toccarla** e scrivi alla master con `--serve_master`.
3. Lancia `controllo_severo.py` sul tuo video attuale (titolo = titolo esatto della lezione). L'elenco degli errori è la tua lista di lavoro.

## 1. Cosa rifai
**Riusa tutto quello che è giusto:** trascrizione, tagli del prof, voci già fatte, quiz, verifica, compiti, fettine del libro, sigla.

**Testo più grande (Sara, 22/11), sempre:**
- Visto che ricomponi comunque le slide: testo delle card a **40 px** (mai sotto 36), interlinea **1,5**; titoli, etichette e piè di pagina come sono.
- Se a 40 px tre card non entrano, la slide si divide: **mai rimpicciolire**. Restano le regole delle card intere e della schermata mai ferma oltre 3 minuti.
- La dispensa resta identica al video, quindi anche lei con il testo più grande.
- **Solo per questa volta** (riallineamento) il limite delle 2 ore e mezza può essere superato, ma la **scadenza è fissa: consegna entro le 19:30 UTC (20:30 in Italia)**. Al controllo di 1 ora scrivi alla master **quanto tempo ti serve davvero** per finire, con l'ora di consegna prevista.

1. **Mappe**
   - Il prof ha fatto **una sola mappa per lezione** (`MAPPE/LEZIONE N.pdf`, zip `MAPPE-…zip` della release). **Togli tutte le mappe inventate da noi**: ne resta una, la sua.
   - Si ridisegna nitida nel **modello BES approvato** (`modello_mappa_BES/`):
     - stessa struttura, stesse frecce, **stesse parole** del prof;
     - testo in maiuscolo e minuscolo, 34–50 px;
     - colori del disciplinare con la legenda in alto a destra: pesca = concetto centrale, celeste = date e sequenze, paglierino = parole chiave, menta = esempi e opere, lilla = conseguenze.
   - **Si costruisce ramo per ramo** mentre una voce Kore la legge: il riquadro si accende in giallo finché la voce parla, alla fine la mappa intera resta ferma 4 secondi.
   - **Dove va:** se riguarda un solo argomento, alla fine di quell'argomento (prima della pillola). Se riguarda tutta la lezione, prima del glossario. **Una volta sola** (niente «già visto»).
   - Molte mappe vengono da mappe-scuola.com: **ridisegnale senza il loro marchio e senza la foto dell'autore** (decisione di Sara). Scrivilo nel rapporto.
   - **Voci:** numeri e anni in lettere («millenovecentosettantatré»). Trascrivi ogni voce e controlla parola per parola, numeri compresi. Bordi sotto 0,03. La prima prova della lezione 20 diceva «1873» invece di «1973».
2. **Slide del prof**
   - Al massimo 3 card per slide. **Ogni card è una frase intera**: mai «…», mai iniziale minuscola perché continua la frase prima. Card alte quanto il testo.
   - La slide cambia quando il prof passa alla 4ª frase. Il bordo giallo si accende quando il prof **inizia** la frase (±1 s).
   - **Nessuna schermata identica oltre 3 minuti**, nessuna card sola oltre 60 s (se è sola, si unisce alla slide prima o dopo, salvo un'immagine accanto).
   - Le fettine del libro restano, una alla volta, a tempo con la voce.
3. **Copertina:** titolo esatto, mai sotto il riquadro del prof. L'introduzione del prof sopra la copertina dura **al massimo 3 minuti**, poi slide «Di cosa parliamo» con gli argomenti in card che si accendono quando li nomina.
4. **Audio:** parlato del prof a **−16 LUFS ±1**, picco ≤ −1 dBTP. Pause oltre 2,5 s accorciate a circa 1 s, solo tra due frasi e dove la slide non cambia. **Il timbro della voce non deve cambiare** (§2.4 delle regole: tra −9 e −20 dB).
5. **Disciplinare BES:**
   - **niente «già visto»**: una slide o immagine del prof in un solo argomento;
   - **ogni sigla rispiegata ogni volta** che compare;
   - glossario presente.
6. **Mai il prof tagliato a metà frase:** nel rapporto la tabella con inizio e fine di ogni pezzo del prof (minuto, parole, frase intera sì/no).
7. **Dopo il montaggio rigenera sul video finale:**
   - il `.vtt`;
   - `timeline.json`;
   - `scheda_pubblicazione.json`, con titolo «Letteratura V · Lezione N · Titolo»;
   - `quiz_argomenti.json` e `verifica_finale.json`, con i secondi nuovi.
   - Poi le due **dispense A4**, slide e mappa: identiche al video e **con lo strato di testo invisibile** (testo selezionabile, letto dalla sintesi vocale, aspetto identico).

## 2. Controllo prima di consegnare
1. `controllo_severo.py` su ogni Parte finale: **esito OK**, zero errori. Se tesseract manca, installalo (`apt-get install -y tesseract-ocr`). Se non riesci, scrivilo nel rapporto.
2. Poi avvia un **agente separato**, che non ha montato la lezione, e fagli spuntare tutta la lista del §11 di `REGOLE_BLINDATE.md`. Ogni difetto si corregge e il controllo si ripete.
3. Nel `RAPPORTO_REVISIONE.md`: cosa hai cambiato, l'esito del controllo severo, la tabella dei pezzi del prof e **cosa non hai potuto verificare**.

## 3. Consegna
- Stesso ramo **`revisione-letteratura-V-lezNN`**: video a pezzi con sha256, più tutti i file del punto 1.7.
- Stato `REVISIONATA` con nota «correzioni 22/11 fatte» e la durata misurata.
- La master ricontrolla, sostituisce il video su Vimeo **con lo stesso link** e rigenera la pagina della lezione.
- Commit senza firma. Mai dati di alunni.
- **Sara oggi non segue le chat:** ogni dubbio va alla master con `stato.py --serve_master "..."`. A ogni cambio di fase guarda `scambio/letteratura-V-lezNN/DALLA_MASTER.txt` sul tuo ramo `voci-letteratura-V-lezNN`.

## 4. Tempo
Una lezione così si corregge in circa **2,5 ore**: la lezione 3 del 16/11 è stata rifatta nel modello in 2 ore. Scrivi lo stato ogni 30 minuti. Se dopo 1 ora vedi che non ce la fai, scrivilo subito alla master.
