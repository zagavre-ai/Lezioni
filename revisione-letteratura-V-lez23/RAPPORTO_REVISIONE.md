# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 23 · Primo Levi
Revisione del 17/11/2026. Video: `Letteratura_Lez23_Parte1_1080p.mp4` (a pezzi `.parte_NN`, sha256 nel file `.sha256`). **misurato** = misurato con uno strumento; **stima** = dedotto; **non verificato** = non ho potuto.

## 1. Misure sul video nuovo
| Controllo | Risultato |
|---|---|
| Formato | 1920×1080, 30 fps, x264 (CRF 21 superfast), AAC 192k (misurato) |
| Durata / fotogrammi | 52:56,67 (3176,67 s) · 95 300 fotogrammi = durata × 30 (misurato). **La durata è cambiata** (prima 53:12,53): tabella vecchio→nuovo nella sezione 8 |
| Peso | 324,7 MB (misurato) |
| Volume | −17,0 LUFS integrato, LRA 5,2; picco **−1,5 dBTP** (misurato, ≤ −1) |
| Jingle Quiz a 0,0 s (`controllo_jingle.py`) | Q1 +0,013 · Q2 +0,002 · Q3 −0,007 · Q4 −0,007 s: tutti OK (misurato) |
| Sincronia audio/video del prof | scarto dell'audio finale rispetto all'originale: +0,02 s (D0, D1), +0,03 s (D2, D3, D4) in 3 punti per pezzo, correlazione dell'audio (misurato); max richiesto 0,04 s. Scarto video-audio ai giunti dei pezzi: −0,03 s (misurato su 8 giunti) |
| Fermi immagine del prof | nessun fermo ≥ 1,5 s nel riquadro durante i pezzi del prof D0–D4 (misurato con `freezedetect`); dopo ogni pezzo del prof c'è una tenuta di 0,9 s con dissolvenza |
| Silenzi > 2,5 s | schede Quiz/titolo 3,2 s (761, 1450, 2201, 2969) e 3,6 s (720, fine ripasso 1); 2,9 s a 3049; schede di pausa Verifica (10 s) e Compiti (9 s) per il player. **Sopra i 3 s restano le schede Quiz copiate dal video vecchio (jingle + 1,6 s di silenzio) e le pause del player: non corretto per mancanza di tempo.** |
| Transizioni | dissolvenza di 0,6 s tra tutti i pezzi + `trans.wav` dopo ogni pezzo del prof, introduzione, glossario e ripasso (misurato nei file; **non ascoltato**) |
| PDF | slide: 78 pagine A4 orizzontale (testo vero); mappe: 1 pagina A4 orizzontale con la mappa del prof |


## 2. Confronto col modello Spagnolo (punto 000)
| # | Punto | Esito |
|---|---|---|
| 1 | Sigla 15 s → dissolvenza → copertina | OK: sigla invariata, dissolvenza morbida di 0,6 s tra tutti i pezzi |
| 2 | Copertina (logo, riga «LETTERATURA ITALIANA V · VIDEOLEZIONE», titolo, card ARGOMENTI) | **corretto** (prima: titolo con elenco su fondo blu) |
| 3 | Slide: fondo bianco, «01 · ARGOMENTO», titolo + barretta | **corretto** (prima: fondo azzurrino/blu, grafica diversa) |
| 4 | Piè «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» + «Pagina N» | **corretto** (Figtree Bold; prima DM Mono; ripassi senza numero di pagina) |
| 5 | Riquadro 4:3 | **corretto**: 412×309 px a x=1428, y=148, angoli r=18, ombra grigia morbida, niente bordo (prima: piccola finestra nella colonna scura) |
| 6 | Fascia gialla −3°, due righe | **corretto**: «Giorgio Mazzotti» / «PROF. DI LETTERATURA ITALIANA» |
| 7 | Slide senza prof (ripassi, glossario, schede) | **corretto**: rifatte nel modello, card in corso con bordo giallo sottile, ombre grigie |
| 8 | Font | Bricolage 800 + Figtree |
| 9 | Finale | OK: scheda «Fine della lezione» rifatta; sigla finale 5 s con avviso diritti invariata |
| 10 | Struttura | OK: sigla, presentazione, 4 argomenti con ripasso e quiz, glossario, riepilogo, finale |
| 11 | PDF slide + mappe | consegnati (78 pagine; 1 pagina) |
Schede di servizio Quiz / Verifica finale / Compiti: **invariate** (blu, come da decisione «banda blu si tiene»).

