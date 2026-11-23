# RAPPORTO DI REVISIONE · Storia · «L'Italia repubblicana» · Parte 1 e Parte 2

Rifatta da zero il 22–23/11/2026 dai materiali del prof (release `mazzotti-storia-V`: video 4274 s, slide, MAPPE LEZIONE 18, test Excel, compiti) con le regole del CLAUDE.md. La vecchia consegna del 16/11 (ramo `consegna-storia-V-lez18`) non è stata usata.

> Tutte le voci Kore sono quelle arrivate dalla master e sono montate (nessuna provvisoria). Controllo con trascrizione (tabella in `voci_controllo.md`): parole e numeri corrispondono; **tre voci hanno l'ampiezza degli ultimi 50 ms sopra 0,03 (M2_04 0,076; SC3_3 0,048; AN2b 0,037)**: le parole ci sono tutte ma la fine è brusca; nel montaggio ogni voce ha una dissolvenza di 30 ms. Se la master le rifà, basta sostituire i file e rimontare. Non ho ascoltato le voci: pronuncia di nomi stranieri e latini non verificata.

## 1. Misure sul file finale

| | Parte 1 | Parte 2 |
|---|---|---|
| durata (min) | 50.22 | 60.43 |
| fotogrammi (letti) | 90394 | 108767 |
| fotogrammi attesi (durata×30) | 90395.0 | 108768.0 |
| peso (MB) | 367.9 | 374.8 |
| risoluzione | 1920x1080 | 1920x1080 |
| volume integrato (LUFS) | -16.3 | -16.4 |
| picco (dBFS, campione) | -1.1 | -1.5 |
| pause > 2,5 s | [] | [] |
| timbro del prof: energia >4 kHz meno >100 Hz (dB), 6 campioni (atteso −9…−20; originale ≈ −19…−22) | [-15.9, -15.2, -16.8, -16.5, -17.4, -13.3] | [-15.2, -17.6, -17.3, -16.5, -16.4, -15.4] |

Codifica: x264 veryfast, CRF 19 (Parte 1) e CRF 21 (Parte 2, per stare sotto i 400 MB), 30 fps, AAC 192k 48 kHz, una sola codifica per Parte.

