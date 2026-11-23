# RAPPORTO DI REVISIONE · Storia V · «L'Italia di Giolitti» · correzioni 22/11
Chat di produzione · ramo `revisione-storia-V-lez03` · riparto dalla consegna del 20/11 (video e slide rifatti, voci Kore già esistenti riusate). Ogni dato è etichettato **M** (misurato), **S** (a vista) o **NV** (non verificato).

## 1. Lavoro fatto (prompt correzioni 22/11)
| # | Punto | Esito |
|---|---|---|
| 1 | Mappe del prof | Le 3 mappe del PDF «MAPPE LEZIONE 3» sono ridisegnate nel modello BES (pesca, celeste, paglierino, menta, lilla, legenda in alto a destra, testo 40–44 px), stesse parole e stesse frecce, costruite ramo per ramo con la voce Kore (una voce per ogni riquadro, riquadro acceso in giallo mentre parla, mappa intera ferma 4 s). Mappa 1 (svolta di Giolitti) dopo l'argomento 2; mappa 2 (sviluppo economico) dopo l'argomento 9; mappa 3 («GIOLITTI») dopo l'argomento 11. Tolte tutte le mappe nostre (mappe finali comprese). Gli altri argomenti chiudono con la pillola. La mappa 3 nel PDF del prof non ha la domanda come titolo: ho scritto «Come Giolitti affronta le pressioni dei nazionalisti e l'avanzata dei socialisti?» con parole del prof (come da risposta della master). |
| 2 | Slide del prof | Slide rifatte con testo delle card a 40 px, interlinea 1,5, al massimo 3 card intere (mai «…»), bordo giallo e pallino quando il prof comincia la frase, riquadro 4:3 del prof (412×309 a x=1428, y=148) con fascia gialla. Le slide sono «a finestra»: a ogni cambio di card o di inserto la pagina cambia (Pagina N). Dove il prof resta a lungo su un punto ho messo gli approfondimenti Kore (2 per argomento al massimo). |
| 3 | Introduzione animata | Copertina e «Di cosa parliamo» senza riquadro del prof; il riquadro compare solo quando il prof comincia a parlare (0,35 s prima della prima parola). Il nome del prof non è né detto né scritto nelle animazioni (compare solo nella fascia gialla). |
| 4 | Copertina | Titolo esatto «L'Italia di Giolitti» con l'elenco degli argomenti; introduzione del prof 148,4 s (sotto i 3 minuti), poi «Di cosa parliamo». |
| 5 | Parte 2 | Si apre con lo spiegone: dopo la sigla un ripasso animato con voce Kore della Parte 1, argomento per argomento, con le immagini del prof e la mappa 1 di quella Parte. |
| 6 | Refusi | Corretti nelle nostre slide e nella dispensa: «Sciopero del 1904» → «sciopero del 1904» (titolo p. 5 del PDF); «movimenti femministe» → «movimenti femministi» (p. 11). Anomalie lasciate come le dice il prof: la slide p. 4 scrive «Confederazione Generale del Lavoro (Cgil)» ma il prof dice «CGdL» (la sigla storica del 1906 è CGdL; la Cgil nasce nel 1944); «Ina» scritto con la sola iniziale maiuscola (la slide spiega la sigla); il prof dice «Crispy», «Beccaris» ecc. nel parlato ma le slide hanno l'ortografia giusta. |
| 7 | Audio | Parlato del prof dall'originale con highpass a 80 Hz e riduzione leggera del rumore (afftdn nr 6), nessun altro filtro: timbro misurato più sotto. Pause oltre 2,5 s accorciate a circa 1 s (solo 2 nel parlato). −16 LUFS misurati sulla Parte. La lezione 3 non è tra le 4 e 6 (audio da rifare). |
| 8 | Dispensa e PDF mappe | Dispensa A4 orizzontale per Parte con le stesse slide del video a tutta larghezza e strato di testo invisibile; copertina con sola materia e titolo; piè di pagina «STORIA V · Pagina N» senza nome del prof. PDF delle mappe a parte con copertina identica più «MAPPE». |

