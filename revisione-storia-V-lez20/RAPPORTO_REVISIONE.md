# RAPPORTO DI REVISIONE · Storia · «Gli anni Novanta: il mondo post-bipolare» · CORREZIONI 22/11
Chat `claude/keen-hypatia-d76anw` · ramo di consegna `revisione-storia-V-lez20` · 22/11/2026 22:05 UTC.
Ogni dato è etichettato **M** (misurato), **S** (a vista / stima) o **NV** (non verificato).

## 0. Cosa è stato fatto e cosa no (in breve)
- Lezione **rimontata da zero** dall'originale del prof (release `mazzotti-storia-V`, zip 004): il montaggio precedente non era ricostruibile. Slide, mappe, quiz, pillole, quiz, glossario, ripasso finale, verifica, sigle e compiti sono nuovi.
- **Due Parti**, tagliate a fine argomento 4 (decisione approvata dalla master): Parte 1 = 54:09, Parte 2 = 29:25. La Parte 2 è sotto i 50 minuti perché il materiale del prof è breve (CLAUDE.md §3.6: «va bene, non si allunga»).
- **Voci provvisorie ancora presenti:** vedi §3. Finché non arrivano e non sono sostituite **questa consegna non è definitiva**.

## 1. Misure sui video finali (M)
| | Parte 1 | Parte 2 |
|---|---|---|
| File | `Storia_Lez20_Parte1_1080p.mp4` | `Storia_Lez20_Parte2_1080p.mp4` |
| Durata | 54:09 (3249.87 s) | 29:25 (1765.73 s) |
| Fotogrammi / durata×30 | 97496 / 97496 | 52972 / 52972 |
| Peso | 326.9 MB | 152.8 MB |
| Formato | 1920×1080, 30 fps, x264 veryfast (CRF 19 le schede, CRF 22 i pezzi del prof, per stare sotto 400 MB), AAC 192k 48 kHz | idem |
| Volume | -16.3 LUFS, picco -3.2 dBFS | -16.1 LUFS, picco -2.6 dBFS |
| sha256 | `85cee896b1bd2f458c5183e1e548f43ed9bd6f3a46fe933ac8e32a880f252b71` | `898a574d5fbb8c6eff885e4a98a66c15b071dd8b812187b765f95b32032f9586` |

Audio: una sola codifica AAC sull'intero programma (audio rifatto in un passaggio dai pezzi non compressi, così non ci sono scarti di durata). Video: ogni pezzo codificato una volta, uniti senza ricodifica.

