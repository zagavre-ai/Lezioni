# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 24 · Leonardo Sciascia
Correzioni del 22/11/2026 (regole: `REGOLE_BLINDATE.md` e aggiornamenti della master fino alle 17:00 UTC). Video: `Letteratura_Lez24_Parte1_1080p.mp4` (a pezzi `.parte_00`, `.parte_01`; sha256 nel file `.sha256`).
Etichette: **misurato** = misurato con uno strumento; **stima** = dedotto; **non verificato** = non ho potuto.

## 1. Misure sul video nuovo (misurato)
| Controllo | Risultato |
|---|---|
| Formato | 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192k 48 kHz |
| Durata / fotogrammi | 54:30,7 (3270,67 s) · 98 120 fotogrammi = durata × 30 |
| Peso | 176,7 MB |
| Volume | −16,6 LUFS integrato (LRA 5,9) |
| Picco | −2,4 dBTP |
| Sincronia labbra/voce | scarto massimo 17 ms su tutti i pezzi del prof (correlazione dell'audio del video con l'originale, 2 punti per pezzo) |
| Fermi immagine del prof | 0 fermi ≥ 1 s in D0, D1a–D1d, D2, D3 (`freezedetect`) |
| Jingle Quiz | scatto a inizio scheda + 0,5 s, scarto −0,016 s su Q1, Q2, Q3, Verifica finale, Compiti; jingle titolo su T1–T3 (corr. 0,96) |
| Pause > 2,5 s | nessuna a −45 dB (`silencedetect`) |
| PDF | slide: 69 pagine A4 orizzontale con strato di testo; mappe: 4 pagine (copertina «MAPPE» + 3 schermate) |
| Controllo severo (`controllo_severo.py`) | **non completato** (vedi §6) |

## 2. Cosa è cambiato rispetto alla consegna del 17/11
- **Testo a 40 px** (interlinea 1,5) nelle slide del prof; con 40 px non entrano 3 card, quindi ogni slide ne mostra **2** (finestre «card 1+2» e «card 2+3»), mai rimpicciolito. Approfondimenti: schede da 38/32 px, al massimo 3 per pagina (la 4ª card apre una nuova pagina). Schemi di ripasso e glossario a 36 px.
- **Nessuna schermata identica oltre 3 minuti.** La slide «L'impegno politico e civile» durava 6,8 minuti: il pezzo D1 è ora diviso in D1a–D1d (tagli sulle pause tra due frasi) e **tra i pezzi del prof entrano gli approfondimenti** che commentano quello che il prof ha appena detto (AN1–AN2, AN3, AN4). Nessuna card sola oltre 60 s (tutte le finestre hanno ≥ 2 card).
- **Bordo giallo all'inizio della frase** del prof (stima ±1–2 s da trascrizione): il bordo non c'è più quando il prof parla ancora della slide prima.
- **Mappa: una sola, quella del prof**, nel modello BES (colori pesca / celeste / paglierino / menta / lilla con legenda in alto a destra), tolti il logo mappe-scuola.com e le due foto. Le tre mappe «nostre» (AN8, AN16, AN26) e la mappa finale inventata (ANF) sono state **tolte**. La mappa del prof ha 23 riquadri e a 34 px non entra in una schermata: seguendo l'indicazione della master è **divisa in 3 schermate** («Mappa del professore · 1 di 3 … 3 di 3», una volta sola, prima del glossario): vita (37 px), pensiero + stile (46 px), opere (43 px). Ogni schermata si costruisce riquadro per riquadro con la voce Kore (MP1, MP2, MP3a/b + MP4 + MP5b) e il riquadro in corso è giallo; alla fine resta ferma 4 s. Non esiste la mappa intera rimpicciolita sotto 34 px.
- **Nome del prof**: tolto dalla voce dell'introduzione (nuova voce INTRO1c) e dai piè di pagina (ora «LETTERATURA ITALIANA V» e «Pagina N»). Resta solo nella fascia gialla.
- **Voci nuove** (generate dalla master): INTRO1c, S3c, RF1c, MP1, MP2, MP3a, MP3b, MP4, MP5b. Numeri e anni in lettere; «L'affaire Moro» scritto «L'affèr Moro» nel testo per la voce, «L'affaire Moro» sullo schermo.
- **Sigle:** «PCI» nelle schede di ripasso è scritto «Partito comunista italiano (PCI)»; la voce nuova dice «Partito comunista italiano».
- **Transizioni:** dissolvenza di 0,9 s + `trans.wav` a ogni cambio di pezzo. Pause sotto le schede della mappa riempite con `repaso.wav` (la scheda resta ferma 4 s come da regola) e nel ripasso 2; scheda Compiti 4,6 s e Verifica finale 4 s per non avere pause > 2,5 s.
- **Rigenerati sul video finale:** `.vtt` (842 cue), `timeline.json`, `scheda_pubblicazione.json` (titolo «Letteratura V · Lezione 24 · Leonardo Sciascia»; `inizio_s`, `quiz_s`, `t_verifica`, `t_compiti`), `testo_youtube.txt`, dispensa slide e PDF mappe con testo invisibile selezionabile.

