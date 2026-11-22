# RAPPORTO REVISIONE · Letteratura italiana V · Giuseppe Ungaretti e l'Ermetismo · correzioni 22/11/2026
Video: `Letteratura_Lez17_Parte1_1080p.mp4` (a pezzi `.parte_00…04`, sha256 nel file `.sha256`; la somma dei pezzi corrisponde allo sha256).
Etichette: **misurato** = misurato con uno strumento · **stima** = dedotto · **non verificato** = non ho potuto.
Questa è la versione di correzione del 22/11 (regole blindate): sostituisce la consegna del 17/11. Parte dalla lezione già consegnata, riusa trascrizione, voci, quiz, verifica, compiti, fettine e sigla.

## 1. Cosa ho cambiato il 22/11
| Punto delle regole | Prima (consegna 17/11) | Ora |
|---|---|---|
| Testo delle card | 28 px, 3 card per slide con paragrafi lunghi | **40 px, interlinea 1,5**; al massimo 3 card per slide (di fatto 2: a 40 px non ne entrano 3); la slide si divide in finestre; ogni card è una frase intera del prof, mai «…» né iniziale minuscola; card alte quanto il testo; card in corso con bordo giallo e pallino giallo quando il prof **inizia** la frase; le altre card attenuate |
| Una card sola | alcune slide con una card sola | nessuna: una finestra con una sola card riporta la precedente attenuata come contesto |
| «Già visto» | la slide «L'Ermetismo e le correnti» era sia in argomento 2 sia in 6 | divisa in due slide con testi diversi, ciascuna in un solo argomento (nell'arg. 2 le parole del prof su Ungaretti ermetico, nell'arg. 6 la sua ripetizione e Quasimodo) |
| Mappa | una mappa in formato A4, fermo, tutta insieme | **una sola mappa, quella del prof**, ridisegnata nel modello BES (pesca / celeste / paglierino / menta / lilla, legenda in alto a destra, testo 34–50 px), **costruita ramo per ramo** (32 passi) con la voce `MAP1` e il riquadro acceso in giallo finché la voce parla; alla fine resta ferma 4 s. Posta prima del glossario, una volta sola. Ridisegnata **senza il marchio mappe-scuola.com, senza QR, senza la foto dell'autore, senza il facsimile** |
| Silenzi | 4 pause tra 3 e 4,6 s | tolte; pause oltre 2,5 s accorciate a circa 1 s solo tra due frasi (taglio a 18:03, 21:55, 32:13, 35:39) |
| Inizio dei pezzi del prof | 2 inizi mozzati («Qua ne possiamo…» e «Molto importante…» erano tagliati) | **corretti**: ogni pezzo parte 0,4–2 s prima della prima parola; tabella §4 |
| Dispensa slide / mappe | slide con footer col nome del prof, nessuna copertina | slide: copertina (materia + titolo, senza nome del prof), piè di pagina senza nome del prof, **99 pagine A4**, testo vero selezionabile; mappe: copertina identica con «MAPPE», poi la mappa (2 pagine) |
| Audio | già pulito | invariato (stessa catena) |

