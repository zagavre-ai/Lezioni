# RAPPORTO · Storia V · «L’Italia dal ’68 alla crisi della Prima Repubblica» · correzioni del 22/11

Lezione rifatta da zero nel modello del 22/11 sul video originale del prof (4795,9 s, release `mazzotti-storia-V`), in 2 Parti. Marcature: [misurato], [per costruzione], [non verificato].

## 1 · Misure

| | Parte 1 | Parte 2 |
|---|---|---|
| Durata | 52:06,7 [misurato] | 51:04,8 [misurato] |
| Fotogrammi | 93799 (attesi 93801: −2) / 91944 (attesi 91944) [misurato] | |
| Formato / peso | 1920×1080 30 fps, x264 CRF 19, AAC 192k 48 kHz; 280 MB [misurato] | idem; 260 MB [misurato] |
| Loudness / picco | -16.5 LUFS, -1.9 dBFS [misurato] | -16.2 LUFS, -1.9 dBFS [misurato] |
| Timbre della voce del prof (acuti >4 kHz meno >100 Hz) | −16,05 dB [misurato] (originale −19,0; limiti −9…−20) | −15,75 dB [misurato] |
| `controllo_rapido.py` | ESITO OK, nessun errore [misurato] | ESITO OK, nessun errore [misurato] |
| `controllo_finale.py` | TUTTO OK (sottotitoli: attacco sulla voce 86% di 7 verificabili) | TUTTO OK (80% di 10) |
| Scatto `quiz.wav` | 4 quiz a 0,0 s [misurato, controllo_jingle.py] | 4 quiz a 0,0 s [misurato] |

Foglio dei fotogrammi e json del controllo rapido: `foglio_fotogrammi_*.jpg`, `controllo_rapido_*.json` (accanto ai video). Ho guardato il foglio della Parte 1 con gli occhi: fondo bianco, schede blu scuro a tutto schermo, card a 40 px intere, piè di pagina senza nome del docente, riquadro 4:3 con fascia gialla, sigla finale con avviso diritti. Il foglio della Parte 2 non l’ho riaperto dopo l’ultima codifica [non verificato a occhio; il controllo rapido è OK].

## 2 · Cosa è stato fatto rispetto al prompt del 22/11
- **Mappe del prof**: solo le 3 del PDF «MAPPE LEZIONE 19» (argomenti 3, 4, 7), ridisegnate nel modello BES (5 colori, legenda in alto a destra), stesse parole e stesse frecce (anche le parole sulle frecce), un riquadro alla volta con la voce Kore e fermo finale di 4 s; il riquadro in lettura è evidenziato in giallo. Tolte tutte le mappe inventate (MAP1–8, MAPF). Gli argomenti 1, 2, 5, 6, 8 non hanno mappa e si chiudono con la pillola di ripasso (come stabilito dalla master). **La mappa 3 del prof non ha la domanda come titolo: l’ho scritta io, «Come cambia il quadro politico negli anni Novanta?»**. Nella mappa 3 «DC» è rispiegata sullo schermo («la DC, cioè Democrazia Cristiana»).
- **Slide**: card a 40 px (mai sotto), interlinea 1,5, al massimo 3 card intere (nel campione 1–2 per la lunghezza delle card), bordo giallo sulla frase in corso, riquadro 4:3 (412×309 a x=1428, y=148). Per non avere schermate identiche oltre 3 minuti ogni 100 s si alterna la finestra normale con la card in primo piano (testo a 50 px) e si inseriscono gli approfondimenti Kore. Le pagine-immagine del prof sono divise per argomento: Piazza Fontana solo nell’arg. 3, Berlinguer e Moro solo nell’arg. 4, ognuna col suo titolo.
- **Introduzione animata senza riquadro**; **nome del docente** mai detto né scritto nelle animazioni (rifatte le voci BENV1, MD1–3); la fascia gialla è l’unico posto. L’introduzione del prof sopra la copertina dura circa 147 s, poi 3 slide «Di cosa parliamo».
- **Parte 2 si apre con lo spiegone** (voce Kore, argomento per argomento, con le foto e le mappe della Parte 1; nessun riquadro).
- **Compiti letti con la voce COMPITI** (parole esatte del docente, uno alla volta con bordo giallo, frase finale su «Consegna»). Schede quiz e verifica con «Rispondi · premi Controlla · poi Continua».
- **Verifica di sbarramento**: scheda di 4,5 s nel video con jingle a +0,5 s; le 10 domande (test Excel del prof) sono in `verifica_finale.json`/`.xlsx` per la pagina, come i quiz (confermato dalla master 22/11 22:20).
- **Audio del prof**: filtro dei bassi, riduzione leggera del rumore, lieve recupero degli acuti, −16 LUFS; pause oltre 2,5 s accorciate a circa 1 s; incespicamenti isolati («Um», «Mm») tolti; niente mai a metà frase (tabella nella sezione 5).
- **Suoni**: i jingle `titolo`, `repaso`, `quiz`, `finale` e `trans.wav` a ogni cambio di pezzo (da mezzo secondo prima del cambio) con dissolvenza di 0,4 s. Sul fermo finale delle mappe suona una volta `trans.wav` a metà del fermo, per non avere scheda muta [scelta mia].

