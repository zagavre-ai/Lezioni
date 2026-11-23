# RAPPORTO DI REVISIONE · Storia dell'arte V · «Le Avanguardie» (Parte 1)

**STATO: CONSEGNA PARZIALE. NON REVISIONATA.** Le voci Kore nuove (pillole P1–P7, mappe, compiti) non sono ancora arrivate sul ramo `voci-storia-arte-V-lez07` (controllato alle 12:00 italiane). Quelle parti sono **mute nel video** e vanno sostituite: il montaggio è pronto per farlo in circa 40 minuti. Il controllo rapido dà quindi **ESITO: DA CORREGGERE** (solo per le pause mute dei segnaposto, vedi sotto). L'agente separato del §11 **non è stato eseguito**.

## Misure sul video (Storia_arte_Lez7_Parte1_1080p.mp4)
- 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192k 48 kHz; durata 53,4 min (3201,8 s); fotogrammi = durata × 30; **288 MB**. sha256 nel file `.sha256` (video a 4 pezzi da 90 MiB: `cat *.parte_* > video.mp4`).
- Volume −16,4 LUFS, picco reale −1,2 dBTP (controllo_rapido: −3,4 dBFS sul campione).
- Timbro del docente: acuti >4 kHz meno volume >100 Hz = −16,17 dB sull'originale, −16,11 dB dopo la pulizia (filtro dei bassi a 90 Hz + riduzione leggera del rumore): entro −9/−20 dB. Un limitatore agisce solo sui rari picchi.
- Scatto del jingle dei quiz: +0,012 s su 7 schede su 7 (misura a 8 kHz, tolleranza 0,05 s). Non 0,0 esatto.
- Nessun nome del docente nel piè di pagina, nessuna scheda con fasce, nessuna schermata uguale oltre 3 min, titolo in copertina trovato (controllo_rapido).
- Pause mute oltre 2,5 s: **11, tutte dovute ai segnaposto senza voce**: pillole P1–P7, mappe M2 (8:21), M5 (35:37) e finale (51:03), compiti (52:07). Nel pezzo del docente la pausa più lunga era 2,93 s: accorciata a circa 1 s.
- Durata 53,4 min: una sola Parte (tra 50 e 65 minuti), niente spiegone.

## Tabella dei tagli del docente (D1–D7: inizio, ultime 8 parole, frase finita)
Trascrizione automatica del pezzo montato; i nomi sono quelli sbagliati dall'ASR, non dal video.

| Pezzo | Inizio | Prime parole | Fine | Ultime parole | Frase finita |
|---|---|---|---|---|---|
| D1 | 0:49 | «Buongiorno e benvenuti alla lezione sulle…» | 7:37 | «…volta, ma in questo caso in queste modalità.» | sì |
| D2 | 8:59 | «Matis il primo, almeno dal punto…» | 15:13 | «…Maurice Vlaming, Andre Déven e Kies van Degen.» | sì |
| D3 | 17:35 | «Ora parliamo in particolare, e in…» | 21:36 | «…Non c'è prospettiva e se c'è è sfalsata.» | sì |
| D4 | 22:52 | «Ecco, sulla falsar riga di Matisse,…» | 28:14 | «…fortunata, anche se dipende dal punto di vista.» | sì |
| D5 | 29:26 | «Quindi ci sono diverse fasi. Allora,…» | 34:58 | «…debito quando cronologicamente entreremo in quegli argomenti, d'accordo?» | sì |
| D6 | 37:19 | «Ecco, allora, comunque andiamo avanti. Il…» | 40:24 | «…universali e primordiali, come Abbiamo addormentato il bacio.» | sì |
| D7 | 41:36 | «Ecco, usciamo dall'avanguardia cupista, ma usciamo…» | 48:26 | «…panorama, appunto della storia dell'arte del primo Novecento.» | sì |

