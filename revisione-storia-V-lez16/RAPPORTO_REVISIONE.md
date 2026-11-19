# RAPPORTO · Storia V · Lezione 16 · Gli anni Sessanta tra crisi e progressi

**Stato: rifatta da zero, Parte unica** sul video originale del prof. Della consegna precedente ho riusato solo le voci Kore già fatte (benvenuto, glossario, riepilogo e saluto) e i quiz (7×5). Ogni affermazione è etichettata **[misurato]**, **[stima]** o **[non verificato]**.

## 1 · Misure sul video

| | Parte unica (argomenti 1–7) |
|---|---|
| Durata | 49:10.6 (2950.6 s) [misurato] |
| Fotogrammi / 30 fps | 88517 = durata×30 [misurato] |
| Formato | 1920×1080, x264 veryfast CRF 19, keyint 60, AAC 192k 48 kHz [misurato] |
| Peso | 373,7 MB [misurato] |
| Loudness integrata (file finale) | −16,7 LUFS [misurato] |
| Picco (true peak, file finale) | −4,1 dBFS [misurato] (limite −1) |
| Parlato del prof (mediana dei pezzi) | −16,3 LUFS [misurato] |
| Scatto `quiz.wav` | 7 quiz a +0,005 s dall'atteso [misurato, controllo_jingle.py] |
| Fermi immagine del prof ≥ 1 s | nessuno [misurato, controllo_finale.py] |
| Sfasamento audio/labbra | −15 ms (correlazione dell'inviluppo, 3 punti: min 5, 20, 33) [misurato, limite 40 ms] |
| Sottotitoli: attacco sulla voce entro 0,3 s | 94% di 16 blocchi verificabili (soglia 80%) [misurato] |
| sha256 | vedi `.sha256`; ricomponendo i `.parte_NN` coincide [misurato] |

Uscita integrale di `controllo_finale.py`:

```
durata 49:10.6 (2950.6 s) | fotogrammi 88517 (attesi 88517) OK | peso 373.7 MB (356.4 MiB) OK | 1920x1080 OK
quiz 7 scatto 0,0 s: OK
fermi immagine nei pezzi del docente: nessuno OK
volume del parlato (mediana dei pezzi del docente): -16.3 LUFS OK
sottotitoli: 679 blocchi, sovrapposti 0, oltre la fine 0, attacco sulla voce entro 0,3 s: 94% di 16 verificabili OK
foglio di miniature: out/Storia_Lez16_Parte1_1080p.mp4.miniature.jpg
ESITO: TUTTO OK
```

## 2 · Tabella dei pezzi (sezione C della scheda tecnica)

| Pezzo | Presente | Minuto | Durata misurata |
|---|---|---|---|
| 1 · Sigla | sì | 0:00.0 | 15.0 s |
| 3 · Copertina + voce di benvenuto | sì | 0:13.6 | 13.7 s |
| 3 · Introduzione del prof sulla copertina (riquadro del prof) | sì | 0:26.9 | 130.7 s |
| 4a · Titolo argomento 1 | sì | 2:37.2 | 4.0 s |
| 4b · Prof + slide argomento 1 | sì | 2:40.8 | 16.8 s |
| 4c · Approfondimenti animati argomento 1 | no (non necessari: il prof copre già tutto) | – | – |
| 4d · Mappa del prof argomento 1 | no (il prof non ha mappa per questo argomento: non inventata) | – | – |
| 4e · Pillola di ripasso argomento 1 | sì | 2:57.2 | 7.9 s |
| 4f · Schema guidato argomento 1 | sì | 3:04.7 | 38.9 s |
| 4g · Scheda Quiz 1 | sì | 3:43.2 | 5.0 s |
| 4a · Titolo argomento 2 | sì | 3:47.8 | 4.0 s |
| 4b · Prof + slide argomento 2 | sì | 3:51.4 | 530.2 s |
| 4c · Approfondimenti animati argomento 2 | no (non necessari: il prof copre già tutto) | – | – |
| 4d · Mappa del prof argomento 2 | no (il prof non ha mappa per questo argomento: non inventata) | – | – |
| 4e · Pillola di ripasso argomento 2 | sì | 12:41.2 | 8.1 s |
| 4f · Schema guidato argomento 2 | sì | 12:48.9 | 32.9 s |
| 4g · Scheda Quiz 2 | sì | 13:21.4 | 5.0 s |
| 4a · Titolo argomento 3 | sì | 13:26.0 | 4.0 s |
| 4b · Prof + slide argomento 3 | sì | 13:29.6 | 399.8 s |
| 4c · Approfondimenti animati argomento 3 | no (non necessari: il prof copre già tutto) | – | – |
| 4d · Mappa del prof argomento 3 | no (il prof non ha mappa per questo argomento: non inventata) | – | – |
| 4e · Pillola di ripasso argomento 3 | sì | 20:09.0 | 8.2 s |
| 4f · Schema guidato argomento 3 | sì | 20:16.8 | 33.0 s |
| 4g · Scheda Quiz 3 | sì | 20:49.4 | 5.0 s |
| 4a · Titolo argomento 4 | sì | 20:54.0 | 4.0 s |
| 4b · Prof + slide argomento 4 | sì | 20:57.6 | 443.5 s |
| 4c · Approfondimenti animati argomento 4 | no (non necessari: il prof copre già tutto) | – | – |
| 4d · Mappa del prof argomento 4 | no (il prof non ha mappa per questo argomento: non inventata) | – | – |
| 4e · Pillola di ripasso argomento 4 | sì | 28:20.7 | 7.7 s |
| 4f · Schema guidato argomento 4 | sì | 28:28.0 | 33.4 s |
| 4g · Scheda Quiz 4 | sì | 29:01.0 | 5.0 s |
| 4a · Titolo argomento 5 | sì | 29:05.6 | 4.0 s |
| 4b · Prof + slide argomento 5 | sì | 29:09.2 | 536.0 s |
| 4c · Approfondimenti animati argomento 5 | no (non necessari: il prof copre già tutto) | – | – |
| 4d · Mappa del prof (USA anni Sessanta) argomento 5 | sì | 38:04.8 | 39.0 s |
| 4e · Pillola di ripasso argomento 5 | sì | 38:43.4 | 7.9 s |
| 4f · Schema guidato argomento 5 | sì | 38:50.9 | 25.8 s |
| 4g · Scheda Quiz 5 | sì | 39:16.3 | 5.0 s |
| 4a · Titolo argomento 6 | sì | 39:20.9 | 4.0 s |
| 4b · Prof + slide argomento 6 | sì | 39:24.5 | 133.7 s |
| 4c · Approfondimenti animati argomento 6 | no (non necessari: il prof copre già tutto) | – | – |
| 4d · Mappa del prof (mondo socialista) argomento 6 | sì | 41:37.8 | 32.7 s |
| 4d · Mappa del prof (Medio Oriente) argomento 6 | sì | 42:10.1 | 25.4 s |
| 4e · Pillola di ripasso argomento 6 | sì | 42:35.0 | 10.3 s |
| 4f · Schema guidato argomento 6 | sì | 42:44.9 | 26.0 s |
| 4g · Scheda Quiz 6 | sì | 43:10.5 | 5.0 s |
| 4a · Titolo argomento 7 | sì | 43:15.1 | 4.0 s |
| 4b · Prof + slide argomento 7 | sì | 43:18.7 | 238.0 s |
| 4c · Approfondimenti animati argomento 7 | no (non necessari: il prof copre già tutto) | – | – |
| 4d · Mappa del prof argomento 7 | no (il prof non ha mappa per questo argomento: non inventata) | – | – |
| 4e · Pillola di ripasso argomento 7 | sì | 47:16.3 | 8.6 s |
| 4f · Schema guidato argomento 7 | sì | 47:24.5 | 34.6 s |
| 4g · Scheda Quiz 7 | sì | 47:58.7 | 5.0 s |
| 5 · Glossario | sì | 48:03.3 | 35.2 s |
| 6 · Riepilogo finale + saluto | sì | 48:38.1 | 27.9 s |
| 7 · Finale 5 s | sì | 49:05.6 | 5.0 s |

`trans.wav` + dissolvenza (0,4 s; 1,4 s dopo la sigla) a ogni cambio di pezzo [per costruzione]; `titolo.wav`, `repaso.wav`, `quiz.wav` (+0,5 s), `finale.wav` [per costruzione; il solo scatto del quiz è misurato].

## 3 · Confronto con Spagnolo Lez. 1

Immagine: `confronto_Spagnolo.jpg`. Schede blu fatte SOLO con `schede_spagnolo.py` a scala 1.0 [misurato]. Differenze dichiarate:

- Pillola blu: 7,7–10,3 s invece di 14 s; il testo mostrato è la frase della voce, parola per parola.
- Schema guidato: 26–39 s invece di ≈46 s.
- Riepilogo finale + saluto: 28 s [nei limiti].
- Pannello «PAROLE CHIAVE»: aggiunta approvata, tenuta. Approfondimenti 4c: non fatti.
- Mappe del prof: 3 (USA, mondo socialista, Medio Oriente), tutte e tre collocate dopo gli argomenti 5 e 6 (dove il prof ne tratta i temi); per gli altri argomenti il prof non ne ha mandate.
- L'argomento 1 («L'età del benessere») è breve: il prof ne parla per 16 secondi e passa a Kennedy; la pillola e lo schema ripetono la slide.

