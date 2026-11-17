# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 7
**Il romanzo nell'Europa e nell'Italia del Decadentismo** · Prof. Giorgio Mazzotti · 17/11/2026
Etichette: **[misurato]**, **[stima]**, **[non verificato]**.

## 1. Misure sul video nuovo
- Durata 55:50,6 (3350,6 s), **100 518 fotogrammi** (= durata×30), 1920×1080 30 fps, **207,6 MB**, x264 veryfast CRF 19, AAC 192k (`finale_a_pezzi.py`) [misurato]. Durata uguale al video vecchio, quindi Vimeo/quiz restano allineati tranne T2 e Q1 (−4,0 s: 11:00 e 10:55) [misurato].
- Volume: −17,1 LUFS integrato (parlato del prof −16,2 LUFS prima del limitatore), **picco −1,6 dBTP** [misurato].
- **Sincronia audio/originale**: scarto −0,015 s (costante) su 41 punti dei 5 pezzi del prof; massimo 0,015 s ≤ 0,04 s [misurato, `syncchk.py`]. Il video del riquadro è tagliato dallo stesso istante dell'originale (stesso `-ss`): sfasamento labbra non misurato separatamente [non verificato a occhio].
- **Jingle Quiz** (`controllo_jingle.py`): Q1–Q4 scatto a +0,005 s dall'attacco atteso, OK [misurato]. Aggiunti anche `titolo.wav` sui 4 titoli, `repaso.wav` sui 4 ripassi, `trans.wav` in 22 transizioni, `finale.wav` sul finale, quiz.wav su Verifica e Compiti [misurato per Q e T; gli altri inseriti, non misurati].
- **Fermi immagine**: nessun fermo ≥ 1,5 s nei 5 pezzi del prof [misurato, `freezedetect`]. Nelle dissolvenze (1,3–1,6 s) tra un pezzo e l'altro l'ultimo fotogramma del pezzo precedente resta fermo mentre sfuma (transizione, non fermo).
- Il riquadro del prof compare **solo con il prof vivo** (D0, D1–D4); presentazione con voce narrante senza riquadro [misurato].
- Correzione 18:30 (richiesta 10:12): titolo della slide pagina 19 (23:20–24:30 circa, nel video 22:50–24:30) mandato a capo su due righe a sinistra del riquadro; verificato a fotogramma (min. 23:40) e controllate le altre slide col riquadro (titoli più corti, nessuna sovrapposizione) [misurato a vista]. Ricodificato D3 e rifatto il PDF slide; sha256 e parti rifatti.
- Contatto: `controllo_minuti.jpg` (1 fotogramma ogni 30 s, 112 fotogrammi) [misurato].

### Fine e inizio di ogni pezzo del prof (regola 01:25)
| Pezzo | Minuto video | Prime parole | Ultime parole | Frase finita |
|---|---|---|---|---|
| D0 | 0:45,8–2:09,3 | «Buongiorno e benvenuti alla lezione…» | «…del decadente, dell'esteta piuttosto che del simbolista.» | sì |
| D1 | 2:15,5–4:59,5 | «Allora. Iniziamo quindi in questo modo…» | «…o uno sfondo sociale storicamente definito.» | sì |
| D2 | 11:04,9–14:04,5 | «D'accordo, il testo si risolve…» | «…poi abbiamo la poesia di Verlaine e Rimbaud.» | sì |
| D3 | 21:47,9–31:02,0 | «Spostiamoci, come detto, in Inghilterra…» | «…Qua e, soprattutto, chi è e cosa scrive.» | sì |
| D4 | 40:57,7–45:57,4 | «Allora, spostando lo sguardo al contesto italiano…» | «…sempre in letteratura italiana, con Italo Svevo.» | sì |
Tutti i pezzi iniziano prima della prima parola e finiscono dopo l'ultima, a una pausa tra frasi [misurato sulla trascrizione]. In D3 sono tolti 3 tratti di pausa (1,4 s ciascuno, nei silenzi tra frasi) e in D4 5 pause sono rallentate ×0,5 (non fermate) per tenere la durata: nessuna parola toccata.

