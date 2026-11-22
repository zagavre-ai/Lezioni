# RAPPORTO REVISIONE · Letteratura italiana V · «Carlo Emilio Gadda» · CORREZIONI 22/11 (versione 3)
Partenza: `revisione-letteratura-V-lez20` (v2 del 17/11). **Misurato** = misurato con uno strumento; **stima** = dedotto; **non verificato** = non ho potuto. Titolo esatto della lezione: «Carlo Emilio Gadda».

## 1. Misure sul video finale (misurato)
| Controllo | Risultato |
|---|---|
| Formato | 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192k 48 kHz, una sola codifica |
| Durata | **47:46,6 (2866,6 s) = 85 999 fotogrammi** (durata × 30). Sotto i 50 minuti: lezione con il solo materiale del prof, come previsto dalle regole (non si allunga) |
| Peso | 171,2 MB |
| Volume | −16,6 LUFS integrato; **parlato del prof per pezzo: D0 −16,1 · D1 −16,1 · D2 −16,3 · D3 −16,2 · D4 −16,5 · D5 −16,4 · D6 −16,2 LUFS** (tutti entro −16 ±1; D0, D3 e D6 alzati di 0,9–1,1 dB dopo la verifica indipendente); picco ≤ −1 dBTP (`ebur128=peak=true`, vedi ultima misura nel file `controllo_picco.txt`) |
| Scatto dei quiz | `controllo_jingle.py`: Q1–Q6 a **0,000 s** |
| Fermi immagine del prof | nessuno (freezedetect ≥ 1 s sui pezzi D) |
| Pause/silenzi > 2,5 s | **nessuno** (silencedetect −45 dB, d=2,5 s) |
| Sincronia labbra/voce | scarto audio finale vs audio dell'originale, 3 punti per pezzo: **−10 … −15 ms** su tutti e 7 i pezzi (correlazione dell'inviluppo, punteggio 0,77–0,95); limite 0,04 s |
| Timbro del prof | rapporto fra energia sopra 4 kHz ed energia sopra 100 Hz, 14 finestre da 30 s: originale −11,8…−19,4 dB, finale −11,9…−19,8 dB; **differenza massima 1,0 dB**, tutto fra −9 e −20 dB |
| Sottotitoli | 686 blocchi, max 2 righe da 42 caratteri, nessuna sovrapposizione; rigenerati sul video finale |
| Voce R1 (mappa) | trascritta; bordi: ultimi 50 ms max 0,0009, primi 50 ms 0,0018 (< 0,03) |

