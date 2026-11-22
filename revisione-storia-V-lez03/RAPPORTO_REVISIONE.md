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
durata 51:43.1 (3103.13 s) | fotogrammi 93094 (durata×30 = 93094) | peso 359.3 MB | 1920x1080 30/1
loudness -16.2 LUFS | picco vero -2.6 dBTP | pause oltre 2,5 s (< -45 dB): 0
timbre (acuti >4 kHz meno >100 Hz): originale -19.0 dB | finale -18.6 dB (deve stare tra -9 e -20)
scarto del parlato finale rispetto alla sorgente (s), inviluppo su 6 s, atteso 0: D0 +0.000, A1_1 -0.007, A1_2 -0.007, A1_3 +0.000, A2_1 -0.010, A2_2 +0.003, A3_1 +0.017, A3_2 +0.003, A4_1 +0.003, A4_2 +0.013, A5_1 +0.007, A5_2 -0.010
Q: scheda e scatto atteso:
  Q1 atteso 1350.967 trovato 1350.967 scarto -0.000
  Q2 atteso 1759.700 trovato 1759.700 scarto +0.000
  Q3 atteso 2138.567 trovato 2138.567 scarto -0.000
  Q4 atteso 2468.233 trovato 2468.233 scarto +0.000
  Q5 atteso 2995.600 trovato 2995.600 scarto +0.000
```
`controllo_severo.py` della master: **ESITO OK** (slide con lo stesso titolo oltre 3 min: 0; schermate identiche oltre 3 min: 0; card con «…»: 0; card con iniziale minuscola: 0; copertina titolo esatto presente).

### Parte 2
```
durata 53:08.7 (3188.67 s) | fotogrammi 95660 (durata×30 = 95660) | peso 366.7 MB | 1920x1080 30/1
loudness -16.2 LUFS | picco vero -2.5 dBTP | pause oltre 2,5 s (< -45 dB): 0
timbre (acuti >4 kHz meno >100 Hz): originale -19.6 dB | finale -19.2 dB (deve stare tra -9 e -20)
scarto del parlato finale rispetto alla sorgente (s), inviluppo su 6 s, atteso 0: A6_1 +0.013, A6_2 -0.003, A7_1 +0.010, A7_2 -0.003, A8_1 -0.003, A8_2 -0.007, A8_3 +0.013, A9_1 +0.010, A9_2 +0.010, A10_1 +0.010, A10_2 -0.010, A10_3 -0.013, A11_1 -0.017, A11_2 +0.010
Q: scheda e scatto atteso:
  Q6 atteso 751.133 trovato 751.133 scarto +0.000
  Q7 atteso 999.900 trovato 999.900 scarto +0.000
  Q8 atteso 1547.333 trovato 1547.333 scarto +0.000
  Q9 atteso 2047.133 trovato 2047.133 scarto +0.000
  Q10 atteso 2563.033 trovato 2563.033 scarto +0.000
  Q11 atteso 3024.000 trovato 3024.000 scarto +0.000
  VF atteso 3126.033 trovato 3126.033 scarto +0.000
