# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 12 · Prof. Giorgio Mazzotti
**PRIMA VERSIONE (verifica A+B+C+D parziale) · 16/11/2026 · stato IN_REVISIONE**

## Cosa ho verificato (misurato)
- Ricomposizione dei pezzi: sha256 **corretto** (240b9c1d…). Durata **56:43,5**, 1920×1080, 30 fps, H.264 + AAC.
- Audio: **−17,0 LUFS** integrati (entro −16 ±2). Silenzi > 3 s solo sulle schede Quiz (3,1–3,7 s) e sulle schede finali (verifica/compiti, ~10 s): previsti dalla struttura.
- Trascrizione completa con tempi (770 segmenti): `trascrizione_video_montato.srt`.
- Fotogrammi ogni 2 s (1.702) e riepilogo 1 ogni 30 s: `controllo_minuti_1/2/3.jpg`.
- Originale del prof: 20:41, 1092×614. Nel montato il prof occupa 20:43 (D0–D5, 1.243 s): coerente.
- Verifica finale (Excel del prof): le 10 domande ci sono tutte (confronto dopo aver tolto gli spazi iniziali). Il file di test ha 4+2 colonne per riga di risposte vuote: da pulire.
- Mappa concettuale del prof: trovata nella release (`MAPPE-…zip`, `LEZIONE 12.pdf`, **1 pagina** per tutta la lezione).
- Compiti: `LEZIONE 12.pdf` presente (4 consegne), da confrontare con `compiti.json`.
- Pagine del libro: la lezione 12 non ne ha, punto B-bis saltato.

## Problemi trovati
| Minuto | Tipo | Com'era | Correzione prevista |
|---|---|---|---|
| tutto | visivo | Grafica vecchia: banda laterale blu notte, prof in riquadro piccolo, nome senza fascia gialla, nessuna ombra | Rifare nel modello Spagnolo (punto 000): fondo bianco, riquadro 4:3 ≈410×308, fascia gialla inclinata a due righe |
| 0:17–2:30 | visivo/sync | Presentazione degli argomenti: sulla slide c'è solo il titolo, sullo schermo non ci sono i 5 argomenti (nella slide d'apertura si vedono 3 voci su 5) | Copertina con card «ARGOMENTI» completa (5 argomenti dal pptx) |
| 0:45–2:30 | visivo/sync | Copertina ferma mentre il prof parla | Slide che segue il discorso |
| AN (circa 30 min) | visivo | Schede, confronti, analisi, linee del tempo, mappe, ripassi e glossario sono su fondo blu scuro con font/griglia diversi | Rifare con grafica Spagnolo (slide senza prof: testo grande, giallo solo sulle parole in corso), voci Kore già pronte da riusare |
| ~38:00 | visivo | Scheda «Virginia Woolf e il flusso di coscienza»: carte sovrapposte durante la transizione, testo illeggibile per alcuni fotogrammi | Rifare l'animazione senza sovrapposizione |
| 8:24, 25:59, 38:09, 54:04 | visivo/testo | Mappe concettuali costruite da noi (5 parziali + finale), non quella del prof | Usare la mappa del prof (1 pagina, release) impaginata con matrice v3, contenuto identico |
| fine | testo | Test con colonne di risposte vuote | Allineare al formato dell'Excel del prof (4 risposte) |
| 0–16 s | audio | Sigla: da controllare con `kit/sigle/Sigla_Letteratura_15s.mp4` | Verificare e sostituire se diversa |

## Ancora da fare (prima delle 2 ore)
- OCR di tutte le slide, sottotitoli `.vtt` letti riga per riga, confronto voce–immagine nei punti «ecco / guarda / in questa mappa» (trovati 15 punti, i principali sono le mappe: 8:24, 25:59, 38:09, 54:04: a vista l'immagine c'è).
- Sincronia card gialla / frase del prof (±1,5 s) nelle 5 parti D1–D5; durate delle slide ferme.
- Confronto `compiti.json` con il PDF del prof; scheda_pubblicazione; PDF slide e mappe A4 orizzontale.

## Piano di correzione e tempi (stima)
Rifare tutte le slide nel modello Spagnolo e rendere di nuovo il video con le voci Kore esistenti, riquadro 4:3 dall'originale, audio pulito del kit. Stima: **molto oltre le 4 ore** se si rifà tutto; per questo ho chiesto a Sara se rifare tutto o solo ciò che è sbagliato.

## Cosa non ho potuto verificare finora
Tutto quanto è nella sezione «Ancora da fare».
