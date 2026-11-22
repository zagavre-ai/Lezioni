# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 8 · «Gabriele d'Annunzio» · correzioni 22/11
Consegna sul ramo `revisione-letteratura-V-lez08`. La lezione è in **2 Parti** (decisione della master delle 17:00): Parte 1 = introduzione + argomenti 1 e 2; Parte 2 = spiegone + argomenti 3, 4, 5, glossario, mappa, riepilogo, verifica, compiti. Ogni dato è etichettato **misurato** / **stima** / **non verificato**.

## 1. Misure sui video finali
| Controllo | Parte 1 | Parte 2 |
|---|---|---|
| Durata / fotogrammi | misurato: 38:56,6 · 70 098 fotogrammi (= durata × 30) | misurato: 34:42,7 · 62 482 fotogrammi (= durata × 30) |
| Peso | misurato: 212,6 MB | misurato: 180,6 MB |
| Formato | misurato: 1920×1080, 30 fps, H.264, AAC 192k 48 kHz | idem |
| Jingle Quiz (`controllo_jingle.py`) | misurato: Q1 +0,002 s · Q2 +0,002 s (OK) | misurato: Q3 · Q4 · Q5 +0,002 s (OK) |
| Fermi immagine del prof ≥ 1 s (`freezedetect`) | misurato: nessuno (sulla versione precedente: video dei pezzi del prof invariato) | misurato: nessuno (idem) |

**Controllo severo della master** (`controllo_severo.py`, passo 15 s), eseguito sui video finali: **esito RESPINTA su entrambe le Parti** per i motivi seguenti (nessuno nascosto):
| Voce | Parte 1 | Parte 2 |
|---|---|---|
| Copertina (titolo esatto, ≤ 180 s) | OK: titolo presente, **150 s** | OK: titolo presente |
| Loudness (−16 ±1,5) | OK: −16,5 LUFS | OK: −16,8 LUFS (picco −3,0 dBFS, misurato) |
| Voce del prof (timbro) | OK: tono 145–164 Hz, chiarezza 1290–1390 Hz | OK: tono 148–168 Hz, chiarezza 1243–1435 Hz |
| Pause > 2,5 s | OK: 0 | OK: 0 (dopo la correzione; misurato con `silencedetect`) |
| Card con «…» | OK | **6 campioni = testo delle pagine del libro** (T6, T7: i versi del libro contengono «…»): non sono card |
| Schermata identica > 3 min | OK: nessuna | OK: nessuna |
| Slide con stesso titolo > 3 min | **1 residuo**: «La svolta politica e l'azione», pagina 20, 34:15–37:45 (3,5 min = 209 s): le card «L'impresa di Fiume» (167 s) e «L'esilio sul Garda» (42 s) stanno nella stessa finestra di 2 card, senza cambio di pagina. Non risolto: serviva un quinto approfondimento (la master ne ha concessi 4) | OK |
| Una card sola > 60 s | 1 segnalazione (35:37, 75 s) sulla stessa finestra: **stima: falso positivo dell'OCR** (le card sono 2; il numero «2» del pallino grigio non viene letto) | 1 segnalazione (4:52, 75 s): idem, 2 card visibili (fotogrammi guardati) |
| Durata (45–65 min) | **38:57** | **34:43** |
Il controllo segnala la **durata** perché la lezione è divisa in 2 Parti come deciso dalla master; non ho allungato niente né tagliato parole del prof. Il controllo severo è stato eseguito sulla versione finale del video salvo una correzione successiva solo dell'audio della Parte 2 (pause in silenzio coperte con jingle): rimisurate a mano con `silencedetect`, jingle Quiz e loudness.

