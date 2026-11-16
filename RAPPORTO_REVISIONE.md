# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 26 · Italo Calvino (Prof. Giorgio Mazzotti)
**Versione 1 (16/11/2026, entro le 2 ore) · stato: IN_REVISIONE** — verifica fatta, correzione in corso.

## Come ho verificato (misurato / stimato)
- Video montato: pezzi ricomposti, sha256 **OK** (364e9af1…). Misurato: 1920×1080, 30 fps, 55:29,7, 99.891 fotogrammi, 166,7 MB.
- Visione: fotogrammi ogni 2 s (1.665) e contact sheet ogni 30 s (`cs0–cs3.jpg`); confronto con `kit/modello_spagnolo/`. Fotogrammi puntuali guardati a vista nei punti critici.
- Audio **misurato**: parlato −16,3 LUFS (target −16 ±2: OK), picco −0,7 dBFS, nessun silenzio > 3 s tranne gli ultimi 7,9 s (coda del finale).
- Testo: `.vtt` (722 cue, tutte ≤ 2 righe) riletto con elenco delle parole sospette; quiz, Excel, compiti, mappa del prof confrontati con i file della release.
- **NON ho potuto verificare:** la trascrizione indipendente con Whisper. Dall'ambiente della chat il download del modello è bloccato dalla rete (HuggingFace e simili: 403/non raggiungibili). Per l'ascolto uso il `.vtt` esistente (fatto da Whisper sul video finale) + testi delle voci Kore (`testi_voci.json`) + misure con ffmpeg. Le sincronie «ecco/guarda/in questa foto» le controllo quindi sui testi, non su una nuova trascrizione. Né l'OCR delle slide né il confronto visivo sono stati bloccati (tesseract installato).

## Confronto con il modello Spagnolo (punti 1–11 del punto 000)
| # | Punto | Esito | Nota |
|---|---|---|---|
| 1 | Sigla → dissolvenza → copertina | da ricontrollare | sigla ok per durata; la transizione verso la copertina va guardata fotogramma per fotogramma (0:15–0:17) |
| 2 | Copertina (card ARGOMENTI, titolo, riga blu, logo) | **DA CORREGGERE** | niente card «ARGOMENTI» come Spagnolo; l'elenco dice «Il secondo Calvino» per l'argomento 4, che nel video si chiama «Scienza, combinatoria e città invisibili» |
| 3 | Slide: fondo bianco, riga «01 · ARGOMENTO», titolo Bricolage + barretta | **DA CORREGGERE** | fondo grigio-azzurro (non bianco); testo delle card minuscolo; titolo senza barretta blu sulle slide «approfondimento» |
| 4 | Piè di pagina «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» + «Pagina N» | **DA CORREGGERE** | a destra compaiono «Introduzione», «Approfondimento», «Ripasso», «Glossario» e numeri di pagina ripetuti/non progressivi invece di «Pagina N» |
| 5 | Riquadro 4:3 (410×308), ombra grigia, nessun bordo | **DA CORREGGERE** | oggi è un **tondo** con bordo; da rifare 4:3 dall'originale (che è 1092×614: il prof sta in un riquadro piccolo in basso a destra, quindi il ritaglio è ingrandito: qualità limitata, lo scrivo in chiaro) |
| 6 | Fascia gialla col nome su due righe | **DA CORREGGERE** | oggi c'è solo un testo piccolo sotto il tondo, senza fascia gialla |
| 7 | Slide senza prof | da correggere | stessa grafica da portare a fondo bianco, testo grande |
| 8 | Font (Bricolage / Figtree / DM Mono) | da ricontrollare con OCR | etichette in mono ok |
| 9 | Finale `Sigla_finale_5s_con_avviso_diritti` | **DA CORREGGERE** | c'è un finale nero «GRAZIE PER L'ATTENZIONE» senza avviso dei diritti, e dopo di esso una card «Compiti» (ordine sbagliato) |
| 10 | Struttura obbligatoria | in gran parte ok | presentazione, 5 argomenti con ripasso e quiz, glossario, riepilogo ci sono. Il glossario ha solo 3 voci |
| 11 | PDF A4 orizzontale slide + mappe | **MANCANTI** | in consegna c'è solo una dispensa; non i due PDF richiesti |