## 3 · Voci Kore
- 18 voci nuove: BENV1_R2, RIP2A, A2N, MP1_0–5, MP2_0–3, MP3_0–3, COMPITI. Ognuna è stata trascritta e confrontata con il testo; bordi (ultimi 50 ms) sotto 0,003 su tutte.
- Differenze di trascrizione dell’ASR (non riascoltate): MP1_1 e MP1_3 (parole dell’anno/«settanta» non riconosciute), MP2_3 («rosse» letta «russe»), MP3_0, COMPITI («operaie»/«operai»), A2N («negli anni cinquanta» → «negni»). [non verificato all’ascolto: la master le riascolti, in particolare MP2_3]
- Voci già presenti (AN*, P*, SC*, R*, GL*, RF*, FIN*) riusate; nessuna dice il nome del docente (controllato sui testi).

## 4–5 · Tabelle
## 4 · Tabella dei pezzi

**Parte 1**

| Pezzo | Id | Minuto (Parte) | Durata |
|---|---|---|---|
| Sigla (15 s) | sigla | P1 0:00.0 | 15.0 s |
| Copertina animata + benvenuto (voce Kore, senza riquadro del docente) | cover_kore | P1 0:15.5 | 21.6 s |
| Introduzione del docente | intro_cover | P1 0:37.6 | 144.8 s |
| Introduzione del docente | intro_args | P1 3:02.9 | 136.7 s |
| Titolo argomento (jingle titolo.wav) · arg. 1 | t1 | P1 5:20.1 | 4.0 s |
| Docente + slide | a1a | P1 5:24.6 | 95.3 s |
| Approfondimento animato (voce Kore) · arg. 1 | an1_13_18 | P1 7:00.4 | 60.5 s |
| Docente + slide | a1b | P1 8:01.4 | 441.3 s |
| Docente + slide | a1c | P1 15:23.2 | 166.9 s |
| Approfondimento animato (voce Kore) · arg. 1 | an1_14 | P1 18:10.6 | 28.3 s |
| Pillola/schema di ripasso (jingle repaso.wav) · arg. 1 | sch1 | P1 18:39.3 | 36.2 s |
| Scheda Quiz (jingle quiz.wav a +0,5 s) · arg. 1 | q1 | P1 19:16.0 | 4.5 s |
| Titolo argomento (jingle titolo.wav) · arg. 2 | t2 | P1 19:21.0 | 4.0 s |
| Docente + slide | a2a | P1 19:25.5 | 244.3 s |
| Approfondimento animato (voce Kore) · arg. 2 | an2_1 | P1 23:30.3 | 63.5 s |
| Docente + slide | a2b | P1 24:34.3 | 87.1 s |
| Pillola/schema di ripasso (jingle repaso.wav) · arg. 2 | sch2 | P1 26:01.9 | 26.9 s |
| Scheda Quiz (jingle quiz.wav a +0,5 s) · arg. 2 | q2 | P1 26:29.3 | 4.5 s |
| Titolo argomento (jingle titolo.wav) · arg. 3 | t3 | P1 26:34.3 | 4.0 s |
| Docente + slide | a3a | P1 26:38.8 | 131.8 s |
| Approfondimento animato (voce Kore) · arg. 3 | an3_2 | P1 28:51.1 | 46.9 s |
| Docente + slide | a3b | P1 29:38.5 | 135.7 s |
| Approfondimento animato (voce Kore) · arg. 3 | an3_20 | P1 31:54.7 | 24.9 s |
| Docente + slide | a3c | P1 32:20.1 | 211.6 s |
| Approfondimento animato (voce Kore) · arg. 3 | an3_19 | P1 35:52.2 | 22.9 s |
| Docente + slide | a3d | P1 36:15.6 | 128.3 s |
| Approfondimento animato (voce Kore) · arg. 3 | an3_16 | P1 38:24.4 | 20.7 s |
| Docente + slide | a3e | P1 38:45.5 | 116.7 s |
| Mappa del docente (BES, ramo per ramo, voce Kore) · arg. 3 | map1 | P1 40:42.8 | 37.3 s |
| Pillola/schema di ripasso (jingle repaso.wav) · arg. 3 | sch3 | P1 41:20.6 | 32.5 s |
| Scheda Quiz (jingle quiz.wav a +0,5 s) · arg. 3 | q3 | P1 41:53.6 | 4.5 s |
| Titolo argomento (jingle titolo.wav) · arg. 4 | t4 | P1 41:58.6 | 4.0 s |
| Docente + slide | a4a | P1 42:03.1 | 181.7 s |
| Approfondimento animato (voce Kore) · arg. 4 | an4_4_21 | P1 45:05.3 | 50.5 s |
| Docente + slide | a4b | P1 45:56.3 | 121.4 s |
| Approfondimento animato (voce Kore) · arg. 4 | an4_17 | P1 47:58.2 | 17.9 s |
| Docente + slide | a4c | P1 48:16.6 | 90.3 s |
| Mappa del docente (BES, ramo per ramo, voce Kore) · arg. 4 | map2 | P1 49:47.4 | 33.2 s |
| Pillola/schema di ripasso (jingle repaso.wav) · arg. 4 | sch4 | P1 50:21.2 | 30.7 s |
| Scheda Quiz (jingle quiz.wav a +0,5 s) · arg. 4 | q4 | P1 50:52.4 | 4.5 s |
| Glossario animato | gl1 | P1 50:57.4 | 33.6 s |
| Ripasso finale | rf1 | P1 51:31.5 | 16.3 s |
| Saluto | fin1 | P1 51:48.2 | 13.0 s |
| Sigla finale con avviso diritti | finale | P1 52:01.7 | 5.0 s |

