# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 14 · Pirandello (2 Parti)
Revisione del 16–17/11/2026. Video: `Letteratura_Lez14_Parte1_1080p.mp4` e `…Parte2…` (a pezzi `.parte_00…`, sha256 nei `.sha256`).
**misurato** = misurato con uno strumento · **stima** = dedotto · **non verificato** = non ho potuto.
**Stato: consegna con riserve** (sezione 5 e DA DECIDERE): non dico «tutto perfetto».

## 1. Misure sul video nuovo (misurato)
| Controllo | Parte 1 | Parte 2 |
|---|---|---|
| Formato | 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192k | uguale |
| Durata | 45:45.4 (2745.43 s, 82363 fotogrammi) | 45:45.9 (2745.90 s, 82377 fotogrammi) |
| Vecchia durata | 50:07,5 (90 226 fotogrammi) | 48:36,4 (87 491 fotogrammi) |
| Peso | 327.3 MB | 353.0 MB |
| Volume intero file (ebur128) | I:         -14.4 LUFS · LRA:         6.0 LU · Peak:       -1.3 dBFS | I:         -14.8 LUFS · LRA:         6.2 LU · Peak:       -1.1 dBFS |
| Audio del prof | pulito dall'originale con la catena del kit (`aresample 48000, highpass 80, arnndn sh.rnnn, loudnorm, alimiter`): −16,9 LUFS integrato, picco −2,0 dBTP (misurato sull'intero originale pulito) | uguale |
| Jingle Quiz a 0,0 s (`controllo_jingle.py`) | Q1–Q4: scarti −0,001…−0,004 s · OK | Q1–Q6: scarti −0,001…−0,006 s · OK |
| Altri jingle (correlazione col kit) | titolo 4/4 · ripasso 4/4 · transizione 5/5 | titolo 6/6 · ripasso 6/6 · transizione 7/7 |
| Silenzi > 3 s | 0: nessuno | 2: 45:19.9–45:25.8 (6.0 s) · pezzo VER; 45:38.7–45:45.9 (7.3 s) · pezzo COMP (solo schede di servizio Verifica e Compiti, vecchie) |
| Fermi immagine del prof (`freezedetect` sul solo riquadro, −55 dB, ≥ 0,7 s) | nessuno nei 5 pezzi D (misurato) | nessuno nei 7 pezzi D (misurato) |
| Sincronia audio del prof con l'originale | scarto massimo 0,5 ms su 36 punti (3 per pezzo D) | uguale |
| Sottotitoli | `.vtt` rigenerati dall'audio del video nuovo: 995 cue, max 2 righe da ≤43 caratteri | 946 cue |
| PDF | slide: 6 pagine A4 orizzontale | slide: 8 pagine; mappa del prof: 1 pagina (`…_mappe.pdf`) |
Le **durate sono cambiate** (decisione di Sara 17/11): la Parte 1 è **sotto i 50 minuti**, la Parte 2 anche. Vedi DA DECIDERE.

## 2. Confronto col modello Spagnolo (punto 000)
| # | Punto | Esito |
|---|---|---|
| 1 | Sigla → dissolvenza → copertina | sigla invariata; dissolvenze rifatte tra tutti i pezzi, con `trans.wav` |
| 2 | Copertina (logo, riga «LETTERATURA ITALIANA V · VIDEOLEZIONE», titolo, card ARGOMENTI) | **corretto**. Nella presentazione (voce di benvenuto) niente riquadro del prof: non parla |
| 3 | Slide: fondo bianco, «01 · ARGOMENTO», titolo+barretta, card | **corretto** per tutte le slide del prof |
| 4 | Piè di pagina + «Pagina N» | **corretto** (numerazione progressiva per Parte, copertina = 1) |
| 5 | Riquadro 4:3 con ombra grigia morbida, senza bordo | **corretto**: 412×309 px a x=1428 y=148, angoli r=18, correzione immagine del kit |
| 6 | Fascia gialla −3°, due righe | **corretto**, sempre visibile mentre parla il prof |
| 7 | Slide senza prof | **NON FATTO**: approfondimenti, pillole di ripasso, glossario, riepilogo e schede Quiz restano nella vecchia grafica scura (vedi sezione 5) |
| 8 | Font Figtree Bold / Bricolage 800 | corretto sulle slide rifatte (etichette in Figtree Bold) |
| 9 | Finale 5 s con avviso diritti | invariato (presente) |
| 10 | Struttura | mantenuta; **tolte le 12 mappe nostre**, inserita 1 mappa del prof con voce R1 (Parte 2) |
| 11 | PDF slide + mappe A4 orizzontale | slide: solo le slide nuove; mappe: sì |
Card in corso: bordo giallo sottile + numero su pallino giallo, fondo bianco, altre card con bordo grigio chiaro; ombre grigie morbide (richiesta di Sara 17/11 01:30).

