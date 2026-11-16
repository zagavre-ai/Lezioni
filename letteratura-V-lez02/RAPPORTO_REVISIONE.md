# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 2 · La Scapigliatura
**Versione 1 (prima versione, 16/11/2026) · stato: IN REVISIONE**
Video controllato: `Letteratura_Lez2_Parte1_1080p.mp4` del ramo `consegna-letteratura-V-lez02` (sha256 ricomposto = file `.sha256`: OK).

## 1. Che cosa ho MISURATO (strumenti) e che cosa è una STIMA
| Controllo | Risultato | Tipo |
|---|---|---|
| Durata / formato | 59:17,1 · 1920×1080 · 30 fps · 222,6 MB | misurato |
| Volume parlato | −16,2 LUFS integrato (ebur128) | misurato |
| Silenzi > 2 s | 24, tutti sulle schede Quiz/titolo (5 s di scheda muta) **tranne** 3531–3539 s e 3549–3557 s (vedi problema 4) | misurato |
| Sottotitoli `.vtt` | 739 blocchi; «Scapigliatura» scritta bene 24 volte, nessun «lettatura» | misurato (solo ricerca di termini) |
| Fotogrammi ogni 60 s e ogni 30 s (`controllo_minuti.jpg`) | guardati a vista | misurato |
| Video originale del prof (release) | 1092×614, 39:19; il montato dura 59:17 (con schede, ripassi, mappe, glossario) | misurato |

**NON ho potuto verificare (blocco tecnico):**
- **Trascrizione audio completa (Whisper): non eseguibile.** Il modello va scaricato da `huggingface.co`, che da questa macchina è bloccato dalla rete (403 del proxy). Quindi punti A1–A3 della verifica (frase per frase, «ecco/guarda…», tagli dentro le frasi, sincronia labbra) **non sono ancora fatti**. Serve: sbloccare `huggingface.co` (o un file modello Whisper `small` in una release), oppure la trascrizione dalla master.
- OCR automatico delle slide (nessun OCR installato): il testo delle slide l'ho letto a vista solo su un campione; refusi non ancora esclusi.
- Ascolto dei 3 punti per fruscio/ronzio/metallico: non possibile qui (nessun ascolto); misuro solo il volume.

## 2. Problemi trovati finora
| # | Minuto | Tipo | Com'è | Correzione prevista |
|---|---|---|---|---|
| 1 | tutte le slide con il prof (dal minuto 0:46 alla fine del ripasso finale) | visivo | Prof nel **TONDO** (≈300 px, x≈1700 y≈400), nome su una riga sotto il tondo («Prof. Giorgio Mazzotti» + «LETTERATURA ITALIANA»), niente fascia gialla | Riquadro **4:3 410×308 a x≈1428 y≈146**, angoli arrotondati, ombra grigia, ritaglio dall'originale con testa e spalle intere, correzione immagine kit; fascia gialla −3° su due righe «Giorgio Mazzotti» / «PROF. DI LETTERATURA ITALIANA» |
| 2 | tutto | visivo | **Modello grafico diverso da Spagnolo (punto 000)**: fondo grigio-azzurro invece di bianco; barretta **gialla** invece di blu; etichetta in alto «LETTERATURA ITALIANA» invece di «01 · NOME ARGOMENTO»; nessun filetto sotto il logo; piè di pagina con numeri/etichette diverse («Introduzione», «Ripasso», «Testo dal libro · Pagina 41»); il nome del piè di pagina cambia da slide a slide (a vista: «PROF. GIORGIO MAZZOTTI» in maiuscolo nei ripassi, «Prof. Giorgio Mazzotti» altrove); card con bordo giallo su fondo grigio | Rifare tutte le slide con il modello `kit/modello_spagnolo/` (fondo bianco, barretta blu, «0N · ARGOMENTO», piè di pagina «LETTERATURA ITALIANA · Prof. Giorgio Mazzotti» + «Pagina N», tabelle/card come Spagnolo) |
| 3 | 0:15–0:46 | visivo | Copertina: la lista dei 7 argomenti è su una sola colonna e **l'ultima voce («Dualismo di Arrigo Boito») tocca il filetto del piè di pagina**; manca il titolo grande con barretta come Spagnolo e la riga «LETTERATURA ITALIANA V · VIDEOLEZIONE» | Copertina del modello, card «ARGOMENTI» su due colonne |
| 4 | 58:51–59:17 | visivo + audio | **Finale rotto:** «GRAZIE PER L'ATTENZI» **tagliato** e fuori centro (testo a metà schermo), senza logo e senza avviso dei diritti; **8 s di silenzio totale** (3549–3557 s) e altri 7 s muti (3531–3539 s). Non è la sigla del kit | Sostituire con `kit/sigle/Sigla_finale_5s_con_avviso_diritti.mp4` (5 s) |
| 5 | glossario (≈ 3300 s) | visivo/testo | Nel fotogramma campione il glossario mostra una sola parola («Bohémien») in evidenza; non ho verificato le altre schede | Verificare e completare |
| 6 | slide «Testo dal libro» (Preludio e Dualismo, 2ª metà della lezione; minuti esatti da fissare con la trascrizione) | pagina | Le pagine del libro (Preludio p. 38–39, Dualismo p. 41–44) compaiono come **pagina intera rimpicciolita** dentro una card, con righe poco leggibili; la regola B-bis chiede le **«fettine» dallo screen HD**, rigo ≥ 26–30 px, evidenziate a tempo | Rifare dalle 6 immagini HD della release (`Lez02_p038/039/041/042/043/044.png`), ritagli sulle righe bianche, senza intestazioni/numeri pagina/QR |
| 7 | slide «Dualismo di Arrigo Boito» (nota a destra) | pagina/visivo | La nota a destra («2. cherubo: …») risulta **tagliata** in fondo («…vagare per il mondo.» a metà) | Con le fettine HD |
| 8 | mappe | visivo | Le mappe (una per argomento + finale) sono su fondo grigio con grafica non del modello; devono essere **quelle del prof** (release `MAPPE.zip` → `LEZIONE 2.pdf`) in matrice v3 | Confronto contenuto con `LEZIONE 2.pdf` e reimpaginazione; PDF mappe A4 |
| 9 | PDF | testo | Mancano i due PDF A4 orizzontali nuovi: `…_slide.pdf` (slide identiche al video, senza riquadro) e `…_mappe.pdf`. Nel ramo consegna c'è «Dispensa» e «Mappe» vecchie | Da generare dopo il rifacimento |
| 10 | .vtt | testo | `controllo_finale.py` della consegna segnava **sottotitoli 64% < 80%** («DA SISTEMARE»); consegnata comunque | Rigenerare con `sub_finale.py` sul video nuovo |
| 11 | compiti / verifica | testo | **Excel della verifica: identico byte per byte** a quello del prof (OK). **Compiti:** testo identico ai primi esercizi di `LEZIONE 2.pdf` (confronto completo da finire), ma `compiti.json` ha chiavi `compiti`/`risposta_aperta`/`stato` invece del formato richiesto `{"titolo","esercizi":[{"n","tipo":"aperta","testo"}]}` | Riscrivere nel formato richiesto |

