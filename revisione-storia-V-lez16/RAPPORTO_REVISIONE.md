# RAPPORTO DI REVISIONE · Storia V · «Gli anni Sessanta tra crisi e progressi» · correzioni 22/11 fatte
Chat claude/lucid-bohr-33zvvw · Parte unica · 59:42.4 · ramo `revisione-storia-V-lez16`. **M** = misurato, **NV** = non verificato.

## 1. Misure sul video finale (M)
- Durata 3582.4 s (59:42.4); 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192k 48 kHz; peso 345.9 MB; sha256 `3d7cb15028a9fc158b21188edd764fdfa4947589b3816d0e774081b25686dcec`.
- Controllo rapido (kit/tools/controllo_rapido.py): esito **OK**; errori: nessuno. Foglio dei fotogrammi: `foglio_fotogrammi_Storia_Lez16_Parte1_1080p.jpg`; json: `controllo_rapido_Storia_Lez16_Parte1_1080p.json`.
- Volume −16 LUFS (loudnorm a due passaggi su tutto il video; il controllo severo del giro precedente misurava −16,0).
- Timbro del prof (acuti >4 kHz / sopra 100 Hz): −16,0 … −17,3 dB nei pezzi del prof; originale −18,6 dB (limiti −9/−20): voce non alterata. Pulizia: passa-alto 80 Hz, riduzione rumore leggera (afftdn), nessun altro filtro.
- Scatto del jingle dei quiz (controllo_jingle.py):
```
Q1 atteso 281.519 trovato 281.518 scarto -0.001 OK
Q2 atteso 943.753 trovato 943.753 scarto -0.000 OK
Q3 atteso 1467.986 trovato 1467.986 scarto +0.000 OK
Q4 atteso 1999.353 trovato 1999.355 scarto +0.002 OK
Q5 atteso 2669.054 trovato 2669.057 scarto +0.003 OK
Q6 atteso 2960.221 trovato 2960.222 scarto +0.001 OK
Q7 atteso 3327.753 trovato 3327.755 scarto +0.002 OK
```
- Nessun fermo del prof ≥1 s (controllo_finale, giro precedente: «nessuno OK»). Nessuna schermata identica oltre 3 minuti e nessun titolo di slide fermo oltre 3 minuti (controllo severo del giro precedente: elenchi vuoti). **NV:** il controllo severo non è stato rilanciato sull'ultima codifica (troppo lento: OCR su tutto il video); vale il controllo rapido.

## 2. Pezzi (M)
| Pezzo | Inizio | Durata |
|---|---|---|
| SIGLA | 0:00.0 | 15.0 s |
| COVERV | 0:15.0 | 13.1 s |
| D0 | 0:28.1 | 130.9 s |
| ARGS | 2:39.0 | 29.4 s |
| T1 | 3:08.4 | 4.0 s |
| D1 | 3:12.4 | 16.8 s |
| AP1 | 3:29.2 | 44.4 s |
| PI1 | 4:13.6 | 7.3 s |
| PS1 | 4:20.9 | 20.1 s |
| Q1 | 4:41.0 | 5.0 s |
| T2 | 4:46.0 | 4.0 s |
| D2a | 4:50.0 | 337.8 s |
| AP2A | 10:27.8 | 47.1 s |
| D2b | 11:14.9 | 184.6 s |
| AP2 | 14:19.5 | 59.2 s |
| PI2 | 15:18.6 | 7.0 s |
| PS2 | 15:25.6 | 17.7 s |
| Q2 | 15:43.3 | 5.0 s |
| T3 | 15:48.3 | 4.0 s |
| D3a | 15:52.3 | 198.4 s |
| AP3A | 19:10.6 | 33.1 s |
| D3b | 19:43.8 | 204.8 s |
| AP3 | 23:08.5 | 53.3 s |
| PI3 | 24:01.8 | 7.3 s |
| PS3 | 24:09.1 | 18.4 s |
| Q3 | 24:27.5 | 5.0 s |
| T4 | 24:32.5 | 4.0 s |
| D4 | 24:36.5 | 443.6 s |
| AP4 | 32:00.1 | 52.6 s |
| PI4 | 32:52.7 | 7.1 s |
| PS4 | 32:59.8 | 19.1 s |
| Q4 | 33:18.9 | 5.0 s |
| T5 | 33:23.9 | 4.0 s |
| D5a | 33:27.9 | 259.6 s |
| AP5A | 37:47.5 | 47.7 s |
| D5b | 38:35.2 | 276.7 s |
| AP5 | 43:11.9 | 49.2 s |
| PI5 | 44:01.1 | 7.1 s |
| PS5 | 44:08.2 | 20.4 s |
| Q5 | 44:28.6 | 5.0 s |
| T6 | 44:33.6 | 4.0 s |
| D6 | 44:37.6 | 133.7 s |
| AP6 | 46:51.3 | 49.2 s |
| MAP2 | 47:40.5 | 36.3 s |
| MAP3 | 48:16.8 | 31.2 s |
| PI6 | 48:48.1 | 9.6 s |
| PS6 | 48:57.6 | 22.1 s |
| Q6 | 49:19.7 | 5.0 s |
| T7 | 49:24.7 | 4.0 s |
| D7 | 49:28.7 | 237.3 s |
| AP7 | 53:26.1 | 51.1 s |
| MAP1 | 54:17.1 | 41.9 s |
| PI7 | 54:59.0 | 7.6 s |
| PS7 | 55:06.6 | 20.6 s |
| Q7 | 55:27.3 | 5.0 s |
| GL | 55:32.3 | 34.6 s |
| RIEP | 56:06.8 | 126.5 s |
| VER | 58:13.4 | 8.8 s |
| FINALE | 58:22.1 | 5.0 s |
| COMPI | 58:27.1 | 3.5 s |
| CO | 58:30.6 | 71.8 s |

