# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 2 · La Scapigliatura
**Correzioni 22/11/2026** (terza versione) · stato: REVISIONATA con i limiti in §6 · ogni dato è *misurato*, *stima* o *non verificato*.

## 1. Cosa ho cambiato il 22/11
1. **Slide a card, testo 40 px.** Tutte le slide del prof (e schemi, approfondimenti, glossario, riepilogo) rifatte con card: una frase intera per card, **al massimo 3 card per slide**, testo 40 px interlinea 1,5, card alte quanto il testo, bordo giallo e pallino giallo sulla card in corso (le altre attenuate), pallino numerato. Quando le card non entrano la slide si divide (mai rimpicciolire). La slide cambia anche quando una pagina durerebbe più di 165 s. Nessuna pagina supera 3 minuti (misurato sul manifest: massimo 154 s; fettine del libro massimo 132 s).
2. **Mappa: una sola, quella del prof**, ridisegnata nel modello BES (colori del disciplinare con legenda in alto in ogni schermata). Il testo a 36 px non entra in una schermata (≈ 1300 caratteri): divisa in **2 schermate** («Mappa · 1 di 2», «Mappa · 2 di 2»), come autorizzato dalla master (messaggio 22/11 17:00 UTC). Si costruisce **riquadro per riquadro** con la voce Kore (17 voci RN1–RN17, una per riquadro, il riquadro si accende in giallo mentre la voce parla) e ogni schermata resta ferma 4 s. Posizionata **prima del glossario**, una volta sola. Le 7 mappe nostre e la loro voce sono tolte. La mappa originale del prof (`MAPPE/LEZIONE 2.pdf`) non ha marchio di altri siti né foto dell'autore: nessun elemento da togliere. Parole identiche a quelle del prof; unica disposizione adattata: nella seconda schermata le frecce dai sei princìpi sono verticali tra le righe invece che tutte dal riquadro centrale.
3. **Nome del docente non nelle animazioni.** Nuova voce di benvenuto `INTRO2` senza il nome; tolto il nome dai piè di pagina di titoli, quiz, verifica, compiti, fine, copertina animata e mappa. Il nome compare solo nella fascia gialla (e nel piè di pagina delle slide del prof, come nel modello Spagnolo).
4. **Pause:** nessuna pausa ≥ 2,5 s nel video (prima 2,9 s dopo i jingle di titoli e Quiz): riempite con `trans.wav`.
5. **Mai «già visto»:** la slide «Il culto del vero» compariva in due argomenti; ora le card 1–2 sono nell'argomento 3 e la card 3 («Romanticismo straniero») solo nell'argomento 4.
6. **PDF:** `Letteratura_Lez2_slide.pdf` ora con copertina (solo materia e titolo), piè di pagina materia + pagina (senza nome del docente), tutte le card visibili, testo vero selezionabile (vettoriale); `Letteratura_Lez2_mappe.pdf` con copertina «MAPPE» + le 2 schermate della mappa. Pagine uguali al video (stesso generatore).
7. Resta valido tutto il lavoro del 17/11 (riquadro 4:3, fascia, fettine HD, tagli del prof a fine frase, audio rifatto agganciato ai fotogrammi, jingle Quiz).

## 2. Controllo severo (`controllo_severo.py`, tesseract, passo 10 s)
Esito sull'ultimo video: **RESPINTA**
- copertina: titolo presente e intero, 80 s (limite 180) · durata 55.66 min · loudness -15.2 LUFS · pause > 2,5 s: 0 · slide con lo stesso titolo > 3 min: 0 · schermate identiche > 3 min: 0
- errori residui: ['«…» in 12 campioni', '4 tratti con una card sola oltre 60 s']
- **Card «sola oltre 60 s»**: il controllo conta le card dalle righe che iniziano con 1–3 e sulle pagine a due card legge quasi sempre solo il numero della card in corso. **Controllo sul manifest di montaggio: nessuna pagina con una sola card dura più di 60 s** (massimo 54 s); le pagine a una card sono quelle dell'ultima frase di una slide. Il controllo severo, rilanciato 3 volte con contrasti diversi, resta a 4 tratti: va riguardato dalla master (mia ipotesi: lettura OCR, *non verificata*).
- note: `card_con_puntini` scatta sulle **fettine della poesia** (Preludio), dove il testo del libro ha davvero «…» (es. «ai lembi del Sudario⁶…», «tu puoi morir!⁷…»): falso positivo, il testo del libro non si cambia (segnalato alla master). Le «iniziali minuscole» sono errori di lettura OCR delle etichette (la prima lettera «I»/«Il» scambiata) sulle slide a card.
- Tono della voce del prof (campioni): [152, 164, 160, 148, 148, 176] Hz, chiarezza [1363, 1464, 1543, 1547, 1551, 1439] Hz (soglia 800 Hz): voce non alterata.