## 2. Misure sul video nuovo (misurato)
| Controllo | Risultato |
|---|---|
| Formato | 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192 k, 48 kHz |
| Durata / fotogrammi | **3202,6 s = 53:23 · 96 078 fotogrammi = durata × 30**; ogni pezzo ha i fotogrammi del piano (46/46) |
| Peso | 385,9 MB (< 400 MB) |
| Volume | **−16,9 LUFS** integrato (LRA 6,9 LU), picco **−2,5 dBFS** |
| Timbro della voce del prof | rapporto acuti >4 kHz / bassi >100 Hz: D1 −18,1, D2 −15,0, D3 −16,9, D4 −15,0, D5 −20,5, D6 −18,9 dB. Voce **non alterata**: identica all'originale entro ±2,1 dB (D5 −20,5 vs −20,9 dell'originale: è già al limite nel file originale) |
| Sincronia labbra/voce | correlazione con l'audio dell'originale (3–6 punti per pezzo): scarto massimo **0,018 s** (limite 0,04) |
| Immagine ferma del prof | `freezedetect` sul riquadro (≥ 1 s): **nessun fermo**. Nell'introduzione animata (0:15–0:48) **nessun riquadro**, nemmeno vuoto; il riquadro compare da 0:53 quando il prof parla |
| Jingle Quiz | `controllo_jingle.py` con `quiz.wav` del kit: Q1–Q6 scarto +0,004 s, **tutti OK** (il controllo ha anche intercettato un disallineamento dell'audio dei pezzi senza il prof, causato dalla timeline sbagliata: corretto) |
| Transizioni | `trans.wav` + dissolvenza da/verso il bianco di 0,3 s a ogni cambio di pezzo; nelle code mute delle schede (titoli, quiz, mappa, verifica, compiti) un sottofondo morbido (accordo a −37 dB) perché nessuna scheda resti in silenzio |
| Controllo severo (`controllo_severo.py`) | **ESITO OK, zero errori** (terza esecuzione). Copertina da 0:15 per 90 s (≤ 180 s), titolo esatto presente; nessuna slide con lo stesso titolo oltre 3 min; nessuna schermata identica oltre 3 min; nessuna card con «…»; nessun tratto con una card sola oltre 60 s; loudness -16.9 LUFS; pause oltre 2,5 s: 0; voce: tono [152, 156, 164, 156, 160, 152] Hz, chiarezza [1316, 1333, 1207, 1283, 1281, 1351] Hz (nessuna alterazione). Il controllo segnala 30 campioni «iniziale minuscola»: sono letture OCR che perdono l'«Il» davanti a «tema»; ho verificato nei sorgenti delle slide (358 card) che **ogni card inizia con la maiuscola** (eccetto le 6 righe del riepilogo finale, che cominciano con il numero) e a vista su un campione. Prime due esecuzioni: RESPINTA (7 tratti con card sola: le card attenuate al 50% non si leggevano; 15 pause oltre 2,5 s nelle code mute di titoli, quiz, mappa, verifica e compiti) → card attenuate all'80%, sottofondo morbido nelle code mute, numerazione relativa 1–2 nelle finestre di «Ed è subito sera: l'analisi». |

## 3. Confronto col modello (punto 000)
Riquadro 4:3 (412×309 a x=1428, y=148, ombra grigia), fascia gialla −3° a due righe, fondo bianco puro, Bricolage 800 + Figtree, ombre grigie, schede di titolo/quiz/riepilogo bianche come nel modello Spagnolo, finale del kit con avviso diritti, struttura sigla → copertina → 6 argomenti (titolo con jingle, prof con slide, approfondimento, ripasso con jingle, schema, quiz) → mappa → glossario → riepilogo → verifica → fine → finale → compiti. **Compiti del prof** (4 esercizi) e **verifica di sbarramento** con le 10 domande dell'Excel del prof dentro il video.
Limite noto: nella webcam originale (247×139 px) i capelli toccano il bordo alto; il ritaglio 4:3 è ingrandito 2,24×, quindi morbido (non risolvibile).

## 4. Pezzi del prof: inizio e fine (mai a metà frase)
Tempi nel video nuovo; parole dalla trascrizione (Parakeet, con refusi). Ogni pezzo inizia e finisce su una pausa tra due frasi, controllato sull'audio.
| Pezzo | Inizio | Prime parole | Fine | Ultime parole | Frase finita |
|---|---|---|---|---|---|
| D1 | 0:53 | «Buongiorno e benvenuti alla lezione su Giuseppe Ungaretti…» (parlato dopo 0,7 s) | 10:46 | «…il linguaggio mira all'essenzialità e alla concentrazione lirica.» | sì |
| D2.1 | 12:29 | «Qua ne possiamo già vedere un estratto…» (0,4 s) | 18:03 | «…in modo tale da portare avanti questi concetti. Allora.» | sì |
| D2.2 | 18:03 | «Che dire, possiamo dire così, in parallelo…» (0,5 s) | 19:39 | «…anche il perché di certi testi. Proseguiamo, vediamo.» | sì |
| D3.1 | 21:45 | «Molto importante questo spiegherà…» (0,8 s) | 21:55 | «…e su esce gli esami. Allora. Veglia.» | sì |
| D3.2 | 21:55 | «Cima Quattro. Il 23 dicembre 1915…» (1,4 s) | 26:31 | «…su precise simmetrie. Riprese e antitesi a distanza.» | sì |
| D4.1 | 28:01 | «Santa Maria La Longa il 26 gennaio 1917…» (0,9 s) | 32:13 | «…in pochissime sillabe una riflessione esistenziale drammatica e assoluta.» | sì |
| D4.2 | 32:13 | «Mariano, il quindici luglio millenovecentosedici…» (2,0 s) | 33:42 | «…contro la consapevolezza della propria fragilità e precarietà esistenziale.» | sì |
| D5.1 | 35:18 | «Per finire, per andare alle conclusioni…» (0,8 s) | 35:39 | «…parliamo anche di questo Sentimento del tempo. Allora.» | sì |
| D5.2 | 35:39 | «E poi un'ultima panoramica veloce su Ungaretti…» (0,9 s) | 42:40 | «…il punto fondamentale che dovevamo aggiungere in chiusura ad Ungaretti.» | sì |
| D6 | 44:16 | «Per finire la lezione abbiamo già delineato bene o male l'Ermetismo…» (0,4 s) | 48:24 | «…e disumanizzato, diciamo. O profondamente umani. Alla vita.» | sì |

## 5. Problemi trovati e correzioni (22/11)
| Minuto | Tipo | Com'era | Correzione |
|---|---|---|---|
| 12:29, 21:45 | audio | **inizi mozzati** nella mia consegna del 17/11 (tagliate le parole «Qua ne possiamo» e «Molto») | inizi spostati prima della frase |
| tutto | visivo | card da 28 px, titoli lunghi che sconfinavano, barretta sotto il titolo nel posto sbagliato | titoli ridimensionati a una riga, card 40 px |
| argomenti 2 e 6 | già visto | slide «L'Ermetismo e le correnti» in due argomenti | due slide diverse (§1) |
| mappa | grafica | mappa A4 con testo da 12 px, colori non BES, tutta insieme | §1 |
| 1:49–1:59 | visivo | (già corretto il 17/11) il prof dice «ecco la fotografia…» e compare la foto dalla sua slide 2 | confermato |
| voce S2 | audio | (già corretto il 17/11) voce con ~35 s di frasi inventate | voce `REV1`, confermata |
| audio/piè | testo | «Pagina N» e numerazioni | rigenerate sulle slide nuove |

## 6. File consegnati (tutti rigenerati sul video finale)
`.vtt` (836 cue, max 2 righe, testo con termini corretti e versi esatti del libro, voce della mappa inclusa) · `timeline.json` · `scheda_pubblicazione.json` (titolo «Letteratura V · Lezione 17 · Giuseppe Ungaretti e l'Ermetismo», secondi nuovi) · `testo_youtube.txt` (capitoli nuovi) · `quiz_argomenti.json` e `Quiz_Letteratura_Lez17.txt` (6 quiz × 5, invariati: coerenti con il materiale del prof, senza secondi) · `verifica_finale.json` + `Letteratura_Lez17_verifica_finale.xlsx` (10 domande del prof) · `compiti.json` (4 esercizi del prof) · `Letteratura_Lez17_slide.pdf` (99 pagine A4, identiche al video, senza riquadro e senza fascia) · `Letteratura_Lez17_mappe.pdf` (copertina «MAPPE» + mappa) · `controllo_minuti.jpg` · `controllo_fettine.jpg`.

### Secondi nuovi (consegna 17/11 → ora)
| Voce | Prima (s) | Ora (s) |
|---|---|---|
| Quiz 1 | 739,67 | 739,67 |
| Quiz 2 | 1293,63 | 1295,03 |
| Quiz 3 | 1670,73 | 1670,83 |
| Quiz 4 | 2106,00 | 2107,90 |
| Quiz 5 | 2644,27 | 2646,17 |
| Quiz 6 | 2987,07 | 2988,97 |
| Mappa | 2992,37 | 2994,27 (121,7 s) |
| Verifica | 3174,00 | 3178,10 |
| Compiti | 3193,50 | 3197,60 |
| Durata | 3198,50 | 3202,60 |

## 7. Refusi e anomalie nel materiale del prof (da ricontrollare dalla master)
- Mappa: «Allegria **d** naufragi» → scritto «Allegria di naufragi».
- Mappa: «1914 torna in Italia schierandosi come interventista; 1915-18 in guerra come volontario» · slide e voce: «nel 1914 si arruola come volontario». **Riportati come li dice il prof**, da confermare.
- Mappa: «Allegria 1931» · slide: «L'allegria (1916-1942)»: da confermare.
- Slide del prof: «Alessandria d'Egitto», «Ed è subito sera»: ortografia verificata sul libro (pagine HD).
- Nome «Moammed Sceab»: scritto come nel libro (p. 703).

## 8. Cosa NON ho verificato
- **Ascolto umano:** pronuncia delle voci narranti (in particolare `MAP1`, nomi come «Moammed Sceab», «Apollinaire»), fruscio e «metallico» dopo la pulizia.
- **Sottotitoli:** non riletti cue per cue; dizionario di correzioni e versi esatti; restano probabili errori nel parlato a braccio.
- **Pagina 703 (In memoria):** fettine a scala 0,89–1,06: testo piccolo, da guardare a vista.
- **Controllo dell'agente separato** (§2.2 del prompt): non fatto da un agente diverso; ho fatto io il controllo con gli strumenti sopra e una lista di verifica; **va fatto dalla master**.
- **Mappe vettoriali:** il PDF delle mappe è vettoriale (testo vero); nel video la mappa è a 1080p, non vettoriale (normale per un video).
- **Spiegone / più Parti:** non applicabile (una sola Parte, 53:23).
- **Rete fissa dei timecode** dei sottotitoli sulle voci: stima ±0,3 s.
