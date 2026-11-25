# RAPPORTO DI REVISIONE · Storia V · «Il dopoguerra italiano (1919-1925) e il fascismo» · correzioni 22/11
Etichette: **misurato** / **stima** / **non verificato**.

## 1 · Misure (misurato)
| Parte | Durata | Fotogrammi (attesi) | Peso | Volume | Risoluzione |
|---|---|---|---|---|---|
| 1 | 51:36 (3096,15 s) | 92884 (92884) | 326,2 MB | −15,9 LUFS | 1920×1080 · 30 fps |
| 2 | 60:07 (3607,29 s) | 108218 (108219, scarto 1) | 355,3 MB | −16,0 LUFS | 1920×1080 · 30 fps |
x264 veryfast CRF 19, AAC 192k 48 kHz, una sola codifica. Timbro del prof (campione): acuti/bassi −17,6 dB dopo la pulizia contro −17,7 dB dell'originale (limite −9/−20).
Jingle quiz (controllo_jingle.py): scarto massimo 0,013 s (Q1–Q7 OK). Tono voce e chiarezza (controllo_severo): nessuna voce alterata.

## 2 · controllo_severo.py (misurato) — ESITO: RESPINTA, residui da leggere
- Nessuna slide oltre 3 minuti, nessuna schermata identica oltre 3 minuti, nessuna «…», nessuna card con iniziale minuscola, nessuna card sola oltre 60 s, voce non alterata.
- Parte 1: «titolo copertina incompleto: italiano» = **falso positivo dell'OCR** (la copertina contiene il titolo esatto, letto a mano su un fotogramma). 2 pause > 2,5 s (2,6 s): silenzio **tra la pillola e la scheda Quiz** (code dei pezzi, non pause del prof).
- Parte 2: «copertina non trovata»: la Parte 2 **non ha copertina per regola** (si apre con sigla e spiegone). 4 pause > 2,5 s: stessa natura (code tra pillole e quiz, 2,5–2,6 s).
Non ho avuto il tempo di accorciare quelle code e ricodificare.

## 3 · Cosa è stato rifatto (CLAUDE.md e prompt correzioni)
- **Mappe del prof** (PDF «MAPPE LEZIONE 8»: 3 mappe): ridisegnate in vettoriale nel modello BES (5 colori, legenda in alto a destra, testo 38–50 px), **costruite ramo per ramo con la voce Kore**, nodo acceso in giallo mentre la voce lo legge, mappa intera ferma 4 s. Posizione: MAP1 a fine argomento 2, MAP2 a fine argomento 4, MAP3 a fine argomento 7. Le mappe inventate dalle versioni precedenti sono tolte. **La mappa 3 non aveva il titolo-domanda: «Come Mussolini conquista il potere?» è scritto da me con le parole del prof** (come da risposta della master). Mappe del prof = 3 per 7 argomenti: gli altri argomenti chiudono con la pillola.
- **Slide**: testo card a 40 px (48 px solo quando una card sta da sola), interlinea 1,5, al massimo 3 card intere, bordo giallo sulla frase in corso, riquadro 4:3 (412×309 a x=1428, y=148) con ombra grigia e fascia gialla, correzione colore leggera. Nessuna «pagina» resta uguale oltre 150 s (cambio di finestra con nuovo numero di pagina).
- **Introduzione**: copertina con voce di benvenuto **senza riquadro del docente**; il riquadro compare quando parla. Introduzione del prof sopra la copertina 174,9 s (< 3 min), poi slide «Di cosa parliamo». Il nome del prof non è mai detto né scritto nelle animazioni (BEN_R2 sostituisce la voce che lo diceva); compare solo nella fascia gialla.
- **Parte 2** si apre con lo **spiegone** (voce Kore, immagini del prof in alta risoluzione migliorate e mappa 1).
- **Approfondimenti** nuovi AP1–AP8 (44–54 s, solo dalle slide del prof, numeri in lettere); i vecchi (con dati non del prof) sono tolti.
- **Audio**: −16 LUFS; pause oltre 2,5 s portate a ~1 s tra segmenti; i riempitivi isolati («Um», «Mm») NON sono stati tolti quando stanno dentro una frase continua (non fatto); filtro dei bassi 70 Hz e riduzione leggera del rumore; timbro intatto.
- **Quiz**: domanda sulla Legge Acerbo spostata da Q7 a Q6 (è nella slide del primo governo; tolta «triennio di consolidamento») e **aggiunta in Q7 una domanda nuova sul 10 giugno 1924**: **da approvare dalla master**.
- Verifica finale (10 domande del prof) e Compiti (4 domande) dentro la Parte 2, con intro «Compiti» di 3,5 s e jingle. Dispensa A4 (64 pagine, testo invisibile selezionabile) e PDF mappe con copertina «MAPPE».