## 3. Piano di correzione e tempi (stima)
1. Sblocco trascrizione (vedi §1) — **serve da Sara/master**; senza, A1–A3 restano non verificati.
2. Ricostruzione di tutte le slide in grafica Spagnolo (HTML → PNG 1080p) a partire dai testi già nel video e dalle slide del prof (`Letteratura_Lez2_videodispensa.pptx`): ~1,5 h.
3. Riquadro 4:3 + fascia gialla: ritaglio dall'originale 1092×614 (la qualità è limitata dalla sorgente: 410×308 è reso in 1:1, nessun ingrandimento oltre il 100%), allineamento con `kit/tools/rettangolo/`: ~1 h.
4. Pagine del libro dalle immagini HD: ~1 h.
5. Ricodifica, finale kit, `.vtt`, PDF A4 (slide e mappe), controlli, rapporto finale: ~1 h.
Totale stimato: **~4,5 h dalla partenza** (entro 5 h), a condizione che la trascrizione si sblocchi nella prima ora.

## 4. Tabella di confronto con il modello (punto 000) — stato attuale
| Punto | Esito |
|---|---|
| 1 Sigla → dissolvenza → copertina | sigla ok (15 s Letteratura); da guardare la dissolvenza |
| 2 Copertina | **da correggere** (problema 3) |
| 3 Slide (fondo bianco, «0N · ARGOMENTO», barretta blu) | **da correggere** (problema 2) |
| 4 Piè di pagina | **da correggere** (problema 2) |
| 5 Riquadro 4:3 | **da correggere** (problema 1) |
| 6 Fascia gialla | **da correggere** (problema 1) |
| 7 Slide senza prof | **da correggere** (grafica, problema 2) |
| 8 Font | Bricolage/Figtree/DM Mono presenti: ok a vista |
| 9 Finale kit | **da correggere** (problema 4) |
| 10 Struttura (presentazione, 7 argomenti con ripasso e quiz, glossario, riepilogo) | presente (timeline: 7 quiz, 7 ripassi, 7 mappe, 2 approfondimenti, GL, RF, mappa finale) |
| 11 PDF A4 | **mancano** (problema 9) |

Allegato: `controllo_minuti.jpg` (1 fotogramma ogni 30 s del video attuale).
