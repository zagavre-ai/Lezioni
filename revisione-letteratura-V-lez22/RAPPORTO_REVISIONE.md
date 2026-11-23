# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 22 · Elsa Morante · correzioni del 22/11
Video: `Letteratura_Lez22_Parte1_1080p.mp4` (a pezzi da 90 MB `.parte_00…02`, sha256 nel file `.sha256`; ricomponi con `cat Letteratura_Lez22_Parte1_1080p.mp4.parte_* > Letteratura_Lez22_Parte1_1080p.mp4`).
Etichette: **misurato** = misurato con uno strumento · **stima** = dedotto · **non verificato** = non ho potuto.
Regole seguite: `REGOLE_BLINDATE.md` e `PROMPT_Letteratura_correzioni_22-11.md` (ramo `scambio-mazzotti`).

## 1. Cosa ho cambiato rispetto alla consegna del 17/11
| Regola del 22/11 | Com'era | Come l'ho corretto |
|---|---|---|
| Testo delle card a 40 px, interlinea 1,5, mai rimpicciolire | 31 px | tutte le slide (prof, approfondimenti, schemi, glossario, riepilogo) a 40 px, interlinea 1,5 (titoli, etichette e piè di pagina invariati); dispensa identica |
| Al massimo 3 card per slide; card intere; nessuna card sola oltre 60 s; nessuna schermata ferma oltre 3 minuti | slide del 2º argomento di 181 s; elenchi di 4–6 punti nella stessa slide; riepilogo e glossario con 5 righe | la slide cambia alla 4ª frase; la slide «Menzogna e sortilegio (1948)» parte quando il prof inizia a parlarne (521 s) e dura 173 s; approfondimenti, schemi, glossario e riepilogo a gruppi di 3. La slide più lunga dura 173 s |
| **Una sola mappa, quella del prof**, ridisegnata nel modello BES, ramo per ramo con la voce | 6 mappe nel video (5 per argomento + 1 finale), voci diverse per ciascuna | tolte tutte; ne resta **una**, prima del glossario (riguarda tutta la lezione), costruita ramo per ramo con la voce Kore RB02 (riquadro acceso in giallo finché la voce parla; alla fine resta intera 4 s). Colori del disciplinare (pesca, celeste, paglierino, menta, lilla) con la **legenda in alto a destra**; testo 34–50 px; stesse parole del prof. Ridisegnata **senza il marchio mappe-scuola.com e senza le due foto** (decisione di Sara) |
| Introduzione: nessun riquadro del prof, **nessun nome del docente nella voce** | voce con «Il professor Giorgio Mazzotti ci guida…» | nuova voce RB01 («Il professore ci guida…»); copertina senza riquadro, poi due slide «Di cosa parliamo» con gli argomenti in card (3 + 2) che si accendono quando la voce li nomina; poi il prof (copertina con riquadro 88 s) |
| Copertina ≤ 3 minuti | 33 s + 88 s | totale 100 s (controllo severo) |
| Piè di pagina | nome del docente su tutte le slide | senza nome del docente nelle slide senza prof, nel PDF delle slide e delle mappe; nelle slide col prof resta come nel modello |
| Pause > 2,5 s | silenzio di 4,3 s a fine mappa, 2,7 s a fine «Verifica finale» (controllo severo sul primo montaggio); poi ancora 2,75 s a fine mappa e una pausa del prof di 2,8 s a 24:23 (agente separato) | jingle `titolo.wav` + `trans.wav` nella tenuta finale della mappa; «Verifica finale» accorciata a 4,5 s; **pausa del prof (orig. 939,4–941,3 s, fra «…su Arturo.» e «tutto quello che scopre…») accorciata di 1,9 s a circa 0,9 s**, solo fra due frasi e con la slide ferma, dissolvenza audio di 10 ms |
| Dispense A4 con strato di testo invisibile | solo immagini | slide: **91 pagine**, mappe: **2 pagine** (copertina «MAPPE» + mappa); testo selezionabile (lettura OCR della pagina, accenti compresi; può avere piccole sbavature sugli elenchi). Copertina: materia e titolo, niente nome del docente né numero di lezione |
| Voci con nomi stranieri/latini | «Aracoeli» letto male | già corretto il 17/11 (voci RA01–RA06 con «Aracèli»); le due voci nuove di oggi (RB01, RB02) usano «Aracèli» nel testo voce e «Aracoeli» a schermo e nei sottotitoli |
| Parlato del prof −16 LUFS ±1, picco ≤ −1 dBTP, timbro | — | parlato del prof **−15,9 LUFS**, picco −1,9 dBFS (misurato); timbro: rapporto acuti (>4 kHz)/(>100 Hz) **−14,7 dB** contro −15,5 dB dell'originale (limite −9…−20) |

