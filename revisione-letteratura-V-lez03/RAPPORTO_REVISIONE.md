# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 3 · Giosuè Carducci
Correzioni del 22/11/2026. Video: `Letteratura_Lez3_Parte1_1080p.mp4` (4 pezzi `.parte_00…03` da 90 MiB + `.sha256`). Ogni dato è etichettato **misurato**, **stima** o **non verificato**.

## 1. Misure sul video finale (misurato)
| Controllo | Risultato |
|---|---|
| Formato | 1920×1080, 30 fps, x264, AAC 192k 48 kHz |
| Durata / fotogrammi | **64:46,7 (3886,7 s)** · 116 602 fotogrammi (limite 65 min: margine 13 s) |
| Peso | 306 MB (una sola codifica, sotto i 400; video CRF 25, AAC 160k) |
| Volume | −16,7 LUFS; picco vero −1,6 dBTP (`ebur128=peak=true`, misurato sul file finale) |
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
- Checklist §11: spunta indipendente in `CHECKLIST_11.md`. Voci aperte: copertina PDF/video con sottotitolo e card ARGOMENTI (come nel modello); «Prof. Giorgio Mazzotti» nel piè delle slide del **video** (tolto solo nei PDF) e in testo_youtube; qualche errore ASR nel vtt («Josué», «Val di Castello»). Dopo la ricodifica per il peso il `controllo_severo` non è stato rilanciato (stessi fotogrammi, stessa durata; scatto jingle e fotogrammi rimisurati).

## 6. Correzione ingresso approfondimenti (25/11, seconda versione)
**File nuovo: `Letteratura_Lez3_Parte1_1080p.mp4` (4 pezzi `.parte_00…03` + `.sha256`), consegnato il 25/11/2026 alle 21:20 (UTC).** sha256 `5077745372543faeeb00c8ea3248defb73e2e950d8b7a51d206706a28a2243e2`.
- La prima versione metteva AP2 a **25:07** (nel video nuovo). Sara chiedeva **25:48**. Ora AP2 entra a **25:51,0** nel video nuovo (1550,97 s): è la fine di frase più vicina a 25:48 (le precedenti stanno a 25:36 e 25:07).
- **Verifica sulla trascrizione/energia:** il prof finisce «…per fuggire verso il sogno del passato.» (25:49,7), poi un «Mm.» (25:50,5–25:50,8), poi **silenzio −60 dB** fino a 25:51,5; la frase seguente («Una sorta di estetismo…») parte a 25:51,5 dopo l'approfondimento. Entrata e uscita (dissolvenza 0,33 s con `trans.wav`) cadono tutte nel silenzio; nessuna parola tagliata.
- **Slide al ritorno:** l'approfondimento rientra sulla «Pagina 16» (card «Ritorno all'ordine e al classicismo» accesa), cioè la slide che prima compariva a 26:30. Il cambio di slide (orig. 26:27) cade sotto l'approfondimento, quindi non ho composto nessuna schermata: sono fotogrammi originali.
- **Vecchio punto (23:19):** tolto l'approfondimento; il prof dice «…fosse clericale» · pausa 0,2 s · «lo era molto meno…». Per 0,25 s i fotogrammi del riquadro del prof (dissolvenza originale dell'approfondimento) sono stati **ricostruiti** per inversione: da guardare a 23:20.
- **AP1** (19:55): entra nel silenzio dopo «…il millecinque, no.»: già a posto, non spostato.
- **Durata e fotogrammi invariati: 116 602 fotogrammi (3886,7 s)**; Q1–Q4, mappa, glossario, verifica e compiti allo stesso secondo (nessuna modifica dopo 26:32). Rigenerati `.vtt`, `timeline.json` (AP2 = 1550,967 s), `scheda_pubblicazione.json`. Codifica: solo 23:18–26:32 ricodificato (CRF 25), il resto copiato; audio AAC 192k rifatto. 298 MB, −16,7 LUFS, −1,6 dBTP.
- **controllo_rapido.py: ESITO «DA CORREGGERE»** per un solo motivo, già presente il 22/11 e non toccato: «Prof. Giorgio Mazzotti» nel piè di pagina delle slide (non bloccante dal 23/11, §12). Pause mute: nessuna; schermate ferme >3 min: nessuna; titolo copertina «3/4 parole» (la copertina dice «Giosuè Carducci»).
- **NON fatto — schede blu:** schemi di ripasso, glossario, riepilogo e compiti di questa lezione sono **ancora bianchi con l'onda a barre in alto a destra** (visibile sul foglio a 47:14 e 63:25). Non li ho rifatti (non ho i sorgenti e la correzione chiedeva solo lo spostamento). Se vanno rifatti in blu scuro serve una decisione della master e più tempo.
- **Non verificato:** ascolto umano delle giunzioni (23:19, 25:51); sync labbra e sottotitoli non rimisurati.

