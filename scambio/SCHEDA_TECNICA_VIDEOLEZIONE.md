# SCHEDA TECNICA DELLA VIDEOLEZIONE (modello: Spagnolo Lez. 1 + aggiunte approvate) · 18/11/2026
Fonti: canovaccio di montaggio di Spagnolo Lez. 1 (v9), brief tecnico 01/11, brief approvato 31/10, decisioni di Sara fino al 18/11.
Ogni videolezione contiene **tutti** questi pezzi, **in quest'ordine**, con questi tempi e questa grafica. Fotogrammi di riferimento: `scambio/mazzotti/MODELLO_Spagnolo_pezzi.jpg` (ogni pezzo con il suo nome) e `MODELLO_Spagnolo_schede.jpg`.

## A. I pezzi, uno per uno (misurati sul video finale di Spagnolo Lez. 1)
Riferimento visivo con il nome di ogni pezzo: **`scambio/mazzotti/MODELLO_Spagnolo_pezzi.jpg`**. Le schede blu si fanno SOLO con `scambio/strumenti/schede_spagnolo.py` (scala 1.0): accanto a ognuna c'è la riga esatta da usare.

**1 · Sigla** — 15 s. File `kit/sigle/Sigla_<Materia>_15s.mp4` (fondo nero, musica). Negli ultimi 2 s + primi 3 s dopo: avviso di copyright in basso al centro, bianco, 24 px. Poi **dissolvenza 1,0–1,8 s** con `trans.wav`.

**3 · Copertina + introduzione** — tempo del docente (2–4 min). Fondo bianco. In alto a sinistra logo Telesio; sotto, «<MATERIA> · VIDEOLEZIONE» (Figtree Bold, maiuscolo spaziato, blu Telesio); titolo della lezione (Bricolage 800, blu notte, ~64 px) con barretta blu; card bianca con ombra leggera, etichetta «ARGOMENTI» e l'elenco puntato degli argomenti (2 colonne se servono). Riquadro del prof in alto a destra **solo mentre il prof parla**. Prima del prof: **voce di benvenuto** Kore (es. «Benvenuti alla lezione di Storia. Oggi parliamo di … Il professor Giorgio Mazzotti ci guida attraverso N argomenti.»).

**Per OGNI argomento, in quest'ordine (4a → 4g):**

**4a · Titolo dell'argomento** — **4 s** (3,6–4,9). Scheda blu scura animata: in alto **«ARGOMENTO 0N / N»** (arancio, maiuscolo spaziato, lettera per lettera); **titolo dell'argomento** grande bianco su 1–2 righe; linea sfumata arancio→azzurro; **chip** in vetro con 2–3 parole chiave o un esempio (es. «el chico → la chica»); in basso **barra di avanzamento** (N trattini, quelli fatti pieni); numero gigante trasparente sullo sfondo. Suono: `titolo.wav` all'inizio. Nessuna voce.
`{"type":"title","num":"0N","total":N,"lines":["riga 1","riga 2"],"ex":"parole · chiave","fs":128,"lineY":720,"dur":4}` (una riga sola: `"fs":150,"lineY":600`).

**4b · Docente + slide** — tempo del docente, **mai tagliato a metà frase**. Slide bianca: «0N · NOME ARGOMENTO» in alto (Figtree Bold, blu), titolo della slide (Bricolage 800) con barretta, card/tabelle; la **card della frase in corso** ha bordo giallo e numero su pallino giallo (le altre bordo grigio chiaro), a tempo con la voce del prof (±1,5 s). **Riquadro del prof 4:3** in alto a destra (~410×308, x≈1428 y≈146), angoli arrotondati, ombra grigia morbida; **fascia gialla** inclinata −3° con «Nome Cognome» (Bricolage 800) e sotto «PROF. DI <MATERIA>» (maiuscolo piccolo); sotto la fascia il **pannello «PAROLE CHIAVE»** (aggiunta approvata). Piè: «<MATERIA> · Prof. Giorgio Mazzotti» a sinistra, «Pagina N» a destra. Mai contenuti sotto il riquadro.

**4c · Approfondimenti animati** — 40–60 s ciascuno, dove servono. Slide bianche animate con voce Kore; titolo della slide come 4b, niente riquadro del prof. In Letteratura: **fettine HD del libro**, fettina in corso evidenziata.

**4d · Mappa del prof** — 40–60 s. La mappa del prof (release) impaginata con la nostra grafica; i nodi compaiono a tempo con la voce Kore («Ecco la mappa di … Primo ramo: …»).

**4e · Pillola di ripasso — INTRODUZIONE BLU** (OBBLIGATORIA) — **14 s**. Scheda blu scura: in alto **«PILLOLA DI <MATERIA>»** (arancio, spaziato; Spagnolo: «Pillola di grammatica»); **«RIPASSO»** gigante bianco (Spagnolo: «REPASO»); sotto, **nome dell'argomento** in azzurro; **onda audio** animata (barre azzurre) che si muove con la voce; in basso riquadro in vetro con **la frase che la voce sta dicendo**. Audio: `repaso.wav` all'inizio, poi **voce Kore che ANNUNCIA il ripasso** in 1–2 frasi (es. «Ripassiamo insieme la formazione del plurale.» / «Facciamo un riepilogo di quello che hai appena visto: …. Guarda lo schema e ripeti ad alta voce.»).
`{"type":"repaso","kicker":"Pillola di storia","big":"RIPASSO","topic":"<argomento>","caps":[[0.9,6.0,"frase 1"],[6.0,13.4,"frase 2"]],"dur":14}`

