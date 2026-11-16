# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 26 · Italo Calvino (Prof. Giorgio Mazzotti)
**Versione finale (16/11/2026) · stato: REVISIONATA** · ramo `revisione-letteratura-V-lez26`

## Risultato in una riga
Lezione rifatta nella grafica identica a Spagnolo Lez. 1 (fondo bianco, riquadro 4:3, fascia gialla col nome), con mappe del prof, voci e schermo allineati, sottotitoli corretti, finale con avviso diritti e i due PDF A4. Il montaggio dei contenuti, le voci e le slide del prof sono rimasti quelli già approvati.

## Misure sul video nuovo (misurato)
| Controllo | Esito |
|---|---|
| Formato | 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192k 48 kHz |
| Durata / fotogrammi | 52:34,2 (3154,2 s) · 94.626 fotogrammi (identici alla versione precedente) · OK (50–60 min) |
| Peso | 190,9 MB (< 400 MB) · tre pezzi `.parte_00/01/02`, sha256 nel file `.sha256` |
| Volume del parlato | −16,1 LUFS · picco vero **−1,5 dBTP** (limitatore; richiesto ≤ −1) · OK (prima −16,3 e −0,6 dB) |
| Silenzi > 2,5 s | 6, tutti nelle schede «Pausa del video / Quiz» e nei titoli (2,96–3,9 s, non parlato: sono le pause previste). Nessun silenzio nel parlato. Sparita la coda muta di 7,9 s |
| Sincronia prof (labbra/mani) | 25 punti a caso: somiglianza vecchio tondo ↔ nuovo riquadro min 0,85, media 0,96 (soglia 0,75) → OK. Le 5 tracce del prof vengono dall'originale con offset costanti (allineamento audio su 3.041 finestre su 3.120) |
| Sincronia slide–prof | 17 cambi di evidenziazione confrontati col parlato: tutti coerenti (±2 s). Nessuna slide ferma > 60 s mentre il prof parla d'altro |
| PDF slide ↔ video | 45 pagine; confronto automatico pagina per pagina con il fotogramma finale della slide nel video: differenza media 5,8/255, massima 9,1 (dovuta a evidenziazione e compressione) → coincidono |
| Quiz | 5 domande per argomento, risposte giuste controllate (una per una); verifica finale: 10 domande **identiche** all'Excel del prof (riga per riga); compiti identici al PDF del prof |

## Confronto con il modello Spagnolo (punto 000)
| # | Punto | Esito |
|---|---|---|
| 1 | Sigla → dissolvenza → copertina | **corretto**: c'era uno stacco secco a 0:15, ora dissolvenza morbida |
| 2 | Copertina (card ARGOMENTI, riga blu, titolo + barretta) | **corretto**: la card «ARGOMENTI» mancava |
| 3 | Slide: fondo bianco, «01 · ARGOMENTO», titolo + barretta | **corretto**: era grigio-azzurro, testo minuscolo |
| 4 | Piè di pagina + «Pagina N» | **corretto**: c'erano «Introduzione / Approfondimento / Ripasso» e numeri ripetuti; ora «Pagina N» progressiva (1–45) |
| 5 | Riquadro 4:3 | **corretto**: era un tondo con bordo. Ora 410×308, angoli arrotondati, ombra grigia, tutta testa e spalle, ritaglio dall'originale con correzione immagine del kit (contrasto 1,04, saturazione 1,03, hqdn3d 1.5:1.5:3:3, cas 0,35). **Limite**: nell'originale il prof è un riquadro di 243×135 px, quindi il 4:3 è ingrandito 2,3×: la nitidezza è quella che la sorgente permette |
| 6 | Fascia gialla col nome, due righe, −3° | **corretto**: non c'era; ora sempre visibile quando il prof è in video |
| 7 | Slide senza prof | **corretto** (testo grande, parole in giallo, stessi logo e piè) |
| 8 | Font | **corretto (16/11 15:10)**: «01 · ARGOMENTO», riga copertina e piè di pagina in **Figtree Bold maiuscolo spaziato** come nel modello (prima DM Mono); nel video e nei PDF solo Bricolage Grotesque e Figtree |
| 9 | Finale kit con avviso diritti | **corretto**: c'era un finale nero senza avviso, poi una card «Compiti» (ordine sbagliato). Ora la sigla del kit da 5 s, in coda |
| 10 | Struttura | **OK**; verifica finale e compiti sono fuori dal video (le card «Verifica» e «Compiti» sono state tolte) |
| 11 | PDF A4 orizzontali | **creati**: `Letteratura_Lez26_slide.pdf` (45 pagine, senza riquadro e fascia, testo vero) e `Letteratura_Lez26_mappe.pdf` (6 pagine) |

