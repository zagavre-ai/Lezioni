# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 9 · correzioni 22/11
Etichette: **[misurato]** · **[stima]** · **[non verificato]**

## 1. Cosa è cambiato rispetto alla consegna del 17/11
- **Mappa:** solo la mappa del prof, ridisegnata con i colori BES (5 colori + legenda), costruita ramo per ramo con la voce, evidenziazione gialla mentre la voce parla, una sola volta; tolti marchio e foto di terzi; le altre 9 mappe tolte. Compiti: solo Parte 2 (Parte 1 senza).
- **Slide:** card con frasi intere, testo 40 px (interlinea 1,5), al massimo 3 card; card gialla quando il prof comincia la frase; inserti «dal parlato del prof» per spezzare le slide lunghe.
- **Copertina Parte 1:** ora ≤ 3 min (140 s di D1 + intro), poi «Di cosa parliamo».
- **Spiegone Parte 2:** dopo la sigla, ripasso animato con voce Kore della Parte 1 (voci SPG), con immagini e mappa.
- **Voci Kore** rigenerate dalla master (R15–R20: erano troncate o con il nome del prof); verificate con trascrizione, bordi < 0,03.
- **Nome del prof** tolto dal piè di pagina (resta solo nella fascia gialla) e dai PDF. PDF slide A4 orizzontale + PDF mappe separato (copertina «MAPPE»).
- **Audio:** −16,4 / −16,1 LUFS [misurato], picco −2,1 dBFS; due pause lunghe del prof in P2 D1 accorciate di 1,4 s ciascuna.
- Rigenerati vtt, timeline_ParteN.json, scheda_pubblicazione_ParteN.json (titolo «Letteratura V · Lezione 9 · Giovanni Pascoli · Parte N»), secondi quiz/verifica.
- Durata: P1 53:28,6 (96 259 fotogrammi = durata × 30), P2 55:37,1 (100 116) [misurato].

## 2. Controllo severo (controllo_severo.py, Giovanni Pascoli)
**ESITO: RESPINTA nell'ultima esecuzione completa (P2); P1 prima della correzione copertina. NON è OK.**
Residui:
1. «…» segnalato in 30 campioni: sono i testi delle poesie del prof (X Agosto «dono…», L'assiuolo «chiù…») e «[...]» del brano T2; non sono card spezzate [da confermare].
2. «Pause > 2,5 s» (P1 9, P2 12): sono pause previste di quiz (pensiero), schede titolo e jingle, più alcune pause del prof di 2,7–3,0 s non accorciate (P1 ~1065, ~1384, ~1388, ~2578 s; P2 ~1164, ~2009, ~2908, ~2912 s). **Non corrette per mancanza di tempo.**
3. Dopo le correzioni (copertina P1, nome nel piè di pagina) il controllo severo **non è stato rieseguito** (tesseract troppo lento, scadenza 19:30 UTC).
Controllo indipendente (altro agente, 28–29 fotogrammi per Parte, non l'intera lista §11): copertina ≤ 3 min sì; mappa BES con legenda sì; nessuna sovrapposizione; nessun refuso evidente. Difetti trovati: (a) le slide «elenco 01/02/03» (P1 «La visione del mondo e Il fanciullino», P2 «Le idee politiche») hanno corpo ~24 px, **sotto 36 px: da correggere**; (b) nome del prof nel piè delle schermate mappa: coperto con rettangolo bianco nel video, **ma ancora presente nelle sorgenti**; (c) mappe senza «Pagina N»; (d) sigla finale kit troncata a «GRAZIE PER L'ATTE…» (asset del kit).
Il piè di pagina con il nome del prof era rimasto in tutte le slide per una cache di render: è stato **coperto in post con un rettangolo bianco** (ricodifica x264 CRF 19 aggiuntiva), non rigenerato.

## 3. Pezzi del prof (mai tagliati a metà frase)
| Parte | Pezzo | Nel video (min:s) | Nel video fino a | Tempo originale lezione | Finito a fine frase |
|---|---|---|---|---|---|
| 1 | D1 | 0:47 | 12:23 | 0:00–11:36 | sì |
| 1 | D2 | 17:48 | 21:15 | 11:36–15:02 | sì |
| 1 | D3 | 23:07 | 36:48 | 15:02–28:43 | sì |
| 1 | D4 | 43:01 | 46:49 | 28:44–32:31 | sì (l'inizio entra a metà frase del prof, già così nell'originale: da confermare) |
| 2 | D1 | 5:13 | 15:49 | 32:30–43:06 | sì |
| 2 | D2 | 19:27 | 30:58 | 43:09–54:40 | sì |
| 2 | D3 | 33:33 | 45:05 | 54:41–66:12 | sì |
| 2 | D4 | 48:31 | 51:36 | 66:12–69:17 | sì |
Tempi originali [stima da offset audio]. Tutti i fini pezzo verificati sulla trascrizione ASR come fine frase; l'unico inizio a metà frase è P1 D4 (già nell'originale).

## 4. Anomalie nel materiale del prof (non corrette, decide Sara)
Mappa: «1905/1906», «stupidi/stupiti»; risposte Excel «Italy» e «L'aria è del gemma»; mappa «studia all'università di Bologna: (come docente ha Carducci)».

## 5. NON verificato
Ascolto delle voci Kore (pronuncia); sottotitoli del prof non riletti per intero (ASR + correzioni); tempi di comparsa dei rami della mappa stimati dalle frasi; la mappa è su 3 schermate, non una; trans.wav solo ai Compiti (nessuna dissolvenza fra pezzi oltre 0,4 s di entrata); webcam morbida (ritaglio 184×138); lista §11 completa non spuntata; true-peak non misurato.