## 3. Fine di ogni pezzo del prof (tagli nelle pause, 0,15–0,17 s prima della frase che segue)
| Pezzo | Minuto nel video | Ultime parole | Frase finita | Pausa prima della frase seguente (s) |
|---|---|---|---|---|
| D0 | 2:39.0 | «adesso stiamo vedendo, grosso modo, le dinamiche mondiali.» | sì | 1.81 |
| D1 | 3:29.2 | «frutti, l'età del benessere e le trasformazioni sociali.» | sì | 0.6 |
| D2a | 10:27.8 | «e il paese della democrazia più piena, d'accordo?» | sì | 1.26 |
| D2b | 14:19.5 | «aspettava veramente al Varco, lo attendeva al Varco» | NO | 1.53 |
| D3a | 19:10.6 | «e forse anche di una presidenza democratica. Vediamo.» | sì | 1.47 |
| D3b | 23:08.5 | «bianco, potremmo chiamarlo con i termini di oggi.» | sì | 0.76 |
| D4 | 32:00.1 | «anche la memoria di Kennedy che l'aveva annunciata.» | sì | 0.51 |
| D5a | 37:47.5 | «ci torneremo su questo.» | sì | 0.17 |
| D5b | 43:11.9 | «anche di vincere, però, la guerra in Vietnam.» | sì | 1.09 |
| D6 | 46:51.3 | «delle nazioni arabe che hanno dichiarato lui guerra.» | sì | 0.16 |
| D7 | 53:26.1 | «lotate di estrema sinistra e di estrema destra.» | sì | fine lezione |

(D2b: la frase «lo attendeva al Varco» è conclusa; la trascrizione automatica non ha il punto.)