**controllo_severo.py Parte 1:** esito **OK con passo 9 s** (con passo 10 s l'OCR perde il numero di pagina su alcuni campioni e segnala per errore «1 slide oltre 3 min» e una card con «…» che è rumore di riconoscimento; json di entrambi i passi in `severo_*.json`) · errori: [] · tono voce [148, 164, 148, 148, 156] · chiarezza [1297, 1472, 1309, 1404, 1350] · copertina 135 s

**controllo_severo.py Parte 2:** esito **OK** · errori: [] · tono voce [168, 148, 160, 148, 156] · chiarezza [1382, 1423, 1404, 1193, 1341] · copertina 10 s

## 2. Tagli del prof (fine di ogni pezzo)
Ogni pezzo comincia 0,15–0,35 s prima della prima parola e finisce in una pausa (livello nel taglio sotto −45 dB). Tabella con minuto nel video, sorgente, ultime parole, frase finita:

**Parte 1**

| pezzo | inizio nel video | prime parole | fine nel video | fine (sorgente) | ultime 8 parole | frase finita | livello nel taglio |
|---|---|---|---|---|---|---|---|
| IN1 | 0:37.37 | Buongiorno e benvenuti alla lezione sull'Italia repubblicana. Come… | 3:40.93 | 183.97 s | …discorso. Quindi adesso non faremo altro che ripercorrerlo. | sì | -58 dB |
| P1a_0 | 3:44.93 | E infatti, facendo appunto, sforzandoci di tornare un… | 8:42.03 | 484.67 s | …giorno dopo, figuriamoci concepire piani di aiuto americani. | sì | -48 dB |
| P1b_0 | 9:24.90 | A questa precarietà economica, insomma, si affiancava un… | 12:22.50 | 662.27 s | …anche molto arrabbiato, materialmente povero. più di prima. | sì | -64 dB |
| P1c_0 | 12:58.57 | In questo contesto, in questo contesto è emerse… | 16:34.90 | 880.27 s | …veramente un crocevia temporale Que riguarda molte questioni. | sì | -57 dB |
| P2a_0 | 19:53.07 | Quindi il panorama politico è appunto la nascita… | 27:47.97 | 1355.63 s | …i moderati si riconoscono nella DC, grosso modo. | sì | -52 dB |
| P2b_0 | 28:29.10 | Il partito comunista italiano, il PC, di Togliatti,… | 33:04.10 | 1630.63 s | …Comunque, questo è il panorama italiano del quarantacinque. | sì | -59 dB |
| P2c_0 | 33:47.20 | Ma la svolta istituzionale definitiva avvenne il 2… | 40:26.27 | 2029.70 s | …ed entra in vigore il 1 gennaio 1948 | sì (pausa) | -55 dB |
| P3a_0 | 44:23.07 | Ecco, questa costituzione lo sappiamo, quindi affronto, come… | 45:25.07 | 2096.43 s | …non entra in carica. Quindi c'è la fiducia. | sì | -62 dB |

**Parte 2**

| pezzo | inizio nel video | prime parole | fine nel video | fine (sorgente) | ultime 8 parole | frase finita | livello nel taglio |
|---|---|---|---|---|---|---|---|
| P4a_0 | 1:56.87 | Va bene, e quindi di conseguenza anche la… | 8:21.43 | 2482.90 s | …antisovietica sicuramente. Bene, stagione del centrismo. Allora, insomma. | sì | -53 dB |
| P4b_0 | 9:03.63 | Lo sappiamo, il millovequantotto rappresentò a parte l'anno… | 17:25.93 | 2985.20 s | …colma il divario, negli anni 40 era sprofondata. | sì | -46 dB |
| P5a_0 | 20:52.07 | E negli anni cinquanta, diciamo, torna a una… | 26:37.57 | 3330.70 s | …e in alcuni contesti almeno una volta all'anno. | sì | -49 dB |
| P5b_0 | 27:17.60 | Prima il contadino non andava in vacanza, ma… | 31:30.87 | 3583.97 s | …e in cambio chiedono certe riforme sociali. Come. | sì | -45 dB |
| P6a_0 | 35:30.03 | La scuola media unica? Eh sì, perché prima… | 43:13.07 | 4047.00 s | …riusciremo con i socialisti, antisovietica e antinazionalista, antifascista. | sì | -53 dB |
| P6b_0 | 44:00.30 | Ecco, e quindi anche la Chiesa di Giovan… | 47:47.20 | 4273.90 s | …stragismo. di estrema sinistra e di estrema destra. | sì | -65 dB |

Note: IN1 finisce su «…non faremo altro che ripercorrerlo.»; la false partenza «Ma dal lato italiano, diciamo» è stata tolta (incespicamento). P2c finisce con «…il 1° gennaio 1948» (frase conclusa, senza punto nella trascrizione automatica).

## 3. Struttura e regole (CLAUDE.md §3, §4, §6, §9)
- Sigla 15 s → copertina animata con voce di benvenuto (senza riquadro del prof) → intro del prof sulla copertina (112 s, poi slide «Di cosa parliamo») → per ogni argomento: titolo (`titolo.wav`), prof con slide a card (max 3, frase intera, bordo giallo all'inizio della frase), 1–2 approfondimenti animati con voce Kore, mappa del prof (solo argomenti 2, 5, 6), pillola di ripasso (`repaso.wav`) + schema, quiz di 5 domande (`quiz.wav` a +0,5 s).
- Parte 2: dopo la sigla, copertina animata e **spiegone** della Parte 1 (3 argomenti, con la mappa dell'arg. 2).
- Fine: glossario, ripasso finale, **verifica di sbarramento (10 domande dell'Excel del prof, 80%)** e sigla finale con avviso diritti, poi intro «Compiti» di 3,5 s con jingle e i 4 compiti del prof (tutto nel video della Parte 2).
- Transizioni: `trans.wav` + dissolvenza su ogni cambio di pezzo.
- Dispense A4 orizzontali per Parte (`Storia_Lez18_ParteN_slide.pdf`): stesse slide del video senza riquadro del prof, con strato di testo invisibile; copertina solo «Storia» + titolo; piè «STORIA» e «Pagina N». PDF mappe per Parte (`…_ParteN_mappe.pdf`), copertina con «MAPPE».
- Sottotitoli `.vtt` fatti sul video finale (parlato del prof da riconoscimento automatico con correzioni dei nomi: **da rileggere a campione**; voci Kore dai testi).

## 4. Mappe (come da risposta della master delle 18:45 UTC)
- Mappe del prof (PDF «MAPPE LEZIONE 18»), ridisegnate in vettoriale nel modello BES (5 colori, legenda in alto a destra, testo 36 px), costruite ramo per ramo con la voce, mappa intera ferma ≥ 4 s: **arg. 2** «Come nasce la Repubblica italiana?» (Parte 1), **arg. 5** «Quali sono i principali avvenimenti dell'età detta del centrismo?» e **arg. 6** (Parte 2).
- **Titolo scritto da noi (dichiarato):** la mappa dell'arg. 6 nel PDF del prof non ha la domanda; ho scritto «Come nascono i governi di centrosinistra?» con parole del prof.
- Nella mappa dell'arg. 5 la sigla «Cee» è rispiegata con una nota a piè mappa («Cee: Comunità economica europea»); le parole dei riquadri restano quelle del prof.
- Argomenti 1, 3, 4: il prof non ha mappa → nessuna mappa inventata, l'argomento si chiude con pillola e quiz; nessuna mappa finale della lezione.
- Differenza tra mappa del prof («Fronte popolare democratico») e quiz/Excel («Fronte democratico popolare»): lasciati come sono.

## 5. Immagini e fonti
Tutte dal PDF del prof: carta «Il confine orientale italiano (1920-1954)» e foto Piano INA-Casa (ingrandite 3× con nitidezza, erano 792×470 e 255×392: restano di qualità limitata, da guardare). Nessuna immagine presa dal web; nessuna foto di persone scaricata. Le foto di De Gasperi e di Fanfani–Moro del PDF non sono state usate (non corrispondono a ciò che il prof dice in quel momento).

## 6. Anomalie del materiale del prof (riportate come le dice lui, da portare a Sara)
- **Arg. 1:** «circa il venti per cento delle industrie e il sessanta per cento delle case distrutte» (370–386 s): cifra riconosciuta dal riconoscimento automatico, da riascoltare. Partito repubblicano fuori dal CLN: detto dal prof, non in card.
- **Arg. 2:** il prof dice «Vittorio Emanuele II» (è il III): nome omesso nella card. MSI «fondato a dicembre del 48… del 45»: la card riporta 1945 (nella storia reale 1946). Dice «PC» per PCI e «MS» per MSI: scritti per esteso. Paragone con il Movimento 5 Stelle e riferimento a Fratelli d'Italia nelle card: parole del prof.
- **Arg. 3:** la Costituzione è trattata in modo molto breve (68 s); la card dice «la sappiamo già».
- **Arg. 4:** «1948-1953» e primo settennato di Einaudi come li dice il prof; zona A «che poi verrà all'Italia» al futuro; frase sul Piano Marshall (2556 s) contraddittoria e non usata; Piano INA-Casa: il prof non spiega la sigla (card: «il piano per far costruire case»).
- **Arg. 5:** Corte Costituzionale «non parte nel 48, siamo a quasi dieci anni dopo»; regioni «che non esistono ancora»; «due terzi degli abitanti di Torino» di origine meridionale.
- **Arg. 6:** ENEL detto «ente energetico nazionale» (nome vero: Ente nazionale per l'energia elettrica): usato come lo dice lui anche nelle voci e nelle schede; «Piano Solo architettato nel 1964»; «Pietro Nenni» detto «Pietronelli»; titolo della slide del prof «Centrosinistra (1953-1963)» (i governi di centrosinistra cominciano nel 1962-63): lasciato com'è; Chruščëv scritto «Khrushchev» nella card.
- **Test Excel del prof:** domanda 10 usa «PCI» senza spiegarlo: sullo schermo ho aggiunto «(Partito comunista italiano)»; il file originale non è stato modificato.
- **Refusi corretti nelle nostre slide:** «Centro- Nord» → «Centro-Nord»; nomi propri e accenti dalla trascrizione automatica (Istria, Togliatti, Fanfani, Chruščëv, De Gasperi, Einaudi); sigle PC/MS → PCI/MSI.


## 7. Voci
- Voci Kore già presenti usate dopo controllo con trascrizione (Parakeet): AN*, R*, P*, SC*, GL*, RF*, FIN*. Troncate in fondo e da rifare: AN2a, AN2b, AN6a, R6. Sigle non spiegate nelle voci vecchie (rifatte in `_R2`): R4, AN4c, SC4_4, R6, AN6b, RF2, SC6_2.
- Voci nuove richieste: INTRO1_R2, INTRO2_R2, SP2_1-3, M2_01-08, M5_01-10, M6_01-07 (`voci_da_generare.json` nel ramo di lavoro).
- Numeri e anni in lettere nel testo per la voce, in cifre sullo schermo.

## 8. Cosa è stato verificato e cosa NO
**Verificato con misure (script e controlli nel ramo di lavoro; quattro controlli separati di un agente che non ha montato la lezione):**
- Fotogrammi = durata × 30, 1920×1080, peso < 400 MB, −16 LUFS ±1, picco ≤ −1 dBTP, nessuna pausa > 2,5 s (le schede quiz e compiti hanno un sottofondo morbido), timbro del prof dentro −9…−20 dB (6 campioni per Parte; l'originale è già a −19…−22 dB, la pulizia aggiunge un leggero schiarimento).
- `controllo_severo.py` della master: esito OK su entrambe le Parti (nessuna slide o schermata identica oltre 3 min, nessuna card sola oltre 60 s, nessuna card con «…», copertina intera, intro sulla copertina 112 s).
- `controllo_finale.py` del kit: fotogrammi, peso, scatto quiz a 0,0 s, nessun fermo del prof.
- Tagli del prof: tutti in pausa (livello nel taglio sotto −42 dB) e a frase intera (tabella al §2); card: 208 card confrontate con la trascrizione e con il video a 5 fotogrammi/s (card accesa entro ±1,5 s dall'inizio della frase salvo poche eccezioni elencate sotto).
- Sigle rispiegate a schermo (quiz, schemi, glossario, approfondimenti, titoli, mappe); numeri in cifre a schermo; nome del prof solo nella fascia gialla; piè di pagina senza nome; dispensa = video (stesso ordine e numeri di pagina) con strato di testo invisibile; PDF mappe con copertina «MAPPE»; verifica finale = Excel del prof; compiti = quelli del prof.

**NON verificato / difetti noti (da guardare):**
- **Voci Kore:** non ho potuto ascoltare nulla; le voci nuove erano provvisorie fino al loro arrivo (vedi stato delle voci in testa). Pronuncia dei nomi stranieri e latini, trascrizione e bordi vanno controllati a ogni voce.
- Sincronia labbra/voce: l'audio del prof è tagliato con gli stessi campioni del video; misurato uno scarto costante di circa −0,03 s (entro 0,04 s); non controllato a vista su tutti i pezzi.
- `trans.wav` e dissolvenza a ogni cambio di pezzo: messi dal programma a ogni giunzione, controllati solo a campione.
- Immagini: solo quelle del PDF del prof (carta del confine orientale 792×470, foto INA-Casa 255×392, De Gasperi 469×398, Fanfani–Moro 717×632), ingrandite 2–3× con nitidezza: restano di qualità limitata; la carta è piccola sullo schermo.
- Card: poche card (circa 10 su 208) si accendono fino a 4 s dopo l'inizio della frase che riassumono (frasi lunghe unite da due pezzi) e restano alcuni tratti > 5 s in cui il prof parla di altro (commenti fuori tema, aperture lunghe) senza una card accesa.
- Sottotitoli: i pezzi del prof non coperti dalle card sono riconoscimento automatico con dizionario dei nomi: restano errori di parole; **da rileggere prima della pubblicazione**. Circa il 20% dei cue coperti dalle card parte da 1 a 6 s lontano dalla parola esatta.
- Fine di P5b / inizio di P6a: «…chiedono certe riforme sociali. Come.» e la risposta «La scuola media unica?» sono separate da mappa, pillola e quiz dell'argomento 5 (il prof le dice di seguito, la pausa tra le due frasi è troppo breve per tagliare): **decide Sara**.
- L'approfondimento dell'argomento 6 (AN6a) dura circa 38 s (voce da 40 s in su dopo il rifacimento).
- AAC a bitrate variabile (media 150–180 kb/s) invece di 192k fisso.
- Quiz e compiti: senza voce, con sottofondo musicale morbido e un solo jingle iniziale.


## 9. Note finali
- Parte 2 dura 60,4 min (un poco oltre i 60: l'argomento 6 è lungo e le voci dei compiti sono tutte in fila); resta una sola Parte per argomenti 4–6.
- `controllo_rapido.py`: ESITO OK su entrambe le Parti; foglio e json nel ramo.
- Rispetto alle correzioni della master: schede di ripasso e schema in blu scuro, carta del confine orientale grande, nessuna scheda muta (sottofondo musicale morbido su quiz, verifica e compiti), compiti letti dalla voce COMPITI.