```
`controllo_severo.py` della master: **ESITO OK** (slide con lo stesso titolo oltre 3 min: 0; schermate identiche oltre 3 min: 0; card con «…»: 0; card con iniziale minuscola: 0; copertina titolo esatto presente).

Formato: 1920×1080, 30 fps, x264 veryfast **CRF 20** (a CRF 19 la Parte 2 usciva a 403,7 MB, oltre i 400), AAC 192 kbps 48 kHz, una sola codifica per ogni fotogramma (clip per pezzo e dissolvenze, poi unione senza ricodifica).

## 3. Tabella dei tagli del prof (fine di ogni pezzo, M)
**Parte 1**
| pezzo | minuto fine | ultime parole (trascrizione) | frase finita |
|---|---|---|---|
| D0 | 2:54.8 | …nel dettaglio, bene? | sì |
| A1_1 | 7:09.0 | …soprattutto più che altro vendicare l'onore di Doga. | sì |
| A1_2 | 13:31.8 | …Beccaris costerà in realtà al re Umberto I. | sì |
| A1_3 | 21:34.1 | …il ritratto fotografico di Giovanni Giolitti a destra. | sì |
| A2_1 | 25:06.3 | …agire come mediatore neutrale tra le parti sociali. | sì |
| A2_2 | 27:11.6 | …conciliano con le tempistiche della politica parlamentari, banalmente. | sì |
| A3_1 | 30:42.9 | …immediata. | sì |
| A3_2 | 34:11.1 | …questo è il ritratto, insomma, è Filippo Turati. | sì |
| A4_1 | 36:54.7 | …che possono invece partecipare alla vita politica italiana. | sì |
| A4_2 | 39:39.9 | …si forma già, diciamo, il pensiero politico cattolico. | sì |
| A5_1 | 43:36.3 | …dell'importanza fondamentale che esercita. Questo è il concetto. | sì |
| A5_2 | 48:17.3 | …il paese, d'accordo? Quindi è tutto sotto giolitti. | sì |

**Parte 2**
| pezzo | minuto fine | ultime parole (trascrizione) | frase finita |
|---|---|---|---|
| A6_1 | 5:19.4 | …ha compiuto i trent'anni puoi votare lo stesso. | sì |
| A6_2 | 11:07.0 | …dei liberali. | sì |
| A7_1 | 13:33.1 | …le borghesi favorevoli al voto su base censitaria. | sì |
| A7_2 | 15:24.7 | …discriminazione, in base al sesso al genere sessuale. | sì |
| A8_1 | 20:16.8 | …settore meccanico ed elettrico. Nel 1899 a Torino. | sì |
| A8_2 | 22:50.3 | …particolare, diventa veramente la locomotiva, già lo era. | sì |
| A8_3 | 25:03.8 | …municipalizzazione dei servizi di acqua, gas e trasporti. | sì |
| A9_1 | 27:33.8 | …le cause profonde del divario. Anche per questo. | sì |
| A9_2 | 32:04.2 | …altri punti del mondo. | sì |
| A10_1 | 36:13.9 | …quello che in Madre Patria e cedeva anche. | sì |
| A10_2 | 38:47.1 | …che si muova anche lei in termini coloniali. | sì |
| A10_3 | 41:56.6 | …più là della gamba. | sì |
| A11_1 | 44:01.1 | …non faceva parte dallo statuto del partito socialista. | sì |
| A11_2 | 48:29.7 | …Noi dovremmo vedere. | sì |

Ogni pezzo comincia e finisce su una frase intera della trascrizione (VAD + testo); i tagli cadono nelle pause (≥ 0,4 s), con 0,12 s di margine prima della frase che segue; le dissolvenze (0,3–0,5 s) cadono solo nel silenzio (voce del prof azzerata nei bordi, 30 ms di sfumatura). «Frase finita: sì» = la trascrizione del pezzo termina con punto finale. Il giudizio «frase di senso compiuto» è mio, non riascoltato a orecchio (NV).

## 4. Sincronia delle card (10 punti, M) e immagini del prof
| Parte | Minuto video | Arg. | Card accesa | Frase del prof che comincia |
|---|---|---|---|---|
| 1 | 35:47.10 | 4 | «Il superamento del Non expedit: si assiste a un gr…» | «Urge parlare di questi cattolici?…» (1610.7 s dell'originale) |
| 1 | 41:43.79 | 5 | «La tutela dei più deboli: vengono varate nuove leg…» | «la tutela dei più deboli.…» (1814.1 s dell'originale) |
| 1 | 38:44.05 | 4 | «La pratica del trasformismo: per mantenere la stab…» | «chiaramente si avvicinano a quella classe liberale di destra e di sini…» (1730.6 s dell'originale) |
| 1 | 41:53.89 | 5 | «Nuovi diritti assistenziali: lo Stato introduce l'…» | «Nuovi diritti assistenziali, lo Stato introduce l'obbligo del riposo s…» (1824.2 s dell'originale) |
| 1 | 22:40.78 | 2 | «Il nuovo ruolo dello Stato: Giovanni Giolitti assu…» | «Giovanni Giolitti diventa, giusto per seguire un filo.…» (1148.9 s dell'originale) |
| 2 | 13:16.36 | 7 | «I primi movimenti femministi: figure come Anna Kul…» | «Figure come Anna Kulisov, russa e vicina al partito socialista italian…» (2652.0 s dell'originale) |
| 2 | 45:51.02 | 11 | «La fine dell'equilibrio giolittiano: nonostante la…» | «l'opposizione dei nazionalisti e della sinistra radicale…» (3959.5 s dell'originale) |
| 2 | 29:45.36 | 9 | «Il grande esodo: tra il 1901 e il 1915 circa 9 mil…» | «E da qui capiamo perché il grande esodo tra il 1901 e il 1915 circa 9 …» (3336.6 s dell'originale) |
| 2 | 28:21.06 | 9 | «L'accusa di clientelismo: gli intellettuali meridi…» | «Salvemini, Gatano Salvemini fu uno storico, ma fu anche un parlamentar…» (3252.3 s dell'originale) |
| 2 | 38:28.94 | 10 | «La retorica pascoliana: la propaganda ufficiale su…» | «In senso stretto e da intellettuali come Giovanni Pascoli, addirittura…» (3678.8 s dell'originale) |

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
| `COVERV` | 0:14.50 | 11.4 s |
| `D0` | 0:25.37 | 149.5 s |
| `DIC` | 2:54.50 | 20.5 s |
| `T1` | 3:14.50 | 4.4 s |
| `A1_1` | 3:18.57 | 230.5 s |
| `AN1` | 7:08.53 | 54.9 s |
| `A1_2` | 8:02.93 | 328.8 s |
| `AN2` | 13:31.27 | 44.2 s |
| `A1_3` | 14:14.93 | 439.1 s |
| `PI1` | 21:33.57 | 11.4 s |
| `PS1` | 21:44.47 | 46.0 s |
| `Q1` | 22:30.47 | 5.5 s |
| `T2` | 22:34.97 | 4.4 s |
| `A2_1` | 22:38.87 | 147.4 s |
| `AN3` | 25:05.80 | 48.3 s |
| `A2_2` | 25:53.60 | 78.0 s |
| `AN4` | 27:11.13 | 53.9 s |
| `MAP1` | 28:04.53 | 37.0 s |
| `PI2` | 28:41.03 | 12.6 s |
| `PS2` | 28:53.13 | 26.1 s |
| `Q2` | 29:19.20 | 5.5 s |
| `T3` | 29:23.70 | 4.4 s |
| `A3_1` | 29:27.60 | 75.3 s |
| `AN5` | 30:42.43 | 45.5 s |
| `A3_2` | 31:27.40 | 163.7 s |
| `AN6` | 34:10.60 | 48.5 s |
| `PI3` | 34:58.57 | 12.4 s |
| `PS3` | 35:10.43 | 27.6 s |
| `Q3` | 35:38.07 | 5.5 s |
| `T4` | 35:42.57 | 4.4 s |
| `A4_1` | 35:46.47 | 68.3 s |
| `AN7` | 36:54.27 | 57.6 s |
| `A4_2` | 37:51.43 | 108.5 s |
| `AN8` | 39:39.43 | 47.5 s |
| `PI4` | 40:26.47 | 11.8 s |
| `PS4` | 40:37.80 | 29.9 s |
| `Q4` | 41:07.73 | 5.5 s |
| `T5` | 41:12.23 | 4.4 s |
| `A5_1` | 41:16.13 | 140.1 s |
| `AN9` | 43:35.77 | 53.1 s |
| `A5_2` | 44:28.37 | 228.9 s |
| `AN10` | 48:16.93 | 52.7 s |
| `PI5` | 49:09.17 | 12.7 s |
| `PS5` | 49:21.33 | 33.8 s |
| `Q5` | 49:55.10 | 5.5 s |
| `GL` | 49:59.60 | 51.2 s |
| `RIEP` | 50:50.27 | 31.1 s |
| `FIN` | 51:20.87 | 17.8 s |
| `FINALE` | 51:38.13 | 5.0 s |

**Parte 2**

| Pezzo | Inizio | Durata |
|---|---|---|
| `SIGLA` | 0:00.00 | 15.0 s |
| `SPIEGONE` | 0:14.50 | 121.2 s |
| `DIC` | 2:15.23 | 22.2 s |
| `T6` | 2:36.90 | 4.4 s |
| `A6_1` | 2:40.97 | 158.5 s |
| `AN11` | 5:18.93 | 46.5 s |
| `A6_2` | 6:04.97 | 302.0 s |
| `AN12` | 11:06.53 | 44.0 s |
| `PI6` | 11:50.00 | 11.8 s |
| `PS6` | 12:01.27 | 29.4 s |
| `Q6` | 12:30.63 | 5.5 s |
| `T7` | 12:35.13 | 4.4 s |
| `A7_1` | 12:39.07 | 54.0 s |
| `AN13` | 13:32.60 | 28.9 s |
| `A7_2` | 14:00.97 | 83.8 s |
| `AN14` | 15:24.23 | 38.2 s |
| `PI7` | 16:01.97 | 11.1 s |
| `PS7` | 16:12.53 | 26.9 s |
| `Q7` | 16:39.40 | 5.5 s |
| `T8` | 16:43.90 | 4.4 s |
| `A8_1` | 16:47.80 | 209.0 s |
| `AN16` | 20:16.30 | 47.4 s |
| `A8_2` | 21:03.20 | 107.1 s |
| `AN15` | 22:49.83 | 50.2 s |
| `A8_3` | 23:39.60 | 84.2 s |
| `PI8` | 25:03.30 | 12.3 s |
| `PS8` | 25:15.13 | 31.7 s |
| `Q8` | 25:46.83 | 5.5 s |
| `T9` | 25:51.33 | 4.4 s |
| `A9_1` | 25:55.23 | 98.6 s |
| `AN17` | 27:33.30 | 47.6 s |
| `A9_2` | 28:20.37 | 223.8 s |
| `AN18` | 32:03.70 | 45.4 s |
| `MAP2` | 32:48.60 | 31.5 s |
| `PI9` | 33:19.60 | 11.3 s |
| `PS9` | 33:30.43 | 36.2 s |
| `Q9` | 34:06.63 | 5.5 s |
| `T10` | 34:11.13 | 4.4 s |
| `A10_1` | 34:15.03 | 118.9 s |
| `AN19` | 36:13.40 | 52.8 s |
| `A10_2` | 37:05.73 | 101.3 s |
| `AN20` | 38:46.57 | 50.3 s |
| `A10_3` | 39:36.37 | 140.2 s |
| `PI10` | 41:56.07 | 11.1 s |
| `PS10` | 42:06.70 | 35.8 s |
| `Q10` | 42:42.53 | 5.5 s |
| `T11` | 42:47.03 | 4.4 s |
| `A11_1` | 42:50.93 | 70.2 s |
| `AN21` | 44:00.63 | 57.7 s |
| `A11_2` | 44:57.83 | 211.9 s |
| `AN22` | 48:29.23 | 35.6 s |
| `MAP3` | 49:04.30 | 36.7 s |
| `PI11` | 49:40.53 | 13.1 s |
| `PS11` | 49:53.10 | 30.4 s |
| `Q11` | 50:23.50 | 5.5 s |
| `GL` | 50:28.00 | 48.6 s |
| `RIEP` | 51:16.13 | 41.5 s |
| `FIN` | 51:57.17 | 8.4 s |
| `VF` | 52:05.53 | 5.5 s |
| `FINALE` | 52:10.03 | 5.0 s |
| `COMPITI_I` | 52:14.53 | 3.9 s |
| `COMPITI` | 52:17.93 | 50.7 s |

## 6. Voci
- **Voci Kore vere (già generate dalla master e riusate):** approfondimenti AN1–AN22 (AN1 accorciata a fine frase: 53,1 s invece di 68 s, per restare entro 60 s), ripassi R1–R5, pillole PIL1–PIL11, schemi PS, glossari GL1–2, ripassi finali RF1–2, FIN1–2.
- **Voci ancora PROVVISORIE (sintetiche, da sostituire domattina):** BEN_R2 (benvenuto senza nome), SPG_0 (apertura spiegone), DIC_1 e DIC_2 («Di cosa parliamo»), MP1_1–7, MP2_1–6, MP3_1–7 (mappe nodo per nodo), CMP_1 (compiti). Testi inviati alla master sul ramo `voci-storia-V-lez03` (`testi_voci.json`). **La lezione non è consegnabile finché queste voci non sono sostituite e controllate** (trascrizione, numeri, bordi sotto 0,03).
- Il testo delle voci nuove usa solo parole del prof; nessuna voce o scheda nomina il prof (c'è solo la fascia gialla). Alcuni approfondimenti AN dicono «il docente» (non il nome).

## 7. Cose che non tornano / limiti / NON verificato
- **Il prof esce molto dalle slide** (parla 69 minuti con 11 pagine): ho agganciato le card alle frasi in cui introduce l'argomento. I punti incerti sono elencati al §4.
- Sottotitoli: generati dalla trascrizione automatica del prof con correzione dei nomi propri (Giolitti, Crispi, Bava Beccaris, Zanardelli, Kuliscioff, Salvemini…); **non riletti per intero** (NV); possono restare errori del riconoscimento. Le voci Kore sono nei sottotitoli con il testo vero.
- Webcam: il prof è 184×138 nell'originale, ingrandita 2,2× nel riquadro 4:3 (morbida, come nelle altre lezioni); testa vicina al bordo alto già nell'originale.
- Immagini del prof: sono piccole (da 193×454 a 777×497); migliorate con riduzione del rumore, ingrandimento ×4 (EDSR) e nitidezza, senza cambiare i tratti. L'infografica dei flussi migratori e la carta della Libia restano poco leggibili nei dettagli minuti (la risoluzione dell'originale non lo permette).
- Non esiste una «mappa finale della lezione» del prof: non l'ho inventata (le 3 mappe del prof sono nel video). Dopo gli argomenti senza mappa c'è solo la pillola.
- Durata: P1 51:43, P2 53:09 (50–60 min).
- Il parlato del prof è stato ripulito solo con highpass 80 Hz e riduzione rumore leggera: nessun altro filtro (lezione non tra quelle da rifare).
- Dispensa: stesse slide del video senza riquadro del prof e senza fascia con il nome; strato di testo invisibile con il testo di ogni card. Mappe in PDF a parte con copertina «MAPPE».
- Quiz (5 domande per argomento), verifica finale (xlsx del prof) e compiti sono quelli della consegna del 20/11 (JSON in questa cartella): non rivisti da me (NV).