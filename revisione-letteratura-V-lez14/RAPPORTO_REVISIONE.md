# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 14 · Pirandello (2 Parti)
Revisione del 16–17/11/2026. Video: `Letteratura_Lez14_Parte1_1080p.mp4` e `…Parte2…` (a pezzi `.parte_00…`, sha256 nei `.sha256`).
**misurato** = misurato con uno strumento · **stima** = dedotto · **non verificato** = non ho potuto.
**Stato: consegna con riserve** (sezione 5 e DA DECIDERE): non dico «tutto perfetto».

## 1. Misure sul video nuovo (misurato)
| Controllo | Parte 1 | Parte 2 |
|---|---|---|
| Formato | 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192k | uguale |
| Durata | 45:45.4 (2745.43 s, 82363 fotogrammi) | 45:45.9 (2745.90 s, 82377 fotogrammi) |
| Vecchia durata | 50:07,5 (90 226 fotogrammi) | 48:36,4 (87 491 fotogrammi) |
| Peso | 327.3 MB | 353.0 MB |
| Volume intero file (ebur128) | I:         -14.4 LUFS · LRA:         6.0 LU · Peak:       -1.3 dBFS | I:         -14.8 LUFS · LRA:         6.2 LU · Peak:       -1.1 dBFS |
| Audio del prof | pulito dall'originale con la catena del kit (`aresample 48000, highpass 80, arnndn sh.rnnn, loudnorm, alimiter`): −16,9 LUFS integrato, picco −2,0 dBTP (misurato sull'intero originale pulito) | uguale |
| Jingle Quiz a 0,0 s (`controllo_jingle.py`) | Q1–Q4: scarti −0,001…−0,004 s · OK | Q1–Q6: scarti −0,001…−0,006 s · OK |
| Altri jingle (correlazione col kit) | titolo 4/4 · ripasso 4/4 · transizione 5/5 | titolo 6/6 · ripasso 6/6 · transizione 7/7 |
| Silenzi > 3 s | 0: nessuno | 2: 45:19.9–45:25.8 (6.0 s) · pezzo VER; 45:38.7–45:45.9 (7.3 s) · pezzo COMP |
| Fermi immagine ≥ 1 s nei pezzi del prof (`freezedetect`) | 103: 0:52.3 (2.0 s) · D0; 1:04.3 (1.2 s) · D0; 1:13.2 (1.0 s) · D0; 2:01.6 (1.3 s) · D0; 2:30.3 (1.5 s) · D0; 3:18.5 (1.1 s) · D0; 3:45.7 (1.5 s) · D0; 4:13.8 (2.0 s) · D1; 4:23.5 (2.3 s) · D1; 4:31.8 (1.0 s) · D1; 4:41.5 (1.2 s) · D1; 5:05.4 (1.3 s) · D1; 5:10.4 (1.4 s) · D1; 5:11.8 (2.2 s) · D1; 5:26.0 (1.1 s) · D1; 5:28.0 (1.0 s) · D1; 5:36.1 (1.1 s) · D1; 6:01.6 (1.1 s) · D1; 6:14.5 (1.1 s) · D1; 6:20.2 (1.2 s) · D1; 6:23.4 (1.1 s) · D1; 6:36.1 (1.3 s) · D1; 6:55.5 (1.6 s) · D1; 7:12.5 (1.2 s) · D1; 7:14.9 (1.0 s) · D1; 7:23.7 (1.1 s) · D1; 7:41.6 (1.1 s) · D1; 8:24.5 (1.0 s) · D1; 8:36.6 (1.1 s) · D1; 8:42.3 (1.0 s) · D1; 8:58.8 (1.3 s) · D1; 9:03.2 (1.4 s) · D1; 9:07.2 (1.1 s) · D1; 9:51.3 (1.0 s) · D1; 10:05.1 (1.9 s) · D1; 11:22.4 (1.8 s) · D1; 11:34.9 (1.1 s) · D1; 11:57.1 (1.0 s) · D1; 12:56.9 (1.8 s) · D1; 13:37.9 (1.7 s) · D1; 13:56.8 (1.1 s) · D1; 14:17.5 (1.5 s) · D1; 14:29.0 (1.1 s) · D1; 15:46.7 (1.1 s) · D1; 16:10.6 (1.1 s) · D1; 16:13.0 (1.7 s) · D1; 16:30.8 (1.2 s) · D1; 20:44.8 (1.0 s) · D2; 20:48.3 (1.2 s) · D2; 22:40.3 (1.7 s) · D2; 22:43.2 (1.6 s) · D2; 22:58.2 (1.9 s) · D2; 23:04.2 (1.7 s) · D2; 23:21.4 (1.4 s) · D2; 23:23.1 (1.7 s) · D2; 23:24.8 (1.9 s) · D2; 23:35.0 (1.7 s) · D2; 24:08.5 (1.1 s) · D2; 25:02.6 (1.1 s) · D2; 25:37.0 (1.4 s) · D2; 25:43.1 (1.7 s) · D2; 25:48.3 (1.4 s) · D2; 25:56.8 (1.0 s) · D2; 26:02.7 (1.4 s) · D2; 26:58.6 (1.5 s) · D2; 27:02.8 (1.4 s) · D2; 29:10.5 (1.5 s) · D3; 29:38.5 (1.4 s) · D3; 29:40.7 (1.1 s) · D3; 29:53.2 (1.1 s) · D3; 29:58.3 (1.6 s) · D3; 31:08.0 (1.1 s) · D3; 32:11.9 (1.5 s) · D3; 32:14.5 (1.1 s) · D3; 32:31.2 (1.3 s) · D3; 33:10.3 (1.6 s) · D3; 33:41.8 (1.1 s) · D3; 33:43.1 (1.2 s) · D3; 33:44.8 (1.3 s) · D3; 33:54.8 (1.7 s) · D3; 34:23.7 (1.5 s) · D3; 34:25.2 (1.1 s) · D3; 34:26.3 (1.3 s) · D3; 34:27.6 (2.3 s) · D3; 34:51.7 (1.0 s) · D3; 35:34.3 (1.3 s) · D3; 38:29.5 (1.1 s) · D4; 38:31.2 (1.0 s) · D4; 38:43.7 (2.0 s) · D4; 39:22.6 (1.2 s) · D4; 39:29.1 (1.4 s) · D4; 39:36.5 (1.1 s) · D4; 39:37.7 (1.8 s) · D4; 39:51.7 (1.2 s) · D4; 39:53.7 (1.9 s) · D4; 39:56.2 (1.5 s) · D4; 39:57.7 (1.4 s) · D4; 40:32.9 (1.1 s) · D4; 40:34.5 (1.0 s) · D4; 41:00.5 (1.4 s) · D4; 41:42.4 (1.1 s) · D4; 42:07.6 (1.1 s) · D4; 42:20.8 (1.4 s) · D4 | 149: 1:04.8 (3.5 s) · D0; 1:14.5 (1.6 s) · D1; 1:23.3 (1.1 s) · D1; 1:28.6 (1.1 s) · D1; 1:29.8 (2.1 s) · D1; 1:32.1 (1.1 s) · D1; 1:33.5 (1.1 s) · D1; 1:36.5 (1.0 s) · D1; 1:41.1 (1.4 s) · D1; 1:42.4 (1.3 s) · D1; 1:43.7 (1.8 s) · D1; 1:48.9 (2.1 s) · D1; 1:51.6 (1.1 s) · D1; 1:53.6 (2.5 s) · D1; 2:11.1 (1.1 s) · D1; 2:25.1 (1.0 s) · D1; 2:40.5 (1.1 s) · D1; 2:55.8 (1.3 s) · D1; 3:21.5 (1.1 s) · D1; 5:53.8 (2.2 s) · D2; 6:10.9 (1.4 s) · D2; 6:17.0 (1.2 s) · D2; 6:27.2 (1.5 s) · D2; 6:33.0 (1.1 s) · D2; 7:07.6 (1.4 s) · D2; 7:45.0 (1.0 s) · D2; 8:08.0 (1.9 s) · D2; 10:16.6 (1.3 s) · D3; 10:18.6 (1.5 s) · D3; 10:20.1 (1.1 s) · D3; 10:25.7 (1.2 s) · D3; 10:52.2 (1.2 s) · D3; 10:57.8 (1.0 s) · D3; 10:58.8 (2.1 s) · D3; 11:12.7 (1.8 s) · D3; 11:19.3 (1.6 s) · D3; 11:22.0 (1.4 s) · D3; 11:23.4 (1.5 s) · D3; 11:25.4 (1.0 s) · D3; 11:31.5 (1.1 s) · D3; 11:32.6 (1.0 s) · D3; 11:34.5 (1.3 s) · D3; 11:39.4 (1.2 s) · D3; 11:49.0 (1.0 s) · D3; 13:21.7 (1.1 s) · D4; 13:22.8 (1.3 s) · D4; 13:27.5 (1.1 s) · D4; 13:31.9 (1.3 s) · D4; 13:35.3 (1.2 s) · D4; 14:03.6 (1.3 s) · D4; 14:36.2 (1.0 s) · D4; 14:54.1 (1.1 s) · D4; 14:58.1 (1.7 s) · D4; 15:08.9 (1.1 s) · D4; 15:14.1 (1.2 s) · D4; 15:28.5 (2.0 s) · D4; 15:31.5 (1.2 s) · D4; 15:34.9 (1.1 s) · D4; 15:36.0 (1.6 s) · D4; 15:55.9 (1.4 s) · D4; 15:57.3 (1.3 s) · D4; 16:00.0 (2.1 s) · D4; 16:06.5 (2.3 s) · D4; 16:09.5 (1.2 s) · D4; 16:10.6 (1.1 s) · D4; 16:22.5 (2.3 s) · D4; 16:24.8 (1.0 s) · D4; 16:25.8 (1.7 s) · D4; 16:27.5 (1.0 s) · D4; 16:28.5 (2.3 s) · D4; 16:33.6 (2.9 s) · D4; 16:39.1 (1.4 s) · D4; 16:41.4 (1.0 s) · D4; 16:47.1 (1.2 s) · D4; 16:50.1 (1.9 s) · D4; 16:52.8 (1.7 s) · D4; 16:54.5 (2.0 s) · D4; 17:05.0 (1.1 s) · D4; 17:13.4 (1.1 s) · D4; 17:14.5 (3.1 s) · D4; 17:39.5 (1.2 s) · D4; 18:33.8 (1.2 s) · D4; 20:48.7 (2.1 s) · D5; 21:00.8 (1.3 s) · D5; 21:25.8 (1.1 s) · D5; 21:33.0 (1.1 s) · D5; 21:37.6 (2.0 s) · D5; 21:44.1 (1.4 s) · D5; 21:56.9 (2.7 s) · D5; 21:59.8 (1.3 s) · D5; 22:09.1 (1.0 s) · D5; 22:25.8 (1.9 s) · D5; 22:27.8 (1.3 s) · D5; 22:31.4 (1.6 s) · D5; 22:33.0 (1.6 s) · D5; 22:58.5 (2.4 s) · D5; 23:02.9 (1.3 s) · D5; 23:07.7 (1.3 s) · D5; 23:37.6 (1.4 s) · D5; 23:39.5 (1.3 s) · D5; 23:40.8 (1.6 s) · D5; 23:42.4 (1.3 s) · D5; 23:43.7 (1.7 s) · D5; 23:45.5 (1.3 s) · D5; 23:54.1 (1.1 s) · D5; 23:55.9 (1.1 s) · D5; 24:01.1 (1.0 s) · D5; 24:27.0 (1.1 s) · D5; 24:29.0 (4.7 s) · D5; 25:00.7 (2.2 s) · D5; 25:05.2 (1.6 s) · D5; 25:29.0 (1.8 s) · D5; 27:43.3 (1.4 s) · D6; 28:37.4 (1.0 s) · D6; 29:50.3 (1.1 s) · D6; 30:35.5 (1.3 s) · D6; 30:37.7 (1.3 s) · D6; 30:43.4 (1.0 s) · D6; 30:54.2 (1.2 s) · D6; 31:09.0 (2.6 s) · D6; 31:18.6 (1.5 s) · D6; 31:45.7 (2.2 s) · D6; 31:54.0 (1.3 s) · D6; 31:55.3 (1.6 s) · D6; 31:56.9 (1.0 s) · D6; 31:57.9 (1.9 s) · D6; 32:10.7 (2.0 s) · D6; 32:18.1 (1.9 s) · D6; 32:20.0 (1.4 s) · D6; 32:21.8 (1.5 s) · D6; 32:25.6 (1.5 s) · D6; 32:27.7 (1.9 s) · D6; 32:29.6 (1.8 s) · D6; 33:02.1 (1.4 s) · D6; 33:03.5 (1.5 s) · D6; 33:04.9 (1.2 s) · D6; 33:20.2 (1.2 s) · D6; 33:22.2 (1.3 s) · D6; 33:27.4 (1.1 s) · D6; 33:31.3 (1.8 s) · D6; 34:06.2 (1.7 s) · D6; 34:08.1 (1.3 s) · D6; 34:09.4 (1.1 s) · D6; 34:51.4 (1.3 s) · D6; 34:52.7 (1.2 s) · D6; 35:03.4 (1.0 s) · D6; 36:08.2 (1.1 s) · D6; 38:09.8 (1.0 s) · D6; 38:21.6 (1.8 s) · D6 |
| Sincronia audio del prof con l'originale | scarto massimo 0,5 ms su 36 punti (3 per pezzo D) | uguale |
| Sottotitoli | `.vtt` rigenerati dall'audio del video nuovo: 995 cue, max 2 righe da ≤43 caratteri | 946 cue |
| PDF | slide: 6 pagine A4 orizzontale | slide: 8 pagine; mappa del prof: 1 pagina (`…_mappe.pdf`) |
Le **durate sono cambiate** (decisione di Sara 17/11): la Parte 1 è **sotto i 50 minuti**, la Parte 2 anche. Vedi DA DECIDERE.

