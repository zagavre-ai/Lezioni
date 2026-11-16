# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 24 (prima versione, in corso)

Stato: IN_REVISIONE. Lezione NON ancora corretta.

## Verificato (misurato)
- Video montato ricomposto dai pezzi: sha256 OK, 1920x1080, 30 fps, 55:38 (3338,4 s), 163,5 MB, H.264 + AAC.
- Scaricati dalla release: originale Letteratura_Lez24.mp4 (369 MB), MAPPE.zip, compiti zip, Excel zip. Lez24 non ha pagine del libro (B-bis non si applica).
- Guardati i fotogrammi ogni 30 s (`sheet0-4.jpg`, prime 111 immagini).

## Confronto con il modello Spagnolo (punto 000), dal primo esame visivo
| # | Punto | Esito |
|---|---|---|
| 1 | Sigla 15 s + dissolvenza | sigla nera presente; dissolvenza da verificare |
| 2 | Copertina | DIVERSA: riga «LETTERATURA ITALIANA · QUINTO ANNO», titolo piccolo, elenco «GLI ARGOMENTI DI OGGI» senza card ARGOMENTI; nome prof sotto il titolo |
| 3 | Slide | DIVERSE: fondo grigio-azzurro (non bianco), titolo piccolo |
| 4 | Piè di pagina | presente («Prof. Giorgio Mazzotti», Pagina N): da controllare |
| 5 | Riquadro 4:3 con ombra grigia | NON conforme: prof in TONDO |
| 6 | Fascia gialla inclinata a due righe | NON conforme: nome piccolo con sottolineatura gialla |
| 7 | Slide senza prof | pagine blu scuro (linea del tempo, schede, parole chiave): NON conformi al modello (fondo bianco) |
| 8 | Font | da controllare con OCR |
| 9 | Finale 5 s | da verificare |
| 10 | Struttura | presenti sigla, argomenti, pillole «RIPASSO», quiz, glossario, riepilogo; da verificare in dettaglio |
| 11 | PDF A4 | presenti dispensa e mappe nel ramo consegna: da confrontare col video |

## Cosa NON ho ancora potuto fare
- Trascrizione (Whisper) e OCR: strumenti non installati e l'installazione con pip non è stata autorizzata dall'ambiente.
- Verifica sincronia, audio (-16 LUFS, rumore), .vtt, compiti, quiz, verifica finale, mappe del prof.
- Rifare grafica e riquadro 4:3: richiede il rifacimento di tutte le slide (le sorgenti HTML non sono nel ramo consegna; ci sono solo video e PDF).

## Piano
1. Installare Whisper+OCR (serve consenso) e fare A+B+C+D.
2. Ritagliare il prof 4:3 dall'originale e rifare slide in stile Spagnolo (sorgenti da ricostruire da dispensa/timeline).
3. Ricodificare, controlli, PDF, consegna. Stima: oltre le 4 ore previste.
