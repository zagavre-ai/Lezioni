# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 9 (Giovanni Pascoli) · VERSIONE 2 (consegna)
Chat di revisione 9 · Parte 1 e Parte 2 rifatte nel modello grafico Spagnolo. Etichette: **[misurato]** · **[stima]** · **[non verificato]**.
Stato: consegnata con i limiti elencati al §5 e §7. **La lezione NON è ancora «perfetta»: i punti §5 devono essere visti da Sara/master prima del caricamento su Vimeo.**

## 1. Misure sul video nuovo [misurato]
| | Parte 1 | Parte 2 |
|---|---|---|
| Durata / fotogrammi | 53:50,6 · 96 918 (= durata × 30) | 53:36,2 · 96 485 (= durata × 30) |
| Formato | 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192k (unica codifica dei pezzi) | idem |
| Peso | 220,8 MB (3 pezzi da 90 MB + sha256) | 262,4 MB (3 pezzi + sha256) |
| Volume (EBU R128, tutto il file) | −16,5 LUFS | −16,2 LUFS |
| Picco campione | −2,5 dBFS (≤ −1 dBTP: il picco vero è maggiore di pochi decimi, non misurato con true-peak) | −2,5 dBFS |
| Jingle Quiz (controllo_jingle.py, scarto ±0,05 s) | Q1–Q4 OK (+0,005/+0,005/+0,004/+0,005 s) | Q1–Q4 OK (+0,005…+0,006 s) |
| Fermi ≥ 1 s del riquadro del prof dentro i pezzi del prof (freezedetect sul riquadro) | nessuno | nessuno (i 4 «fermi» rilevati iniziano alla fine del pezzo, dove il riquadro non c'è più) |
Durata: 50–60 min ✓. **La durata è cambiata** rispetto al vecchio (decisione Sara 17/11 00:40): le 10 mappe del prof sono lette da voci nuove più brevi; in P1 sono tolte anche le schede Compiti (solo in P2).

### Tabella secondo vecchio → nuovo (quiz, verifica, compiti)
| Punto | Parte 1 | Parte 2 |
|---|---|---|
| Quiz 1 | 1114,4 → 1090,4 | 949,9 → 931,6 |
| Quiz 2 | 1467,5 → 1427,5 | 1836,1 → 1800,5 |
| Quiz 3 | 2706,8 → 2648,6 | 2775,8 → 2720,1 |
| Quiz 4 | 3179,4 → 3109,7 | 3165,9 → 3092,6 |
| Verifica finale | 3299,8 → 3220,5 | 3291,0 → 3197,5 |
| Compiti | tolti (solo Parte 2) | 3304,6 → 3211,1 |
| Durata | 3318,5 → 3230,6 | 3309,7 → 3216,2 |
`scheda_pubblicazione_P1/P2.json` e `timeline_P1/P2.json` sono già aggiornati (titolo «Letteratura V · Lezione 9 · Giovanni Pascoli · Parte N»). `quiz_argomenti_P*.json` non contiene secondi.

## 2. Confronto col modello Spagnolo (punto 000)
| # | Punto | Esito |
|---|---|---|
| 1 | Sigla 15 s → dissolvenza → copertina | **corretto**: sigla del kit, dissolvenza di 1 s sulla copertina (nessun lampo) |
| 2 | Copertina | **corretto**: logo, riga blu, titolo Bricolage, card ARGOMENTI (P2 su 2 colonne) |
| 3 | Slide bianche, «01 · ARGOMENTO», titolo + barretta | **corretto** (numero = argomento, mai la lezione) |
| 4 | Piè di pagina «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» + «Pagina N» | **corretto**, Figtree Bold (non DM Mono) |
| 5 | Riquadro 4:3 ≈ 412×310, ombra grigia, niente bordo | **corretto**. Ritaglio webcam 184×138 ingrandito 2,2× → **immagine morbida (limite noto)**; testa che tocca il bordo alto già nell'originale (es. P1 0:48, 3:23: **non risolvibile**) |
| 6 | Fascia gialla 2 righe −3° | **corretto**, sempre visibile dove c'è il prof |
| 7 | Slide senza prof | **corretto** (presentazione, approfondimenti, ripassi, glossario, mappe, riepilogo) |
| 8 | Font | **corretto**: Bricolage / Figtree; nessun DM Mono |
| 9 | Finale | **corretto**: `Sigla_finale_5s_con_avviso_diritti.mp4` |
| 10 | Struttura | **mantenuta** (sigla, presentazione, argomenti, approfondimenti, ripasso, quiz, glossario, riepilogo, verifica, finale; compiti solo P2) |
| 11 | PDF A4 | **fatti** (§6) |
Ombre sempre grigie e morbide, card «in corso» con bordo giallo e fondo giallo chiarissimo, le altre bordo grigio (aggiornamento 01:30) [visto sui fotogrammi].

## 3. Problemi trovati nel vecchio e correzioni
| Dove (vecchio) | Tipo | Com'era | Correzione |
|---|---|---|---|
| tutto | visivo | grafica non Spagnolo (fascia blu, DM Mono) | rifatte tutte le slide |
| P1 4:10 | visivo | «Ecco, questa è una sua fotografia»: foto non sullo schermo | foto dalla slide 2 del prof a tempo (3:23 orig.) |
| P1 22:06 | visivo | «Pascoli, ecco Pascoli e le due sorelle»: foto non sullo schermo | foto dalla slide 5 del prof a tempo |
| 10 mappe | contenuto | mappe nostre/inventate, per decine di secondi solo il nodo centrale; narrazione di un'altra mappa | **mappa del prof** (`LEZIONE 9.pdf`) nella nostra grafica, **senza il marchio di terzi**, svelata nodo per nodo; 10 voci nuove R5–R14 |
| pagine del libro | visivo | bassa risoluzione, QR, «AUDIOLETTURA», note tagliate | fettine dagli screen HD (§4) |
| slide del prof | testo | testo riscritto | testo identico al `.pptx` |
| voce Kore | audio | «Mirìce» (accento errato) in presentazione P1/P2, ripasso Myricae, riepilogo P1 | R1–R4 («Mìrike»), inserite |
| P2 3:xx | titolo | «Quattro segni…» con 5 carte | «Segni da cercare in una poesia di Pascoli» |
| sottopancia/compiti | struttura | scheda Compiti anche in P1 | tolta da P1 |
| sincronia | visivo | evidenziazioni non legate alle parole | evidenziazioni dal parlato (tempi parola per parola), slide scelta per argomento detto (es. «simboli» mostrata quando il prof ne parla) |
| Quiz/titoli | audio | — | jingle del Quiz presenti a +0,5 s (OK) |

## 4. Pagine del libro in HD (tabella brano · pagina · file · minuto) [misurato su fotogrammi]
Fettine ritagliate dagli screen `Lez09_pNNN.png` **su righe bianche**, solo colonna del brano, senza QR/etichette/note/intestazioni; strofe intere. Foglio con un fotogramma per fettina: `controllo_fettine.jpg` (21 fotogrammi, tutte le righe intere, nessun frammento estraneo visto).
| Brano | Pagina | Fettine | Minuto (nuovo) |
|---|---|---|---|
| T2 · Una poetica decadente (primo paragrafo) | p286 | 1 (righe 1–8) | P1 ≈ 22:11–23:51 |
| T6 · X Agosto | p304 | 6 strofe | P2 ≈ 2:10–3:30 |
| T7 · L'assiuolo | p306–p307 | 3 strofe (la 2ª unisce due fettine su pagine diverse) | P2 ≈ 16:30–18:00 |
| T8 · Temporale | p310 | 1 | P2 ≈ 23:26 |
| T9 · Novembre | p312 | 3 | P2 ≈ 31:00–31:40 |
| T10 · Il lampo | p314 | 1 | P2 ≈ 34:13 |
| T13 · Il gelsomino notturno | p324 | 6 | P2 ≈ 37:00–38:10 |
Note: il prof legge anche un brano del *Fanciullino* («Il quale tintinnio segreto…», P1 ≈ 23:50–25:00 orig.) che **non è nelle pagine HD fornite**: resta la fettina del primo paragrafo. Il dipinto di Giorgione (p314) non è mai nominato dal prof: non inserito.

## 5. Cosa NON ho verificato / limiti aperti
- **Sottotitoli `.vtt`: NON riletti tutti.** Sono la trascrizione automatica (parola per parola) con un dizionario di correzioni (Pascoli, D'Annunzio, Myricae, Carducci, fanciullino, assiuolo, gelsomino…); per le voci narranti e le mappe il testo è quello degli script. **Restano errori nel parlato del prof** (es. «Carlata», «Teria»). Da fare: rilettura completa.
- **Voci Kore/R1–R14: non ascoltate** (solo durate e adattamento: R2 accelerata ≈ 3 %). ESITI del servizio: R8 «DA CONTROLLARE».
- **Mappe: le voci descrivono la mappa del prof, ma i tempi di comparsa dei nodi sono stimati** dalla posizione del testo (±2 s), non da una trascrizione delle voci nuove.
- **Sincronia labbra/voce non misurata sul fotogramma**: l'audio pulito e il riquadro sono presi dallo stesso istante dell'originale (stesso offset, ±1 fotogramma = 0,033 s [stima]).
- **Transizioni:** ogni pezzo entra con una dissolvenza da bianco di 0,4 s; **non c'è** il suono `trans.wav` né una dissolvenza incrociata tra pezzi, e i jingle `titolo.wav`/`repaso.wav` non sono stati aggiunti (restano quelli già presenti nell'audio vecchio). Da rivedere con la master.
- **Inizio pezzo P1 D4 (44:17,6)**: il pezzo comincia a metà frase («…delle cose attraverso il suono delle parole»): non corretto (taglio ereditato dal vecchio montaggio).
- **PDF slide**: generati dalle stesse slide del video (stesso HTML) e senza riquadro/fascia; il confronto pagina per pagina con i fotogrammi è **visivo a campione** (12 pagine P1), non automatico. Mappe: P1 5 pagine, P2 5 pagine.
- **Picco true-peak** non misurato (solo picco campione −2,5 dBFS).
- Mappa P2 per gli argomenti sulle poesie: la mappa del prof non ha rami sulle poesie → usati i rami «poetica» e «opere» (Myricae/Canti) con evidenziazione dei nodi pertinenti. **Decide Sara.**
- Quiz di argomento: riusati quelli del vecchio (40 domande dal materiale del prof, riviste a lettura: nessuna risposta errata trovata).

## 6. File consegnati
`Letteratura_Lez9_Parte{1,2}_1080p.mp4.parte_NN` + `.sha256` · `Letteratura_Lez9_Parte{1,2}.vtt` · `Letteratura_Lez9_Parte{1,2}_slide.pdf` (P1 42 pagine, P2 44) · `Letteratura_Lez9_Parte{1,2}_mappe.pdf` · `quiz_argomenti_P{1,2}.json` + `Quiz_Letteratura_Lez9.txt` · `verifica_finale_Lez9.json` + `Test_Letteratura_Lez9.xlsx` (10 domande, identiche all'Excel del prof) · `compiti.json` (testo identico al PDF del prof) · `scheda_pubblicazione_P{1,2}.json` · `timeline_P{1,2}.json` · `tabella_vecchio_nuovo.json` · `controllo_minuti_P{1,2}.jpg` (1 fotogramma ogni 30 s) · `controllo_fettine.jpg` · voci nuove su `voci-letteratura-V-lez09` (R1–R14).

## 7. DA CONFERMARE COL PROF (non deciso da me)
1. Anno della cattedra a Bologna: **1905** (slide, Excel, voce) ≠ **1906** (mappa del prof, mostrata com'è).
2. Mappa: «occhi **stupidi** del bambino» (probabile «stupiti»): mostrato com'è.
3. Excel domanda 4: una risposta sbagliata è «**Italy**» (non è un saggio, ma è una poesia: distrattore debole) · domanda 10: la risposta giusta è scritta «L'aria è del gemma, il sole così chiaro» (il verso è «**Gemmea** l'aria, il sole così chiaro»): testo lasciato come nel file.
4. Il prof legge un passo del *Fanciullino* non presente nelle pagine HD (§4).

## 8. Fine dei pezzi del prof (controllo 01:25) [misurato sulla trascrizione]
| Pezzo | Fine (min) | Ultime parole | Frase finita | Inizio (min) e prime parole |
|---|---|---|---|---|
| P1 D1 | 12:23.2 | «…letteratura che noi dovremmo andare ad analizzare, studiare.» | sì | 0:47.7 «Buongiorno e benvenuti alla lezione…» |
| P1 D2 | 21:45.8 | «…Pascoli e le due sorelle di cui parlavo.» | sì | 18:19.4 «Allora la sua esistenza…» |
| P1 D3 | 37:37.6 | «…e scrivere Brum, d'accordo l'onomatopea è esattamente questa.» | sì | 23:56.5 «Andando avanti, entrando sempre di più nella…» |
| P1 D4 | 48:05.0 | «…pezzettato diciamo.» | sì | 44:17.6 «delle cose attraverso il suono delle parole.…» |
| P2 D1 | 11:40.4 | «…agosto è una poesia fondamentale per comprendere Pascole.» | sì | 1:01.6 «Ovviamente analizziamola prima di queste composizioni, la…» |
| P2 D2 | 27:11.6 | «…accedere, cercare di capire, insomma erano più criptici.» | sì | 15:40.6 «Proseguendo sempre da Mirice abbiamo la suolo,…» |
| P2 D3 | 41:41.2 | «…Gesù Notturno è quasi un grido di dolore.» | sì | 30:09.5 «Pascoli è più chiaro, ma ogni cosa…» |
| P2 D4 | 48:33.3 | «…poi affrontare altri autori della letteratura italiana.» | sì | 45:29.1 «Per concludere parliamo dei poemetti e le…» |
Tutti e 8 i pezzi finiscono a fine frase. **Un inizio non è pulito: P1 D4 (vedi §5).**