## 2. Cosa ho cambiato oggi
- **Testo a 40 px, interlinea 1,5** in tutte le card (slide del prof, approfondimenti, ripassi, glossario, riepilogo, tabella). Titoli, etichette e piè di pagina invariati.
- **Slide del prof:** a 40 px **tre card non entrano mai** (misurato nel browser su ogni terna): le slide mostrano **al massimo 2 card intere**, ognuna è una frase intera del prof (nessun «…», nessuna iniziale minuscola); quando il prof passa oltre, la finestra scorre (la card successiva non resta mai sola: l'ultima finestra riprende la card precedente). Bordo giallo + pallino giallo quando il prof **inizia** la frase (tempi parola per parola dalla trascrizione, ±1 s). Titolo con «(1/2)», «(2/2)» sui pezzi più lunghi di 170 s, così nessuna schermata ha lo stesso titolo per più di 3 minuti.
- **Una sola mappa, quella del prof** (`MAPPE/LEZIONE 20.pdf`), ridisegnata nel **modello BES approvato** (colori pesca/celeste/paglierino/menta/lilla con legenda in alto a destra, testo 34–50 px, frecce blu notte, stesse parole). Si costruisce **ramo per ramo** mentre la voce Kore **R1** la legge (riquadro acceso in giallo finché la voce parla); alla fine la mappa intera resta ferma **4 s**. Posizione: prima del glossario, una volta sola. La mappa del prof di questa lezione **non ha marchio né foto**: non c'era niente da togliere.
- **Copertina:** titolo esatto; introduzione del prof sopra la copertina **57,8 s** (< 3 minuti); nessun riquadro del prof nell'introduzione animata.
- **Audio:** pause > 2,5 s eliminate (jingle `repaso/titolo/finale` nelle schede che restavano in silenzio: fine mappa, verifica finale, compiti, finale); nessun pezzo del prof alterato di timbro (§ 1).
- **Dispense:** `Letteratura_Lez20_slide.pdf` (A4 orizzontale, **61 pagine**) identica alle slide del video, a tutta larghezza, con **testo vero** (vettoriale, selezionabile e leggibile dalla sintesi vocale: l'estrazione del testo dà le parole giuste, ma con le etichette spaziate in lettere separate, p.es. «L A V I TA»); copertina con solo materia e titolo; piè di pagina materia + pagina, **senza il nome del docente**. `Letteratura_Lez20_mappe.pdf`: copertina identica con «MAPPE» + la mappa.
- **File rigenerati sul video finale:** `.vtt`, `timeline_Parte1.json`, `scheda_pubblicazione_Parte1.json` (titolo «Letteratura V · Lezione 20 · Carlo Emilio Gadda», inizio_s/quiz_s/durata_s/t_verifica/t_compiti nuovi), `quiz_argomenti.json` e `verifica_finale.json` (le domande restano quelle del prof, i secondi stanno nella scheda).
- Ripresa dei lavori del 17/11 (già nel video): pezzi del prof contigui e tagliati a fine frase; audio del prof a 48 kHz corretto; jingle e transizioni `trans.wav` su ogni cambio di pezzo; card in corso gialla.

Tabella **secondo vecchio → nuovo** (durata 3290,4 → 2866,6 s):
| Pezzo | v1 del 16/11 (s) | ora (s) |
|---|---|---|
| T1 | 112.4 | 113.1 |
| Q1 | 688.6 | 624.4 |
| T2 | 693.9 | 629.7 |
| Q2 | 1350.3 | 1218.8 |
| T3 | 1355.6 | 1224.1 |
| Q3 | 1708.1 | 1513.6 |
| T4 | 1713.4 | 1518.9 |
| Q4 | 2143.2 | 1873.7 |
| T5 | 2148.5 | 1879.0 |
| Q5 | 2450.4 | 2124.8 |
| T6 | 2455.7 | 2130.1 |
| Q6 | 3048.4 | 2652.7 |
| GL1 | 3132.6 | 2708.9 |
| RF1 | 3190.5 | 2766.7 |
| VER | 3265.3 | 2841.5 |
| COMP | 3284.1 | 2860.3 |

## 3. Pezzi del prof: inizio e fine (misurato dalla trascrizione dell'originale)
| Pezzo | inizio (min) | fine (min) | prime parole | ultime parole | frase finita |
|---|---|---|---|---|---|
| D0 | 0:54 | 1:52 | «Buongiorno a tutti e benvenuti alla lezione su Carlo Emilio Gadda» | «…una fotografia di Carlo Emilio Gadda.» | sì |
| D1 | 1:58 | 7:00 | «Vediamo nella vita.» | «…segnata da profondi avvenimenti luttuosi.» | sì |
| D2 | 10:35 | 16:51 | «Ecco, vediamo però la poetica gaddiana…» | «…primo dopoguerra. Allora, il Giornale di guerra e di prigionia.» | sì (enunciato che annuncia il tema) |
| D3 | 20:29 | 23:17 | «Andiamo pure su quest'altra slide, il Giornale appunto di guerra e di prigionia…» | «…è sicuramente La cognizione del dolore.» | sì |
| D4 | 25:24 | 29:07 | «Pubblicato inizialmente a puntate, i famosi romanzi a puntate.» | «…della mediocrità del mondo.» | sì |
| D5 | 31:24 | 33:41 | «Altre opere: L'Adalgisa, Eros e Priapo…» | «…ma anche di incredibilmente polemico.» | sì |
| D6 | 35:35 | 40:07 | «Bene, il giallo filosofico, Quer pasticciaccio brutto de via Merulana.» | «…il contenuto e le modalità che abbiamo delineato.» | sì (fine della registrazione) |
Ogni attacco e ogni fine cadono in una pausa (minimo di energia, ≥ 0,4 s): nessuna parola mozzata.

## 4. Controllo severo della master (`controllo_severo.py`)
Il controllo severo (OCR di una schermata ogni 10 s) è molto lento in questa macchina: al momento della consegna era al 75 % e **non aveva ancora dato l’esito**; lo scrivo qui appena finisce (file `controllo_severo.txt`). I controlli equivalenti li ho fatti io, misurandoli (§ 1) e con l’agente separato (§ 5).

## 5. Controllo di un agente separato (lista §11)
Un agente che non ha montato la lezione ha spuntato la lista (51 chiamate, ~70 fotogrammi, PDF, vtt, json). **Esiti OK:** tagli su frase intera (6 su 7 verificati sulla trascrizione, D4 «non verificabile senza ascolto» perché la trascrizione dell'ultima frase è frammentata); nessun fermo immagine del prof; card sempre 2 per slide e intere, nessun «…», bordo giallo; nessuna schermata identica > 3 minuti (massimo 135 s) e nessuna card sola; riquadro 4:3 (412×309) solo nei pezzi D e mai nell'introduzione animata; nome del docente mai a schermo se non in fascia e piè di pagina e mai nei sottotitoli; mappa unica del prof con i testi dei riquadri identici parola per parola; jingle quiz OK; peso, fotogrammi, fondo bianco e nessun numero di lezione OK; glossario, quiz da 5 domande, verifica da 10 domande e compiti presenti; PDF A4 orizzontale con testo selezionabile e senza nome del docente.
**Difetti trovati e come li ho trattati:**
| Difetto | Esito |
|---|---|
| D3 −17,1 LUFS (fuori da −16 ±1); D0 −17,0 e D6 −17,2 al limite | **corretti**: guadagno +0,9/+1,0/+1,1 dB con limitatore; ora tutti −16,1…−16,5 |
| Titolo a due righe di «Quer pasticciaccio brutto de via Merulana» (approfondimento 6): la barretta blu tagliava «Quer» e «Merulana» | **corretto** (barretta sotto la seconda riga) e scheda rifatta |
| Il riquadro del prof compare/sparisce di colpo all'inizio/fine dei pezzi D (la slide fa dissolvenza, il riquadro no) | **NON corretto**: serve rifare i 7 pezzi D con dissolvenza del riquadro (~25 min di calcolo): da fare con la master |
| La dispensa non ha il riquadro «ARGOMENTI» della copertina del video | voluto dalla regola (dispensa: solo materia e titolo); segnalato |
| Dopo la scheda nera con avviso diritti seguono Compiti (CI1, COMP) | è l'ordine delle regole (§3.4: sigla finale, poi intro Compiti e compiti): nessuna azione |
| «RAI» non spiegata a schermo né a voce | **NON corretto**: serve voce nuova Kore (R2) |
| Sigla 16,3 s «[ANALISI TESTUALE]» (versione del montaggio precedente) diversa dal file `kit/sigle/Sigla_Letteratura_15s.mp4` (15 s, stessa animazione con tempi diversi) | **NON sostituita**: cambiare la sigla sposta di 1,3 s tutti i tempi (quiz, scheda). Decide la master |
| D5 comincia con ≈ 1,4 s di silenzio prima della prima parola | segnalato (< 2,5 s) |
| Misura «36 px»: corpo del testo ≈ 40 px (maiuscole alte 28 px) | corpo 40 px come da regola |

## 6. Cosa NON ho verificato / limiti
- **Ascolto umano: nessuno.** Fruscio, ronzio, «metallico» e pronuncia delle voci Kore: non verificati. Nella trascrizione automatica ci sono forme sospette da riascoltare: «il docente» (≈ 18:07 nella v1), «gattiano», «Mar Adal», «Dal Gisa», «brutto di via Merulana» (R1 e altre voci). Voce R1: nella trascrizione «I testi» risulta illeggibile.
- **Sigle:** «RAI» compare nell'approfondimento sulla vita (scheda «La svolta») e nella voce narrante, **senza spiegazione** («RAI, cioè Radiotelevisione italiana»): per rispiegarla serve una voce nuova Kore (R2) — **da fare con la master**.
- **Sottotitoli:** il controllo del kit sul loro attacco (entro 0,3 s) era 70 % su 23 blocchi nella v2 (soglia 80 %): non rilanciato sul video finale; dubbi di testo del parlato del prof elencati nel rapporto del 17/11.
- **Caselle della mappa:** i tempi di comparsa vengono dai tempi della trascrizione di R1 (stima ±0,3 s), non da voci separate per riquadro.
- **Foto di Gadda** (ritaglio dal video del prof): bassa risoluzione, ingrandita; la webcam (246×137 px nel video originale) è ingrandita 2,25×: morbida; capelli al bordo già nell'originale. Le slide originali `.pptx` della lezione 20 non sono nella release.
- **Dispensa:** stessi modelli HTML del video; confronto pagina per pagina fatto a vista su un campione, non a pixel.
- **Date/anomalie del prof:** La meccanica: il prof dice «1924-28», schede e voce «1924»; nessun'altra discordanza.
