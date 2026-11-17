# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 3 · Giosuè Carducci
Riconsegna del 17/11/2026 (regole fino alle 08:45). Video: `Letteratura_Lez3_Parte1_1080p.mp4` (4 pezzi `.parte_00…03` + `.sha256`, ricomposto e controllato).
Ogni dato è etichettato **misurato**, **stima** o **non verificato**. La durata è **cambiata** (decisione di Sara 00:40): i secondi nuovi sono già in `scheda_pubblicazione.json`; tabella al §3-bis.

## 1. Misure sul video nuovo (misurato, file finale)
| Controllo | Risultato |
|---|---|
| Formato | 1920×1080, 30 fps, x264 veryfast (prof CRF 22, il resto CRF 19), AAC 192k 48 kHz |
| Durata / fotogrammi | 63:32,9 (3812,9 s) · 114 387 fotogrammi = durata × 30 (prima: 62:12,9) |
| Peso | 398,2 MB (379,8 MiB) |
| Volume | −16,6 LUFS (LRA 7,0). **Picco vero −1,5 dBTP** (`ebur128=peak=true`) |
| Silenzi | nessuno > 3 s: il più lungo è 2,93 s (3583–3586, pausa tra la fine del prof e il ripasso 4). Prima: 11 silenzi ≥ 2,5 s, fino a 7,9 s |
| Scatto jingle Quiz (`controllo_jingle.py`) | Q1 +0,000 s · Q2 +0,000 s · Q3 +0,000 s · Q4 +0,000 s (limite 0,05): tutti OK |
| Fermi immagine nel riquadro (`freezedetect` −55 dB, ≥ 1 s, 0:45–59:00) | 13 fermi, **tutti su schede senza prof** (ripassi 11:08–11:40, 28:55–29:50, 45:55–46:15, schede quiz). **Nessun fermo mentre il prof parla.** In copertina il riquadro compare solo da 0:45, quando il prof parla davvero (prima non c'è né riquadro né fascia) |
| Sincronia audio/video del prof (misurato per pezzo, 6 punti a pezzo) | scarto A/V: copertina −0,005 s · A1 −0,001 s · A2 −0,014 s · A3 +0,003 s · A4 −0,004 s (limite 0,04). Metodo: audio = correlazione col parlato pulito dell'originale; video = confronto del riquadro con la webcam dell'originale (risoluzione 1/30 s) |
| PDF | slide: 47 pagine A4 orizzontale; mappe: 1 pagina A4 orizzontale |

## 2. Confronto col modello Spagnolo (punto 000)
| # | Punto | Esito |
|---|---|---|
| 1 | Sigla 15 s → dissolvenza → copertina | OK (sigla invariata; dissolvenza di 1 s) |
| 2 | Copertina (logo, riga «LETTERATURA ITALIANA V · VIDEOLEZIONE», titolo, card ARGOMENTI) | **corretto** |
| 3 | Slide: fondo bianco, «01 · ARGOMENTO», card | **corretto**; card «in corso» = bordo giallo sottile, numero su pallino giallo, ombre grigie morbide (mai nere) |
| 4 | Piè di pagina + «Pagina N» | **corretto**, Figtree Bold spaziato; numeri 1–47 uguali nel video e nel PDF |
| 5 | Riquadro 4:3 | **corretto**: 412×309 px a x=1428, y=148, angoli arrotondati, ombra grigia morbida |
| 6 | Fascia gialla due righe | **corretto** (compare insieme al riquadro) |
| 7 | Slide senza prof | **corretto**: ripassi, mappa, glossario, riepilogo |
| 8 | Font | Bricolage Grotesque 800, Figtree; etichette e piè in Figtree Bold (aggiornamento 15:10). DM Mono non usato nelle schede nuove |
| 9 | Finale | **corretto**: `Sigla_finale_5s_con_avviso_diritti.mp4` del kit; tolte le schede «Verifica finale» e «Compiti» (stanno fuori dal video) |
| 10 | Struttura | OK: sigla, presentazione, 4 argomenti (titolo, prof, ripasso, quiz), **mappa del prof**, glossario, riepilogo, finale |
| 11 | PDF A4 | fatti (slide 47 pagine, mappe 1 pagina) |

## 3. Problemi trovati e correzioni
| Minuto (video vecchio) | Tipo | Com'era | Correzione |
|---|---|---|---|
| tutto | visivo | prof nel tondo, grafica diversa dal modello | tutto rifatto (punti 000) |
| 0:17–0:45 | visivo | foto ferma del prof nel riquadro durante la voce di benvenuto | via riquadro e fascia: compaiono a 0:45 con il video vivo |
| tutto | visivo | card in corso con bordo spesso e filetto nero; ombre bluastre | bordo giallo sottile, pallino giallo, ombre grigie (aggiornamento 01:30); anche cornici delle pagine del libro |
| 3:43–4:36 · 8:12–9:12 | sincronia | card 2 mai evidenziata (53 s e 80 s senza card) | accese dal parlato del prof |
| 59:52–60:30 (ripasso 4) | testo | «Rime e ritmi, è del 1890nove» | «1899» |
| 61:13–61:50 (riepilogo) | testo | schede 3 e 4 senza titolo, testo in grassetto con «Tre,» e «Quattro,» | titoli come le schede 1 e 2 |
| ripasso 3 · riepilogo | voce | Kore leggeva male «Levia Gravia», «Giambi ed Epodi», «Le Odi barbare» (anche «Leo di barbare») | voci nuove **S3B** e **RF2** (testo con gli accenti: «Iuvenìlia, Lèvia Gràvia, Giàmbi ed Èpodi», «Òdi bàrbare»), rimontate; volume +2 dB per pareggiare le vecchie |
| 37:37–45:52 · 47:51–57:47 | pagina | fettine sbagliate (righe e colonne tagliate) | rifatte tutte (§4) |
| vtt | testo | ~60 errori | corretti (800 cue, max 2 righe) |
| 46:33→ | silenzio | 7,2 s di silenzio alla fine del ripasso 3 (la voce nuova è più corta) | tolti 5,0 s di fermo (la slide restava ferma): da qui i secondi cambiano di −5,0 s |
| schede Quiz / titoli argomento | audio | **nessun jingle** (silenzi di 3–4 s) | `quiz.wav` (a inizio scheda + 0,5 s), `titolo.wav` a ogni titolo, `repaso.wav` a ogni ripasso (sfumato sotto la voce), `trans.wav` a ogni passaggio (0:43, 1:57, 11:49, 29:45, 46:38 e nella coda), con dissolvenza |
| fine | struttura | schede «Verifica finale» e «Compiti» dentro il video, ~16 s | tolte |
| mappe | contenuto | nessuna mappa del prof nel video | **mappa del prof** in 3 slide (vita · linguaggio, poesia, tematiche · raccolte) con voce nuova **MAPPA1** (1:43), evidenziazione in sincronia; contenuto identico alla mappa, tolti logo di terzi e immagini |
| audio prof | audio | non pulito con la catena del kit (non dimostrabile all'ascolto) | rifatto dall'originale: `aresample 48000, highpass 80, arnndn (sh.rnnn), loudnorm −16, alimiter`; stessi offset del video |
| fine | audio | picco −0,8 dBTP | −1,5 dBTP |
| scheda | dati | titolo «… · Parte 1» | «Letteratura V · Lezione 3 · Giosuè Carducci»; secondi aggiornati |

### 3-bis. Secondo vecchio → secondo nuovo (aggiornato in `scheda_pubblicazione.json`; la master rigenera la pagina)
| Elemento | vecchio | nuovo |
|---|---|---|
| Argomenti 1, 2, 3: titolo e Quiz 1, Quiz 2 | 112,799 · 699,266 · 704,566 · 1775,766 · 1781,066 | identici |
| Quiz 3 | 2793,133 | **2788,133** |
| Argomento 4 (titolo) | 2798,433 | **2793,433** |
| Quiz 4 | 3627,632 | **3622,632** |
| Mappa del prof (nuova) | – | 3627,3 |
| Glossario | 3632,3 | **3731,8** |
| Riepilogo | 3673 | **3771,9** |
| Finale (5 s) | 3716 | 3807,9 |
| Durata | 3732,933 | **3812,9** |
I sottotitoli dopo 46:33 sono spostati di −5,0 s (177 cue). Capitoli YouTube aggiornati in `testo_youtube.txt`.

### 3-ter. Il prof non è mai tagliato a metà frase (aggiornamento 01:25) — tempi del video nuovo
| Pezzo | Inizio · prime parole | Fine · ultime parole | Frase finita |
|---|---|---|---|
| Presentazione | 0:45 «Buongiorno e benvenuti alla lezione su Giosuè Carducci…» | 1:52 «…sul pianeta Carducci, che è tutta un'altra realtà.» | sì |
| Argomento 1 | 1:57 «Allora, partiamo dalle basi, quindi…» | 11:06 «…per i suoi versi, d'accordo?» | sì |
| Argomento 2 | 11:48 «Va bene, però dobbiamo capire come funzionano. Questi versi…» | 28:57 «…tutte le sue fasi e alcuni testi.» | sì |
| Argomento 3 | 29:44 «Quindi in questa seconda parte della lezione faremo esattamente questo…» | 45:50 «…in questo caso piuttosto dolorosa.» | sì |
| Argomento 4 | 46:36 «Concludiamo parlando delle Odi barbare…» | 59:44 «…lo abbiamo ricostruito e affrontato con tanto di testi.» | sì |
Letto dalla trascrizione automatica (**stima**: non riascoltato). Nessun pezzo è stato accorciato né allungato rispetto a prima.

## 4. Pagine del libro in alta risoluzione (B-bis)
Zip `Lez03_ingrandita.1.zip`: pagine 50, 51, 53, 54, 56, 57, 58. Una sola colonna per fettina; inizio e fine su una riga bianca; bordi senza testo tagliato (controllo automatico dei 4 bordi su ogni fettina); niente intestazioni, numeri di pagina, QR, etichette laterali, esercizi di comprensione né il quadro di p. 58; tabelle intere; titoletti uniti al paragrafo. Fettina in corso con bordo giallo, dentro una cornice con margine bianco. Fotogramma di ognuna delle 38 righe (a metà intervallo, dal video finale) in `controllo_fettine.jpg`. **Abbinamento fettina → voce scritto a mano dalla trascrizione: stima ±3 s, non verificato all'ascolto.**
| # | Brano | Pagina | Parte | File HD e ritaglio (px) | Minuto (video nuovo) |
|---|---|---|---|---|---|
| 1 | Pianto antico (Rime nuove) | 50 | testata del brano | `Lez03_p050.png` x 330–1650, y 1927–2385 | 37:37–38:06 |
| 2 | Pianto antico (Rime nuove) | 50 | versi | `Lez03_p050.png` x 444–969, y 2463–2965 | 38:06–38:24 |
| 3 | Pianto antico (Rime nuove) | 51 | versi | `Lez03_p051.png` x 427–966, y 237–750 | 38:24–38:42 |
| 4 | Pianto antico (Rime nuove) | 50 | testata del brano | `Lez03_p050.png` x 330–1650, y 1927–2385 | 38:42–39:59 |
| 5 | Pianto antico (Rime nuove) | 50 | riquadro «Temi principali» | `Lez03_p050.png` x 1680–2197, y 1930–2165 | 39:59–40:34 |
| 6 | Pianto antico (Rime nuove) | 50 | versi | `Lez03_p050.png` x 444–969, y 2463–2965 | 40:34–40:50 |
| 7 | Pianto antico (Rime nuove) | 50 | note | `Lez03_p050.png` x 1385–2195, y 2472–2969 | 40:50–42:31 |
| 8 | Pianto antico (Rime nuove) | 51 | note, colonna sinistra | `Lez03_p051.png` x 170–830, y 819–944 | 42:31–43:19 |
| 9 | Pianto antico (Rime nuove) | 51 | versi | `Lez03_p051.png` x 427–966, y 237–750 | 43:19–43:40 |
| 10 | Pianto antico (Rime nuove) | 51 | note, colonna centrale | `Lez03_p051.png` x 850–1511, y 816–947 | 43:40–44:12 |
| 11 | Pianto antico (Rime nuove) | 51 | note, colonna destra | `Lez03_p051.png` x 1532–2192, y 496–951 | 44:12–44:44 |
| 12 | Pianto antico (Rime nuove) | 51 | versi | `Lez03_p051.png` x 427–966, y 237–750 | 44:44–45:18 |
| 13 | Pianto antico (Rime nuove) | 51 | «Analisi del testo» | `Lez03_p051.png` x 507–2192, y 1315–2134 | 45:18–45:52 |
| 14 | Nella piazza di San Petronio | 53 | testata del brano | `Lez03_p053.png` x 330–1630, y 1238–1593 | 47:46–48:17 |
| 15 | Nella piazza di San Petronio | 53 | riquadro «Temi principali» | `Lez03_p053.png` x 1640–2193, y 1240–1519 | 48:17–48:26 |
| 16 | Nella piazza di San Petronio | 53 | testata del brano | `Lez03_p053.png` x 330–1630, y 1238–1593 | 48:26–48:52 |
| 17 | Nella piazza di San Petronio | 53 | metro | `Lez03_p053.png` x 506–2191, y 1612–1797 | 48:52–49:08 |
| 18 | Nella piazza di San Petronio | 53 | versi | `Lez03_p053.png` x 427–1474, y 1866–2312 | 49:08–49:31 |
| 19 | Nella piazza di San Petronio | 53 | versi | `Lez03_p053.png` x 427–1474, y 2312–2607 | 49:31–49:49 |
| 20 | Nella piazza di San Petronio | 54 | versi | `Lez03_p054.png` x 425–1454, y 241–690 | 49:49–50:08 |
| 21 | Nella piazza di San Petronio | 54 | versi | `Lez03_p054.png` x 425–1454, y 690–1056 | 50:08–50:28 |
| 22 | Nella piazza di San Petronio | 54 | «Analisi del testo» | `Lez03_p054.png` x 505–2192, y 1579–1961 | 50:28–51:08 |
| 23 | Nella piazza di San Petronio | 54 | «Analisi del testo» | `Lez03_p054.png` x 505–2192, y 2664–2965 | 51:08–51:58 |
| 24 | Alla stazione in una mattina d'autunno | 56 | testata del brano | `Lez03_p056.png` x 260–1720, y 240–512 | 51:58–52:01 |
| 25 | Alla stazione in una mattina d'autunno | 56 | introduzione | `Lez03_p056.png` x 507–1659, y 538–684 | 52:01–52:14 |
| 26 | Alla stazione in una mattina d'autunno | 56 | metro | `Lez03_p056.png` x 507–1656, y 703–802 | 52:14–52:26 |
| 27 | Alla stazione in una mattina d'autunno | 56 | versi | `Lez03_p056.png` x 428–1397, y 902–1440 | 52:26–52:50 |
| 28 | Alla stazione in una mattina d'autunno | 56 | versi | `Lez03_p056.png` x 428–1397, y 1440–1979 | 52:50–53:20 |
| 29 | Alla stazione in una mattina d'autunno | 57 | versi | `Lez03_p057.png` x 421–1365, y 241–771 | 53:20–53:40 |
| 30 | Alla stazione in una mattina d'autunno | 57 | versi | `Lez03_p057.png` x 421–1365, y 771–1324 | 53:40–54:20 |
| 31 | Alla stazione in una mattina d'autunno | 57 | versi | `Lez03_p057.png` x 421–1365, y 1324–1854 | 54:20–54:43 |
| 32 | Alla stazione in una mattina d'autunno | 58 | versi | `Lez03_p058.png` x 424–1349, y 238–769 | 54:43–55:06 |
| 33 | Alla stazione in una mattina d'autunno | 58 | versi | `Lez03_p058.png` x 424–1349, y 769–1321 | 55:06–55:31 |
| 34 | Alla stazione in una mattina d'autunno | 58 | versi | `Lez03_p058.png` x 424–1349, y 1321–1650 | 55:31–55:49 |
| 35 | Alla stazione in una mattina d'autunno | 56 | testata del brano | `Lez03_p056.png` x 260–1720, y 240–512 | 55:49–56:15 |
| 36 | Alla stazione in una mattina d'autunno | 56 | metro | `Lez03_p056.png` x 507–1656, y 703–802 | 56:15–56:32 |
| 37 | Alla stazione in una mattina d'autunno | 56 | riquadro «Temi principali» | `Lez03_p056.png` x 1740–2194, y 242–513 | 56:32–57:33 |
| 38 | Alla stazione in una mattina d'autunno | 56 | testata del brano | `Lez03_p056.png` x 260–1720, y 240–512 | 57:33–57:42 |

## 5. DA CONFERMARE COL PROF
- Date della mappa e delle slide non coincidono: mappa «Giambi ed Epodi 1879», «Odi barbare 1889», «Rime e ritmi 1897»; slide e voce «Odi barbare dal 1877», «Rime e ritmi 1899». Nella mappa (e sullo schermo) ho lasciato le date del prof; la voce nuova della mappa **non legge gli anni delle raccolte**, per non ripetere date in contrasto.

## 6. Cosa NON ho verificato / limiti
- **Ascolto umano:** non ho riascoltato nulla. In particolare **S3B è segnata «DA CONTROLLARE»** negli esiti del servizio voci e **non so se «Lèvia Gràvia / Giàmbi / Èpodi / Òdi bàrbare» sono ora pronunciate giuste**: la trascrizione automatica non basta. Da ascoltare a 45:56 (ripasso 3), 61:37 (riepilogo) e nella mappa (1:13–1:38 dalla sua partenza, 61:13 del video). Se sono sbagliate, si rigenerano con nuove voci `R…`.
- **Rumore del prof dopo la pulizia** (fruscio/ronzio/metallico): non ascoltato.
- **Evidenziazioni delle card:** dalla trascrizione automatica (±8 s); fettine e mappa: ±3 s (stima).
- **Schede di servizio «Quiz» e «titolo argomento»** (fondo scuro animato): non rifatte nel modello; ci ho aggiunto i jingle. Font di quelle schede non controllato.
- Sincronia labbra: misurata solo come scarto tra audio e riquadro rispetto all'originale (≤ 0,014 s); non ho giudicato il movimento delle labbra a vista.
- **Testa nel riquadro:** i capelli toccano il bordo alto già nell'originale in diversi punti (es. 5:00 e 28:20 dell'originale); la webcam è 184×138 px ingrandita 2,2×, quindi più morbida del modello.
- **Sottotitoli:** corretti 60 errori noti; a 18:18 («alla Cereberi») e 22:31 («cantore italilo») la parola non è decifrabile e resta com'è.
- Quiz: riletti contro le slide del prof, invariati.

## 7. Come ho verificato
Trascrizione completa (Parakeet) del video vecchio e di ogni voce nuova, OCR, 3733 fotogrammi a 1/s sul vecchio, 127 fotogrammi a 1/30 s sul nuovo (`controllo_minuti.jpg`), `controllo_jingle.py` con `quiz.wav` del kit, `ebur128`, `silencedetect`, `freezedetect`, controllo automatico dei bordi delle fettine, piano di montaggio verificato fotogramma per fotogramma (37 pezzi = 114 387 fotogrammi), ricomposizione dei pezzi con sha256.
