# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 4 · «Naturalismo e Verismo» (prof. Giorgio Mazzotti)
Chat di revisione 4 · 17/11/2026 · ramo `revisione-letteratura-V-lez04`. Ogni dato è etichettato **misurato** / **stima** / **non verificato**.

## 1. Misure sul video nuovo (`Letteratura_Lez4_Parte1_1080p.mp4`)
| Misura | Valore | Tipo |
|---|---|---|
| Durata / fotogrammi | 2948,8 s (49:08,8) · 88463 fotogrammi = durata×30 | misurato |
| Formato | 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192 kb/s 48 kHz, 198,4 MB | misurato |
| Volume | −16,6 LUFS integrato; parlato del prof (mediana dei pezzi) −16,7 LUFS | misurato |
| Picco | −1,9 dBTP (limite −1) | misurato |
| Scatto jingle Quiz | +0,004 / +0,005 / +0,005 / +0,003 s (limite 0,05): OK | misurato |
| Silenzi > 3 s (−45 dB) | 0 | misurato |
| Fermi immagine nei pezzi del prof | nessuno (`controllo_finale.py` e `freezedetect` sul riquadro) | misurato |
| Sottotitoli | 660 blocchi, 0 sovrapposti, 0 oltre la fine, max 2 righe; attacco sulla voce entro 0,3 s: 70% di 20 punti verificabili (il controllo automatico è disturbato dai jingle: **da guardare**) | misurato / da guardare |
| Sincronia audio/video del prof | scarto audio finale vs originale −0,02 s su 12 punti (3 per pezzo, 4 pezzi): ≤ 0,04 s | misurato |

## 2. Confronto con il modello Spagnolo Lez. 1 (punto 000, 11 voci)
| # | Punto | Esito |
|---|---|---|
| 1 | Sigla 15 s → dissolvenza morbida → copertina | **OK** (sigla del kit; dissolvenza da nero di 1 s sulla copertina, nessun lampo) |
| 2 | Copertina: logo, riga «LETTERATURA ITALIANA V · VIDEOLEZIONE», titolo Bricolage 800 con barretta, card ARGOMENTI su due colonne | **corretto** (prima: fondo scuro, elenco senza card) |
| 3 | Slide: fondo bianco, riga «01 · ARGOMENTO» = numero dell'argomento, titolo + barretta, card, giallo solo sul punto in corso | **corretto** (prima: fascia scura laterale, intestazione scura) |
| 4 | Piè di pagina «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» + «Pagina N» | **corretto**; numeri di pagina = ordine di comparsa = pagine del PDF (49) |
| 5 | Riquadro 4:3, 412×310 px, x=1428 y=148, angoli arrotondati, ombra grigia morbida, niente bordo | **corretto** (prima: ~270×175 px con bordo giallo). Ritaglio 184×138 dall'originale + correzione del kit (contrasto 1,04, saturazione 1,03, hqdn3d 1.5:1.5:3:3, cas 0.35) |
| 6 | Fascia gialla −3°, due righe «Giorgio Mazzotti» / «PROF. DI LETTERATURA ITALIANA» | **corretto** (prima: assente, solo una scritta in DM Mono). Sempre visibile in tutti i pezzi con il prof |
| 7 | Slide senza prof: testo grande, parole chiave in giallo | **OK** (schede titolo, ripassi, glossario, riepilogo) |
| 8 | Solo Bricolage Grotesque / Figtree (etichette in Figtree Bold, aggiornamento 15:10) | **corretto** (prima: DM Mono) |
| 9 | Finale `Sigla_finale_5s_con_avviso_diritti.mp4` | **OK** |
| 10 | Struttura: sigla → presentazione → per argomento (titolo, prof, approfondimenti, ripasso, quiz) → glossario → riepilogo → finale | **OK**; la mappa del prof è nell'argomento 3 |
| 11 | PDF A4 orizzontale: slide identiche al video + mappe del prof | **OK**: `Letteratura_Lez4_slide.pdf` (49 pagine, A4 orizzontale, una slide per pagina nello stato finale, senza riquadro e senza fascia), `Letteratura_Lez4_mappe.pdf` (1 pagina, vettoriale) |