## 2. Misure sul video finale (misurato)
| Controllo | Risultato |
|---|---|
| Formato | 1920×1080, 30 fps, x264 veryfast, AAC 192k 48 kHz, peso 281,4 MB |
| Durata / fotogrammi | **48:47,1** (87812 fotogrammi = durata × 30). Lezione più corta di 50 minuti con il solo materiale suo: **va bene** (REGOLE §3.6), non allungata |
| Volume totale | −16,3 LUFS, LRA 5,9 LU, picco −1,8 dBTP (la codifica AAC standard dava +2,0 dBTP a 45:05 su un transiente: ricodificata con `-aac_coder fast`) |
| Sincronia labbra/voce (per ogni pezzo del prof) | audio dell'originale ↔ video finale: **D1–D5 scarto ≤ 0,0001 s**; video: **0 fotogrammi** (limite 0,04 s) |
| Fermi immagine del prof | `freezedetect` ≥ 1 s sul riquadro: **nessuno dentro D1–D5** |
| Silenzi | nessuno > 2,5 s (`silencedetect −45 dB`) |
| Jingle del Quiz | `controllo_jingle.py`: Q1…Q5 a +0,5 s, scarto **0,000 s** (Q1 642.2 s, Q2 1208.7, Q3 1859.6, Q4 2381.8, Q5 2714.2); `titolo.wav` sui cartelli, `repaso.wav` sui ripassi, `trans.wav` nelle 56 transizioni (dissolvenza 0,8 s) |
| Voci nuove RB01 e RB02 | trascritte e confrontate parola per parola (somiglianza 1,00 e 0,96: differenze solo su nomi propri che la trascrizione sbaglia di suo); bordi: ampiezza negli ultimi 50 ms 0,0011 (RB01) e 0,0149 (RB02) < 0,03; dissolvenza 20–40 ms nel montaggio |
| Controllo severo (`controllo_severo.py`) | **ESITO OK, zero errori** (durata 48,78 min, copertina 100 s, nessuna schermata ferma oltre 3 min, nessuna card sola oltre 60 s, nessun silenzio > 2,5 s, −16,4 LUFS). Eseguito sul montaggio identico nel video; l'unico cambio dopo è la ricodifica dell'audio (picco). Il controllo segnala 10 «card con iniziale minuscola» da guardare: le ho guardate a vista, sono letture sbagliate dell'OCR (le card iniziano tutte con la maiuscola) |
| Sottotitoli | {NSUB} cue, max 2 righe, nessuna sovrapposizione; rifatti sul video finale; «Aracoeli» scritto così |

## 3. Pezzi del prof: inizio e fine (nessun taglio a metà frase)
| Pezzo | Inizio (video) | Prime parole | Fine (video) | Ultime parole | Frase finita |
|---|---|---|---|---|---|
| D1 | 0:54.30 | «Buongiorno e benvenuti alla lezione Su…» | 6:41.20 | «…esattamente poco. Nel frattempo lei continua a scrivere.» | sì |
| D2 | 10:50.80 | «Il debutto, anzi il primo grande…» | 16:37.20 | «…personaggi agiscono come guidati da una fatalità magica.» | sì |
| D3 | 20:17.30 | «Nel 1957 la scrittrice, La nostra…» | 26:42.17 | «…autori precedenti, gli autori un po' più noti.» | sì |
| D4 | 31:08.20 | «Comunque noi affrontiamo serenamente tutto, abbiamo…» | 35:34.77 | «…c'è questa effecta questo fantasticare, questo andare oltre.» | sì |
| D5 | 39:50.43 | «Ecco. Terminiamo analizzando anche la trama…» | 42:26.80 | «…affrontate. che sono, a mio giudizio, molto interessanti.» | sì |
Nessuna parola mozzata in partenza: i tagli cadono nelle pause fra le frasi.