### Controlli automatici
- `controllo_finale.py` Parte 1:
```
durata 54:09.9 (3249.9 s) | fotogrammi 97496 (attesi 97496) OK | peso 326.9 MB (311.8 MiB) OK | 1920x1080 OK
quiz 4 scatto 0,0 s: OK
fermi immagine nei pezzi del docente: nessuno OK
volume del parlato (mediana dei pezzi del docente): -16.4 LUFS OK
sottotitoli: 837 blocchi, sovrapposti 0, oltre la fine 0, attacco sulla voce entro 0,3 s: 71% di 21 verificabili DA GUARDARE
foglio di miniature: out/Storia_Lez20_Parte1_1080p.mp4.miniature.jpg
ESITO: DA SISTEMARE: sottotitoli

```
- `controllo_finale.py` Parte 2:
```
durata 29:25.7 (1765.7 s) | fotogrammi 52972 (attesi 52972) OK | peso 152.8 MB (145.7 MiB) OK | 1920x1080 OK
quiz 4 scatto 0,0 s: OK
fermi immagine nei pezzi del docente: nessuno OK
volume del parlato (mediana dei pezzi del docente): -15.8 LUFS OK
sottotitoli: 430 blocchi, sovrapposti 0, oltre la fine 0, attacco sulla voce entro 0,3 s: 53% di 17 verificabili DA GUARDARE
foglio di miniature: out/Storia_Lez20_Parte2_1080p.mp4.miniature.jpg
ESITO: DA SISTEMARE: sottotitoli

```
- `controllo_severo.py` Parte 1 (M): copertina 150 s; slide stesso titolo >3 min: 0; schermate identiche >3 min: 0; card con puntini: 0; card che iniziano minuscole: 0; una card sola >60 s: 0; pause >2,5 s: 5; esito: **RESPINTA** — errori: ['5 pause > 2,5 s']
- `controllo_severo.py` Parte 2 (M): copertina 0 s; slide stesso titolo >3 min: 0; schermate identiche >3 min: 0; card con puntini: 0; card che iniziano minuscole: 0; una card sola >60 s: 0; pause >2,5 s: 8; esito: **RESPINTA** — errori: ['titolo copertina incompleto: gli anni novanta mondo post bipolare', 'copertina non trovata', 'durata 29.43 min', '8 pause > 2,5 s'] — «copertina non trovata» e «durata < 50 min» sono attesi: la Parte 2 non ha copertina (si apre con sigla e spiegone) ed è breve per scelta approvata.
- Pause >2,5 s: sono le code silenziose di 4 s con la mappa intera ferma (richieste dal §6), le code dei jingle delle schede titolo/quiz e, finché sono provvisorie, i silenzi delle voci non ancora arrivate. Nel parlato del prof non ci sono pause >2,5 s (M, rilevamento sulla trascrizione: nessun intervallo da accorciare).
- Quiz: scatto del jingle a 0,0 s su tutte e 8 le schede (M).
- Fermi immagine ≥1 s nei pezzi del prof: nessuno (M, `freezedetect`). Resta una fermata di 0,8 s all'inizio di ogni pezzo (fotogramma fisso con dissolvenza, 24 fotogrammi) e di 0,5 s in coda (S).
- **Timbro del prof (M):** acuti >4 kHz meno volume >100 Hz, originale −17,7 dB; nei pezzi finali: D0 -17.4, D1 -17.0, A1a -17.1, A1b -16.3, A2 -17.4, A3a -16.6, A3b -15.6, A4 -16.7, A5 -15.6, A6 -17.0, A7 -15.6, A8 -16.1 dB → tutti tra −9 e −20 (nessun filtro che cambi il timbro: solo passa-alto 70 Hz, riduzione rumore leggera, guadagno e limitatore).
- Sottotitoli: `Storia_Lez20_Parte1.vtt` e `..._Parte2.vtt`, ricavati dalla trascrizione del prof con i tempi parola per parola rimappati sul video finale, termini corretti (Iugoslavia, Eltsin, Milošević, Gorbaciov, Tienanmen, URSS, NATO, Al-Qaeda…) e le frasi delle voci Kore. Il controllo «attacco sulla voce» di `controllo_finale.py` dà 71 % (P1) e 53 % (P2) di blocchi entro 0,3 s su pochi blocchi verificabili (21 e 17): la mediana dello scarto è 0,02 s (M), ma la metrica automatica è severa sui blocchi che seguono un jingle. **NV: ascolto completo non fatto.** Residui di trascrizione automatica possibili nei sottotitoli del prof (parole non riconosciute): da controllare a campione.