Correzione fatta durante il controllo: il pezzo 6 finiva a metà frase («…primordiali, come»); ora termina su «…come la Musa addormentata, Il bacio.». I tagli cadono in pause con rumore di fondo a −58/−65 dB. Taglio interno tolto: 10 s in cui il prof sposta le finestre («Pazienza, mi sposto…») e una pausa da 2,93 s accorciata a 1 s. Nessun altro taglio: le parole del prof non sono toccate.

## Sincronia e webcam
- Il video del prof è 1092×614 (registrazione dello schermo); la sua webcam è 246×139 px. Ritaglio 4:3 centrato (180×135) ingrandito a 412×309 con nitidezza leggera e colore leggero, angoli arrotondati, a x=1428, y=148, con ombra grigia e fascia gialla. La finestra della webcam cambia posto nel video (a 24:03, 27:00 e 33:03 circa): seguita fotogramma per fotogramma.
- Immagine e voce provengono dagli stessi fotogrammi dell'originale (taglio a fotogrammi interi, audio a 1600 campioni per fotogramma). Misura a campione su 11 punti: scarto 0–1 fotogramma (≤0,033 s). Nel pezzo 2 manca un fotogramma finale (audio accorciato di 33 ms). **Non misurato** con un rilevatore di labbra.

## Opere e fonti
- Dalle slide del prof (`pdfimages`, risoluzione 340–900 px), ingrandite 2× con EDSR (OpenCV) e ritagliate senza didascalia: Luxe, calma e voluttà; Acrobata e giovane equilibrista; La vita; Les Demoiselles d'Avignon; Ritratto di Vollard; Violino e tavolozza; Fruttiera e bicchiere; Chitarra; Chagall (Io e il mio villaggio, Parigi attraverso la finestra); Modigliani (Nudo disteso, Ritratto di Jeanne Hébuterne). **Sono ancora meno nitide di una scansione originale** (autori ancora protetti, non su Commons).
- Procurate dalla master da Wikimedia Commons (1920 px): La Danse (Public domain: File:La Danse II, par Henri Matisse.jpg); Le Bonheur de vivre (PD: File:Le Bonheur de vivre Barnes (01c) - Flickr - rverc.jpg); L'Atelier rouge (PD); Odalisque à la culotte rouge (PD); Henri Rousseau, La guerre (PD); Robert Delaunay, Les Fenêtres simultanées sur la ville (PD); Facade of Grand Palais, Paris (CC BY-SA 3.0); Petit Palais Paris 8e (CC BY-SA 3.0). Elenco completo in FONTI.md della master.
- **Opere nominate dal prof e non mostrate** (non disponibili): Picasso, Ritratto di Gertrude Stein e Testa di donna (Fernande); Braque, Case all'Estaque; Archipenko, Donna che cammina; Brâncuși, La Musa addormentata e Il bacio.
- Nota: nell'estrazione dalle slide due file di Braque «Violino e tavolozza» e «Fruttiera e bicchiere» erano invertiti nell'estrazione; corretti.

