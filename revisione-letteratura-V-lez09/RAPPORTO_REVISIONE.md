# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 9 (Giovanni Pascoli) · VERSIONE 1 (piano)
Chat di revisione 9 · stato **IN_REVISIONE** · prima versione del rapporto: verifica A+B+C+D fatta sul video vecchio, correzione in corso.
Etichette: **[misurato]** = misura con strumento · **[stima]** · **[non verificato]**.

## 0. Cosa ho scaricato e controllato
- `consegna-letteratura-V-lez09`: Parte 1 e Parte 2 ricomposte dai pezzi, **sha256 uguale** a quello consegnato (P1 `c47fd3f3…`, P2 `d76b112d…`) [misurato].
- Release `mazzotti-letteratura-V`: `Letteratura_Lez9.mp4` (1092×614, 69:17), `Letteratura_Lez9_videodispensa.pptx` (45 slide), `Lez09_ingrandita.zip` (11 pagine HD, 2352×3141 px), mappa `LEZIONE 9.pdf`, compiti `LEZIONE 9.pdf`, Excel `DOMANDE LEZIONE 9.xlsx`.
- Trascrizione di tutto l'audio con `trascrivi.py` (parola per parola) e 1 fotogramma al secondo di P1 e P2 (3318 + 3309 fotogrammi) [misurato].

## 1. Misure sul video vecchio (consegnato)
| | Parte 1 | Parte 2 |
|---|---|---|
| Durata | 55:18,5 (99 554 fotogrammi) | 55:09,7 (99 290 fotogrammi) |
| Risoluzione | 1920×1080, 30 fps | idem |
| Volume parlato | −16,2 LUFS | −17,7 LUFS (primi 4 s) / vedi controllo completo |
| Picco | −1,5 dBFS (primi s) | −2,8 dBFS |
**Struttura reale (misurata sulle cross-correlazioni audio):** i pezzi del prof (D1–D4) sono **contigui nell'originale**: P1 = 0,57–1951,5 s; P2 = 1950,97–4157,0 s. Somma pezzi = originale meno ~1,2 s. Il piano di rimontaggio manterrà **gli stessi fotogrammi** (P1 99 554, P2 99 290) → quiz, verifica e compiti restano agli stessi secondi su Vimeo.

## 2. Confronto col modello Spagnolo (punto 000) — video VECCHIO
| # | Punto | Esito sul vecchio | Azione |
|---|---|---|---|
| 1 | Sigla → dissolvenza → copertina | sigla c'è | da verificare/rifare transizione |
| 2 | Copertina: logo, riga blu, titolo Bricolage, card ARGOMENTI | **no**: fondo grigio, fascia blu a destra, titolo non in stile | rifare |
| 3 | Slide fondo bianco, «01 · ARGOMENTO», barretta | **no**: fascia blu laterale, titolo con «Parte 1 · Argomento 1 · …» in DM Mono | rifare |
| 4 | Piè di pagina «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» + «Pagina N» | parziale (DM Mono, piccolo) | rifare in Figtree Bold |
| 5 | Riquadro 4:3 con ombra grigia, senza bordo blu | **no**: rettangolo piccolo con bordo giallo/blu su fascia scura | rifare 4:3 ≈ 412×310 |
| 6 | Fascia gialla, 2 righe, −3° | **no**: testo «Prof. Giorgio Mazzotti» in DM Mono sotto il riquadro | rifare |
| 7 | Slide senza prof | presenti, ma etichette in DM Mono e fondo grigio | rifare |
| 8 | Font solo Bricolage/Figtree (etichette Figtree Bold) | DM Mono usato ovunque | rifare |
| 9 | Finale `Sigla_finale_5s_con_avviso_diritti.mp4` | da verificare | usare quello del kit |
| 10 | Struttura obbligatoria | presente (intro, argomenti, ripasso, quiz, glossario, riepilogo, finale) | mantenere |
| 11 | PDF slide A4 + PDF mappe A4 | `Mappe_…pdf` del vecchio contiene mappe **inventate** | rifare |

