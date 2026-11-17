# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 6 · Decadentismo e Simbolismo
Revisione del 17/11/2026. Video corretto: `Letteratura_Lez6_Parte1_1080p.mp4` (a pezzi `.parte_00…`, sha256 nel file `.sha256`).
Regola: **misurato** = misurato con uno strumento; **stima** = dedotto; **non verificato** = non ho potuto.

## 1. Misure sul video nuovo
| Controllo | Risultato |
|---|---|
| Formato | 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192k 48 kHz (**misurato**) |
| Durata / fotogrammi | 53:07,93 · **95 638 fotogrammi = durata × 30, identici al montaggio precedente** (55 pezzi, somma verificata): quiz, verifica e compiti restano agli stessi secondi (schede quiz a 11:56,3 · 20:59,9 · 29:45,8 · 40:44,9 · 50:41,1; verifica 52:43,1; compiti 52:59,4) |
| Peso | 210,2 MB (sotto i 400 MB), 3 pezzi da 95 MiB + `.sha256` (somma dei pezzi = sha256 del file, **misurato**) |
| Volume | −16,9 LUFS integrato (LRA 6,4 LU), picco **−1,9 dBTP** (true peak, `ebur128=peak=true`): ≤ −1 dBTP (**misurato** sul file finale) |
| Audio del prof | rifatto dall'originale: `aresample=48000, highpass=80, arnndn (sh.rnnn del kit), volume +4,7 dB, alimiter` (rumore di fondo −63,4 → −66,6 dBFS nel pezzo D2 e −63,2 → −66,0 nel D4, **misurato**); poi limitatore finale a −2,4 dBFS |
| Sincronia prof | audio del video finale confrontato per correlazione con l'originale in 3 684 finestre da 2 s: scarto massimo **0,003 s (D1), 0,019 (D2), 0,013 (D3), 0,013 (D4), 0,020 (D5)** (limite 0,04 s). Immagine e audio del prof escono dallo stesso istante dell'originale (**misurato**) |
| Jingle dei Quiz (`controllo_jingle.py`) | 5 su 5 a 0,0 s: scarti +0,002, +0,004, +0,002, +0,004, +0,003 s. Jingle del titolo (`titolo.wav`) sulle 5 schede degli argomenti (correlazione 0,98–1,00); **aggiunti** `repaso.wav` all'inizio dei 5 ripassi (−9 dB sotto la voce) e `trans.wav` sulle transizioni AN1–AN5, mappa finale, glossario, riepilogo, compiti (−11 dB) |
| Transizioni | dissolvenza di 9 fotogrammi all'inizio di ogni pezzo (tranne la sigla, già dissolta nella copertina, e il finale): nessun taglio secco (**misurato** sul codice di montaggio; visivo a campione) |
| Fermi immagine del prof | `freezedetect` sul riquadro (0,5 s): nessun fermo ≥ 1 s in D1…D5; un solo fermo di 0,5 s a 21:13 (**misurato**). I fermi del riquadro restano solo nelle schede senza prof (benvenuto, approfondimenti, ripassi, quiz) dove il riquadro non c'è |
| Prof mai tagliato a metà frase | vedi tabella sotto (§3-bis) |
| PDF | `…_slide.pdf`: 66 pagine A4 orizzontale; `…_mappe.pdf`: 6 pagine A4 orizzontale (una per argomento + mappa di tutta la lezione) |
| Sottotitoli | 794 cue, max 2 righe, nessuna sovrapposizione, riletti e corretti a mano (circa 280 correzioni); sincronia con la voce: su 149 cue verificabili (trascrizione del video nuovo), scarto mediano 0,00 s; entro 0,3 s il 94%, entro 1 s il 99% (**misurato**) |