## Mappe del prof (3, dal PDF MAPPE LEZIONE 7)
- Ridisegnate in vettoriale, colori BES con legenda, testo ≥ 34 px, costruite ramo per ramo (l'ordine segue il testo della voce) e riquadro giallo mentre si legge. Tutte le parole sono quelle del prof; disposizione ricostruita da me. **Titoli scritti da me** (il prof non li ha): «Chi sono i Fauves?», «Che cos'è il Cubismo?», «Che cosa sono le Avanguardie?».
- Nella mappa finale restano Futurismo, Astrattismo, Dadaismo, Surrealismo, Metafisica: sono nella mappa del prof (argomenti di altre lezioni); ho lasciato com'è. Omesse: le miniature delle opere sotto la mappa e il marchio del sito della mappa.
- Mappe nel video: **mute (segnaposto)**: la voce arriverà dalla master. Il Futurismo ecc. non hanno mappe proprie.
- PDF delle mappe: `Storia_arte_Lez7_mappe.pdf` (A4 orizzontale, copertina con «MAPPE»).

## Refusi e anomalie del materiale del prof
- Corretti nelle slide (la master ricontrolla): «antiacademica» → «antiaccademica»; «fauvet» → «fauve»; apostrofi tipografici ’ → '.
- Anomalie lasciate come le dice il prof: nel parlato Modigliani «Ritratto di Jeanne» è del 1918, la didascalia della slide dice 1919 (nel video uso 1919 della slide); nel parlato Matisse «scrive nel 1908» e «Shuskin» (nella slide Shchukin).
- Ho scritto sullo schermo i nomi come sono nella slide (Shchukin, Brâncuși, Salon d'Automne, Les Demoiselles d'Avignon).

## Voci Kore
- Riusate (15/11): INTRO, S1–S7 (approfondimenti), GL, RF. Trascritte e confrontate: testo corrispondente, bordi sotto 0,03 tranne S7 (0,032 in coda). **RF ha l'attacco troncato** (manca «Prima di salutarci»): ho chiesto RF_R2 e S7_R2.
- **Nuove da generare**: P1–P7, MAP_FAUVES, MAP_CUBISMO, MAP_FINALE, COMPITI (testi già su `testi_voci.json`).
- Ogni voce ha dissolvenza di 20–30 ms. **La pronuncia dei nomi stranieri non è stata ascoltata**: l'ASR italiano li trascrive in modo fonetico (es. Fauves → «fov»): da ascoltare.

## Struttura (tutto dal materiale del prof)
Sigla Storia dell'arte 15 s → copertina «Le Avanguardie» con argomenti e voce di benvenuto (senza riquadro del prof) → per ognuno dei 7 argomenti: titolo con jingle, docente con slide a card intere (40 px, max 3, bordo giallo all'inizio della frase), approfondimento animato (31–38 s: **sotto i 40 s richiesti**, perché la voce del 15/11 dura così; da allungare solo con testi nuovi della master), mappa (argomenti 2 e 5), pillola di ripasso (5 righe), quiz da 5 domande (scatto a +0,5 s) → glossario (8 voci) → riepilogo → mappa finale → verifica di sbarramento (10 domande, soglia 80%) → sigla finale con avviso diritti → intro «Compiti» → compiti. Ponte con dissolvenza di 0,9 s e `trans.wav` a ogni cambio di pezzo.
Un argomento (il 1) non ha opere nelle slide del prof: l'approfondimento è solo testo.

## File e metadati
- Quiz: `quiz_argomenti.json` (35 domande, dal 15/11, da far approvare alla master). Verifica: `verifica_finale.json` e `Test_finale_…xlsx` (10 domande del prof). `compiti.json`: 4 compiti dal PDF «LEZIONE 7».
- Dispensa A4 (39 pagine, copertina con materia e titolo, testo invisibile, nessun nome del docente) e PDF delle mappe.
- Sottotitoli `.vtt` (spenti all'avvio, 924 blocchi): docente = trascrizione automatica con correzione dei nomi principali (**non riletta parola per parola**); voci Kore = testo esatto. Rigenerati sul video attuale: da rifare dopo la sostituzione delle voci.
- `timeline_Parte1.json` e `scheda_pubblicazione_Parte1.json` sul video attuale (titolo «Storia dell'arte V · Lezione 7 · Le Avanguardie», con `t_verifica`, `t_compiti`, `t_sigla_finale`).

## Cosa NON è stato verificato / cosa manca
1. Voci nuove (P1–P7, 3 mappe, COMPITI) e RF_R2, S7_R2: assenti; ricostruzione, sottotitoli, timeline e controllo rapido da rifare dopo.
2. Pronuncia dei nomi stranieri non ascoltata.
3. Agente separato del §11 non eseguito.
4. Labbra e voce solo per costruzione e a campione; sottotitoli del docente non riletti.
5. 10 punti di controllo card/trascrizione fatti sui tempi della mia scheda, non da un secondo agente.
6. Immagini delle slide ingrandite ma non nitide come un originale.