## 7. Correzioni di Sara del 26/11 (terza versione)
**File nuovo: `Letteratura_Lez3_Parte1_1080p.mp4` (3 pezzi `.parte_00…02` + `.sha256`), consegnato il 26/11/2026 alle 12:27 UTC.** sha256 `7e0c169ec4704af1ea65c55e9550db826df913ec2dc8eaf79a349639e2c63769`.
**Nuova durata: 3957,9 s = 65:57,9** (118 736 fotogrammi; prima 64:46,7). Oltre i 65 minuti per via dei compiti letti da Kore (76,5 s): decide la master se dividere in due Parti.
1. **Schema di ripasso 2 (30:10):** tolto «va bene» che il prof diceva sopra la scheda e 2,0 s di scheda muta (taglio nel silenzio −57 dB, 30:12,4–30:14,4). L'ultima frase del prof finisce intera («…tutte le sue fasi e alcuni testi.» a 30:12,1). **Resta:** la scheda blu entra alla stessa posizione di prima, cioè durante «…tutte le sue fasi e alcuni testi» (dissolvenza 30:10,4–30:10,9): per non averla sopra la voce servirebbe il video del prof nel pezzo coperto, che non ho. La scheda non è stata toccata.
2. **Schema di ripasso 3 (47:01):** la scheda parte 2,4 s prima: tolti i secondi muti del prof (taglio in silenzio digitale, 46:59,2–47:01,6 del video precedente; dissolvenza di 0,2 s tra due fotogrammi del prof fermo). Scheda e sua voce non toccate. Inoltre accorciata di 1,5 s la pausa muta di 2,8 s prima del Quiz 3 (nella scheda, −45 dB).
3. **Mappa (61:32):** tolta la schermata bianca «Le parole chiave della lezione» (lampo del glossario) e il bianco vuoto: dal Quiz 4 si dissolve (0,4 s) sulla pagina della mappa con titolo, legenda e piè di pagina; la voce «La mappa concettuale del professore.» resta e il riquadro «Giosuè Carducci» compare dove compariva. Durata invariata.
4. **Verifica finale** e **Compiti**: ora blu scuro animato a tutto schermo, senza fasce. Verifica: dissolvenza 0,5 s dalla scheda di riepilogo, stesso testo, dissolvenza al nero come prima.
5. **Compiti letti da Kore (voce COMPITI):** dopo l'intro «Compiti» (jingle), una scheda per compito, bordo giallo, parole esatte del docente come in `compiti.json`, scheda finale con «Svolgi i compiti qui sotto e premi Consegna…». Cambio scheda nelle pause della voce (misurate sul file: 18,9 s, 34,5 s, 49,3 s, 70,4 s). Voce con +2 dB, picco −1,6 dBTP. Compiti di 78,5 s (prima 1,4 s).
- Rigenerati: `.vtt` (cue compiti aggiunte e spostamenti), `timeline.json`, `scheda_pubblicazione.json` (`durata_s`, quiz e mappa spostati; `compiti_s`). Quiz e verifica non cambiano contenuto: **tempi spostati** di −2,0 s (Q2), −5,9 s (Q3, Q4, mappa, glossario, riepilogo).
- **controllo_rapido.py:** ESITO «DA CORREGGERE» solo per il nome del docente nel piè di pagina (già c'era, non bloccante dal 23/11). Pause mute: nessuna; peso 245 MB; −16,6 LUFS; picco −1,6 dBTP; schede con fasce: nessuna.
- **Non verificato:** ascolto della voce COMPITI e dei tagli; i 4 cambi scheda dei compiti sono stimati dalle pause del file audio, non da una trascrizione. Le schede blu dei ripassi (R1–R4), glossario e riepilogo sono quelle di prima (le rifà la master). Sincronia labbra/sottotitoli non rimisurate.
