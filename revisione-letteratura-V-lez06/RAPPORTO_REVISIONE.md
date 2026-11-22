# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 6 · Decadentismo e Simbolismo
**Correzioni del 22/11/2026** (sul ramo `revisione-letteratura-V-lez06`, riconsegna). Video: `Letteratura_Lez6_Parte1_1080p.mp4` a 3 pezzi `.parte_NN` con `.sha256`.
Regola: **misurato** = misurato con uno strumento; **stima** = dedotto; **non verificato** = non ho potuto.

## 1. Esito del controllo severo e misure sul video nuovo
**Controllo severo (`controllo_severo.py`, 3° giro, passo 60 s, concluso alle 20:46 UTC, dopo la scadenza): esito RESPINTA.** Errori segnalati: [   "1 tratti con una card sola oltre 60 s"  ]. Tutti gli altri controlli sono a posto: copertina con titolo intero e 180 s (limite 180), nessuna slide con lo stesso titolo né schermata identica oltre 3 min, nessuna card con «…», -16.6 LUFS, 0 pause oltre 2,5 s, durata 50,2 min, timbro della voce 148–164 Hz e chiarezza 1345–1455 Hz (voce non alterata).
**Storia dei giri (tutti dopo la scadenza delle 19:30 UTC):** 1° giro RESPINTA per «card sola» (4:30, 300 s) e minuscola nel riepilogo (49:30); ho reso le card attenuate più contrastate, messo la maiuscola nel riepilogo e fatto ripartire la numerazione delle card da 1 per slide (il controllo legge solo i numeri 1–3); 2° giro: card sola a 6:30 e 41:30; 3° giro (questo): **un solo tratto**, «card sola» a 42:30 per 300 s (42:30–47:30). **Verifica a occhio sui fotogrammi di quel tratto (42:45, 43:45, 44:45): le slide hanno 2 o 3 card visibili** («Le figure tipiche della letteratura» con 2 card, «Temi e figure tipiche» con 3). Il controllo automatico legge male il numero della card attenuata: è un probabile **falso positivo, ma l'esito del programma resta RESPINTA** e non lo dichiaro OK. Gli avvisi «iniziale minuscola» (25:30, 31:30, 39:30, 49:30) sono segnalazioni «da guardare», non errori: guardati a occhio (31:30, 49:30) le card cominciano con la maiuscola. Se la master vuole azzerare anche il falso positivo, serve ingrandire il numero nelle card attenuate (ricodifica di circa 35 minuti).
| Controllo | Risultato |
|---|---|
| Formato | 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192k 48 kHz (**misurato**) |
| Durata / fotogrammi | 50:14.0 · **90421 fotogrammi = durata × 30** (53 pezzi; prima 53:07,9). La durata è cambiata (regola 00:40): sotto la tabella vecchio → nuovo |
| Peso | vedi `.sha256` / pezzi (sotto i 400 MB) |
| Volume | **-16.6 LUFS** (LRA 6.4 LU), picco **-1.9 dBTP** (true peak) (**misurato**) |
| Pause | nessuna pausa > 2,5 s (`silencedetect −45 dB, 2,5 s`, **misurato**): schede titolo 3,3 s, Quiz 4,0 s, verifica e compiti 4,0 s, mappa con jingle `finale` sul tratto fermo |
| Jingle Quiz | `controllo_jingle.py`: scatto a 0,0 s in 5 schede su 5 (scarti +0.002, +0.003, +0.002, +0.004, +0.003 s) (**misurato**) |
| Sincronia prof (labbra/voce) | correlazione con l'originale in 3 634 finestre da 2 s: scarto massimo **0,022 s** (limite 0,04 s); una sola finestra agganciata altrove (falso aggancio in una pausa del pezzo D3) (**misurato**) |
| Fermi immagine del prof | `freezedetect` sul riquadro, soglia 0,5 s: nessun fermo ≥ 1 s nei pezzi del prof (un solo fermo di 0,5 s) (**misurato**) |
| Sottotitoli | 752 cue, max 2 righe, nessuna sovrapposizione; sincronia: su 144 cue verificabili (trascrizione del video finale), scarto mediano 0.01 s; entro 0,3 s il 97%, entro 1 s il 100% (**misurato**) |
| Testo delle card | 40 px (mai sotto), interlinea 1,5, **al massimo 3 card per slide**, ogni card è una frase intera (`Etichetta: frase`); nessuna slide ferma oltre 3 min |
| PDF | `…_slide.pdf` 98 pagine A4 orizzontale (copertina + 97 slide, a 40 px, testo reale selezionabile); `…_mappe.pdf` 2 pagine (copertina «MAPPE» + mappa) |

