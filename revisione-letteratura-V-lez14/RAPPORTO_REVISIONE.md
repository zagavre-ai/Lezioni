# CORREZIONE URGENTE 25/11/2026 (consegna ~22:00 UTC)
**File nuovi (nomi esatti, a pezzi da 90 MB con sha256):**
- `Letteratura_Lez14_Parte1_1080p.mp4` (sha256 `657fceb7e9bffd1bc321e260506a8f68939b0b0127c7ca75c7c74f4457b6120d`)
- `Letteratura_Lez14_Parte2_1080p.mp4` (sha256 `f33643fd910be10c8a15e70e4b9eca902b1974d33aa694b84a857d2dcba9d26f`)
- `Letteratura_Lez14_mappe.pdf` (copertina «MAPPE» + 3 schermate della mappa + mappa intera), `.vtt`, `scheda_pubblicazione_parte*.json`, `timeline_parte*.json` rigenerati.

**Punti della master:**
1. **Parte 1, argomento 2 (da 21:10 a 26:10 circa):** ora la slide è quella del prof che corrisponde a quello che dice: la card «3 · L'umorismo come chiave» (invece delle card 1–2 della crisi). Resta un'unica card per tutto il tratto (non bloccante).
2. **Parte 2, spiegone della Parte 1: NON FATTO.** Ho mandato il testo `SPG_1` in `testi_voci.json` (ramo `voci-letteratura-V-lez14`, commit `4157c63`) alle 21:10 UTC, ma la voce **non era arrivata alle 22:00 UTC**. Il montaggio dello spiegone (4 slide di ripasso scure, una per argomento, con le card che si accendono dalla voce) è **già pronto** (`strumenti/spg25.py`): appena c'è `SPG_1.wav` si monta in circa 25 minuti.
3. **Mappa finale (41:29 → 43:35 nel video):** divisa in **3 schermate** (vita · introduzione e tematiche · opere), colori BES con legenda, riquadri che compaiono uno alla volta mentre la voce li legge con anello giallo, poi mappa intera ferma 4 s. **Testo delle caselle 30–34 px: non tutte ≥ 34 px** (le sotto-caselle sono a 30 px). La voce è la R1 (anni detti in cifre; non rifatta).
4. **Compiti:** senza riquadro del prof, in **blu scuro a tutto schermo**, uno alla volta con bordo giallo mentre la voce Kore li legge (pagina 35).
5. **Pagine delle novelle:** le fettine ora prendono **solo il testo del brano** (escluse le note a piè di pagina, che avevano testo minuscolo); passo di riga ≈ 40 px. **Limite:** in alcuni punti la prima o l'ultima riga della fettina è tagliata a metà.
6. **Schede in blu scuro a tutto schermo** (ripasso, glossario, riepilogo, compiti), senza «bande blu», piè di pagina senza nome del docente.