**Parte 2**

| Pezzo | Id | Minuto (Parte) | Durata |
|---|---|---|---|
| Sigla (15 s) | sigla2 | P2 0:00.0 | 15.0 s |
| Spiegone della Parte 1 (voce Kore) | spiegone | P2 0:15.5 | 87.2 s |
| Titolo argomento (jingle titolo.wav) · arg. 5 | t5 | P2 1:43.2 | 4.0 s |
| Docente + slide | a5a | P2 1:47.7 | 137.4 s |
| Approfondimento animato (voce Kore) · arg. 5 | an5_5 | P2 4:05.5 | 31.1 s |
| Docente + slide | a5b | P2 4:37.2 | 102.9 s |
| Docente + slide | a5c | P2 6:20.6 | 133.5 s |
| Approfondimento animato (voce Kore) · arg. 5 | an5_6_7 | P2 8:34.6 | 45.9 s |
| Docente + slide | a5d | P2 9:21.0 | 68.3 s |
| Pillola/schema di ripasso (jingle repaso.wav) · arg. 5 | sch5 | P2 10:29.8 | 38.0 s |
| Scheda Quiz (jingle quiz.wav a +0,5 s) · arg. 5 | q5 | P2 11:08.2 | 4.5 s |
| Titolo argomento (jingle titolo.wav) · arg. 6 | t6 | P2 11:13.2 | 4.0 s |
| Docente + slide | a6a | P2 11:17.7 | 200.5 s |
| Approfondimento animato (voce Kore) · arg. 6 | an6_8 | P2 14:38.7 | 44.1 s |
| Docente + slide | a6c | P2 15:23.3 | 334.2 s |
| Approfondimento animato (voce Kore) · arg. 6 | an6_9 | P2 20:58.0 | 23.5 s |
| Docente + slide | a6d | P2 21:22.0 | 433.9 s |
| Pillola/schema di ripasso (jingle repaso.wav) · arg. 6 | sch6 | P2 28:36.3 | 36.9 s |
| Scheda Quiz (jingle quiz.wav a +0,5 s) · arg. 6 | q6 | P2 29:13.7 | 4.5 s |
| Titolo argomento (jingle titolo.wav) · arg. 7 | t7 | P2 29:18.7 | 4.0 s |
| Docente + slide | a7a | P2 29:23.2 | 459.9 s |
| Approfondimento animato (voce Kore) · arg. 7 | an7_10_11 | P2 37:03.6 | 46.2 s |
| Docente + slide | a7b | P2 37:50.3 | 227.4 s |
| Mappa del docente (BES, ramo per ramo, voce Kore) · arg. 7 | map3 | P2 41:38.2 | 37.7 s |
| Pillola/schema di ripasso (jingle repaso.wav) · arg. 7 | sch7 | P2 42:16.4 | 30.5 s |
| Scheda Quiz (jingle quiz.wav a +0,5 s) · arg. 7 | q7 | P2 42:47.4 | 4.5 s |
| Titolo argomento (jingle titolo.wav) · arg. 8 | t8 | P2 42:52.4 | 4.0 s |
| Docente + slide | a8a | P2 42:56.9 | 171.8 s |
| Approfondimento animato (voce Kore) · arg. 8 | an8_12_22 | P2 45:49.2 | 52.0 s |
| Docente + slide | a8b | P2 46:41.7 | 48.4 s |
| Pillola/schema di ripasso (jingle repaso.wav) · arg. 8 | sch8 | P2 47:30.5 | 30.3 s |
| Scheda Quiz (jingle quiz.wav a +0,5 s) · arg. 8 | q8 | P2 48:01.4 | 4.5 s |
| Glossario animato | gl2 | P2 48:06.4 | 33.6 s |
| Ripasso finale | rf2 | P2 48:40.5 | 16.8 s |
| Scheda Verifica di sbarramento | verifica | P2 48:57.7 | 4.5 s |
| Saluto | fin2 | P2 49:02.7 | 13.8 s |
| Sigla finale con avviso diritti | finale2 | P2 49:17.0 | 5.0 s |
| Intro «Compiti» (jingle) | compiti_i | P2 49:22.5 | 3.5 s |
| Compiti del docente | compiti_voce | P2 49:26.5 | 97.8 s |

