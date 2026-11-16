# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 13 (Svevo) · PRIMA VERSIONE
Prof. Giorgio Mazzotti · chat di revisione 13 · 16/11/2026 · stato: IN REVISIONE (non ancora corretta)

**Misurato** = ricavato da file/strumenti. **Stima** = valutazione mia.

## 1. Che cosa ho verificato finora
- Video montato ricomposto dai pezzi, **sha256 OK** (Parte 1: 52:24 = 3143,9 s; Parte 2: 53:20 = 3200,3 s). Misurato.
- Originale del prof scaricato (82 min, 1092×614). La webcam nell'originale è **fissa a x 815–1061, y 339–477 = 247×139 px** (misurato su 5 fotogrammi, da 400 s a 4000 s): è più stretta del solito, quindi il 4:3 è un ritaglio 185×139 ingrandito ~2,2×.
- **Trascrizione completa** (parola per parola) di Parte 1 e Parte 2 con `trascrivi.py`: letta tutta la voce narrante.
- Contact sheet di entrambe le Parti (1 fotogramma ogni 30 s).
- Dispensa (84 pagine A4 orizzontale), compiti, test, mappe, sottotitoli: controllati a campione/confronto con i file del prof.
- **Non ancora fatto:** OCR di tutte le slide, ascolto a 3 punti del rumore, confronto pagina per pagina PDF slide / fotogrammi, tabella pagine HD (zip `Lez13_ingrandita` scaricato, non ancora confrontato), sincronia labbra sul nuovo riquadro.

## 2. Problemi trovati
| # | Minuto | Tipo | Com'è | Correzione prevista |
|---|---|---|---|---|
| 1 | P1 e P2, tutti i pezzi del prof | visivo | il prof è nel **tondo** (centro 1656,300, r 153) con nome in nero sotto, senza fascia gialla | riquadro **4:3 412×308** a x1428 y146, angoli arrotondati, ombra grigia, fascia gialla −3° «Giorgio Mazzotti / PROF. DI LETTERATURA ITALIANA», correzione immagine del kit. **In corso: Parte 1 codificata, Parte 2 da fare** |
| 2 | ovunque c'è il piè di pagina | testo | «LETTERATURA ITALIANA · Prof. Giorgio Mazzotti»; il modello vuole «LETTERATURA ITALIANA **V** · Prof. Giorgio Mazzotti» | ritocco del piè di pagina nelle slide (e nel PDF slide) |
| 3 | P1 0:18–0:56 (INTRO1), P1 27:07–28:10 (ripasso S1) e altri ripassi | testo | **sottotitoli assenti** sulla voce narrante (0 sottotitoli in 0–56 s e 1627–1690 s); presenti solo sul prof e su parte delle animazioni | rifare il .vtt con la trascrizione e i termini corretti |
| 4 | P2 .vtt (es. «analitico delinetto»), P1 .vtt | testo | refusi nei .vtt: «analitico delinetto», «Linetto»; da rileggere tutti | rilettura completa |
| 5 | P2 0:00 | struttura | **La Parte 2 non si apre con il ripasso della Parte 1** (regola 2 del kit). Nel montato non ci sono IN2/RIP; i due testi sono in `testi_voci_P2.json` ma **le voci non sono mai state generate** (non esistono `IN2.wav`, `RIP.wav`) | aggiungo IN2 e RIP a `testi_voci.json` sul ramo voci e le inserisco appena arrivano |
| 6 | P1 24:29 (AN2) e 25:28 (AN1b): «Chi vince spesso si è solo adattato ed è più svuotato degli altri» | audio | **frase ripetuta** a 60 s di distanza | taglio una delle due se la sincronia lo permette, altrimenti lo segnalo |
| 7 | P1 38:42 (AN4) e 39:36 (AN4b) | audio | «il narratore in terza persona interviene per giudicare e smascherare le bugie» detto due volte | idem |
| 8 | P1 48:56 (AN6) e 49:44 (AN7b) | audio | «Zeno interrompe la cura / il dottore pubblica per vendetta» ripetuto | idem |
| 9 | P1 40:00 (AN4b) | audio | «Il successo con il pubblico però non arriva» fuori contesto dopo il tema della maschera | verifico sul testo della voce |
| 10 | P2 49:37 (AN4b) | testo | «Il lettore resta con la mano in bocca» (voce e slide) | verifico sul testo del prof e correggo se è un errore |
| 11 | P1 e P2, animazioni «MAPPA CONCETTUALE» (AN3, AN5, AN7, AN4, MF1, MF2) | contenuto | **le mappe nel video e il PDF `Mappe_letteratura-V-lez13.pdf` (6 pagine) sono nostre**, con 5 rami per argomento. La mappa del prof (`MAPPE/LEZIONE 13.pdf`) è **una sola**: «ITALO SVEVO» con vita, stile, tematiche, opere. Le regole dicono: mappe del prof, senza inventare | rifaccio `…_mappe.pdf` con la mappa del prof nella nostra grafica. **Nel video** vedi sotto: serve una decisione |
| 12 | P1, P2 | grafica | animazioni su **fondo blu notte** («SCHEDE», «LINEA DEL TEMPO», ripasso con onda audio) diverse dal modello Spagnolo (fondo bianco) | da valutare (vedi §3) |
| 13 | P1 | contenuto | la timeline «Linea del tempo» e altre animazioni citano date/fatti non presenti nelle slide del prof | da controllare con OCR nella fase 2 |
| 14 | P2 | pagine libro | nel D4 (prof) ci sono pagine del libro in HD («fettine») dai testi T4, T5, T6, T9: **da verificare** leggibilità (rigo ≥ 26–30 px), evidenziazione e sincronia con la voce; dal contact sheet alcune sono pagine intere con testo minuto | confronto con `Lez13_ingrandita.zip`, tabella nel rapporto finale |

Controllati e **corretti** (nessun errore): compiti (4 esercizi, testo identico al PDF del prof), test finale (10 domande, uguali all'Excel del prof), sha256, fotogrammi/durata dei due pezzi.

## 3. Decisioni che mi servono (una riga ciascuna)
1. **Mappe nel video (#11):** togliere le 6 animazioni di mappa inventate accorcerebbe la Parte 1 a circa 49 min (**sotto i 50**). Propongo: tengo le animazioni ma **sostituisco la mappa dell'ultimo ripasso con la mappa del prof**; le altre restano finché non decidi. Se preferisci toglierle tutte, dimmelo.
2. Voci nuove (IN2, RIP): servono 10–30 min dalla master; intanto lavoro sul resto.

## 4. Piano e tempi (stima)
- Riquadro 4:3 Parte 1: codificato; Parte 2: ~60 min di elaborazione. 
- Footer + sottotitoli + PDF slide/mappe: ~60 min.
- Ripasso Parte 1 in apertura della Parte 2 e tagli delle frasi ripetute: dopo l'arrivo delle voci.
- Ricodifica finale con `finale_a_pezzi.py` (CRF 19, <400 MB) e `controllo_finale.py`: ~60 min per Parte.
- **Stima totale: consegna entro 5 ore dall'inizio** (lezione con pagine del libro).