## Problemi trovati (prima tabella)
| Minuto | Tipo | Com'era | Correzione prevista |
|---|---|---|---|
| tutta la lezione | visivo | prof nel tondo con bordo, nome senza fascia gialla | riquadro 4:3 + fascia gialla come Spagnolo, ritaglio dall'originale con correzione immagine del kit |
| tutta la lezione | visivo | fondo grigio-azzurro, testo piccolo | fondo bianco, testo grande, modello Spagnolo |
| 0:15–1:00 | visivo | copertina senza card ARGOMENTI; argomento 4 con nome diverso | card ARGOMENTI su due colonne, titoli identici a quelli del video |
| 1:08 | audio/visivo | il prof dice «ecco appunto una sua fotografia» ma sullo schermo non c'è alcuna foto | la slide 2 del prof contiene la foto (`Immagine p2`): la metto a tempo |
| ~12:00 | visivo | confronto «Calvino e Pavese»: terza card tagliata e sovrapposta al piè di pagina | slide rifatta con card che stanno nella pagina |
| ~22:00 | visivo | confronto «Lo sguardo di un bambino»: terza card tagliata sul piè di pagina | idem |
| 5 punti | visivo | 5 mappe + 1 finale **inventate da noi** (es. «Barone rampante e realismo»), non quelle del prof | mappa del prof (file `LEZIONE 26.pdf` nel pacchetto MAPPE della release) impaginata con la matrice v3; contenuto identico: **vita / pensiero / opere** con le 5 famiglie di opere e gli anni; tolgo il logo «mappe per la scuola» e la foto del personaggio pubblico; nessuna mappa inventata |
| 55:20–55:29 | audio | 7,9 s di silenzio in coda; finale nero senza avviso | finale kit da 5 s con avviso diritti; card «Compiti» fuori dal video |
| `.vtt` | testo | **molti errori di trascrizione** (es. «Nacordo», «Itholo Calvino», «Santiago della Svegas», «polliedri», «Inetiamo», «viragno», «Napolone», «spicolazione», «slaque», «tricene»…) | riletto tutto e corretto; riallineo ai tempi del video nuovo (±0,3 s) |
| compiti | testo | `compiti.json` è una lista di 4 frasi, non nel formato `{"titolo","esercizi":[{n,tipo,testo}]}`; «meta- romanzo» spezzato | riscritto nel formato richiesto, testo identico al PDF del prof |
| quiz/verifica | testo | Verifica finale: **10 domande identiche all'Excel del prof: OK (confrontate riga per riga)** | nessuna modifica |
| consegna | file | mancano i due PDF A4 orizzontali (slide identiche al video; mappe) | prodotti dopo il video nuovo |
| pagine del libro | — | la lezione 26 non ha pagine del libro (regola B-bis: salta) | — |

## Piano di correzione (stima) e rischi
1. Rifare le slide in grafica Spagnolo (fondo bianco, testo grande, mappe del prof) — **~1,5 h**.
2. Rifare il riquadro 4:3 e la fascia gialla sul video del prof dall'originale; audio del prof con la catena del kit — **~1 h** (la sorgente è piccola: qualità limitata dall'originale).
3. Riusare le voci Kore già fatte; per le mappe nuove servono **frasi nuove** (R1…): la master le genera in 10–30 min.
4. Codifica con `finale_a_pezzi.py`, controlli, `.vtt` corretto, PDF A4, rapporto finale — **~1 h**.
**Rischio dichiarato:** il kit non contiene il modello `arnndn` citato nelle regole e non c'è il file `timeline.json` della lezione: dovrò ricostruire i tempi dal video montato. Se a metà tempo non ci sto lo scrivo subito.

*(Versione 1 — in corso)*