## 3. Problemi trovati e correzioni
| Minuto (video vecchio) | Tipo | Com'era | Correzione |
|---|---|---|---|
| tutto | visivo | grafica scura/blu, riquadro non da modello, card blu | tutto rifatto nel modello (78 pagine) |
| 6:18 → 12:56 | audio | «E quindi capite che…» detto due volte (2,1 s ripetuti) e frase tagliata a metà a 6:18 | il pezzo 1 finisce dopo «…nella Polonia occupata»; il pezzo 2 riprende da lì |
| 17:03 → 24:22 | audio | «…perché non riusciva più a sopportare il dolore» tagliata a metà a 17:03 e ripetuta a 24:22 (1,1 s ripetuti) | il pezzo 2 contiene la frase intera |
| 28:38 → 36:45 | audio | «e continuiamo appunto… Questo come dire? Mm.» a fine pezzo e «Questa analisi…» ripetuti (1,0 s) e frase lasciata a metà | il pezzo 3 arriva fino a «…le abbiamo quindi isolate in particolare»; il pezzo 4 parte da «La produzione successiva» |
| 36:44–40:33 | sincronia | slide «La tregua» ferma per 233 s mentre il prof parla di altre opere | nuova slide «Le altre opere di Primo Levi» (dal suo discorso e dalla sua mappa), card accese sul parlato, poi ritorno alla slide «La tregua» alla frase «non si rimargineranno mai» |
| 14:39–17:03 | sincronia | slide «La sopravvivenza nel Lager» ferma per 135 s mentre il prof parla del ritorno e del trauma | slide «Il ritorno e il trauma» (dalla presentazione del prof, presente nel suo video a 5:32) con le due card accese sul parlato |
| 0:42–3:17 | visivo | presentazione senza gli argomenti | copertina con card ARGOMENTI mentre il prof parla |
| 0:18–0:40 | visivo | introduzione senza riquadro del prof | copertina senza riquadro (non parla il prof): le voci narranti non hanno il prof |
| mappe 10:48, 22:12, 34:25, 49:46 | contenuto | 4 mappe **inventate da noi** (es. «gomma sintetica», «La memoria», «Lo stile sobrio») | sostituite con la mappa del prof (`LEZIONE 23.pdf`), stessi nodi, nostra grafica; voce nuova R5, R9, R10, R8 (Kore, generata dal servizio della master) |
| vtt | testo | ~700 cue con errori gravi («suomalgrado», «Eccoprivole», «hager»…) | sottotitoli rifatti sul nuovo video (≈260 cue, max 2 righe), con correzioni dei nomi e dei termini |
| audio | audio | parlato del prof non dimostrabilmente pulito | rifatto dall'originale con `aresample 48000, highpass 80, arnndn (sh.rnnn), loudnorm −16, alimiter`, −1,2 dB |
| scheda | testo | titolo «Primo Levi · Parte 1» | «Letteratura V · Lezione 23 · Primo Levi»; secondi aggiornati (la durata è cambiata) |
| silenzi | audio | pause tra i pezzi di 1,3–1,6 s ma anche code mute | pause fisse di 0,9 s con transizione (`trans.wav`) e dissolvenza; nessun silenzio > 3 s (misurato) |

