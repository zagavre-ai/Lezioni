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

## NON ancora fatto
- **Ascolto/trascrizione (A): non fatto.** Whisper non utilizzabile qui: il download del modello da Hugging Face è bloccato dalla rete (403). Serve un modello locale o un host abilitato.
- OCR di tutte le slide, `.vtt`, sincronia riquadro-labbra, audio −16 LUFS e rumore, confronto PDF slide.
- Tabella pagine HD (brano · pagina · file · minuto), mappe del prof, compiti, verifica 10 domande.

## Piano e tempo (S)
Rifare riquadro+fascia+fondo da originale: ~2 h di codifica. Fettine HD e slide: ~2 h. Quindi **5 ore** servono tutte; senza Whisper l'ascolto non è fattibile.