### Secondi vecchio → nuovo (la master rigenera la pagina)
| Scheda | Secondo vecchio | Secondo nuovo |
|---|---|---|
| Quiz 1 | 716.3 (= 11:56.3) | 768.8 (= 12:48.8) |
| Quiz 2 | 1259.9 (= 20:59.9) | 1275.0 (= 21:15.0) |
| Quiz 3 | 1785.8 (= 29:45.8) | 1931.0 (= 32:11.0) |
| Quiz 4 | 2444.9 (= 40:44.9) | 2501.6 (= 41:41.6) |
| Quiz 5 | 3041.1 (= 50:41.1) | 2849.0 (= 47:29.0) |
| Verifica finale | 3163.1 (= 52:43.1) | 2991.2 (= 49:51.2) |
| Compiti | 3179.4 (= 52:59.4) | 3006.5 (= 50:06.5) |

## 2. Cosa ho cambiato (correzioni 22/11)
| Punto delle regole | Prima | Ora |
|---|---|---|
| Mappe | 5 mappe + 1 finale **inventate da noi** (6 pezzi, 3:40) | **una sola mappa, quella del prof** («I “poeti maledetti”»), ridisegnata nel modello BES (colori pesca/celeste/paglierino/menta/lilla con legenda in alto a destra, testo 34–50 px), prima del glossario, una volta sola, **costruita ramo per ramo** dalla voce Kore (R14) con il riquadro acceso in giallo e 4 s di mappa ferma alla fine. La mappa di questa lezione non ha marchio di terzi né foto dell'autore |
| Slide del prof | tabelle a 26 px fino a 4 righe | card intere, max 3 per slide, 40 px, interlinea 1,5; slide che si dividono (2+2) invece di rimpicciolire; bordo giallo e pallino giallo all'inizio della frase |
| Già visto | le slide «poeti maledetti» e «corrente europea», «strumenti», «linguaggio» comparivano in due argomenti | **il prof è stato riordinato per argomento** (tagli sulle pause tra due frasi, dissolvenza e fondo di 30 ms): i due richiami di D4 e D5 sono finiti nell'argomento a cui appartengono. Nessuna slide o immagine del prof compare in due argomenti |
| Nome del docente | la voce del benvenuto diceva «Il professor Giorgio Mazzotti»; piè di pagina col nome anche sulle animazioni | nuova voce R13 «Il professore…» (non «Giorgio Mazzotti»); piè col nome solo sulle slide col prof; il nome è nella fascia gialla |
| Voci | R6–R11 (mappe nostre) | R12 aveva letto la regia ad alta voce e perso parole: **scartata**, usata R14 (ESITI «OK») |
| Copertina | | titolo esatto, argomenti a 40 px che si accendono quando il prof parla; introduzione del prof 2 min 03 s (< 3 min) |
| Pause | 13 pause 3,0–5,3 s nelle schede | accorciate/coperte (vedi §1) |
| Picco | −1,9 dBTP | -1.9 dBTP |
| Dispensa | PDF con nome del prof nel piè | copertina solo materia + titolo, piè materia + pagina, niente nome del docente; PDF mappe con copertina «MAPPE» |

