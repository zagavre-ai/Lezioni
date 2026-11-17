# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 13 (Svevo) · Prof. Giorgio Mazzotti
Chat di revisione 13 · 17/11/2026 · **Misurato** = ricavato da file/strumenti; **stima** = valutazione mia. Stato: consegnata per il controllo della master.

## 0. Che cosa è cambiato rispetto alla consegna parziale del 16/11
Tutti i problemi del primo rapporto sono stati trattati, più quelli degli aggiornamenti del 17/11 (jingle, prof mai tagliato a metà frase, ombre, mappe solo del prof). Non ho rifatto il montaggio da zero (mancano i sorgenti): i video sono ricomposti a segmenti dal montato vecchio e dal video originale del prof, con filtri e inserti nuovi.

## 1. Durate e tabella vecchio → nuovo (la durata è cambiata: mappe nostre tolte, frasi ripetute tolte, apertura Parte 2 e mappa del prof aggiunte)
| | Parte 1 | Parte 2 |
|---|---|---|
| Durata vecchia | 3143,9 s (52:23,9) | 3200,3 s (53:20,3) |
| **Durata nuova (misurata)** | **3108,0 s (**51:48**)** | **3303,5 s (**55:03,5**)** |
| Peso | 324,9 MB (<400) | 341,0 MB (<400, ricodificata a CRF 21 perché a CRF 19 pesava 401,9 MB) |
Secondi di inizio argomento e di quiz (vecchio → nuovo), da riportare in `scheda_pubblicazione.json` (file `scheda_P1.json` / `scheda_P2.json` già aggiornati):
| Parte | Argomento | inizio vecchio → nuovo | quiz vecchio → nuovo |
|---|---|---|---|
| 1 | 1 · L'inetto e il pensiero sveviano | 227.848 → 227.833 s | 1687.981 → 1645.4 s |
| 1 | 2 · Una vita e Senilità | 1693.281 → 1650.7 s | 2500.748 → 2417.9 s |
| 1 | 3 · La coscienza di Zeno | 2506.048 → 2423.2 s | 3098.249 → 2983.8 s |
| 2 | 4 · Testi da La coscienza di Zeno | 17.982 → 67.0 s | 3059.716 → 3085.467 s |

## 2. Problemi del rapporto 16/11 e come sono stati chiusi
| # | Problema | Esito |
|---|---|---|
| 1 | Prof nel tondo | **CORRETTO** riquadro 4:3 **372×279 px a x 1468, y 146** (non 410×308: a 410 copriva il bordo destro delle pagine del libro), angoli arrotondati, **ombra grigia morbida**, fascia gialla −3° «Giorgio Mazzotti / PROF. DI LETTERATURA ITALIANA» solo dove il prof c'è. Il vecchio nome sotto il tondo è coperto ovunque |
| 2 | Sfondo grigio-azzurro | **CORRETTO** bianco su tutto il video e nel PDF |
| 3 | Piè di pagina senza «V» | **CORRETTO** «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» (anche sopratitolo della copertina «LETTERATURA ITALIANA V · VIDEOLEZIONE») |
| 4 | Sottotitoli mancanti sulla voce | **CORRETTO** rifatti dai testi esatti delle voci |
| 5 | Sottotitoli del prof con errori | **RILETTI**: 3 revisori hanno letto tutti i 1142 cue del prof; 698 corretti applicati (nomi, parole inesistenti, apostrofi; 27 correzioni meno sicure le ho riportate al testo originale). Restano **148 cue segnalati come dubbi** (elenco in `sottotitoli_da_riascoltare.txt`) . Non ho riascoltato l'audio: i passi del libro letti dal prof sono ricostruiti a memoria del testo di Svevo, **da riascoltare a campione** |
| 6 | Apertura Parte 2 senza ripasso | **CORRETTO**: benvenuto (voce IN2) + ripasso della Parte 1 (voce RIP) con le 4 card che si evidenziano a tempo |
| 7 | Frasi ripetute (3 punti P1) | **CORRETTO** tagliate audio+video insieme su pause: P1 24:29/25:28, 38:42/39:36, 48:56/49:44 (vecchi minuti) |
| 8 | «Il successo con il pubblico…», «l'amaro in bocca» | **NON ERANO ERRORI**: sono nel testo delle voci (la «mano in bocca» era solo la trascrizione automatica) |
| 9 | Mappe inventate (6) | **CORRETTO** tolte; nel video e nel PDF **solo la mappa del prof** («ITALO SVEVO»): panoramica + zoom su vita, stile, tematiche, opere, letta dalle voci nuove MP1–MP3 (testo tratto solo dalla mappa), a fine di ogni Parte |
| 10 | Fettine del libro tagliate | **CONTROLLATE tutte**: 220 stati di slide; **8 con riga tagliata** (2 in basso: note a piè di pagina, 6 in alto), coperte → restano solo righe intere. Le altre erano già intere |
| 11 | Dispensa PDF difettosa | **CORRETTO**: `Letteratura_Lez13_slide.pdf` dai fotogrammi del video (senza riquadro e senza nome) |
| 12 | Titoli schede | **CORRETTO** «Letteratura V · Lezione 13 · Italo Svevo · Parte N» + descrizione |