## 3. Misure sul video nuovo
| Voce | Valore | Tipo |
|---|---|---|
| Durata / fotogrammi | 55:39,4 · 100 182 fotogrammi (= durata × 30) · 1920×1080 · 268 MB | misurato |
| Volume | −15,2 LUFS integrato (parlato del prof −16,0 LUFS sul file pulito); picco reale −1,2 dBTP | misurato |
| Jingle Quiz (`controllo_jingle.py`) | 7/7 a +0,005 s | misurato |
| Sincronia labbra/voce dei pezzi del prof | audio −20 ms costanti (ritardo AAC), video 0 ms su D1–D7 (5 punti per pezzo): massimo 20 ms | misurato |
| Fermo immagine del riquadro del prof ≥ 1 s | nessuno dentro i pezzi del prof | misurato |
| Pause ≥ 2,5 s | nessuna | misurato |
| Sottotitoli | 927 blocchi; voci Kore col testo esatto, prof da trascrizione automatica con correzioni | misurato / **non riletti per intero** |

### Voci nuove (RN1–RN17, INTRO2): trascrizione e bordi
Bordo = ampiezza massima negli ultimi 50 ms (soglia 0,03; in montaggio ogni voce ha dissolvenza 30 ms in entrata e uscita). «Differenze» = trascrizione automatica confrontata col testo (numeri in lettere ↔ cifre non contano).
| Voce | s | bordo fine | bordo inizio | differenze |
|---|---|---|---|---|
| RN1 | 2.3 | 0.001 | 0.004 | — |
| RN2 | 2.8 | 0.029 | 0.002 | [['1860', 'milleottocentosessanta']] |
| RN3 | 2.5 | 0.0 | 0.002 | — |
| RN4 | 3.7 | 0.001 | 0.002 | — |
| RN5 | 9.9 | 0.001 | 0.001 | [['', 'il'], ['boheme boheme', 'boem boemo']] |
| RN6 | 2.4 | 0.001 | 0.003 | — |
| RN7 | 11.5 | 0.0 | 0.002 | [['gino', 'igino']] |
| RN8 | 11.9 | 0.022 | 0.002 | — |
| RN9 | 5.0 | 0.0 | 0.001 | — |
| RN10 | 7.5 | 0.031 | 0.033 | [['baudelaire', 'bodler']] |
| RN11 | 12.3 | 0.03 | 0.032 | — |
| RN12 | 4.8 | 0.001 | 0.021 | — |
| RN13 | 4.3 | 0.012 | 0.046 | — |
| RN14 | 8.2 | 0.055 | 0.025 | — |
| RN15 | 3.9 | 0.001 | 0.001 | — |
| RN16 | 4.0 | 0.001 | 0.024 | — |
| RN17 | 6.4 | 0.0 | 0.014 | [['patologi', 'patologiche']] |
| INTRO2 | 29.8 | 0.0 | 0.001 | [['5', 'cinque'], ['l80', 'lottanta per cento']] |
Bordi sopra 0,03 (RN10 0,031 · RN11 0,030 · RN14 0,055): tutte le parole sono intere (nessuna differenza di testo) e la dissolvenza di 30 ms le chiude; non rigenerate. «Igino» (RN7) è reso «Gino» dalla trascrizione: da ascoltare.

### Secondi vecchio → nuovo (scheda e timeline già aggiornate)
| Pezzo | vecchio (s) | nuovo (s) |
|---|---|---|
| Q1 | 529.1 | 491.0 |
| Q2 | 740.5 | 668.5 |
| Q3 | 1133.9 | 1028.9 |
| Q4 | 1710.2 | 1545.1 |
| Q5 | 1896.4 | 1696.8 |
| Q6 | 2570.7 | 2332.6 |
| Q7 | 3295.6 | 3006.8 |
| VERIFICA | 3538.4 | 3320.7 |
| COMPITI | 3552.0 | 3334.3 |