## 3. Problemi trovati e correzioni
Tempi **vecchi** = video consegnato (`consegna-…`, 53:46,2); tempi **nuovi** vedi §7.
| Minuto (vecchio) | Tipo | Com'era | Correzione |
|---|---|---|---|
| tutto | visivo | grafica diversa da Spagnolo (fondo scuro e bande blu, intestazione scura, riquadro piccolo con bordo, nessuna fascia gialla, font DM Mono) | tutta la lezione rifatta nel modello (§2) |
| D1 (0:54–9:03) | visivo | card 1 accesa dal minuto 0:52 al 5:43 **del pezzo** (291 s) ma il prof parla della card 1 solo da 4:41 («Il Naturalismo nasce in Francia…»); card 3 accesa a 6:38, il prof ne parla a 6:47 | evidenziazioni ricavate dal parlato (trascrizione con tempi); copertina con ARGOMENTI fino a 0:51 poi slide del prof |
| D2 (13:40–21:34) | visivo | card 2 («Il ciclo dei Rougon-Macquart») accesa per 188 s (minuti 2:00–5:08 del pezzo): il prof passa ai temi (card 3) a 3:21 e ai Goncourt a 5:21; card 3 mai accesa; card 1 poi ferma per 165 s mentre si parla dei Goncourt | card 1 → 2 → 3 sul parlato; ritorno del prof sulla slide di Zola (come nell'originale) senza card ferma |
| D3 (25:49–36:36) | visivo | slide del prof 7–10 in sequenza semplice; il prof in realtà torna indietro (slide 2, 3, 4, 6, 7, 8) negli ultimi ~80 s | sequenza delle slide ricavata dalla registrazione dello schermo del prof (cambi slide rilevati sull'originale) e dal parlato |
| D4 (42:40–47:57) | visivo | card 2 («Madame Bovary») accesa per 272 s (dal minuto 0:44 del pezzo alla fine); card 3 («Innovazioni stilistiche») mai accesa | card 1 → 2 → 3 → 2 sul parlato |
| D2, minuto 5:07 del pezzo | visivo | ritratto di Zola (slide 5 del prof, `image1.jpg`) mai mostrato | inserita la slide 5 per i ~4 s in cui il prof la mostra |
| intero VTT | testo | 726 blocchi, 384 con errori: «scappigliatura», «totina filosofica», «la rasca / miglio» per race / milieu, «ritmo italiano» per Verismo italiano, «il Naturalismo, in accordo, naffe», «Flopè/Flobèr», «Zolà», «in personale», «le reditabiologiche», «salanno», «arrazioni»… | riletti tutti e corretti contro la trascrizione e il contesto; max 2 righe; i blocchi che superavano 2 righe sono stati divisi |
| AN03 11:42 · AN06 23:51 · AN10 40:33 · AN12 49:21 · AN13 51:00 (vecchio) | audio/visivo | **5 «mappe» nostre** (Naturalismo francese, Zola, Verismo, Flaubert, tutta la lezione) con la loro voce: decisione 00:40 → solo mappe del prof | via le 4 mappe nostre (e la loro voce); al posto di «Il Verismo italiano» la **mappa del prof** (`MAPPE/LEZIONE 4.pdf`) impaginata nella matrice v3, con voce nuova R1 che ne legge i nodi (voce Kore, generata dalla master) |
| 3226 s | audio | picco −0,3 dBTP | picco −1,2 dBTP (misurato) |
| Q/T/VERIFICA/finale | audio | silenzi di 3,2–3,6 s (schede) e 6,5 s a fine video | schede più brevi (Quiz 3,5 s, Compiti 3,0+3,5 s): nessun silenzio > 3 s |
| T1–T3, COMPITI, RF | audio | schede senza jingle (T4, S, GL sì) | jingle del kit: `titolo.wav` sulle 4 schede titolo, `quiz.wav` sui Compiti, `trans.wav` a ogni stacco dopo il prof e sul riepilogo |
| tutti gli stacchi | visivo | taglio secco | dissolvenza breve (8 fotogrammi, 6 sul prof) |
| AN11, 48:57–49:08 (vecchio 2937–2948 s) | testo | tre frasi d'esempio su Emma («Emma disse: …») costruite da noi, non del prof | restano ma con la scritta «ESEMPIO COSTRUITO PER SPIEGARE LA TECNICA» → **DA CONFERMARE COL PROF** |
| ripassi S1–S4, RF, GL | visivo | liste spezzate in due «pagine» (la 2ª pagina mostrava solo gli ultimi punti) | una sola slide con tutti i punti, il punto in corso in evidenza |

## 4. Pagine del libro in HD
**Non pertinente**: la lezione 4 non ha pagine del libro (elenco del rapporto 5/11). `Lez04_ingrandita.1.zip` contiene solo `Lez04_docente.pdf` (le slide del prof, già usate).

## 5. Cosa NON ho verificato
- **Ascolto umano**: nessuno ha riascoltato il video; tutto è misurato o letto da trascrizione/fotogrammi. Pronuncia della voce Kore (nomi: Zola, Taine, Rougon-Macquart, Flaubert, Médan): **non verificata all'orecchio**. La trascrizione automatica di R1–R5 dà «Ten» per Taine e «Emilia» per «Émile Zola» in R3 (voce rimossa).
- **Sincronia labbra/voce a vista**: misurata solo come scarto audio/originale (§6) e per costruzione (audio e video ritagliati con lo stesso offset 0,351 dall'originale); non guardata fotogramma per fotogramma.
- **Assegnazione delle slide dell'ultimo pezzo del prof** (fine D3, 25–27 s di rimbalzi tra slide 3, 4, 6, 7, 8): segue i cambi slide della registrazione, non il contenuto.
- Gli esami del brief su «nessun lampeggio» (≤3 lampi/s): non misurati (le dissolvenze sono ≥ 6 fotogrammi; nessun lampo a fondo bianco→nero oltre la sigla).
- Testa del prof tagliata già nell'originale (limite noto): la webcam è 245×138 px e in più punti la testa tocca il bordo alto (es. 0:30, 6:40, 16:40 dell'originale); non si può correggere. Il riquadro è ingrandito 2,24× e quindi morbido.
- Mappe degli altri 3 argomenti: **il prof ha mandato una sola mappa (Il Verismo)**; non esistono mappe per Naturalismo, Zola e Flaubert → **DA CONFERMARE CON SARA/PROF** se ne servono.

## 6. Come ho verificato
- Video vecchio: ricomposto dai pezzi, sha256 OK; trascrizione completa con tempi (Parakeet/`trascrivi.py`); fotogrammi 1/s; evidenziazioni lette dai pixel gialli.
- Originale (32:07): slide e cambi slide dal fotogramma 1/s e da OCR del titolo; offset dei 4 pezzi del prof ricavati per correlazione audio (D1 0,351 s; D2 489,76 s; D3 963,05 s; D4 1609,99 s; i 4 pezzi sono un unico tratto continuo dell'originale: nessuna parola tagliata dentro).
- Video nuovo: `controllo_finale.py`, `controllo_jingle.py`, `ebur128` (volume e picco), correlazione audio finale/originale, contact sheet.

**Sincronia (misurata)**: D1 −0,02/−0,02/−0,02 s · D2 −0,02/−0,02/−0,02 s · D3 −0,02/−0,02/−0,02 s · D4 −0,02/−0,02/−0,02 s (correlazione dell'audio del video finale con l'audio dell'originale a 10%/50%/90% di ogni pezzo; −0,02 s = ritardo del codec AAC, costante). Il video è ritagliato dallo stesso file con lo stesso offset (0,351 s).

## 7. Secondi vecchi → nuovi
La durata è cambiata (rimosse 4 mappe nostre, schede più corte). **Quiz, Verifica e Compiti hanno nuovi secondi**: `scheda_pubblicazione.json` e `timeline.json` sono aggiornati; la master rigenera la pagina.
| Pezzo | secondo vecchio | secondo nuovo |
|---|---|---|
| T1 | 50.167 | 50.167 |
| AN03 | 702.433 | tolto |
| Q1 | 811.566 | 737.5 |
| T2 | 816.566 | 741.0 |
| AN06 | 1431.233 | tolto |
| Q2 | 1540.2 | 1399.833 |
| T3 | 1545.2 | 1403.333 |
| AN10 | 2432.8 | 2290.933 |
| Q3 | 2551.067 | 2409.2 |
| T4 | 2556.067 | 2412.7 |
| AN12 | 2961.3 | tolto |
| Q4 | 3055.233 | 2853.7 |
| AN13 | 3060.233 | tolto |
| GL | 3131.166 | 2857.2 |
| RF | 3169.133 | 2895.167 |
| VERIFICA | 3202.9 | 2928.933 |
| FIN | 3207.9 | 2932.433 |
| SIGLA_FINALE | 3212.733 | 2937.267 |
| COMPITI_INTRO | 3217.733 | 2942.267 |
| COMPITI | 3221.233 | 2945.267 |
Durata: vecchio 3226,2 s (53:46,2) → nuovo 2948,8 s (49:08,8). Fotogrammi 96787 → 88463.

## 8. Fine di ogni pezzo del prof (frase finita?)
| Pezzo | Inizio (prime parole) | Fine (ultime parole) | Frase finita |
|---|---|---|---|
| D1 | «Buongiorno e benvenuti alla lezione Naturalismo e Verismo» | «…sarà più incisivo, siamo anche nel secondo Ottocento» (0,78 s di silenzio dopo) | sì |
| D2 | «Va bene, quindi il vero caposcuola…» | «…molto personale di Zola, che però ha un certo seguito» (0,55 s dopo) | sì |
| D3 | «Va bene, ma oltre a che cosa abbiamo?» | «…è molto importante capirla e studiarla proprio perché si parla di Naturalismo» (1,05 s dopo) | sì |
| D4 | «Eh, se volete, come dire, delineare…» | «…nella prossima lezione affronteremo in ambiente italiano, o meglio siciliano, Verga» (1,64 s dopo) | sì |
Misurato sulla trascrizione con tempi. I 4 pezzi sono contigui nell'originale: l'audio del prof non è mai tagliato; i pezzi non si accorciano.

## 9. DA CONFERMARE COL PROF / CON SARA
1. Esempi sul discorso indiretto libero («Emma disse…») costruiti da noi (AN11).
2. Mappe del prof per Naturalismo, Zola e Flaubert: non pervenute (solo «Il Verismo»).
3. Durata finale sotto i 50 minuti (regola 7/11) perché tolte le mappe nostre: decide Sara se allungare.
4. Nella mappa del prof «Federico De Roberto» compare solo nella mappa; il prof nella lezione non lo nomina.

## 10. Stato dei controlli obbligatori
- `controllo_finale.py`: durata, fotogrammi, peso, quiz a 0,0 s, fermi, volume: OK; sottotitoli: DA GUARDARE (vedi §1).
- `controllo_jingle.py`: 4/4 Quiz OK (`controllo_jingle.txt`).
- Jingle del kit: `titolo.wav` sulle 4 schede titolo, `quiz.wav` su Quiz/Verifica (già presenti) e Compiti, `repaso.wav` sui ripassi/glossario (già presenti), `trans.wav` agli stacchi. Dissolvenza breve a ogni stacco (8 fotogrammi, 6 sul prof).
- Ombre grigie morbide, card in corso con bordo giallo sottile e numero su pallino giallo, riquadro e foto con ombra grigia: applicato a tutte le slide e al PDF.
- Mai il numero della lezione nel video; nessun testo tagliato (controllato sul contact sheet `controllo_minuti.jpg`, 1 fotogramma ogni 30 s).