## 2. Confronto col modello Spagnolo (punto 000)
| # | Punto | Esito |
|---|---|---|
| 1 | Sigla 15 s → dissolvenza → copertina | OK: sigla del kit invariata (450 fotogrammi); dissolvenza morbida di 20 fotogrammi sulla copertina (nessun lampo) |
| 2 | Copertina (logo, «LETTERATURA ITALIANA V · VIDEOLEZIONE», titolo con barretta, card ARGOMENTI) | **corretto**: rifatta nel modello. Card su una colonna (5 argomenti); gli argomenti si accendono in giallo mentre la voce li nomina |
| 3 | Slide: fondo bianco, «01 · ARGOMENTO», titolo Bricolage 800 + barretta, tabelle con intestazione blu notte | **corretto**: 66 slide rifatte (tutte, una per pagina del PDF); «01…05» è il numero dell'argomento, mai della lezione |
| 4 | Piè di pagina «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» + «Pagina N» | **corretto** su tutte le slide (le mappe hanno il piè senza numero, come le altre schede senza pagina) |
| 5 | Riquadro 4:3 in alto a destra, ombra grigia, niente bordo | **corretto**: 412×310 px a x=1428, y=148, angoli r=20, ombra morbida; ritaglio 184×138 px dalla webcam dell'originale (ingrandita 2,24×) con contrasto 1,04, saturazione 1,03, `hqdn3d=1.5:1.5:3:3`, `cas=0.35` |
| 6 | Fascia gialla −3°, due righe | **corretto**: «Giorgio Mazzotti» / «PROF. DI LETTERATURA ITALIANA», visibile in tutte le slide col prof |
| 7 | Slide senza prof | **corretto**: presentazione, approfondimenti, ripassi, sintesi, glossario, riepilogo, mappe e schede rifatti nel modello |
| 8 | Font | Bricolage Grotesque 800 (titoli), Figtree (testo, etichette e piè in Figtree Bold come nel modello). DM Mono non usato |
| 9 | Finale 5 s con avviso diritti | OK: `Sigla_finale_5s_con_avviso_diritti.mp4` (150 fotogrammi) a 53:02; prima c'è la scheda «Fine della lezione» con la voce |
| 10 | Struttura | OK: sigla → presentazione → 5 argomenti (titolo, prof con slide, approfondimenti animati, ripasso, sintesi, quiz) → mappa → glossario → riepilogo → finale. Verifica finale e compiti restano a fine video, agli stessi secondi |
| 11 | PDF slide + mappe A4 orizzontale | consegnati (vedi §1): slide 66 pagine, mappe 6 pagine |

**Presentazione col prof:** la voce di benvenuto (INTRO, 35 s) è la voce narrante Kore: lì **non c'è il prof**, per non avere le labbra fuori sincrono con un'altra voce. Appena il prof parla (da 0:55) la copertina ha il riquadro e la fascia.
**Testa nel riquadro:** la webcam dell'originale è 246×138 px; il 4:3 ne prende 184×138. Nei tre fotogrammi dell'originale guardati (1:40, 15:00, 25:00) i capelli toccano il bordo alto già nella ripresa. Non risolvibile.