## Problemi trovati e corretti (minuti riferiti al video PRIMA della correzione)
| Minuto | Tipo | Com'era | Come l'ho corretto |
|---|---|---|---|
| tutta | visivo | prof nel tondo, nome senza fascia, fondo grigio, testo minuscolo | grafica Spagnolo (punti 1–7 sopra) |
| 0:15 | visivo | stacco secco sigla → copertina | dissolvenza di 0,6 s |
| 1:08 | audio/visivo | il prof dice «ecco appunto una sua fotografia» e sullo schermo non c'è la foto | inserita la foto presa dalla **slide 2 del prof** (immagine `p2`) da 1:07 a 1:14 nella copertina. *Da confermare da Sara: è un'immagine editoriale dentro le slide del prof* |
| 8:45–10:00 e 17:10–18:15 | visivo | confronti «Calvino e Pavese» e «Lo sguardo di un bambino»: terza card tagliata e sovrapposta al piè | slide rifatte, tutte le card dentro la pagina |
| 10:00–11:00, 19:40–20:40, 30:30–32:00, 41:10–42:00, 50:20–51:30, 52:10–53:20 | visivo/audio | 5 mappe + mappa finale **inventate** («Barone rampante e realismo»…), con voce che le descriveva | mappe del prof (`LEZIONE 26.pdf`, «Italo Calvino 1923-1985») impaginate con la nostra grafica, **contenuto identico**: vita, pensiero, saggista, opere (neorealismo, problemi sociali, fiabe/avventure, fantascienza, combinatorio). Tolti il logo «Mappe per la scuola» e la foto del personaggio. Una mappa per argomento (parti della mappa del prof) + mappa finale intera. **Voci nuove** M1–M5 e MF (Kore, dalla master) |
| 11:00–11:45, 20:40–21:25, 33:00–33:45, 41:20–42:00, 51:20–52:10 | audio/visivo | **pillole di ripasso**: la voce legge frasi che non erano sullo schermo (pillola 2: «Il realismo della guerra si unisce…»; pillola 4: frase sulle Città invisibili; pillola 5: «La letteratura non può contenere tutta la realtà…»); pillola 1 chiudeva con la sola riga «Muore a Siena.» per 1 s | schermo = testo letto dalla voce; ogni riga compare quando la voce la dice |
| 53:19–54:20 | audio/visivo | **glossario**: la voce legge 8 termini, sullo schermo ne comparivano 6 (mancavano «Dimezzato» e «Speculazione edilizia») | 8 termini, a tempo con la voce |
| 55:05–55:29 | audio/visivo | finale senza avviso diritti; card «Verifica finale» (5 s muta) e «Compiti» (8 s muta) dentro il video | finale kit 5 s con avviso; verifica e compiti restano fuori dal video |
| 55:29 | audio | coda muta 7,9 s | tolta |
| `.vtt` | testo | 722 sottotitoli con errori di trascrizione («Nacordo», «Itholo», «Santiago della Svegas», «polliedri», «Inetiamo», «viragno», «Napolone», «spicolazione», «slaque», «tricene»…); **nessun sottotitolo** per benvenuto, ripassi, glossario, riepilogo e finale (buchi di 45–60 s) | riletti i 325 sottotitoli del prof e corretti; aggiunti quelli mancanti (testi delle voci Kore); 769 cue, ≤ 2 righe, nessuna sovrapposizione, tempi sul video nuovo |
| scheda/quiz | testo | argomenti con nomi diversi da quelli del video («La vita di Calvino», «Scienza, combinatoria e città invisibili» vs «La vita», «Il secondo Calvino») | allineati a quelli del video (scheda, quiz, YouTube) |
| `compiti.json` | testo | lista di 4 frasi, formato sbagliato | formato `{"titolo","esercizi":[{n,tipo,testo}]}`, testo identico al PDF del prof |
| `scheda_pubblicazione.json` | testo | titolo «Italo Calvino · Parte 1», tempi del video vecchio | titolo «Letteratura V · Lezione 26 · Italo Calvino», tempi nuovi |

