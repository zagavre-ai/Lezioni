# RAPPORTO DI REVISIONE · Storia V · Lezione 5 · La Rivoluzione russa e la nascita dell'URSS (prof. Giorgio Mazzotti)

**Correzioni 19/11 fatte** (8 punti della master) sulla lezione 5, in 2 Parti. Rifatti da zero, dal video originale del prof (release `mazzotti-storia-V`, zip 007), slide, mappe, approfondimenti, schema, transizioni e schede blu; riusati le voci Kore già fatte (ramo `voci-storia-V-lez05`) e i quiz. Aggiunte 4 voci nuove (MA1–MA4) per le mappe del prof. Ogni valore è etichettato **[misurato]**, **[stima]** o **[non verificato]**.

## 1. Misure sul video nuovo

| | Parte 1 (argomenti 1–4) | Parte 2 (argomenti 5–9) |
|---|---|---|
| Durata [misurato] | 44:33.2 (2673.2 s) | 35:00.4 (2100.4 s) |
| Fotogrammi [misurato] | 80196 = durata × 30 | 63011 = durata × 30 |
| Formato [misurato] | 1920×1080, 30 fps, H.264 veryfast CRF 20, AAC 192k 48 kHz | 1920×1080, 30 fps, H.264 veryfast CRF 20, AAC 192k 48 kHz |
| Peso [misurato] | 302.7 MB | 266.2 MB |
| Parlato [misurato] | −17,4 LUFS, picco −2,1 dBFS (limite −1) | −17,7 LUFS, picco −2,1 dBFS (limite −1) |
| Fermi del prof ≥ 1 s [misurato, freezedetect −55 dB] | 0 | 0 |
| Jingle Quiz [misurato, controllo_jingle.py] | Q1–Q4 scarto ≤ 0,008 s, OK | Q5–Q9 scarto ≤ 0,008 s, OK |
| Silenzi > 3 s [misurato, −45 dB] | 2 di 3,0–3,5 s (tenuta di 2,8 s a fine schema + coda della voce) | 9 di 3,0–3,8 s (stesso motivo); nessuno più lungo |
| sha256 | `4ee66c5b2a22ca5d75e0ff263ce1f7ba95c5bd6871e792bea675e1a42a2616a9` | `6c8d8df5bc39caafc43b53022e52ecf51481960ceae125f6448a613802f977fc` |

Video a pezzi `.parte_NN` (ricomporre con `cat Storia_Lez5_ParteK_1080p.mp4.parte_* > Storia_Lez5_ParteK_1080p.mp4`) + `.sha256`. Il numero della lezione non compare nel video [misurato a vista]. Parlato a −17,4/−17,7 LUFS: dentro −16 ± 2, ma più basso di prima perché ho abbassato il limitatore per stare sotto −1 dBFS.

## 2. Tabella C della scheda tecnica (presente · minuto di inizio nella Parte · durata misurata)

### Parte 1

