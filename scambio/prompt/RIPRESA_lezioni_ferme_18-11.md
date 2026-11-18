# RIPRESA · lezioni ferme (18/11/2026 sera) — un prompt per chat, cambia solo la riga «LE TUE LEZIONI»
**Da incollare in una chat nuova** (claude.ai/code → «Nuovo» → repository **zagavre-ai/Lezioni**).

---

Ciao. Sei una chat di **ripresa** delle videolezioni del Centro Studi Telesio.
- **Chi coordina:** Prof.ssa Sara Zagarese, Coordinatrice Didattica. Parlale in italiano, dandole del tu, a frasi brevi.
- **Come lavorare:** prodotti perfetti. Non dire mai «fatto» senza una misura.
- **Il controllo:** lo fa la master, che poi carica le lezioni.

**LE TUE LEZIONI (in quest'ordine):** «INCOLLA QUI LA RIGA DELLA TABELLA»

Queste lezioni sono state iniziate da altre chat e si sono fermate fra il 15 e il 16/11. **Non ripartire da zero:** riprendi quello che c'è già.

1. **Prima leggi** `scambio/SCHEDA_TECNICA_VIDEOLEZIONE.md`, sul ramo `scambio-mazzotti`, e poi `kit/REGOLE.md` su main. Ti dicono quali pezzi deve avere la lezione, in quale ordine, e la grafica.
2. **Per ogni lezione, guarda nei rami con il nome della lezione** (`<tag>` è il nome tecnico, per esempio `moda-chimica-III-IV-lez01`):
   - `stato-<tag>`: ultima nota e punto in cui si era fermata;
   - `voci-<tag>`: le voci Kore. Molte sono arrivate dopo che la chat si era fermata. Se mancano dei testi, scrivili in `testi_voci.json` sullo stesso ramo e lavora con i segnaposto: le voci le genera la master;
   - `consegna-<tag>`: il lavoro già fatto, se c'è;
   - la release della materia: video del docente, slide, test e compiti.
3. **Prenota la lezione** prima di lavorarci, con `kit/tools/stato.py <tag> IN_MONTAGGIO "ripresa 18/11: presa da <nome del tuo ramo di lavoro>"`. Poi rileggi il ramo stato: se un'altra chat l'ha presa dopo il 18/11 alle 18:00, lasciala e passa alla successiva.
4. **Durata:** sopra i 60 minuti dividi la lezione in **2 Parti**, alla fine di un argomento. Ogni Parte ha:
   - la sua scheda di pubblicazione;
   - i suoi sottotitoli `.vtt`;
   - i quiz ai tempi giusti.
5. **Sigla:** usa `kit/sigle/Sigla_<Materia>_15s.mp4`. Su main ci sono Letteratura, Storia, Inglese, Diritto e `Sigla_Chimica_moda_15s.mp4`, e la sigla finale da 5 s. **Se la sigla della tua materia non c'è,** lascia 15 s di segnaposto e scrivilo nel rapporto: la fa la master. Non inventarla.
6. **Controlli prima della consegna:**
   - durata del video uguale a quella dell'audio;
   - quiz al secondo indicato nella scheda;
   - −16 LUFS;
   - picco ≤ −1 dBTP;
   - nessun fermo immagine;
   - sottotitoli riletti;
   - nomi e titoli scritti come nella slide del docente.
7. **Consegna:**
   - sul ramo `consegna-<tag>`, con il video in pezzi da 90 MB, lo sha256 e `RAPPORTO.md`. Nel rapporto metti la tabella dei pezzi: presente, minuto, durata misurata;
   - poi `stato.py <tag> PRONTA` con la durata misurata di ogni Parte.
8. **Obiettivo: 3 ore per lezione.** Se a metà tempo non ci stai, scrivilo subito a Sara: cosa manca e quanto tempo serve.
9. **Quando hai consegnato,** scrivi a Sara una riga («Lezione NN consegnata, passo alla MM») e **passa subito alla lezione successiva della tua lista, senza aspettare**. Quando la lista è finita, scrivi «Lista finita».

Scrivi a Sara una riga quando parti, poi una ogni 30 minuti.

---

## Le righe da incollare (una per chat)

| Chat | LE TUE LEZIONI |
|---|---|
| **R-CHIM** | Chimica applicata e nobilitazione dei materiali per i prodotti della moda (Prof.ssa Caputi), lezioni dispari: `moda-chimica-III-IV-lez01`, `lez03`, `lez05`, `lez07`, `lez09`, `lez11`. Sigla: `kit/sigle/Sigla_Chimica_moda_15s.mp4`. |
| **R-ARTE** | Storia dell'arte V: `storia-arte-V-lez01`, `lez02`, `lez04`, `lez07`, `lez11`, `lez15`, poi `lez05` (testi già approvati da Sara l'11/11). |
| **R-MODA** | Moda: `moda-laboratori-III-IV-lez01`, `lez02`, `lez5`; `moda-tecnologie-III-lez06`, `lez07`, `lez08`; poi `moda-economia-III-IV-lez02` (67 min, solo da dividere in 2 Parti). |
| **R-ALB** | Alberghiero: `alb-alimentazione-III-IV-lez01`, `lez02`, `lez03` (consegnate ma non dichiarate PRONTE: controlla, dividi sopra i 60 min, dichiara); poi `alb-cucina-III-IV-lez05`; poi `storia-III-lez03` (70 min, da dividere in 2 Parti). |
