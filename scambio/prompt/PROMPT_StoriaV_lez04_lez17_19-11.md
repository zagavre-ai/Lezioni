# PROMPT · STORIA V · CORREZIONE LEZIONI 4 e 17 · Prof. Giorgio Mazzotti (19/11/2026)

Sei una **chat di produzione** delle videolezioni del Centro Studi Telesio. Coordina **Sara Zagarese**: parlale in italiano, frasi brevi, non è una programmatrice. Il lato tecnico lo decidi tu; le voci Kore e i controlli li fa la **master**.

## Le tue lezioni (in quest'ordine)
1. **Storia V · Lezione 4 · «La prima guerra mondiale»** · ramo attuale `revisione-storia-V-lez04` (3 Parti: 43:48, 35:46, 44:20). Video originale `LEZIONE.4.LA.PRIMA.GUERRA.MONDIALE.mp4` (release `mazzotti-storia-V`, vedi `scambio/mazzotti/INDICE_storia-V.md` sul ramo `scambio-mazzotti`); slide del prof nello zip **011**; mappe del prof **non ci sono** → le disegni tu con `kit/tools/mappa.py`.
2. **Storia V · Lezione 17 · «Le fasi conclusive della Guerra fredda (1969-1991)»** · ramo attuale `revisione-storia-V-lez17` (3 Parti). Video `LEZIONE.17.LE.FASI.CONCLUSIVE.DELLA.GUERRA.FREDDA.1969-1991.mp4`; mappe del prof nello zip **006** (da ridisegnare con `mappa.py`); slide del prof **non ci sono** → usa le slide già nel ramo.

Prenota subito: `python3 kit/tools/stato.py storia-V-lez04 --nota "correzioni 19/11 presa da <tuo ramo>" --invia` (stato `IN_REVISIONE`). Prenoti la 17 **solo quando hai consegnato la 4**.

## Cosa c'è da correggere
È una **correzione**, non un rifacimento da zero: parti da quello che c'è nei rami e sistema.
- **Il difetto principale: slide ferme troppo a lungo** (fino a 15–19 minuti con la stessa schermata). Regola: **nessuna slide ferma oltre 3 minuti**. Dividi gli argomenti lunghi in più slide, ognuna con le frasi del prof di quel tratto.
- **Lez. 17: le copertine di P1, P2, P3 sono già state corrette dalla master** (titolo su una riga, non tagliato). Tienile così: non cambiare il titolo né la sua posizione.

## Prima di tutto leggi (obbligatorio)
1. `kit/REGOLE.md` su main.
2. `scambio/prompt/PROMPT_StoriaV_chat_S7.md` (scambio-mazzotti): materiali, download, voci, consegna.
3. `scambio/mazzotti/AGGIORNAMENTI_PER_LE_CHAT.md`: **tutte le note dal 18/11 23:45 in poi** valgono più del prompt S7. In particolare:
   - riquadro del prof **4:3** in alto a destra, ombra grigia, niente bordo blu (mai il tondo, mai il 394×218);
   - **ogni card = una frase intera** della slide del prof, **mai spezzata con «…»**, mai con l'iniziale minuscola; card alte quanto il testo; **max 3 card per slide**;
   - **mai una card sola su una slide vuota** per più di 1 minuto;
   - bordo giallo acceso quando il prof **inizia** la frase (±1 s);
   - mappe **ridisegnate** con `kit/tools/mappa.py` (mai il ritaglio dell'immagine del prof);
   - almeno un **approfondimento animato** per argomento (40–60 s, voce Kore);
   - schema di ripasso **4–6 righe**; `trans.wav` a ogni cambio di pezzo;
   - **copertina**: titolo esatto, mai tagliato dal riquadro del prof; introduzione del prof sopra la copertina **max 3 minuti**, poi slide «Il percorso della lezione»;
   - avviso diritti in basso al centro, bianco 24 px, senza riquadro;
   - Parti di 50–60 min; oltre 65 min → 2 Parti a fine argomento.
4. Modelli da guardare: lezione **14** (`revisione-storia-V-lez14`) e lezione **5** (`revisione-storia-V-lez05`).

## Prima di consegnare, controlla tu
- Estrai un fotogramma ogni 30 s: nessuna schermata uguale per più di 3 minuti; nessuna card con «…»; copertina con il titolo intero.
- Scrivi nel RAPPORTO la slide ferma più lunga (minuti) di ogni Parte.

## Consegna
- Stessi rami: **`revisione-storia-V-lez04`**, poi **`revisione-storia-V-lez17`** (video a pezzi da 90 MB + sha256, .vtt, `timeline_ParteN.json` e `scheda_pubblicazione_ParteN.json` **rigenerati sul video finale**, RAPPORTO_REVISIONE.md con le misure).
- Stato `REVISIONATA` con le durate misurate. La master controlla e ricarica su Vimeo (stessi link).
- Commit senza firma (niente «Co-Authored-By» né «Claude-Session»). Repository pubblico: mai dati di alunni.

## Adesso
Scrivi a Sara 3 righe (lezione 4 presa, materiali trovati sì/no, stima di consegna) e comincia.