Durate misurate sui file dei pezzi; a ogni confine `trans.wav` + dissolvenza di 0,4 s (ultimo fotogramma tenuto 0,5 s sotto `trans.wav`, poi dissolvenza nel pezzo seguente): nessun taglio secco [per costruzione].

## 5 · Fine di ogni pezzo del docente (CLAUDE.md §2.2)

«Frase finita» = l'ultima parola chiude la frase (controllato sulla trascrizione, a occhio). Il segno `*` = la trascrizione automatica non mette il punto, ma la frase è finita (letto a mano).

| Pezzo | Minuto originale (fine) | Ultime parole | Frase finita |
|---|---|---|---|
| P1 intro_cover (0:37.6) | 2:27 | …tensioni politiche e crisi economiche. | sì |
| P1 intro_args (3:02.9) | 4:47 | …il decennio dei settanta. | sì |
| P1 a1a (5:24.6) | 6:23 | …o meno, e quindi anche poi nelle università. | sì |
| P1 a1b (8:01.4) | 13:49 | …vogliamo sfornare cittadini e non appunto autoritaristi, eccetera. | sì |
| P1 a1c (15:23.2) | 16:38 | …molti casi il liceo classico, vado a ripetere. | sì |
| P1 a2a (19:25.5) | 20:42 | …tutte queste conquiste maggiori forme di partecipazione democratica. | sì |
| P1 a2b (24:34.3) | 22:09 | …punto di vista. Chiaramente i conservatori sono scontenti. | sì |
| P1 a3a (26:38.8) | 24:26 | …rimasta, ecco, quella titolazione Banca Nazionale dell'agricoltura. | sì |
| P1 a3b (29:38.5) | 26:43 | …far capire che la tensione politica era estrema. | sì |
| P1 a3c (32:20.1) | 30:16 | …però fu anche responsabile di tutte queste stragi. | sì |
| P1 a3d (36:15.6) | 32:25 | …tali del mondo dei partiti e del governo. | sì |
| P1 a3e (38:45.5) | 34:22 | …Omicidio! | sì |
| P1 a4a (42:03.1) | 37:27 | …come dire poi il fenomeno viene viene fermato | sì* |
| P1 a4b (45:56.3) | 39:34 | …o meno e socialisti comunisti al potere insieme. | sì |
| P1 a4c (48:16.6) | 41:04 | …proprio ponte di collegamento tra le due parti. | sì |
| P2 a5a (1:47.7) | 43:22 | …in Italia | sì* |
| P2 a5b (4:37.2) | 45:05 | …quell'altra domenica circoleranno le altre targhe, per dire. | sì |
| P2 a5c (6:20.6) | 47:18 | …e la questione lavorativa si sposta un po'. | sì |
| P2 a5d (9:21.0) | 48:27 | …dall'86 con il disastro di Cerno. | sì |
| P2 a6a (11:17.7) | 51:51 | …rivendicavano il loro diritto in effetti. | sì |
| P2 a6c (15:23.3) | 57:25 | …certo, la disoccupazione era bassa, gli investimenti c'erano. | sì |
| P2 a6d (21:22.0) | 64:46 | …Va bene? Altre sigle poi andarono avanti. | sì |
| P2 a7a (29:23.2) | 72:26 | …Fiat, la Fiat aveva nel suo libro nero. | sì |
| P2 a7b (37:50.3) | 76:15 | …uscire dalla crisi finanziaria e politica, voi capite. | sì |
| P2 a8a (42:56.9) | 79:07 | …Così l'Italia iniziò gli anni novanta. | sì |
| P2 a8b (46:41.7) | 79:55 | …Di sorprese. | sì |


