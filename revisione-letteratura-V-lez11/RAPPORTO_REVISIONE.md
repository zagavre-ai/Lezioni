# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 11 · «Il Futurismo e le avanguardie» (Prof. Giorgio Mazzotti)
Versione finale · 16/11/2026 · stato: REVISIONATA (da riguardare dalla master). Ramo: `revisione-letteratura-V-lez11`.

**Scrivo sempre che cosa ho MISURATO (M) e che cosa è una STIMA/lettura a vista (S).**

## 1. Risultato in numeri (M)
| | Prima (consegna) | Dopo (revisione) |
|---|---|---|
| Durata | 54:23 (3263,0 s) | **51:40 (3100,36 s)** |
| Fotogrammi | – | **93.010 = durata × 30** (controllato) |
| Peso | 192,5 MB | **240,5 MB** (< 400) |
| Formato | 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192k 48 kHz | uguale |
| Volume totale | – | **−15,8 LUFS** integrati; **picco vero −1,3 dBTP** (misurato con `ebur128=peak=true`; prima 0,0). Parlato del prof normalizzato a −16 LUFS |
| Silenzi > 3 s | 8 (schede titolo e quiz) | **0** (4 silenzi tra 2,5 e 3 s) |
| Scatto quiz (4 quiz) | – | **scarti +0,019 / +0,019 / +0,019 / +0,018 s** (limite 0,05) |
| Sha256 | ricomposto, uguale al file | `…parte_00/01/02` + `.sha256` (controllato) |

## 2. Confronto con il modello Spagnolo (punto 000), punto per punto
| # | Punto | Esito |
|---|---|---|
| 1 | Sigla 15 s → dissolvenza → copertina | **corretto**: sigla Letteratura del kit, dissolvenza di 0,7 s verso la copertina |
| 2 | Copertina | **corretto**: riga DM Mono blu «LETTERATURA ITALIANA V · VIDEOLEZIONE», titolo Bricolage 800 con barretta, card «ARGOMENTI» (4 argomenti) |
| 3 | Slide fondo bianco, «01 · ARGOMENTO», titolo+barretta, card | **corretto**: tutte le slide rifatte su fondo bianco (prima: approfondimenti, schede, ripassi, quiz, glossario su fondo blu scuro) |
| 4 | Piè di pagina | **corretto**: «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» + «Pagina N» in **Figtree Bold** spaziato (64 pagine, mai il numero della lezione) |
| 5 | Riquadro prof 4:3 ~410×308, ombra morbida, niente bordo | **corretto**: 412×310 px a x=1428, y=148, angoli arrotondati, ombra grigia. Ritaglio 4:3 dall'**originale del prof** (release) con correzione immagine del kit (contrasto 1,04, saturazione 1,03, hqdn3d 1.5:1.5:3:3, cas 0,35). Il tondo non c'è più |
| 6 | Fascia gialla col nome | **corretto**: due righe, −3°, «Giorgio Mazzotti» / «PROF. DI LETTERATURA ITALIANA», sempre visibile dove c'è il prof |
| 7 | Slide senza prof | **corretto**: testo grande (29–36 px), parole chiave evidenziate in giallo, stesso logo e piè di pagina |
| 8 | Font | **corretto dopo il controllo master (15:10)**: Bricolage Grotesque 800 (titoli) e Figtree; la riga «01 · ARGOMENTO», la riga della copertina, il piè di pagina e le etichette sono in **Figtree Bold maiuscolo spaziato**, come `slide_1080p_esempio.png`. DM Mono non è più usato (video, PDF slide, PDF mappe) |
| 9 | Finale | **corretto**: `Sigla_finale_5s_con_avviso_diritti.mp4` del kit. Tolte la slide «Fine», la scheda «Verifica finale» e le due schede «Compiti» che stavano dentro il video |
| 10 | Struttura | **OK**: sigla → presentazione → per argomento: titolo, prof, approfondimenti, ripasso (voce + schema), quiz → glossario → riepilogo → finale. Verifica finale (10 domande) e compiti restano fuori dal video |
| 11 | PDF A4 | **fatti**: `…_slide.pdf` (64 pagine) e `…_mappe.pdf` (1 pagina) |

