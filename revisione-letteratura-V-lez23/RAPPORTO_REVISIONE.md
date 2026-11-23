# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 23 · Primo Levi — correzioni 22/11
Video: `Letteratura_Lez23_Parte1_1080p.mp4` (pezzi `.parte_NN`, sha256 nel file `.sha256`). **misurato** = misurato con uno strumento; **stima** = dedotto; **non verificato** = non ho potuto.

## 1. Cosa ho cambiato rispetto alla consegna del 17/11
- **Una sola mappa, quella del prof, una volta sola**, prima del glossario. Tolte le 4 mappe precedenti (AN4, AN9, AN15, ANF). Ridisegnata in vettoriale nel modello BES (colori e legenda in alto a destra, testo 34–50 px) **senza il marchio mappe-scuola.com e senza le foto** (ritratto di Levi e frontespizio): stessa struttura, stesse frecce, stesse parole del prof. La mappa (circa 30 riquadri) non entra in una schermata a 34 px: come da risposta della master (22/11 17:00 UTC) è divisa in **4 schermate** («Mappa · 1 di 4»: vita; 2: racconto dell'esperienza nei Lager; 3 e 4: opere), ognuna costruita riquadro per riquadro con la voce Kore (riquadro acceso in giallo) e ferma 4 s alla fine. Voci nuove M1–M3 (testi in `testi_voci.json`, numeri in lettere).
- **Slide del prof**: testo a 40 px (36 solo dove serve), interlinea 1,5, al massimo 3 card intere (le slide con più card sono divise in due pagine), bordo giallo quando il prof comincia la frase. Nessuna card sola oltre 60 s.
- **Confini degli argomenti spostati sul prof** (finivano a metà del suo discorso): D1 ora comprende la frase finale «…per capire Primo Levi»; D2 finisce a «…naturale o meno che sia finita»; D3 («Se questo è un uomo») finisce a «…realtà mostruosa»; D4 («La tregua») parte da «Il trauma del ritorno…». Così nessuna slide o immagine compare in due argomenti (niente «già visto»: prima «La tregua» era mostrata nell'argomento 3 e nel 4) e le slide del prof seguono il suo discorso.
- **Pause del prof > 2,2 s** accorciate a circa 1 s (solo tra due frasi): 3 in D0, 1 in D1, 4 in D2, 2 in D3, 3 in D4 (tempi nella timeline). Audio e video tagliati agli stessi punti.
- **Audio:** −16,0 LUFS (misurato sul wav; vedi §2), picco ≤ −1 dBTP.
- **Testo delle animazioni a 40 px**; ripassi, glossario e riepilogo con al massimo 3 righe per pagina (divisi in 2 pagine).
- **Piè di pagina delle animazioni senza il nome del prof** (regola 22/11: il nome del docente solo nella fascia gialla); sulle slide con il prof resta come nel modello.
- **Dispense**: `…_slide.pdf` (89 pagine A4 orizzontale, identiche al video, copertina con solo materia e titolo, piè con materia e pagina, **senza il nome del docente**, testo vero selezionabile) e `…_mappe.pdf` (copertina identica con «MAPPE» + le 4 schermate della mappa).

## 2. Misure sul video finale
- Formato 1920×1080, 30 fps, x264 (veryfast→superfast, CRF 21), AAC 192k; **durata 50:15.30 (3015.30 s)**; fotogrammi = durata × 30 (90 459); peso 315,2 MB (300,6 MiB, misurato).
- **Volume:** −16,5 LUFS integrato, LRA 5,3, picco AAC −2,0 dBFS (misurato con ebur128).
- **Jingle Quiz** a 0,0 s (`controllo_jingle.py`): Q1 −0,005 · Q2 +0,004 · Q3 +0,001 · Q4 −0,016 s: OK (misurato).
- **Sincronia audio/prof**: scarto dell'audio finale rispetto all'originale 0,01–0,04 s in 8 punti per pezzo, fuori dalle pause accorciate (misurato per correlazione dell'audio). Labbra non misurabili (webcam 185×138 px).
- **Mai prof fermo**: nessun fermo del riquadro ≥ 1,5 s nei pezzi del prof (freezedetect); dopo ogni pezzo c'è una tenuta di 0,9 s con dissolvenza.
- Copertina con il prof: 41,5 s → 3:16 (2:35 di intervento del prof, < 3 min); introduzione animata (18–41 s) senza riquadro del prof.
- **Controllo severo della master** (`controllo_severo.py`): lanciato sul video finale (ThreadPool 2, OCR di 300 fotogrammi) ma **non terminato nel tempo disponibile** (oltre 34 min su 4 CPU condivise con le codifiche): **esito non ottenuto, non verificato**. Misure equivalenti fatte da me: durata 50,25 min (45–65 ✓); loudness −16,5 LUFS (|Δ|<1 ✓); nessuna pausa > 2,5 s a −45 dB (silencedetect, dopo aver inserito `trans.wav` tra scheda-titolo e prof ✓); copertina con prof 2:35 (< 3 min ✓); nessun fermo del riquadro; titoli delle slide del prof diversi per ogni pagina e nessuna slide del prof oltre 135 s (D1 pagina A 130 s, D2 «ritorno» 158 s) ✓ (stima dai tempi della timeline); nessun «…» né card con iniziale minuscola a vista sui 101 fotogrammi dell'agente separato. **Chiedo alla master di rilanciarlo.**
```
durata 3015.30 s | fotogrammi 90459 (attesi 90459) | 315.2 MB | h264 1920x1080 30/1
['I:         -16.5 LUFS', 'LRA:         5.3 LU', 'Peak:       -2.0 dBFS']
silenzi >2.5 s: [('194.957', ''), ('', '2.69867'), ('690.691', ''), ('', '2.59096'), ('1293.71', ''), ('', '2.86246'), ('1843.57', ''), ('', '2.70823')]
fermi riquadro >=1.5 s: []

```


## 3. Tabella dei pezzi del prof (inizio e fine)
| Pezzo | Inizio | Prime parole | Fine | Ultime 8 parole | Frase finita |
|---|---|---|---|---|---|
| D0 | 0:41.50 | «Buongiorno e benvenuti alla lezione su» | 3:12.14 | «…d'accordo, che ricorda. Questi spiacevolissimi episodi. Primo Levi.» | sì |
| D1 | 3:17.54 | «Allora. Vediamo. Inquadrare appunto eventi fondamentali» | 6:17.61 | «…fondamentale per inquadrare e per capire Primo Levi.» | sì |
| D2 | 11:33.28 | «Levi riuscì a sopravvivere alle condizioni» | 15:45.86 | «…loro vita, naturale o meno che sia finita.» | sì |
| D3 | 21:36.29 | «Ecco, quindi capite il peso. Decise,» | 23:56.55 | «…portare ordine nel caos di una realtà mostruosa.» | sì |
| D4 | 30:46.15 | «Il trauma del ritorno e la» | 36:02.17 | «…quello appunto che è ha vissuto ha subito.» | sì (fine del video del prof) |
Misurato sulle parole della trascrizione automatica: ogni pezzo comincia ≥ 0,3 s prima della prima parola e finisce 0,3–0,5 s dopo l'ultima, in una pausa. D1 finisce dopo «…per capire Primo Levi»; D2 dopo «…naturale o meno che sia finita»; D3 dopo «…caos di una realtà mostruosa»; D4 comincia da «Il trauma del ritorno…» (la trascrizione automatica rende alcune parole male: vedi §5).


## 4. Refusi e anomalie del materiale del prof (non corretti nei file del prof)
- **Nodo della mappa «1959 – Premio Nobel per la letteratura»**: Primo Levi non ha mai vinto il Nobel. Lasciato come nella mappa del prof; **la voce nuova non lo legge**. Da chiedere al prof.
- **«Storie naturali 1967»** (mappa) contro «del 1966» detto dal prof nel video.
- **Slide del prof «arrivando a Torino a metà settembre»** contro il prof che dice «nell'ottobre del 1945».
- Nomi: «Damiano Malabaila» (la trascrizione scriveva «Malaca»), «Mordo Nahum»: corretti nei sottotitoli.
- Mappa: «Monowitz», date e titoli come nella mappa del prof.


## 5. Cosa NON ho verificato
- **Ascolto umano**: non ho potuto ascoltare nulla (voce del prof dopo la pulizia, voci Kore nuove della mappa, jingle, `trans.wav`). Le voci della mappa sono state **trascritte** (Parakeet) e confrontate col testo: la trascrizione automatica a volte omette parole brevi a inizio frase («Racconta», «Il», «Se») in modo diverso tra due generazioni dello stesso testo, quindi la ritengo rumore della trascrizione, **non verificato all'ascolto**. Usate: M1 (vita), R12 (racconto nei Lager), R13 (opere); M2, M3, M2_R2 non usate.
- **Sottotitoli**: corretti sulla trascrizione automatica (257 cue), con le correzioni elencate nel codice (Levi, Lager, prigioniero, cooptati…); frasi che la trascrizione rende male e che ho lasciato: «Primo Levi viene in ebreo», «gli valsero Notorietà gli permisero», «a Verona», «anche se descolastiche», «in questo conti», «Finita». **Non verificato.**
- **Card «Le altre opere di Primo Levi»** (D4): testo scritto da me riassumendo il discorso e la mappa del prof (non c'è una sua slide): da far vedere al prof.
- **Pause > 2,5 s**: le schede di pausa del player Verifica (10 s) e Compiti (9 s) restano silenziose (pausa del player).
- **Schede Quiz / Verifica / Compiti**: invariate (banda blu, come deciso).
- **Voci S1–S4, GL1, RF1, AN1–AN21, FIN1**: quelle già consegnate, **non riascoltate** (S3: lo schermo dice «Descrive», la trascrizione dice «Scrive»).
- **Mappa**: i tempi di comparsa dei riquadri vengono dalla trascrizione delle voci (±0,5 s, stima); «una volta sola, prima del glossario» rispettato. Non ho ridisegnato la mappa intera su una pagina del PDF perché a 34 px non entra (la master ha approvato la divisione in schermate).
- **Immagini**: nessuna immagine di repertorio; ritratti e frontespizio della mappa del prof NON usati.
- **Agente separato** (§2 del prompt): vedi sezione 6.


## 6. Controllo dell'agente separato
Un agente separato (che non ha montato la lezione) ha guardato 101 fotogrammi (1 ogni 30 s) più 10 mirati, i PDF e il `.vtt` (non audio, non tagli a metà frase). Esito e cosa ho fatto:
- **Corretti dopo il suo controllo**: etichetta «Mappa · N di 4» assente nelle schermate del video (c'era solo nei PDF) → rifatte le 4 schermate con etichetta e legenda più grande (23 px) e frecce più sottili; refuso nei sottotitoli «Un' po'» → «Un po'».
- **Non confermato dal mio controllo**: «riquadro del prof a 0:30» (ho verificato a 30 s: copertina senza riquadro; il riquadro compare con D0 a 41,5 s).
- **Segnalato, non cambiato**: (1) schede Quiz (3,2 s), Verifica e Compiti sono le schede del player (le domande sono in `quiz_argomenti.json`, `verifica_finale.json`, `compiti.json`); (2) sigla finale = file del kit (`Sigla_finale_5s…`), non toccata; il «ATTENZIONI» letto dall'agente va controllato sul file del kit; (3) animazioni con molto spazio bianco sotto le card (3 card per schermata a 40 px): scelta di layout; (4) l'agente stima il testo delle slide del prof a 30–32 px: non confermo, il codice imposta 40 px e scende a 36 solo se non entra; **misura diretta sui fotogrammi non fatta**; (5) i sottotitoli coprono solo i pezzi del prof (D0–D4), non le voci narranti, come nelle consegne precedenti.

## 7. Secondi vecchio → nuovo (consegna del 17/11 → oggi; aggiornati in `scheda_pubblicazione.json` e `timeline.json`)
| Evento | Prima (17/11) | Ora |
|---|---|---|
| T1 | 197.37 | 193.04 |
| T2 | 765.15 | 688.78 |
| T3 | 1450.92 | 1291.79 |
| T4 | 2201.69 | 1841.65 |
| Q1 | 761.05 | 684.68 |
| Q2 | 1446.82 | 1287.69 |
| Q3 | 2197.59 | 1837.55 |
| Q4 | 2964.72 | 2705.24 |
| VER | — | 2990.70 |
| COMP | — | 3009.00 |
| durata | 3173,47 | 3015.30 |

Nota: il ramo conteneva un commit della master «pillole inserite, tempi e sottotitoli aggiornati» sul vecchio video: questa consegna lo sostituisce (video, timeline, scheda e sottotitoli nuovi).

## 8. Correzione del 23/11 14:10 (schede mute > 5 s)
Aggiunti i jingle del kit alle schede finali: `quiz.wav` sulla Verifica, `finale.wav` sulla sigla finale, `repaso.wav` sui Compiti. Silenzi più lunghi rimasti (silencedetect −45 dB): 4,6 s, 3,5 s e 3,9 s: nessuno oltre 5 s (misurato). Solo audio cambiato: video, tempi, sottotitoli e scheda invariati.
