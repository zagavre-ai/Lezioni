# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 11 · «Il Futurismo e le avanguardie» (Prof. Mazzotti)
Prima versione (verifica A+B+C+D finita; correzione non ancora consegnata). Stato: IN_REVISIONE. 16/11/2026.

## Cosa ho misurato (M) e cosa è una stima (S)
- (M) Video ricomposto dai 3 pezzi: sha256 **corretto**. 1920×1080, 30 fps, 3263,0 s (54:23), 192,5 MB.
- (M) Trascrizione completa dell'audio con `trascrivi.py` (646 segmenti, tempi parola per parola). Originale del prof: 33:04 (1092×614, bassa risoluzione).
- (M) Parlato del prof 51–772 s: −16,3 LUFS (OK). Nessun silenzio > 2,5 s sotto −45 dB rilevato (controllo di questo tipo fatto sull'intero audio).
- (M) 1632 fotogrammi (uno ogni 2 s) guardati in contact sheet; cambi di slide/evidenziazione misurati per differenza di immagine.
- (S) Rumore dell'audio del prof (fruscio/ronzio/metallico): non verificabile a orecchio qui; la catena del kit sarà rifatta comunque dall'originale.
- Non ho OCR automatico (strumento non installabile in questo ambiente): il testo delle slide è stato letto a vista e confrontato con la dispensa A4 della consegna e con `_videodispensa.pptx`.

## Confronto con il modello Spagnolo (punto 000), punto per punto
| # | Punto | Esito prima | Azione |
|---|---|---|---|
| 1 | Sigla 15 s → dissolvenza → copertina | sigla c'è; copertina subito dopo | da verificare/ricostruire |
| 2 | Copertina (riga DM Mono blu, titolo Bricolage, card ARGOMENTI) | copertina con titolo e elenco, ma stile «LETTERATURA ITALIANA · QUINTO ANNO», senza card | rifare |
| 3 | Slide fondo bianco, «01 · ARGOMENTO», titolo+barretta, card come Spagnolo | slide D bianche con card gialle a bordo; **approfondimenti, schede, ripassi, quiz, glossario, riepilogo su fondo blu scuro** | rifare tutte su fondo bianco |
| 4 | Piè di pagina «LETTERATURA ITALIANA · Prof. Giorgio Mazzotti» + «Pagina N» | presente ma in stile diverso (maiuscolo piccolo, «PAGINA N») | rifare |
| 5 | Riquadro prof 4:3 ~410×308, ombra morbida | **tondo** (non rettangolo, non 4:3) | rifare dal video originale |
| 6 | Fascia gialla col nome su due righe, −3° | **assente** (solo scritta piccola «Prof. Giorgio Mazzotti / LETTERATURA ITALIANA» sotto il tondo) | aggiungere |
| 7 | Slide senza prof (ripassi, glossario…) testo grande, giallo | fondo blu scuro, testo piccolo | rifare |
| 8 | Font Bricolage / Figtree / DM Mono | stile simile ma slide scure usano altro | rifare |
| 9 | Finale kit 5 s con avviso diritti | finale nero con «GRAZIE PER L'ATTENZIONE» **senza avviso dei diritti**; prima c'è una slide «Fine» | sostituire col file del kit |
| 10 | Struttura | sigla, intro, 4 argomenti (T, D, AN, AP, MP, R, S, Q), MPF, GL, RF ok; **dopo il finale ci sono ancora schede «Verifica finale» e «Compiti» (dentro il video)** | tolte dal video (stanno fuori) |
| 11 | PDF A4 slide + PDF mappe | esiste solo una «dispensa» (29 pagine) in vecchia grafica e `Mappe_…pdf` | rifare entrambi |

## Problemi trovati
| Minuto | Tipo | Com'era | Correzione prevista |
|---|---|---|---|
| tutto | visivo | prof nel tondo, nessuna fascia gialla | riquadro 4:3 + fascia, dall'originale |
| 0:51–0:54 | testo | sottotitolo «**Buogiorno** benvenuti» | rigenerati tutti i .vtt dalla trascrizione corretta |
| .vtt | testo | 679 cue, nomi del prof trascritti male in vari punti (es. «Palazzeschi e la sua concessione») | rilettura completa e correzione |
| 38:26 (AN3) | visivo/voce | la voce dice «Ecco le immagini più forti del manifesto» ma sullo schermo non c'è nessuna immagine | frase tagliata (solo voce narrante) + transizione morbida |
| 12:51–… e 33:xx–38:xx | pagina libro | pagine del Manifesto e del Monologo di Molly in **bassa risoluzione, ritagliate dal video**, righe illeggibili (<26 px) | rifatte con le «fettine» dagli screen HD (Lez11_p377–379, p399–402) |
| 50:xx | struttura | slide «Fine» + finale senza avviso diritti + schede VF/Compiti dopo il finale | struttura corretta |
| tutto | visivo | fermi: da misurare slide per slide (la sincronia evidenziazione/frase verrà ricontrollata sul video nuovo) | |
| compiti.json | dati | formato `compiti/risposta_aperta` invece di `esercizi/aperta` | formato di regole |
| scheda_pubblicazione.json | dati | titolo «Il Futurismo e le avanguardie» | «Letteratura V · Lezione 11 · Il Futurismo e le avanguardie» |
| Test xlsx | dati | 10 domande identiche all'Excel del prof | OK |
| Compiti | dati | 4 domande identiche al PDF del prof | OK (solo formato) |
| Mappe | contenuto | mappa del prof `LEZIONE 11.pdf` (A5, 1 pagina) in release; nel video ci sono mappe proprie per argomento | da rifare con la mappa del prof (vedi sotto) |

## Libro (B-bis)
Brani con pagina: T1 «Manifesto del Futurismo» (Marinetti) pp. 377–379; T9 «Il monologo di Molly» (Joyce) pp. 399–402. Screen HD presenti nella release (`Lez11_ingrandita.zip`, 7 file).

## Piano di correzione e tempi (S)
Ricostruzione di tutte le slide in grafica Spagnolo (HTML→PNG), riquadro 4:3 + fascia dall'originale con la catena audio del kit, fettine HD, finale del kit, ricodifica, PDF A4, rifacimento sottotitoli e nuova verifica: circa 3–4 ore.