## 2. Confronto col modello Spagnolo (punto 000)
| # | Punto | Esito |
|---|---|---|
| 1 | Sigla → dissolvenza → copertina | sigla invariata; dissolvenze rifatte tra tutti i pezzi, con `trans.wav` |
| 2 | Copertina (logo, riga «LETTERATURA ITALIANA V · VIDEOLEZIONE», titolo, card ARGOMENTI) | **corretto**. Nella presentazione (voce di benvenuto) niente riquadro del prof: non parla |
| 3 | Slide: fondo bianco, «01 · ARGOMENTO», titolo+barretta, card | **corretto** per tutte le slide del prof |
| 4 | Piè di pagina + «Pagina N» | **corretto** (numerazione progressiva per Parte, copertina = 1) |
| 5 | Riquadro 4:3 con ombra grigia morbida, senza bordo | **corretto**: 412×309 px a x=1428 y=148, angoli r=18, correzione immagine del kit |
| 6 | Fascia gialla −3°, due righe | **corretto**, sempre visibile mentre parla il prof |
| 7 | Slide senza prof | **NON FATTO**: approfondimenti, pillole di ripasso, glossario, riepilogo e schede Quiz restano nella vecchia grafica scura (vedi sezione 5) |
| 8 | Font Figtree Bold / Bricolage 800 | corretto sulle slide rifatte (etichette in Figtree Bold) |
| 9 | Finale 5 s con avviso diritti | invariato (presente) |
| 10 | Struttura | mantenuta; **tolte le 12 mappe nostre**, inserita 1 mappa del prof con voce R1 (Parte 2) |
| 11 | PDF slide + mappe A4 orizzontale | slide: solo le slide nuove; mappe: sì |
Card in corso: bordo giallo sottile + numero su pallino giallo, fondo bianco, altre card con bordo grigio chiaro; ombre grigie morbide (richiesta di Sara 17/11 01:30).

