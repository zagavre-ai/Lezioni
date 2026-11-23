# RAPPORTO DI REVISIONE · Storia dell'arte V · «Il Romanticismo» (Prof. Giorgio Mazzotti)
Ramo `revisione-storia-arte-V-lez02` · consegna **PROVVISORIA** del 23/11 (voci Kore solo in parte). Etichette: **M** = misurato, **S** = stima/lettura a vista, **NV** = non verificato.

## 0. Stato (leggere prima)
- **Voci Kore: 13 su 72 arrivate** (AP2, AP4, R1a, R1c, R1e, R2a, R2c, R2e, R3b, R3d, TIT1, TIT3, TIT5). Tutte le altre sono **voci provvisorie** (sintesi del computer, stessi testi): **il video NON è finale**. Appena arrivano le altre, rimonto solo le schede interessate e riconsegno.
- **Compiti:** il PDF «LEZIONE 2.pdf» a 1 pagina contiene 4 domande su **Scapigliatura e Boito (Letteratura)**, non su Storia dell'arte. Non l'ho usato: `compiti.json` ha l'elenco **vuoto**, nel video **non** ci sono l'intro «Compiti» né la scheda compiti. Serve il file giusto o un ok della master.
- **Opere da procurare (Commons):** Füssli, *L'incubo* (1781, Detroit Institute of Arts; il prof lo nomina al min 1671 ma nelle slide non c'è l'immagine) e Turner, *Il naufragio del negriero* (1840, MFA Boston; nella mappa del prof c'è solo una miniatura ingrandita ×2).
- **Video:** in questa consegna ci sono foglio dei fotogrammi, json del controllo rapido, timeline, schede, quiz, verifica, `.vtt`, dispense e questo rapporto. **I video a pezzi da 90 MB non sono ancora sul ramo** (il repository è vicino al limite di spazio e il video non è finale): li carico alla consegna finale con le voci complete.

## 1. Divisione in Parti
Totale con tutto il materiale: circa 75 min (il solo prof dura 59,9 min) → oltre 65 min, divisione a fine argomento (CLAUDE.md §3.6):
- **Parte 1** = sigla, copertina, introduzione del prof, argomenti 1–4: **60,81 min** (M; 0,8 min oltre i 60 per la lunghezza delle voci reali).
- **Parte 2** = sigla, **spiegone** (ripasso animato degli argomenti 1–4 con le loro opere), argomento 5, glossario, ripasso finale, mappa, verifica, fine, sigla finale: **14,34 min**. Più corta di 50 min perché il materiale restante è questo: non l'ho allungata. **Da confermare dalla master** (alternativa: una sola Parte da circa 75 min).

