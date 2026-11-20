# RAPPORTO DI REVISIONE · Storia V · Lezione 12 · «L'Europa e il mondo negli anni Trenta» · CARD INTERE 19/11 (Prof. Giorgio Mazzotti)
19/11/2026 · chat v3 · ramo `revisione-storia-V-lez12` (sostituisce la consegna precedente della lezione) · modello: Spagnolo Lez. 1. Ogni dato è etichettato **M** (misurato), **S** (stima / lettura a vista), **NV** (non verificato).

**Cosa è cambiato rispetto alla consegna precedente (note master 19/11: 8 punti delle 03:40 + card intere delle 05:10, controlli delle 05:25, copertina delle 08:55).** Rifatto da zero: trascrizione, tagli, slide (il prof non ha mandato il PDF: testo letto dai fotogrammi), mappe, approfondimenti, copertina. Riusati: voci Kore già presenti (benvenuto, mappe, pillole, schemi, glossari, riepiloghi, approfondimenti AN), quiz, compiti e verifica della consegna precedente.

## 1. Le 8 correzioni punto per punto
| # | Punto della master | Esito |
|---|---|---|
| 1 | Al massimo 3 card per slide; nessuna slide ferma oltre 3 minuti; immagini a tempo | fatto: ogni punto della slide del prof è UNA card intera (nessuna card spezzata con «…», titolo in grassetto una sola volta), card alte quanto il loro testo e allineate in alto, al massimo 3 card per slide (mai una card sola, salvo accanto a un'immagine del prof); il bordo giallo si accende quando il prof inizia quel punto. Le slide di testo sono 12; durata massima misurata 535 s. Slide oltre 180 s: arg. 2 slide 1 (192 s), arg. 3 slide 1 (182 s), arg. 6 slide 2 (418 s), arg. 7 slide 2 (284 s), arg. 8 slide 1 (388 s), arg. 9 slide 1 (535 s). Le immagini del prof sono messe a tempo (invariato).  |
| 2 | Sincronia: il bordo giallo si accende quando il prof INIZIA il punto (±1 s); 10 punti a caso | fatto in modo diverso dal calcolo automatico di prima: l'inizio di ogni card è stato scelto leggendo la trascrizione (frase per frase) da revisori; tabella dei 10 punti qui sotto. Alcune card non hanno corrispondenza nel parlato (vedi sezione 4). |
| 3 | Mappe ridisegnate con `kit/tools/mappa.py`, intere, nodi a tempo con la voce Kore | fatto: le 3 mappe del prof (L'autoritarismo, La guerra civile spagnola, Hitler) sono ridisegnate (centro + rami, nodi con la voce Kore a tempo); dopo gli argomenti 5, 6 e 9. |
| 4 | Almeno un approfondimento animato (4c) per argomento, 40–60 s, voce Kore | fatto: 9 approfondimenti (uno per argomento), voce Kore AN già esistente tagliata a fine frase, durata dei pezzi AP1 50,2; AP2 51,9; AP3 51,5; AP4 55,3; AP5 51,1; AP6 52,1; AP7 50,4; AP8 50,5; AP9 52,4 (compresi 0,9 s iniziali e 1,2 s finali di pausa), card che compaiono a tempo con la voce; i testi vengono dal parlato del prof (da far confermare, sezione 5). |
| 5 | Schema di ripasso: 4–6 righe | già a norma: 4–6 righe per argomento. |
| 6 | `trans.wav` + dissolvenza a ogni cambio di pezzo | a norma (tutti i pezzi, anche prof → approfondimento → mappa → pillola); dissolvenza 0,5 s dal fotogramma precedente. Dentro il pezzo del prof il cambio di slide è un taglio netto (NV: non ho aggiunto dissolvenze fra slide dello stesso pezzo). |
| 7 | Copertina: titolo esatto; card ARGOMENTI non sovrapposta | a norma: «L'Europa e il mondo negli anni Trenta» su 2 righe a sinistra del riquadro del prof; la card ARGOMENTI sotto il titolo (vista a occhio sul fotogramma). |
| 8 | Avviso diritti: in basso al centro, bianco 24 px senza riquadro, mai sopra il piè di pagina della copertina | fatto: sulla sigla (nera) negli ultimi 2 s, testo bianco 24 px senza riquadro; tolto dalla copertina bianca (il testo bianco non si vede su bianco). |

### Sincronia: 10 punti a caso (M)
| Dove | Argomento | Card accesa | Frase del prof che inizia in quel punto (trascrizione) | Scarto dall'inizio della frase |
|---|---|---|---|---|
| Parte 1 · 12:29.47 | arg. 2 | «nel 1936 una coalizione di sinistra (comunisti, sociali…» | «Sia le organizzazioni di estrema destra, che le organizzazioni forse di sin…» | +0.0 s |
| Parte 1 · 15:55.27 | arg. 3 | «nel 1926 il generale Józef Piłsudski instaura un regime…» | «Non c'è solo Francia e Gran Bretagna che, tutto sommato, pur con gli opport…» | -0.3 s |
| Parte 2 · 2:28.10 | arg. 6 | «nel luglio 1936 il generale Francisco Franco guida un c…» | «Nel luglio 1936 il generale Francisco Franco guidò una sollevazione militar…» | +0.0 s |
| Parte 2 · 4:01.20 | arg. 6 | «Italia e Germania sostengono apertamente Franco con tru…» | «Chiaramente la guerra spagnola si internazionalizzò rapidamente: l'Italia f…» | -0.0 s |
| Parte 2 · 8:03.60 | arg. 6 | «lacerata da scontri interni tra le sue stesse fazioni (…» | «Nonostante la resistenza, le divisioni interne al fronte repubblicano, perc…» | -0.0 s |
| Parte 2 · 14:06.53 | arg. 7 | «salito al potere nel 1933, Adolf Hitler decide di smant…» | «Ecco, però vediamo la Seconda, l'inizio, verso la Seconda guerra mondiale. …» | -0.5 s |
| Parte 2 · 14:34.63 | arg. 7 | «crolla il fragile equilibrio internazionale; nel 1935 l…» | «La stabilità internazionale, faticosamente garantita dai trattati degli ann…» | +0.0 s |
| Parte 2 · 21:14.20 | arg. 8 | «nel marzo 1938 le truppe tedesche occupano l'Austria, c…» | «Hitler si muove, e quando dico si muove intendo si espande ormai, sempre pi…» | -0.2 s |
| Parte 2 · 29:24.60 | arg. 9 | «nel marzo 1939 Hitler viola gli accordi occupando Praga…» | «se nel marzo 1939…» | -0.6 s |
| Parte 2 · 33:49.10 | arg. 9 | «il 23 agosto 1939, Germania e URSS firmano a sorpresa u…» | «Marzo, aprile, maggio del 1939, appunto, Italia e Germania stipulano il Pat…» | +0.0 s |

L'accensione coincide con l'inizio di una frase del prof per costruzione (M: scarto dall'inizio della frase). Che la frase sia davvero quella della card l'hanno giudicato i revisori leggendo la trascrizione: io non l'ho riverificato punto per punto (NV).

## 2. Misure sul video nuovo (M)

### Parte 1
```
durata 1981.63 s = 33:01.63 | fotogrammi 59449 (durata*30=59449) = somma dei pezzi 59449 | peso 164.5 MB | 1920x1080
LUFS -15.0  TP -1.9 dBFS
Q1 atteso 659.267 trovato 659.267 scarto +0.000 OK
Q2 atteso 946.767 trovato 946.768 scarto +0.000 OK
Q3 atteso 1225.067 trovato 1225.068 scarto +0.001 OK
Q4 atteso 1546.200 trovato 1546.201 scarto +0.001 OK
Q5 atteso 1864.100 trovato 1864.100 scarto -0.000 OK
```
Silenzi > 3 s (−45 dB): 0.
Fermi del prof ≥ 1 s: nessuno.
Fotogramma Quiz ai `quiz_s`: Q1 658.77s OK, Q2 946.27s OK, Q3 1224.57s OK, Q4 1545.70s OK, Q5 1863.60s OK.
sha256 (ricomposto dalle parti): `5e0d0d66e26fb1797435d9d495b93234a2932377b09599e7821eca859a418b56  Storia_Lez12_Parte1_1080p.mp4`

### Parte 2
```
durata 2513.43 s = 41:53.43 | fotogrammi 75403 (durata*30=75403) = somma dei pezzi 75403 | peso 235.5 MB | 1920x1080
LUFS -15.2  TP -1.9 dBFS
Q6 atteso 838.033 trovato 838.034 scarto +0.000 OK
Q7 atteso 1265.700 trovato 1265.701 scarto +0.001 OK
Q8 atteso 1756.100 trovato 1756.101 scarto +0.001 OK
Q9 atteso 2414.133 trovato 2414.133 scarto +0.000 OK
```
Silenzi > 3 s (−45 dB): 0.
Fermi del prof ≥ 1 s: nessuno.
Fotogramma Quiz ai `quiz_s`: Q6 837.53s OK, Q7 1265.20s OK, Q8 1755.60s OK, Q9 2413.63s OK.
sha256 (ricomposto dalle parti): `b9bd1bdb1e3c49e7cddc8165b85e69a39a3bc6472f1a4dea2d3db6cb3064643a  Storia_Lez12_Parte2_1080p.mp4`

Formato: 1920×1080, 30 fps, x264 veryfast CRF 25, AAC 192 kbps 48 kHz; parlato del prof dall'originale con la catena del kit; voci Kore a −16 LUFS. **Le Parti durano meno dei 50 minuti** (materiale del prof).

## 3. Tabella dei pezzi (sezione C della scheda tecnica) (M)

**Parte 1**

| Pezzo | Presente | Inizio | Durata |
|---|---|---|---|
| 1 · Sigla `SIGLA` | sì | 0:00.00 | 15.0 s |
| 3 · Copertina + benvenuto (voce Kore) `COVERV` | sì | 0:15.00 | 11.8 s |
| 3 · Introduzione del prof (copertina con riquadro) `D0` | sì | 0:26.80 | 196.3 s |
| 4a · Titolo argomento `T1` | sì | 3:43.10 | 4.0 s |
| 4b · Docente + slide `A1` | sì | 3:47.10 | 341.2 s |
| 4c · Approfondimento animato (voce Kore) `AP1` | sì | 9:28.30 | 50.2 s |
| 4e · Pillola di ripasso (introduzione blu) `PI1` | sì | 10:18.53 | 10.3 s |
| 4f · Pillola di ripasso (schema guidato bianco) `PS1` | sì | 10:28.83 | 29.9 s |
| 4g · Scheda Quiz `Q1` | sì | 10:58.77 | 5.0 s |
| 4a · Titolo argomento `T2` | sì | 11:03.77 | 4.0 s |
| 4b · Docente + slide `A2` | sì | 11:07.77 | 191.9 s |
| 4c · Approfondimento animato (voce Kore) `AP2` | sì | 14:19.67 | 51.9 s |
| 4e · Pillola di ripasso (introduzione blu) `PI2` | sì | 15:11.57 | 10.5 s |
| 4f · Pillola di ripasso (schema guidato bianco) `PS2` | sì | 15:22.03 | 24.2 s |
| 4g · Scheda Quiz `Q2` | sì | 15:46.27 | 5.0 s |
| 4a · Titolo argomento `T3` | sì | 15:51.27 | 4.0 s |
| 4b · Docente + slide `A3` | sì | 15:55.27 | 182.0 s |
| 4c · Approfondimento animato (voce Kore) `AP3` | sì | 18:57.27 | 51.5 s |
| 4e · Pillola di ripasso (introduzione blu) `PI3` | sì | 19:48.73 | 10.5 s |
| 4f · Pillola di ripasso (schema guidato bianco) `PS3` | sì | 19:59.20 | 25.4 s |
| 4g · Scheda Quiz `Q3` | sì | 20:24.57 | 5.0 s |
| 4a · Titolo argomento `T4` | sì | 20:29.57 | 4.0 s |
| 4b · Docente + slide `A4` | sì | 20:33.57 | 222.1 s |
| 4c · Approfondimento animato (voce Kore) `AP4` | sì | 24:15.67 | 55.3 s |
| 4e · Pillola di ripasso (introduzione blu) `PI4` | sì | 25:11.00 | 11.1 s |
| 4f · Pillola di ripasso (schema guidato bianco) `PS4` | sì | 25:22.10 | 23.6 s |
| 4g · Scheda Quiz `Q4` | sì | 25:45.70 | 5.0 s |
| 4a · Titolo argomento `T5` | sì | 25:50.70 | 4.0 s |
| 4b · Docente + slide `A5` | sì | 25:54.70 | 200.9 s |
| 4c · Approfondimento animato (voce Kore) `AP5` | sì | 29:15.60 | 51.1 s |
| 4d · Mappa del prof (voce Kore) `MAP1` | sì | 30:06.70 | 19.4 s |
| 4e · Pillola di ripasso (introduzione blu) `PI5` | sì | 30:26.07 | 11.7 s |
| 4f · Pillola di ripasso (schema guidato bianco) `PS5` | sì | 30:37.73 | 25.9 s |
| 4g · Scheda Quiz `Q5` | sì | 31:03.60 | 5.0 s |
| 5 · Glossario `GL` | sì | 31:08.60 | 54.4 s |
| 6 · Riepilogo finale `RIEP` | sì | 32:02.97 | 53.7 s |
| 7 · Finale `FINALE` | sì | 32:56.63 | 5.0 s |

**Parte 2**

| Pezzo | Presente | Inizio | Durata |
|---|---|---|---|
| 1 · Sigla `SIGLA` | sì | 0:00.00 | 15.0 s |
| 3 · Copertina + benvenuto (voce Kore) `COVERV` | sì | 0:15.00 | 48.1 s |
| 4a · Titolo argomento `T6` | sì | 1:03.10 | 4.0 s |
| 4b · Docente + slide `A6` | sì | 1:07.10 | 656.1 s |
| 4c · Approfondimento animato (voce Kore) `AP6` | sì | 12:03.20 | 52.1 s |
| 4d · Mappa del prof (voce Kore) `MAP2` | sì | 12:55.30 | 17.0 s |
| 4e · Pillola di ripasso (introduzione blu) `PI6` | sì | 13:12.27 | 10.3 s |
| 4f · Pillola di ripasso (schema guidato bianco) `PS6` | sì | 13:22.57 | 35.0 s |
| 4g · Scheda Quiz `Q6` | sì | 13:57.53 | 5.0 s |
| 4a · Titolo argomento `T7` | sì | 14:02.53 | 4.0 s |
| 4b · Docente + slide `A7` | sì | 14:06.53 | 327.5 s |
| 4c · Approfondimento animato (voce Kore) `AP7` | sì | 19:34.03 | 50.4 s |
| 4e · Pillola di ripasso (introduzione blu) `PI7` | sì | 20:24.40 | 11.7 s |
| 4f · Pillola di ripasso (schema guidato bianco) `PS7` | sì | 20:36.07 | 29.1 s |
| 4g · Scheda Quiz `Q7` | sì | 21:05.20 | 5.0 s |
| 4a · Titolo argomento `T8` | sì | 21:10.20 | 4.0 s |
| 4b · Docente + slide `A8` | sì | 21:14.20 | 388.2 s |
| 4c · Approfondimento animato (voce Kore) `AP8` | sì | 27:42.40 | 50.5 s |
| 4e · Pillola di ripasso (introduzione blu) `PI8` | sì | 28:32.93 | 12.8 s |
| 4f · Pillola di ripasso (schema guidato bianco) `PS8` | sì | 28:45.77 | 29.8 s |
| 4g · Scheda Quiz `Q8` | sì | 29:15.60 | 5.0 s |
| 4a · Titolo argomento `T9` | sì | 29:20.60 | 4.0 s |
| 4b · Docente + slide `A9` | sì | 29:24.60 | 534.7 s |
| 4c · Approfondimento animato (voce Kore) `AP9` | sì | 38:19.27 | 52.4 s |
| 4d · Mappa del prof (voce Kore) `MAP3` | sì | 39:11.67 | 18.6 s |
| 4e · Pillola di ripasso (introduzione blu) `PI9` | sì | 39:30.30 | 13.3 s |
| 4f · Pillola di ripasso (schema guidato bianco) `PS9` | sì | 39:43.63 | 30.0 s |
| 4g · Scheda Quiz `Q9` | sì | 40:13.63 | 5.0 s |
| 5 · Glossario `GL` | sì | 40:18.63 | 46.6 s |
| 6 · Riepilogo finale `RIEP` | sì | 41:05.23 | 43.2 s |
| 7 · Finale `FINALE` | sì | 41:48.43 | 5.0 s |

## 4. Cose che non tornano nel parlato / limiti
- **Durata (M):** Parte 1 e Parte 2 durano meno dei 50 minuti della regola (vedi sezione 2): il prof parla 54 minuti e il materiale non basta per arrivare a 50 per Parte senza inventare contenuti. La master decide se va bene.
- **Slide ferme oltre i 3 minuti (M): molte.** Con le card intere un argomento in cui il prof parla a lungo su pochi punti resta sulla stessa slide: elenco al punto 1 (arg. 8: 388 s su 2 card; arg. 9: 535 s su 3 card; arg. 6 seconda slide 482 s; arg. 7 seconda slide 284 s). Non c'è altro modo di accorciarle senza spezzare le card o inventare contenuti. Le immagini del PDF/video del prof sono messe a tempo dove il prof le mostra (carta della Cina e della Spagna).
- **Introduzione (M):** il prof parla 196 s sopra la copertina; dopo ~2 min (115,8 s) passano 2 slide «Di cosa parliamo» con gli argomenti della Parte 1 in card (3+2). Il prof nell'introduzione non nomina i singoli argomenti uno per uno: **le card non hanno il bordo giallo** (nessun aggancio nel parlato).
- **Copertina:** titolo su 2 righe a sinistra del riquadro del prof; la card ARGOMENTI scende sotto il titolo (8 argomenti: carattere più piccolo).
- **La lezione non ha slide in PDF:** il testo delle 5 pagine è stato letto a mano dai fotogrammi del video; le parole coperte dalla webcam (bordo destro) sono ricostruite («Commonwealth», «Nuova Zelanda», «instabilità politica», «autoritario», «Patto d'acciaio», «e sottomettendo») (NV). Il prof tratta la Spagna già a 1014 s mentre l'argomento 4 ha una sola card (digressione): per non lasciare la slide ferma 222 s ho messo la pagina della guerra civile (1015–1106 s) come immagine a tempo.
- Il prof non segue l'ordine delle slide: arg. 3 (Ungheria prima di Polonia), arg. 6 (punto 4 agganciato alle divisioni interne), arg. 7 (coscrizione e Renania dopo l'appeasement), arg. 9 (Patto d'acciaio e Molotov-Ribbentrop): i tempi dei punti sono approssimati dove il prof tratta in ordine diverso.
- Webcam del prof 184×138 ingrandita 2,2× (morbida); testa vicina al bordo alto già nell'originale (S).

## 5. DA CONFERMARE COL PROF / cosa NON ho verificato (NV)
- Gli **approfondimenti** (testi AN della catena precedente, tagliati a fine frase) vanno riletti dal prof o dalla master. Non li ho riverificati frase per frase (NV).
- Voci: tutte Kore (ramo `voci-storia-V-lez12`, già presenti, nessuna nuova richiesta); le 9 voci degli approfondimenti sono le voci AN tagliate a fine frase (controllo della trascrizione sul file tagliato); non le ho riascoltate a orecchio (NV).
- Sottotitoli: parlato del prof corretto a blocchi da revisori automatici (consegna precedente), non riletti per intero; tempi ±0,3 s non misurati (NV). Le voci Kore sono nei sottotitoli.
- PDF slide: stesse immagini del video (S); confronto pagina per pagina con i fotogrammi non fatto (NV). Quiz di argomento riusati (da approvare dalla master).