## 4 · Controlli obbligatori del prompt v3

- **Chip**: «Baby boom · Welfare State · Bretton Woods», «Kennedy · Martin Luther King · Dallas 1963», «Johnson · Civil Rights Act · Voting Rights Act», «Sputnik · Gagarin · Apollo 11», «Muro di Berlino · Cuba · Vietnam», «Chruščëv · Brežnev · Primavera di Praga», «Hippy · Femminismo · Vietnam» [misurato a vista nel `foglio.png`].
- **Didascalia pillola** = testo della voce Kore parola per parola (da `testi_voci.json`) [misurato: `foglio.png`, 2 didascalie per pillola].
- **Argomento lungo** nel quiz: `tfs` ricalcolato sulla lunghezza: nessun titolo tocca il pulsante play [misurato a vista].
- **Riepilogo finale**: ultimo fotogramma con TUTTE e 7 le card [misurato a vista].
- **Nomi e titoli** uguali in schede, quiz (`quiz_argomenti.json` aggiornato), copertina, slide [misurato a vista].
- **Foglio di controllo**: `foglio.png`. **Tempi**: i Quiz cadono ai `quiz_s` della scheda di pubblicazione (+0,005 s) [misurato].

## 5 · Problemi trovati e correzioni

| Minuto | Tipo | Com'era | Correzione |
|---|---|---|---|
| Tutto | testo | Trascrizione automatica con errori sui nomi («Khrushchev», «Briesnev», «Lindon Johnson», «Civil Rights Heads»…) e disturbi | Correzioni automatiche per regole (nomi, date) e righe di disturbo tolte (`subs_fix_sottotitoli.py`) |
| Argomento 3 | visivo | ~195 s di parlato sulla successione a Johnson senza una card dedicata | Resta accesa la card «Fine tragica» di Kennedy (dalla stessa slide), nessuna card inventata |
| Argomento 5, min 24:00–29:00 | altro | ~260 s del prof sulla strategia del contenimento (terzo mondo, dottrina Truman) senza card nella slide | Slide ferma senza card accesa: segnalato qui, nessuna card inventata |
| Argomento 5 | visivo | Carta del Vietnam della slide | Mostrata dal prof a 1854 s del suo video, a tempo con il parlato |