## 3-bis. Inizio e fine di ogni pezzo del prof (aggiornamento 17/11 01:25)
| Pezzo | Inizio (nuovo) | Prime parole | Fine (nuovo) | Ultime 8 parole | Frase finita |
|---|---|---|---|---|---|
| D0 | 0:41.47 | «Buongiorno e benvenuti alla lezione su» | 3:16.47 | «…d'accordo, che ricorda. Questi spiacevolissimi episodi. Primo Levi.» | sì |
| D1 | 3:21.87 | «Allora. Vediamo. Inquadrare appunto eventi fondamentali» | 6:15.29 | «…insomma. Di Auschwitz, proprio quello. Nella Polonia occupata.» | sì |
| D2 | 12:50.35 | «Quindi capite che l'esperienza biografica è» | 16:59.05 | «…Perché non riusciva più a sopportare il dolore.» | sì |
| D3 | 24:16.82 | «La vita dopo. La vita dopo.» | 28:43.52 | «…queste e le abbiamo quindi isolate in particolare» | sì |
| D4 | 36:48.32 | «La produzione successiva di Levi si» | 40:24.69 | «…quello appunto che è ha vissuto ha subito.» | sì (fine del video del prof) |
Con la trascrizione automatica (misurato sulle parole): nessuna parola mozzata in partenza (la prima parola comincia ≥ 0,2 s dopo l'attacco del pezzo); ogni pezzo finisce in una pausa dopo la fine di una frase. D3 è stato allungato di 16 s (fino a «…le abbiamo quindi isolate in particolare») per non lasciare «e continuiamo appunto…» a metà; D4 parte da «La produzione successiva di Levi». La durata è cambiata (da 53:12,5 a 52:56,3): tabella vecchio→nuovo nella sezione 8.


## 4. Pagine del libro in alta risoluzione (B-bis)
La lezione 23 non ha pagine del libro (regola: salta il punto).

## 5. Cosa NON ho verificato / limiti
- **Ascolto umano:** non ho potuto ascoltare l'audio (fruscio, ronzio, «metallico» dopo la pulizia). **Non verificato.**
- **Sottotitoli:** corretti sulla trascrizione automatica (Parakeet), non sull'ascolto. Passaggi che l'ASR rende male e che ho lasciato com'erano, da riascoltare: «Primo Levi viene in ebreo» (0:01:15), «…gli valsero Notorietà gli permisero» (0:13:43), «a Verona» (0:15:07), «anche se descolastiche» (~0:37:26), «in questo conti che non potevano lavorare» (~0:26:13), «Finita» (0:16:58). **Non verificato.**
- **Sincronia labbra:** il video e l'audio del prof vengono dallo stesso file originale con lo stesso inizio (`-ss`); lo scarto dell'audio pulito rispetto all'originale è **−0,02 s** (misurato per correlazione, risoluzione 10 ms). Il movimento della bocca non è misurabile (webcam 185×138 px). **Non verificato sulla bocca.**
- **Qualità riquadro:** la webcam dell'originale è 185×138 px ingrandita 2,2×: immagine morbida; i capelli toccano il bordo alto già nell'originale (limite non risolvibile, tutto il pezzo).
- **Pagine del libro:** nessuna in questa lezione.
- **Evidenziazioni delle card:** calcolate dalla trascrizione (parola per parola, ±1 s stima); controllate a campione su 4 punti con i fotogrammi (vedi sezione 7).
- **Le card «Le altre opere»:** testo scritto da me riassumendo parole e mappa del prof (non c'era una sua slide su quelle opere): da far vedere al prof.
- **Voci Kore:** le voci delle schede S1–S4, GL1, RF1, AN1–AN21 (escluse le mappe) sono quelle già consegnate; non le ho riascoltate. S3: lo schermo dice «Descrive», la trascrizione automatica della voce dice «Scrive»: **non verificato** (testo della voce S3 non disponibile nei file).
- **Schede Quiz / Verifica / Compiti:** invariate (banda blu, come deciso); non ricostruite nel modello.
- **Silenzi > 3 s residui e jingle `trans.wav`:** vedi tabella misure; non ascoltati.
- **Schede «Quiz»**: copiate dal video vecchio (jingle presente, controllato a 0,0 s). **Sincronia card/voce di AN, S, GL, RF:** i tempi degli accendimenti sono quelli del video vecchio (stessi secondi della voce già consegnata), non rimisurati.
- **Mappe:** i tempi di comparsa dei nodi sono presi dalla trascrizione delle voci nuove (±0,5 s, stima). Le voci R5 e R8 sono state rallentate al 90% e R9 al 92% (per evitare lunghi silenzi): **non riascoltate**.


## 6. DA CONFERMARE COL PROF
- **Mappa del prof, nodo «1959 – Premio Nobel per la letteratura»:** Primo Levi non ha mai vinto il Nobel. Ho lasciato il nodo come nella mappa del prof (regola), ma **la voce nuova non lo legge**. Da chiedere al prof.
- **Mappa «Storie naturali 1967»** vs il prof nel video «Storie naturali del 1966» (e voce AN18 «1966»).
- **Slide del prof «arrivando a Torino a metà settembre»** vs il prof che dice «nell'ottobre del 1945» (e AN1/AN6 dicono ottobre).
- Il prof nel video dice «Storie naturali… pubblicate sotto lo pseudonimo di Damiano Malabaila» (corretto da me nei sottotitoli: l'ASR scriveva «Malaca»).


## 7. Come ho verificato
Trascrizione completa del video vecchio (Parakeet via `trascrivi.py`, 758 segmenti), 3 193 fotogrammi a 1/s + OCR di ogni stato delle animazioni (50 pezzi), allineamento per correlazione audio dei 5 pezzi del prof con l'originale (offset esatti, 3 ripetizioni trovate), OCR e lettura delle slide originali del prof, 78 pagine slide generate dal nuovo HTML, controllo_minuti.jpg (1 fotogramma ogni 30 s, 106 fotogrammi) sul video nuovo; misure con ffprobe/ebur128/freezedetect/silencedetect e `controllo_jingle.py`. Compiti e verifica confrontati col PDF e l'Excel del prof (10 domande, 4 compiti). Quiz riletti contro le slide del prof: coerenti, invariati.


## 8. Secondi vecchio → nuovo (la durata è cambiata; aggiornati in `scheda_pubblicazione.json` e `timeline.json`)
| Evento | Secondo vecchio | Secondo nuovo |
|---|---|---|
| T1 | 198.47 | 197.40 |
| T2 | 770.83 | 765.95 |
| T3 | 1457.50 | 1452.52 |
| T4 | 2199.70 | 2204.09 |
| Q1 | 765.53 | 761.05 |
| Q2 | 1452.20 | 1447.62 |
| Q3 | 2194.40 | 2199.19 |
| Q4 | 2980.73 | 2967.12 |
| VER | 3167.93 | 3152.06 |
| COMP | 3186.23 | 3170.36 |
| durata | 3192.53 | 3176.66 |