| Pezzo | Presente | Inizio | Durata |
|---|---|---|---|
| 1 · Sigla | sì | 0:00.0 | 15.0 s |
| 3 · Copertina + benvenuto (voce Kore) | sì | 0:15.0 | 13.0 s |
| 3 · Copertina + introduzione del prof (con il percorso dei 9 argomenti) | sì | 0:28.0 | 194.4 s |
| **Argomento 1: La crisi della Russia zarista** | | | |
| 4a · Titolo (4 s, titolo.wav) | sì | 3:42.4 | 4.0 s |
| 4b · Docente + slide (max 3 card per slide) | sì | 3:46.4 | 343.3 s |
| 4c · Approfondimento animato (voce Kore) | sì | 9:29.7 | 61.6 s |
| 4d · Mappa del prof | no: il PDF del prof ha 4 mappe (argomenti 2, 4, 6, 8) | – | – |
| 4e · Pillola, introduzione blu (repaso.wav) | sì | 10:31.3 | 8.3 s |
| 4f · Pillola, schema guidato (4–5 righe) | sì | 10:39.6 | 27.1 s |
| 4g · Scheda Quiz (quiz.wav a +0,5 s) | sì | 11:06.7 | 5.0 s |
| **Argomento 2: La Rivoluzione di Febbraio (1917)** | | | |
| 4a · Titolo (4 s, titolo.wav) | sì | 11:11.7 | 4.0 s |
| 4b · Docente + slide (max 3 card per slide) | sì | 11:15.7 | 510.5 s |
| 4c · Approfondimento animato (voce Kore) | sì | 19:46.2 | 51.8 s |
| 4d · Mappa del prof (ridisegnata con mappa.py) | sì | 20:37.9 | 26.9 s |
| 4e · Pillola, introduzione blu (repaso.wav) | sì | 21:04.8 | 8.3 s |
| 4f · Pillola, schema guidato (4–5 righe) | sì | 21:13.1 | 25.0 s |
| 4g · Scheda Quiz (quiz.wav a +0,5 s) | sì | 21:38.1 | 5.0 s |
| **Argomento 3: Dualismo di potere e Lenin** | | | |
| 4a · Titolo (4 s, titolo.wav) | sì | 21:43.1 | 4.0 s |
| 4b · Docente + slide (max 3 card per slide) | sì | 21:47.1 | 511.3 s |
| 4c · Approfondimento animato (voce Kore) | sì | 30:18.4 | 48.6 s |
| 4d · Mappa del prof | no: il PDF del prof ha 4 mappe (argomenti 2, 4, 6, 8) | – | – |
| 4e · Pillola, introduzione blu (repaso.wav) | sì | 31:07.0 | 9.3 s |
| 4f · Pillola, schema guidato (4–5 righe) | sì | 31:16.4 | 28.8 s |
| 4g · Scheda Quiz (quiz.wav a +0,5 s) | sì | 31:45.2 | 5.0 s |
| **Argomento 4: Dalle giornate di luglio a Ottobre** | | | |
| 4a · Titolo (4 s, titolo.wav) | sì | 31:50.2 | 4.0 s |
| 4b · Docente + slide (max 3 card per slide) | sì | 31:54.2 | 547.8 s |
| 4c · Approfondimento animato (voce Kore) | sì | 41:02.0 | 56.1 s |
| 4d · Mappa del prof (ridisegnata con mappa.py) | sì | 41:58.0 | 17.1 s |
| 4e · Pillola, introduzione blu (repaso.wav) | sì | 42:15.2 | 10.0 s |
| 4f · Pillola, schema guidato (4–5 righe) | sì | 42:25.1 | 25.1 s |
| 4g · Scheda Quiz (quiz.wav a +0,5 s) | sì | 42:50.2 | 5.0 s |
| 5 · Glossario (8 termini) | sì | 42:55.2 | 57.4 s |
| 6 · Riepilogo finale | sì | 43:52.7 | 35.5 s |
| 7 · Finale (5 s) | sì | 44:28.2 | 5.0 s |

### Parte 2