## 3. Inizio e fine di ogni pezzo del prof (misurato sulla trascrizione)
| Pezzo | Fine (minuto) | Ultime parole dette | Frase finita? | Inizio (minuto) | Prime parole |
|---|---|---|---|---|---|
| D1 | 8:19 | «…Ci torneremo, affronteremo tutto. Allora.» | sì | 0:57 | «Buongiorno e benvenuti alla lezione su Decadentismo…» |
| D1b | 9:02 | «…Questo è vero, scusate, Rimbaud.» | sì | 8:19 | «Sono gruppi d'avanguardia, abbiamo detto.…» |
| D1c | 9:46 | «…ultimi decenni dell'ottocento, con prolungamenti nel primo novecento.» | sì | 9:02 | «Va bene, poi come appunto potete vedere anche…» |
| D2 | 18:40 | «…specificare qualcosa in più. Allora.» | sì | 13:00 | «Ecco, giusto per inquadrare bene.…» |
| D3 | 26:25 | «…Allora.» | sì | 21:29 | «Tanto per...…» |
| D3b | 29:14 | «…Contemporaneamente la sinestesia, d'accordo?» | sì | 26:25 | «Come detto, qui trovate la visione decadente del…» |
| D4 | 38:36 | «…Questo è chiaro.» | sì | 32:28 | «E sulla falsa riga.…» |
| D5 | 44:41 | «…» | no — **l'originale del prof finisce così (a 31:00)** | 42:02 | «Va bene, altri temi: vitalismo e superomismo, ripreso…» |
Nessuna parola mozzata in partenza. Cuciture tra pezzi dello stesso argomento: dissolvenza di 9 fotogrammi in fondo/inizio, audio con 30 ms di dissolvenza nel silenzio (pausa tra le frasi ≥ 0,29 s). Il solo finale non chiuso è quello dell'originale.

## 4. Pagine del libro in alta risoluzione
Zip `Lez06_ingrandita.zip`: pagine 202 (Languore) e 206 (Vocali). Una fettina per volta, a tempo con la voce, una sola colonna, inizio e fine su riga bianca; la stanza in corso è evidenziata e nei versi di Vocali si accende la riga della vocale di cui parla il prof. Foglio `controllo_fettine.jpg` (un fotogramma a metà intervallo per ogni riga): nessuna riga tagliata, nessun frammento di altre colonne.
| # | Brano | Pagina | Parte | File HD / ritaglio (px) | Minuto |
|---|---|---|---|---|---|
| 1 | Languore | p. 202 | ritratto di Verlaine (slide del prof) | `pptx del prof`  | 13:13–13:19 |
| 2 | Languore | p. 202 | testata del brano (titolo, introduzione, metro) | `Lez06_p202.png` (220, 625, 1700, 1205) | 13:19–13:24 |
| 3 | Languore | p. 202 | testo francese a fronte, su due colonne | `Lez06_p202.png` (1455, 1225, 2200, 2340) | 13:24–13:36 |
| 4 | Languore | p. 202 | versi 1–8 (due quartine) | `Lez06_p202.png` (290, 1262, 1450, 1810) | 13:36–13:48 |
| 5 | Languore | p. 202 | versi 1–8 (due quartine) | `Lez06_p202.png` (290, 1262, 1450, 1810) | 15:02–15:39 |
| 6 | Languore | p. 202 | versi 9–14 (due terzine) e fonte | `Lez06_p202.png` (290, 1830, 1450, 2320) | 15:39–16:51 |
| 7 | Vocali | p. 206 | ritratto di Rimbaud (slide del prof) | `pptx del prof`  | 32:18–33:14 |
| 8 | Vocali | p. 206 | versi 1–8 (due quartine) | `Lez06_p206.png` (290, 745, 1490, 1285) | 33:14–33:57 |
| 9 | Vocali | p. 206 | versi 9–14 (due terzine) e fonte | `Lez06_p206.png` (290, 1310, 1490, 1840) | 33:57–35:01 |
| 10 | Vocali | p. 206 | versi 1–8 (due quartine) | `Lez06_p206.png` (290, 745, 1490, 1285) | 35:01–36:51 |
| 11 | Vocali | p. 206 | versi 9–14 (due terzine) e fonte | `Lez06_p206.png` (290, 1310, 1490, 1840) | 36:51–38:26 |