## 2. Cosa ho cambiato rispetto alla consegna del 17/11
| Punto | Cosa |
|---|---|
| Testo | card a **40 px, interlinea 1,5** (mai sotto 36); card intere (una frase del prof, mai «…»); **finestre di 2 card** (a 40 px tre non entrano) che scorrono a tempo con il prof; la card in corso ha bordo e pallino giallo, l'altra resta attenuata. Le slide del prof sono quelle del suo PPTX (testo identico); le virgolette dritte sono diventate «…» |
| Schermate ferme | nessuna schermata identica oltre 3 minuti (un residuo di 3,5 min sullo stesso titolo, vedi §1): **4 approfondimenti animati con voce Kore** (A1 «Esistenza e arte» 5:58, A3 svolta del superuomo 19:56, A5 impegno politico 28:25, A7 crisi dell'estetismo nel *Piacere*, Parte 2 6:06), solo dove il prof resta a lungo sulla stessa card (max 4, indicazione della master) |
| Copertina | titolo esatto «Gabriele d'Annunzio»; presentazione con voce Kore **senza riquadro del prof**; il riquadro compare quando il prof parla; la copertina resta **143 s** (limite 180), poi slide «Di cosa parliamo» con gli argomenti |
| Mappa | **una sola mappa, quella del prof** (la mappa delle mappe-scuola ridisegnata: tolti il marchio del sito e le due foto). 25 riquadri non entrano a 34 px in una schermata: **3 schermate** («Mappa 1 di 3»: vita; 2 di 3: poetica e personalità; 3 di 3: opere), legenda BES in ognuna, costruite **ramo per ramo** con la voce Kore (riquadro giallo finché la voce parla), ferme 4 s. Nel video 2:34 (Parte 2, prima del riepilogo). Testo a **40–45 px** (schermata 3: 40 px; etichette dei rami 30–34 px). La sigla «I^ Guerra mondiale» è scritta «Prima guerra mondiale» (sigla rispiegata) |
| Mappa nel PDF | PDF mappe A4 orizzontale: copertina con «MAPPE», poi le 3 schermate (come nel video) |
| Parte 2 | si apre dopo la sigla con lo **spiegone** (voce Kore: ripasso animato degli argomenti 1 e 2, riusando le voci dei ripassi) |
| Audio | parlato del prof dal montaggio, `highpass 80 + arnndn`, **−16 LUFS**, picco limitato (≤ −3 dBTP); jingle Quiz a **+0,002 s** (misurato, 5 su 5); `trans.wav` a ogni stacco con dissolvenza di 1,3 s; jingle su titoli, quiz, verifica e compiti; nessuna scheda in silenzio |
| Piè di pagina | solo «LETTERATURA ITALIANA V» e «Pagina N» (**tolto il nome del docente** da slide, animazioni, PDF); il nome resta solo nella fascia gialla |
| File | video a pezzi con sha256, `.vtt`, `timeline` e `scheda_pubblicazione` di ogni Parte rigenerati sui video finali (secondi nuovi), `verifica_finale.json`, `compiti.json`, PDF slide (63 pagine) e PDF mappe (4 pagine) con **testo selezionabile** |

## 3. Pezzi del prof: inizio e fine (nessun taglio a metà frase)
| Pezzo | Parte | Inizio | Fine | Prime parole | Ultime parole | Frase intera |
|---|---|---|---|---|---|---|
| D0 | 1 | 0:54.9 | 3:22.4 | «Buongiorno e benvenuti alla lezione su…» | «…altro ti.» | sì |
| D1a | 1 | 3:28.6 | 5:56.9 | «Questa è una fotografia del d'annunzio.…» | «…il suo gusto, d'accordo? È stato tutto questo.» | sì |
| D1b | 1 | 6:20.1 | 19:54.6 | «Che nelle scopre già emerge quella…» | «…un superuomo, i suoi protagonisti, i suoi romanzi.» | sì |
| D1c | 1 | 20:17.1 | 23:24.2 | «Non è detto che lo sia,…» | «…avrà anche altre donne in realtà in parallelo.» | sì |
| D2a | 1 | 24:48.7 | 28:23.7 | «Nonostante il disprezzo ostentato per l'esistenza…» | «…gode anche di una certa impunità e immunità.» | sì |
| D2b | 1 | 28:46.5 | 37:36.9 | «In questo senso, no, perché nel…» | «…nel millecentrentotto.» | sì |
| D3a | 2 | 2:37.6 | 6:04.6 | «Dobbiamo assolutamente parlare, in questa seconda…» | «…al fine di evitare il disastro economico.» | sì |
| D3b | 2 | 6:31.2 | 11:07.7 | «vita dispendiosa la conduceva anche lei.…» | «…Metato nell'Arabruzzo, primitivo e magico dei pastori.» | sì |
| D4 | 2 | 12:25.9 | 26:36.6 | «Ecco.…» | «…testo, diciamo così, piuttosto noto, insieme al piacere.» | sì |
| D5 | 2 | 27:33.2 | 29:34.8 | «Per concludere il periodo del notturno.…» | «…annunciare» | sì (fine della registrazione: frase non conclusa) |
Controllo fatto sulla trascrizione automatica (**stima**): i punti di taglio dei 4 approfondimenti cadono su una fine di frase con pausa ≥ 0,5 s. Nel pezzo D5 l'originale del prof termina a 3533,7 s con la frase non conclusa: non allungabile.

## 4. Voci Kore
Voci nuove M1–M5, A1, A3, A5, A7, P2 generate dalla master. **Trascritte e confrontate con i testi** (Parakeet): parole e numeri (1863, 1938, 1884–86, 1897, 1900, 1919…) coincidono. Bordi: A1 (fine 0,070) e A7 (inizio 0,072) hanno ampiezza > 0,03 nei 50 ms di bordo (le altre sotto 0,03); nel montaggio ogni voce ha dissolvenza di 30 ms. «Nietzsche» è stato scritto «Nìce» nel testo voce: la trascrizione ha capito «Nietzsche». **Non ascoltate da un umano.**

## 5. Refusi, anomalie, immagini
- Refusi del PPTX del prof: nessuno certo trovato; ho solo normalizzato le virgolette. Mappa: «I^» → «Prima» (sigla rispiegata); «Gardone R.» → «Gardone Riviera».
- Da confermare col prof: mappa «1898 va a vivere vicino Firenze con Eleonora Duse» (slide: Capponcina, senza anno); mappa «Laudi 1903-12» vs slide «Alcyone 1903».
- Immagini: le due foto della lezione (slide 2 e 5) sono quelle del PPTX del prof (713×850 e 1491×850), non ingrandite; pagine del libro: fettine ad alta risoluzione del PPTX (ritagli esatti degli screen HD, corrispondenza 1,00 misurata sulle fettine 13–26). Nelle fettine restano QR e riquadri «analisi interattiva» del libro dove li ha: **non risolto**. Nessuna immagine scaricata dal web.

## 6. Cosa NON ho verificato
- **Ascolto umano**: pulizia dell'audio (fruscio, ronzio, «metallico»), pronuncia di «Alcyone» e dei nomi, qualità delle voci Kore.
- **Sincronia delle card**: la card in corso cambia ai tempi del montaggio precedente; confronto automatico con la trascrizione su 41 cambi: 20 entro ±1 s, gli altri fino a ~20 s (la frase della card a volte arriva dopo). **Stima**: potrebbero non passare il controllo «bordo giallo ±1 s» in ~10 punti (es. 17:29, 19:20, 26:11, 33:00, 53:14).
- **Sottotitoli** (.vtt): dalla trascrizione automatica con correzioni sistematiche dei nomi; **non riletti cue per cue**; restano errori di riconoscimento. Le voci Kore non sono sottotitolate.
- **Labbra/voce**: video preso dall'originale con lo stesso scarto dell'audio del montaggio (errore di quantizzazione ≤ 0,017 s, **stima**); nessuna misura indipendente sulle labbra. Nessun fermo immagine del prof (riquadro vivo).
- **Agente di controllo separato** (§11 delle regole): non avviato per mancanza di tempo.
- **Testa nel riquadro**: la webcam originale è 246×138 px (ingrandita 2,2×): immagine morbida; la testa è intera nei fotogrammi guardati.
- Il PDF slide ha il testo selezionabile (testo vettoriale), identico alle slide del video **senza** i riquadri (63 slide distinte); le schede di servizio (titoli, ripassi, quiz, approfondimenti, mappa) non hanno numero di pagina.
- **Dispensa**: copertina uguale alla copertina del video (con la card ARGOMENTI) e non «solo materia e titolo».