| Pezzo | Presente | Inizio | Durata |
|---|---|---|---|
| 1 · Sigla | sì | 0:00.0 | 15.0 s |
| 3 · Copertina + benvenuto (voce Kore) | sì | 0:15.0 | 9.5 s |
| Ripasso della Parte 1 (voce RIP2) | sì | 0:24.5 | 62.0 s |
| **Argomento 5: I primi provvedimenti bolscevichi** | | | |
| 4a · Titolo (4 s, titolo.wav) | sì | 1:26.6 | 4.0 s |
| 4b · Docente + slide (max 3 card per slide) | sì | 1:30.6 | 260.7 s |
| 4c · Approfondimento animato (voce Kore) | sì | 5:51.3 | 64.2 s |
| 4d · Mappa del prof | no: il PDF del prof ha 4 mappe (argomenti 2, 4, 6, 8) | – | – |
| 4e · Pillola, introduzione blu (repaso.wav) | sì | 6:55.4 | 8.4 s |
| 4f · Pillola, schema guidato (4–5 righe) | sì | 7:03.8 | 27.0 s |
| 4g · Scheda Quiz (quiz.wav a +0,5 s) | sì | 7:30.8 | 5.0 s |
| **Argomento 6: Brest-Litovsk e la guerra civile** | | | |
| 4a · Titolo (4 s, titolo.wav) | sì | 7:35.8 | 4.0 s |
| 4b · Docente + slide (max 3 card per slide) | sì | 7:39.8 | 360.8 s |
| 4c · Approfondimento animato (voce Kore) | sì | 13:40.6 | 58.9 s |
| 4d · Mappa del prof (ridisegnata con mappa.py) | sì | 14:39.6 | 22.2 s |
| 4e · Pillola, introduzione blu (repaso.wav) | sì | 15:01.7 | 9.4 s |
| 4f · Pillola, schema guidato (4–5 righe) | sì | 15:11.1 | 28.0 s |
| 4g · Scheda Quiz (quiz.wav a +0,5 s) | sì | 15:39.1 | 5.0 s |
| **Argomento 7: Il «Comunismo di guerra»** | | | |
| 4a · Titolo (4 s, titolo.wav) | sì | 15:44.1 | 4.0 s |
| 4b · Docente + slide (max 3 card per slide) | sì | 15:48.1 | 177.7 s |
| 4c · Approfondimento animato (voce Kore) | sì | 18:45.8 | 55.7 s |
| 4d · Mappa del prof | no: il PDF del prof ha 4 mappe (argomenti 2, 4, 6, 8) | – | – |
| 4e · Pillola, introduzione blu (repaso.wav) | sì | 19:41.5 | 8.2 s |
| 4f · Pillola, schema guidato (4–5 righe) | sì | 19:49.7 | 29.9 s |
| 4g · Scheda Quiz (quiz.wav a +0,5 s) | sì | 20:19.5 | 5.0 s |
| **Argomento 8: La Nuova Politica Economica (NEP)** | | | |
| 4a · Titolo (4 s, titolo.wav) | sì | 20:24.5 | 4.0 s |
| 4b · Docente + slide (max 3 card per slide) | sì | 20:28.5 | 245.9 s |
| 4c · Approfondimento animato (voce Kore) | sì | 24:34.4 | 60.6 s |
| 4d · Mappa del prof (ridisegnata con mappa.py) | sì | 25:35.1 | 21.5 s |
| 4e · Pillola, introduzione blu (repaso.wav) | sì | 25:56.6 | 8.2 s |
| 4f · Pillola, schema guidato (4–5 righe) | sì | 26:04.8 | 26.7 s |
| 4g · Scheda Quiz (quiz.wav a +0,5 s) | sì | 26:31.5 | 5.0 s |
| **Argomento 9: La nascita dell'URSS e la successione** | | | |
| 4a · Titolo (4 s, titolo.wav) | sì | 26:36.5 | 4.0 s |
| 4b · Docente + slide (max 3 card per slide) | sì | 26:40.5 | 270.9 s |
| 4c · Approfondimento animato (voce Kore) | sì | 31:11.4 | 54.8 s |
| 4d · Mappa del prof | no: il PDF del prof ha 4 mappe (argomenti 2, 4, 6, 8) | – | – |
| 4e · Pillola, introduzione blu (repaso.wav) | sì | 32:06.2 | 9.8 s |
| 4f · Pillola, schema guidato (4–5 righe) | sì | 32:16.0 | 27.3 s |
| 4g · Scheda Quiz (quiz.wav a +0,5 s) | sì | 32:43.3 | 5.0 s |
| 5 · Glossario (8 termini) | sì | 32:48.3 | 73.3 s |
| 6 · Riepilogo finale | sì | 34:01.6 | 53.8 s |
| 7 · Finale (5 s) | sì | 34:55.4 | 5.0 s |

## 3. Correzioni della master 19/11 (8 punti)