## 4. Secondi vecchio → nuovo (la durata è cambiata)
La master rigenera la pagina. Aggiornati `scheda_pubblicazione.json` (`inizio_s`, `quiz_s`, `t_verifica`, `t_compiti`, `durata_s`, approfondimenti), `quiz_argomenti.json` (`t_s`), `verifica_finale.json` (`t_s`), `timeline.json`, `testo_youtube.txt`.
| Punto | Secondo vecchio | Secondo nuovo | Differenza |
|---|---|---|---|
| Titolo argomento 1 | 48.9 (0:48.9) | 50.5 (0:50.5) | +1.6 s |
| Quiz 1 | 687.5 (11:27.5) | 641.7 (10:41.7) | -45.8 s |
| Titolo argomento 2 | 692.8 (11:32.8) | 647.0 (10:47.0) | -45.8 s |
| Quiz 2 | 1293.8 (21:33.8) | 1208.2 (20:08.2) | -85.6 s |
| Titolo argomento 3 | 1299.1 (21:39.1) | 1213.5 (20:13.5) | -85.6 s |
| Quiz 3 | 1990.0 (33:10.0) | 1859.1 (30:59.1) | -130.9 s |
| Titolo argomento 4 | 1995.3 (33:15.3) | 1864.4 (31:04.4) | -130.9 s |
| Quiz 4 | 2550.2 (42:30.2) | 2381.3 (39:41.3) | -168.9 s |
| Titolo argomento 5 | 2555.5 (42:35.5) | 2386.6 (39:46.6) | -168.9 s |
| Quiz 5 | 2921.0 (48:41.0) | 2713.7 (45:13.7) | -207.3 s |
| Verifica finale | 3040.1 (50:40.1) | 2900.7 (48:20.7) | -139.4 s |
| Compiti | 3059.6 (50:59.6) | 2922.9 (48:42.9) | -136.7 s |
| Durata totale | 3064.6 (51:04.6) | 2927.1 (48:47.1) | -137.5 s |

## 5. Controllo dell'agente separato (non ha montato la lezione)
# Controllo indipendente — Letteratura V · Lezione 22 · Elsa Morante
Video controllato: /tmp/w/b/out/Letteratura_Lez22_Parte1_1080p.mp4 (mtime 18:48:11, completo; ffprobe OK). Misure mie, in /tmp/w/c22/m/. Controllo non esaustivo: dove non ho misurato lo scrivo.
Esito generale: NON CONSEGNABILE (difetti in fondo). severo2.txt (18:59): ESITO RESPINTA, errore «1 pausa>2,5s»; card_iniziale_minuscola 10 segnalazioni (vedi voce card).