## 3. Problemi trovati e correzioni
| Minuto (vecchio video) | Tipo | Com'era | Correzione |
|---|---|---|---|
| tutta la lezione | visivo | banda blu a destra, riquadro rettangolare con bordo blu, nome bianco su blu, etichetta «ARGOMENTO 1 ·» | rifatte tutte le slide del prof nel modello (punti 000) |
| P1 ≈ 4:00–8:00 (contact sheet) | sincronia | evidenziazione ferma sulla card 1 per minuti | evidenziazioni ricalcolate dal parlato (stima: parole chiave di ogni card nella trascrizione, percorso monotono; ogni card si accende) |
| tutta la lezione | sincronia | slide scelte dal video vecchio | la sequenza delle slide ora segue lo schermo dell'originale (il prof torna più volte tra le slide 3 e 4: nell'originale ai minuti 8:50, 13:30, 14:33, 15:05) |
| 10 confini su 11 tra pezzi del prof | audio | il pezzo del prof finiva a **metà frase** (da +0,9 a +9,1 s prima della fine frase) e il pezzo seguente ripeteva parlato | tutti i confini spostati sulla fine frase (pausa ≥0,45 s, minimo di energia); tabella in fondo |
| 6 punti: P1 D3 (30:38) e D4 (40:22); P2 D3 (11:02), D4 (15:06), D5 (23:18), D6 (30:56) del video vecchio | audio | **ripetizione** di 0,8–1,9 s di parlato del prof dopo gli inserti (misurata con gli offset costanti) | tolta: i pezzi D sono contigui nell'originale |
| P2 1:00–1:10 | visivo | per 3 s la slide di «Uno, nessuno» con etichetta del teatro | ora copertina Parte 2 |
| P1 (5 pezzi AN03/06/09/11/12) · P2 (7 pezzi AN02/04/06/08/10/12/13) | grafica | 12 mappe fatte da noi con nodi non del prof | tolte (con la loro voce); inserita la mappa del prof nella Parte 2 (41:29 del video nuovo, 120 s) |
| P2 Ciàula e Belluca (pezzi D4–D6) | pagina | pagina del libro piccola nel video | fettina dagli screen HD (vedi §4) |
| vtt | testo | 470 cue da un riconoscimento mediocre (es. «Piranvello», «lettratura», «pire andere»), tempi sfasati fino a 1 s | rigenerati dall'audio del video nuovo; nomi corretti: Ciàula, Meis, Moscarda, zi' Scarda, Casinò |
| scheda | testo | titolo «Pirandello · Parte 1»; argomento 2 «La visione del mondo e la trappola sociale» (≠ video), 3 «I primi grandi romanzi» | titolo standard «Letteratura V · Lezione 14 · Pirandello · Parte N», titoli argomento allineati al video, secondi aggiornati |
| audio | audio | la catena di pulizia del kit non era verificabile sul video vecchio | audio dei pezzi del prof rifatto dall'originale con la catena del kit |
| audio | jingle | transizioni e ripasso non rilevati dalla correlazione | `trans.wav` in ogni transizione, `repaso.wav` prima delle pillole |
Quiz: 5 domande per argomento già presenti; ho allineato i titoli. Verifica finale: le 10 domande coincidono con l'Excel del prof (similarità 1,0). Compiti: i 4 del PDF del prof, identici.