| # | Punto | Esito |
|---|---|---|
| 1 | Max 3 card per slide; nessuna slide ferma oltre 3 minuti | fatto: 24 slide del prof (invece di 9), 1–3 card ciascuna, ordinate come parla il prof; la più lunga resta 177 s (3a, 1048–1225 s dell'originale) [misurato]. Dove la slide del prof aveva 4–5 card ma il prof ne tratta una per 150–250 s, ho diviso la slide in più slide; 3 card sono mie e riprendono le parole del prof: «Dalla Repubblica all'insurrezione» (1830–1981 s) e il diritto delle donne spostato nell'argomento 5 (il prof ne parla a 2198 s con la slide 8 sullo schermo). Slide delle immagini del prof (Lenin, Trockij, carta di Brest-Litovsk, carta dell'URSS) mostrate a tempo con la voce |
| 2 | Sincronia ±1 s | fatto: ogni card si accende alla prima parola della frase del prof (tempi parola per parola); 46 punti controllati, scarto massimo 0,94 s [misurato]; 12 a caso nella tabella sotto |
| 3 | Mappe ridisegnate con mappa.py | fatto: 4 mappe del prof (PDF MAPPE, 4 pagine) → `mappa.py`, rami a tempo con le nuove voci MA1–MA4. Il tool ha solo la forma «centro + rami»: l'albero del prof è stato ridotto a 3 rami con le stesse parole |
| 4 | Approfondimento animato per argomento, voce Kore | fatto: 9 (uno per argomento, 55–64 s); per gli argomenti 6 e 9 la voce legge la carta (Brest-Litovsk, URSS) mostrata a schermo |
| 5 | Schema di ripasso 4–6 righe | fatto: 4 righe (5 per l'argomento 7) |
| 6 | trans.wav + dissolvenza a ogni cambio di pezzo | fatto: trans.wav a ogni inizio di pezzo, dissolvenza 0,3 s (0,8 s sigla→copertina; 0,3 s anche slide→slide dentro il prof) [non rimisurato sul file finale] |
| 7 | Copertina: titolo esatto, card ARGOMENTI senza sovrapposizioni | OK: titolo su 2 righe, la card (9 argomenti) scende sotto; nessuna sovrapposizione. La Parte 2 ha la stessa copertina con «PARTE 2» |
| 8 | Avviso diritti in basso al centro, bianco 24 px, senza riquadro, mai sopra il piè | fatto: bianco sulla sigla (ultimi 2 s); sulla copertina bianca resta 3 s grigio-blu 24 px sopra la linea del piè (il bianco non si vedrebbe) |

### Controllo sincronia (12 punti a caso)

| Card | acceso a (s, originale) | frase del prof inizia a | scarto | frase |
|---|---|---|---|---|
| D1 · S1a_2 | 217.1 | 217.09 | +0.01 s | Nonostante l'enorme esercito russo si fosse mobi… |
| D1 · S1b_1 | 372.6 | 372.61 | -0.01 s | In questo contesto di profonda crisi sociale… |
| D2 · S2c_1 | 760.6 | 760.65 | -0.05 s | portando alla quindi lo zar nel corso poi delle … |
| D3 · S3b_1 | 1232.4 | 1232.42 | -0.02 s | Il principale elemento di divergenza tra i due p… |
| D4 · S4a_2 | 1621.2 | 1621.19 | +0.01 s | A luglio a seguito di questi eventi il principe … |
| D4 · S4b_1 | 1663.5 | 1663.53 | -0.03 s | Veramente a dura prova da tutto, fu messo ulteri… |
| D5 · S5a_2 | 2179.4 | 2179.43 | -0.03 s | Nazionalizzazione economica decretò… |
| D5 · S5a_3 | 2198.0 | 2197.99 | +0.01 s | E poi le riforme sociali e di genere. La nuova c… |
| D6 · S6c_1 | 2610.2 | 2610.21 | -0.01 s | Nel luglio del 1918, nel corso appunto della gue… |
| D7 · S7b_1 | 2793.6 | 2793.64 | -0.04 s | Parte del governo, dello stato comunista e la re… |
| D8 · S8b_3 | 3121.7 | 3121.7 | +0.00 s | La denazionalizzazione delle piccole imprese ind… |
| D9 · S9a_2 | 3216.4 | 3216.42 | -0.02 s | La costituzione sovietica, a questo punto, non p… |

## 4. Confronto col modello Spagnolo

Schede blu fatte SOLO con `schede_spagnolo.py` (scala 1.0): titoli, pillole, Quiz, riepilogo, ripasso. `foglio_Parte1.png` e `foglio_Parte2.png`: un fotogramma di ogni titolo, di ogni pillola (intro e didascalia), di ogni Quiz e del riepilogo (ultimo fotogramma, con tutti gli argomenti della Parte) e del ripasso di apertura della Parte 2. `confronto_spagnolo.png`: i pezzi accanto a quelli di Spagnolo. Font solo Bricolage 800 e Figtree; Quiz con `tfs` ridotto (nessun titolo tocca il play); didascalie delle pillole = testo della voce Kore parola per parola. Chip dei titoli: parole chiave vere (es. «Nicola II · Duma · Rasputin», «Kerenskij · Kornilov · Guardie rosse»).

## 5. Problemi trovati e correzioni

| Minuto | Tipo | Com'era | Correzione |
|---|---|---|---|
| Parte 1/2, tutti | visivo | una sola slide per argomento per 8–16 minuti; nessun approfondimento; mappe fatte da noi o assenti | vedi §3 |
| Parte 1/2 | audio | pillola blu di 9 s ma schema di 33 s con silenzi | pillola 8–10 s con la voce P1–P9 e schema a righe, nessun silenzio > 3,8 s |
| Verifica finale, domanda 5 | pagina | le 4 risposte erano date «2026-10-25 00:00:00»… (Excel aveva trasformato le date) | lette come «25 ottobre», «23 febbraio», «15 settembre», «18 gennaio»; domanda 10: anni come testo. Testo del prof invariato |
| Sottotitoli | testo | strumento automatico con errori | trascrizione nuova + ~25 regole di correzione (Trockij, Rasputin, Kerenskij, Kornilov, L'vov, Romanov, URSS, Čeka…); tolti i riempitivi («Uh», «All right») |

### Secondo vecchio → secondo nuovo

| Argomento | inizio_s vecchio | nuovo | quiz_s vecchio | nuovo |
|---|---|---|---|---|
| 1 · La crisi della Russia zarista (P1) | 220.233 | 222.367 | 608.367 | 666.7 |
| 2 · La Rivoluzione di Febbraio (1917) (P1) | 612.967 | 671.7 | 1235.933 | 1298.1 |
| 3 · Dualismo di potere e Lenin (P1) | 1240.533 | 1303.1 | 1756.733 | 1905.167 |
| 4 · Dalle giornate di luglio a Ottobre (P1) | 1761.333 | 1910.167 | 2372.0 | 2570.233 |
| 5 · I primi provvedimenti bolscevichi (P2) | 84.633 | 86.567 | 405.333 | 450.833 |
| 6 · Brest-Litovsk e la guerra civile (P2) | 409.933 | 455.833 | 863.967 | 939.1 |
| 7 · Il «Comunismo di guerra» (P2) | 868.567 | 944.1 | 1025.167 | 1219.533 |
| 8 · La Nuova Politica Economica (NEP) (P2) | 1029.767 | 1224.533 | 1375.133 | 1591.5 |
| 9 · La nascita dell'URSS e la successione (P2) | 1379.733 | 1596.5 | 1695.3 | 1963.333 |

durata_s: Parte 1 2486.933 → 2673.2; Parte 2 1841.4 → 2100.367.

## 6. DA CONFERMARE COL PROF

- La slide dice «20 dicembre 1922» come data di nascita dell'URSS, il prof dice a voce «30 dicembre 1922». Nella scheda dei punti chiave e nella voce SC9_1 resta «20 dicembre» (come la slide e come le voci già fatte).
- La slide dell'argomento 8 dice «organo di repressione repressivo speciale (la Čeka)»: refuso del PDF, riportato com'è (i testi del prof non si toccano).
- Nella slide 6 il prof dice a voce che l'ordine dell'uccisione della famiglia reale è discusso fra gli storici: non c'è nella slide.
- Il prof dice «Ramanov» (pronuncia): i sottotitoli riportano «Romanov».

## 7. Cosa NON ho verificato

- Sottotitoli: trascrizione automatica corretta con regole, NON riascoltata parola per parola: possono restare errori nel parlato spontaneo.
- Sincronia labbra e fruscio/ronzio dopo arnndn: non ascoltati.
- Pronuncia delle voci Kore (ESITI.txt: tutte «OK»).
- Le card sono accese all'inizio della frase che le introduce; per alcune (es. 2926 s, 2787 s) il prof passa alla card nel mezzo di un segmento: scarto fino a 0,94 s.
- Non ho verificato ogni «ecco la foto/la carta» del parlato: ho messo le 4 immagini del PDF dove il prof le nomina (Lenin 1549 s, Trockij 2102 s, carta di Brest-Litovsk 3369 s, carta dell'URSS 3389 s).
- Voci FIN1/FIN2 (saluti a fine Parte) non montate: la scheda tecnica 18/11 prevede solo il finale da 5 s.

## 8. Come ho verificato

- Trascrizione dell'originale (`trascrivi.py`), cambi slide del prof dalla differenza tra fotogrammi, tempi delle card dalle parole del prof.
- Misure: ffprobe, ebur128, freezedetect sul riquadro, silencedetect, `controllo_jingle.py`.
- A vista: foglio_Parte1/2.png, controllo_minuti_Parte1/2.jpg (1 fotogramma ogni 30 s).