## 6 · Refusi e anomalie (per la master / il prof)
Refusi corretti nelle nostre slide/dispense: nelle slide del prof non ho trovato refusi di ortografia; ho solo esplicitato le sigle sullo schermo («DC, cioè Democrazia Cristiana», «PSI, cioè Partito Socialista Italiano», «Loggia P2, cioè Propaganda Due», «PCI, cioè Partito Comunista Italiano»). Titolo della slide 2: nel PDF del prof è «Il Sessantotto e il malcontento sociale»; nelle nostre slide la pagina è divisa in due argomenti e i titoli sono quelli degli argomenti.
Anomalie del parlato del prof, riportate come le dice (da confermare col prof):
1. Corpo di Moro ritrovato in una «Fiat rossa» (originale 35:46; storicamente Renault 4).
2. Treno Italicus: «tutti i passeggeri» morti (27:17; storicamente 12).
3. Legge Mattarella: nel parlato «premio di maggioranza … 25% o 65%» (77:34), nella slide 75% maggioritario / 25% proporzionale.
4. Governo Craxi: parlato «dal 1983 al 1986», slide «dal 1983 al 1987».
5. Verifica, domanda 1 (ateneo occupato per primo alla fine del 1967 → Cattolica di Milano): il prof nel parlato cita le «Tesi della Sapienza» (1967).
6. Quiz 4, domanda 2: ruolo di Moro (presidente della DC secondo la slide; nel parlato «più volte presidente del Consiglio»).
7. Tagliato come falsa partenza il frammento «Ecco, per affrontare… durante il sequestro appunto delle brigate rosse» (originale 2247–2252 s): la master lo giudichi.

## 7 · Cosa NON ho verificato
- Sincronia labbra/voce a 0,04 s: audio e video del prof escono dallo stesso istante dell’originale [per costruzione], ma non misurata.
- Le 18 voci nuove non sono state riascoltate (vedi sezione 3).
- Ripasso/pillola, glossario e approfondimenti: testo = parole della voce Kore, con numeri in cifre sullo schermo; non ho controllato uno per uno tutti i nomi stranieri nei sottotitoli.
- Sottotitoli: fatti sul video finale dalle parole dell’originale e dalle voci Kore; non riascoltati; refusi di trascrizione corretti solo per i termini che conosco. Spenti all’avvio: lo decide il lettore [non verificato].
- Immagini del prof: ingrandite con Lanczos e nitidezza (originali 300–1100 px): restano morbide, in particolare Moro/Brigate Rosse (originale 400×331) e Craxi.
- Webcam del prof: 185×139 px ingrandita a 412×309: morbida (limite dell’originale).
- Dispensa (65 pagine A4 orizzontali, testo invisibile) e PDF mappe (4 pagine, copertina «MAPPE») rigenerati, non riaperti pagina per pagina dopo l’ultima versione.
- L’agente separato ha controllato una versione precedente (con voci provvisorie): difetti trovati e corretti (card che si toccavano, foto non corrispondenti, schermate ferme, refusi nei sottotitoli, voci Kore nei sottotitoli); **dopo l’ultima ricodifica non è stato rilanciato** [non verificato].