## 2. Misure (M)
### Parte 1
```
durata 51:55.0 (3115.03 s) | fotogrammi 93451 (durata×30 = 93451) | peso 368.7 MB | 1920x1080 30/1
loudness -16.1 LUFS | picco vero -1.2 dBTP | pause oltre 2,5 s (< -45 dB): 0
timbre (acuti >4 kHz meno >100 Hz): originale -19.0 dB | finale -18.6 dB (deve stare tra -9 e -20)
scarto del parlato finale rispetto alla sorgente (s), inviluppo su 6 s, atteso 0: D0 +0.000, A1_1 -0.007, A1_2 -0.007, A1_3 +0.000, A2_1 -0.010, A2_2 +0.003, A3_1 +0.017, A3_2 +0.003, A4_1 +0.003, A4_2 +0.013, A5_1 +0.007, A5_2 -0.010
Q: scheda e scatto atteso:
  Q1 atteso 1356.100 trovato 1356.100 scarto +0.000
  Q2 atteso 1771.600 trovato 1771.600 scarto +0.000
  Q3 atteso 2150.467 trovato 2150.467 scarto -0.000
  Q4 atteso 2480.133 trovato 2480.133 scarto +0.000
  Q5 atteso 3007.500 trovato 3007.500 scarto +0.000
```
`controllo_severo.py` della master: **ESITO RESPINTA** (slide con lo stesso titolo oltre 3 min: 0; schermate identiche oltre 3 min: 0; card con «…»: 0; card con iniziale minuscola: 0; copertina titolo esatto presente).

### Parte 2
```
durata 53:31.4 (3211.40 s) | fotogrammi 96342 (durata×30 = 96342) | peso 378.4 MB | 1920x1080 30/1
loudness -16.2 LUFS | picco vero -1.9 dBTP | pause oltre 2,5 s (< -45 dB): 0
timbre (acuti >4 kHz meno >100 Hz): originale -19.6 dB | finale -19.2 dB (deve stare tra -9 e -20)
scarto del parlato finale rispetto alla sorgente (s), inviluppo su 6 s, atteso 0: A6_1 +0.013, A6_2 -0.003, A7_1 +0.010, A7_2 -0.003, A8_1 -0.003, A8_2 -0.007, A8_3 +0.013, A9_1 +0.010, A9_2 +0.010, A10_1 +0.010, A10_2 -0.010, A10_3 -0.013, A11_1 -0.017, A11_2 +0.010
Q: scheda e scatto atteso:
  Q6 atteso 755.700 trovato 755.700 scarto +0.000
  Q7 atteso 1004.467 trovato 1004.467 scarto -0.000
  Q8 atteso 1551.900 trovato 1551.900 scarto +0.000
  Q9 atteso 2056.500 trovato 2056.500 scarto +0.000
  Q10 atteso 2572.400 trovato 2572.400 scarto +0.000
  Q11 atteso 3040.500 trovato 3040.500 scarto +0.000
  VF atteso 3142.533 trovato 3142.533 scarto +0.000
```
`controllo_severo.py` della master: **ESITO OK** (slide con lo stesso titolo oltre 3 min: 0; schermate identiche oltre 3 min: 0; card con «…»: 0; card con iniziale minuscola: 0; copertina titolo esatto presente).

Formato: 1920×1080, 30 fps, x264 veryfast **CRF 20** (a CRF 19 la Parte 2 usciva a 403,7 MB, oltre i 400), AAC 192 kbps 48 kHz, una sola codifica per ogni fotogramma (clip per pezzo e dissolvenze, poi unione senza ricodifica).

## 3. Tabella dei tagli del prof (fine di ogni pezzo, M)
**Parte 1**
| pezzo | minuto fine | ultime parole (trascrizione) | frase finita |
|---|---|---|---|
| D0 | 2:56.1 | …nel dettaglio, bene? | sì |
| A1_1 | 7:14.2 | …soprattutto più che altro vendicare l'onore di Doga. | sì |
| A1_2 | 13:36.9 | …Beccaris costerà in realtà al re Umberto I. | sì |
| A1_3 | 21:39.2 | …il ritratto fotografico di Giovanni Giolitti a destra. | sì |
| A2_1 | 25:11.4 | …agire come mediatore neutrale tra le parti sociali. | sì |
| A2_2 | 27:16.8 | …conciliano con le tempistiche della politica parlamentari, banalmente. | sì |
| A3_1 | 30:54.8 | …immediata. | sì |
| A3_2 | 34:23.0 | …questo è il ritratto, insomma, è Filippo Turati. | sì |
| A4_1 | 37:06.6 | …che possono invece partecipare alla vita politica italiana. | sì |
| A4_2 | 39:51.8 | …si forma già, diciamo, il pensiero politico cattolico. | sì |
| A5_1 | 43:48.2 | …dell'importanza fondamentale che esercita. Questo è il concetto. | sì |
| A5_2 | 48:29.2 | …il paese, d'accordo? Quindi è tutto sotto giolitti. | sì |

