# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 24 · Leonardo Sciascia
Revisione del 16–17/11/2026. Video: `Letteratura_Lez24_Parte1_1080p.mp4` (a pezzi `.parte_00`, `.parte_01`; sha256 nel file `.sha256`).
Regole applicate: fino all'aggiornamento delle 08:45 del 17/11. Etichette: **misurato** = misurato con uno strumento; **stima** = dedotto; **non verificato** = non ho potuto.

## 1. Misure sul video nuovo
| Controllo | Risultato |
|---|---|
| Formato | 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192k 48 kHz (misurato) |
| Durata / fotogrammi | 55:55,9 (3355,87 s) · 100 676 fotogrammi = durata × 30 (misurato). **La durata è cambiata**: era 55:38,4 (+17,4 s), vedi §6 |
| Peso | 177,4 MB (misurato) |
| Volume | −16,7 LUFS integrato, LRA 6,1 LU (misurato) |
| Picco | −2,1 dBTP (ebur128 peak=true) (misurato) |
| Sincronia audio/prof | scarto massimo 1,4 ms su 20 punti dei 4 pezzi del prof (correlazione dell'audio del video con l'originale) (misurato). Il video è tagliato dagli stessi istanti dell'audio (stima: ≤ 17 ms di arrotondamento al fotogramma) |
| Fermi immagine riquadro del prof | `freezedetect` sul video finale: 0 fermi ≥ 1 s in D0, D1, D2, D3 (misurato) |
| Jingle Quiz | lo scatto cade a inizio scheda + 0,5 s con scarto −0,016 s su Q1, Q2, Q3, Verifica finale, Compiti (corr. 0,90–0,99) (misurato). Jingle titolo argomento (T1–T3) presente (misurato) |
| Silenzi > 2,9 s | nessuno, tranne gli ultimi 4,2 s della scheda Compiti (ultima scheda, in attesa dell'esercizio) (misurato) |
| PDF | slide: 40 pagine A4 orizzontale; mappe: 1 pagina A4 orizzontale (il prof ha una sola mappa per tutta la lezione) |

## 2. Confronto col modello Spagnolo (punto 000)
| # | Punto | Esito |
|---|---|---|
| 1 | Sigla 15 s → dissolvenza → copertina | OK. Sigla invariata; dissolvenza di 1,6 s + `trans.wav` |
| 2 | Copertina (logo, riga «LETTERATURA ITALIANA V · VIDEOLEZIONE», titolo, card ARGOMENTI) | **corretto** (era titolo piccolo + elenco senza card) |
| 3 | Slide: fondo bianco, «01 · ARGOMENTO», titolo + barretta | **corretto** (era fondo azzurrino, titolo piccolo) |
| 4 | Piè di pagina «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» + «Pagina N» | **corretto**; numerazione 1–40 uguale nel PDF |
| 5 | Riquadro 4:3 con ombra grigia morbida | **corretto**: 412×310 px a x=1428, y=148, angoli r=18 (era un tondo) |
| 6 | Fascia gialla −3°, due righe | **corretto**: «Giorgio Mazzotti» / «PROF. DI LETTERATURA ITALIANA», sempre visibile dove c'è il prof |
| 7 | Slide senza prof | **corretto**: approfondimenti, schemi di ripasso, glossario, riepilogo, mappe in stile Spagnolo (erano pagine blu scuro) |
| 8 | Font | Bricolage Grotesque 800, Figtree (etichette in Figtree Bold come da aggiornamento 15:10) |
| 9 | Finale 5 s con avviso diritti | OK (non toccato) |
| 10 | Struttura | OK: sigla, presentazione, 3 argomenti con approfondimenti, ripasso, quiz; glossario, riepilogo, finale |
| 11 | PDF slide + mappe | consegnati |
Card in corso: bordo giallo sottile + numero su pallino giallo, ombre grigie morbide (aggiornamento 01:30). Titoli lunghi accanto al riquadro ristretti per stare a sinistra (pagine 13 e 26).

## 3. Problemi trovati e correzioni
| Minuto (nuovo) | Tipo | Com'era | Correzione |
|---|---|---|---|
| tutto | visivo | prof nel tondo, nome piccolo senza fascia, slide grigio-azzurre, pagine blu scuro per approfondimenti | tutto rifatto nel modello: 40 pagine |
| 19:19–20:48, 34:33–35:40, 51:04–52:19, 53:14–54:25 (mappe) | contenuto | mappe concettuali **inventate da noi** (6 rami diversi dal prof) con voce corrispondente | sostituite con la **mappa del prof** (`MAPPE/LEZIONE 24.pdf`) impaginata nella nostra grafica, contenuto identico (tolti logo mappe-scuola.com e le due foto). 4 voci nuove: `RM1c`, `RM2c`, `RM3d`, `RMFd` |
| 25:24 (fine D2) | prof | il pezzo del prof finiva a metà frase («…trova il suo culmine nel romanzo») | D2 ora finisce a «…e i sistematici depistaggi istituzionali.»; D3 inizia da «Questo quadro radicalmente negativo e impietoso…» |
| tutti i pezzi del prof | sincronia | evidenziazioni delle card scelte a occhio | rifatte dal parlato del prof (§6 e stime in §5) |
| audio prof | audio | non verificabile se pulito con la catena del kit | rifatto dall'originale: `aresample 48000, highpass 80, arnndn (sh.rnnn), loudnorm −16, alimiter` |
| VF 55:25 | jingle | scheda «Verifica finale» e «Compiti» senza jingle | aggiunto `quiz.wav` a +0,5 s |
| tra i pezzi | transizioni | silenzio nelle transizioni | dissolvenza + `trans.wav` in tutte le transizioni |
| vtt | testo | cue con durata negativa (1:05,153→1:05,144), «Ciasca», «Todomoto», «briantaggio», «debutato», «elento», «deipistagi», «milanti», anni scritti male | rigenerato: 888 cue, max 2 righe, anni in cifre, nomi corretti; testi delle voci Kore presi dai testi originali |
| scheda | testo | titolo «Leonardo Sciascia» | «Letteratura V · Lezione 24 · Leonardo Sciascia»; secondi aggiornati |
| picco audio | audio | 0 dBFS circa | −2,1 dBTP |

## 4. Pagine del libro
Lezione 24: nessuna pagina del libro (regola B-bis non applicabile).

## 5. Cosa NON ho verificato / limiti
- **Ascolto umano:** non ho ascoltato il video. Fruscio/ronzio/metallico dopo `arnndn` **non verificati**.
- **Pronuncia della voce Kore — probabili errori, NON corretti:** la trascrizione automatica rende «L'affaire Moro» come «l'affermoro», «L'affermo oro», «La Fer Moro» in RM3d (nuova), S3 e RF1. Va ascoltato; se è sbagliato, scrivere nel testo della voce «Laffèr Moro» e rigenerare. Altre stranezze nella trascrizione delle voci (non verificate all'ascolto): «Todomoto», «Pultima», «Creta» (= «quarta/ultima»). **Non corretto.**
- **Evidenziazioni delle card** del prof: da parlato (trascrizione Parakeet, tempi parola per parola); incertezza stimata ±2 s. In D2 la card 3 è accesa solo 4,5 s perché il prof alterna le card. Da riguardare in 4 punti.
- **Sincronizzazione delle schede degli approfondimenti** (compaiono sulla parola chiave della voce): stima ±2 s, dove la trascrizione non trova la parola le schede sono spaziate in modo uniforme.
- **Sottotitoli:** riletti per le parole sospette e rigenerati; non riletti cue per cue contro l'audio. Punti di dubbio nel parlato del prof, lasciati con la lettura più probabile: «Ve ritiero?» → «Vero?» (~8:12), «pe i supistieri» → «per i misteri» (~38:40), «scomparsi inserisamente» (~39:55). Da riascoltare.
- **Testa nel riquadro:** webcam originale 184×138 px ingrandita 2,2×: immagine morbida; i capelli toccano il bordo alto già nell'originale (ad es. 2:34): non risolvibile.
- **Quiz:** riletti contro le slide del prof: domande e risposte giuste coerenti. Invariati. Verifica finale = Excel del prof (10 domande), compiti = PDF del prof (4 domande), testo identico.
- **Voce narrante senza immagine:** controllati «ecco/guarda/leggi la frase/linea del tempo»: le immagini nominate ora sono sullo schermo (linee del tempo AN1/AN14/AN17, frase evidenziata AN12/AN19/AN24, mappa). Il controllo è sulla trascrizione, non sull'ascolto.
- **Coda silenziosa 4,2 s** sull'ultima scheda (Compiti): scheda ferma in attesa dell'esercizio.

