# RAPPORTO · Storia V · La prima guerra mondiale · correzioni 22/11 (3 Parti)
Etichette: **misurato** = misura sul file consegnato; **non verificato** = non controllato.

## Misure (misurato su Storia_Lez4_ParteN_1080p.mp4)
| Parte | durata | fotogrammi (= durata×30) | peso | LUFS | picco | 1920×1080 30 fps |
|---|---|---|---|---|---|---|
| 1 | 45:25 | 81749 | 295 MB | −16,6 | −1,0 dBFS | sì |
| 2 | 38:47 | 69824 | 262 MB | −16,4 | −1,3 dBFS | sì |
| 3 | 50:28 | 90850 | 345 MB | −16,7 | −1,4 dBFS | sì |
Una sola ricodifica finale x264 veryfast CRF 22 (CRF 19 superava i 400 MB), AAC 192k 48 kHz. Le Parti 1 e 2 sono sotto i 50 minuti: la lezione ha ~104 min di prof (per la master, 3 Parti da ~45 min; la risposta non è arrivata).

## Cosa è stato rifatto
- **Audio del prof dall'originale** (release `mazzotti-storia-V`, LEZIONE 4): solo filtro dei bassi 70 Hz, riduzione leggera del rumore (afftdn nr 6) e +2,5 dB sopra 4 kHz. Timbro (acuti >4 kHz meno >100 Hz) **misurato** su 10 campioni: originale −15,8…−21,8 dB, dopo la pulizia −15,5…−19,8 (prima del +2,5 dB: uguale all'originale). Tono 129–148 Hz e chiarezza ~1250–1360 Hz **identici all'originale** nei 6 punti controllati (stessa misura di controllo_severo). Pause oltre 2,5 s accorciate a circa 1 s (tagli solo nelle pause tra frasi).
- **Mappe**: le 6 del prof (PDF «MAPPE LEZIONE 4»), ridisegnate in vettoriale nel modello BES, ramo per ramo con la voce MAP1–6; colori BES assegnati da noi (il prof ha date e armistizi in arancio: da approvare). Mappe inventate dalle chat tolte; i 5 argomenti senza mappa (2, 4, 7, 8, 11) chiudono con la pillola; **nessuna mappa finale della lezione**. Dettagli: mappe_video/RAPPORTO_MAPPE.md. Voce MAP2: non dice «e di Leopoli» (è nel riquadro).
- **Slide**: card intere a 40 px, interlinea 1,5, massimo 3 per slide (di solito 2), finestre a rotazione ogni ≤150 s, bordo giallo all'inizio della frase (cue dal parlato); riquadro 4:3, piè di pagina «Storia V» senza nome del docente, nome solo nella fascia.
- **Introduzione**: copertina Kore senza riquadro né nome; prof sopra la copertina (100 s) poi «Il percorso della lezione» (sotto i 3 minuti).
- **Spiegone** all'apertura delle Parti 2 e 3 (voci SP2_x, SP3_x, senza nome del docente).
- **Approfondimenti animati** (AP1–AP11, voce Kore, solo materiale del prof), uno per argomento.
- **Ripasso**: pillola e schema in blu scuro a tutto schermo.
- **Parte 3**: scheda «Verifica finale» (jingle quiz + voce VER_0), sigla finale con avviso dei diritti, intro «Compiti» con jingle e compiti letti dalla voce Kore (CP_0–CP_4, parole del prof) a uno a uno con bordo giallo.
- Dispense A4 orizzontali con strato di testo invisibile, copertina solo materia e titolo (stessa grafica della copertina slide); PDF mappe a parte (Storia_Lez4_mappe.pdf, copertina «MAPPE»). Sottotitoli .vtt, timeline, scheda di pubblicazione.

## Voci (controllate: trascritte e confrontate parola per parola, controllo_voci.json)
Le 28 voci nuove: differenze solo di forma (numeri in cifre/in lettere, grafie ASR come «Tirpiz»). Bordi: ampiezza negli ultimi 50 ms <0,03 in 27 su 28; **SP3_1 = 0,23** (finisce secca): messa dissolvenza 30 ms su tutte le voci, non rifatta. Pronuncia dei nomi stranieri: **non ascoltata**.

## Refusi
Controllo automatico di accenti e forme errate sul testo delle slide e del test Excel: nessun refuso trovato. Controllo ortografico completo: **non fatto**. Nessun numero modificato.

## Difetti noti / non verificato
- Controllo rapido (controllo_rapido.py): i json/fogli allegati sono quelli prodotti sulle versioni intermedie dei file (stesso montaggio; cambia solo il guadagno audio); sul file finale delle Parti 1 e 3 il programma non ha terminato (bloccato sotto carico). Misure sopra fatte a parte con ffprobe/ebur128.
- Controllo severo (OCR): non completato su nessuna Parte.
- **Agente separato del §11: non eseguito** (consumo).
- Immagini degli approfondimenti e degli spiegoni: nella versione consegnata sono nel riquadro a destra (~840 px, più piccole di quanto richiesto); versione con immagine grande pronta nello script ma non montata.
- Immagini del prof: i PDF le contengono a ≤800 px; ingrandite 2× (Lanczos + nitidezza), non nitide come l'alta risoluzione.
- Compiti: manca la frase finale «Svolgi i compiti qui sotto e premi Consegna…» (voce non richiesta in tempo; solo scheda).
- Verifica: scheda + file Excel/json (le domande non scorrono nel video).
- Numeri pagina sulle slide non coincidono con la dispensa.
- Sottotitoli: generati dai testi e dalla trascrizione del prof con correzioni, **non** rifatti dal video finale con ASR.
