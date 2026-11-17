# REGOLE DEFINITIVE videolezioni · Letteratura V e Storia V (17/11/2026, congelate)
Bozza in revisione da Sara. Valgono **sopra** tutte le altre regole e aggiornamenti. Nessuna regola nuova a lavori in corso.

## 1. Modello unico: SPAGNOLO LEZIONE 1
- Il modello è **solo la Lezione 1 di Spagnolo** (consegnata con il Brief) **più le aggiunte promosse nel tempo** (mappe del prof, fettine HD del libro, pronuncia dei nomi, prof mai fermo e mai tagliato a metà frase). Ogni lezione è **identica** a Spagnolo: grafica, schede, suoni, ordine dei pezzi. **La lezione 11 di Letteratura NON è il modello.**
- Riferimento: `scambio/mazzotti/MODELLO_Spagnolo_schede.jpg` + `kit/modello_spagnolo/`. Prima di consegnare metti ogni tipo di scheda accanto a quella di Spagnolo.
- **Schede blu scure animate** (come Spagnolo): titolo dell'argomento, pillola di ripasso, scheda Quiz, riepilogo finale. **Fondo bianco**: copertina, slide di contenuto col prof, glossario, tabelle.
- Font: solo **Bricolage Grotesque 800** e **Figtree** (Figtree Bold per etichette e piè). **Niente DM Mono.** Il pannello **«PAROLE CHIAVE»** sotto il riquadro del prof è un'aggiunta approvata da Sara: **si tiene** (dove la lezione ce l'ha).

## 2. Struttura (come Spagnolo)
1. Sigla della materia (15 s), dissolvenza morbida.
2. Copertina bianca: titolo, card «ARGOMENTI», voce di benvenuto (riquadro del prof solo se parla davvero).
3. Per **ogni argomento**: titolo (`titolo.wav`) → prof con slide sincronizzate e card in corso gialla → approfondimenti animati con voce → **mappa del prof** (release) con la nostra grafica → **pillola di ripasso** (ripasso animato con voce narrante, **jingle `repaso.wav`** all'inizio: OBBLIGATORIA) → **schema di ripasso** → **scheda Quiz** (`quiz.wav` a +0,5 s).
4. Glossario animato · 5. Riepilogo finale · 6. Sigla finale 5 s con avviso diritti e `finale.wav`.
Fuori dal video: verifica finale (10 domande dall'Excel del prof) e compiti del prof. Ogni Parte 50–60 minuti.

## 3. Schede (come Spagnolo)
- **Titolo dell'argomento:** blu scura animata, «ARGOMENTO 0N / N», titolo grande bianco; `titolo.wav`.
- **Pillola di ripasso:** blu scura, etichetta «PILLOLA DI …», titolo grande «RIPASSO» (Spagnolo: «REPASO»), sottotitolo azzurro con l'argomento, **onda audio** animata, riga col testo della voce; `repaso.wav`.
- **Scheda Quiz:** blu scura animata con stelline, «PAUSA DEL VIDEO · QUIZ», «Quiz N» grande, argomento in giallo, riquadro «5 domande · per continuare almeno l'80%», «Rispondi · premi Check · poi Continua», **pulsante play** a destra; `quiz.wav` a +0,5 s.
- **Riepilogo finale:** blu scuro, titolo grande, argomenti numerati.
- **Slide, copertina, glossario, tabelle:** fondo bianco, «01 · NOME ARGOMENTO», piè «MATERIA · Prof. …» e «Pagina N». Mai il numero della lezione nel video.

**Le schede blu si fanno SOLO con `scambio/strumenti/schede_spagnolo.py`** (è il programma originale di Spagnolo): così sono identiche in tutte le lezioni. Non disegnarle a mano.

## 4. Suoni (kit `home/claude/v5/snd/` in `Telesio_kit_produzione_v1.zip`)
`titolo.wav` su ogni titolo · `repaso.wav` su ogni pillola · `quiz.wav` su ogni Quiz · `trans.wav` + dissolvenza breve a **ogni** passaggio tra pezzi (mai tagli secchi) · `finale.wav` su «Fine». Parlato −16 LUFS ±2, picco < −1 dBTP, nessun silenzio > 3 s.

## 5. Il prof
Riquadro 4:3 in alto a destra, ombra grigia morbida, fascia gialla col nome su due righe sempre visibile. **Mai immagine ferma** (nessun fermo ≥ 1 s). Mai tagliato a metà frase. Sincronia labbra ≤ 0,04 s. Audio pulito con la catena del kit.

## 6. Tempi
- Una lezione per chat, **consegna entro 3 ore** dall'avvio. Stato ogni 20 minuti (`kit/tools/stato.py`). Riga a Sara alla partenza e ogni 30 minuti.
- **Riusa tutto quello che c'è**: trascrizione, tagli e sincronia del prof, voci Kore già fatte (ramo `voci-…`). Rifai la grafica nel modello. Voci nuove: **tutte insieme all'inizio** in un solo `testi_voci.json`.
- Se manca un materiale: una riga a Sara e intanto lavori sul resto.

## 7. Controllo prima della consegna (scrivilo nel rapporto)
sha256 · durata · fotogrammi · LUFS e picco · jingle Quiz a ogni Quiz · minuto di ogni `titolo`, `repaso`, `trans` · nessun fermo del prof (`freezedetect`) · un fotogramma per tipo di scheda accanto a quello di Spagnolo · sottotitoli riletti · PDF slide identico al video. **Niente si consegna con un difetto noto.**

## 8. Consegna
Ramo `revisione-<materia>-lezNN`: video a parti `.parte_NN` + `.sha256` (nome `Storia_LezN_ParteK_1080p.mp4`), `.vtt`, `scheda_pubblicazione_ParteK.json`, `compiti.json`, `verifica_finale.json`, PDF slide e mappe, `RAPPORTO_REVISIONE.md`. Commit senza firma (utente «Sara Zagarese», responsabiletecnicaegraficacst@gmail.com, nessun Co-Authored-By). La master verifica, confronta con Spagnolo e carica.