## 3. Problemi trovati (video vecchio) — tabella
| Dove | Tipo | Com'era | Correzione prevista |
|---|---|---|---|
| tutto | visivo | grafica non Spagnolo (vedi §2) | rifare tutte le slide nel modello |
| P1 ~0:50–1:10 e P2 | visivo | la copertina mostra gli argomenti ma con fascia blu | copertina con card ARGOMENTI come Spagnolo |
| P1 4:10 (orig. 3:23) | visivo/audio | il prof dice «Ecco, questa è una sua fotografia»: **la foto non è sullo schermo** (slide 2 del prof, 3 s) | metto la foto (dalla slide 2 del prof) a tempo [±3 s] |
| P1 22:06 (orig. 14:59) | visivo | il prof dice «Pascoli, ecco Pascoli e le due sorelle»: **la foto non è sullo schermo** (slide 5) | metto la foto dalla slide 5 |
| tutti i MAPPA_* (10 pezzi, 34–57 s) | visivo/contenuto | mappe **inventate** da noi, nodi che compaiono uno alla volta; per decine di secondi si vede **solo il nodo centrale** (es. P1 ≈ 17:40 «Il nido familiare»); non sono la mappa del prof | rifare con i nodi **del prof** (`LEZIONE 9.pdf`), nostra grafica, senza il marchio «MAPPE per la SCUOLA» (marchio di terzi) |
| pagine del libro (T2 «Una poetica decadente», T6, T7, T8, T9, T10, T13) | visivo/pagina | pagine a **bassa risoluzione** dal video; si vedono **QR code**, etichetta «AUDIOLETTURA», colonne di note tagliate a metà riga, intestazioni | fettine dagli screen HD, tagliate su righe bianche, solo colonna del brano, QR/note/intestazioni fuori |
| slide del prof ↔ testo | testo | alcune slide hanno il testo **riscritto** (es. «lutti familiari» al posto di «numerosi luttuosi destini familiari») | testo uguale alla slide del prof (`.pptx`) |
| P2 ~3:00 verso la fine di arg. 3 | struttura | il prof passa ai **Poemetti** (slide 42) a **orig. 3665 s**, ma il montaggio mette il titolo «Argomento 4» a 3972 s: ~5 min di Poemetti stanno nell'argomento 3 | da verificare nel rimontaggio; se serve spostare un confine lo scrivo con la tabella vecchio→nuovo dei quiz |
| voce Kore | audio | «Mirìce» (accento sbagliato) al posto di «Mìricae» in INTRO1, S4, GL, riepiloghi | frasi nuove `R1, R2…` in `testi_voci.json` (push sul ramo voci) e rimontaggio |
| quiz | contenuto | verifica 10 domande: Excel del prof ha una risposta sbagliata «Italy» (domanda 4) e una risposta corretta con testo guasto («L'aria è del gemma, il sole così chiaro») | **DA CONFERMARE COL PROF** (non decido io) |
| P2 | contenuto | slide/mappa: **1906** (mappa del prof) ≠ **1905** (slide, voce, Excel) per la cattedra a Bologna; mappa: «occhi **stupidi** del bambino» | **DA CONFERMARE COL PROF**: nel video lascio quello che dice il prof in ciascun documento |
| compiti | contenuto | scheda Compiti generica; testo dei compiti del prof è in `compiti.json` | scheda Compiti nel modello + testo del prof |
| dispensa | testo | `Dispensa_…pdf` del vecchio ≠ slide del video | nuovo PDF slide = slide del video |

## 4. Piano di correzione (tempi stimati) [stima]
1. Slide, copertina, riquadro 4:3 (ritaglio webcam 184×138 → 412×310, ingrandita 2,2×: **limite noto, immagine morbida**), fascia, pezzi D1–D4: 1,5–2 h.
2. Fettine HD con controllo (`controllo_fettine.jpg`): 1 h.
3. Approfondimenti, mappe del prof, glossario, riepilogo, quiz, verifica, compiti nel modello; audio prof pulito dall'originale (già fatto: −17,1 LUFS, picco −1,5 dBFS [misurato]): 1,5 h.
4. Voci nuove R1.. (servizio master 10–30 min), rimontaggio, sottotitoli, PDF, controlli: 1 h.
**Consegna prevista: entro 5 ore dalla partenza (lezione lunga, in due parti con pagine del libro).**

## 5. Cosa NON ho ancora verificato
- Ascolto della sola voce Kore (non posso sentirla: confronto solo con la trascrizione automatica).
- OCR completo dei fotogrammi del vecchio (in corso), sincronia fine di tutte le card del vecchio.
- Parte 2: trascrizione in corso.

## 6. Come ho verificato
Cross-correlazione audio originale↔montato (offset dei pezzi del prof, costanti su 3 punti per pezzo), trascrizione parola per parola, ricerca di «ecco/guarda/vedete/in questa foto…», rilevamento dei cambi slide nell'originale, abbinamento delle 33 fettine del prof alle pagine HD (match 0,89–1,00, scala 1,0), misure ebur128 e silencedetect.
