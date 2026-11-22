# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 18 · Eugenio Montale
**Correzioni del 22/11/2026** (secondo giro, sopra la consegna del 17/11). Video: `Letteratura_Lez18_Parte1_1080p.mp4` (a pezzi `.parte_NN`, sha256 nel file `.sha256`).
Etichette: **misurato** = con uno strumento; **stima** = dedotto; **non verificato** = non potuto.

## 1. Cosa ho cambiato in questo giro
| Punto | Prima (17/11) | Ora (22/11) |
|---|---|---|
| Testo delle card | 30 px, 3 card lunghe per slide | **40 px**, interlinea 1,5, **al massimo 3 card intere** per slide (di solito 2); ogni card è una frase/paragrafo intero del prof, mai «…»; l'ultima card non sta mai sola se c'è la precedente |
| Mappe | 7 inserti con mappa spezzettata + mappa del prof in 1 pagina piccola | **una sola mappa, quella del prof**, in **3 schermate** BES (vita / poetica / opere), testo 34–54 px, legenda in ogni schermata, costruita **ramo per ramo** con una voce Kore (riquadro in giallo finché la voce parla) e ferma 4 s a fine ramo; messa **una volta sola**, prima del glossario (decisione master 22/11: niente mappa intera rimpicciolita). Ridisegnata senza il marchio mappe-scuola.com e senza le due foto |
| Colori mappa | arancio/verde del sito | pesca = concetto centrale; celeste = date e sequenze; paglierino = parole chiave; menta = esempi e opere; lilla = conseguenze |
| Introduzione | copertina con voce, poi il prof | copertina con voce di benvenuto **senza riquadro del prof**, slide «Di cosa parliamo» con le 6 card che si accendono quando la voce nomina l'argomento, poi il prof sopra la copertina (**69,5 s**, < 3 min) |
| Pause del prof > 2,5 s | 6 pause da 2,5 a 4,3 s | accorciate a ~1 s (tagli solo fra due frasi): 347,8; 560,0; 625,8; 769,3; 1011,1; 1215,9 s dell'originale (−13,0 s in tutto) |
| «Già visto» | la slide «Satura» tornava nell'argomento 6 | ogni slide del prof compare in **un solo argomento**: «La storia» (orig. 27:49) si vede sulla slide dell'argomento 6 |
| Piè di pagina / nome del prof | «…· Prof. Giorgio Mazzotti» | solo «LETTERATURA ITALIANA V» e «Pagina N» (il nome compare solo nella fascia gialla) |
| Dispensa | slide su A4 con piè col nome | **110 pagine** A4 orizzontale = ogni slide del video senza riquadro e fascia; testo vero selezionabile; copertina solo materia e titolo; PDF mappe a parte con copertina «MAPPE» |
| Durata | 53:39,5 | 50:31,1: ≥ 50 min non richiesto per lezioni con solo materiale del prof (regola 3.6); i secondi dei quiz cambiano (§5) |