## 2. Cosa è cambiato rispetto alla consegna precedente (punti del prompt 22/11)
| # | Punto | Esito |
|---|---|---|
| 1 | Mappe del prof, ridisegnate nel modello BES, costruite ramo per ramo con la voce | **Fatto per le 4 mappe del PDF del prof** (Iugoslavia, Europa, Italia, globalizzazione), identiche per struttura, frecce e parole, titolo = domanda del prof; legenda a 5 colori in alto a destra; testo 38–40 px; un riquadro alla volta, giallo mentre la voce lo legge, mappa intera ferma 4 s. Togliere tutte le mappe inventate: **fatto** (nessuna mappa per gli argomenti 1, 2, 6, 7 e nessuna mappa finale, come da messaggio della master 19:25). I colori sono una mia scelta per categoria (pesca centro; celeste date; paglierino parole chiave; menta esempi; lilla conseguenze): la master li ricontrolli. Il titolo della mappa Iugoslavia ha «URSS (Unione Sovietica)» perché ogni sigla va spiegata. |
| 2 | Slide del prof: card a 40 px, max 3 card intere, bordo giallo all'inizio della frase, nessuna schermata identica oltre 3 minuti | **Fatto.** Card intere (mai «…»), testo 40 px (interlinea 1,5; le viste «focus» 48 px), massimo 2–3 card per pagina in finestra scorrevole, bordo giallo e pallino all'inizio della frase (tabella §6). Sotto-slide a finestra: ogni pagina che dura >150 s alterna la vista d'insieme e una vista «focus» sulla card con titolo e numero di pagina propri (ogni vista ha il suo «Pagina N»). Riquadro 4:3 (412×309 a x=1428, y=148) con ombra grigia. |
| 3 | Introduzione animata senza riquadro; nome del prof mai detto/scritto | Copertina animata con voce di benvenuto **senza riquadro**; il riquadro compare con la prima parola del prof. Il nome del prof è solo nella fascia gialla. **Attenzione:** la voce di benvenuto provvisoria (`INTRO1`) dice il nome: va sostituita con `INTRO1_N` (richiesta alla master). Nelle schede animate non compare. |
| 4 | Copertina con titolo esatto; intro ≤3 min; poi «Di cosa parliamo» | Titolo «GLI ANNI NOVANTA: IL MONDO POST-BIPOLARE». Copertina+introduzione = 150 s (M, controllo severo). Poi slide «Gli argomenti di oggi». |
| 5 | Spiegone all'inizio della Parte 2 | **Fatto:** SP0 + ripasso degli argomenti 1–5 con le voci `R1`–`R5` già fatte, ciascuno con l'immagine del prof e, per gli argomenti 3–5, la sua mappa. La master aveva scritto «ciascuna mappa una volta sola»: nello spiegone le mappe tornano perché il §3.6 le prevede; se non va, si tolgono. |
| 6 | Refusi del prof | vedi §5 |
| 7 | Audio −16 LUFS, pause lunghe, timbro | −16 LUFS (M); timbro intatto (M); nessuna pausa >2,5 s nel prof (M). |
| 8 | Dispensa identica al video + PDF mappe | **Fatto:** `Storia_Lez20_Parte1_dispensa.pdf` e `..._Parte2_dispensa.pdf` (A4 orizzontale; copertina con solo materia e titolo; piè di pagina «STORIA» + «Pagina N», nessun nome del prof) e `Storia_Lez20_mappe.pdf` (copertina identica + «MAPPE»). Le pagine sono HTML stampato in PDF: il testo è vero e selezionabile (equivale allo strato invisibile). Le pagine «focus» e le immagini del prof sono incluse come nel video. |
| 9 | Lezione 18 | non è la mia lezione. |