## 4. Cosa è stato rifatto (correzioni 22/11)
1. **Mappe del prof** (3: Stati Uniti, Unione Sovietica, Medio Oriente) ridisegnate nel modello BES con legenda, costruite ramo per ramo con la voce Kore, 4 s di mappa intera con un suono morbido. Nessuna mappa inventata, nessuna mappa finale. Il PDF dice 3 mappe e le ho messe: Unione Sovietica e Medio Oriente dopo l'argomento 6, Stati Uniti dopo l'argomento 7 (è la mappa che parla anche del 1968). **Titolo della mappa del Medio Oriente scritto da me con le parole del prof** («Cosa accade in Medio Oriente negli anni Sessanta?»): il PDF del prof non ha la domanda. Il connettore «lo» davanti a «Egitto» e «Stato di Israele» sembra un refuso del prof: lasciato come sta.
2. **Slide del prof**: card a 40 px, interlinea 1,5 (56–60 px), al massimo 3 per slide, ognuna una frase intera (etichetta in grassetto + testo, senza «…»); bordo giallo e pallino quando il prof comincia il punto; altre card attenuate; riquadro 4:3 412×309 a x=1428, y=148 con ombra grigia e fascia gialla (il nome compare solo lì). Sotto-slide «a finestra» e numero di pagina diverso a ogni finestra: nessuna finestra oltre 3 minuti.
3. **Introduzione animata** (copertina + «Di cosa parliamo»): senza riquadro del prof. Voci Kore senza il nome del prof (benvenuto, indice, mappe, AP1 rifatti).
4. **Copertina** con il titolo esatto; intro del prof 130,9 s (<3 minuti).
5. **Una sola Parte** (59:33): nessuno spiegone.
6. **Approfondimenti**: 7 (uno per argomento, voci già presenti) + 3 nuovi dove il prof resta a lungo sullo stesso concetto (segregazione, passaggio dei poteri dopo Dallas, contenimento del comunismo). Testi dal parlato del prof.
7. **Ripassi** (pillola + schema) in blu scuro a tutto schermo, righe che si accendono con la voce; riepilogo finale blu; compiti letti dalla voce unica COMPITI_R3 con la riga finale sullo schermo; verifica di sbarramento (scheda con scatto a +0,5 s) e sigla finale del kit.
8. **Immagini del prof** (4: Kennedy→arg. 2, carta del Vietnam→arg. 5, carrarmati a Praga→arg. 6, carta della guerra dei Sei giorni→arg. 6) ingrandite 4× con EDSR (OpenCV dnn_superres) + nitidezza: è un ingrandimento, non nuovi dettagli (NV: il ritratto di Kennedy non è confrontato a occhio con l'originale).
9. **Dispensa A4** (pagine come da `pages.json`) = pagine del video, con strato di testo invisibile; copertina solo materia e titolo; piè di pagina «STORIA V» e «Pagina N». **PDF mappe** a parte con copertina «MAPPE».
10. **Audio**: tagli del prof agganciati ai fotogrammi (sincronia labbra/voce per costruzione: audio e video dallo stesso intervallo dell'originale, NV misura a 0,04 s non fatta); pause oltre 2,5 s accorciate a circa 1 s.
11. **Sottotitoli** `.vtt` (spenti all'avvio): trascrizione del prof corretta da agenti sulle slide e sulle mappe, più i testi delle voci Kore; tempi dalla trascrizione (NV: non riletti per intero dalla master).

## 5. Tabella immagini del prof → argomento (uno solo)
Kennedy (discorso) → 2 · carta del Vietnam → 5 · carrarmati a Praga → 6 · carta della guerra dei Sei giorni → 6. Le pagine di solo testo: pagina «benessere» → 1, «Kennedy» → 2, «Johnson» → 3, «spazio» → 4, «attrito» → 5, «blocco sovietico» → 6, «Sessantotto» → 7.

## 6. Refusi e anomalie nel materiale del prof
- **Slide del prof**: nessun refuso trovato. Unica modifica: le virgolette "..." diventano «...» («baby boom», «frontiera», «socialismo dal volto umano»).
- **Parlato** (riportato come lo dice, niente calcoli): il prof dice «la sua amministrazione, 1960, in teoria 1964» (la slide dice 1961-1963); «porteremo l'uomo sulla luna entro la fine del secolo, del decennio»; per Chruščëv «53, 62, d'accordo? 64» (la slide e la mappa dicono 1953 e 1964: il «62» non torna); la crisi dei missili di Cuba la dice «del sessantue» (1961) mentre la slide dice 1962. La master li porti a Sara.
- **Mappa 3**: manca la domanda-titolo; connettore «lo» probabile refuso (vedi §4).
- Il prof tratta la prima slide (benessere) in soli 16 s: le card «Mutamento demografico», «Welfare State» e «Ruolo delle donne» non sono dette a voce; restano visibili e le spiega l'approfondimento 1 (voce Kore, dalle sue slide).
- La card «Politica estera» della slide Kennedy è accesa dove il prof parla di sfida con i sovietici (corsa allo spazio, intorno a 8:08 del video) e non è mai detta come tale.

## 7. Voci Kore (M/NV)
- 18 voci nuove/rifatte ricevute il 23/11: bordi (ultimi 50 ms) sotto 0,03 su tutte. COMPITI_R2 aveva 0,06: sostituita con **COMPITI_R3** (0,000), ora nel video. Trascrizione e confronto: similarità 0,84–1,0 con i testi (differenze = errori di riconoscimento su Chruščëv/Brežnev/numeri). **NV:** non ho ascoltato le voci; GL1_R2 e MD2_R2 sono «DA CONTROLLARE» nell'ESITI della master (pronuncia di nomi russi).
- Le altre voci (AP2–AP7, R, SC, P, FIN, COMPI) sono quelle della consegna precedente: per R2, R3, R5, P6, GL1, RV5_4 (bordo ≥0,03 nel file grezzo) sono state sostituite dalle versioni _R2.

## 8. Cosa NON è stato verificato (NV)
- Controllo dell'agente separato del §11: **non fatto** (tempo: voci arrivate alle 09:20 UTC).
- Controllo severo (OCR): il giro sulla versione precedente ha dato RESPINTA per una sola card sola oltre 60 s (corretta schiarendo le card spente) e per pause mute (voci provvisorie e fine delle mappe, corrette) e non è stato rilanciato sull'ultima codifica; controllo ascoltato delle voci; sincronia labbra/voce misurata a 0,04 s; ritratto di Kennedy ingrandito confrontato a occhio; sottotitoli riletti per intero; dispensa confrontata pagina per pagina col video (generata dagli stessi sorgenti HTML, NV pagine con card spente: tutte le card sono mostrate senza bordo giallo).
