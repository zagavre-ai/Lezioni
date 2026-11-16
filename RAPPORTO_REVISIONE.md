# RAPPORTO REVISIONE · Letteratura V · Lezione 5 (Verga) · PRIMA VERSIONE, 16/11

Stato: **IN REVISIONE**. Verifica **parziale**: finora solo visione a campione. Misurato = M, stima = S.

## Fatto
- Pezzi ricomposti, sha256 corretto (M). Video 1920×1080, 30 fps, 3417,7 s = 56:57, 247,5 MB (M).
- Scaricati dalla release: originale `Letteratura_Lez5.mp4`, `videodispensa.pptx`, `Lez05_ingrandita.zip` (screen HD), mappe, compiti, Excel.
- Contact sheet a campione (1 fotogramma ogni 30 s): `revisione/sheet0.jpg`, `sheet2.jpg`, `sheet5.jpg`.

## Problemi trovati finora (visione, M)
| Minuto | Tipo | Com'era | Correzione prevista |
|---|---|---|---|
| tutto | visivo | prof nel **tondo** con bordo; non 4:3 | riquadro 4:3 ~410×308 con ombra grigia, ritaglio dall'originale |
| tutto | visivo | **fascia gialla** col nome assente (c'è solo testo piccolo sotto il tondo) | fascia −3° su due righe |
| tutto | visivo | fondo **grigio-azzurro**, non bianco | fondo bianco come Spagnolo |
| 0:30–1:00 | visivo | copertina senza logo in alto a sinistra, riga «QUINTO ANNO» invece di «LETTERATURA ITALIANA V · VIDEOLEZIONE»; elenco argomenti a una colonna in card piccola | rifare come modello |
| 0:41 ss. | visivo | etichetta «01 · …» presente, ok; piè di pagina «Pagina N» da controllare | controllare |
| ~48–54 | visivo | slide di ripasso e glossario con **onda audio** decorativa in alto a destra, non nel modello | togliere |
| ~57:00 | visivo | **fotogramma nero con linea** a fine video: finale non è `Sigla_finale_5s_con_avviso_diritti.mp4`? | verificare e sostituire |
| 18–28 | pagina | pagine del libro intere (T3, T9, T10) con rigo piccolo, molte ritagliate male e QR/codici dell'editore visibili | rifare «fettine» da `Lez05_ingrandita.zip` |
| fine | struttura | quiz non visti nei campioni; verifica finale e compiti sono fuori dal video | preparare `compiti.json` e verifica da Excel |

## Aggiornamento · ascolto (A) con trascrivi.py — misurato
- Trascrizioni complete con tempi: `revisione/trascrizione_video_montato.srt` (636 segmenti) e `revisione/trascrizione_originale_prof.srt` (547). Originale del prof: 48:56.
- Volume del montato: **−15,9 LUFS** integrato (nel limite −16 ±2), LRA 6,1; picco vero **−1,0 dBTP** (al limite: va abbassato un po' per stare sotto −1) (M).
- Silenzi > 3 s tra segmenti di parlato (M): 0:00–0:16 (sigla), 0:40–0:45, 10:34–10:47 (12 s), 28:45–28:56, 33:24–33:34, 44:07–44:17, 54:18–54:26. Quelli a 10:34, 28:45, 33:24, 44:07 coincidono con le fine-argomento/quiz (schede quiz): **da confermare all'ascolto**, non sono errori certi.
- `.vtt`: 649 cue. Errori sicuri trovati: «cicolo dei vinti» (righe 897, 1329, 1368, 1451), «Malavoglia, ad acordo, alla voglia», «mal voglio in»; «Mastro-don Gesualdo» non compare mai nel `.vtt` mentre la trascrizione lo sente 20 volte: i sottotitoli sono da rileggere tutti (M, parziale).
- Frasi con «vedete / guardate / ecco qui» (M): 1:05, 14:41, 19:43 («eccolo qui in tutta la sua costruzione»), 20:30, 28:56 («Ecco qua»), 30:35, 35:13, 50:44. **Da verificare** che l'immagine nominata sia sullo schermo (±3 s): non ancora fatto.
- Slide del prof: `Letteratura_Lez5_videodispensa.pptx` ha 134 slide: 5 di contenuto (Verga, vita, spostamenti, svolta, ciclo dei Vinti, capolavori), 120 con una «fettina» del libro (T3 Rosso Malpelo, T4, T5, T7, T8, T9 La roba, T10 Libertà, T12), una finale. (M)

## NON ancora fatto
- Ascolto vero (voce Kore: frasi che nominano immagini, parole tagliate, rumore dell'audio del prof, sincronia labbra): **non fatto** (ho solo la trascrizione e le misure sopra).
- OCR di tutte le slide, `.vtt`, sincronia riquadro-labbra, audio −16 LUFS e rumore, confronto PDF slide.
- Tabella pagine HD (brano · pagina · file · minuto), mappe del prof, compiti, verifica 10 domande.

## Cosa NON è stato prodotto
Nessun video nuovo, nessun PDF slide/mappe, nessun `compiti.json`/verifica, nessun `.vtt` corretto: **la lezione non è ancora consegnabile**. Il generatore del kit (`build_slides.py` ecc.) è nel repo ma richiede di ricostruire l'intero montaggio (piano di 100+ pezzi, evidenziazioni dalla trascrizione, fettine HD, ritaglio 4:3 dall'originale): non l'ho ancora fatto.

## Piano e tempo (S)
Rifare riquadro+fascia+fondo da originale: ~2 h di codifica. Fettine HD e slide: ~2 h. Quindi **5 ore** servono tutte; senza Whisper l'ascolto non è fattibile.