**4f · Pillola di ripasso — SCHEMA GUIDATO BIANCO** — **≈46 s** (≈43 s guidati + 3 s fermo). Slide bianca senza prof: etichetta-pillola **«PILLOLA DI <MATERIA>»** in alto, titolo dell'argomento (Bricolage 800) con barretta; **tabella o schema** con intestazione blu notte; **le righe compaiono e si evidenziano in giallo una alla volta** a ritmo della voce Kore, che dice la parola chiave di ogni riga e lascia ~2,5 s per ripetere; eventuale card «CONCORDANZA/NOTA» in fondo; ultimi **3 s schema fermo**, senza voce. Piè con la sola materia.

**4g · Scheda Quiz** — **5 s**, poi il video si ferma (quiz di 5 domande, soglia 80%). Scheda blu scura animata: in alto **«PAUSA DEL VIDEO · QUIZ»** (azzurro, spaziato); **«Quiz N»** grande bianco; sotto, **l'argomento in arancio**; riquadro in vetro **«5 domande · per continuare almeno l'80%»**; sotto «Rispondi · premi **Check** · poi **Continua**»; a destra **pulsante play** azzurro che pulsa; punto interrogativo gigante trasparente e puntini che salgono. Suono: `quiz.wav` a +0,5 s. Nessuna voce.
`{"type":"quiz","act":"Quiz N","topic":"<argomento>","tfs":84,"pts":"5 domande · per continuare almeno l'80%","dur":5}` (argomento lungo: `tfs` più piccolo, non deve toccare il play).

**5 · Glossario** — 40–70 s. Slide bianca «GLOSSARIO · PAROLE CHIAVE», parole chiave con definizione, evidenziate a tempo con la voce Kore.

**6 · Riepilogo finale** — 12–35 s (tempo della voce + 1,7 s). Scheda blu scura: in alto «<MATERIA> V» (arancio, spaziato); **«RIEPILOGO»** bianco gigante e sotto **«FINALE»** arancio; a destra l'**elenco numerato degli argomenti** in card di vetro che entrano una alla volta; sotto il titolo una frase («Ripassiamo insieme ciò che abbiamo imparato.»). Voce Kore che ricapitola argomento per argomento.
`{"type":"final","kicker":"Storia V","l1":"RIEPILOGO","l2":"FINALE","items":[["Argomento 1",""],…],"sub":"Ripassiamo insieme ciò che abbiamo imparato.","dur":<voce+1.7>}`

**7 · Finale** — 5 s. `kit/sigle/Sigla_finale_5s_con_avviso_diritti.mp4` (nero, «GRAZIE PER L'ATTENZIONE», logo bianco, avviso diritti) + `finale.wav`.

Fuori dal video (pagina della lezione): **verifica finale** (10 domande dall'Excel del prof), **compiti** (PDF del prof), PDF slide A4 orizzontale **identico al video** (senza riquadro), PDF mappe del prof, sottotitoli `.vtt`.

## B. Standard tecnici
- Video 1920×1080, 30 fps, H.264 (`-preset veryfast -crf 19`, keyint 60), audio AAC 48 kHz.
- Parlato **−16 LUFS ±2**, picco **≤ −1 dBTP**; voci narranti allo stesso livello del docente.
- **Transizioni:** `trans.wav` + dissolvenza breve (0,3–1 s) a **ogni** cambio di pezzo; mai tagli secchi; nessun lampeggio.
- **Nessun silenzio > 3 s**; **nessun fermo del prof ≥ 1 s**; sincronia labbra ≤ 0,04 s.
- Una **Parte** dura 50–60 minuti; se la lezione è più lunga si divide **alla fine di un argomento**.
- Impaginazione: margini 80 px; niente contenuto a destra di x 1473 quando c'è il prof; testo minimo 28 px; tabelle **mai spezzate**; testo fermo almeno 1,5 s.
- Font: solo **Bricolage Grotesque 800** (titoli) e **Figtree** (testo; Figtree Bold per etichette e piè). **Niente DM Mono.**
- Colori: blu notte #0B1530, blu Telesio #2060AF, giallo #FFE600 solo per evidenziare; fondo bianco per le slide.
- Correzione immagine del prof e catena audio: quelle del kit (brief approvato §5).
- Mai il numero della lezione nel video. Nessun marchio di terzi.

## C. Controllo prima della consegna (nel rapporto, con i minuti)
Per ogni pezzo della sezione A (1, 3, 4a–4g per ogni argomento, 5, 6, 7): presente sì/no, minuto di inizio, durata misurata. Poi: sha256 · fotogrammi · LUFS e picco · jingle a ogni titolo, pillola e quiz · `trans` a ogni cambio · `freezedetect` · un fotogramma di ogni tipo di scheda accanto a quello di Spagnolo · sottotitoli riletti · PDF slide = video.