## 2. Esito del controllo severo (`controllo_severo.py`)
**Il `controllo_severo.py` NON è arrivato a esito su questa versione finale**: sulla versione precedente ha girato oltre 40 minuti (tesseract su 600 fotogrammi) senza finire e l'ho interrotto alla scadenza; **esito non ottenuto, non OK**. Al suo posto ho fatto fare a un **agente indipendente** la lista del §11 (misure sul video e sul PDF). Difetti che ha trovato e che **ho corretto** in questa versione: taglio di D0 a metà frase («…beh…» ora la frase è intera); 4 card accese in ritardo (Il correlativo oggettivo, Il testo di *Spesso il male*, L'angoscia della memoria, Il rifiuto delle ideologie); refusi nei sottotitoli (virandello, Vieux, Mollussi, redità, scapro, buffere d'altro, diallettali, Exenia, viggente); volume del prof (era a −14…−15 LUFS, ora −16,1 in tutto) e delle voci (−17…−18, alzate); bordi della voce della mappa (dissolvenze di 30 ms); testo della mappa (ora 38–54 px, prima 30–36); riquadri della mappa in anticipo sulla voce; copertina della dispensa (solo materia e titolo); schede VER/CI1/COMP/FIN1 senza suono (ora `trans.wav`) e CI1 accorciata a 3,6 s.
**Difetti dell'agente NON corretti (decide la master):**
1. Residuo del prof sul montaggio a 9:01–9:10 («Ripetiamo le slide… per costruire montaggio… Vabbè»): taglio in mezzo al parlato, non fatto per non toccare le parole del prof senza decisione.
2. Tratti di 78–118 s del prof senza card accesa (2:02–3:40, 7:19–9:09, 19:37–21:35, 42:06–43:25: il prof parla in generale) e 5 tratti con una sola card accesa oltre 60 s (la slide ha 2–3 card visibili). Nessuna schermata supera i 3 minuti.
3. Schede titolo, quiz, ripasso, fine, verifica, compiti su fondo bianco: l'agente ricorda che §4 le vuole in blu scuro animato; non rifatte.
4. VER→SFIN e SFIN→CI1: tagli secchi bianco/nero (la sigla finale è il file del kit).
5. Pagine PDF con le poesie: testo solo come immagine (sono le scansioni del libro).
6. Quiz: la scheda_pubblicazione ha il titolo con «Lezione 18» (titolo standard richiesto dalle regole di consegna).
7. Pause tra i rami della mappa: 4 s di fermo a fine di ogni schermata (misurato dall'agente); la pausa vocale fra rami è breve.
8. Font monospazio nella sigla del kit («[ANALISI TESTUALE]»).

## 3. Misure sul video finale
| Controllo | Risultato |
|---|---|
| Formato | 1920×1080, 30 fps, x264 veryfast, AAC 192k 48 kHz; **50:31,1**, **90 934** fotogrammi = durata × 30; 159,4 MB in 2 parti ≤ 90 MB, sha256 verificato (**misurato**) |
| Volume | **−16,1 LUFS** integrato (LRA 5,9), true peak **−1,2 dBTP** (**misurato**) |
| Jingle quiz (`controllo_jingle.py`) | Q1…Q6 scarto **0,000 s** OK (**misurato**) |
| Sincronia labbra/voce | audio contro originale, D0…D6: scarto **−0,015 s** (≤ 0,04; **misurato**); il video del prof è tagliato con la stessa mappa delle pause (un primo montaggio perdeva 1 fotogramma per taglio: **trovato e corretto**, differenza fotogramma/originale a 0 nei 3 punti controllati) |
| Fermi immagine del prof | `freezedetect` (versione precedente dello stesso montaggio): nessuno dentro i pezzi del prof (**misurato**); riquadro assente da copertina con voce e da «Di cosa parliamo» |
| PDF | slide **110 pagine** A4 orizzontale = slide del video (copertina senza card ARGOMENTI); mappe: copertina «MAPPE» + 3 schermate (**misurato**) |

## 4. Fine e inizio di ogni pezzo del prof
| Pezzo | Minuto nuovo | Prime parole | Ultime parole | Frase finita |
|---|---|---|---|---|
| D0 | 0:45.0–1:56.8 (orig. 0:00.1–1:09.6) | «Buongiorno e benvenuti alla lezione su Eugenio» | «ma vedrete. In ogni caso. Eugenio Montale, beh...» | sì |
| D1 | 2:01.8–4:57.1 (orig. 1:11.9–4:07.3) | «Eugenio Montale, beh... Direi che è appunto una sua» | «e muore nel 1981, attraverso veramente. in novecento.» | sì |
| D2 | 7:19.1–11:16.6 (orig. 4:07.3–8:06.9) | «Vediamo la prima raccolta, la più importante,» | «ciò che non siamo, ciò che non vogliamo.» | sì |
| D3 | 13:54.7–25:48.8 (orig. 8:06.9–20:10.0) | «Bene, e allora come propone giustamente il» | «nostra condizione, se no addirittura ci potrebbe attaccare.» | sì |
| D4 | 29:22.9–31:51.8 (orig. 20:10.0–22:40.7) | «Seconda raccolta, le occasioni. Allora. Mm. Beh,» | «immobile e privo di un varco di salvezza.» | sì |
| D5 | 33:57.4–36:29.3 (orig. 22:40.7–25:12.7) | «Poi viene ve ne un'altra di raccolta,» | «i linguaggi alienanti. della moderna società di consumo.» | sì |
| D6 | 39:30.0–43:43.1 (orig. 25:12.7–29:25.7) | «All'interno di quest'opera la sezione Xenia, oksenia,» | «diciamolo, in sede scolastica. Di solito. sono richieste.» | sì |


## 5. Quiz, verifica e compiti: secondi vecchio → nuovo (misurato)
| Elemento | Vecchio | Nuovo |
|---|---|---|
| Quiz 1 | 7:53 (473.1 s) | 7:08 (428.8 s) |
| Quiz 2 | 15:12 (912.6 s) | 13:44 (824.4 s) |
| Quiz 3 | 28:17 (1697.5 s) | 29:12 (1752.6 s) |
| Quiz 4 | 34:20 (2060.2 s) | 33:47 (2027.1 s) |
| Quiz 5 | 42:24 (2544.8 s) | 39:19 (2359.7 s) |
| Quiz 6 | 50:17 (3017.8 s) | 45:47 (2747.9 s) |
| Verifica finale | 53:14 (3194.9 s) | 50:08 (3008.0 s) |
| Compiti | 53:33 (3213.2 s) | 50:24 (3024.8 s) |

Aggiornati `scheda_pubblicazione_Parte1.json`, `timeline_Parte1.json`, `testo_youtube.txt`. **La pagina del video va riallineata ai secondi nuovi.**

## 6. Cosa NON ho verificato
- **Controllo severo: non completato** (vedi §2). **Ascolto umano** di tutto il video (voci, timbro, jingle, trans): non fatto.
- **Voce della mappa (RMAP3):** la trascrizione automatica non vede «Le occasioni» e «Satura», ma c'è una pausa di ~2 s dove vanno: sembrano dette; **da riascoltare** (schermata 3 di 3, intorno a 46:10–47:40). RMAP e RMAP2 avevano parole mancanti e non le ho usate.
- **Altre voci Kore** (ripassi, approfondimenti, glossario, riepilogo, benvenuto): sono quelle del 17/11, trascritte dall'agente (nessuna parola tagliata, anni giusti) ma non riascoltate; «Vieusseux» (S1, AP1a) da riascoltare.
- **Sottotitoli:** non riletti cue per cue; poesie dal libro con tempi proporzionali (stima ±1–2 s).
- **Mappa:** frecce ridisegnate come catene dentro ogni colonna (le linee a ventaglio del prof si sarebbero incrociate); stessi nodi e stesse parole; marchio e foto del sito tolti.
- **Pixel-identico PDF/video:** confrontato a vista su 11 pagine.
- **Il «già visto»:** la terza card della slide «Satura» non compare: il prof ne parla solo a fine lezione, mostrata sulla slide dell'argomento 6.
- **Webcam** 243×139 px ingrandita 2,2×: immagine morbida, capelli al bordo alto nell'originale.

## 7. DA CONFERMARE COL PROF (anomalie nel suo materiale, non corrette)
- Slide «Le occasioni (1939)»: «nel clima storico del **dopoguerra** e degli anni trenta» (la raccolta è del 1939). Lasciata com'è; il quiz 4 usa «anni Trenta».
- Mappa del prof: «I^ Guerra mondiale» (la voce dice «prima guerra mondiale»).
- Slide «Meriggiare…»: il prof dice «tre quartine e una strofa di cinque versi»; il libro (p. 762–763) conferma.
- A 1:14 (orig.) il prof dice «Questa è appunto una sua fotografia»: nella sua slide c'è un ritratto di Montale che non ho messo (regola: foto di persone reali solo dal materiale del prof, alla massima risoluzione, migliorate se sgranate: **da decidere**; l'immagine è nel suo PDF, p. 1).
- Refusi corretti nelle nostre slide: nessuno di rilievo (accenti e maiuscole già giusti); «scorni», «milione» sono nel libro.

## 8. Come ho verificato
Trascrizione di originale e video (Parakeet), controllo severo della master (tesseract, loudness, voce), `controllo_jingle.py`, correlazione audio/originale per la sincronia, `freezedetect` sul riquadro, fotogrammi ogni 30 s (`controllo_minuti.jpg`) e fettine (`controllo_fettine.jpg`).
