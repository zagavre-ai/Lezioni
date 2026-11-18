# PROVA DEL METODO IN 2 ORE · LETTERATURA ITALIANA V · LEZIONE 19 · Prof. Giorgio Mazzotti
**Da incollare in una chat nuova** (claude.ai/code → «Nuovo» → repository **zagavre-ai/Lezioni**). Questa è una **prova**: se funziona, il metodo diventa uguale per tutte le chat.

---

Ciao. Sei la chat di **revisione della lezione 19 di Letteratura italiana V** del Centro Studi Telesio. Coordina Sara Zagarese (italiano, del tu, frasi brevi; è stanca e vuole prodotti perfetti: mai «fatto» senza una misura). La master controlla e carica su Vimeo.

**OBIETTIVO: lezione completa, corretta e consegnata in 2 ORE da quando parti** (la lezione 3 l'ha fatto con questo metodo). Non accorciare la qualità: se a un'ora non ci stai, scrivilo subito a Sara in una riga (cosa manca e quanto serve).

1. Leggi **tutto** `scambio/REVISIONE_LetteraturaV_REGOLE.md` (ramo `scambio-mazzotti`), **in particolare la sezione 000 (modello Spagnolo) e la sezione 5 «METODO COLLAUDATO»**, poi `scambio/mazzotti/AGGIORNAMENTI_PER_LE_CHAT.md` e `kit/REGOLE.md` su main. Esempio funzionante da aprire: ramo `revisione-letteratura-V-lez03` (leggi `RAPPORTO_REVISIONE.md` e copiane la struttura).
2. La tua lezione: **`letteratura-V-lez19`** (ramo `consegna-letteratura-V-lez19`, voci su `voci-letteratura-V-lez19`, originale `Letteratura_Lez19.mp4` e pptx del prof nella release `mazzotti-letteratura-V`; mappa del prof in `MAPPE/`). La 19 **non ha pagine del libro**.
3. **Fai come la lezione 3, in quest'ordine:** (a) scarica, ricomponi, sha256; lancia subito `kit/tools/trascrivi.py` in background e intanto estrai i fotogrammi del video vecchio a 1 al secondo + OCR; (b) piano di montaggio contiguo: **stessa durata e stessi fotogrammi del video vecchio** (quiz, verifica e compiti restano agli stessi secondi); (c) rifai tutta la lezione nel modello Spagnolo (non rattoppare); (d) evidenziazioni dal parlato del prof; (e) audio del prof pulito dall'originale con la catena del kit; (f) sottotitoli riletti contro la trascrizione; (g) tutte le consegne (video+sha256, vtt, `…_slide.pdf`, `…_mappe.pdf` con la mappa del prof, `verifica_finale.json`+xlsx, `compiti.json`, `quiz_argomenti.json`, scheda col titolo standard); (h) controllo sul video nuovo (fotogramma ogni 30 s + punti a caso).
4. **Chiudi i punti che la lezione 3 aveva lasciato aperti:**
   - voce Kore pronunciata male (nomi di opere/autori): aggiungi le frasi corrette come `R1`, `R2`… a `testi_voci.json`, fai push, **rimonta** quando il servizio le ha generate (10–30 min);
   - schede finali «Quiz», «Verifica finale», «Compiti» rifatte nel modello Spagnolo;
   - `controllo_jingle.py` sui quiz (se manca il jingle, cercalo nel kit e scrivi cosa hai trovato);
   - picco audio ≤ −1 dBTP;
   - date o dati che non coincidono tra mappa, slide e voce: non decidere tu, lista **«DA CONFERMARE COL PROF»** in fondo al rapporto;
   - mappa del prof nel video solo se la durata resta uguale; altrimenti solo nel PDF e lo scrivi nel rapporto;
   - se per correggere devi cambiare la durata, tabella **secondo vecchio → secondo nuovo** di quiz, verifica e compiti nel rapporto.
5. **Cronometro (serve a Sara per decidere se il metodo vale per tutti):** tieni un file `CRONOMETRO.md` sul ramo con l'ora di inizio e, per ogni fase (a–h + punti del 4), ora di inizio e fine. Alla consegna scrivi il totale e cosa ti ha rallentato di più.
6. Stato: `kit/tools/stato.py letteratura-V-lez19 IN_REVISIONE "prova metodo 2 ore"` subito; entro 1 ora prima versione di `RAPPORTO_REVISIONE.md`; alla fine `REVISIONATA` con la durata misurata.
7. Consegna sul ramo **`revisione-letteratura-V-lez19`**. Commit senza firma (utente «Sara Zagarese», responsabiletecnicaegraficacst@gmail.com, nessun Co-Authored-By).

Scrivi a Sara una riga quando parti e una ogni 30 minuti.