## 3. Tabella dei pezzi del prof (misurato sulla trascrizione)
| Pezzo | Minuto | Inizio (prime parole) | Fine (ultime parole) | Frase intera |
|---|---|---|---|---|
| D0 | 0:51–1:33 | «Buongiorno e benvenuti alla lezione su Leonardo Sciascia» | «In effetti c'è quest'altra tematica.» | sì |
| D1a | 1:39–4:07 | «Leonardo Sciascia. Allora. Comprendiamo…» | «…lo specchio della realtà, d'accordo?» | sì |
| D1b | 7:04–9:34 | «Allora. Nelle sue prime opere narrative…» | «…lotta contro lo Stato, d'accordo?» | sì |
| D1c | 10:39–12:19 | «Ecco, poi le cose andarono diciamo così.» | «…Gesto d'accusa. Certamente.» | sì |
| D1d | 13:38–16:13 | «L'impegno di Sciascia andò ben oltre la pagina scritta.» | «…poi passiamo alla successiva.» | sì |
| D2 | 20:36–24:01 | «Passiamo alla successiva, dopo tutto, perché sto per introdurre l'opera.» | «…e i sistematici depistaggi istituzionali.» | sì |
| D3 | 34:18–39:12 | «Questo quadro radicalmente negativo e impietoso trova il suo culmine nel romanzo Todo Modo…» | «…ma che certamente dà fastidio.» | sì |
I tagli cadono nelle pause tra due frasi; ogni pezzo inizia 0,15 s prima della frase (le frasi di inizio/fine sono lette dalla trascrizione automatica; **non verificate all'ascolto**).

## 4. Pagine del libro
Lezione 24: nessuna pagina del libro.

## 5. Cosa NON ho verificato / limiti
- **Ascolto umano:** non ho ascoltato né guardato il video per intero. Pronuncia delle voci nuove (in particolare «L'affèr Moro» in S3c, RF1c, MP4 e i nomi stranieri) **non verificata all'ascolto**: ho letto solo la trascrizione automatica delle voci.
- **Dimensione del testo della mappa:** 37, 46 e 43 px nelle tre schermate; il minimo richiesto (34 px) è rispettato.
- **Slide del prof a 2 card:** con 40 px tre card (220–280 px l'una) non entrano nell'area utile (circa 600 px): scelta di dividere la slide.
- **Evidenziazioni:** tempi da trascrizione automatica; incertezza stimata ±1–2 s. Da riguardare in almeno 4 punti.
- **Sincronizzazione delle schede degli approfondimenti** sulle parole chiave della voce: stima ±2 s.
- **Sottotitoli:** nomi e parole sospette corretti; non riletti riga per riga contro l'audio. Dubbi sul parlato del prof (lasciati con la lettura più probabile): «Ve ritiero?» → «Vero?» (~8:12 nel video precedente), «pe i supistieri» → «per i misteri», «scomparsi inserisamente».
- **Testa nel riquadro:** webcam originale 184×138 px ingrandita 2,2×: immagine morbida; i capelli toccano il bordo alto già nell'originale: non risolvibile.
- **Quiz:** riletti contro le slide del prof: coerenti. Invariati. Verifica finale = Excel del prof (10 domande), compiti = PDF del prof (4 domande), testo identico.
- **Voce narrante dell'introduzione dell'8 ottobre:** nessuna; l'introduzione animata non ha il riquadro del prof.
- **Controllo indipendente (agente separato):** esito nel §6 (non ha potuto ascoltare né guardare tutti i pezzi: approfondimenti AN2–AN25, S2, S3, Q2, Q3, R, FIN non guardati).

## 6. Esito dei controlli severi
- **`controllo_severo.py`: NON concluso.** L'ho lanciato con tesseract sul video (passo 20 s): con la macchina carica dalle codifiche è rimasto in esecuzione oltre 30 minuti senza dare l'esito e l'ho fermato per non perdere la scadenza. **Esito OK non dimostrato.** Le stesse misure del controllo le ho fatte a mano sul video finale: durata 54:30,7; −16,6 LUFS; nessuna pausa > 2,5 s (`silencedetect` a −45 dB); copertina da 0:17 a 1:33 (circa 76 s, ≤ 180 s) con titolo «Leonardo Sciascia»; nessuna schermata con la stessa pagina oltre 3 minuti (la corsa più lunga con la stessa pagina è D1b, 150 s; stima dai tempi delle finestre, non da OCR); nessun «…» nelle card; card con iniziale maiuscola.
- **Verifica indipendente (agente separato che non ha montato):** trovati e **corretti**: (a) suono di transizione fuori posto (cadeva prima della dissolvenza, ora nella dissolvenza); (b) sigla «PCI» non rispiegata nella slide di D3 («Il distacco dal PCI (Partito comunista italiano)»); (c) mappa: etichette dei rami tutte in maiuscolo, frecce più grandi, «saggi» non più collegato a «Il mare colore del vino»; (d) sottotitoli: tolti i cue di soli riempitivi («Uh», «Um», «Mm»), corretti «il Candide di Voltaire», «le ipocrisie sociali», «Il consiglio d'Egitto e Il contesto»; (e) scheda Verifica finale accorciata a 4 s (restava una pausa di 2,8 s).
- **Difetti segnalati e NON corretti** (da decidere con la master):
  - **Mappa del prof non identica nella struttura:** le foglie «sulla mafia», «ambientato nel '700», «sulla corruzione politica», «romanzo giallo» sono fuse nel riquadro del romanzo con «·» (l'originale ha riquadri separati); «sulla corruzione politica» compare sia su «Il contesto» sia su «Todo modo» (nell'originale è uno solo collegato a entrambi); nella schermata 1 la vita è una catena di frecce (nell'originale è a raggiera). Le parole sono quelle del prof.
  - **Card accesa a lungo:** in D1b la card 1 resta accesa 124 s, in D1c circa 100 s, in D1d la card 2 circa 155 s (le slide hanno sempre 2 card; la regola «card sola» riguarda una sola card per schermata). Nessuna schermata resta identica oltre 3 minuti.
  - **Bordo giallo:** in D1b la card 1 si accende ~1,6 s prima della frase (fuori da ±1 s); in D3 l'agente segnala un possibile ritardo di ~7 s ma la misura assume gli stessi tagli del video vecchio e **non è dimostrata**: da guardare.
  - **Mappa MAP2:** resta ferma a mappa intera circa 2,5–4 s (richiesto 4 s): non misurato con precisione.
  - **Dispensa:** la copertina mostra anche l'elenco ARGOMENTI e «Pagina 1» (identica alla copertina del video).
  - **Schede Verifica finale e Compiti:** nel video si vedono solo i titoli («10 domande», «Quattro domande aperte»); le domande sono nei file `verifica_finale.json` e `compiti.json` (interattive nel lettore: non verificato).

## 7. DA CONFERMARE COL PROF (dati che non coincidono; nella mappa ho lasciato le date del prof)
- **Morte dell'Inquisitore**: mappa 1964; voce degli approfondimenti 1963.
- **L'affaire Moro**: mappa 1978; slide, voce ed Excel (domanda 5) 1979.
- **Porte aperte (1987)**: in slide, voce ed Excel, non nella mappa. «A ciascuno il suo (1966)»: nella mappa, non nelle slide.
Refusi del materiale del prof corretti nelle nostre slide: nessuno trovato nelle 7 slide del prof.

## 8. Come ho verificato
Trascrizione completa (Parakeet TDT, `trascrivi.py`), correlazione audio per i tagli, misure ffmpeg/ebur128/`freezedetect`/`silencedetect`, fotogrammi a 1/30 s (`controllo_minuti.jpg`), `controllo_severo.py` con tesseract, controllo di un agente separato che non ha montato la lezione.
