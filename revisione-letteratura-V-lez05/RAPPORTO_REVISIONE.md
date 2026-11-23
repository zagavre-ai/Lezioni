# RAPPORTO REVISIONE · Letteratura V · Lezione 5 · Giovanni Verga — correzioni 22/11/2026
Etichette: **M** misurato · **S** stima · **NV** non verificato. Video a pezzi `.parte_00…04` + `.sha256` (sha256 dei pezzi ricomposti verificato: M).


## 0. Aggiornamento 23/11 (ultima consegna)
- `controllo_rapido.py`: **ESITO OK**, nessun errore (59,33 min, −16,4 LUFS, −1,4 dBTP, 381 MB); foglio dei fotogrammi guardato e consegnato (`foglio_fotogrammi_Letteratura_Lez5.jpg`, `controllo_rapido_Letteratura_Lez5.json`).
- Corretto: piè di pagina **senza nome del docente** in tutte le slide, dispensa e mappa (il nome è solo nella fascia gialla); **schede blu a tutto schermo** (argomento, ripasso, quiz, fine, compiti); testo «Rispondi · premi Controlla · poi Continua» su quiz e verifica; **QR e bottoni dell'editore tolti** dalle fettine (prima per un errore di percorso non venivano tolti); **bordo giallo** ricalcolato sulle parole della trascrizione (prima occorrenza della parola-guida della card, non a stima: molti punti ora corretti, ma resta un abbinamento lessicale da verificare); pagine lunghe divise con «Parole chiave» nell'area sinistra.
- **NON fatto**: voce Kore dei **COMPITI** (testo `COMPITI` inviato sul ramo voci, la voce non è ancora arrivata: la scheda dei compiti resta senza voce, 5 s); glossario su due pagine; mappa a gruppi di riquadri.