## 4. Pagine del libro in HD (B-bis)
Zip `Lez14_ingrandita.zip`: pagine 526–531 (Ciàula) e 533–538 (Belluca); **la pagina 532 manca nello zip**.
| Brano | Pagina | File HD | Minuto Parte 2 |
|---|---|---|---|
| Ciàula scopre la luna | 526 | Lez14_p526.png · prima fettina (titolo, temi principali, inizio) | dal pezzo D4 (≈ 20:45) a fine D5 |
| Il treno ha fischiato | 533 | Lez14_p533.png · prima fettina | D5 finale e tutto D6 |
Il prof **non legge** i brani: riassume mentre sullo schermo resta la prima pagina. Ho fatto scattare un'altra fettina solo se il testo citato coincide a lungo; non è scattata mai. Quindi **una sola fettina per novella**, ferma per minuti: lontano dalla lezione 11 di riferimento.

## 5. Cosa NON ho verificato / limiti noti / DA DECIDERE
- **Slide senza prof nella vecchia grafica**: approfondimenti animati, pillole, glossario, riepilogo (e schede Quiz/Verifica/Compiti con banda blu, come da prompt) **non sono stati rifatti** nel modello. Non ho il generatore dei loro testi; l'OCR sarebbe stato lungo. È il difetto più grosso rimasto: la lezione **non è nel modello in tutto**.
- **PDF slide**: contiene solo le slide nuove (copertina e slide del prof, 6 + 8 pagine); mancano le slide degli inserti vecchi. Non ho confrontato pagina per pagina col video.
- **Fettine del libro**: una per novella (§4). Niente `controllo_fettine.jpg` con più fettine.
- **Durata**: Parte 1 45:45.4, Parte 2 45:45.9: entrambe **sotto i 50 minuti**. Decide Sara (unire, aggiungere, accettare).
- **Voce R1** (mappa del prof): la trascrizione dell'ascolto automatico rende «giorfatara», «Fumathia Pascal», «Uno Nessuno ai 100.000»: potrebbe essere errore del riconoscimento o pronuncia sbagliata della voce. **Non ascoltata da me.** Se è la voce, serve R2 con il testo riscritto.
- Il **riquadro del prof 4:3**: la webcam originale è 184×138 px ingrandita 2,2×: immagine morbida; la testa tocca il bordo alto già nell'originale (es. 0:20, 11:40, 23:20 dell'originale).
- **Sincronia labbra**: video e audio sono presi dallo stesso istante dell'originale (scarto audio misurato ≤0,5 ms); il movimento delle labbra **non l'ho verificato indipendentemente**.
- **Evidenziazioni** delle card: stima da parole chiave; non ascoltate a mano. Slide 47 (Serafino Gubbio) non è mai mostrata dal prof: non c'è nel video.
- **Mappa del prof**: una sola per tutta la lezione, messa nella Parte 2 (decisione mia, da confermare). Nel PDF mappe i nodi sono identici (letti dall'immagine). 
- Nella mappa del prof: «Così è **se** (se vi pare)» (probabile refuso) e «Il **gioco** delle parti» (nelle slide «giuoco»): DA CONFERMARE COL PROF.
- Le pillole e gli approfondimenti vecchi contengono ancora qualche contenuto che non coincide con le slide (es. quiz 2 titolo vecchio): ho allineato solo i titoli.

## Tabella: fine e inizio di ogni pezzo del prof (misurato su pause ≥ 0,45 s)
| Pezzo | Inizio | Prime parole | Inizia a inizio frase | Fine | Ultime parole | Frase finita |
|---|---|---|---|---|---|---|
| P1 D0 | 0:52 | «Buongiorno e benvenuti alla lezione su…» | sì | 3:55 | «…i testi di Luigi Pirandello, alcuni dei quali.» | sì |
| P1 D1 | 4:01 | «come dire sono oggetto D Interrogazione…» | sì | 16:40 | «…perché hai sempre recitato un ruolo. We need.» | sì |
| P1 D2 | 20:40 | «ai tuoi occhi anche. Ecco questa,…» | sì | 27:27 | «…capire esattamente cosa ha scritto e cosa racconta.» | sì |
| P1 D3 | 29:08 | «Passiamo a, beh, insomma, al capolavoro,…» | sì | 36:00 | «…verghiano, per dare corpo alla relatività del reale.» | sì |
| P1 D4 | 37:54 | «E questa riflessione continua in... Uno,…» | sì | 42:24 | «…ha già abbozzato nel Fu Mattia Pascal. Proseguiamo.» | sì |
| P2 D0 | 1:00 | «uno sono centomila importante romanzo. Ora…» | sì | 1:08 | «…uno sono centomila importante romanzo. Ora dobbiamo parlare.» | sì |
| P2 D1 | 1:14 | «di come dire Beh, insomma, della…» | sì | 3:23 | «…infrange in tutto questo e viene sommerso, d'accordo?» | sì |
| P2 D2 | 4:51 | «Ecco, se i personaggi cerca d'autore,…» | sì | 8:21 | «…e poi Enrico IV, un altro dramma teatrale.» | sì |
| P2 D3 | 9:50 | «Questo un po più storico, d'accordo?…» | sì | 11:53 | «…sta male e alla fine non risolve nulla.» | sì |
| P2 D4 | 13:08 | «Ora, giusto perché siamo, diciamo così,…» | sì | 19:04 | «…se stessi, e soprattutto il concetto della maschera.» | sì |
| P2 D5 | 20:45 | «Però queste novelle in alcune, insomma,…» | sì | 25:40 | «…seconda, ed ultima, è in chiusura due parole.» | sì |
| P2 D6 | 27:39 | «su Pirandello è il rapporto con…» | sì | 39:25 | «…Poi si rese conto. Ma era troppo tardi.» | sì |

(«Frase finita» e «Inizia a inizio frase» = punteggiatura della trascrizione automatica seguita da pausa; le «ultime parole» sono del riconoscimento, non riascoltate.)

## Tabella secondo vecchio → secondo nuovo
**Parte 1**
| Pezzo | Vecchio | Nuovo | Differenza |
|---|---|---|---|
| T1 | 234.6 | 236.4 | +1.8 |
| Q1 | 1278.9 | 1230.1 | -48.8 |
| T2 | 1284.2 | 1235.4 | -48.8 |
| Q2 | 1828.3 | 1738.3 | -90.0 |
| T3 | 1833.6 | 1743.6 | -90.0 |
| Q3 | 2412.1 | 2264.2 | -147.9 |
| T4 | 2417.4 | 2269.5 | -147.9 |
| Q4 | 2821.7 | 2622.9 | -198.7 |
| GL1 | 2890.6 | 2628.5 | -262.1 |
| RF1 | 2939.2 | 2677.1 | -262.1 |
**Parte 2**
| Pezzo | Vecchio | Nuovo | Differenza |
|---|---|---|---|
| T1 | 70.3 | 69.6 | -0.7 |
| Q1 | 319.5 | 280.8 | -38.7 |
| T2 | 324.8 | 286.1 | -38.7 |
| Q2 | 651.8 | 579.9 | -71.9 |
| T3 | 657.1 | 585.2 | -71.9 |
| Q3 | 896.0 | 778.7 | -117.3 |
| T4 | 901.3 | 784.0 | -117.3 |
| Q4 | 1388.0 | 1234.8 | -153.2 |
| T5 | 1393.3 | 1240.1 | -153.2 |
| Q5 | 1846.3 | 1649.2 | -197.1 |
| T6 | 1851.6 | 1654.5 | -197.1 |
| Q6 | 2727.0 | 2484.0 | -243.0 |
| GL1 | 2782.8 | 2612.3 | -170.5 |
| RF1 | 2830.3 | 2659.8 | -170.5 |
| VER | 2891.3 | 2720.8 | -170.5 |
| CI1 | 2904.5 | 2734.0 | -170.5 |
| COMP | 2910.1 | 2739.6 | -170.5 |
La master rigenera la pagina con i secondi di `scheda_pubblicazione_parte*.json`, `quiz_argomenti_parte*.json` e `timeline_parte*.json`.

## 6. Come ho verificato
Trascrizione dell'originale (64 min) e dei due video con `trascrivi.py`; allineamento per correlazione dell'audio (offset costanti per pezzo); scene dell'originale (differenza di fotogrammi + OCR dei titoli); fotogrammi ogni 30 s (`controllo_minuti_parte*.jpg`); `controllo_jingle.py`; `ebur128`, `silencedetect`, `freezedetect`; correlazione col kit per i jingle; confronto Excel/PDF del prof con le consegne.