## 3. Voci
- **Voci provvisorie presenti in questa consegna:**
- `INTRO1_N`: INTRO1 (dice il nome del prof)
- `PS2_4`: Dopo la Guerra del Golfo Bush Senior non depone Saddam Hussein: per molti conservatori americani è stato troppo leggero, e non viene rielett
- `PS3_4`: In Kosovo la NATO interviene anche senza il permesso dell'ONU; alla fine Milosevic viene arrestato e portato davanti alla Corte penale inter
- `FINP1`: La prima parte finisce qui. Nella parte successiva trovi gli ultimi argomenti, il glossario, la verifica finale e i compiti.
- `SP0`: Prima di continuare, facciamo un ripasso di tutto quello che abbiamo visto nella parte precedente, argomento per argomento.
- `COMP1`: Analizza le conseguenze geopolitiche ed economiche del crollo dell'Unione Sovietica nel 1991, spiegando la tesi della "fine della storia" di
- `COMP2`: Ricostruisci le cause e le principali fasi delle guerre nella ex Iugoslavia negli anni Novanta, soffermandoti sul conflitto in Bosnia Erzego
- `COMP3`: Descrivi le principali trasformazioni politiche ed economiche dell'Europa e dell'Italia negli anni Novanta, illustrando la riunificazione te
- `COMP4`: Esamina le dinamiche della globalizzazione e i nuovi equilibri economici in Asia alla fine del XX secolo, analizzando il modello cinese del 
- Voci Kore già esistenti riusate (85 file dal ramo `voci-storia-V-lez20`): ognuna **trascritta** (Parakeet) e **confrontata parola per parola** con il suo testo (numeri in lettere convertiti), **bordi** misurati (ampiezza negli ultimi 50 ms < 0,03) e ogni voce portata a −16 LUFS con dissolvenze di 30–35 ms (M). Esito: tutte entro il 90 % di corrispondenza e bordi < 0,03 tranne voci **non usate** (GL1, INTRO1 in sostituzione, MAP*, MAPF1, che nel montaggio non compaiono) e differenze di sola grafia del riconoscitore (centrodestra / centro destra, Jugoslavia / Iugoslavia, Qaida / Qaeda). Da riascoltare a mano: `PS5_3` (il riconoscitore non ha trovato l'ultima parola «inedito»: possibile taglio, **NV**).
- **Pronuncia dei nomi stranieri e latini: NV** (non posso ascoltare). Da far controllare: Fukuyama, Eltsin, Tienanmen, Srebrenica, Maastricht, Al-Qaeda, Milošević, Dayton, Seattle.
- Testi: solo dal materiale del prof. Controllati contro la trascrizione: i fatti degli approfondimenti (Dayton 1995, Montenegro 2006, Kosovo 2008, Tangentopoli, Putin) sono tutti nel parlato del prof (S).
- Numeri e anni: in lettere nelle voci, in cifre sullo schermo (conversione automatica, M su tutti i testi).
- Righe di pillola: per gli argomenti 2 e 3 le voci esistenti erano 3, le regole chiedono 4–6: ho aggiunto una riga a testo del prof (`PS2_4`, `PS3_4`), da far generare.

## 4. Struttura montata (tempi misurati)

**Parte 1**

| Pezzo | Inizio | Durata (s) |
|---|---|---|
| SIGLA1 | 0:00 | 15.0 |
| COVER | 0:15 | 29.8 |
| D0 | 0:44 | 142.5 |
| D1 | 3:07 | 92.0 |
| T1 | 4:39 | 3.4 |
| DA1a | 4:42 | 360.5 |
| AN1a | 10:43 | 31.2 |
| DA1b | 11:14 | 738.7 |
| AP1 | 23:33 | 61.5 |
| PI1 | 24:34 | 39.4 |
| Q1 | 25:14 | 4.2 |
| T2 | 25:18 | 3.4 |
| DA2 | 25:21 | 327.7 |
| AP2 | 30:49 | 60.0 |
| PI2 | 31:49 | 40.6 |
| Q2 | 32:29 | 4.2 |
| T3 | 32:34 | 3.4 |
| DA3a | 32:37 | 365.8 |
| AP3 | 38:43 | 57.9 |
| DA3b | 39:41 | 105.7 |
| AN3a | 41:26 | 36.3 |
| MAP3 | 42:03 | 28.6 |
| PI3 | 42:31 | 41.6 |
| Q3 | 43:13 | 4.2 |
| T4 | 43:17 | 3.4 |
| DA4 | 43:21 | 505.4 |
| AP4 | 51:46 | 52.6 |
| MAP4 | 52:38 | 30.1 |
| PI4 | 53:09 | 41.9 |
| Q4 | 53:50 | 4.2 |
| FINP1 | 53:55 | 9.8 |
| SIGF1 | 54:04 | 5.0 |

**Parte 2**

| Pezzo | Inizio | Durata (s) |
|---|---|---|
| SIGLA2 | 0:00 | 15.0 |
| SP0 | 0:15 | 9.0 |
| SP1 | 0:24 | 32.1 |
| SP2 | 0:56 | 26.9 |
| SP3 | 1:23 | 25.9 |
| SP4 | 1:48 | 28.2 |
| SP5 | 2:17 | 28.3 |
| T5 | 2:45 | 3.4 |
| DA5 | 2:48 | 285.0 |
| AP5 | 7:33 | 47.9 |
| MAP5 | 8:21 | 31.1 |
| PI5 | 8:52 | 43.5 |
| Q5 | 9:36 | 4.2 |
| T6 | 9:40 | 3.4 |
| DA6 | 9:44 | 183.4 |
| AP6 | 12:47 | 48.2 |
| PI6 | 13:35 | 45.4 |
| Q6 | 14:21 | 4.2 |
| T7 | 14:25 | 3.4 |
| DA7 | 14:28 | 125.2 |
| AP7 | 16:33 | 52.5 |
| PI7 | 17:26 | 35.2 |
| Q7 | 18:01 | 4.2 |
| T8 | 18:05 | 3.4 |
| DA8 | 18:09 | 158.9 |
| AP8 | 20:48 | 53.8 |
| MAP8 | 21:41 | 32.9 |
| PI8 | 22:14 | 39.9 |
| Q8 | 22:54 | 4.2 |
| GLOSS | 22:58 | 43.2 |
| RF1 | 23:42 | 32.0 |
| RF2 | 24:14 | 26.8 |
| RF3 | 24:40 | 25.8 |
| RF4 | 25:06 | 28.1 |
| RF5 | 25:34 | 28.2 |
| RF6 | 26:03 | 28.1 |
| RF7 | 26:31 | 23.6 |
| RF8 | 26:54 | 22.4 |
| RFIN | 27:17 | 29.7 |
| FIN | 27:46 | 10.1 |
| VERIFICA | 27:57 | 4.6 |
| SIGF2 | 28:01 | 5.0 |
| COMPITI | 28:06 | 3.5 |
| COMP1 | 28:10 | 19.8 |
| COMP2 | 28:29 | 19.4 |
| COMP3 | 28:49 | 17.4 |
| COMP4 | 29:06 | 19.0 |


## 5. Refusi e anomalie nel materiale del prof
Corretti nelle nostre slide/dispensa (i file originali non sono toccati):
- «Boris **Elcin**» → «Boris **Eltsin**» (slide arg. 1; test finale e compiti: stesso refuso, corretto nei nostri JSON).
- «dell'ex **rft**» → «dell'ex **RFT** (Repubblica Federale Tedesca)» (slide arg. 4), sigla da spiegare.
- Sigle spiegate sullo schermo alla prima comparsa in ogni card: USA, URSS, UE, NATO, PSI, RFT. A voce non posso spiegarle: la voce del prof non si tocca (le voci Kore le spiegano dove il testo lo permette, es. «Unione Sovietica»).
- Nel test finale: «Elcin» → «Eltsin».
- Nelle mappe del prof non ho trovato refusi (S).
**Anomalie (riportate come le dice il prof, nessun calcolo):**
- Mappa Iugoslavia: «Kosovo (1998)»; la slide dice «nel 1999 … intervento NATO» e il prof dice «98-99»: i due anni sono coerenti con eventi diversi, ma da far vedere a Sara.
- A voce il prof dice che Gorbaciov «all'epoca» era presidente della Russia (era presidente dell'URSS): lasciato com'è.
- A voce il prof pronuncia «Yelsin/Yeltsin/Nielsen»: nei sottotitoli «Eltsin».
- Il prof chiama «Jugoslavia» la ex Iugoslavia a voce; sullo schermo «Iugoslavia» (grafia italiana della slide).