## 6. Tabelle richieste
### Fine e inizio di ogni pezzo del prof (misurato sulla trascrizione)
| Pezzo | Minuto | Inizio (prime parole) | Fine (ultime parole) | Frase finita |
|---|---|---|---|---|
| D0 | 0:48–1:30 | «Buongiorno e benvenuti alla lezione su Leonardo Sciascia» | «In effetti c'è quest'altra tematica.» | sì |
| D1 | 1:36–10:52 | «Leonardo Sciascia. Allora.» | «…stiamo pure ancora su questa e poi passiamo alla successiva.» | sì |
| D2 | 21:58–25:24 | «Passiamo alla successiva, dopo tutto, perché sto per introdurre l'opera.» | «…e i sistematici depistaggi istituzionali.» | sì (corretto) |
| D3 | 36:43–41:36 | «Questo quadro radicalmente negativo e impietoso trova il suo culmine nel romanzo Todo Modo…» | «…ma che certamente dà fastidio.» | sì |
Tutti i tagli interni ai pezzi del prof (7) sono su pause di 0,6–1,4 s (energia al minimo), non dentro le frasi (misurato).

### Secondi vecchio → nuovo (quiz, verifica, compiti)
| Elemento | Vecchio (s) | Nuovo (s) |
|---|---|---|
| Quiz 1 | 1294,9 | 1307,8 |
| Argomento 2 (T2) | 1300,2 | 1313,1 |
| Quiz 2 | 2191,1 | 2192,9 |
| Argomento 3 (T3) | 2196,4 | 2198,2 |
| Quiz 3 | 3176,6 | 3188,5 |
| Verifica finale | 3307,9 | 3325,4 |
| Compiti | 3332,1 | 3349,6 |
| Durata | 3338,4 | 3355,9 |
`scheda_pubblicazione.json`, `testo_youtube.txt` e `timeline.json` sono aggiornati a questi secondi; la master rigenera la pagina.

## 7. DA CONFERMARE COL PROF
Nella mappa del prof le date non coincidono con slide, voce e Excel. Nella mappa ho lasciato le date del prof:
- **Morte dell'Inquisitore**: mappa 1964; voce degli approfondimenti 1963.
- **L'affaire Moro**: mappa 1978; slide, voce ed Excel (domanda 5) 1979.
- **Porte aperte (1987)**: presente in slide, voce ed Excel ma non nella mappa.
- La mappa dice «A ciascuno il suo (1966)», non trattato nelle slide.

## 8. Come ho verificato
Trascrizione completa (Parakeet TDT, `trascrivi.py`, 760 segmenti), 3338 fotogrammi a 1/s sul video vecchio, correlazione audio per i tagli del prof (7 tagli, ±0,2 s di partenza poi cercati sul minimo di energia), 112 fotogrammi a 1/30 s sul video nuovo (`controllo_minuti.jpg`), misure ffmpeg/ebur128, controllo contiguità (somma dei pezzi = 100 676 fotogrammi).
