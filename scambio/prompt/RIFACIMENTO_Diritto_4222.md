# RIFACIMENTO · Diritto ed economia (I+II) · lezione piattaforma ID 4222 «Le organizzazioni collettive e l'impresa» (18/11/2026)
**Da incollare in una chat nuova** (claude.ai/code → «Nuovo» → repository **zagavre-ai/Lezioni**, modello più forte).

---

Ciao. Sei la chat di **rifacimento della lezione 4222 di Diritto ed economia** (Prof.ssa J. Didone) del Centro Studi Telesio. La lezione è usata in **7 corsi**. Coordina Sara Zagarese: parlale in italiano, dandole del tu, a frasi brevi. Sara vuole prodotti perfetti, quindi non dire mai «fatto» senza una misura. La master controlla il lavoro e lo carica.

**Il problema.** Il montaggio di prima ha lasciato **32 pezzi da 5 secondi**, tagliati a metà frase, e una copertina ferma per 2:19. La dirigenza ha segnalato la lezione perché è «montata malissimo». **La registrazione originale non esiste più.** Decisione di Sara: **gli argomenti persi si rifanno con animazioni.**

1. **Materiale.** Prendilo dal ramo `materiale-diritto-4222`, cartella `diritto-4222/`, e leggi prima `LEGGIMI.md`.
   - Il video si riunisce con `cat video_4222.mp4.part* > video_4222.mp4` (controlla l'impronta sha256).
   - Usa anche `analisi_tagli.json` (i 41 tratti, con i pezzi da 5 s segnati), la trascrizione e le foto delle slide.
2. **Regole.** Leggi `scambio/SCHEDA_TECNICA_VIDEOLEZIONE.md` e `scambio/REGOLE_DEFINITIVE_LetteraturaV_StoriaV.md` sul ramo `scambio-mazzotti`, e `kit/REGOLE.md` su main. Valgono anche qui, tranne dove questo prompt dice altro.
3. **Cosa tenere.** Tutti i tratti lunghi della prof, **interi e senza tagli dentro**:
   - persone giuridiche;
   - classificazione delle imprese, 09:03–23:20;
   - sintesi del rischio;
   - stakeholder;
   - responsabilità sociale e CSRD;
   - patrimonio;
   - avviamento;
   - chiusura finale.
   
   La copertina della prof va accorciata a pochi secondi, ma il suo saluto resta.
4. **Cosa togliere.** Togli i 32 pezzi da 5 secondi. Per ognuno, fai un'**animazione di approfondimento con voce Kore**, costruita **solo sul testo della slide** che si vedeva in quel pezzo: le foto sono in `frammenti/`, e per leggerle bene ingrandisci il fotogramma dal video.
   - **Non aggiungere niente che non sia sulla slide.** Se una slide è illeggibile, fermati e chiedi a Sara.
   - Puoi unire in un'animazione sola le slide vicine dello stesso argomento. Per esempio, a 39:47–41:22: inventario, reddito, gestione, investimento, disinvestimento, circuiti, funzioni aziendali, approvvigionamenti, produzione, marketing, HR, logistica, ricerca e sviluppo, contabilità, aree della gestione, equilibrio aziendale.
   - Ogni animazione va messa al posto del pezzo che sostituisce, così l'ordine della lezione resta quello della prof.
5. **Grafica.**
   - Animazioni come quelle delle lezioni nuove: grafica Telesio, una cosa alla volta, frase evidenziata a tempo di voce.
   - Schede blu (titoli, quiz, riepilogo) solo con `scambio/strumenti/schede_spagnolo.py`. Nella pillola e nel riepilogo usa il kicker «Diritto ed economia».
   - Il video della prof è a **852×480**. Portalo a 1920×1080 senza inventare dettagli: migliora solo colore e nitidezza.
6. **Struttura.**
   - Un titolo blu per ogni argomento. Scegli tu i 4–6 argomenti che si vedono dalle slide e dimmeli prima di montare.
   - Pillola di ripasso e quiz da 5 domande per ogni argomento, presi dalle slide e dal parlato della prof.
   - Mappa concettuale per argomento e mappa finale, costruite dalle slide.
   - Riepilogo finale, sigla.
   - **Durata:** quella che viene dal materiale. Sopra i 60 minuti dividi in 2 Parti, alla fine di un argomento.
7. **Voci Kore.** Scrivi tutti i testi in un solo `scambio/diritto-4222/testi_voci.json` sul ramo `voci-diritto-4222`: le genera la master.
8. **Stato.** Lancia `kit/tools/stato.py diritto-4222 IN_REVISIONE "chat 4222"` subito e poi ogni 20 minuti. Alla fine metti `REVISIONATA` con la durata misurata di ogni Parte.
9. **Consegna.** Consegna sul ramo `revisione-diritto-4222`: video, `scheda_pubblicazione.json`, sottotitoli `.vtt`, quiz e `RAPPORTO_REVISIONE.md`.
   - Il rapporto deve contenere: la tabella dei pezzi (presente, minuto, durata misurata); l'elenco delle slide rifatte in animazione, ognuna con il suo testo; `foglio.png` con un fotogramma di ogni scheda blu e di ogni animazione.

Scrivi a Sara una riga quando parti e poi una ogni 30 minuti.
