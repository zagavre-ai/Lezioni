# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 3 · Giosuè Carducci
Correzioni del 22/11/2026. Video: `Letteratura_Lez3_Parte1_1080p.mp4` (6 pezzi `.parte_00…05` da 90 MiB + `.sha256`). Ogni dato è etichettato **misurato**, **stima** o **non verificato**.

## 1. Misure sul video finale (misurato)
| Controllo | Risultato |
|---|---|
| Formato | 1920×1080, 30 fps, x264, AAC 192k 48 kHz |
| Durata / fotogrammi | **64:46,7 (3886,7 s)** · 116 602 fotogrammi (limite 65 min: margine 13 s) |
| Peso | ≈ 495 MB |
| Volume | −16,0 LUFS (LRA 7,0); picco −1,5 dBFS (campioni, dopo limitatore) |
| Pause > 2,5 s (silencedetect −45 dB, `controllo_severo`) | nessuna dopo i tagli: massimo 2,43 s |
| Scatto jingle Quiz | Q1–Q4: +0,003 s (limite 0,05) |
| Sincronia labbra/voce (sync5, 6 punti per pezzo) | copertina −0,008 · A1 −0,004 · A2 −0,034 · A3 0,000 · A4 −0,007 s (limite 0,04; A2 è un fotogramma, vicino al limite) |
| Timbro voce prof | rapporto >4 kHz/>100 Hz −11,7…−16,2 dB (originale ≈ −12,5/−15,9): dentro −9…−20 |
| PDF | slide: 63 pagine A4 orizzontale, testo selezionabile; mappe: 2 pagine (copertina «MAPPE» + mappa) |

## 2. Cosa è stato rifatto (22/11)
- **Testo a 40 px** in tutte le slide, interlinea 1,5, al massimo 3 card intere (nessuna «…», nessuna iniziale minuscola nelle card nuove), card alte quanto il testo; dove non entrava ho diviso la slide in **sotto-slide a finestra** che scorrono con la voce del prof (decisione della master: opzione 2).
- **Bordo giallo** all'inizio della frase del prof (±1 s sulla trascrizione).
- **Copertina** con titolo esatto; introduzione del prof 1:30 (≤3 min), poi slide «Di cosa parliamo».
- **2 approfondimenti** Kore (AP1 41,5 s a 19:55, AP2 41,0 s a 23:20), solo con frasi e slide del prof, inseriti in pause tra frasi.
- **Mappa unica = quella del prof**, ridisegnata nei colori BES con legenda in alto a destra, costruita ramo per ramo con la voce (3 slide, riquadro giallo mentre la voce lo legge, mappa intera tenuta 4 s). Tolti logo mappe-scuola.com e foto dell'autrice.
- Ripassi R1–R4, glossario e riepilogo rifatti a 40 px (voci nuove S3B e RF2 per ripasso 3 e riepilogo; MAPPA1 per la mappa).
- **Nessuna schermata identica > 3 min:** la slide «Dal radicalismo alla sintesi classica» restava ferma 3,5 min (circa 26:50–30:15); ho aggiunto una finestra con la card 1 quando il prof parla dell'Italia di Umberto I (stessa «Pagina 17»).
- **Pause > 2,5 s accorciate** (8 tagli, 7,8 s in tutto, solo tra frasi e dove la slide non cambia; più 7,9 s di silenzio nelle schede finali). Tagli e ripasso 3: i secondi cambiano rispetto alla consegna del 17/11.
- Audio prof: catena del kit, −16 LUFS; jingle quiz/titolo/repaso/trans del kit su ogni cambio.
- Dati rigenerati sul video finale: `.vtt` (1129 cue, anche le voci Kore), `timeline.json`, `scheda_pubblicazione.json` (titolo «Letteratura V · Lezione 3 · Giosuè Carducci»), `testo_youtube.txt`. `quiz_argomenti.json` e `verifica_finale.json` non contengono secondi (invariati).
- Nuove sezioni nella scheda: `approfondimenti_s`, `mappa_s`, `glossario_s`, `riepilogo_s`. Argomenti e quiz: vedi `scheda_pubblicazione.json` (es. Quiz 1 a 11:35, Quiz 4 a 61:27).

## 3. Pezzi del prof: inizio e fine (misurato sulla trascrizione)
| Pezzo | Inizio (min) | Prime parole | Fine (min) | Ultime parole | Frase finita |
|---|---|---|---|---|---|
| Introduzione | 0:45,8 | «Buongiorno e benvenuti alla lezione su…» | 1:50,8 | «…Realtà.» | sì |
| Argomento 1 | 1:59,5 | «visto che è il primo vero e proprio…» | 11:04,0 | «…per i suoi versi, d'accordo?» | sì |
| Argomento 2 | 11:46,7 | «Questi versi, l'evoluzione ideologica…» | 30:12,1 | «…tutte le sue fasi e alcuni testi.» | sì (le ultime parole, ~1,7 s, si sentono mentre compare la scheda del ripasso) |
| Argomento 3 | 30:57,9 | «Quindi in questa seconda parte…» | 46:58,9 | «…piuttosto dolorosa.» | sì |
| Argomento 4 | 47:50,6 | «e dicendo questo allora» | 60:49,6 | «…con tanto di testi in questa lezione.» | sì |
Il prof non è mai tagliato a metà frase: i tagli di pausa cadono solo in silenzio tra una frase e la successiva.

## 4. Controllo severo (`controllo_severo.py`, passo 15 s)
Esito dell'ultima esecuzione: vedi la riga finale in `controllo_severo_esito.txt`. Residui noti, non risolvibili senza alterare il materiale del prof:
- **«…» in 8 campioni (43:52–45:52, pagina del libro «Pianto antico»):** sono i puntini scritti nelle **note del libro** («7. lo ristora … calor», «8. Tu fior … inaridita», «11. estremo … fior») nelle fettine del prof, non card spezzate. Le fettine sono intere (vedi `controllo_fettine.jpg`).
- «Possibili card con iniziale minuscola» (4:37, 6:07, 6:37, 8:52, 64:22): segnalazioni da guardare; le card nuove iniziano con la maiuscola, l'OCR legge la riga d'appoggio / una parola della scheda finale.

## 5. Cosa NON ho verificato
- Le voci Kore **AP1, AP2, S3B, RF2, MAPPA1** non sono state ascoltate (solo trascritte con ASR: testi giusti, numeri giusti); la pronuncia di «Levia Gravia», «Giambi ed Epodi», «Odi barbare» va controllata all'orecchio. S3B resta «DA CONTROLLARE».
- Date nella mappa e nelle slide del prof: **DA CONFERMARE col prof** dove non coincidono (la mappa dice 1835–1907; le slide hanno gli stessi anni, ma «1860 cattedra» vs «dal 1860… per 40 anni»).
- Tempi di evidenziazione delle card e delle fettine: **stimati** dalla trascrizione, ±1 s, non misurati fotogramma per fotogramma.
- Rumore del prof (arnndn) non dimostrabile all'ascolto.
- Schede Quiz, titoli argomento e la coda (Verifica finale, sigla, Compiti) sono quelle già approvate, non rifatte; i silenzi lunghi di queste schede sono stati accorciati a 2,4 s.
- Checklist §11 della master: la spunta indipendente è in `CHECKLIST_11.md` (se presente), altrimenti non fatta.