## 6 · DA CONFERMARE COL PROF

1. Date: la mappa dice Vietnam 1964-1973, la carta della slide 1966-1975; le schede riportano le date della mappa (voce di lettura) e della carta (titolo della pagina).

## 7 · Cosa NON ho verificato

- **I sottotitoli NON sono stati riletti riga per riga**: ho applicato solo correzioni automatiche per regole (nomi, date, disturbi) sul testo della trascrizione; molte frasi della trascrizione automatica restano imprecise [non verificato].
- Webcam: 184×138 px ingrandita 2,2×: **morbida**; testa tagliata in alto nell'originale [misurato a vista].
- PDF slide (24 pagine) e mappe (3 pagine): stessa grafica del video senza riquadro (il pannello «PAROLE CHIAVE» resta); **non** ho confrontato pagina per pagina con i fotogrammi [non verificato].
- Quiz: 35 quesiti nel ramo `voci-…`, riletti solo a campione [non verificato]. Verifica = Excel del prof (10 domande) invariato; compiti = PDF del prof (4 domande) invariato [misurato].
- L'allineamento delle card al parlato è fatto con un confronto automatico di parole chiave, controllato a mano solo sui punti con più dubbi [stima].
- Suono `trans.wav` ai confini: per costruzione, non ascoltato [non verificato].

## 8 · Come ho verificato

Trascrizione con `trascrivi.py` (361 segmenti); audio del prof rifatto dall'originale con la catena del kit; `controllo_finale.py`, `controllo_jingle.py`, ebur128; fotogrammi ogni 30 s (`controllo_minuti_Parte1.jpg`), `foglio.png`, `confronto_Spagnolo.jpg`.

## 9 · Tempi nel video nuovo

Durata 2950.567 s: arg. 1 «L'età del benessere»: inizio 157.233 s, quiz 223.167 s; arg. 2 «Kennedy e la Nuova Frontiera»: inizio 227.767 s, quiz 801.367 s; arg. 3 «Johnson e la Great Society»: inizio 805.967 s, quiz 1249.4 s; arg. 4 «La corsa allo spazio»: inizio 1254.0 s, quiz 1741.0 s; arg. 5 «I punti di attrito della guerra fredda»: inizio 1745.6 s, quiz 2356.3 s; arg. 6 «Il blocco sovietico da Chruščëv a Brežnev»: inizio 2360.9 s, quiz 2590.5 s; arg. 7 «Il Sessantotto: una protesta globale»: inizio 2595.1 s, quiz 2878.667 s

La durata è cambiata rispetto alla consegna precedente (53 minuti): i secondi vecchi non valgono più.