### Inizio e fine di ogni pezzo del prof (*stima* dalla trascrizione)
| pezzo | inizio | prime parole | fine | ultime parole | frase finita |
|---|---|---|---|---|---|
| D1 | 0:50.8 | Buongiorno e benvenuti alla lezione sulla | 7:10.3 | organizzato. con manifestazioni teoriche o manifesti codificati. | sì |
| D2 | 8:20.0 | Tra un bel po' di lezioni, | 10:19.3 | tra gli autori, i bersagli della polemica. | sì |
| D3 | 11:17.5 | Ecco, proviamo a parlare di questo | 16:15.3 | sempre uguali, a leggere cose sempre tranquille. | sì |
| D4 | 17:17.9 | Noi vogliom la barriera, ecco, capite | 24:27.8 | andiamo a leggere. almeno alcune di queste. | sì |
| D5 | 25:54.1 | Allora, parliamo di Emilio Praga, come | 27:32.3 | mistero. Vediamo quindi preludio di Emilio Prague. | sì |
| D6 | 28:25.8 | Allora, questa è, come potete vedere, | 36:41.8 | disperazione, e torna ovviamente su questo Podler. | sì |
| D7 | 39:01.6 | Arrigo Boito, dualismo. Come vedete, 1863, | 47:59.8 | e lo capite anche voi. a risolversi. | sì |

## 4. Pagine del libro in HD (fettine)
Sorgente `Lez02_ingrandita.1.zip` → `Lez02/screen/Lez02_p038, 039, 041, 042, 043, 044.png`; ogni fettina inizia e finisce su una riga bianca, solo la colonna del brano, senza intestazioni, numeri di pagina o riquadri. Foglio dei fotogrammi: `controllo_fettine.jpg` (controllate a vista: nessuna riga tagliata).
| Fettina | Pagina | File (rettangolo px) | Minuto video (17/11) |
|---|---|---|---|
| A1 | p. 38 | Lez02/screen/Lez02_p038.png (334,235)-(875,507) | 28:41.6 |
| A2 | p. 38 | Lez02/screen/Lez02_p038.png (503,512)-(1593,731) | 29:41.3 |
| D | p. 38 | Lez02/screen/Lez02_p038.png (845,940)-(1602,1184) | 30:32.6 |
| E | p. 38 | Lez02/screen/Lez02_p038.png (839,1221)-(1573,1462) | 30:47.6 |
| F | p. 38 | Lez02/screen/Lez02_p038.png (761,1502)-(1592,1746) | 31:02.6 |
| G | p. 38 | Lez02/screen/Lez02_p038.png (760,1785)-(1694,2024) | 31:18.6 |
| H | p. 39 | Lez02/screen/Lez02_p039.png (740,232)-(1586,475) | 31:36.1 |
| I | p. 39 | Lez02/screen/Lez02_p039.png (830,511)-(1695,759) | 31:50.6 |
| J | p. 39 | Lez02/screen/Lez02_p039.png (740,794)-(1627,1046) | 32:01.1 |
| K | p. 39 | Lez02/screen/Lez02_p039.png (740,1078)-(1671,1317) | 32:40.6 |
| A2 | p. 38 | Lez02/screen/Lez02_p038.png (503,512)-(1593,731) | 33:33.1 |
| D | p. 38 | Lez02/screen/Lez02_p038.png (845,940)-(1602,1184) | 33:59.6 |
| G | p. 38 | Lez02/screen/Lez02_p038.png (760,1785)-(1694,2024) | 34:47.1 |
| H | p. 39 | Lez02/screen/Lez02_p039.png (740,232)-(1586,475) | 35:33.6 |
| K | p. 39 | Lez02/screen/Lez02_p039.png (740,1078)-(1671,1317) | 36:11.4 |
| S1 | p. 41 | Lez02/screen/Lez02_p041.png (272,1762)-(880,2109) | 39:13.7 |
| S2 | p. 41 | Lez02/screen/Lez02_p041.png (438,2356)-(1113,2765) | 39:43.3 |
| S3 | p. 42 | Lez02/screen/Lez02_p042.png (424,230)-(1047,642) | 40:08.3 |
| S4 | p. 42 | Lez02/screen/Lez02_p042.png (419,680)-(1047,1096) | 40:24.8 |
| S5 | p. 42 | Lez02/screen/Lez02_p042.png (417,1133)-(1011,1543) | 40:41.3 |
| S6 | p. 42 | Lez02/screen/Lez02_p042.png (419,1580)-(1098,1994) | 40:59.8 |
| S7 | p. 42 | Lez02/screen/Lez02_p042.png (418,2034)-(1066,2448) | 41:31.3 |
| S8 | p. 43 | Lez02/screen/Lez02_p043.png (414,232)-(1003,644) | 41:57.3 |
| S9 | p. 43 | Lez02/screen/Lez02_p043.png (414,685)-(1046,1106) | 42:11.3 |
| S10 | p. 43 | Lez02/screen/Lez02_p043.png (417,1143)-(1003,1555) | 42:26.3 |
| S11 | p. 43 | Lez02/screen/Lez02_p043.png (416,1601)-(1073,2013) | 42:39.3 |
| S12 | p. 43 | Lez02/screen/Lez02_p043.png (415,2051)-(1072,2473) | 42:57.8 |
| S13 | p. 43 | Lez02/screen/Lez02_p043.png (417,2507)-(1146,2927) | 43:16.3 |
| S14 | p. 44 | Lez02/screen/Lez02_p044.png (419,218)-(1060,629) | 43:28.8 |
| S15 | p. 44 | Lez02/screen/Lez02_p044.png (421,670)-(1085,1081) | 43:42.3 |
| S16 | p. 44 | Lez02/screen/Lez02_p044.png (402,1122)-(1058,1536) | 43:56.8 |
| S17 | p. 44 | Lez02/screen/Lez02_p044.png (408,1568)-(1074,1982) | 44:12.8 |
| S2 | p. 41 | Lez02/screen/Lez02_p041.png (438,2356)-(1113,2765) | 45:27.8 |
| S6 | p. 42 | Lez02/screen/Lez02_p042.png (419,1580)-(1098,1994) | 47:05.3 |
| S17 | p. 44 | Lez02/screen/Lez02_p044.png (408,1568)-(1074,1982) | 47:48.3 |
(I minuti sono quelli della versione del 17/11: i pezzi D6 e D7 non si sono spostati.)

