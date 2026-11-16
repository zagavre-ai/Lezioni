# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 18 · Eugenio Montale
**PRIMA VERSIONE (17/11/2026, ~01:30 ora italiana) — stato: IN REVISIONE, non ancora consegnata.**
Etichette: **misurato** = con uno strumento; **stima** = dedotto; **non verificato** = non potuto.
Fonte: video montato `consegna-letteratura-V-lez18` (sha256 corretto, 53:39,5, 96 585 fotogrammi, 1080p) contro l'originale `Letteratura_Lez18.mp4` (29:25,7). Trascrizione di entrambi con `trascrivi.py`; fotogrammi 1/s sul video vecchio; allineamento audio con `allinea.py`.

## 1. Problemi trovati (tutti **misurati**, tempi sul video vecchio)
| Minuto | Tipo | Com'era | Correzione prevista |
|---|---|---|---|
| 28:27–31:44, 34:30–38:51 | **sincronia (grave)** | I pezzi del prof non corrispondono agli argomenti: il pezzo «D4» (orig. 16:52–20:09) è la spiegazione di *Spesso il male di vivere* (argomento 3) ma sta dopo il quiz 3 e sotto il cartello «Le occasioni»; mentre il prof spiega *Spesso il male* sullo schermo c'è la slide «Le occasioni (1939)». Il pezzo «D5» (orig. 20:09–24:30) è Le occasioni + La bufera, ma sta sotto «La bufera e altro e Satura». Stesso sfasamento per D6. | Rifatto il piano: argomento 3 = orig. 8:07–20:10; 4 = 20:10–22:41; 5 = 22:41–25:12; 6 = 25:12–29:25. I quiz 3, 4, 5 cambiano secondo: tabella vecchio→nuovo nel rapporto finale. Durata totale invariata. |
| tutto il video | **pagina** | **Nessuna pagina del libro** nel video, ma il prof legge e mostra 4 testi (orig. 8:16–10:55 *I limoni*, 12:55–13:52 *Meriggiare*, 16:55–17:25 *Spesso il male*, 25:50–26:28 *Ho sceso*). Zip HD `Lez18_ingrandita.zip`: p. 756, 757, 758, 762, 763, 765, 789. | Fettine dagli screen HD a tempo con la voce, controllo `controllo_fettine.jpg`. |
| 6:24, 16:21, 21:00, 33:06, 41:01, 48:59, 50:22 | **visivo/contenuto** | Le 7 «mappe concettuali» del video e del PDF `Mappe_…pdf` sono **inventate da noi** (nodi tipo «es. 1896», «antilirico»…); la mappa del prof (`LEZIONE 18.pdf`) è **una sola** (Vita; poesia; linguaggio; Opere: 4 raccolte e 3 opere in prosa). | Mappa del prof impaginata nella nostra grafica (senza logo di terzi né foto), PDF mappe = quella; nel video 7 inserti con voce nuova (`R1…R6`, `RF`, **già inviati** a `voci-letteratura-V-lez18`) che leggono **solo** la mappa del prof (+ riprendono le slide). |
| 38:49–38:51 e 42:35 | **audio** | **Frase ripetuta** «…con tanto di testo/testi» (fine D5 e inizio D6 sovrapposti di 1,8 s, orig. 24:28–24:30). | Taglio dei pezzi su una pausa (orig. 25:12,65). |
| 12:02 / 15:22 | audio | Pezzo D2 finisce a metà parola «vog|liamo» (orig. 8:05,9) e D3 riprende da lì (con 4 pezzi di mezzo). | Tagli su pause ≥ 0,4 s (misurate sull'originale). |
| tutto | **visivo** | Grafica non nel modello Spagnolo: fondo scuro nelle schede, pannello laterale blu nelle slide col prof, riga «ARGOMENTO 1 · LA VITA» (deve essere «01 · LA VITA»), riquadro piccolo con bordo blu, niente fascia gialla, piè di pagina diverso, schede Quiz/Verifica/Compiti scure. | Tutto rifatto nel modello (punti 000.1–000.11). |
| 5:28, 16:21… | visivo | Highlight scelte a occhio (card in corso ≠ frase del prof). | Rifatte dalle parole del prof (trascrizione). |
| file | testo | `scheda_pubblicazione.json` e `testo_youtube`: titolo «Eugenio Montale · Parte 1» | «Letteratura V · Lezione 18 · Eugenio Montale» |
| file | consegna | `Test_Letteratura_Lez18.xlsx` è il modello vuoto con 38 righe; mancano `verifica_finale.json`+xlsx del prof | Prodotti dalle 10 domande di «DOMANDE LEZIONE 18.xlsx» (misurato: 10 domande, 4 risposte ciascuna). |
| file | consegna | mancano `…_slide.pdf` come da regola (c'è `dispensa_A4.pdf`, 13 pagine, grafica scura) | `…_slide.pdf` A4 orizzontale, pagine = fotogrammi del video. |
| 22:08 slide p. 9 | contenuto | «clima storico del **dopoguerra** e degli anni trenta» (Le occasioni, 1939) — è anche nella slide originale del prof | **DA CONFERMARE COL PROF** (lasciato com'è). |

**Verificati e OK (misurati):** compiti = PDF del prof (4 esercizi, testo identico); sha256; 1920×1080 30 fps; volume prof −16,6 LUFS (controllo_finale del montatore); mappa del prof = 1 pagina.

## 2. Piano e tempi (stima)
Ore 01:30 prima versione → ~04:30 consegna (stato `consegna prevista 04:30`). Passi: slide nel modello (generatore HTML → PNG) · riquadro 4:3 dall'originale (webcam 243×139 px, crop 185×139 → 412×310) · audio del prof dall'originale con la catena del kit · fettine HD · voci R1…RF (in generazione) · video a pezzi + sha256 · vtt riletto e corretto · PDF slide/mappe · verifica_finale/compiti/scheda · controlli.

## 3. Cosa NON ho ancora verificato
Ascolto dei punti (rumore), sottotitoli cue per cue, pronuncia di Kore (**Viessò** in S1 e S6 va riascoltato), fettine, PDF. Verranno trattati nella versione finale.