## 2. Confronto col modello (punto 000)
| # | Voce | Esito |
|---|---|---|
| 1 | Sigla → dissolvenza → copertina | corretto (sigla del kit, dissolvenza morbida) |
| 2 | Copertina (logo, riga blu, titolo Bricolage, card ARGOMENTI) | corretto, 4 argomenti |
| 3 | Slide (fondo bianco, «NN · ARGOMENTO», titolo+barretta, card gialla in corso) | corretto |
| 4 | Piè di pagina «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» + «Pagina N» | corretto |
| 5 | Riquadro 4:3 412×310 a x1428 y148, ombra grigia, niente bordo blu | corretto; **limite noto**: la testa tocca il bordo alto già nell'originale (webcam 246×138, ritaglio 184×138 ingrandito 2,24×: immagine morbida), per tutta la lezione |
| 6 | Fascia gialla −3°, due righe | corretto |
| 7 | Slide senza prof | corretto |
| 8 | Font Bricolage / Figtree Bold (non DM Mono) | corretto [a vista, non con OCR] |
| 9 | Finale con avviso diritti | corretto (kit) |
| 10 | Struttura obbligatoria | presente |
| 11 | PDF A4 slide e mappe | fatti: slide 40 pagine, mappe 5 pagine; **confronto pagina per pagina col fotogramma fatto a vista su un campione, non su tutte le 40** [parzialmente verificato] |
Card in corso: bordo giallo sottile, numero su pallino giallo, fondo bianco; ombre grigie morbide (regola 01:30) [a vista].

