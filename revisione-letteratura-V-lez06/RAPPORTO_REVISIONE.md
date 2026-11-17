# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 6 · Decadentismo e Simbolismo
**PRIMA VERSIONE (17/11/2026, circa 1 ora dalla partenza). Stato: IN REVISIONE. Consegna prevista: 04:30 (ora italiana).**
Etichette: **misurato** = misurato con uno strumento; **stima** = dedotto; **non verificato** = non ho potuto.

## 1. Cosa ho verificato finora
- Video vecchio ricomposto dai 2 pezzi: sha256 uguale a quello del file `.sha256` (**misurato**). 1920×1080, 30 fps, 95 638 fotogrammi, 53:07,9.
- Trascrizione completa con `trascrivi.py` del video vecchio (692 segmenti) e dell'originale del prof (362 segmenti, 31:00). 3 188 fotogrammi a 1/s sul video vecchio.
- Il prof è stato allineato all'originale per correlazione audio: offset costante in ognuno dei 5 pezzi (D1…D5), quindi l'originale è usato per intero e in ordine (**misurato**).

## 2. Problemi trovati nel video vecchio
| Minuto | Tipo | Com'era |
|---|---|---|
| tutto | visivo | prof nel tondo; fondo azzurrino; titoli e card diversi dal modello Spagnolo; etichette in DM Mono; ripassi e glossario con piè «Ripasso» e senza numero di pagina; schede nere/blu di titolo, quiz, verifica e compiti fuori modello |
| 1:03–2:59 | sincronia | slide degli argomenti ferma 116 s, evidenziazione assente (misurato con differenza tra fotogrammi) |
| 4:22–6:12 · 6:19–7:13 | sincronia | stessa card evidenziata per 110 s e 54 s mentre il prof passa dai gruppi d'avanguardia alla reazione degli artisti e agli esponenti |
| 14:19–15:47 | sincronia | «Languore: l'analisi» ferma 88 s |
| 25:03–26:06 · 30:29–31:37 · 32:01–33:22 | sincronia | slide ferme 63, 68 e 81 s |
| D1–D5 | contenuto | le slide mostrate non sono quelle del prof (`_videodispensa.pptx`): schede riscritte («Una corrente culturale europea», «Languore: l'analisi»…) con frasi che il prof non ha scritto |
| 8:xx, 17:xx, 26:xx, 35:xx, 45:xx | contenuto | 5 mappe + mappa finale **inventate da noi** (nodi non del prof). La mappa del prof è una sola («I “POETI MALEDETTI”») |
| vtt | testo | errori nelle prime righe: «benvenute la lezione», «distudiarlo», «dispiegarlo»… (667 cue da rileggere tutti) |
| fine | consegna | mancano `…_slide.pdf`, `…_mappe.pdf`, `verifica_finale.json`; titolo scheda non standard |

## 3. Piano di correzione (tempo stimato)
1. Rifare tutta la lezione nel modello Spagnolo: slide dal pptx del prof, riquadro 4:3, fascia, stessi fotogrammi del vecchio (95 638) → quiz, verifica e compiti restano agli stessi secondi (circa 2 h).
2. Mappa del prof al posto delle mappe inventate: nuove voci `R6…R11` (già arrivate), pezzi di uguale durata (fatto).
3. Sottotitoli rifatti e riletti, PDF slide e mappe, `verifica_finale`, `compiti`, `scheda` (circa 1 h).
4. Controlli sul video nuovo e rapporto definitivo (circa 30 min).