## 3. Aggiornamenti del 17/11 (01:20, 01:25, 01:30, 08:15)
- **Jingle (01:20):** nel montato c'erano già il jingle dei Quiz (correlazione 0,95, scatto **+0,5 s dall'inizio scheda = 0,0 s sull'audio**) e `titolo.wav` sui titoli (0,98). Mancavano negli approfondimenti animati e nella pillola nuova: aggiunti i jingle **ufficiali del kit** (`trans.wav` all'inizio di ogni approfondimento e della mappa, `repaso.wav` sulla pillola di apertura Parte 2), con **transizione**: dissolvenza di 0,5 s dalla scena precedente. Scarto dello scatto Quiz (`controllo_jingle.py`, atteso inizio scheda +0,5 s): P1 Q1 −0,043 s, Q2 −0,044 s, Q3 −0,045 s; P2 Q4 −0,043 s: **tutti ≤ 0,05 → OK**. Jingle nuovi: 8 nella Parte 1, 7 nella Parte 2 (+ pillola di apertura e mappa). Le pillole «R» del montato hanno già il loro jingle (correlazione 0,33–0,48 perché sotto la voce): **non riascoltato**. I jingle nuovi **non li ho ascoltati**, solo misurati.
- **Prof mai tagliato a metà frase (01:25):** trovati 2 pezzi della Parte 1 e 1 inizio della Parte 2 sbagliati. Corretti: **D1** finiva su «…i suoi» → esteso con «fondamentali.» (audio e riquadro dall'originale, ≈ +0,85 s); **D3** finiva su «narrativa» → esteso con «psicologica.» (+0,9 s); **inizio P2** partiva dalla fine di «psicologic[a]» → tagliato alla frase successiva. Tabella sotto.
- **Ombre e card (01:30):** il riquadro ha ombra grigia sfocata; le card «in corso» del montato hanno già bordo giallo e ombra morbida (verificato a vista nelle slide); le slide nuove (ripasso Parte 2, mappa) usano lo stesso stile.
- **Mai immagine ferma del prof (08:15):** `freezedetect` (n=−55 dB, d≥0,8 s) **sul solo riquadro del prof**: **0 fermi nei pezzi del prof** (P1: 61 fermi totali nel riquadro, tutti fuori dai pezzi del prof; P2: 4, tutti fuori). (Sull'intero fotogramma la funzione dà falsi allarmi perché il riquadro è il 5% dell'immagine.) In copertina/presentazione il riquadro del prof **non c'è** (voce narrante): prima c'era il tondo fermo.
- **Sincronia labbra/voce (08:15):** misurata la correlazione tra l'audio del finale e quello dell'originale agli stessi offset del ritaglio: **Parte 1: 21 finestre, scarto massimo 0,037 s; Parte 2: 19 finestre, scarto massimo 0,020 s** (limite 0,04 s).
- **Picco audio:** limitato a ≈ −1,4 dBFS; **volume** P1 −16,6 LUFS, picco −1,5 dBFS; P2 −16,2 LUFS, picco −2,1 dBFS (ebur128, limiter prima della codifica AAC 192k).

### Fine e inizio di ogni pezzo del prof
| Pezzo | Fine (ultime parole) | Frase finita |
|---|---|---|
| P1 D0 | «…Partirei da qui. Allora.» | sì |
| P1 D1 | «…ciò che lo muove, ciò che lo interessa, i suoi temi **fondamentali**.» (esteso) | sì |
| P1 D2 | «…Emilio e la realtà dei fatti.» | sì |
| P1 D3 | «…Stiamo parlando di narrativa **psicologica**.» (esteso) | sì |
| P2 D4 | «…Terapia alla fine rimane ancora una volta malata.» (verificato sull'originale) | sì |
Inizi: D0 «Buongiorno e benvenuti alla lezione…», D1 «Dunque. Come vedete…», D2 «Adesso dobbiamo analizzare i tre romanzi», D3 «Giungiamo, in definitiva…», P2 D4 «Il testo si concentra in modo approfondito…»: nessuna parola mozzata.

## 4. Cosa NON ho fatto o non ho potuto verificare (dichiaro)
1. **Font delle etichette (15:10):** nelle slide già montate sopratitolo e piè di pagina sono in **DM Mono**, il modello ha **Figtree Bold**. Le slide sono immagini nel video e i sorgenti mancano: cambiarlo ovunque (incluso «Pagina N») richiede di rifare le slide. **NON CORRETTO**; le slide nuove usano lo stesso DM Mono per restare coerenti con il resto della lezione.
2. **Jingle:** non posso ascoltarli; ho misurato correlazioni e tempi. Il jingle Quiz dei Quiz: vedi §3.
3. **Rumore:** audio già pulito (−62 dB nelle pause); il modello arnndn del kit non è nel repository, non ho riapplicato la catena. Ascolto a 3 punti **non fatto**.
4. **Pagine del libro:** non ho rifatto le fettine con nuove posizioni (erano già per righe intere salvo 8 casi); manca la **tabella brano/pagina/minuto** e l'evidenziazione della fettina in corso. HD disponibili: `Lez13_ingrandita.zip` (26 pagine, pp. 464–497).
5. **Quiz e animazioni scure** («SCHEDA», «LINEA DEL TEMPO»): grafica diversa dal modello Spagnolo (fondo blu notte), non rifatta (mancano i sorgenti).
6. **Copertina:** la lista a card degli argomenti c'è, ma non è identica al modello (non rifatta).
7. **Sottotitoli del prof:** vedi riga 5 della tabella.
8. `controllo_finale.py` non eseguito (usa percorsi della master); ho eseguito a parte: controllo jingle, sincronia, freeze, volume, picco, conteggio fotogrammi.

## 5. Consegna
Video a pezzi `.parte_NN` + `.sha256` (`cat … > file.mp4`), `.vtt`, `Letteratura_Lez13_slide.pdf` (125 pagine A4 orizzontali), `Letteratura_Lez13_mappe.pdf` (mappa del prof), quiz, test (10 domande), compiti (4), schede, testo YouTube, timeline nuove, `controllo_minuti.jpg`, `sottotitoli_da_riascoltare.txt`, i jingle usati.