## 3. Problemi trovati e correzioni
| # | Minuto (video vecchio) | Tipo | Com'era | Correzione |
|---|---|---|---|---|
| 1 | tutto | visivo | Grafica diversa dal modello Spagnolo: banda blu notte a destra, prof piccolo senza riquadro 4:3 né ombra, nessuna fascia gialla, animazioni su fondo blu notte, piè di pagina diverso | Tutta la lezione rifatta nel modello (fondo bianco, riquadro 4:3 412×310 a x1428 y148, fascia gialla −3° su due righe, riga «NN · ARGOMENTO», piè di pagina e «Pagina N») |
| 2 | 0:18–0:44 | visivo | La presentazione elencava **3 argomenti su 4** (mancava Grazia Deledda) | Copertina con card ARGOMENTI con tutti e 4, evidenziati man mano che la voce li nomina |
| 3 | 0:30–0:45 | visivo | Dissolvenza dalla sigla con titolo doppio sovrapposto | Dissolvenza morbida sigla → copertina, nessun testo sovrapposto |
| 4 | AN5 (9:21), AN11 (19:44), AN19 (38:49), AN24 (50:10), ANF (52:02) | contenuto | Mappe concettuali **inventate da noi** (rami «i due pilastri», «la psicologia», «la trama», «Nato a Dublino»…) | Mappa **del prof** (MAPPE/LEZIONE 7.pdf), nodi identici, impaginata con la nostra grafica; una per argomento (stessa mappa, nodi dell'argomento accesi) + mappa finale; voci nuove M5b, M11, M19b, M24, MF che leggono solo i nodi del prof |
| 5 | 2:15 (inizio D1) | audio | La parola «Allora.» del prof (orig. 84,1–84,6 s) era tagliata via | D1 ora parte da 83,9 s e la include |
| 6 | 30:57–31:02 e 40:57–41:00 | audio | Frasi del prof **ripetute** (D2→D3 0,2 s; D3→D4 2,0 s: «…Cosa c'entra Deledda soprattutto?») | Pezzi contigui senza ripetizioni |
| 7 | 4:59 (fine D1) | audio | Pezzo del prof finito a metà frase («…il testo si risolve») | D1 finisce a «…storicamente definito.» (247,9 s), D2 parte da «D'accordo, il testo si risolve…» (248,4 s) |
| 8 | fine D4 | audio/video | D4 durava 1,2 s oltre la fine dell'originale | Chiude esattamente sull'ultima parola |
| 9 | tutto | audio | Audio del prof non rifatto dall'originale con la catena del kit | Rifatto: aresample 48k, highpass 80, arnndn (sh.rnnn), loudnorm −16, alimiter; picco −1,5 dBTP |
| 10 | 0:46–… | testo | Sottotitoli con frasi senza senso («injustamente isolandola», «simbolismo in giudanale», «Uism»…); ~660 parole su 2627 dei pezzi del prof diverse nel nuovo | `.vtt` rifatto dall'originale, riletto cue per cue, nomi corretti (Huysmans, Des Esseintes, Zola, Médan, Wilde, Ruskin e Pater…), max 2 righe da 42, anche voce narrante |
| 11 | file | testo | `compiti.json` in formato sbagliato (chiave `compiti`) | `{"titolo","esercizi":[{"n","tipo","testo"}]}`, testo identico al PDF del prof |
| 12 | file | testo | `scheda_pubblicazione.json` con titolo senza «Letteratura V · Lezione 7 ·» | Titolo standard; secondi di T2/Q1 aggiornati (−4,0 s) |
| 13 | file | testo | `Test_Letteratura_Lez7.xlsx` non era la verifica del prof | `verifica_finale.json` + `.xlsx` con le **10 domande** di «DOMANDE LEZIONE 7.xlsx» |
| 14 | file | testo | `testo_youtube.txt`: capitoli sbagliati (5:44, 9:36, 19:48, 25:38) | Rigenerato: 2:10, 11:00, 21:42, 40:52, 53:18 |
| 15 | file | testo | `timeline.json`: S4 con inizio sbagliato (2758,8 invece di 3078,4) | Corretto |
| 16 | file | pagina | Dispensa A4 vecchia (21 pagine, grafica vecchia) | `…_slide.pdf` 40 pagine A4 orizzontali nel modello, `…_mappe.pdf` 5 pagine |
| 17 | 55:32 | video | Finale nero senza logo né avviso diritti | `Sigla_finale_5s_con_avviso_diritti.mp4` del kit |
| 18 | schede Quiz/Verifica/Compiti/Fine | visivo | Schede di servizio su fondo blu notte | Rifatte nel modello (bianco) |


## 4. Pagine del libro in alta risoluzione
La lezione 7 non ha pagine del libro e nella release non c'è lo zip «ingrandita» (elenco asset) [misurato]. Nessuna fettina, nessun `controllo_fettine.jpg`.

## 5. Cosa NON ho verificato / limiti residui
- **Silenzi > 3 s ancora presenti (5)**, dopo l'inserimento dei jingle [misurato]: 9:13–9:16 (3,0 s, coda AN4), 44:14–44:19 (**5,3 s**: pausa naturale del prof 2,7 s + 2,5 s di rallentamento in D4; da accorciare ricodificando D4), 53:14–53:18 (4,5 s, coda voce mappa finale), 55:20–55:24 (3,7 s), 55:45–55:50 (4,8 s, fine). Vanno tolti con un'altra ricodifica.
- **Ascolto umano delle voci Kore** (pronuncia di Huysmans, Des Esseintes, Médan, Wilde, titoli) e delle 5 voci nuove delle mappe (M5b, M11, M19b, M24, MF; M5b e M19b velocizzate del 4,5% per entrare nella durata): non fatto, solo trascrizione automatica.
- **Sottotitoli**: corretti sul senso e sui nomi, allineati con i tempi parola per parola della trascrizione; non riascoltati a orecchio. Tratti dubbi: 218,8–219,9 s dell'originale («per forza robotica», omesso), 225,6–229,5, 230–233, 358–362 (frammenti non decifrabili, in parte omessi), 536–548 (Stevenson/«L'isola del tesoro»), 559–567 e 570 s («Basil», parafrasato), 1176–1180. Sincronia sottotitoli non misurata col criterio ±0,3 s.
- Evidenziazione delle card: derivata dalla trascrizione del prof, controllata solo a campione su fotogrammi; la card «L'estetismo» della slide 3 resta spenta perché il prof ne parla più avanti.
- Pagina interattiva e quiz: contenuto letto, non provato nella pagina. Il quiz Q2-3 («ne condensa la visione») è un'interpretazione.
- Non ho controllato a vista tutti i fotogrammi, né il PDF slide pagina per pagina, né la dispensa col video.
- La pronuncia/accento di «Wismans» nelle voci, riconosciuta dal trascrittore, può indicare una pronuncia sbagliata della voce: **da ascoltare**.

## 6. Come ho verificato
Trascrizione Parakeet (`trascrivi.py`) di originale e voci; fotogrammi e contact sheet; correlazione audio (sync e jingle); `freezedetect`, `silencedetect`, `ebur128`; confronto parole `.vtt` vecchio/nuovo (≈660 su 2627 dei pezzi del prof diverse).

## DA CONFERMARE COL PROF
- Slide 3, card «L'estetismo»: nel video la spiega con Wilde (min. 467 s dell'originale), non in quel punto.
- «Basil» (nome del pittore) è in AN13/voce narrante e nei sottotitoli; il prof dice un nome poco chiaro (570 s).
- Quiz/verifica: la domanda 3 della verifica del prof («…vita oscilla tra noia e dolore») non è letteralmente nelle slide.