## 6. Tagli, card e immagini

#### Parte 1: fine di ogni pezzo del docente

| Pezzo | Fine (minuto) | Ultime 8 parole (trascrizione) | Frase finita |
|---|---|---|---|
| A1a | 10:42 | …siamo all'indomani del del dicembre novantuno. | sì |
| A1b | 23:32 | …vincitori invece della guerra fredda, gli Stati Uniti. | sì |
| A2 | 30:48 | …Uniti interverranno anche, non solo gli Stati Uniti. | sì |
| A3a | 38:42 | …stato sovrano, e quindi non è proprio corretto. | sì |
| A3b | 41:26 | …ritorna alla prima guerra mondiale, se ci pensiamo. | sì |
| A4 | 51:45 | …Però, ecco, come dire, sono ancora questioni aperte. | sì |

#### Parte 1: accensione delle card (tutti i punti)

| Video | Pezzo | Card | Frase del prof vicina | Scarto da inizio frase |
|---|---|---|---|---|
| 4:43 | A1a | 1 | In modo tale poi da concludere il crollo dell'Unione Sovietica, riflet | +0.0 s |
| 5:41 | A1a | 2 | Questo mutamento epocale portò inizialmente alcuni intellettuali, come | -0.0 s |
| 8:56 | A1a | 3 | Spinte autonomistiche e anche secessionistiche, e nuove aree di instab | +0.0 s |
| 11:15 | A1b | 3 | Che cosa fare? | -0.0 s |
| 18:04 | A1b | 4 | scusate, l'ex agente segreto dei servizi segreti sovietici che Gebe. | +0.0 s |
| 19:44 | A1b | 4 | Questa è la situazione in Russia. Ma la situazione gli anni 90 russi s | -0.0 s |
| 25:22 | A2 | 1 | Allora, mentre l'ex spazio sovietico si frammentava, lo scenario inter | -0.0 s |
| 25:41 | A2 | 2 | Sotto la presidenza di George. | -0.0 s |
| 27:49 | A2 | 2 | Ma intervento armato no? Quando si tratta del Kuit, invece, gli Stati  | +0.0 s |
| 29:30 | A2 | 3 | Bene, la presidenza Clinton | +0.0 s |
| 32:38 | A3a | 1 | Cerchiamo di capire. Contemporaneamente, l'Europa si è trovata a gesti | -0.0 s |
| 34:09 | A3a | 2 | E allora comincia una guerra che per certi aspetti è civile, una guerr | +0.2 s |
| 36:50 | A3a | 3 | Dopo numerose risoluzioni e dibattite all'ONU, | -0.0 s |
| 43:21 | A4 | 1 | Europa occidentale, ecco, nel resto del continente europeo gli anni no | +0.0 s |
| 44:02 | A4 | 3 | Problemi che anche la Russia sperimenta e non solo la Russia, economia | -0.1 s |
| 45:17 | A4 | 2 | Il cammino verso l'integrazione europea ha compiuto un passo decisivo  | +0.0 s |
| 47:41 | A4 | 4 | Anche se molti stati passati poi all'estrema destra come l'Ungheria pe | -0.4 s |

