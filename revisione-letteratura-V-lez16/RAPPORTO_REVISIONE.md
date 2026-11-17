# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 16 · Umberto Saba
Revisione del 17/11/2026. Video corretto: `Letteratura_Lez16_Parte1_1080p.mp4` (a pezzi `.parte_00…`, sha256 nel file `.sha256`).
Regola: **misurato** = misurato con uno strumento; **stima** = dedotto; **non verificato** = non ho potuto.

## 1. Misure sul video nuovo
| Controllo | Risultato |
|---|---|
| Formato | 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192k 48 kHz, codificato una sola volta con `finale_a_pezzi.py` |
| Durata / fotogrammi | durata 3311.700 s (55:11.7) · fotogrammi 99351 (attesi 99351) OK · 1920x1080 · 30/1 fps · peso 205.9 MB |
| Quiz e posizioni | **cambiano 2 secondi per i pezzi del prof tagliati a fine frase (§3-bis):** Q1 958,4 s e Q4 3139,77 s uguali a prima; **Q2 1694,97 s (era 1693,67) e Q3 2821,03 s (era 2823,33)**; GL, RF, FIN, verifica 3293,2 s e compiti 3306,7 s uguali. Nuovi secondi in `scheda_pubblicazione.json`, `timeline_P1.json`, `testo_youtube.txt` |
| Volume | volume integrato -16.3 LUFS · picco reale −1,0 dBTP (**al limite**: nel WAV prima della codifica AAC era −1,5) |
| Jingle Quiz (`controllo_jingle.py`) | Q1 atteso 958.900 trovato 958.900 scarto +0.000 OK<br>Q2 atteso 1695.467 trovato 1695.466 scarto -0.001 OK<br>Q3 atteso 2821.533 trovato 2821.532 scarto -0.001 OK<br>Q4 atteso 3140.267 trovato 3140.265 scarto -0.002 OK |
| Silenzi | silenzi > 3 s (soglia −50 dB): **uno solo, 55:03–55:11 (7,8 s)**: schede finali Verifica/Compiti sotto la pagina interattiva (era uguale nel video vecchio). Un silenzio di 6 s a 45:26 (dopo la voce della mappa 3, più corta del tempo disponibile) è stato tolto rallentando la voce del 6 % e centrandola |
| Fermi immagine del prof (`freezedetect` sul riquadro, ≥ 1 s, nei pezzi del prof) | nessuno |
| Sincronia audio/video del prof | audio: max 1.75 ms (misurato, correlazione sull originale, 15 punti); video: max 2 fotogrammi (misura grossolana sul riquadro: il rumore del confronto è ±2 fotogrammi; per costruzione audio e immagine del prof escono dallo stesso fotogramma dell originale) |
| PDF | slide: 59 pagine A4 orizzontale (testo selezionabile, **stesso layout del video senza riquadro e fascia**); mappe: 5 pagine A4 orizzontale |
| Sottotitoli | 845 blocchi, max 2 righe da 42 caratteri, max 6,6 s; **95,7 %** dei blocchi parte con la voce presente entro 0,4 s (misurato sull audio finale) |