## Correzioni dopo il controllo della master (16/11)
1. **Slide vuote:** la scheda «Il visconte dimezzato» (e tutte le altre slide senza prof: schede opera, linee del tempo, confronti, analisi, parole chiave) restava a solo titolo fino alla prima card. Ora la prima card/punto/riga è presente dal primo fotogramma; nei ripassi, nel glossario e nel riepilogo tutte le righe sono presenti sbiadite e si accendono a tempo con la voce; le mappe partono con centro + primo ramo. Controllo: nessuna pagina ha uno stato senza contenuto (misurato su tutte le 45 pagine).
2. **Font delle etichette:** Figtree Bold maiuscolo spaziato (anche nelle etichette gialle delle card e nei PDF; il pallino dell'elenco della copertina ora è disegnato, non un carattere).
3. **Picco audio:** limitatore sul parlato, picco vero −1,5 dBTP, −16,1 LUFS; stesso numero di fotogrammi (94.626).

## Da chiarire con il prof / da riascoltare (non sono stati modificati o sono dubbi)
1. **Anni:** il prof dice «Siena nel 1983» (a 42:37 nel video nuovo): la sua mappa dice 1985 (morte); la sua slide dice 1983. La speculazione edilizia è «1957» nella slide e nel quiz, «1963» nella **mappa del prof**: nelle mappe ho lasciato 1963 (contenuto identico) e la voce lo dice («segnate entrambe con l'anno 1963»). Il sottotitolo riporta ciò che il prof dice. Sara: confermare con il prof.
2. **Ordine in apertura:** la card «ARGOMENTO 01» (0:40–0:44) compare prima del benvenuto del prof. Non l'ho spostata per non rompere le sigle audio.
3. **Frase del narratore** AN4c (≈ 38:23 nel video nuovo): «Le città invisibili, con una mappa e una piccola analisi guidata»: a schermo non c'è una mappa. Frase di 3 s da tagliare dalla voce o riscrivere (serve la master).
4. **Testa nell'originale:** in alcuni momenti il capo tocca il bordo alto della webcam dell'originale (es. originale 5:00, nel video nuovo 5:44): non è recuperabile.
5. **Voci M2 e M3**: il servizio le ha segnate «DA CONTROLLARE» (parole diverse 4/6 e 5/5); velocità di lettura normale (2,0–2,3 parole/s). Non le ho ascoltate.

## Cosa NON ho potuto verificare
- **Ascolto vero e proprio.** Whisper non è scaricabile dalla rete della chat (modello bloccato) e io non posso ascoltare l'audio. Ho quindi usato: il `.vtt` esistente (fatto da Whisper sul video finale), i testi delle voci Kore, misure ffmpeg (volume, silenzi, offset) e l'allineamento audio. I sottotitoli del prof sono corretti **per contesto** (slide del prof, testi, nomi); i passaggi dubbi sono nell'elenco sopra. La master deve riascoltare 3 punti: 0:50, 25:00, 42:30.
- **Rumore del prof:** il parlato ha già il passa-alto a 80 Hz (energia < 60 Hz −9,6 dB rispetto all'originale), ma il modello `arnndn` citato nelle regole non è nel kit e non ho potuto fare un ascolto: non ho rifatto l'audio del prof.
- **Tempi dei sottotitoli di voci Kore** (benvenuto, ripassi, glossario, mappe): calcolati sul parlato reale (pause misurate) ma non con allineamento forzato: stima ±0,3–0,5 s.
- **Tempi di apparizione** delle card negli approfondimenti: presi dal video vecchio (eventi di cambio immagine), stima ±1 s.
- Pagine del libro: **la lezione 26 non ne ha** (B-bis non si applica).

## Come è stato rifatto (breve)
Audio: lo stesso del video approvato (voci Kore e prof già a −16 LUFS), con le 6 voci nuove delle mappe (normalizzate a −16 LUFS) e il finale del kit. Video: 45 pagine nuove generate in grafica Spagnolo, sincronizzate agli stessi istanti (scene vecchie solo per sigla e schede quiz/titolo, con dissolvenze); prof dall'originale (`Letteratura_Lez26.mp4`, release `mazzotti-letteratura-V`), 5 pezzi continui allineati sull'audio.

## File consegnati
`Letteratura_Lez26_Parte1_1080p.mp4.parte_00..02` + `.sha256` · `Letteratura_Lez26_Parte1.vtt` · `Letteratura_Lez26_slide.pdf` · `Letteratura_Lez26_mappe.pdf` · `Quiz_Letteratura_Lez26.txt` · `quiz_argomenti.json` · `Verifica_finale_Letteratura_Lez26.xlsx` · `compiti.json` · `scheda_pubblicazione.json` · `testo_youtube.txt` · `controllo_minuti.jpg` (1 fotogramma ogni 30 s). Ricomporre: `cat Letteratura_Lez26_Parte1_1080p.mp4.parte_* > Letteratura_Lez26_Parte1_1080p.mp4 && sha256sum -c Letteratura_Lez26_Parte1_1080p.mp4.sha256`.