#### Parte 2: fine di ogni pezzo del docente

| Pezzo | Fine (minuto) | Ultime 8 parole (trascrizione) | Frase finita |
|---|---|---|---|
| A5 | 7:33 | …dal dai governi di coalizione nazionale. | sì |
| A6 | 12:46 | …ad attaccare poi i simboli dell'Occidente. | sì |
| A7 | 16:33 | …a lui e in alcuni casi lo supera. | sì |
| A8 | 20:47 | …nel mondo dal 2000 in poi. | sì |

#### Parte 2: accensione delle card (tutti i punti)

| Video | Pezzo | Card | Frase del prof vicina | Scarto da inizio frase |
|---|---|---|---|---|
| 2:49 | A5 | 1 | È molto importante, visto che ne accennavamo a chiusura di questa lezi | +0.0 s |
| 3:05 | A5 | 2 | a partire dalle elezioni del novantaquattro quando | -0.0 s |
| 4:12 | A5 | 3 | Delle libertà di Silvio Berlusconi, imprenditore televisivo. | +0.0 s |
| 5:54 | A5 | 4 | riesce a governare due anni e affronta come governò Berlusconi prima. | +0.2 s |
| 9:44 | A6 | 1 | Va bene, adesso proviamo ad affrontare... | +0.0 s |
| 10:20 | A6 | 2 | Il periodo ha visto anche la preoccupante diffusione del fondamentalis | +0.2 s |
| 10:41 | A6 | 3 | In Africa alle croniche difficoltà legate a povertà e conflitti intern | +0.4 s |
| 10:58 | A6 | 4 | E l'elezione del carcerato, è il caso di dirlo Nelson Mandela, | -0.3 s |
| 11:08 | A6 | 5 | L'America Latina ha invece vissuto una complessa transizione verso la  | -0.4 s |
| 11:41 | A6 | 2 | Ora, ricordatevi che Al Qaida, fondata da Osama bin Laden, opera in Af | -0.3 s |
| 14:29 | A7 | 1 | Ecco, per concludere vediamo i nuovi protagonisti. | -0.0 s |
| 15:12 | A7 | 2 | Accanto alla Cina le cosiddette Tigri asiatiche, come la Corea del Sud | -0.0 s |
| 15:29 | A7 | 4 | Anche l'India, se per questo è registrato un forte boom economico. Tra | -0.0 s |
| 16:02 | A7 | 3 | Tutte le nazioni sovrane. Il Giappone ha attraversato al contrario un  | +0.0 s |
| 18:10 | A8 | 1 | Ed è il caso, appunto, di parlare della globalizzazione. Tutti questi  | -0.0 s |
| 18:26 | A8 | 2 | Nel bene e nel male, questo fenomeno è stato straordinariamente accele | +0.5 s |
| 18:46 | A8 | 3 | dall'altro ha sollevato forti critiche e resistenze. | +0.2 s |
| 19:36 | A8 | 4 | Il 2000 si è aperto dunque con un pianeta globalizzato, segnato da una | +0.0 s |