## 3. Problemi trovati e correzioni
| Minuto (vecchio video) | Tipo | Com'era | Correzione |
|---|---|---|---|
| tutta la lezione | visivo | banda blu a destra, riquadro rettangolare con bordo blu, nome bianco su blu, etichetta «ARGOMENTO 1 ·» | rifatte tutte le slide del prof nel modello (punti 000) |
| P1 ≈ 4:00–8:00 (contact sheet) | sincronia | evidenziazione ferma sulla card 1 per minuti | evidenziazioni ricalcolate dal parlato (stima: parole chiave di ogni card nella trascrizione, percorso monotono; ogni card si accende) |
| tutta la lezione | sincronia | slide scelte dal video vecchio | la sequenza delle slide ora segue lo schermo dell'originale (il prof torna più volte tra le slide 3 e 4: nell'originale ai minuti 8:50, 13:30, 14:33, 15:05) |
| 10 confini su 11 tra pezzi del prof | audio | il pezzo del prof finiva a **metà frase** (da +0,9 a +9,1 s prima della fine frase) e il pezzo seguente ripeteva parlato | tutti i confini spostati sulla fine frase (pausa ≥0,45 s, minimo di energia); tabella in fondo |
| 6 punti: P1 D3 (30:38) e D4 (40:22); P2 D3 (11:02), D4 (15:06), D5 (23:18), D6 (30:56) del video vecchio | audio | **ripetizione** di 0,8–1,9 s di parlato del prof dopo gli inserti (misurata con gli offset costanti) | tolta: i pezzi D sono contigui nell'originale |
| P2 1:00–1:10 | visivo | per 3 s la slide di «Uno, nessuno» con etichetta del teatro | ora copertina Parte 2 |
| P1 (5 pezzi AN03/06/09/11/12) · P2 (7 pezzi AN02/04/06/08/10/12/13) | grafica | 12 mappe fatte da noi con nodi non del prof | tolte (con la loro voce); inserita la mappa del prof nella Parte 2 (41:29 del video nuovo, 120 s) |
| P2 Ciàula e Belluca (pezzi D4–D6) | pagina | pagina del libro piccola nel video | fettina dagli screen HD (vedi §4) |
| vtt | testo | 470 cue da un riconoscimento mediocre (es. «Piranvello», «lettratura», «pire andere»), tempi sfasati fino a 1 s | rigenerati dall'audio del video nuovo; nomi corretti: Ciàula, Meis, Moscarda, zi' Scarda, Casinò |
| scheda | testo | titolo «Pirandello · Parte 1»; argomento 2 «La visione del mondo e la trappola sociale» (≠ video), 3 «I primi grandi romanzi» | titolo standard «Letteratura V · Lezione 14 · Pirandello · Parte N», titoli argomento allineati al video, secondi aggiornati |
| audio | audio | la catena di pulizia del kit non era verificabile sul video vecchio | audio dei pezzi del prof rifatto dall'originale con la catena del kit |
| audio | jingle | transizioni e ripasso non rilevati dalla correlazione | `trans.wav` in ogni transizione, `repaso.wav` prima delle pillole |
Quiz: 5 domande per argomento già presenti; ho allineato i titoli. Verifica finale: le 10 domande coincidono con l'Excel del prof (similarità 1,0). Compiti: i 4 del PDF del prof, identici.

