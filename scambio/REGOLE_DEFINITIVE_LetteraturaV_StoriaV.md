# REGOLE DEFINITIVE videolezioni · Letteratura V e Storia V (17/11/2026, congelate)
Valgono **sopra** tutte le altre regole e aggiornamenti. Nessuna regola nuova a lavori in corso.

## 1. Modello unico
- Modello: **lezione 11 di Letteratura V** (ramo `revisione-letteratura-V-lez11`, online). Ogni lezione è **identica** alla 11: grafica, schede, suoni, ordine dei pezzi. Per Storia cambia solo la materia nei testi («STORIA V · Prof. Giorgio Mazzotti»).
- Prima di consegnare confronta i tuoi fotogrammi con quelli della 11: copertina, slide col prof, approfondimento, pillola di ripasso, schema di ripasso, scheda Quiz, glossario, riepilogo finale.
- Font: solo **Bricolage Grotesque 800** (titoli) e **Figtree** (testo; Figtree Bold per etichette e piè). **Niente DM Mono, niente fondi scuri/blu notte, niente stelle, niente onde audio decorative, niente pannello laterale «parole chiave» sotto il prof.**

## 2. Struttura (come la 11)
1. Sigla della materia (15 s), dissolvenza morbida.
2. Copertina bianca: titolo, card «ARGOMENTI», voce di benvenuto (riquadro del prof solo se parla davvero).
3. Per **ogni argomento**: titolo (`titolo.wav`) → prof con slide sincronizzate e card in corso gialla → approfondimenti animati con voce → **mappa del prof** (release) con la nostra grafica → **pillola di ripasso** (ripasso animato con voce narrante, **jingle `repaso.wav`** all'inizio: OBBLIGATORIA) → **schema di ripasso** → **scheda Quiz** (`quiz.wav` a +0,5 s).
4. Glossario animato · 5. Riepilogo finale · 6. Sigla finale 5 s con avviso diritti e `finale.wav`.
Fuori dal video: verifica finale (10 domande dall'Excel del prof) e compiti del prof. Ogni Parte 50–60 minuti.

## 3. Schede uguali in tutte le lezioni
- **Scheda Quiz** = `scambio/mazzotti/MODELLO_scheda_quiz_lez11.jpg`: fondo bianco, «QUIZ · 01» Figtree Bold maiuscolo spaziato blu (senza pillola), «Quiz: <argomento>» Bricolage 800 + barretta blu, «Rispondi alle domande sull'argomento appena visto.», «5 domande · per continuare almeno l'80%» evidenziato giallo, piè come le slide. Niente play, niente «Pausa del video». Durata 4,9 s.
- Verifica, Compiti, Fine: stessa grafica bianca della 11.
- Slide: fondo bianco, «01 · NOME ARGOMENTO», piè «MATERIA · Prof. …» e «Pagina N». Mai il numero della lezione nel video.

## 4. Suoni (kit `home/claude/v5/snd/` in `Telesio_kit_produzione_v1.zip`)
`titolo.wav` su ogni titolo · `repaso.wav` su ogni pillola · `quiz.wav` su ogni Quiz · `trans.wav` + dissolvenza breve a **ogni** passaggio tra pezzi (mai tagli secchi) · `finale.wav` su «Fine». Parlato −16 LUFS ±2, picco < −1 dBTP, nessun silenzio > 3 s.

## 5. Il prof
Riquadro 4:3 in alto a destra, ombra grigia morbida, fascia gialla col nome su due righe sempre visibile. **Mai immagine ferma** (nessun fermo ≥ 1 s). Mai tagliato a metà frase. Sincronia labbra ≤ 0,04 s. Audio pulito con la catena del kit.

## 6. Tempi
- Una lezione per chat, **consegna entro 3 ore** dall'avvio. Stato ogni 20 minuti (`kit/tools/stato.py`). Riga a Sara alla partenza e ogni 30 minuti.
- **Riusa tutto quello che c'è**: trascrizione, tagli e sincronia del prof, voci Kore già fatte (ramo `voci-…`). Rifai la grafica nel modello. Voci nuove: **tutte insieme all'inizio** in un solo `testi_voci.json`.
- Se manca un materiale: una riga a Sara e intanto lavori sul resto.

## 7. Controllo prima della consegna (scrivilo nel rapporto)
sha256 · durata · fotogrammi · LUFS e picco · jingle Quiz a ogni Quiz · minuto di ogni `titolo`, `repaso`, `trans` · nessun fermo del prof (`freezedetect`) · un fotogramma per tipo di scheda accanto a quello della 11 · sottotitoli riletti · PDF slide identico al video. **Niente si consegna con un difetto noto.**

## 8. Consegna
Ramo `revisione-<materia>-lezNN`: video a parti `.parte_NN` + `.sha256` (nome `Storia_LezN_ParteK_1080p.mp4`), `.vtt`, `scheda_pubblicazione_ParteK.json`, `compiti.json`, `verifica_finale.json`, PDF slide e mappe, `RAPPORTO_REVISIONE.md`. Commit senza firma (utente «Sara Zagarese», responsabiletecnicaegraficacst@gmail.com, nessun Co-Authored-By). La master verifica, confronta con la 11 e carica.