**Tabella immagine del prof → argomento (uno solo)**
| Immagine (PDF slide) | Argomento in cui compare | Minuto video | Qualità |
|---|---|---|---|
| Carta «Dove si trova la Cecenia» (542×675) | 1 | 19:30 (Parte 1) | originale, nitida (S) |
| Carta «Dove si trova il Kuwait» (253×333) | 2 | 27:06 (Parte 1) | **piccola**: ingrandita 2,2× con Lanczos e nitidezza leggera (S) |
| Carta «L'ex Iugoslavia 1991-2008» (1231×748) | 3 | 39:42 (Parte 1) | originale, nitida (S) |
| Carta «Le tappe dell'integrazione europea» (783×655) | 4 | 48:58 (Parte 1) | originale (S) |
| Ritratti Berlusconi (298×367) e Prodi (216×487) | 5 | 6:41 (Parte 2) | **piccoli**: ingranditi 1,4–1,8× con Lanczos e nitidezza leggera, tratti invariati (S) |
Le immagini sono quelle del PDF del prof alla massima risoluzione disponibile; non scaricato nulla dal web. Il prof fa vedere la carta del Kuwait solo per 3,5 s: l'ho tenuta mentre parla del Kuwait (la mostro dove lo cita).

## 7. Controllo dell'agente separato
_Controllo dell'agente separato non ancora eseguito._

## 8. Cosa NON ho verificato (NV)
- Ascolto delle voci Kore (pronuncia, interpretazione): nessun ascolto possibile qui.
- Sincronia labbra/voce: i pezzi del prof sono tagliati con gli stessi istanti sull'audio e sul video dello stesso file (scarto 0 per costruzione); misura indipendente con tracciamento delle labbra non fatta.
- Il riquadro del prof ha la testa tagliata in alto **nell'originale** (la webcam è già così nel video del prof): non recuperabile.
- La risoluzione della webcam è bassa (246×138 nell'originale a 1092×614): ritaglio 4:3 centrato sul volto e ingrandito a 412×309, un po' morbido.
- Immagini piccole del prof: vedi §6.
- «Ripetizioni e incespicamenti» del prof: tolte solo le pause; non ho tagliato interiezioni ed esitazioni dentro le frasi (per non rischiare tagli a metà frase).
- Quiz, test e compiti: testi dei JSON precedenti (quiz 8×5, verifica da 10 domande dal file Excel del prof, compiti 4 esercizi), con i refusi corretti; la verifica nel video è una scheda con jingle (come i quiz) e le domande sono in `verifica_finale.json`: se la master vuole le domande lette nel video, va deciso.
- Compiti nel video: schede con il testo del prof e voce (provvisoria finché non arrivano `COMP1–4`).
