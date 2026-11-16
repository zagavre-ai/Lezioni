# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 25 · Pasolini
**Versione 1 (16/11/2026, prima stima, non ancora corretta). Stato: IN_REVISIONE.**
Misurato = ffprobe/ebur128/fotogrammi guardati. Stima = dichiarato.

## Verifica fatta finora
- Video montato ricomposto, sha256 **OK**. Misurato: 1920×1080, 30 fps, **2718,9 s = 45:19**, 166 MB, AAC 48 kHz, parlato **−16,5 LUFS** (nel range).
- Originale del prof (release): 1092×614, 20:06. Il prof è una **webcam piccola** (circa 245×138 px) dentro una registrazione dello schermo. Il riquadro 4:3 (410×308) sarà un ingrandimento ×1,7–2,2: la nitidezza ha un limite fisico (stima). Da dichiarare, non risolvibile.
- Materiali nella release: Excel «DOMANDE LEZIONE 25.xlsx» presente; PDF compiti «LEZIONE 25» presente (4 domande, `compiti.json` coincide); **mappa del prof «LEZIONE 25.pdf» presente** (zip MAPPE).
- Lezione senza pagine del libro (punto B-bis: non applicabile).
- Trascrizione Whisper in corso; OCR e contact sheet da fare.

## Problemi trovati (confronto con il modello Spagnolo, punto 000)
| # | Punto | Minuto | Tipo | Com'è | Correzione prevista |
|---|---|---|---|---|---|
| 1 | 000-3 slide | 1:17→ | visivo | Slide su fondo grigio chiaro/blu notte, etichetta «ARGOMENTO 1 · …», titolo non Bricolage 800 | Fondo bianco, riga DM Mono «01 · NOME», titolo Bricolage 800 + barretta blu |
| 2 | 000-4 piè di pagina | tutto | visivo | «LETTERATURA ITALIANA · Prof. Giorgio Mazzotti · Pagina N» tutto a sinistra, senza «V» | Sinistra «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti», destra «Pagina N» |
| 3 | 000-5 riquadro | tutto | visivo | Riquadro piccolo a sinistra del contenuto (≈190 px), bordo blu, banda blu scura laterale | 4:3 ≈410×308 a x≈1428 y≈146, ombra grigia, nessun bordo; ritaglio dall'originale con correzione kit |
| 4 | 000-6 fascia gialla | tutto | visivo | Nome in testo bianco piccolo «Prof. Giorgio Mazzotti / LETTERATURA ITALIANA», niente fascia | Fascia gialla −3°, «Giorgio Mazzotti» + «PROF. DI LETTERATURA ITALIANA» |
| 5 | 000-2 copertina | 0:53 | visivo | da verificare | come modello |
| 6 | 000-7 slide senza prof | approfondimenti, glossario | visivo | Fondo blu notte (approfondimenti AN01–16, glossario, ripasso) | Fondo bianco, testo grande, evidenziazioni gialle, logo e piè di pagina |
| 7 | 000-10 / durata | totale | struttura | Durata 45:19 (<50). Il prof parla 20 min; il resto è grafica | Da decidere con Sara: l'originale non basta per 50 min. Non si allunga con riempitivi. |
| 8 | Brief | 44:50→ | visivo | Slide Verifica finale con **banda blu** e fondo nero in dissolvenza | Verifica e compiti fuori dal video (000-10); sostituire con finale kit |
| 9 | Pagine PDF A4 | — | testo | La dispensa è A4 verticale? da controllare; mancano i due PDF orizzontali slide + mappe | Produrre `_slide.pdf` e `_mappe.pdf` A4 orizzontale |
| 10 | Verifica finale | — | pagina | Nota «manca la verifica finale» (nota di Sara) | `Test_…xlsx` da rifare dall'Excel del prof, 10 domande |

(I punti 5 e 9 sono da confermare con OCR/fotogrammi: non ancora verificati.)

## Piano e tempi (stima)
1. Trascrizione + coerenza voce/immagine + silenzi + rumore (ascolto di 3 punti): 1 h.
2. OCR slide e rilettura `.vtt`: 40 min.
3. Rifare tutte le slide nel modello Spagnolo (HTML→PNG 1080p, font del kit), riquadro 4:3 con `trova_cam`/`allinea`, fascia gialla, rimontaggio e `finale_a_pezzi.py`: 3–4 h.
4. PDF A4, mappe del prof con matrice v3, quiz/test/compiti/scheda: 1 h.
**Totale stima 5–6 h oltre il tempo già usato: oltre le 4 ore previste.** Lo scrivo a Sara ora.

## Non ancora verificato
Tutto A (ascolto), C (OCR, `.vtt`), sincronia slide–labbra, tabella 1–11 definitiva.