## 2. Misure sul video (controllo_rapido.py: ESITO OK su entrambe, M)
| | Parte 1 | Parte 2 |
|---|---|---|
| Formato | 1920×1080, 30 fps | 1920×1080, 30 fps |
| Durata | 60,81 min | 14,34 min |
| Peso | 322 MB | 88 MB |
| Volume | −16,7 LUFS | −16,7 LUFS |
| Picco | −2,4 dBTP | −2,7 dBTP |
| Pause mute > 2,5 s | nessuna | nessuna |
| Schede con fasce / nome nel piè di pagina | nessuna / nessuno | nessuna / nessuno |
| Schermate ferme oltre 3 min | nessuna | nessuna |
Fotogrammi = durata × 30 (Parte 2: 25 817 fotogrammi, M); per la Parte 1 lo controlla `stato.py`.
**Codifica:** x264 veryfast, **CRF 25 sui pezzi del prof e CRF 23 sulle schede** (non CRF 19): a CRF 19 il file era di quasi 1 GB; la webcam del prof è piccola e rumorosa e costava circa 1 Mbit/s. Ho tenuto il tetto dei 400 MB. Il rumore della webcam è ridotto (hqdn3d), niente sfocature dello sfondo. Una sola codifica del video, audio AAC 192k 48 kHz.
- **Scatto del jingle Quiz:** Q1–Q4 e Q5 a **+0,002 s** dal punto atteso (+0,5 s dall'inizio della scheda), scarto accettato 0,05 s (M, correlazione con `quiz.wav`).
- **Timbre della voce del prof (alti >4 kHz / sopra 100 Hz, M):** finale = originale nelle stesse finestre di 60 s: D1 −19,0 / −18,9; D2 −21,9 / −21,9; D4 −19,5 / −19,8; D5 −20,3 / −20,5 dB. Il valore è più basso di −20 dB in D2 e D5 **già nell'originale** (non lo cambia la pulizia; limite di rovina −25 dB).
- **Pulizia audio:** filtro dei bassi a 70 Hz e riduzione leggera del rumore (afftdn), poi un unico guadagno e un limitatore. Il prof parla a −24,2 LUFS nell'originale.
- **Pause del prof:** una sola pausa oltre 2,5 s (min 41:28 dell'originale, 2,76 s) accorciata a circa 1 s, in pieno silenzio. Totale tolto: 1,76 s.
- **Sincronia labbra-voce (S, per costruzione):** audio e immagine del prof sono presi dallo stesso istante dell'originale, allineati alla griglia dei fotogrammi (scarto massimo 1/60 s). **Non ho misurato** lo scarto con la correlazione.
- **Fermi immagine del prof (freezedetect): NV.** La webcam si muove sempre; l'ho visto sul foglio dei fotogrammi ma non ho lanciato lo strumento.

## 3. Pezzi del prof: inizio e fine (M, dalla trascrizione dell'originale)
| Pezzo | Parte | Inizio nel video | Prime parole | Fine nel video | Ultime parole | Frase finita? |
|---|---|---|---|---|---|---|
| D0 | Parte 1 | 0:39.2 | «Buongiorno e benvenuti alla lezione sul…» | 3:33.8 | «…anche in pittura, in scultura e in architettura.» | sì |
| D1 | Parte 1 | 3:41.3 | «I riferimenti al contesto storico.…» | 18:12.0 | «…all'epoca neoclassica, che esaltava tutt'altro.» | sì |
| D2 | Parte 1 | 20:00.6 | «Andiamo in Spagna, andiamo…» | 30:33.3 | «…per dare corpo ad una dimensione onirica visionaria.» | sì |
| D3 | Parte 1 | 32:19.7 | «Ma soprattutto Kaspar David.…» | 43:04.2 | «…al romanticismo francese. Questo è il romanticismo inglese.» | sì |
| D4 | Parte 1 | 44:37.3 | «Jericot in particolare, Théodore Ghericot, introduce…» | 59:13.0 | «…1859.» | sì |
| D5 | Parte 2 | 2:13.2 | «I pre-Raffalliti e le Arts Crafts,…» | 8:49.4 | «…successive.» | sì |
I pezzi sono continui dall'originale; solo il pezzo D0 (introduzione sopra la copertina) dura **174,6 s (< 3 min)**. Tagli nelle pause, 0,15 s prima della frase che segue. Le trascrizioni automatiche contengono errori di parole (es. «Jericot», «Kaspar»): sullo schermo e nei sottotitoli i nomi sono corretti.
Tra un pezzo e l'altro ci sono stati tolti solo silenzi (175,5→176,4; 1047,1→1048,35; 1681,0→1682,64 dell'originale).

## 4. Slide, card e tempi di accensione
- Testo delle card a **40 px**, interlinea 1,45; al massimo 2 card per pagina (a 40 px tre frasi non entrano: la pagina scorre). Ogni card è una frase intera del prof; la frase in corso ha bordo e pallino gialli, le altre attenuate. Pagine numerate 1–54, in ordine di apparizione (dispensa identica).
- **Tempi di accensione:** per tutte le 13 pagine di testo li ho **scelti a mano leggendo la trascrizione** (secondo dell'originale della prima parola della frase). Non ho ricontrollato i 10 punti sul video finale: **NV**. Caso particolare p. 9 (Goya): l'ordine del parlato è diverso da quello della slide (prima i massacri, poi «Il lato oscuro», poi le Maja): le card si accendono nell'ordine in cui il prof ne parla.
- Nessuna pagina oltre 3 min: le pagine d'arte cambiano vista ogni 40 s (immagine intera → dettaglio), la copertina cambia a 90 s. Colonna destra: riquadro 4:3 a x=1428 y=148, fascia gialla, parole chiave (max 5).

## 5. Refusi e interventi sul testo del prof (§2.7)
- «Ilpaesaggismo inglese» → «Il paesaggismo inglese» (titolo slide 18).
- Mappa: «Gericault» → «Géricault», «Rugen» → «Rügen», «La zattera della medusa» → «…Medusa», «all'illuminismo» → «all'Illuminismo», «Il Bacio» → «Il bacio», «La libertà…» → «La Libertà che guida il popolo» (nelle slide).
- **Sigle/abbreviazioni rispiegate** sulle slide: XVIII e XIX (diciottesimo, diciannovesimo), Carlo IV (quarto), J.M. (Joseph Mallord) William Turner, A. (Augustus) Welby Pugin. **«Joseph Mallord» e «Augustus» non sono nel materiale del prof**: sono aggiunte mie per spiegare le sigle; la master le conferma o le toglie. «en plein air» spiegato «cioè all'aria aperta».
- **Incongruenze del prof riportate come le scrive:** la mappa dice «Le scogliere di Rügen, 1819» e la slide 5 «Le falesie di gesso di Rügen, 1819» (stessa opera); la mappa dice «inizio del 1800» (voce: «milleottocento»); «Il naufragio del negriero» (Turner, mappa) non compare nelle slide; la slide 21 dice «Tramonto sul lago, 1840».
- **Mappa del prof:** il titolo non era una domanda: l'ho scritto io, **«Che cos'è il Romanticismo?»** (dalla casella «cos'è» del prof). Il marchio di terzi «MAPPE per la SCUOLA» è tolto (mappa ridisegnata). La miniatura *Il naufragio del negriero* è ritagliata dalla scansione della mappa (153×96 px) e ingrandita ×2: **bassa qualità, da sostituire con la versione Commons**.

## 6. Mappa (M/S)
Mappa unica del prof, ridisegnata in HTML vettoriale, colori BES con legenda in alto a destra (pesca, celeste, paglierino, menta, lilla), testo 34–50 px, costruita **ramo per ramo** con le voci M1–M11 (riquadro acceso in giallo mentre la voce parla), alla fine intera ferma 4 s (con il jingle `repaso` morbido: nessuna pausa muta > 2,5 s). Mappe del prof = 1; per gli argomenti non c'è una mappa propria: si chiudono con la pillola. Stesse parole e stesse frecce della mappa del prof (verificate a vista sul fotogramma finale: S).

## 7. Immagini (M)
Tutte le opere vengono dal **PDF delle slide del prof** (`pdfimages -all`): risoluzioni originali 163–917 px sul lato lungo (portrait Géricault 194×240!). Ritagliate dalla pagina (senza didascalie incorporate) e **ingrandite con EDSR ×2 (lato lungo ≥ 450 px) o ×4**; il risultato è più pulito ma resta una ricostruzione: **le opere non sono ad alta risoluzione vera**. Wikimedia è bloccata dalla rete; per le due opere mancanti vedi §0. Nessuna foto di persone reali (solo dipinti). Webcam del prof: sorgente circa 246×137 px (ritaglio 4:3 di 180×135 px ingrandito ×2,29).

## 8. Voci Kore (NV in gran parte)
- 13 voci reali importate (convertite a 48 kHz stereo). **Non ho ancora trascritto e confrontato** parola per parola le voci reali, né misurato i bordi (< 0,03 negli ultimi 50 ms): **NV**. Dissolvenza di 30 ms in entrata e uscita applicata a ogni voce nel montaggio.
- Le altre 59 voci sono provvisorie (nessun valore come esito): nomi stranieri non verificati a orecchio.
- Il nome del docente non compare nelle voci né nelle schede animate (solo nella fascia gialla); piè di pagina: «STORIA DELL'ARTE V · Pagina N».

## 9. Struttura (M, sul foglio)
Sigla (kit `Sigla_Storia_arte_15s`) → copertina animata con voce (senza riquadro del prof) → introduzione del prof (2:55) → per ogni argomento: titolo con jingle, prof con slide, approfondimento 48–61 s (**alcuni oltre 60 s con le voci reali: AP2 = 61 s**), pillola (4–6 righe accese con la voce, jingle `repaso`), quiz 5 domande (scheda 4 s con jingle). Poi glossario (8 voci), ripasso finale, mappa, verifica di sbarramento (10 domande dell'Excel del prof, soglia 80%), «Fine della lezione», sigla finale con avviso diritti. Transizioni: dissolvenza di 0,6 s con `trans.wav` a ogni cambio di pezzo.
Le domande dei quiz sono scritte da me dal materiale del prof (`quiz_argomenti.json`): **da approvare dalla master**.

## 10. Dispense (M)
`Storia_arte_V_Lez2_dispensa.pdf` (A4 orizzontale, copertina solo materia + titolo, 53 pagine = le slide del video senza riquadro del prof, con strato di testo invisibile, piè di pagina materia + «Pagina N») e `Storia_arte_V_Lez2_mappe.pdf` (copertina con «MAPPE» + mappa). Le schede blu (titoli, pillole, quiz, glossario, ripasso) non sono nella dispensa: la numerazione «Pagina N» coincide con quella del video.

## 11. Sottotitoli
`.vtt` per Parte, dal parlato del video **finale** (prof e voci), con correzione automatica di alcuni nomi (Géricault, Caspar, Füssli, Preraffaelliti…). **Controllo a campione non fatto: NV.** Restano errori di riconoscimento sul parlato colloquiale del prof.

## 12. Controllo indipendente (§11)
**NON fatto.** Nessun agente separato ha spuntato la lista. Lo faccio alla consegna finale, con tutte le voci.

## 13. Difetti trovati e corretti durante il lavoro
Titoli lunghi su 2 righe che finivano sopra la prima card (corretto: colonna a flusso); titolo di slide d'arte troncato («Ritratto di Alessandro Manzoni e La…» → accorciato); transizioni riusate tra Parte 1 e Parte 2 (corretto); picco audio oltre −1 dBTP (limitatore); peso 997 MB (CRF e riduzione del rumore); movimento continuo delle opere (pesante) sostituito da viste a scatti ogni 40 s; numerazione pagine non coerente tra processi (fissata in ordine di apparizione).