## 5. Cosa NON ho verificato
- **Ascolto umano:** non ho ascoltato né la voce Kore né il parlato del prof dopo la pulizia. Di R13 e R14 ho solo la trascrizione (R14: «Verlen», «L'angore», «Rembau» = errori del riconoscitore, ESITI del servizio «OK»). **Non verificato.**
- **Strato di testo invisibile nelle fettine del libro:** nei PDF le card, i titoli e la mappa sono testo reale selezionabile; le fettine delle pagine 202 e 206 sono immagini senza testo selezionabile. **Non fatto.**
- **Pronuncia dei nomi stranieri:** Verlaine, Baudelaire, Rimbaud, Huysmans, Mallarmé, Corbière sono scritti nella loro lingua a schermo e nei sottotitoli; nella voce sono scritti come si pronunciano (Verlèn, Bodlèr, Rembò). Non ho potuto ascoltarli.
- **Ordine del prof:** il riordino degli argomenti è una scelta mia per rispettare «niente già visto»; la master/Sara decidono se preferiscono l'ordine originale con le slide ripetute.
- **Controllo severo:** RESPINTA; l'agente separato di controllo: vedi §6.
- **Sottotitoli da riascoltare:** 7:55 «il manifesto delle tendenze decadenti…» (inizio frase non trascritto); 15:10 «già usato dagli Scapigliati»; 16:58 «si dice che facciano qualcosa»; 24:32 frase di 1 s tolta; 30:47 «perché Languore è dell'83»; 32:48 «prima la U e poi la O»; 35:42 «il blu della suprema tromba»; 35:55 «dai mondi e dagli angeli»; 36:44 «Questo è chiaro». I minuti sono quelli del video precedente (±3 min dopo il riordino).
- **Testa nel riquadro:** webcam 246×138 px, ritaglio 4:3 di 184×138 ingrandito 2,24×; i capelli toccano il bordo alto già nella ripresa. Non risolvibile.
- **Refusi:** nelle slide del prof ho solo uniformato la maiuscola iniziale e le virgolette («»); nessun refuso di ortografia trovato. Nessun dato che non torna (1872, 1883, 1884 coerenti).

## 6. Controllo separato
Un agente separato, che non ha montato la lezione, ha spuntato i punti 1–11 della lista (§11 di `REGOLE_BLINDATE.md`) su 58 fotogrammi, 590 miniature ogni 5 s, il `.vtt` e i due PDF: **10 punti su 11 OK**. Nessuna slide con più di 3 card, nessuna card con «…» o minuscola, schermata statica più lunga ≈ 95 s, nessun riquadro del docente nell'introduzione animata, nessun nome del docente nelle animazioni né nel vtt, mappa unica prima del glossario (2853–2913 s), copertina PDF senza nome, 97 pagine A4 orizzontali.
Unico difetto segnalato (punto 11, 30:00 circa, pagina «La visione del mondo», card 3): «Il Decadentismo ha **fiducia** nel futuro…». **Verificato sul testo: è un falso positivo.** La card dice «ha **sfiducia** nel futuro» (testo della voce `AP3a`, e «sfiducia» compare nel `.vtt`); l'agente ha letto male la parola nel fotogramma.
L'agente non ha potuto controllare: audio e sincronia, i quiz e le 10 domande (nel video ci sono solo le schede), ogni secondo del video (solo campionamento), tutte le pagine del PDF (solo copertina e testo).