## 5. Refusi e anomalie nel materiale del prof (da riportare a Sara, non corretti nel contenuto)
- Il prof dice «Gino Ugo Tarchetti», la slide e la mappa «Igino Ugo Tarchetti».
- La mappa elenca «i fratelli Arrigo e Camillo Boito»; le slide parlano solo di Arrigo.
- «Il 6 febbraio 1862» (slide ed Excel) vs «nel 1862» (voce del prof): coerenti.
- Preludio 1864 / Dualismo 1863: il prof si corregge a voce («un po' più avanti… scusate, più dietro»).
- Refusi corretti nelle nostre slide: nomi propri e maiuscole delle card (prima lettera), virgolette; nessun numero toccato.

## 6. Cosa NON ho verificato / limiti
- **Nessun ascolto umano**: pronuncia delle voci Kore (soprattutto «Bohème» reso «Boèm», «Igino», «Baudelaire» reso «Bodlèr») controllata solo con la trascrizione; rumore del prof non ascoltato. Voci Kore già esistenti (R, S, approfondimenti, glossario, riepilogo) non rigenerate: segnalate dalla trascrizione «Manzonismo» (S3, glossario) e «svolazziam» (approfondimento Preludio) da ascoltare.
- **Pause lunghe del prof** (> 2,5 s tra due frasi) non accorciate: il video non ha pause ≥ 2,5 s (misurato), quindi non servivano tagli.
- **Parole chiave** nella colonna destra: non aggiunte (facoltative).
- **Webcam** originale 244×138 px ingrandita ×2,24: morbida; in alcuni punti la testa tocca il bordo alto già nell'originale.
- **Sottotitoli** non riletti per intero; testo delle slide non verificato con OCR parola per parola (preso dal pptx del prof).
- Card con testo a 40 px: alcune pagine hanno una sola card (frase molto lunga): il controllo severo le segnala solo se durano > 60 s.
- Slide extra «Avanguardia e ritardo italiano» (D4, 1077–1226 s dell'originale) scritta con le parole del prof perché nelle sue slide non c'è nulla per quel tratto: **da confermare col prof**.
- Mappa: 2 schermate invece di una (autorizzato dalla master); frecce della 2ª schermata adattate.

## 7. Come ho verificato
`controllo_severo.py` (tesseract), `controllo_jingle.py`, `ebur128`/`silencedetect`/`freezedetect` (ffmpeg), correlazione audio e fotogrammi col file originale per la sincronia, trascrizione `trascrivi.py` (Parakeet) di voci nuove, originale e video, foglio dei fotogrammi ogni 30 s (`controllo_minuti.jpg`) e fettine (`controllo_fettine.jpg`), PDF generati dalle stesse pagine del video. Video: piano per pezzi (49 pezzi), una codifica x264 veryfast CRF 19, AAC 192k, sha256 dei pezzi da 90 MB.