## 2. Confronto col modello Spagnolo (punto 000)
| # | Punto | Esito |
|---|---|---|
| 1 | Sigla 15 s → dissolvenza → copertina | OK: sigla invariata, dissolvenza dal nero di 0,8 s sulla copertina (misurato a vista) |
| 2 | Copertina (logo, riga «LETTERATURA ITALIANA V · VIDEOLEZIONE», titolo, card ARGOMENTI) | **corretto** (era un cartello con elenco senza card) |
| 3 | Slide: fondo bianco, «01 · ARGOMENTO», titolo + barretta, card | **corretto** (era fondo azzurrino, titolo e card diversi; card gialle con ombra a blocco) |
| 4 | Piè di pagina «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» + «Pagina N» | **corretto** (era «VIDEOLEZIONE» al posto del numero) |
| 5 | Riquadro 4:3, ombra grigia, niente bordo blu | **corretto**: 412×309 px a x=1428, y=148, angoli arrotondati, ombra grigia morbida (era un rettangolo 16:9 con bordo blu) |
| 6 | Fascia gialla −3°, due righe, sempre visibile | **corretto**: «Giorgio Mazzotti» / «PROF. DI LETTERATURA ITALIANA» (era una riga di testo senza fascia) |
| 7 | Slide senza prof | **corretto**: approfondimenti, ripassi, mappe, glossario, riepilogo rifatti nel modello |
| 8 | Font | Bricolage Grotesque 800, Figtree (etichette e piè in Figtree Bold come nel modello). DM Mono non usato |
| 9 | Finale 5 s con avviso diritti | **corretto**: `Sigla_finale_5s_con_avviso_diritti.mp4` del kit, con il suo audio, a 55:00 (nel video vecchio c'era un nero «GRAZIE» senza avviso) |
| 10 | Struttura | OK: sigla, presentazione, 4 argomenti (prof, approfondimenti, ripasso, quiz), glossario, riepilogo, finale; schede Verifica e Compiti dopo il finale |
| 11 | PDF slide + mappe | consegnati: `…_slide.pdf` (59 pagine A4 orizzontale), `…_mappe.pdf` (5 pagine) |

Card «in corso» come da aggiornamento 01:30: bordo giallo sottile, numero su pallino giallo, le altre card con bordo grigio chiaro; ombre grigie morbide ovunque.

## 3. Problemi trovati e correzioni
| Minuto | Tipo | Com'era | Correzione |
|---|---|---|---|
| tutto | visivo | grafica diversa dal modello: fondo grigio, riquadro con bordo blu 16:9, nome senza fascia, piè «VIDEOLEZIONE», card gialle | rifatta tutta nel modello Spagnolo (257 schermate: slide del prof, approfondimenti, ripassi, mappe, glossario, riepilogo, schede di servizio) |
| slide del prof | testo | le card riportavano testi **riscritti** (es. «terapia psicanalitica nel 1929-1931» non è nella slide) | card con il testo esatto del `_videodispensa.pptx` del prof |
| 2:03 orig. (2:21 video) | visivo | il prof dice «questa è una fotografia di Umberto Saba» ma la foto non c'era | inserito il ritratto dalla slide 2 del prof (ritaglio senza grafiche dell'editore) — **DA CONFERMARE** da Sara |
| 30:40–33:19 | pagina | nessuna pagina del libro mentre il prof legge «Città vecchia» | 5 fettine dagli screen HD (§4) |
| 26:17–26:26 (vecchio) | audio | **frase ripetuta**: «C'è anche un confronto con il simbolismo…» detta due volte dalla voce (8,4 s) | tolta la prima ripetizione; durata invariata con 5 pause allungate di 1,7 s (nessun silenzio > 3 s) |
| 14:15–15:08, 26:54–27:34, 45:30–46:23, 50:50–51:41, 52:25–53:28 (vecchio) | contenuto | mappe **inventate da noi** («la parola chiave è identità…») | rifatte con la mappa del prof, contenuto identico, nostra grafica; 5 voci Kore nuove (`MAP1`, `MAP2b`, `MAP3b`, `MAP4b`, `MAPFb`); MAP1 accelerata 8 %, MAP2 4 %, MAPF 12 % per stare nel tempo |
| 0:15–2:21 e altri | sincronia | evidenziazioni «stimate ±3 s», card mai accese | rifatte dal parlato del prof (tempi parola per parola); card in corso con bordo giallo e pallino |
| 5 pezzi del prof | taglio | 4 pezzi iniziavano o finivano **a metà frase** («Direi che…», «…umana del dolore», «…ultimi testi di cui…») | tagliati a fine/inizio frase (§3-bis) |
| fine | audio/visivo | finale: nero «GRAZIE» senza avviso diritti | `Sigla_finale_5s_con_avviso_diritti.mp4` con il suo audio (55:00) |
| passaggi | audio | assenti i jingle di ripasso e le transizioni | `repaso.wav` sui 4 ripassi, `trans.wav` sui 7 passaggi, dissolvenza dal bianco (0,25 s) tra i pezzi, dal nero (0,8 s) sulla copertina |
| tutto | audio | parlato del prof non pulito | rifatto dall'originale: `aresample 48000, highpass 80, arnndn (sh.rnnn), loudnorm −16, alimiter`; −16,3 LUFS, picco −1,5 dBTP |
| vtt | testo | 776 blocchi Whisper base, solo 53 % degli attacchi sulla voce, errori («Savo», «trestino», «Sveo»…) | rifatti: 845 blocchi (prof + voci Kore + mappe); ~150 blocchi del prof riscritti a mano |
| slide ferme > 45 s con il prof | sincronia | vedi sotto | non risolvibili: copertina 124 s, ritratto 146 s, «disturbi psicologici» 112 s (il prof parla del contesto di Trieste), «leggi razziali» 120 s (il prof commenta la card), «poesia terapeutica» 55 s |
| 45:26–45:32 | audio | (nuovo, trovato nel controllo finale) silenzio di 6 s nella mappa 3 | voce `MAP3b` rallentata del 6 % e spostata: nessun silenzio > 3 s tranne le schede finali |
| scheda | testo | «Umberto Saba · Parte 1» | «Letteratura V · Lezione 16 · Umberto Saba» |
| fine | consegna | mancavano PDF slide/mappe, `verifica_finale.json`, compiti nel formato | prodotti (10 domande dell'Excel del prof, 4 compiti identici al PDF) |


## 3-bis. Fine e inizio di ogni pezzo del prof (aggiornamento 01:25)
| Pezzo | Minuto inizio | Prime parole | Minuto fine | Ultime parole | Frase finita |
|---|---|---|---|---|---|
| D1 | 0:15.00 | «Buongiorno e benvenuti alla lezione su Umberto…» | 2:19.63 | «…riprenderà tante tematiche. Allora. Direi che possiamo iniziare.» | sì (pausa dopo l'ultima parola 0.5 s) |
| D2 | 2:23.13 | «Questa è appunto una fotografia di Umberto…» | 10:35.47 | «…la parte dei traumi infantili, nel millovecentocinquant sette.» | sì (pausa dopo l'ultima parola 1.0 s) |
| D3 | 16:06.90 | «Quindi un personaggio che ha avuto una…» | 22:21.23 | «…solidarietà basato sulla comune esperienza umana del dolore.» | sì (pausa dopo l'ultima parola 0.6 s) |
| D4 | 28:23.47 | «Analizziamo il canzoniere. appunto il corpus poetico…» | 39:25.37 | «…E poi, appunto, in chiusura, come avevo detto.» | sì (pausa dopo l'ultima parola 0.8 s) |
| D5 | 47:09.53 | «Abbiamo anche... ultimi testi di cui abbiamo…» | 48:46.53 | «…nei testi più significativi che abbiamo, appunto. Visto.» | sì (pausa dopo l'ultima parola 1.2 s) |

I pezzi D1–D2, D3–D4, D4–D5 sono tagliati in pause tra una frase e l'altra: i tagli erano a metà frase nel video vecchio (D1/D2 a «Direi che possiamo…», D3/D4 a «…umana del dolore.», D4/D5 a «ultimi testi di cui…»). D2–D3 era già in una pausa. D1 inizia a «Buongiorno…» e D5 finisce con «Visto.», entrambi estremi dell originale.

## 3-ter. Secondi vecchi → nuovi (quiz, verifica, compiti)
La durata totale resta 3311,7 s (99 351 fotogrammi). Cambiano solo i secondi di due argomenti, perché tre pezzi del prof sono stati tagliati a fine frase. Valori già aggiornati in `scheda_pubblicazione.json` (`inizio_s`, `quiz_s`, `t_verifica`, `t_compiti`, `durata_s`) e in `timeline_P1.json`; `quiz_argomenti.json` non contiene secondi (domande e risposte invariate).
| Evento | Vecchio (s) | Nuovo (s) |
|---|---|---|
| Titolo argomento 1 (`inizio_s`) | 138,50 | **139,63** |
| Quiz 1 (`quiz_s`) | 958,40 | 958,40 |
| Titolo argomento 2 | 963,40 | 963,40 |
| Quiz 2 | 1693,67 | **1694,97** |
| Titolo argomento 3 | 1698,67 | **1699,97** |
| Quiz 3 | 2823,33 | **2821,03** |
| Titolo argomento 4 | 2828,33 | **2826,03** |
| Quiz 4 | 3139,77 | 3139,77 |
| Glossario | 3208,37 | 3208,37 |
| Riepilogo | 3248,91 | 3248,91 |
| Finale | 3286,94 | 3286,94 |
| Verifica finale (`t_verifica`) | 3293,21 | 3293,21 |
| Compiti (`t_compiti`) | 3306,71 | 3306,71 |
| Durata (`durata_s`) | 3311,71 | 3311,70 |

## 4. Pagine del libro in alta risoluzione (B-bis)
Zip `Lez16_ingrandita.zip`: pagine 679 e 680 (T6 «Città vecchia», Saba). Nel video vecchio **non c'era nessuna pagina del libro** mentre il prof leggeva la poesia: aggiunte 5 fettine dagli screen HD. Ogni fettina è una sola colonna, inizia e finisce su una riga bianca (controllato a vista su `controllo_fettine.jpg`); via intestazione del capitolo, numero di pagina, QR e box «Analisi interattiva».
| # | Brano | Pagina | Parte | File HD e ritaglio (px) | Minuto |
|---|---|---|---|---|---|
| 1 | Città vecchia (Canzoniere) | 679 | testata e metro (senza numero di pagina e box editore) | `Lez16_p679.png x 490–2200, y 264–662` | 30:40–31:39 |
| 2 | Città vecchia (Canzoniere) | 679 | versi 1–4 | `Lez16_p679.png x 770–1640, y 698–972` | 31:39–31:55 |
| 3 | Città vecchia (Canzoniere) | 679 | versi 5–10 | `Lez16_p679.png x 770–1640, y 985–1335` | 31:55–32:09 |
| 4 | Città vecchia (Canzoniere) | 679 | versi 11–19 | `Lez16_p679.png x 770–1640, y 1330–1868` | 32:09–32:29 |
| 5 | Città vecchia (Canzoniere) | 680 | versi 20–22 | `Lez16_p680.png x 740–1560, y 262–452` | 32:29–33:19 |
Abbinamento fettina → voce: fatto a mano leggendo la trascrizione parola per parola; è una **stima di ±1 s** (nessuna verifica all'ascolto).

## 5. Cosa NON ho verificato
- **Pronuncia delle 5 voci nuove delle mappe** (aggiornamento 08:45: nomi come Poli, Sabaz, Carolina Wolfer, Svevo): nessun nome latino o straniero difficile; trascritte automaticamente e coerenti col testo, ma **non ascoltate**. Se una è sbagliata va rigenerata con una `R…`.
- **Nessun ascolto umano.** Tutto è automatico: trascrizione (Parakeet), correlazioni, misure. Pronuncia delle voci Kore **non verificata** (in particolare nomi: Sabaz, Poli, Svevo).
- **Sottotitoli del prof:** corretti da una trascrizione automatica; ~150 blocchi riscritti a mano **senza riascoltare**. Ricostruiti «a senso» (da riascoltare): «Edoardo Weiss» (6:15 orig.), «La rima è ABBA… casa, vecchia, specchia, strada» (19:14 orig.), «celebratrice» (15:31 orig.), «dell'estetismo dannunziano» (12:25 orig.), «Un viaggio di vita» (27:05 orig.), alcune frasi spezzate dal prof.
- **Testi che il prof legge a voce** non confrontati riga per riga con le fonti, salvo la poesia (fettine).
- **Rigo ≥ 26–30 px (B-bis):** le fettine dei versi sì; la fettina della testata/metro (30:40) ha un testo più piccolo (≈ 20 px): è larga 1710 px e sta in 1305 px. Non risolto.
- **Testa nel riquadro:** misurato: capelli a contatto col bordo alto per 8 s su 1750 s nell'originale; webcam 183×137 px ingrandita 2,25×, quindi morbida. Limite dell'originale.
- **Sincronia video** del prof: misura grossolana ±2 fotogrammi (il prof è quasi fermo), per costruzione 0.
- **Transizioni:** dissolvenza dal bianco solo tra i pezzi grandi, non ad ogni cambio di card.
- **Flash/luminanza** non misurati con strumento (solo a vista: slide bianche, nessun lampo).

## DA CONFERMARE COL PROF
- Padre di Saba: **«cristiano»** nelle slide del prof, **«cattolico»** nella mappa del prof.
- «Ernesto»: la mappa dice **1975**, le slide dicono «scritto nel 1953 e pubblicato postumo» (la mappa è nel video com'è).
- «Storia e cronistoria del Canzoniere»: 1948 (mappa e parlato); le slide non danno la data.
- La mappa aggiunge fatti non nelle slide (1906 Firenze, 1908 libreria, 1909 matrimonio con Lina, 1955 ricovero a Gorizia); nel parlato il prof cita «Milano» tra i luoghi di fuga, non nella slide.
- Ritratto di Saba (slide 2 del prof): inserirlo o no, ritagliato come ora?

## 6. Come ho verificato
- Scaricati e ricomposti i pezzi del video vecchio (sha256 uguale), originale, slide del prof, mappa, zip HD, Excel e PDF dei compiti dalla release.
- Trascrizione con `trascrivi.py` dell'originale (29 min) e del video vecchio (55 min), tempi parola per parola; allineamento audio vecchio↔originale per correlazione (offset esatti dei 5 pezzi del prof).
- Slide: generate in HTML (modello Spagnolo, misure da `slide_1080p_esempio.png`) e renderizzate con Chromium; riquadro 4:3 ricavato dalla webcam dell'originale, correzione del kit (contrasto 1,04, saturazione 1,03, hqdn3d, cas 0,35).
- Piano dei pezzi contiguo, 99 351 fotogrammi = durata × 30; verifica con `verifica.py`/`verifica2.py` (ffprobe, ebur128, silencedetect, freezedetect, correlazioni) e `controllo_jingle.py` del kit. Miniature: `controllo_minuti.jpg` (1 ogni 30 s), `controllo_fettine.jpg`.
- Controllo PDF↔video: le pagine PDF sono lo stesso HTML delle slide del video (senza riquadro, fascia e evidenziazione).