## 1. Cosa ho cambiato
- **Testo a 40 px**, interlinea 60 px, in tutte le card (slide del prof, ripassi, riepilogo); glossario a 36 px. Misurato dal controllo indipendente: riga alta 37 px, interlinea 60 (M).
- **Slide del prof a finestre**: al massimo 2 card per slide del prof, 3 nei ripassi; ogni card è una frase intera con iniziale maiuscola, nessun «…» (controllo indipendente su 42 fotogrammi: OK).
- **Nessuna pagina identica oltre 3 minuti**: le pagine più lunghe sono divise in varianti con la colonna «Parole chiave» (max 5, estratte dal testo della slide del prof). Controllo con `controllo_severo.py`: vedi §3.
- **Mappa unica del prof**, ridisegnata nel modello BES (legenda in alto a destra, colori pesca/celeste/paglierino/menta/lilla, testo 34 px), costruita a gruppi di riquadri con 21 voci Kore (MQ01–MQ21, trascritte e controllate: bordi < 0,03, correlazione 0,98–1,00 con l'audio del video). Inserita **una volta sola prima del glossario** (54:25–56:47), ferma 4 s alla fine. **Ridisegnata senza il logo mappe-scuola.com e senza la foto dell'autore.** Le prime voci MP01–MP21 erano tagliate male (anni a fine voce precedente): scartate e rigenerate (MQ).
- **Introduzione**: copertina con titolo esatto, sopra 26 s di voce Kore e 15 s di prof (totale < 1 minuto); card ARGOMENTI che si accendono quando la voce li nomina. Nessun riquadro del prof nella presentazione.
- **Audio**: −16,4 LUFS, picco −1,4 dBTP, nessuna pausa > 2,5 s (riempite con i jingle del kit: `trans`, `titolo`, `repaso`) (M); timbro della voce: tono 156–172 Hz, chiarezza 1464–1615 Hz (M, limiti 95/800).
- **Fascia gialla col nome** su tutte le slide con il prof (nella versione precedente mancava nelle slide a card: corretto); nome del docente tolto dal piè di pagina di tutte le schede animate e dalla mappa.
- **Dispense A4**: `…_slide.pdf` (98 pagine) e `…_mappe.pdf` (copertina con «MAPPE» + mappa), con **strato di testo invisibile** (testo selezionabile, PDF vettoriali) e senza nome del docente.
- **File rigenerati** sul video finale (59:19,87; 106 796 fotogrammi): `.vtt` (1105 cue), `timeline.json`, `timeline_Parte1.json`, `scheda_pubblicazione.json` (titolo «Letteratura V · Lezione 5 · Giovanni Verga»), `testo_youtube.txt`, `quiz_argomenti.json`, `verifica_finale.json`, `compiti.json` (con i secondi). Quiz 1–5 agli stessi secondi di prima salvo quiz 4 (+1,03 s, vedi §4); la mappa entra dopo il quiz 5, quindi **glossario, riepilogo, verifica e compiti slittano di +142,13 s** (verifica a 59:01, compiti a 59:15).

## 2. Controllo indipendente (agente separato, §11)
Esiti OK: card intere e ≤ 3, testo grande, riquadro del prof solo quando parla, copertina, voci MQ intere e a tempo con la mappa (21/21). Difetti trovati e **corretti**: fascia gialla assente nelle slide a card; piè di pagina con il nome del docente nelle schede animate; pagine identiche > 3 min. Difetti **NON corretti** (§5).

## 3. Controllo severo della master
`controllo_severo.py` (tesseract installato) sull'ultimo video: **al momento della consegna non è terminato** (la scansione OCR è lenta); un primo giro sulla versione precedente non ha dato esito. **Esito: NON DISPONIBILE** — da rilanciare dalla master: `python3 controllo_severo.py Letteratura_Lez5_Parte1_1080p.mp4 "Giovanni Verga"`. Misure fatte a parte: durata 59,3 min, volume −16,4 LUFS, nessuna pausa > 2,5 s, voce non alterata (M).

## 4. Pezzi del prof (inizio e fine, tempi dell'originale; frase finita sì/no)
| Pezzo | Inizio (originale) | Fine (originale) | Ultime parole | Frase finita |
|---|---|---|---|---|
| 1 | 0:00 «Buongiorno e benvenuti alla lezione su…» | 8:58 | «…fino alla morte avvenuta nel gennaio del millenovecentoventidue.» | sì |
| 2 | 8:58 «Ma Verga non è solo e…» | 26:09 | «…e io farò il ciclo dei Vinti, capite?» | sì |
| 3 | 26:09 «Ecco qua. Allora, bene, ciclo dei Vinti…» | 29:57 | «…riusciranno mai a riscattare la loro condizione, d'accordo?» | sì |
| 4 | 29:57 «Proviamo a delineare…» | 39:47,6 | «…Ed è il primo del ciclo dei Vinti, il primo romanzo.» | sì (corretto: prima finiva a metà frase; taglio spostato di 1,03 s) |
| 5 | 39:47,6 «A seguire vi sarebbe…» | 48:56 | «…capita e soprattutto sia passata.» | sì (fine dell'originale) |
Scarto audio/video: video preso dall'originale con scarto in fotogrammi interi uguale a quello dell'audio (correlazione: −0,0066/−0,0100/−0,0099/+0,0068/−0,0099 s; limite 0,04) (M). Fermi immagine del prof: nessuno (M, `freezedetect` 0,6 s, nella versione precedente identica; non rifatto sul video nuovo: NV).

## 5. COSA NON HO CORRETTO / NON HO VERIFICATO
- **Bordo giallo delle card non affidabile**: l'abbinamento card↔parlato è lessicale (S); il controllo indipendente su 15 punti ne ha trovati solo 4 entro tolleranza. Le card in corso possono essere accese in anticipo o in ritardo (anche decine di secondi). **Serve una rifinitura a mano con la trascrizione** (`controllo/trascrizione_originale_prof.srt`) — non fatta.
- **Pagine del libro**: restano in alcune fettine il QR «AUDIOLETTURA» (visto a 40:37, 42:37, 44:18, 52:40) e i bottoni dell'editore («ANALISI INTERATTIVA», «ENTRA NEL TESTO», «TESTO CHIAVE»); alcune fettine sono ritagliate nel testo in alto/in basso (fettine del prof, non rifatte dagli screen HD). Testo delle strisce a due colonne piccolo.
- **Mappa**: 4 passi accendono più riquadri insieme (label + primo elemento); frecce poco visibili; riquadri abbreviati rispetto alla voce in alcuni passi (le voci dicono «Nel milleottocentoquaranta…», i riquadri «1840 · …»). Struttura a 4 colonne per gruppi, non identica alla disposizione del prof (stesse parole; correzioni: virgola tolta in «la sconfitta di chi aspira», «Cavalleria rusticana» minuscolo).
- **Glossario**: tabella su due pagine (4+4 righe), contro la regola «mai spezzata».
- **Approfondimenti animati** per argomento (§3.3 delle regole): non presenti.
- Quiz, verifica, compiti: schede da 5 s come prima (le domande sono nella pagina interattiva).
- Sigla (0:15): etichetta «[ANALISI TESTUALE]» nella sigla del kit, da confermare con la master.
- Pulizia del rumore del prof non rifatta con `arnndn`; ascolto umano delle voci: NV (MQ11 trascritta «scride»).
- Sottotitoli `.vtt`: trascrizione automatica, non riletta da una persona.
- Anomalie del materiale: nessun contenuto modificato; refusi corretti nelle nostre slide/mappa come sopra. Mappa vs slide: «La Roba 1882» / «La Lupa 1880» / «Cavalleria rusticana 1880» vs slide T9 «dicembre 1880, raccolta nel 1883»: da confermare col prof.