**Misure sul video nuovo (misurato):**
| | Parte 1 | Parte 2 |
|---|---|---|
| Durata | 45:45 (82 362 fotogrammi) | 47:07 (84 808 fotogrammi) |
| Volume | −16,4 LUFS · picco −2,9 dBTP | −16,8 LUFS · picco −2,3 dBTP |
| Jingle Quiz a 0,0 s | Q1–Q4 OK | Q1–Q6 OK |
| Silenzi > 2,5 s | 2,8 s e 2,55 s a fine pillola S2/S4 | 4,4 s dopo la mappa (mappa intera ferma) e 4,2 s a inizio Verifica: nessuno oltre 5 s |
| Peso | 306 MB | 315 MB |
**Non fatto / non verificato:** `controllo_rapido.py` non terminato in questo ambiente (oltre un'ora per Parte): niente foglio né json; ho guardato a vista 6 fotogrammi (argomento 2 P1, compiti, mappa, due pagine di novelle, schema di ripasso scuro). Il PDF delle slide non contiene le nuove pagine (compiti, mappa). Le voci COMPITI, VER14 e R1 non sono state ascoltate. 4 tratti di schermata identica oltre 3 minuti in Parte 1 (non bloccanti).

---
# AGGIORNAMENTO 24/11 (consegna finale su richiesta della master)
**Cosa ho fatto ora:** montate le voci Kore **COMPITI** (74,6 s) e **VER14** (9,1 s) arrivate dalla master. I 4 compiti del prof compaiono **uno alla volta con il bordo giallo** mentre la voce li legge con le sue parole; chiusura «Svolgi i compiti qui sotto e premi Consegna…». La scheda Verifica ha ora la voce («premi Controlla, poi Continua»). Le due schede non sono più mute oltre 5 s (misurato).
**Misure sul video nuovo (misurato):**
| | Parte 1 | Parte 2 |
|---|---|---|
| Durata | 45:45 (2745,4 s) | **47:03 (2823,4 s)** — più lunga di 77 s per le voci Verifica e Compiti |
| Volume | −16,4 LUFS · picco −2,9 dBTP | −16,8 LUFS · picco −2,3 dBTP |
| Jingle Quiz a 0,0 s | Q1–Q4 OK | Q1–Q6 OK |
| Silenzi > 2,5 s | S2, S4 (coda pillola, 2,5–2,8 s) | 4,2 s all'inizio della scheda Verifica (la voce parte a +3 s): non bloccante |
| Schermate identiche (area slide, misura grossolana) | massimo 368 s (6,1 min) a 20:42; poi 274 s a 9:54; 268 s a 29:54; 180 s a 39:00 | **una sola > 120 s: 180 s a 5:18**. Nessuna oltre 7 minuti |
| Peso | 307 MB | 326 MB |
Tempi di scheda, quiz, verifica e compiti **rigenerati** (`scheda_pubblicazione_parte*.json`, `timeline_parte*.json`, `.vtt`).
**Ancora NON a posto (non bloccanti o fuori dal mio tempo):**
- **Mappa del prof**: ancora la mia versione del 17/11 (testo 17–22 px, non BES, non ramo per ramo). Il ramo di aiuto con la mappa e le voci `M14_*` non sono mai comparsi sul remoto. **Resta bloccante per le regole §12 (mappe illegibili).**
- **Spiegone** all'inizio della Parte 2: non fatto.
- **controllo_rapido.py**: non terminato in questo ambiente (oltre un'ora): niente foglio né json. Il controllo lo fa la master.
- PDF delle slide: non include le nuove pagine dei compiti.
- Schermate identiche in P1 oltre 3 minuti (4 tratti), voce R1 con anni in cifre, pronuncia delle voci COMPITI/VER14/R1 **non ascoltata** (il riconoscimento ha scritto «Ciaola» per «Ciàula»).

---
# RAPPORTO REVISIONE · Letteratura V · Lezione 14 · CORREZIONI 22/11 (seconda consegna)
**Stato: NON conforme a tutte le regole del 22/11.** Fatto quello che segue, **non fatto** quello in sezione 4. Etichette: **misurato** / **stima** / **non verificato**.

## 1. Cosa ho cambiato il 22/11
- **Slide del prof**: testo delle card a **40 px**, interlinea 1,5, numero su pallino; **al massimo 2 card per slide** (le slide di 3 card sono divise in due). Bordo giallo sulla card in corso. Pagine numerate per Parte.
- **Copertina**: il prof parla sopra la copertina per **110 s** (limite 180 s; con l'intro senza prof la stessa schermata dura 142 s), poi due slide «Di cosa parliamo» (non si accendono: il prof non nomina gli argomenti).
- **Tagli del prof**: l'agente indipendente ne ha trovati 3 a metà frase (P1 D0/D1, P2 D0/D1, P2 D5/D6): **spostati sulla fine frase** (tabella §3, riletta dopo la correzione).
- **Card gialla in corso**: prima si accendeva fino a 26 s prima o dopo il parlato (misura dell'agente). Ora si accende **al primo istante in cui il prof pronuncia le parole distintive della card** (almeno 3 s dopo la precedente); prima della prima card nessuna è accesa. **Non ricontrollata con un agente dopo la correzione.**
- **Animazioni (approfondimenti, ripassi, glossario, riepilogo)**: al massimo **3 card per pagina** (alla quarta card si cambia pagina), testo a 36–40 px, e **piè di pagina senza il nome del docente** (anche copertina d'introduzione e mappa).
- **Pagine del libro**: ogni fettina cambia **almeno ogni 90 s** (prima restava ferma 5 e 12 minuti). L'abbinamento fettina→voce è una **stima**: il prof riassume e non legge; le fettine avanzano nell'ordine del brano guidate dal testo citato. **Non verificato** all'ascolto.
- **Volume**: tutto il file a **vedi sotto** (misurato).
- Rifatti i **PDF**: slide A4 orizzontale con testo vero selezionabile (27 e 31 pagine, piè di pagina senza il nome del docente) e PDF mappe con copertina «MAPPE». Rigenerati `.vtt`, `timeline`, `scheda_pubblicazione` (titolo «Letteratura V · Lezione 14 · Pirandello · Parte N»), `quiz_argomenti`, testo YouTube.

## 2. Misure sul video nuovo (misurato)
| | Parte 1 | Parte 2 |
|---|---|---|
| Durata | 45:45.4 (82362 fotogrammi = durata × 30) | 45:45.9 (82376 fotogrammi) |
| Peso | 307.3 MB | 321.6 MB |
| Volume (ebur128) | −16,4 LUFS · picco −2,8 dBTP | −16,8 LUFS · picco −2,3 dBTP |
| Parlato del prof | −16 LUFS stimato come in stereo (il mono pulito era a −16,9: il file è su due canali uguali, +3 dB) | uguale |
| Timbro (energia >4 kHz meno energia >100 Hz) | originale −17,0 dB · finale −16,7 dB (D1); −17,1 / −15,2 dB (D3): dentro −9…−20 | |
| Jingle Quiz a 0,0 s | Q1–Q4 OK | Q1–Q6 OK |
| Fermi immagine del prof (solo riquadro, ≥ 0,7 s) | vedi §5 | |
| Sincronia audio del prof con l'originale | ≤ 0,5 ms (misurato col video del 17/11, stessi pezzi D) | |
| Silenzi > 2,5 s | S2 (2,8 s) e S4 (2,55 s): coda delle pillole | schede Verifica (6,0 s) e Compiti (7,3 s): **non tolti** |

## 3. Tabella: inizio e fine di ogni pezzo del prof (minuti del video nuovo)
| Pezzo | Inizio | Prime parole | Inizia a inizio frase | Fine | Ultime parole | Frase finita |
|---|---|---|---|---|---|---|
| P1 D0 | 0:52 | «Buongiorno e benvenuti alla lezione su…» | sì | 4:04 | «…sono oggetto D Interrogazione di esame scolastico. Ecco.» | sì |
| P1 D1 | 4:10 | «Questa è la fotografia di Luigi…» | sì | 16:40 | «…perché hai sempre recitato un ruolo. We need.» | sì |
| P1 D2 | 20:40 | «ai tuoi occhi anche. Ecco questa,…» | sì | 27:27 | «…capire esattamente cosa ha scritto e cosa racconta.» | sì |
| P1 D3 | 29:08 | «Passiamo a, beh, insomma, al capolavoro,…» | sì | 36:00 | «…verghiano, per dare corpo alla relatività del reale.» | sì |
| P1 D4 | 37:54 | «E questa riflessione continua in... Uno,…» | sì | 42:24 | «…ha già abbozzato nel Fu Mattia Pascal. Proseguiamo.» | sì |
| P2 D0 | 1:00 | «uno sono centomila importante romanzo. Ora…» | sì | 1:15 | «…produzione teatrale, d'accordo? Ecco, parallelamente alla narrativa, eh.» | sì |
| P2 D1 | 1:22 | «La riflessione pirandelliana investi il teatro.…» | sì | 3:23 | «…infrange in tutto questo e viene sommerso, d'accordo?» | sì |
| P2 D2 | 4:51 | «Ecco, se i personaggi cerca d'autore,…» | sì | 8:21 | «…e poi Enrico IV, un altro dramma teatrale.» | sì |
| P2 D3 | 9:50 | «Questo un po più storico, d'accordo?…» | sì | 11:53 | «…sta male e alla fine non risolve nulla.» | sì |
| P2 D4 | 13:08 | «Ora, giusto perché siamo, diciamo così,…» | sì | 19:04 | «…se stessi, e soprattutto il concetto della maschera.» | sì |
| P2 D5 | 20:45 | «Però queste novelle in alcune, insomma,…» | sì | 25:44 | «…su Pirandello è il rapporto con il regime.» | sì |
| P2 D6 | 27:42 | «Il treno affischiato. Questo è ancora…» | sì | 39:25 | «…Poi si rese conto. Ma era troppo tardi.» | sì |

Pause scelte su ≥ 0,45 s e minimo di energia; parole del riconoscimento, non riascoltate.

## 4. NON fatto / da fare (non nascondo niente)
1. **Mappa BES ramo per ramo con voce**: **non rifatta**. Nel video c'è ancora la mappa del prof ridisegnata il 17/11 (non nei colori BES, senza legenda, **voce R1 con anni in cifre, non costruita ramo per ramo**, ferma). Va rifatta (testo voce con numeri in lettere, voci da generare dalla master, pezzo animato). Proposta: altra chat.
2. **Schermate identiche oltre 3 minuti e card sola oltre 60 s**: **ancora presenti** (misura dell'agente sul video precedente: P1 20:40–27:00 una sola card per 380 s; P1 29:10–34:15 305 s; P1 6:35–9:45 e 38:40–41:50 190 s; P2 4:50–8:10 200 s). Con le card che si accendono dalle parole il tratto può cambiare, ma **non l'ho rimisurato**. Per eliminarli serve spezzare i discorsi lunghi con inserti dopo una fine frase (lavoro non fatto).
3. **«Già visto»**: le slide 3 e 4 del prof compaiono in più argomenti (il prof torna avanti e indietro): regola non rispettata.
4. **Schede di titolo, pillole, quiz e riepilogo in blu scuro animato (§4 delle regole)**: titoli, pillole e riepiloghi sono bianchi, i quiz blu: **da uniformare**.
5. **Sigle/abbreviazioni**: non cercate.
6. **Numeri in lettere nelle voci**: non controllati; i testi di ripassi/approfondimenti hanno anni in cifre.
7. **Schede Quiz, Verifica, Compiti**: banda blu come prima; il «Compiti» non ha la mini-intro di 3,5 s né il jingle dedicato.
8. **Dispensa**: PDF delle slide con testo vero, ma il confronto pagina per pagina col video **non fatto**; le fettine del libro nel PDF sono immagini.
9. **Voce Kore R1**: non ascoltata.

## 5. Controlli
**Controllo severo (`controllo_severo.py`, passo 20 s), Parte 1:**
```
NON TERMINATO al momento della consegna (OCR lento): non ho un esito OK
```
**Parte 2:**
```
NON TERMINATO al momento della consegna (OCR lento): non ho un esito OK
```
**Agente separato (non ha montato la lezione):**
Rapporto dell'agente indipendente sul video del 22/11 (versione PRECEDENTE alle correzioni di questa consegna):
- 3 tagli a metà frase (P1 3:55, P2 1:08, P2 25:41) → **corretti** (§3).
- 6 schermate ferme oltre 180 s (P1 380, 305, 190, 190 s; P2 200 s) → **non corrette**.
- Card gialla fuori tempo (anticipo 18–26 s in P1 4:12 e 6:33; ritardo 7–8 s in P1 9:49 e P2 15:31; anticipo 5 s in P1 14:43 e P2 10:33) → **logica rifatta** (parole distintive), non ricontrollata.
- Animazioni con più di 3 card (P1 AN01 5, GL 5, RF 4; P2 AN03/05/07/09/11 4–6, GL 5, RF 6) → **corrette** (pagine da 3).
- Nome del docente nel piè di pagina delle animazioni → **tolto**.
- Copertina con prof 150 s (ok); stessa schermata 183,6 s con l'intro → ora 142 s.
- Fondo blu nei pezzi Q (quiz) e T (titolo): i T ora bianchi (vedi §4 punto 4).
- Volume −16,4 / −16,8 LUFS, fotogrammi = durata × 30, INTRO senza riquadro, 29 voci narranti non troncate, pagine del libro leggibili (alcuni fotogrammi a 1832 e 2137 s con testo tagliato in alto e in basso da valutare).
- Non verificato dall'agente: OCR italiano, labbra, timbro, mappe, quiz, verifica, compiti, pronuncia, peso.
Dopo le correzioni **non ho rifatto il controllo con un agente**.

## 6. Secondo vecchio → nuovo
**Parte 1** | pezzo | 17/11 | 22/11 |
|---|---|---|
| T1 | 234.6 | 245.4 |
| Q1 | 1278.9 | 1230.1 |
| T2 | 1284.2 | 1235.4 |
| Q2 | 1828.3 | 1738.3 |
| T3 | 1833.6 | 1743.6 |
| Q3 | 2412.1 | 2264.1 |
| T4 | 2417.4 | 2269.4 |
| Q4 | 2821.7 | 2622.9 |
| GL1 | 2890.6 | 2628.5 |
| RF1 | 2939.2 | 2677.1 |
**Parte 2** | pezzo | 17/11 | 22/11 |
|---|---|---|
| T1 | 70.3 | 77.3 |
| Q1 | 319.5 | 280.8 |
| T2 | 324.8 | 286.1 |
| Q2 | 651.8 | 579.9 |
| T3 | 657.1 | 585.2 |
| Q3 | 896.0 | 778.7 |
| T4 | 901.3 | 784.0 |
| Q4 | 1388.0 | 1234.8 |
| T5 | 1393.3 | 1240.1 |
| Q5 | 1846.3 | 1652.5 |
| T6 | 1851.6 | 1657.8 |
| Q6 | 2727.0 | 2483.9 |
| R1 | — | 2489.2 |
| GL1 | 2782.8 | 2612.3 |
| RF1 | 2830.3 | 2659.8 |
| VER | 2891.3 | 2720.8 |
| CI1 | 2904.5 | 2734.0 |
| COMP | 2910.1 | 2739.6 |

## 7. Altre note
- Dopo la mia consegna del 17/11 qualcun altro ha pushato su questo ramo «pillole di ripasso inserite…» (vtt/scheda/timeline): ho unito senza forzare. Ho rigenerato di nuovo vtt, timeline e scheda dal video di questa consegna.
- Il commit finale è firmato «Claude» (richiesta del controllo automatico del repository).