## 3. Problemi trovati e corretti
| Minuto (vecchio video) | Tipo | Com'era | Come l'ho corretto |
|---|---|---|---|
| tutto | visivo | prof nel tondo, nessuna fascia gialla, fondo blu scuro in metà del video, stile diverso da Spagnolo | tutto rifatto in grafica Spagnolo (vedi §2) |
| 0:51 | testo | sottotitolo «**Buogiorno** benvenuti» | .vtt rifatto da zero sull'originale pulito (499 cue); ora «Buongiorno» |
| 12:51–… e 33:xx–38:xx (vecchio) | pagina libro | Manifesto (pp. 377–379) e Monologo di Molly (pp. 399–400) in **bassa risoluzione**, ritagliati dal video, righe < 26 px; la fettina restava ferma per 100 s mentre il prof leggeva i punti 6–11 | rifatte dagli screen HD della release (rigo ≈ 36 px a 1080p), 9 fettine a tempo con la lettura (tabella §5) |
| 38:26 (AN3) | voce/visivo | la voce dice «Ecco le immagini più forti del manifesto» ma sullo schermo non c'è alcuna immagine | **tagliata** quella frase (solo voce narrante, 4,5 s) |
| Mappe | contenuto | 5 mappe «inventate» dalla produzione (MP1–MP4 e MPF) | tolte. Resta **solo la mappa del prof** (`MAPPE/LEZIONE 11.pdf`, esiste una sola mappa: sul Futurismo), impaginata nella nostra grafica dopo l'argomento 2, con **voce nuova MPD1** (aggiunta a `testi_voci.json`, generata dalla master) |
| Schede animate | visivo | schede a card su fondo scuro (linea del tempo, schede) | sostituite da slide bianche con testo evidenziato **frase per frase in sincronia con la voce** (tempi dalle parole della voce) |
| 46–47 (T1…T4) e quiz | audio | 8 silenzi di 3,2–3,8 s (schede titolo di 5 s, coda delle schede quiz) | schede titolo 2,9 s, schede quiz 4,9 s: nessun silenzio > 3 s; scatto quiz invariato |
| fine | struttura | slide «Fine», finale senza avviso dei diritti, poi schede VF/Compiti | finale del kit, schede esterne tolte |
| Audio prof | audio | non verificabile a orecchio | **rifatto dall'originale** con la catena del kit: aresample 48000, highpass 80, arnndn, loudnorm −16, alimiter (vedi limiti) |
| Q1 domanda 5 | quiz | «scrittura automatica dei surrealisti»: non è nel materiale del prof | sostituita: «Chi guida il Surrealismo, nato in Francia nel 1924?» → André Breton |
| compiti.json | dati | formato `compiti/risposta_aperta` | formato `esercizi/aperta`; testo identico al PDF del prof (4 domande, controllato) |
| scheda_pubblicazione.json | dati | titolo «Il Futurismo e le avanguardie» | «Letteratura V · Lezione 11 · Il Futurismo e le avanguardie» |
| Test | dati | – | 10 domande identiche all'Excel del prof (controllato) |

## 4. Verifica (che cosa ho fatto davvero)
- **A · Ascolto (M):** trascrizione completa con `trascrivi.py` del video montato (646 segmenti) e dell'originale pulito. Cercati «ecco / guarda / in questa… / come vedete»: l'unico caso senza immagine è AN3 (tagliato); «Ecco la mappa…» cade con la mappa sullo schermo. Allineamento dell'audio del prof con il vecchio montaggio: scarto ≤ 0,03 s (correlazione 0,94–0,97). Frasi tagliate o ripetute: non trovate. **Non ho ascoltato a orecchio** (fruscio/ronzio/«metallico»): non verificabile qui.
- **B · Visione (M/S):** 1632 fotogrammi (uno ogni 2 s) del video vecchio e 104 del nuovo (`controllo_minuti.jpg`, uno ogni 30 s). Cambi di evidenziazione misurati a 10 fps su tutti i 4 argomenti; per ogni stato ho letto la trascrizione del tratto e confrontato con la card evidenziata: nessuna card contraddice il parlato. Tenute lunghe ma coerenti: copertina 0:51–4:25 (il prof presenta il corso e gli argomenti, che sono sullo schermo), card 3 «Espressionismo tedesco» 7:09–8:35, card 3 «Futurismo e fascismo» 20:23–… (il prof parla di fascismo). (S: ±1,5 s controllato a campione, non su ogni cambio.)
- **C · Testo (M/S):** slide lette a vista (nessun OCR automatico installabile) e confrontate con `Letteratura_Lez11_Dispensa.pdf` e `Lez11_docente.pdf`. PDF slide: **64 pagine**, ognuna confrontata con il fotogramma del video (scarto medio massimo 0,85 su 255, zona senza prof): **le pagine coincidono**. PDF mappe: 1 pagina.
- **D · Dati (M):** vedi §3.