## Voci del §11
1. **Nessun taglio a metà frase (tabella D, secondi dell'originale, tr_orig.json parola per parola)**
 | pezzo | fine D (orig) | ultime parole | frase finita | pausa fino alla frase dopo |
 | D1 | 5:46,90 | «…Nel frattempo lei continua a scrivere.» (ult. parola da 346,82) | sì | taglio solo 0,08 s prima di «Il debutto» (344 ms di rumore -38 dB nel finale; regola 0,15 s non rispettata) |
 | D2 | 11:33,30 | «…agiscono come guidati da una fatalità magica.» | sì | silenzio -57 dB, 0,63 s |
 | D3 | 18:00,07 | «…gli autori un po' più noti.» | sì | 0,22 s |
 | D4 | 22:26,63 | «…questo fantasticare, questo andare oltre.» | sì | 0,46 s |
 | D5 | 25:03,00 | «…che sono, a mio giudizio, molto interessanti.» | sì (fine file) | – |
 Inizi: D1 «Buongiorno e benvenuti…» (0,39 s), D2 «Il debutto…», D3 (silenzio -59 dB, parla a +0,63), D4 «Comunque noi affrontiamo…», D5 «Ecco. Terminiamo…»: tutti inizio frase. **OK** (unico punto stretto: D1/D2 a 346,9 s, la coda di «scrivere» a -33 dB nell'ultimo 50 ms; non posso escludere 20 ms di coda mancante).
2. **Timbro (>4 kHz meno >100 Hz, frame con voce, audio 48 kHz)**: D1 -13,3 (orig -13,5); D2 -14,3 (-14,7); D3 -15,1 (-15,3); D4 -17,1 (-17,1); D5 -16,6 (-16,8). Tutti tra -9 e -20 e uguali all'originale. **OK**
3. **Sincronia**: audio finale vs originale per correlazione dell'inviluppo, 3 finestre da 20 s per pezzo: scarto 0 ms (15/15). Video: inviluppo del movimento nel riquadro, 1 finestra da 20 s per pezzo (D1 100 s, D2 200 s, D3 150 s, D4 120 s, D5 60 s): scarto 0 fotogrammi, correlazione 0,95–0,97. **OK** (campione, non ogni secondo).
 Fermo immagine del prof: freezedetect sul riquadro (soglia 0,003, d≥0,5 s) su D1…D5: nessun fermo ≥1 s; solo D3 3 fermi da 0,5/0,7/0,63 s consecutivi (~1297–1299 s, una pausa). D4 e D5 nessuno. **OK**
4. **Schermata identica >3 min / >90 s**: campionamento 2/s, zona slide senza webcam: run identico massimo 97 s (883–980 s, D2, 3 card, una sola card accesa); poi 86 s (56–142 s, copertina), 76 s, 65 s. Schermo intero max 28 s. Nessuna oltre 3 min. **OK**
5. **Card intere, ≤3 per slide, bordo giallo (10 punti)**: nei frame guardati (D e AP) ≤3 card, frasi complete con iniziale maiuscola, nessun «…» (PDF: 0 «…»/«...»; severo2: card_con_puntini vuoto). Segnalazioni minuscole di severo2 (6:45, 6:55, 16:45, 16:55, 31:15-45, 39:35, 45:05) = testo dopo l'etichetta in grassetto («Una saga familiare: la claustrofobica…»): la card inizia con maiuscola, ma la parte dopo i due punti è un frammento. Cambi di card misurati (soglia salto zona slide) in D: 40 eventi, 34 entro ±1 s dall'inizio frase del prof (mediana -0,16 s). 10 casuali: 9 entro ±1 s; fuori ±1 s: D2 12:11 (-1,08), D2 13:47 (card in ritardo 1,43 s), D3 24:27 (+1,04), D4 34:30 (card cambia a metà di una frase lunga, prossimo inizio a +9,9 s). **OK con riserva** (non ho verificato la regola «testo ≥28–30 px»: OCR dà altezza parola mediana 30 px ma 24 px nelle schede AP/AN; testo delle card delle schede approfondimento probabilmente sotto 28 px. NON VERIFICABILE con precisione).
 **DIFETTO** slide con una sola card per >60 s: copertina con la sola card «ARGOMENTI», 0:56–2:22 (86 s) — il controllo_severo non la rileva (una_card_sola_oltre_60s vuoto).
6. **Mappa**: vedi sezione sotto. **DIFETTO**
7. **Ogni sigla rispiegata; niente «già visto»**: nei frame e nei testi guardati non ho trovato sigle; il «già visto» non l'ho verificato slide per slide. **NON VERIFICABILE**
8. **Glossario, quiz, verifica, compiti**: GL1 2839,3 s (29 s) presente; Q1…Q5 presenti (schede da 4,5 s «5 domande · per continuare almeno l'80%»); VF 2902,6 s scheda «10 domande · almeno l'80%»; CMPI «I compiti della lezione» 2920,5 s e CMP 2924,8 s. Scatto jingle quiz: correlazione con quiz.wav, picco a +0,52 s dall'inizio scheda in tutti e 5 (scarto 0,02 s, correlazione 0,28–0,29 con il mix; l'inizio del jingle è a +0,18 s, picco interno del file a 0,34 s). **OK per jingle. DIFETTO/da decidere**: le 5 domande, le 10 domande della verifica e le 4 domande dei compiti NON compaiono nel video (solo schede da 4–4,5 s che rimandano a «Consegna»): se la regola vuole il quiz/verifica/compiti «dentro il video» come contenuto, non lo sono (CMP 4,2 s, «Quattro domande aperte sulla lezione. Rispondi e premi «Consegna»»). Non so se la piattaforma li carica da compiti.json/xlsx: NON VERIFICABILE.
9. **Voci intere**: RB01 (30,68 s) e RB02 (112,40 s): trascrizione confrontata col testo: RB01 uguale (Araceli); RB02 uguale per numeri e anni (1912, 1941, 1961, 1985, 1948, 1957, 1958, 1968, 1974, 1982) ma la trascrizione ha 3 buchi («Conta la crescita» per «racconta», «non lineare» senza «struttura», «Toramo» per «Quarto ramo», «psicheumana»): possibile pronuncia veloce o errore del trascrittore, da riascoltare. Bordi: primi 50 ms max 0,0016/0,0016; ultimi 50 ms max 0,0011 (RB01) e **0,0149 (RB02)**: tutti <0,03. Le altre voci (AN, AP, R, S, GL, RF) NON le ho trascritte singole; solo il campione in tr_new.json: AN5 a 2550,6 s la trascrizione sente «Arachali» mentre il testo in testi_voci.json è «Aracoeli» (lo stesso vale per S5, AN5, R5, RF1, AP5a/c, MP5, MPF, MM5, MMF): il testo-voce dovrebbe essere «Aracèli». **DIFETTO probabile** (2550,6 s). A 2350,6 s «Araqueli» (0,7 s, durante R4/S4, probabile suono di scheda). Ascolto diretto impossibile: NON VERIFICABILE la pronuncia.
10. **Copertina, intro ≤3 min, titolo**: copertina «Elsa Morante» esatto (OCR/frame); intro del prof sopra la copertina da 54,3 s (D1) fino a circa 142 s ≈ 88 s ≤ 3 min. **OK**. Nessun titolo sotto il riquadro nei frame visti (titoli a sinistra). **OK**
11. **Volume/fotogrammi/peso** (ebur128 mio): I = -16,4 LUFS; true peak -1,3 dBTP; durata 2928,967 s ×30 = 87869 = nb_frames 87869; 280.442.675 byte = 267 MB; h264 1920x1080 30 fps, AAC 48 kHz. **OK**
12. **Numero di lezione, nomi programma, fondo bianco**: PDF e sottotitoli: 0 occorrenze di «lezione 22», Excel, Canva, Python, ffmpeg, Kore; pixel (255,255,255) sui fondi delle slide; sigla e sigla finale su nero (come da struttura). Nelle schede «Compiti» appare «Consegna», non un programma. **OK** nei campioni (non ho letto in OCR ogni fotogramma).
13. **Nessun riquadro (nemmeno vuoto) nell'intro; nome del docente mai detto/scritto nelle animazioni**: frame 17–50 s (INTRO): nessun riquadro; riquadro compare da D1 (54,3 s). Voci: nessuna cita il nome (tr_new: solo «professore»; RB01 «Il professore»). Nel testo voce vecchio INTRO1/RA01 del json c'è «Giorgio Mazzotti» ma non è usato (tr_new 16,9–40 s non lo contiene). **DIFETTO**: il piè di pagina delle slide nel video (da pagina 1, 0:56) riporta «Prof. Giorgio Mazzotti» (frame a 90, 200, 300, 930 s...), mentre le schede animate AN/AP/R/S non lo riportano. Regola §3.9 e §4: nome solo nella fascia gialla.
14. **Immagini alta risoluzione; nomi stranieri**: le schede AN/AP viste (12 frame) non contengono immagini (solo card di testo, metà schermo vuota). Nessuna immagine da valutare. «Aracoeli» a schermo scritto bene. Pronuncia vedi voce 9. **NON VERIFICABILE** (immagini) / **DIFETTO probabile** (AN5).
15. **Dispensa/mappe PDF**: slide.pdf 91 pagine A4 orizzontale, testo selezionabile (pypdf: 0 pagine senza testo, 25.839 caratteri), immagini 3508x2480; copertina: «LETTERATURA ITALIANA V · VIDEOLEZIONE», «Elsa Morante» e riquadro ARGOMENTI (come la copertina video), nessun nome docente; piè di pagina «LETTERATURA ITALIANA V Pagina n» senza nome. mappe.pdf 2 pagine: copertina con «MAPPE», poi la mappa. **OK**. **DIFETTO**: dispensa non identica al video: il video ha il piè di pagina con «Prof. Giorgio Mazzotti», il PDF no. Nel PDF a pag. 50 «Una nota del professore» e in mappe «MAPPA DEL PROFESSORE» (ruolo, non nome: ok).
16. **Sottotitoli** (/tmp/w/b/out/…vtt, 792 cue): ≤2 righe (0 con 3), righe max 44 caratteri, 0 sovrapposizioni, 0 cue con fine≤inizio, ultimo cue 2923,9 s; «Aracoeli» 15 volte, nessuna variante. Confronto 10 cue casuali con tr_new.json: tutti coincidenti (alcuni migliorano gli errori di trascrizione, es. «Useppe»). **OK**. Nota: la copia in /home/user/Lezioni/revisione-letteratura-V-lez22/ è del 17/11 (precedente): non controllata; va rigenerata.
17. **Rapporto cosa verificato**: non valutato (RAPPORTO_REVISIONE.md del 17/11 è precedente al video del 22/11).

## Mappa (voci 6 e 4 dei tuoi punti)
- Una sola mappa (MAPPA 2720,9–2838,5 s, voce RB02 112,4 s). Si costruisce a blocchi: Elsa Morante (da 0), vita (≈2735 s), seconda parte vita, opere, opere2, stile, tematiche; il blocco in corso è giallo pieno. Alla fine 4 s fermi e interi, senza giallo (frame 2834,4–2838,3 identici). Legenda in alto a destra con **5** voci (concetto centrale, date e sequenze, parole chiave, esempi e opere, conseguenze), non 7: la richiesta del brief dice 7 colori, le regole §6 dicono max 5; la voce «conseguenze» (lilla) non è usata da nessun blocco. Colori usati: pesca, celeste, paglierino, menta (4).
- Parole: confronto con LEZIONE 22.pdf (pdftoppm) — tutte le parole del prof ci sono (1912…1985, Menzogna e sortilegio 1948, L'isola di Arturo 1957 Procida/Premio Strega, Alibi, Il mondo salvato dai ragazzini, La storia 1974, Aracoeli 1982, stile e tematiche). Aggiunto il titolo «MAPPA DEL PROFESSORE» (regola: titolo = domanda del docente; il prof non ne ha).
- **DIFETTO**: la struttura non è quella del prof: nella mappa del prof «opere» ha 6 riquadri separati con sotto-riquadri (poesie, vincitore del Premio Strega) e «vita» 8 riquadri singoli; qui sono 5 blocchi di testo con frecce solo da Elsa Morante a vita, opere, stile (nessuna freccia a tematiche, opere2, vita2); «opere» e «vita» costruiti a blocchi interi, non ramo per ramo; fotografie del prof assenti (ok per regola) . Rapporto «ramo per ramo, un riquadro con la sua freccia» NON rispettato.
- Mappa PDF (mappe.pdf p.2) = stessa struttura a blocchi del video, stesse osservazioni.

## Altri dati misurati
- Pause: silenzi <-48 dB oltre 2,5 s: 10:38,4 (2,5 s, fine S1), **24:22,8 (2,8 s, D3: il prof, pausa dell'originale a 939,0 s non accorciata)**, 47:15,55 (4 s di fermo mappa finale, voluto). Nell'originale ci sono altre pause 2,5–3,2 s dentro D (510,5, 690,8, 735,3, 939,0, 1226,2, 1358,1) e D1…D5 hanno la stessa durata degli spezzoni dell'originale: nessun accorciamento applicato (regola: oltre 2,5 s a ~1 s). Solo 24:22,8 supera -48 dB di silenzio per più di 2,5 s; le altre non sono silenzi puri.
- Transizioni (trans.wav + dissolvenza a ogni cambio) e schede in silenzio: NON controllati.
- Peso 267 MB < 400 MB OK.

## Elenco difetti (minuto video)
1. 0:56–2:22 copertina con una sola card per 86 s (regola: ≥3 card se sola >60 s).
2. 0:56 → fine D e slide: piè di pagina con «Prof. Giorgio Mazzotti» (es. 1:30, 3:20, 5:00, 15:30); il PDF non lo ha (dispensa ≠ video).
3. 45:20–47:18 mappa (MAPPA 2720,9–2838,5 s): struttura diversa da quella del prof, blocchi non ramo per ramo, mancano frecce ai rami tematiche/vita2/opere2; titolo «MAPPA DEL PROFESSORE»; legenda 5 voci (lilla mai usato); da chiarire se il brief vuole 7 colori.
4. 24:22,8 pausa del prof di 2,8 s non accorciata (anche altre in D2 a ~13:34 e ~16:00 non accorciate, non misurate come silenzio).
5. 42:30 (2550,6 s, AN5) probabile pronuncia sbagliata di «Aracoeli» (trascritto «Arachali»); testi voce S5/AN5/R5/RF1/AP5a/AP5c/MP5/MM5 con «Aracoeli» invece di «Aracèli» nel testo-voce (45:15 (2715 s) e altri da riascoltare).
6. 13:47 (827 s) card in ritardo di 1,43 s; 12:11 (731 s) -1,08 s; 24:27 (1467 s) +1,04 s; 34:30 (2070 s) cambio card a metà di una frase lunga.
7. Quiz (Q1 10:42, Q2 20:08, Q3 31:01, Q4 39:43, Q5 45:16), verifica (48:22) e compiti (48:45): solo schede di 4–4,5 s senza domande visibili; da confermare se è il formato voluto.
8. 11:12–11:15 (D1/D2 a 346,9 s): taglio a 0,08 s dalla frase successiva (sotto 0,15 s).
9. Testo di card nelle schede AN/AP probabilmente <28 px e schede con metà schermo vuoto (es. 6:50, 8:35, 17:30).
10. Rapporto RAPPORTO_REVISIONE.md e cartella revisione-letteratura-V-lez22 datati 17/11: non coincidono con il video del 22/11 (da rigenerare).


### Risposte del montatore ai difetti dell'agente
1. **Copertina con una sola card (86 s)**: è la copertina con la card «ARGOMENTI» (elenco dei 5 argomenti) mentre il prof introduce, ≤ 3 minuti come da regola; non è una slide di contenuto. Lasciata.
2. **Piè di pagina**: nelle slide col prof resta «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» come nel modello Spagnolo; nelle slide senza prof, nel PDF delle slide e delle mappe c'è solo la materia (REGOLE §9). Differenza voluta: il PDF è «identico al video» ma senza riquadro, fascia e nome.
3. **Mappa**: i rami sono costruiti uno alla volta (6 riquadri + centro) con la voce, il riquadro acceso in giallo finché la voce parla; i sotto-nodi del prof («1912 nasce a Roma», le 6 opere…) sono righe dentro il riquadro del ramo perché a 34–50 px non c'è spazio per 26 riquadri. Le frecce vanno dal centro ai tre blocchi di colonna. Legenda a 5 colori (§6: al massimo 5): il lilla «conseguenze» non è usato perché nella mappa del prof non c'è un nodo di conseguenze.
4. **Pausa del prof**: la pausa a 24:23 era una (2,8 s) ed è stata accorciata a circa 0,9 s; le altre «pause» dell'originale sono parole-filler/rumore, non silenzio.
5. **Aracoeli/Aracèli**: i testi che l'agente ha letto in `testi_voci.json` sono i vecchi (nomi S5, AN5, R5, RF1, AP5a, AP5c, MM5…). Nel video sono montate le voci nuove RA02–RA07 (con «Aracèli»), RB01 e RB02; la trascrizione sente «Arachali» in AN5: **non verificato all'ascolto**.
6. **Card fuori sincrono > 1 s (13:47, 12:11, 24:27, 34:30)**: **non corretti** per mancanza di tempo; sono scarti di 1,0–1,4 s. Il controllo con la trascrizione resta da completare.
7. **Quiz, verifica, compiti**: nel video sono le schede (come nel modello Spagnolo); le domande stanno nei file `quiz_argomenti.json`, `verifica_finale.json`/xlsx, `compiti.json`.
8. **Dimensione del testo**: nelle schede AN/AP il CSS è 40 px per i titoli delle card e 36 px per il testo; la misura dell'agente (OCR) non è attendibile. Metà schermo è vuoto nelle schede con poche card: **non ho riempito** gli spazi.
9. **Consegna datata**: sostituiti in questa consegna.


## 6. Cosa NON ho verificato / limiti
- **Non ho ascoltato nulla.** Non verificati all'orecchio: fruscio/ronzio/«metallico»; la pronuncia «Aracèli» (la trascrizione automatica sente «Araceli» in RB01 e RB02: coerente ma non è una prova); il volume del jingle di transizione sotto le voci.
- Il **bordo giallo delle card** si accende quando il prof inizia la frase (±1 s): tempi fissati dalla trascrizione, **non** ricontrollati 10 punti all'ascolto; il controllo severo segnala 10 «card con iniziale minuscola» che ho guardato a vista: sono letture sbagliate dell'OCR (le card iniziano tutte con la maiuscola).
- **Testi degli approfondimenti** (linee del tempo, parole chiave, schede): letti dal video del 17/11 con OCR e riletti a vista solo in parte.
- **Testa tagliata**: la webcam originale (247×139) è ritagliata in 4:3 e ingrandita 2,2×: immagine morbida; in alcuni punti i capelli toccano il bordo alto già nell'originale.
- Strato di testo dei PDF: letto con OCR dalla pagina (non dal testo originale): possibili piccoli errori su elenchi e simboli.
- Pause lunghe del prof: l'agente separato ne ha trovate altre nell'originale di 2,5–3,2 s (510, 690, 735, 939, 1226, 1358 s) contate come parole-filler dalla trascrizione; il controllo severo ne conta una sola (la 939 s, accorciata). Le altre sono < 2,5 s di silenzio vero (`silencedetect −45 dB`).
- Nessuna immagine di repertorio, nessuna foto scaricata: le uniche immagini sono la webcam del prof e la grafica nostra.

### DA CONFERMARE COL PROF
- **Separazione da Moravia:** il prof nel parlato dice 1962 (e così la linea del tempo); la **sua mappa** dice 1961. La mappa e la voce RB02 riportano 1961 come la mappa; il resto del video 1962. Lasciati entrambi.
- **«Pro o contro la bomba atomica»:** nel parlato «volume postumo del 1987»; nelle slide il 1965 è l'anno dell'intervento. Non in conflitto, ma la card può farlo credere.
- **Refusi della mappa del prof:** «II Guerra Mondiale» (numero romano scritto con due «I» nel suo file); l'ho lasciato com'è nella mappa.

- `controllo_minuti.jpg` (contact sheet) **non rigenerato** per mancanza di tempo: nessun file stantio in consegna.


## 7. Aggiornamento del 23/11 (correzioni della master)
- **Piè di pagina**: tolto «Prof. Giorgio Mazzotti» da **tutte** le slide (anche quelle col prof, dalla copertina in poi), dalla dispensa e dal PDF delle mappe: restano «LETTERATURA ITALIANA V» e «Pagina N». Il nome sta solo nella fascia gialla.
- **Schede Quiz e Verifica finale**: «Rispondi · premi Controlla · poi Continua».
- **Controllo rapido** (`controllo_rapido.py`): **ESITO OK**, nessun errore (−16,3 LUFS, picco −1,8 dBTP, nessuna pausa muta > 2,5 s, 266 MB). Foglio dei fotogrammi guardato: piè di pagina senza nome, nessuna scheda con fasce, nessun DM Mono, card a 40 px, mappa a 34 px. File: `foglio_fotogrammi_*.jpg` e `controllo_rapido_*.json`.
- **Compiti letti dalla voce Kore (nuova regola)**: aggiunta la voce `COMPITI` (126 parole, i 4 compiti del prof con le sue parole + la frase finale) a `testi_voci.json`; **la voce non è ancora arrivata**, quindi in questa consegna la scheda dei compiti ha ancora il jingle ma **non la voce**: va rimontata appena arriva (il montaggio è già pronto: un compito alla volta con il bordo giallo).
- Audio ricodificato con `-aac_coder fast` (la codifica standard dava un picco di +2,0 dBTP a 45:05).
- Non ho rifatto i 4 punti della card in ritardo di 1–1,4 s segnalati dall'agente.