**Parte 2**
| pezzo | minuto fine | ultime parole (trascrizione) | frase finita |
|---|---|---|---|
| A6_1 | 5:24.0 | …ha compiuto i trent'anni puoi votare lo stesso. | sì |
| A6_2 | 11:11.6 | …dei liberali. | sì |
| A7_1 | 13:37.7 | …le borghesi favorevoli al voto su base censitaria. | sì |
| A7_2 | 15:29.3 | …discriminazione, in base al sesso al genere sessuale. | sì |
| A8_1 | 20:21.4 | …settore meccanico ed elettrico. Nel 1899 a Torino. | sì |
| A8_2 | 22:54.8 | …particolare, diventa veramente la locomotiva, già lo era. | sì |
| A8_3 | 25:08.4 | …municipalizzazione dei servizi di acqua, gas e trasporti. | sì |
| A9_1 | 27:38.4 | …le cause profonde del divario. Anche per questo. | sì |
| A9_2 | 32:08.8 | …altri punti del mondo. | sì |
| A10_1 | 36:23.3 | …quello che in Madre Patria e cedeva anche. | sì |
| A10_2 | 38:56.4 | …che si muova anche lei in termini coloniali. | sì |
| A10_3 | 42:05.9 | …più là della gamba. | sì |
| A11_1 | 44:10.5 | …non faceva parte dallo statuto del partito socialista. | sì |
| A11_2 | 48:39.1 | …Noi dovremmo vedere. | sì |

Ogni pezzo comincia e finisce su una frase intera della trascrizione (VAD + testo); i tagli cadono nelle pause (≥ 0,4 s), con 0,12 s di margine prima della frase che segue; le dissolvenze (0,3–0,5 s) cadono solo nel silenzio (voce del prof azzerata nei bordi, 30 ms di sfumatura). «Frase finita: sì» = la trascrizione del pezzo termina con punto finale. Il giudizio «frase di senso compiuto» è mio, non riascoltato a orecchio (NV).