## 3. Problemi trovati e correzioni
| Minuto | Tipo | Com'era | Correzione |
|---|---|---|---|
| tutto | visivo | prof nel tondo; fondo azzurrino; titoli e card diversi dal modello Spagnolo; etichette in DM Mono; piè «Ripasso»; schede nere/blu di titolo, quiz, verifica e compiti | tutta la lezione rifatta nel modello (66 slide), riquadro 4:3, fascia gialla |
| 1:03–2:59 | sincronia | slide degli argomenti ferma 116 s senza evidenziazione (differenza tra fotogrammi, **misurato**) | copertina con riquadro e fascia; l'argomento «Il Decadentismo…» si accende quando il prof dice «Come vedete parliamo innanzitutto di…» (2:22); poi la slide «Dal movimento locale alla corrente europea» da 2:58 e «I poeti maledetti e la critica» da 3:17 |
| 4:22–6:12 · 6:19–7:13 | sincronia | stessa card per 110 s e 54 s mentre il prof passa dai gruppi d'avanguardia alla reazione degli artisti e agli esponenti | evidenziazione dal parlato: critica ufficiale 3:17, gruppi d'avanguardia 4:19, reazione 5:57, esponenti 6:24 |
| 14:19–15:47 · 25:03–26:06 · 30:29–31:37 · 32:01–33:22 | sincronia | slide ferme 88, 63, 68 e 81 s | righe/stanze accese a tempo con la lettura (ogni 10–30 s) |
| D1–D5 | contenuto | slide non del prof: schede riscritte («Una corrente culturale europea», «Languore: l'analisi»…) con frasi che il prof non ha scritto | slide dal `_videodispensa.pptx` del prof, testo identico (maiuscola iniziale e virgolette «») |
| 10:21 · 19:35 · 28:16 · 39:13 · 49:10 · 50:46 | contenuto | 5 mappe + mappa finale inventate da noi (nodi non del prof) | **mappa del prof** («I “POETI MALEDETTI”»: Verlaine → Languore, Rimbaud → Vocali, Baudelaire, gruppo d'avanguardia, fondamenti della poesia) nella nostra grafica, in 6 pezzi di uguale durata; nuove voci Kore `R6…R11` (nodi evidenziati a tempo); pause inserite tra le frasi (≤ 1,9 s) |
| INTRO 0:15–0:49 | visivo | prof nel tondo mentre parla la voce narrante | copertina senza prof (voce Kore): il riquadro del prof c'è solo quando il prof parla |
| vtt | testo | errori in tutto il file: «benvenute la lezione», «distudiarlo», «dispiegarlo», «Verlin», «Rainbow», «l'angore», «Uismoth», «Ugom Acar», «a Bodlerano»… | rifatto da zero dalla trascrizione, corretto a mano (nomi, titoli, versi di Languore e Vocali, date); tempi dalla trascrizione parola per parola |
| ripassi | audio | senza jingle (repaso) né transizioni sonore | aggiunti `repaso.wav` e `trans.wav` |
| tra i pezzi | visivo/audio | tagli secchi | dissolvenza di 9 fotogrammi + `trans.wav` |
| picco | audio | picco true peak −0,9 dBTP dopo la prima codifica | limitatore a −2,4 dBFS: −1,9 dBTP |
| fine | consegna | mancavano `…_slide.pdf`, `…_mappe.pdf`, `verifica_finale.json`; titolo scheda non standard | prodotti; titolo «Letteratura V · Lezione 6 · Decadentismo e Simbolismo» |

### 3-bis. Inizio e fine di ogni pezzo del prof (misurato sulla trascrizione)
| Pezzo | Fine (minuto) | Ultime parole dette | Frase finita? | Inizio (minuto) | Prime parole |
|---|---|---|---|---|---|
| D1 | 8:15 | «…Ci torneremo, affronteremo tutto. Allora.» | sì | 0:55 | «Buongiorno e benvenuti alla lezione su Decadentismo e Simbolismo» |
| D2 | 17:46 | «…specificare qualcosa in più. Allora.» | sì | 12:06 | «Ecco, giusto per inquadrare bene» |
| D3 | 26:06 | «…Mentalità da fine secolo, da fine tutto. Allora.» | sì | 21:10 | «Tanto per… continuare a parlare…» |
| D4 | 36:47 | «…rifiuto della razionalità… Questo è chiaro.» | sì | 29:56 | «Sono gruppi d'avanguardia, abbiamo detto» |
| D5 | 47:07 | «…ma era fondamentale comprendere che qui… nasce tu…» | **no: l'originale del prof finisce così, a 31:00** | 40:55 | «Va bene, poi come appunto potete vedere anche nella slide» |
Nessuna parola è mozzata in partenza. L'unico finale non chiuso è quello dell'originale (non si può allungare).

## 4. Pagine del libro in alta risoluzione (B-bis)
Zip `Lez06_ingrandita.zip`: pagine 202 (Languore) e 206 (Vocali), file `Lez06_p202.png` e `Lez06_p206.png` (2373×3159 px). Il prof mostra anche, come slide, i ritratti di Verlaine e Rimbaud (immagini del suo pptx).
**Regole applicate:** una sola colonna per fettina; inizio e fine su una riga bianca; i bordi senza inchiostro tagliato; niente intestazione di pagina, numeri, QR, esercizi. Stanza in corso evidenziata in giallo; nei versi di Vocali si accende la riga della vocale di cui parla il prof (A, E, I, U, O, Omega). Righe a 33–36 px a 1080p (le fettine dei versi); il testo francese a fronte, su due colonne affiancate, è a ≈ 24 px (non è letto dal prof).

| # | Brano | Pagina | Parte | File HD / ritaglio (px) | Minuto |
|---|---|---|---|---|---|
| 1 | Languore | p. 202 | ritratto di Verlaine (slide del prof) | `pptx del prof (s3)`  | 12:23–12:30 |
| 2 | Languore | p. 202 | testata del brano (titolo, introduzione, metro) | `Lez06_p202.png` [220, 625, 1700, 1205] | 12:30–12:34 |
| 3 | Languore | p. 202 | testo francese a fronte | `Lez06_p202.png` [1455, 1225, 2200, 2340] | 12:34–12:47 |
| 4 | Languore | p. 202 | versi 1–8 (due quartine) | `Lez06_p202.png` [290, 1262, 1450, 1810] | 12:47–12:58 |
| 5 | Languore | p. 202 | versi 1–8 (due quartine) | `Lez06_p202.png` [290, 1262, 1450, 1810] | 14:13–14:50 |
| 6 | Languore | p. 202 | versi 9–14 (due terzine) e fonte | `Lez06_p202.png` [290, 1830, 1450, 2320] | 14:50–16:02 |
| 7 | Vocali | p. 206 | ritratto di Rimbaud (slide del prof) | `pptx del prof (s9)`  | 30:45–31:36 |
| 8 | Vocali | p. 206 | versi 1–8 (due quartine) | `Lez06_p206.png` [290, 745, 1490, 1285] | 31:36–32:18 |
| 9 | Vocali | p. 206 | versi 9–14 (due terzine) e fonte | `Lez06_p206.png` [290, 1310, 1490, 1840] | 32:18–33:22 |
| 10 | Vocali | p. 206 | versi 1–8 (due quartine) | `Lez06_p206.png` [290, 745, 1490, 1285] | 33:22–35:13 |
| 11 | Vocali | p. 206 | versi 9–14 (due terzine) e fonte | `Lez06_p206.png` [290, 1310, 1490, 1840] | 35:13–36:47 |

Foglio `controllo_fettine.jpg`: un fotogramma a metà intervallo per ognuna delle 11 righe: nessuna riga tagliata, nessun frammento di altre colonne, nessuna intestazione. Abbinamento letto sulla trascrizione (±2 s, **stima**).

## 5. Cosa NON ho verificato / limiti
- **Ascolto umano:** non ho ascoltato fruscio/ronzio/metallico dopo la pulizia, né la voce Kore. Ho misurato che la voce narrante corrisponde al testo (confronto tra trascrizione e testo: 0,76–1,00, **misurato**); R6 e R7 sono segnate «DA CONTROLLARE» dal servizio delle voci e non le ho potute ascoltare. **Non verificato.**
- **Sottotitoli da riascoltare (parola incerta):** 7:55 «il manifesto delle tendenze decadenti…» (inizio frase non trascritto); 15:10 «già usato dagli Scapigliati»; 16:58 «si dice che facciano qualcosa»; 24:32 frase di 1 s tolta; 30:47 «perché Languore è dell'83»; 32:48 «prima la U e poi la O» (la trascrizione dava U/U); 35:42 «il blu della suprema tromba»; 35:55 «dai mondi e dagli angeli»; 36:44 «Questo è chiaro».
- **Evidenziazioni delle card:** calcolate dalla trascrizione automatica (±1–2 s, **stima**); controllate a campione su 11 fotogrammi. Da guardare in almeno 4 punti.
- **Testa nel riquadro:** la webcam dell'originale è 246×138 px: il ritaglio 4:3 è 184×138 ingrandito 2,24× (immagine morbida) e i capelli toccano il bordo alto già nella ripresa. Non risolvibile.
- **Testo francese a fronte (Languore):** su due colonne a ≈ 24 px, sotto i 26 px; il prof non lo legge.
- **Date da confermare col prof (DA CONFERMARE COL PROF):** nessuna discrepanza trovata tra mappa, slide, voce e trascrizione (1872 Vocali, 1883 Languore, 1884 Controcorrente).
- **Quiz:** riletti contro le slide del prof: domande e risposte coerenti. Invariati.
- **Durata:** invariata (la regola «stessa durata» è stata annullata alle 00:40, ma qui non serve cambiarla): nessun silenzio della voce narrante > 3 s nei pezzi nuovi, nessuna frase senza immagine.
- **Jingle di Spagnolo:** usati i file `quiz.wav`, `titolo.wav`, `repaso.wav`, `trans.wav` del kit; `finale.wav` non aggiunto (il finale è la sigla del kit).
- **Verifica finale e compiti** (schede di servizio a fine video): rifatte nel modello, voce e secondi invariati.

## 6. Come ho verificato
Trascrizione completa con `trascrivi.py` (Parakeet): video vecchio 692 segmenti, originale del prof 362, **video nuovo** (692→ controllo di sincronia dei sottotitoli e `silencedetect`: nessun silenzio ≥ 3 s a −50 dB, **misurato**); OCR a vista dei fotogrammi; 3 188 fotogrammi a 1/s sul video vecchio (differenza tra fotogrammi per i fermi); 107 fotogrammi a 1/30 s sul nuovo (`controllo_minuti.jpg`); controllo del piano (55 pezzi = 95 638 fotogrammi, identici al vecchio).