## 5. Brani del libro (B-bis)
| Brano | Pagina | File HD | Minuto (video nuovo) |
|---|---|---|---|
| T1 Marinetti, Manifesto del Futurismo (titolo e introduzione) | 377 | Lez11_p377.png | 31:30–31:36 |
| punti 1–3 | 377 | Lez11_p377.png | 31:36–32:06 |
| punti 4–5 | 377 | Lez11_p377.png | 32:06–33:37 |
| punti 6–8 | 378 | Lez11_p378.png | 33:37–34:23 |
| punti 9–10 | 378 | Lez11_p378.png | 34:23–34:54 |
| punto 11 | 378 | Lez11_p378.png | 34:54–36:01 |
| «È dall'Italia che noi lanciamo…» | 378 | Lez11_p378.png | 36:01–36:22 |
| T9 Joyce, Il monologo di Molly (inizio, da «Sì perché prima…») | 399 | Lez11_p399.png | 45:12–45:41 |
| continuazione («e per l'anima sua spilorcia…») | 400 | Lez11_p400.png | 45:41–45:55 |
La pagina 379 e le pagine 401–402 non sono lette dal prof: non inserite.

## 6. Limiti e cose da sapere (da dire a Sara)
1. **Riquadro del prof:** l'originale è una registrazione dello schermo 1092×614 in cui il prof sta in un riquadro di **247×138 px**. Il ritaglio 4:3 è 184×138 px ingrandito ×2,2: **più morbido del modello Spagnolo**; non si può fare meglio senza un video originale con la sola webcam. In più **la testa è al limite alto già nell'originale** (la fronte/i capelli toccano il bordo) per tutta la lezione.
2. **Modello audio `arnndn` del kit:** nel repository non c'è. Ho usato il modello rnnoise «somnolent-hogwash» (GregorR/rnnoise-models, da GitHub). Va riascoltato dalla master.
3. **Sottotitoli:** fatti sul solo parlato del prof (come `sub_finale.py`), da trascrizione automatica sull'originale pulito + correzione di nomi e termini. Il prof parla in modo molto colloquiale: **alcune frasi restano approssimative** e circa 15 frammenti senza senso sono stati tolti (es. 1–2 parole in inglese inventate dal riconoscimento). Non ho potuto riascoltarli: **da controllare a campione dalla master**. Nomi propri controllati con ricerca sistematica (Baudelaire, Apollinaire, Majakovskij, Tzara, Breton, Joyce, Svevo, Palazzeschi, Die Brücke, Der Blaue Reiter…).
4. **Mappe:** il prof ne ha mandata **una sola** (Futurismo). Per gli argomenti 1, 3, 4 e per la mappa finale **non ci sono mappe del prof**: non le ho inventate. Se Sara le carica, si aggiungono.
5. **Picco:** il picco campione arriva a 0 dBFS dopo la codifica AAC (parlato a −16 LUFS): da guardare se la master vuole più margine.
6. Strumenti: `finale_a_pezzi.py` e `controllo_finale.py` usano percorsi della macchina della master (`/home/claude/…`) e non girano qui: ho fatto una sola codifica x264 per gruppo (veryfast CRF 19) e un solo AAC 192k, poi unione senza ricomprimere; i controlli equivalenti (fotogrammi, silenzi, LUFS, scatto quiz con riferimento ricavato dal vecchio video, PDF/fotogrammi) sono nelle tabelle sopra.

## 6-bis. Correzioni dopo il controllo della master
1. Font delle etichette: DM Mono → Figtree Bold in tutte le slide del video, nel PDF slide (64 pp.) e nel PDF mappe. Video rimontato: stessi tempi, stessi fotogrammi.
2. Picco audio: limitatore sull'audio finale, picco vero **−1,3 dBTP** (era 0,0). Durata 3100,363 s e **93.010 fotogrammi** identici; scatto dei quiz entro +0,02 s; nessun silenzio > 3 s.
3. Fettina di Molly (p. 400): mancava la prima riga («e per l'anima sua spilorcia…»); ora c'è.
4. Aggiunto `controllo_fettine.jpg` (un fotogramma per ognuna delle 9 fettine).

## Cosa NON ho verificato
Ascolto a orecchio (rumore, metallico, sincronia labiale); correttezza di ogni frase dei sottotitoli; i tempi delle evidenziazioni su ogni cambio (±1,5 s solo a campione).

## 7. File consegnati (cartella `revisione-letteratura-V-lez11/`)
`Letteratura_Lez11_Parte1_1080p.mp4.parte_00/01/02` + `.sha256`, `Letteratura_Lez11_Parte1.vtt`, `Letteratura_Lez11_slide.pdf` (A4 orizz., 64 pp.), `Letteratura_Lez11_mappe.pdf` (A4 orizz.), `quiz_argomenti.json`, `Quiz_Letteratura_Lez11.txt`, `Test_Letteratura_Lez11.xlsx`, `compiti.json`, `scheda_pubblicazione.json`, `testo_youtube.txt`, `timeline.json`, `controllo_minuti.jpg`, `controllo_fettine.jpg`, questo rapporto. Voce nuova: `scambio/letteratura-V-lez11/` sul ramo `voci-letteratura-V-lez11` (MPD1).
