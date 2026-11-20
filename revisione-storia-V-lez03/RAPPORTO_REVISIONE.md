# RAPPORTO DI REVISIONE · Storia V · Lezione 3 · «L'Italia di Giolitti» · CARD INTERE 19/11 (Prof. Giorgio Mazzotti)
19/11/2026 · chat v3 · ramo `revisione-storia-V-lez03` (sostituisce la consegna precedente della lezione) · modello: Spagnolo Lez. 1. Ogni dato è etichettato **M** (misurato), **S** (stima / lettura a vista), **NV** (non verificato).

**Cosa è cambiato rispetto alla consegna precedente (note master 19/11: 8 punti delle 03:40 + card intere delle 05:10, controlli delle 05:25, copertina delle 08:55).** Rifatto da zero: trascrizione, tagli, slide dal PDF, mappe, approfondimenti, copertina. Riusati: voci Kore già presenti (benvenuto, mappe, pillole, schemi, glossari, riepiloghi, approfondimenti AN), quiz, compiti e verifica della consegna precedente.

## 1. Le 8 correzioni punto per punto
| # | Punto della master | Esito |
|---|---|---|
| 1 | Al massimo 3 card per slide; nessuna slide ferma oltre 3 minuti; immagini a tempo | fatto: ogni punto della slide del prof è UNA card intera (nessuna card spezzata con «…», titolo in grassetto una sola volta), card alte quanto il loro testo e allineate in alto, al massimo 3 card per slide (mai una card sola, salvo accanto a un'immagine del prof); il bordo giallo si accende quando il prof inizia quel punto. Le slide di testo sono 21; durata massima misurata 610 s. Slide oltre 180 s: arg. 1 slide 1 (610 s), arg. 1 slide 2 (379 s), arg. 5 slide 1 (199 s), arg. 5 slide 2 (192 s), arg. 6 slide 1 (320 s), arg. 8 slide 2 (269 s), arg. 9 slide 1 (192 s), arg. 10 slide 1 (246 s). Le immagini del prof sono messe a tempo (invariato).  |
| 2 | Sincronia: il bordo giallo si accende quando il prof INIZIA il punto (±1 s); 10 punti a caso | fatto in modo diverso dal calcolo automatico di prima: l'inizio di ogni card è stato scelto leggendo la trascrizione (frase per frase) da revisori; tabella dei 10 punti qui sotto. Alcune card non hanno corrispondenza nel parlato (vedi sezione 4). |
| 3 | Mappe ridisegnate con `kit/tools/mappa.py`, intere, nodi a tempo con la voce Kore | fatto: le 3 mappe del prof del PDF sono ridisegnate (centro + rami, nodi con la voce Kore a tempo); dopo gli argomenti 2, 9 e 11. |
| 4 | Almeno un approfondimento animato (4c) per argomento, 40–60 s, voce Kore | fatto: 11 approfondimenti (uno per argomento), voce Kore AN già esistente tagliata a fine frase, durata dei pezzi AP1 44,8; AP2 54,8; AP3 49,1; AP4 48,1; AP5 53,3; AP6 46,9; AP7 39,2; AP8 47,8; AP9 48,5; AP10 50,7; AP11 62,4 (compresi 0,9 s iniziali e 1,2 s finali di pausa), card che compaiono a tempo con la voce; i testi vengono dal parlato del prof (da far confermare, sezione 5). |
| 5 | Schema di ripasso: 4–6 righe | già a norma: 4–6 righe per argomento. |
| 6 | `trans.wav` + dissolvenza a ogni cambio di pezzo | a norma (tutti i pezzi, anche prof → approfondimento → mappa → pillola); dissolvenza 0,5 s dal fotogramma precedente. Dentro il pezzo del prof il cambio di slide è un taglio netto (NV: non ho aggiunto dissolvenze fra slide dello stesso pezzo). |
| 7 | Copertina: titolo esatto; card ARGOMENTI non sovrapposta | a norma: «L'Italia di Giolitti» su 2 righe a sinistra del riquadro del prof; la card ARGOMENTI sotto il titolo (vista a occhio sul fotogramma). |
| 8 | Avviso diritti: in basso al centro, bianco 24 px senza riquadro, mai sopra il piè di pagina della copertina | fatto: sulla sigla (nera) negli ultimi 2 s, testo bianco 24 px senza riquadro; tolto dalla copertina bianca (il testo bianco non si vede su bianco). |

### Sincronia: 10 punti a caso (M)
| Dove | Argomento | Card accesa | Frase del prof che inizia in quel punto (trascrizione) | Scarto dall'inizio della frase |
|---|---|---|---|---|
| Parte 1 · 29:00.32 | arg. 3 | «Giolitti cerca un accordo politico con i riformisti di …» | «Ora, Giolitti, ecco qua, parlavamo dei socialisti, il Partito Socialista It…» | +0.0 s |
| Parte 1 · 29:35.82 | arg. 3 | «nel settembre 1904 i massimalisti indicono una grande p…» | «nel settembre del 1904, in occasione del primo sciopero generale nazionale,…» | +0.0 s |
| Parte 2 · 11:02.09 | arg. 7 | «la mentalità dell'epoca relega la donna al ruolo subord…» | «Era uno Stato per i maschi, no? Nonostante i dibattiti e riviste come Lucci…» | -0.0 s |
| Parte 2 · 11:42.59 | arg. 7 | «per frenare il comportamento considerato scandaloso del…» | «o venivano persino internate negli ospedali psichiatrici. In particolare il…» | -0.0 s |
| Parte 2 · 13:56.00 | arg. 8 | «le alte tariffe doganali introdotte dallo Stato protegg…» | «Ma l'età giolittiana è anche, in parallelo a tutto questo,…» | -0.4 s |
| Parte 2 · 15:55.09 | arg. 8 | «nuovi istituti finanziari utilizzano i depositi dei ris…» | «E poi c'è anche il supporto finanziario della banca mista, come la Banca Co…» | -0.0 s |
| Parte 2 · 22:22.77 | arg. 9 | «lo sviluppo economico si concentra quasi esclusivamente…» | «Tuttavia, questo sviluppo, come già accennato,…» | -0.7 s |
| Parte 2 · 24:01.50 | arg. 9 | «gli intellettuali meridionali, tra cui Gaetano Salvemin…» | «Salvemini, Gaetano Salvemini, fu uno storico, ma fu anche un parlamentare, …» | +0.0 s |
| Parte 2 · 35:27.96 | arg. 10 | «con il trattato di Losanna del 1912 l'Italia ottiene la…» | «Ecco, però la guerra coloniale...…» | -1.0 s |
| Parte 2 · 40:33.95 | arg. 11 | «nel giugno 1914 l'uccisione di tre dimostranti ad Ancon…» | «Tre mesi dopo, nel giugno 1914, scoppia la prima guerra mondiale, ma l'Ital…» | -0.0 s |

L'accensione coincide con l'inizio di una frase del prof per costruzione (M: scarto dall'inizio della frase). Che la frase sia davvero quella della card l'hanno giudicato i revisori leggendo la trascrizione: io non l'ho riverificato punto per punto (NV).

## 2. Misure sul video nuovo (M)

### Parte 1
```
durata 2893.24 s = 48:13.24 | fotogrammi 86797 (durata*30=86797) = somma dei pezzi 86797 | peso 249.9 MB | 1920x1080
LUFS -15.2  TP -1.9 dBFS
Q1 atteso 1291.833 trovato 1291.833 scarto -0.000 OK
Q2 atteso 1656.333 trovato 1656.334 scarto +0.001 OK
Q3 atteso 1997.600 trovato 1997.601 scarto +0.001 OK
Q4 atteso 2276.967 trovato 2276.968 scarto +0.001 OK
Q5 atteso 2782.667 trovato 2782.668 scarto +0.001 OK
```
Silenzi > 3 s (−45 dB): 0.
Fermi del prof ≥ 1 s: nessuno.
Fotogramma Quiz ai `quiz_s`: Q1 1291.33s OK, Q2 1655.83s OK, Q3 1997.10s OK, Q4 2276.47s OK, Q5 2782.17s OK.
sha256 (ricomposto dalle parti): `f4a6b5462639a131029eab2213e75eb5fe5ebdba43672472ab272f536b0668f8  Storia_Lez3_Parte1_1080p.mp4`

### Parte 2
```
durata 2802.10 s = 46:42.10 | fotogrammi 84063 (durata*30=84063) = somma dei pezzi 84063 | peso 239.3 MB | 1920x1080
LUFS -15.2  TP -1.9 dBFS
Q6 atteso 597.367 trovato 597.367 scarto +0.000 OK
Q7 atteso 827.500 trovato 827.500 scarto +0.000 OK
Q8 atteso 1334.267 trovato 1334.267 scarto +0.000 OK
Q9 atteso 1794.233 trovato 1794.234 scarto +0.001 OK
Q10 atteso 2267.133 trovato 2267.134 scarto +0.001 OK
Q11 atteso 2691.900 trovato 2691.900 scarto +0.000 OK
```
Silenzi > 3 s (−45 dB): 0.
Fermi del prof ≥ 1 s: nessuno.
Fotogramma Quiz ai `quiz_s`: Q6 596.87s OK, Q7 827.00s OK, Q8 1333.77s OK, Q9 1793.73s OK, Q10 2266.63s OK, Q11 2691.40s OK.
sha256 (ricomposto dalle parti): `ea0895ebf8522597b09d8d4aabd1e6a0e706e98752a0c3f4d148cc0e53d254f1  Storia_Lez3_Parte2_1080p.mp4`

Formato: 1920×1080, 30 fps, x264 veryfast CRF 25, AAC 192 kbps 48 kHz; parlato del prof dall'originale con la catena del kit; voci Kore a −16 LUFS. **Le Parti durano meno dei 50 minuti** (materiale del prof).

## 3. Tabella dei pezzi (sezione C della scheda tecnica) (M)

**Parte 1**

| Pezzo | Presente | Inizio | Durata |
|---|---|---|---|
| 1 · Sigla `SIGLA` | sì | 0:00.00 | 15.0 s |
| 3 · Copertina + benvenuto (voce Kore) `COVERV` | sì | 0:15.00 | 12.4 s |
| 3 · Introduzione del prof (copertina con riquadro) `D0` | sì | 0:27.43 | 149.7 s |
| 4a · Titolo argomento `T1` | sì | 2:57.10 | 4.0 s |
| 4b · Docente + slide `A1` | sì | 3:01.10 | 999.0 s |
| 4c · Approfondimento animato (voce Kore) `AP1` | sì | 19:40.07 | 44.8 s |
| 4e · Pillola di ripasso (introduzione blu) `PI1` | sì | 20:24.87 | 11.2 s |
| 4f · Pillola di ripasso (schema guidato bianco) `PS1` | sì | 20:36.03 | 55.3 s |
| 4g · Scheda Quiz `Q1` | sì | 21:31.33 | 5.0 s |
| 4a · Titolo argomento `T2` | sì | 21:36.33 | 4.0 s |
| 4b · Docente + slide `A2` | sì | 21:40.33 | 223.3 s |
| 4c · Approfondimento animato (voce Kore) `AP2` | sì | 25:23.60 | 54.8 s |
| 4d · Mappa del prof (voce Kore) `MAP1` | sì | 26:18.40 | 33.3 s |
| 4e · Pillola di ripasso (introduzione blu) `PI2` | sì | 26:51.67 | 12.4 s |
| 4f · Pillola di ripasso (schema guidato bianco) `PS2` | sì | 27:04.03 | 31.8 s |
| 4g · Scheda Quiz `Q2` | sì | 27:35.83 | 5.0 s |
| 4a · Titolo argomento `T3` | sì | 27:40.83 | 4.0 s |
| 4b · Docente + slide `A3` | sì | 27:44.83 | 238.4 s |
| 4c · Approfondimento animato (voce Kore) `AP3` | sì | 31:43.27 | 49.1 s |
| 4e · Pillola di ripasso (introduzione blu) `PI3` | sì | 32:32.33 | 12.2 s |
| 4f · Pillola di ripasso (schema guidato bianco) `PS3` | sì | 32:44.53 | 32.6 s |
| 4g · Scheda Quiz `Q3` | sì | 33:17.10 | 5.0 s |
| 4a · Titolo argomento `T4` | sì | 33:22.10 | 4.0 s |
| 4b · Docente + slide `A4` | sì | 33:26.10 | 175.8 s |
| 4c · Approfondimento animato (voce Kore) `AP4` | sì | 36:21.90 | 48.1 s |
| 4e · Pillola di ripasso (introduzione blu) `PI4` | sì | 37:09.97 | 11.3 s |
| 4f · Pillola di ripasso (schema guidato bianco) `PS4` | sì | 37:21.30 | 35.2 s |
| 4g · Scheda Quiz `Q4` | sì | 37:56.47 | 5.0 s |
| 4a · Titolo argomento `T5` | sì | 38:01.47 | 4.0 s |
| 4b · Docente + slide `A5` | sì | 38:05.47 | 391.3 s |
| 4c · Approfondimento animato (voce Kore) `AP5` | sì | 44:36.73 | 53.3 s |
| 4e · Pillola di ripasso (introduzione blu) `PI5` | sì | 45:30.00 | 12.4 s |
| 4f · Pillola di ripasso (schema guidato bianco) `PS5` | sì | 45:42.37 | 39.8 s |
| 4g · Scheda Quiz `Q5` | sì | 46:22.17 | 5.0 s |
| 5 · Glossario `GL` | sì | 46:27.17 | 52.3 s |
| 6 · Riepilogo finale `RIEP` | sì | 47:19.47 | 48.8 s |
| 7 · Finale `FINALE` | sì | 48:08.23 | 5.0 s |

**Parte 2**

| Pezzo | Presente | Inizio | Durata |
|---|---|---|---|
| 1 · Sigla `SIGLA` | sì | 0:00.00 | 15.0 s |
| 3 · Copertina + benvenuto (voce Kore) `COVERV` | sì | 0:15.00 | 48.4 s |
| 4a · Titolo argomento `T6` | sì | 1:03.37 | 4.0 s |
| 4b · Docente + slide `A6` | sì | 1:07.37 | 436.3 s |
| 4c · Approfondimento animato (voce Kore) `AP6` | sì | 8:23.63 | 46.9 s |
| 4e · Pillola di ripasso (introduzione blu) `PI6` | sì | 9:10.50 | 11.5 s |
| 4f · Pillola di ripasso (schema guidato bianco) `PS6` | sì | 9:22.00 | 34.9 s |
| 4g · Scheda Quiz `Q6` | sì | 9:56.87 | 5.0 s |
| 4a · Titolo argomento `T7` | sì | 10:01.87 | 4.0 s |
| 4b · Docente + slide `A7` | sì | 10:05.87 | 139.0 s |
| 4c · Approfondimento animato (voce Kore) `AP7` | sì | 12:24.90 | 39.2 s |
| 4e · Pillola di ripasso (introduzione blu) `PI7` | sì | 13:04.10 | 10.9 s |
| 4f · Pillola di ripasso (schema guidato bianco) `PS7` | sì | 13:14.97 | 32.0 s |
| 4g · Scheda Quiz `Q7` | sì | 13:47.00 | 5.0 s |
| 4a · Titolo argomento `T8` | sì | 13:52.00 | 4.0 s |
| 4b · Docente + slide `A8` | sì | 13:56.00 | 400.9 s |
| 4c · Approfondimento animato (voce Kore) `AP8` | sì | 20:36.87 | 47.8 s |
| 4e · Pillola di ripasso (introduzione blu) `PI8` | sì | 21:24.63 | 12.1 s |
| 4f · Pillola di ripasso (schema guidato bianco) `PS8` | sì | 21:36.77 | 37.0 s |
| 4g · Scheda Quiz `Q8` | sì | 22:13.77 | 5.0 s |
| 4a · Titolo argomento `T9` | sì | 22:18.77 | 4.0 s |
| 4b · Docente + slide `A9` | sì | 22:22.77 | 322.2 s |
| 4c · Approfondimento animato (voce Kore) `AP9` | sì | 27:44.97 | 48.5 s |
| 4d · Mappa del prof (voce Kore) `MAP2` | sì | 28:33.47 | 27.4 s |
| 4e · Pillola di ripasso (introduzione blu) `PI9` | sì | 29:00.90 | 11.2 s |
| 4f · Pillola di ripasso (schema guidato bianco) `PS9` | sì | 29:12.07 | 41.7 s |
| 4g · Scheda Quiz `Q9` | sì | 29:53.73 | 5.0 s |
| 4a · Titolo argomento `T10` | sì | 29:58.73 | 4.0 s |
| 4b · Docente + slide `A10` | sì | 30:02.73 | 360.9 s |
| 4c · Approfondimento animato (voce Kore) `AP10` | sì | 36:03.63 | 50.7 s |
| 4e · Pillola di ripasso (introduzione blu) `PI10` | sì | 36:54.37 | 10.8 s |
| 4f · Pillola di ripasso (schema guidato bianco) `PS10` | sì | 37:05.13 | 41.5 s |
| 4g · Scheda Quiz `Q10` | sì | 37:46.63 | 5.0 s |
| 4a · Titolo argomento `T11` | sì | 37:51.63 | 4.0 s |
| 4b · Docente + slide `A11` | sì | 37:55.63 | 282.0 s |
| 4c · Approfondimento animato (voce Kore) `AP11` | sì | 42:37.60 | 62.4 s |
| 4d · Mappa del prof (voce Kore) `MAP3` | sì | 43:40.00 | 23.4 s |
| 4e · Pillola di ripasso (introduzione blu) `PI11` | sì | 44:03.37 | 13.1 s |
| 4f · Pillola di ripasso (schema guidato bianco) `PS11` | sì | 44:16.47 | 34.9 s |
| 4g · Scheda Quiz `Q11` | sì | 44:51.40 | 5.0 s |
| 5 · Glossario `GL` | sì | 44:56.40 | 50.4 s |
| 6 · Riepilogo finale `RIEP` | sì | 45:46.77 | 50.3 s |
| 7 · Finale `FINALE` | sì | 46:37.10 | 5.0 s |

## 4. Cose che non tornano nel parlato / limiti
- **Durata (M):** Parte 1 48:13 e Parte 2 46:42: sotto i 50 minuti della regola. Il prof parla 69 minuti; con 11 argomenti, pezzi di servizio e card intere non ho modo di arrivare a 50 per Parte senza inventare contenuti o riempire. La master decide se va bene.
- **Slide ferme oltre i 3 minuti (M):** elenco al punto 1 (arg. 1 prima slide 610 s e seconda 379 s; arg. 6 prima slide 320 s; arg. 8 seconda slide 269 s; arg. 10 prima slide 246 s). Con le card intere il prof parla a lungo su pochi punti: non c'è modo di accorciarle senza spezzare le card o inventare contenuti.
- **Introduzione (M):** il prof parla 149,7 s: sotto i 3 minuti, quindi non c'è la slide «Di cosa parliamo».
- Il prof non segue sempre l'ordine delle slide: nei casi dubbi gli allineatori hanno scelto un inizio plausibile. Casi incerti: arg. 1 punto 1 (Adua entra a ~245 s), arg. 4 punto 3 (trasformismo non trattato esplicitamente), arg. 6 punto 3, arg. 11 punto 2 (il Patto Gentiloni non è mai nominato), arg. 9 punti 4 e 5 (esodo prima della politica ambigua). Per questi il bordo giallo può anticipare o ritardare l'argomento (S).
- Le immagini a tempo (pag. 3, 6, 8, 14, 16 del PDF) sono messe quando il prof le mostra.
- Webcam del prof 184×138 ingrandita 2,2× (morbida); testa vicina al bordo alto già nell'originale (S).

## 5. DA CONFERMARE COL PROF / cosa NON ho verificato (NV)
- Gli **approfondimenti** (testi AN della catena precedente, tagliati a fine frase) vanno riletti dal prof o dalla master. Non li ho riverificati frase per frase (NV).
- Voci: tutte Kore (ramo `voci-storia-V-lez03`, già presenti, nessuna nuova richiesta); le 11 voci degli approfondimenti sono le voci AN tagliate a fine frase (controllo della trascrizione sul file tagliato); non le ho riascoltate a orecchio (NV).
- Sottotitoli: parlato del prof corretto a blocchi da revisori automatici (consegna precedente), non riletti per intero; tempi ±0,3 s non misurati (NV). Le voci Kore sono nei sottotitoli.
- PDF slide: stesse immagini del video (S); confronto pagina per pagina con i fotogrammi non fatto (NV). Quiz di argomento riusati (da approvare dalla master).
