# SCHEDA TECNICA DELLA VIDEOLEZIONE (modello: Spagnolo Lez. 1 + aggiunte approvate) · 18/11/2026
Fonti: canovaccio di montaggio di Spagnolo Lez. 1 (v9), brief tecnico 01/11, brief approvato 31/10, decisioni di Sara fino al 18/11.
Ogni videolezione contiene **tutti** questi pezzi, **in quest'ordine**, con questi tempi e questa grafica. Fotogrammi di riferimento: `scambio/mazzotti/MODELLO_Spagnolo_schede.jpg`.

## A. Sequenza dei pezzi
| # | Pezzo | Durata | Grafica | Audio |
|---|---|---|---|---|
| 1 | **Sigla della materia** | 15 s | `kit/sigle/Sigla_<Materia>_15s.mp4` (fondo nero). Negli ultimi 2 s e nei primi 3 s dopo: **avviso di copyright** in basso al centro, bianco, 24 px | musica della sigla, sfuma |
| 2 | Dissolvenza | 1,0–1,8 s | morbida, nessun lampo | `trans.wav` |
| 3 | **Copertina + introduzione** | 2–4 min (tempo del docente) | fondo **bianco**: logo Telesio in alto a sinistra; riga «MATERIA · VIDEOLEZIONE» (Figtree Bold maiuscolo spaziato, blu); titolo (Bricolage 800, blu notte) con barretta; card **«ARGOMENTI»** con l'elenco; riquadro del prof **solo se parla** | voce di benvenuto (Kore) + docente |
| — | **Per OGNI argomento (4a–4g):** | | | |
| 4a | **Titolo dell'argomento** | 4 s | scheda **blu scura animata** «ARGOMENTO 0N / N», titolo grande bianco, chip con 2–3 parole chiave, barra di avanzamento | `titolo.wav` |
| 4b | **Docente + slide** | tempo del docente (mai tagliato a metà frase) | slide **bianche**: riga «0N · NOME ARGOMENTO», titolo + barretta, card con la **card in corso evidenziata in giallo** a tempo con la voce (±1,5 s); **riquadro del prof 4:3** in alto a destra (≈410×308 px, x≈1428 y≈146), angoli arrotondati, **ombra grigia morbida**; **fascia gialla** inclinata −3° con nome (2 righe) sempre visibile; **pannello «PAROLE CHIAVE»** sotto il riquadro (aggiunta approvata); piè «MATERIA · Prof. …» e «Pagina N» | docente (audio pulito del kit) |
| 4c | Approfondimenti animati | 40–60 s ciascuno, dove servono | slide bianche animate; Letteratura: **fettine HD del libro** con la fettina in corso evidenziata | voce Kore |
| 4d | **Mappa del prof** | 40–60 s | mappa del prof (release) impaginata con la nostra grafica, nodi che compaiono a tempo con la voce | voce Kore |
| 4e | **Pillola di ripasso** (OBBLIGATORIA) | **13–14 s** | scheda **blu scura**: «PILLOLA DI <MATERIA>», «RIPASSO» grande, argomento in azzurro, **onda audio animata**, riga con la frase della voce | `repaso.wav` all'inizio + voce Kore |
| 4f | **Schema guidato di ripasso** | **≈45 s + 3 s fermo** | slide **bianca**: schema/tabella, righe evidenziate in giallo una alla volta a ritmo della voce; poi 3 s di schema fermo senza voce | voce Kore (pause per ripetere) |
| 4g | **Scheda Quiz** | **4–5 s**, poi il video si ferma | scheda **blu scura animata**: «PAUSA DEL VIDEO · QUIZ», «Quiz N», argomento in giallo, riquadro «5 domande · per continuare almeno l'80%», «Rispondi · premi Check · poi Continua», **pulsante play** | `quiz.wav` a +0,5 s |
| 5 | **Glossario** | 40–70 s | slide bianca: parole chiave con definizione, evidenziate a tempo | voce Kore |
| 6 | **Riepilogo finale** | 12–35 s | scheda **blu scura**: «RIEPILOGO / FINALE», elenco numerato degli argomenti | voce Kore |
| 7 | **Finale** | 5 s | `kit/sigle/Sigla_finale_5s_con_avviso_diritti.mp4`: fondo nero, «GRAZIE PER L'ATTENZIONE», logo bianco | `finale.wav` |
Fuori dal video (nella pagina): **verifica finale** (10 domande dall'Excel del prof), **compiti** (PDF del prof), PDF slide A4 orizzontale **identico al video** (senza riquadro), PDF mappe del prof, sottotitoli `.vtt`.

**Le schede blu (4a, 4e, 4g, 6) si fanno SOLO con `scambio/strumenti/schede_spagnolo.py`** (programma originale di Spagnolo, scala 1.0).

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
Per ogni pezzo della tabella A: presente sì/no, minuto di inizio, durata misurata. Poi: sha256 · fotogrammi · LUFS e picco · jingle a ogni titolo, pillola e quiz · `trans` a ogni cambio · `freezedetect` · un fotogramma di ogni tipo di scheda accanto a quello di Spagnolo · sottotitoli riletti · PDF slide = video.