## 4. Pagine del libro in HD (B-bis)
Zip `Lez14_ingrandita.zip`: pagine 526–531 (Ciàula) e 533–538 (Belluca); **la pagina 532 manca nello zip**.
| Brano | Pagina | File HD | Minuto Parte 2 |
|---|---|---|---|
| Ciàula scopre la luna | 526 | Lez14_p526.png · prima fettina (titolo, temi principali, inizio) | dal pezzo D4 (≈ 20:45) a fine D5 |
| Il treno ha fischiato | 533 | Lez14_p533.png · prima fettina | D5 finale e tutto D6 |
Il prof **non legge** i brani: riassume mentre sullo schermo resta la prima pagina. Ho fatto scattare un'altra fettina solo se il testo citato coincide a lungo; non è scattata mai. Quindi **una sola fettina per novella**, ferma per minuti: lontano dalla lezione 11 di riferimento.

## 5. Cosa NON ho verificato / limiti noti / DA DECIDERE
- **Slide senza prof nella vecchia grafica**: approfondimenti animati, pillole, glossario, riepilogo (e schede Quiz/Verifica/Compiti con banda blu, come da prompt) **non sono stati rifatti** nel modello. Non ho il generatore dei loro testi; l'OCR sarebbe stato lungo. È il difetto più grosso rimasto: la lezione **non è nel modello in tutto**.
- **PDF slide**: contiene solo le slide nuove (copertina e slide del prof, 6 + 8 pagine); mancano le slide degli inserti vecchi. Non ho confrontato pagina per pagina col video.
- **Fettine del libro**: una per novella (§4). Niente `controllo_fettine.jpg` con più fettine.
- **Durata**: Parte 1 45:45.4, Parte 2 45:45.9: entrambe **sotto i 50 minuti**. Decide Sara (unire, aggiungere, accettare).
- **Voce R1** (mappa del prof): la trascrizione dell'ascolto automatico rende «giorfatara», «Fumathia Pascal», «Uno Nessuno ai 100.000»: potrebbe essere errore del riconoscimento o pronuncia sbagliata della voce. **Non ascoltata da me.** Se è la voce, serve R2 con il testo riscritto.
- Il **riquadro del prof 4:3**: la webcam originale è 184×138 px ingrandita 2,2×: immagine morbida; la testa tocca il bordo alto già nell'originale (es. 0:20, 11:40, 23:20 dell'originale).
- **Sincronia labbra**: video e audio sono presi dallo stesso istante dell'originale (scarto audio misurato ≤0,5 ms); il movimento delle labbra **non l'ho verificato indipendentemente**.
- **Evidenziazioni** delle card: stima da parole chiave; non ascoltate a mano. Slide 47 (Serafino Gubbio) non è mai mostrata dal prof: non c'è nel video.
- **Mappa del prof**: una sola per tutta la lezione, messa nella Parte 2 (decisione mia, da confermare). Nel PDF mappe i nodi sono identici (letti dall'immagine). 
- Nella mappa del prof: «Così è **se** (se vi pare)» (probabile refuso) e «Il **gioco** delle parti» (nelle slide «giuoco»): DA CONFERMARE COL PROF.
- Le pillole e gli approfondimenti vecchi contengono ancora qualche contenuto che non coincide con le slide (es. quiz 2 titolo vecchio): ho allineato solo i titoli.

## Tabella: fine e inizio di ogni pezzo del prof (misurato su pause ≥ 0,45 s)
| Pezzo | Inizio | Prime parole | Inizia a inizio frase | Fine | Ultime parole | Frase finita |
|---|---|---|---|---|---|---|
| P1 D0 | 0:52 | «Buongiorno e benvenuti alla lezione su…» | sì | 3:55 | «…i testi di Luigi Pirandello, alcuni dei quali.» | sì |
| P1 D1 | 4:01 | «come dire sono oggetto D Interrogazione…» | sì | 16:40 | «…perché hai sempre recitato un ruolo. We need.» | sì |
| P1 D2 | 20:40 | «ai tuoi occhi anche. Ecco questa,…» | sì | 27:27 | «…capire esattamente cosa ha scritto e cosa racconta.» | sì |
| P1 D3 | 29:08 | «Passiamo a, beh, insomma, al capolavoro,…» | sì | 36:00 | «…verghiano, per dare corpo alla relatività del reale.» | sì |
| P1 D4 | 37:54 | «E questa riflessione continua in... Uno,…» | sì | 42:24 | «…ha già abbozzato nel Fu Mattia Pascal. Proseguiamo.» | sì |
| P2 D0 | 1:00 | «uno sono centomila importante romanzo. Ora…» | sì | 1:08 | «…uno sono centomila importante romanzo. Ora dobbiamo parlare.» | sì |
| P2 D1 | 1:14 | «di come dire Beh, insomma, della…» | sì | 3:23 | «…infrange in tutto questo e viene sommerso, d'accordo?» | sì |
| P2 D2 | 4:51 | «Ecco, se i personaggi cerca d'autore,…» | sì | 8:21 | «…e poi Enrico IV, un altro dramma teatrale.» | sì |
| P2 D3 | 9:50 | «Questo un po più storico, d'accordo?…» | sì | 11:53 | «…sta male e alla fine non risolve nulla.» | sì |
| P2 D4 | 13:08 | «Ora, giusto perché siamo, diciamo così,…» | sì | 19:04 | «…se stessi, e soprattutto il concetto della maschera.» | sì |
| P2 D5 | 20:45 | «Però queste novelle in alcune, insomma,…» | sì | 25:40 | «…seconda, ed ultima, è in chiusura due parole.» | sì |
| P2 D6 | 27:39 | «su Pirandello è il rapporto con…» | sì | 39:25 | «…Poi si rese conto. Ma era troppo tardi.» | sì |

(«Frase finita» e «Inizia a inizio frase» = punteggiatura della trascrizione automatica seguita da pausa; le «ultime parole» sono del riconoscimento, non riascoltate.)

## Tabella secondo vecchio → secondo nuovo
**Parte 1**
| Pezzo | Vecchio | Nuovo | Differenza |
|---|---|---|---|
| T1 | 234.6 | 236.4 | +1.8 |
| Q1 | 1278.9 | 1230.1 | -48.8 |
| T2 | 1284.2 | 1235.4 | -48.8 |
| Q2 | 1828.3 | 1738.3 | -90.0 |
| T3 | 1833.6 | 1743.6 | -90.0 |
| Q3 | 2412.1 | 2264.2 | -147.9 |
| T4 | 2417.4 | 2269.5 | -147.9 |
| Q4 | 2821.7 | 2622.9 | -198.7 |
| GL1 | 2890.6 | 2628.5 | -262.1 |
| RF1 | 2939.2 | 2677.1 | -262.1 |
**Parte 2**
| Pezzo | Vecchio | Nuovo | Differenza |
|---|---|---|---|
| T1 | 70.3 | 69.6 | -0.7 |
| Q1 | 319.5 | 280.8 | -38.7 |
| T2 | 324.8 | 286.1 | -38.7 |
| Q2 | 651.8 | 579.9 | -71.9 |
| T3 | 657.1 | 585.2 | -71.9 |
| Q3 | 896.0 | 778.7 | -117.3 |
| T4 | 901.3 | 784.0 | -117.3 |
| Q4 | 1388.0 | 1234.8 | -153.2 |
| T5 | 1393.3 | 1240.1 | -153.2 |
| Q5 | 1846.3 | 1649.2 | -197.1 |
| T6 | 1851.6 | 1654.5 | -197.1 |
| Q6 | 2727.0 | 2484.0 | -243.0 |
| GL1 | 2782.8 | 2612.3 | -170.5 |
| RF1 | 2830.3 | 2659.8 | -170.5 |
| VER | 2891.3 | 2720.8 | -170.5 |
| CI1 | 2904.5 | 2734.0 | -170.5 |
| COMP | 2910.1 | 2739.6 | -170.5 |
La master rigenera la pagina con i secondi di `scheda_pubblicazione_parte*.json`, `quiz_argomenti_parte*.json` e `timeline_parte*.json`.

## 6. Come ho verificato
Trascrizione dell'originale (64 min) e dei due video con `trascrivi.py`; allineamento per correlazione dell'audio (offset costanti per pezzo); scene dell'originale (differenza di fotogrammi + OCR dei titoli); fotogrammi ogni 30 s (`controllo_minuti_parte*.jpg`); `controllo_jingle.py`; `ebur128`, `silencedetect`, `freezedetect`; correlazione col kit per i jingle; confronto Excel/PDF del prof con le consegne.