## 4 · Voci Kore (misurato)
Ricevute 12 voci nuove (BEN_R2, SPIEGONE_P2, CINTRO_R2, MAP3_R2, AP1–AP8). Trascritte e confrontate con il testo: somiglianza 0,90–1,00; le differenze sono solo cifre al posto delle lettere e piccoli errori dell'ASR (Facta/«fatta»). Bordi: ampiezza negli ultimi 50 ms ≤ 0,001 (limite 0,03). Nessun nome del docente. **Non ascoltate da una persona**: pronuncia dei nomi (d'Annunzio, Facta, Acerbo, Aventino) **non verificata**.

## 5 · Tabella delle fine dei pezzi del prof (tempi dell'originale)
| Pezzo | Intervallo | Ultime parole | Frase finita |
|---|---|---|---|
| D0 | orig 0.0–175.9 s | antico, di reazionario per certi aspetti, di antiliberale. | sì |
| 1 | orig 209.6–1010.0 s | di andare pian piano sempre più avanti allora | da verificare (punteggiatura mancante nella trascrizione automatica) |
| 2 | orig 1010.0–1753.4 s | Or | da verificare (punteggiatura mancante nella trascrizione automatica) |
| 3 | orig 1753.4–2587.8 s | alla fine del Vennio Rosso, l'ho detto 1919. | sì |
| 4 | orig 2587.8–3177.1 s | contro i socialisti ma anche contro i liberali | da verificare (punteggiatura mancante nella trascrizione automatica) |
| 5 | orig 3177.1–4003.7 s | Proseguiamo. | sì |
| 6 | orig 4003.7–4831.2 s | Va bene. | sì |
| 7 | orig 4831.2–5360.5 s | Totalitaria. | sì |
I tagli cadono nelle pause (0,15 s prima della frase che segue). Il pezzo 2 termina su «Andiamo avanti.» (l'«Or» finale è tolto come riempitivo); i pezzi 1 e 4 finiscono con una frase senza punto finale nella trascrizione automatica. **Non ho riascoltato ogni taglio**: non verificato a orecchio.

## 6 · Refusi delle slide del prof (corretti nelle nostre slide) e anomalie
- Maiuscole improprie nei titoli: «Dopoguerra» → «dopoguerra», «Biennio Rosso» → «Biennio rosso», «Fascismo» → «fascismo»; virgolette dritte " " → « ».
- Compiti del prof (PDF): la quarta domanda è numerata «3» per errore; qui n. 4.
- A voce il prof precisa la data della riunione di Milano come «16 ottobre 1922» (la slide dice solo «ottobre 1922»): riportata come la dice lui, **da portare a Sara**. La trascrizione automatica ha anche «Vittorio Emanuele II» in alcuni punti: probabile errore di riconoscimento, **non verificato all'ascolto**. Test del prof (Excel): 10 domande, invariate.
- Sigle: PNF e MVSN rispiegate sullo schermo (colonna «Parole chiave») dove compaiono nelle card; a voce le dice il prof (non modificabile).

## 7 · Sottotitoli
`.vtt` costruiti sul video finale dalla trascrizione automatica rimappata, con correzione dei termini presi dalle slide. **Da rileggere**: restano errori di riconoscimento (es. «dopoguerra Italia», anni scritti in lettere con refusi).

## 8 · Non verificato / residui
Taglio a metà frase e sincronismo labbra (≤0,04 s) non misurati a mano (sincronismo garantito dalla costruzione: stessi intervalli su audio e video); ascolto delle voci Kore; sottotitoli da rileggere; code di 2,6 s tra pillola e quiz; immagini del prof (278–770 px) ingrandite con Lanczos e nitidezza, restano a bassa definizione intrinseca; **mappa 3 senza titolo originale**; sigla «Storia» del kit usata senza modifiche.
Controllo dell'agente separato: vedi sezione 9.

## 9 · Controllo dell'agente separato (misurato su campioni) — ESITO: NON CONSEGNABILE senza correzioni
Difetti **confermati, non corretti** (tempo scaduto):
1. **Numeri in lettere sullo schermo** nelle schede animate (approfondimenti AN e pillole R: «millenovecentoventidue» ecc.). Per regola sullo schermo vanno le cifre (le lettere restano solo nel testo della voce). Es.: AN2 ~1965 s e R6 ~2720 s (Parte 2).
2. **Sigle PNF e MVSN non rispiegate sullo schermo nella pillola R6** (Parte 2, ~2683–2740 s); nelle slide D4 e D6 sono spiegate nelle «Parole chiave».
3. **Colonna «Parole chiave» tagliata sul bordo** in alcune slide della Parte 2 (es. «MVSN = Milizia volontaria per la sicu…» a ~2100 s).
4. **Foto del prof** (Guardie rosse, D1 ~1000 s; foto nello spiegone) troppo vicine/sovrapposte al piè di pagina; didascalie piccole.
5. **Approfondimenti** con schermo quasi vuoto: solo card in alto, nessuna immagine di supporto.
6. D1 ~760–790 s: card «mito bolscevico» accesa mentre il prof parla ancora delle tensioni operaie (sfasamento possibile di 20–100 s; i tempi delle card sono stati assegnati a mano sulla trascrizione automatica).
Esiti dell'agente non confermati da me: «Pagina N» in tutte le schede = previsto dal modello Spagnolo (piè di pagina con numero); «fondo non bianco puro» = sfondo (255,255,255) nel disegno, 253 dopo la codifica video.
**Non verificati dall'agente:** tagli a metà frase, sincronia labbra, timbro, volume, glossario, sottotitoli, 4 s di mappa ferma, scatto del jingle (da me misurato: ≤0,013 s).


## Correzione del 25/11/2026 — voce COMPITI nella Parte 2 (Claude 2, master di riserva)
**File nuovo: `Storia_Lez8_Parte2_1080p.mp4`** — creato il 25/11/2026 ore 20:34 (ora italiana). sha256 `6803c7a49f8d2256cabf159d7a5bb7691d188a33f6b45f0634a36d6458de0a38`, 4 pezzi da 90 MB (`Storia_Lez8_Parte2_1080p.mp4.parte_00` …). Sostituisce il file con lo stesso nome consegnato il 23/11 (sha256 precedente nel ramo, cronologia git).
Su Vimeo lo sostituisce la master, con lo stesso link.

### Cosa ho cambiato (solo questo)
- Nella Parte 2 i compiti erano **muti** a 58:52 (58:52–60:06, 74 s di silenzio). Ho inserito la voce Kore `COMPITI.wav` (78.4 s, dalla master, 24/11: `scambio/storia-V-lez08/vox/COMPITI.wav`). **Non ho scritto né cambiato il testo.**
- Sullo schermo i compiti compaiono **uno alla volta con il bordo giallo**, accesi quando la voce comincia il compito (tempi dalla trascrizione della voce, fatta con ASR). Le parole sono quelle del docente (`compiti.json`, invariato). Alla fine una riga a voce e sullo schermo: «Svolgi i compiti qui sotto e premi Consegna: arrivano al docente nel tuo quaderno dei compiti».
- Voce: +1,6/+1,7 dB per portarla al livello delle altre voci Kore del video; dissolvenza di 30 ms all'inizio e alla fine; bordi sotto 0,002.
- Tutto il resto del video è **copiato senza ricodificare** fino al punto dei compiti (3532,3 s); il pezzo nuovo è ricodificato con gli stessi parametri (x264 veryfast CRF 19, AAC 192k 48 kHz, 1920×1080, 30 fps). Fotogrammi del pezzo prima dei compiti ricodificati: nessuno.

### Durata: CAMBIA (non è identica)
Prima 3607,29 s (60:07); ora **3611.93 s** (+4.6 s). La voce è più lunga della scheda muta: non ho potuto accorciare una pausa vicina senza spostare il quiz o la verifica. I **tempi dei quiz e della verifica non sono cambiati** (stanno prima). Aggiornati: `timeline_Parte2.json` (ultimo pezzo), `scheda_pubblicazione_Parte2.json` (`durata_s`), `.vtt` (aggiunti i sottotitoli dei compiti). **Va aggiornata la durata nella pagina** (`var CFG={… "dur": …}` = 3611.93) quando la master sostituisce il video: non ho toccato `gh-pages`.

### Controlli (misurato)
- Controllo rapido: ESITO **DA CORREGGERE** — volume -16.0 LUFS, picco -1.0 dBTP, peso 340 MB, formato 1920x1080 30/1, fotogrammi = durata × 30 (ok). Compiti: non più mute (verificato con la misura delle pause).
- Piè di pagina senza nome del docente, nessuna scheda con fasce, nessuna schermata ferma oltre 3 minuti.
- Foglio dei fotogrammi guardato (ultimo fotogramma: compito 1 con bordo giallo).
- **Pause mute rimaste (c'erano già, non sono i compiti):** 29:01 (2.5 s), 58:35 (4.4 s), 58:41 (2.7 s). Non le ho toccate: spostano il quiz o la verifica. Per la 09 il tratto di 92 s è la verifica a schermo senza voce: decide Sara.
- Il riquadro del docente non è coinvolto (nessuna parola del docente toccata).

### Non verificato
- Ascolto della voce da parte di una persona (pronuncia dei nomi: d'Annunzio, Rapallo, Matteotti, Acerbo, Etiopia): non ascoltata.
- Sottotitoli dei compiti: tempi proporzionali tra le parole, non parola per parola.
- Confronto con il ramo `consegna-storia-V-lez08`: non fatto.
- Nel `compiti.json` della 08 il titolo contiene «Lezione 8» (numero di lezione): non toccato, da decidere.