## 4. Sincronia delle card (10 punti, M) e immagini del prof
| Parte | Minuto video | Arg. | Card accesa | Frase del prof che comincia |
|---|---|---|---|---|
| 1 | 35:59.00 | 4 | «Il superamento del Non expedit: si assiste a un gr…» | «Urge parlare di questi cattolici?…» (1610.7 s dell'originale) |
| 1 | 41:55.69 | 5 | «La tutela dei più deboli: vengono varate nuove leg…» | «la tutela dei più deboli.…» (1814.1 s dell'originale) |
| 1 | 38:55.95 | 4 | «La pratica del trasformismo: per mantenere la stab…» | «chiaramente si avvicinano a quella classe liberale di destra e di sini…» (1730.6 s dell'originale) |
| 1 | 42:05.79 | 5 | «Nuovi diritti assistenziali: lo Stato introduce l'…» | «Nuovi diritti assistenziali, lo Stato introduce l'obbligo del riposo s…» (1824.2 s dell'originale) |
| 1 | 22:45.91 | 2 | «Il nuovo ruolo dello Stato: Giovanni Giolitti assu…» | «Giovanni Giolitti diventa, giusto per seguire un filo.…» (1148.9 s dell'originale) |
| 2 | 13:20.92 | 7 | «I primi movimenti femministi: figure come Anna Kul…» | «Figure come Anna Kulisov, russa e vicina al partito socialista italian…» (2652.0 s dell'originale) |
| 2 | 46:00.39 | 11 | «La fine dell'equilibrio giolittiano: nonostante la…» | «l'opposizione dei nazionalisti e della sinistra radicale…» (3959.5 s dell'originale) |
| 2 | 29:49.92 | 9 | «Il grande esodo: tra il 1901 e il 1915 circa 9 mil…» | «E da qui capiamo perché il grande esodo tra il 1901 e il 1915 circa 9 …» (3336.6 s dell'originale) |
| 2 | 28:25.62 | 9 | «L'accusa di clientelismo: gli intellettuali meridi…» | «Salvemini, Gatano Salvemini fu uno storico, ma fu anche un parlamentar…» (3252.3 s dell'originale) |
| 2 | 38:38.31 | 10 | «La retorica pascoliana: la propaganda ufficiale su…» | «In senso stretto e da intellettuali come Giovanni Pascoli, addirittura…» (3678.8 s dell'originale) |

| Immagine del prof (pagina PDF) | Argomento in cui compare (uno solo) |
|---|---|
| Il regicidio di Monza (p. 3) | 1 · La crisi di fine secolo e la svolta liberale |
| Giovanni Giolitti (p. 3) | 2 · La nuova linea politica di Giolitti |
| Filippo Turati (p. 6) | 3 · I rapporti con i socialisti e lo sciopero del 1904 |
| Romolo Murri (p. 8) | 4 · Il rapporto con i cattolici e il trasformismo |
| I flussi migratori italiani (p. 14) | 9 · Il divario Nord-Sud e l'emigrazione |
| La guerra di Libia (1911-1912) (p. 16) | 10 · La politica coloniale e la guerra in Libia |

La card si accende all'attacco della frase scelta (scarto 0,0 s sul tempo della frase; la dissolvenza del bordo dura 0,25 s). Che la frase scelta sia davvero quella della card l'ho deciso leggendo la trascrizione: nei punti in cui il prof non nomina la card (es. arg. 4 «trasformismo», arg. 11 «fine dell'equilibrio giolittiano») ho agganciato la frase più vicina (NV).

## 5. Pezzi e tempi (M)
**Parte 1**

| Pezzo | Inizio | Durata |
|---|---|---|
| `SIGLA` | 0:00.00 | 15.0 s |
| `COVERV` | 0:14.50 | 12.6 s |
| `D0` | 0:26.63 | 149.5 s |
| `DIC` | 2:55.77 | 24.4 s |
| `T1` | 3:19.63 | 4.4 s |
| `A1_1` | 3:23.70 | 230.5 s |
| `AN1` | 7:13.67 | 54.9 s |
| `A1_2` | 8:08.07 | 328.8 s |
| `AN2` | 13:36.40 | 44.2 s |
| `A1_3` | 14:20.07 | 439.1 s |
| `PI1` | 21:38.70 | 11.4 s |
| `PS1` | 21:49.60 | 46.0 s |
| `Q1` | 22:35.60 | 5.5 s |
| `T2` | 22:40.10 | 4.4 s |
| `A2_1` | 22:44.00 | 147.4 s |
| `AN3` | 25:10.93 | 48.3 s |
| `A2_2` | 25:58.73 | 78.0 s |
| `AN4` | 27:16.27 | 53.9 s |
| `MAP1` | 28:09.67 | 43.8 s |
| `PI2` | 28:52.93 | 12.6 s |
| `PS2` | 29:05.03 | 26.1 s |
| `Q2` | 29:31.10 | 5.5 s |
| `T3` | 29:35.60 | 4.4 s |
| `A3_1` | 29:39.50 | 75.3 s |
| `AN5` | 30:54.33 | 45.5 s |
| `A3_2` | 31:39.30 | 163.7 s |
| `AN6` | 34:22.50 | 48.5 s |
| `PI3` | 35:10.47 | 12.4 s |
| `PS3` | 35:22.33 | 27.6 s |
| `Q3` | 35:49.97 | 5.5 s |
| `T4` | 35:54.47 | 4.4 s |
| `A4_1` | 35:58.37 | 68.3 s |
| `AN7` | 37:06.17 | 57.6 s |
| `A4_2` | 38:03.33 | 108.5 s |
| `AN8` | 39:51.33 | 47.5 s |
| `PI4` | 40:38.37 | 11.8 s |
| `PS4` | 40:49.70 | 29.9 s |
| `Q4` | 41:19.63 | 5.5 s |
| `T5` | 41:24.13 | 4.4 s |
| `A5_1` | 41:28.03 | 140.1 s |
| `AN9` | 43:47.67 | 53.1 s |
| `A5_2` | 44:40.27 | 228.9 s |
| `AN10` | 48:28.83 | 52.7 s |
| `PI5` | 49:21.07 | 12.7 s |
| `PS5` | 49:33.23 | 33.8 s |
| `Q5` | 50:07.00 | 5.5 s |
| `GL` | 50:11.50 | 51.2 s |
| `RIEP` | 51:02.17 | 31.1 s |
| `FIN` | 51:32.77 | 17.8 s |
| `FINALE` | 51:50.03 | 5.0 s |

**Parte 2**

| Pezzo | Inizio | Durata |
|---|---|---|
| `SIGLA` | 0:00.00 | 15.0 s |
| `SPIEGONE` | 0:14.50 | 121.6 s |
| `DIC` | 2:15.63 | 26.3 s |
| `T6` | 2:41.47 | 4.4 s |
| `A6_1` | 2:45.53 | 158.5 s |
| `AN11` | 5:23.50 | 46.5 s |
| `A6_2` | 6:09.53 | 302.0 s |
| `AN12` | 11:11.10 | 44.0 s |
| `PI6` | 11:54.57 | 11.8 s |
| `PS6` | 12:05.83 | 29.4 s |
| `Q6` | 12:35.20 | 5.5 s |
| `T7` | 12:39.70 | 4.4 s |
| `A7_1` | 12:43.63 | 54.0 s |
| `AN13` | 13:37.17 | 28.9 s |
| `A7_2` | 14:05.53 | 83.8 s |
| `AN14` | 15:28.80 | 38.2 s |
| `PI7` | 16:06.53 | 11.1 s |
| `PS7` | 16:17.10 | 26.9 s |
| `Q7` | 16:43.97 | 5.5 s |
| `T8` | 16:48.47 | 4.4 s |
| `A8_1` | 16:52.37 | 209.0 s |
| `AN16` | 20:20.87 | 47.4 s |
| `A8_2` | 21:07.77 | 107.1 s |
| `AN15` | 22:54.40 | 50.2 s |
| `A8_3` | 23:44.17 | 84.2 s |
| `PI8` | 25:07.87 | 12.3 s |
| `PS8` | 25:19.70 | 31.7 s |
| `Q8` | 25:51.40 | 5.5 s |
| `T9` | 25:55.90 | 4.4 s |
| `A9_1` | 25:59.80 | 98.6 s |
| `AN17` | 27:37.87 | 47.6 s |
| `A9_2` | 28:24.93 | 223.8 s |
| `AN18` | 32:08.27 | 45.4 s |
| `MAP2` | 32:53.17 | 36.3 s |
| `PI9` | 33:28.97 | 11.3 s |
| `PS9` | 33:39.80 | 36.2 s |
| `Q9` | 34:16.00 | 5.5 s |
| `T10` | 34:20.50 | 4.4 s |
| `A10_1` | 34:24.40 | 118.9 s |
| `AN19` | 36:22.77 | 52.8 s |
| `A10_2` | 37:15.10 | 101.3 s |
| `AN20` | 38:55.93 | 50.3 s |
| `A10_3` | 39:45.73 | 140.2 s |
| `PI10` | 42:05.43 | 11.1 s |
| `PS10` | 42:16.07 | 35.8 s |
| `Q10` | 42:51.90 | 5.5 s |
| `T11` | 42:56.40 | 4.4 s |
| `A11_1` | 43:00.30 | 70.2 s |
| `AN21` | 44:10.00 | 57.7 s |
| `A11_2` | 45:07.20 | 211.9 s |
| `AN22` | 48:38.60 | 35.6 s |
| `MAP3` | 49:13.67 | 43.9 s |
| `PI11` | 49:57.03 | 13.1 s |
| `PS11` | 50:09.60 | 30.4 s |
| `Q11` | 50:40.00 | 5.5 s |
| `GL` | 50:44.50 | 48.6 s |
| `RIEP` | 51:32.63 | 41.5 s |
| `FIN` | 52:13.67 | 8.4 s |
| `VF` | 52:22.03 | 5.5 s |
| `FINALE` | 52:26.53 | 5.0 s |
| `COMPITI_I` | 52:31.03 | 3.9 s |
| `COMPITI` | 52:34.43 | 57.0 s |

## 6. Voci
- **Voci Kore vere (già generate dalla master e riusate):** approfondimenti AN1–AN22 (AN1 accorciata a fine frase: 53,1 s invece di 68 s, per restare entro 60 s), ripassi R1–R5, pillole PIL1–PIL11, schemi PS, glossari GL1–2, ripassi finali RF1–2, FIN1–2.
- **Voci nuove, ora vere Kore (ricevute dalla master il 22/11 sera) e montate:** BEN_R2, SPG_0, DIC_1, DIC_2, MP1_1–7, MP2_1–6, MP3_1–7, CMP_1. Controllate (M): trascrizione confrontata col testo (numeri compresi) con concordanza 0,86–1,00 (le 3 sotto 0,95 differiscono solo per «Giolitti»/«imprime» scritti diversamente dal riconoscitore), ampiezza negli ultimi 50 ms e nei primi sotto 0,03 su tutte, nessuna troncata. Pronuncia dei nomi non riascoltata a orecchio (NV). Elenco in `check_voci.txt` non incluso: vedi sopra.
- **Voci rimaste da rifare (testo con la sigla spiegata):** AN21 (PSI), R5 (INA), AN16 e R8 (Fiat): a voce la sigla non è spiegata, sullo schermo sì. Chiesto alla master.
- Il testo delle voci nuove usa solo parole del prof; nessuna voce o scheda nomina il prof (c'è solo la fascia gialla). Alcuni approfondimenti AN dicono «il docente» (non il nome).

## 7. Cose che non tornano / limiti / NON verificato
- **Il prof esce molto dalle slide** (parla 69 minuti con 11 pagine): ho agganciato le card alle frasi in cui introduce l'argomento. I punti incerti sono elencati al §4.
- Sottotitoli: generati dalla trascrizione automatica del prof con correzione dei nomi propri (Giolitti, Crispi, Bava Beccaris, Zanardelli, Kuliscioff, Salvemini…); **non riletti per intero** (NV); possono restare errori del riconoscimento. Le voci Kore sono nei sottotitoli con il testo vero.
- Webcam: il prof è 184×138 nell'originale, ingrandita 2,2× nel riquadro 4:3 (morbida, come nelle altre lezioni); testa vicina al bordo alto già nell'originale.
- Immagini del prof: sono piccole (da 193×454 a 777×497); migliorate con riduzione del rumore, ingrandimento ×4 (EDSR) e nitidezza, senza cambiare i tratti. L'infografica dei flussi migratori e la carta della Libia restano poco leggibili nei dettagli minuti (la risoluzione dell'originale non lo permette).
- Non esiste una «mappa finale della lezione» del prof: non l'ho inventata (le 3 mappe del prof sono nel video). Dopo gli argomenti senza mappa c'è solo la pillola.
- Durata: P1 51:55, P2 53:31 (50–60 min).
- Il parlato del prof è stato ripulito solo con highpass 80 Hz e riduzione rumore leggera: nessun altro filtro (lezione non tra quelle da rifare).
- Dispensa: stesse slide del video senza riquadro del prof e senza fascia con il nome; strato di testo invisibile con il testo di ogni card. Mappe in PDF a parte con copertina «MAPPE».
- Quiz (5 domande per argomento), verifica finale (xlsx del prof) e compiti sono quelli della consegna del 20/11 (JSON in questa cartella): non rivisti da me (NV).
## 8. Controllo dell'agente separato (22/11) e correzioni
Un agente che non ha montato la lezione ha controllato la lista del §11. Difetti trovati e ESITO: bordi del parlato attenuati (corretto: margini più larghi, nessuna sfumatura dentro le parole); sigle non spiegate sullo schermo (corretto: PSI, INA, Fiat spiegate nelle card degli approfondimenti e nelle parole chiave); mappa ferma 3,5 s (corretto: 4,5 s); mini-mappa illeggibile nello spiegone (corretto: a tutto schermo); dispensa senza pillole, glossario, ripasso, compiti (corretto: aggiunti); numero di lezione nella scheda (tolto); voci obsolete in testi_voci.json con il nome del prof (tolte); termini sbagliati nei sottotitoli (corretti Dogali, Giolitti, Falck, Salvemini…).
**Residui, da decidere alla master:** le voci Kore AN21 (PSI), R5 (INA), AN16 e R8 (Fiat) dicono la sigla senza spiegarla (la spiegazione c'è solo sullo schermo): servono testi nuovi; l'avviso dei diritti della sigla finale del kit resta visibile ~3 s; qualche bordo giallo in ritardo di 1–2 s dove il prof anticipa il tema (Parte 1 a ~11:31 e ~18:49); A9_1 e A10_1 finiscono su una frase chiusa ma sintatticamente aperta.
## 9. Correzioni dopo il controllo della master (23/11)
- **Schede RIPASSO** ora in blu scuro a tutto schermo, righe che si accendono con la voce (finestra scorrevole se le righe non entrano). Prima erano bianche.
- **Infografica dei flussi migratori** (Parte 2, arg. 9): grande, a tutta altezza, alla massima risoluzione del file del prof (pdfimages -all, ingrandita ×4 con EDSR); intera, poi ingrandita a zone (testi e barre, poi la carta) mentre il prof ne parla.
- `controllo_rapido.py`: ESITO OK su entrambe le Parti; foglio dei fotogrammi e json in `controllo_rapido/`. `controllo_severo.py`: OK sulla Parte 2; sulla Parte 1 segnala «…» in un campione (22:25): è un falso positivo dell'OCR (la scheda di ripasso a 22:25 verificata a vista: nessun «…»).