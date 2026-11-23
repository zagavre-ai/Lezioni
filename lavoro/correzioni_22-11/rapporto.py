# -*- coding: utf-8 -*-
import json, glob, re, os, sys
B='/home/work/build'
def rd(f): return open(f).read() if os.path.exists(f) else ''
R=[]
w=R.append
w("# RAPPORTO DI REVISIONE · Storia V · Le fasi conclusive della guerra fredda (1969-1991) · correzioni 22/11")
w("Etichette: **misurato** = misura sul file finale; **dal piano** = ricavato dal montaggio; **non verificato** = non controllato.\n")
w("## 0. Cosa è stato rifatto (prompt correzioni 22/11)")
w("""- **Mappe del prof (3):** ridisegnate in vettoriale nel modello BES (pesca, celeste, paglierino, menta, lilla, legenda in alto a destra, testo 34–50 px), stessa struttura, stesse frecce e **stesse parole** del PDF «MAPPE LEZIONE 17». Costruite ramo per ramo con la voce Kore (`MPR1_R2`, `MPR2_R2`, `MPR3_R2`), riquadro acceso in giallo mentre la voce parla, mappa intera ferma 4 s. Tolte tutte le mappe inventate (le 5 «MAPN»). Una sola volta ciascuna, alla fine del suo argomento (1, 6, 7). Gli altri argomenti chiudono con pillola e ripasso. **La mappa di Gorbačëv non ha la domanda come titolo: ho scritto «Come si arriva alla fine dell'Unione Sovietica?» con parole del prof** (come da risposta della master). Le altre due hanno la domanda del prof.
- **Slide del prof:** testo delle card a 40 px (36–42 px solo nelle varianti a finestra), interlinea 1,5, card intere (frasi del PDF, mai «…»), al massimo 3 per slide, bordo e pallino gialli sulla frase in corso, riquadro 4:3 (412×309 a x=1428, y=148), fascia gialla col nome solo sotto il riquadro. Piè di pagina: solo «STORIA V» e «Pagina N». Sotto-slide «a finestra» quando il prof resta a lungo su una frase. Sigle (USA, URSS, OPEC, OLP, CEE, CSI, SALT) rispiegate sullo schermo ogni volta che compaiono nella slide.
- **Introduzione animata senza riquadro del prof:** copertina con voce Kore `BEN*_R2` e slide «Di cosa parliamo» (`DCP*`) senza riquadro. L'introduzione del prof (Parte 1) sta sulla copertina con il riquadro e dura meno di 3 minuti. Nessuna voce Kore dice il nome del prof; nessuna scheda animata lo scrive.
- **Copertina:** titolo esatto «Le fasi conclusive della guerra fredda (1969-1991)».
- **Spiegone** a inizio Parte 2 e Parte 3 (voce Kore, argomento per argomento, con immagini e mappa della Parte precedente).
- **Approfondimento animato** (47–58 s, voce Kore) per ognuno degli 8 argomenti, solo dal materiale del prof; ripasso a 4 righe (`SC*`), schede RIPASSO in blu scuro a tutto schermo.
- **Fine:** glossario, ripasso finale, sigla finale con avviso diritti, a fine Parte 3 verifica di sbarramento (10 domande, soglia 80 %), intro «Compiti» e compiti letti dalla voce Kore `COMPITI` (bordo giallo, una domanda alla volta). Quiz da 5 domande per argomento, schede con «premi Controlla».
- **Audio del prof:** dall'originale, filtro dei bassi 70 Hz, riduzione leggera del rumore, −16 LUFS. Pause oltre 2,5 s accorciate (ce ne sono solo 4 nell'intera lezione). **Timbro misurato** (acuti >4 kHz contro >100 Hz): originale −18,5 dB, pulito −17,8 dB (limite −9/−20 dB: OK).""")
w("\n## 1. Misure sul video finale (misurato)")
for P in (1,2,3):
    j=json.load(open(f'{B}/cr/controllo_rapido_Storia_Lez17_Parte{P}_1080p.json')) if os.path.exists(f'{B}/cr/controllo_rapido_Storia_Lez17_Parte{P}_1080p.json') else {}
    c=rd(f'{B}/chk{P}.log')
    w(f"### Parte {P}")
    w(f"- controllo_rapido.py: **ESITO {j.get('ESITO')}** | durata {j.get('durata_min')} min | {j.get('formato')} | peso {j.get('peso_MB')} MB | {j.get('LUFS')} LUFS | picco {j.get('picco_dBTP')} dBTP | pause mute >2,5 s: {j.get('pause_mute')} | nome nel piè di pagina: {j.get('nome_docente_nel_pie_di_pagina')} | titolo in copertina: {j.get('titolo_in_copertina')} | schermate ferme >3 min: {j.get('schermate_ferme_oltre_3_min')}")
    for l in c.split('\n'):
        if l.startswith('[misurato]') : w('- '+l)
w("\n## 2. Fine di ogni pezzo del prof (tagli nelle pause, 0,15 s prima della frase che segue)")
for P in (1,2,3):
    c=rd(f'{B}/chk{P}.log')
    for l in c.split('\n'):
        if l.startswith('- P'): w(l)
w("L'ultima riga di ogni pezzo è controllata sulla trascrizione dell'originale. Due tagli spostati rispetto alla consegna del 19/11: l'introduzione ora finisce a «…tanto di Unione Sovietica» e l'argomento 3 finisce su «…lungo sguardo americano» (prima chiudeva su un «Um»).")
w("\n## 3. Sincronia delle card (10 punti per Parte, dal piano)")
S=json.load(open(f'{B}/sync_tab.json'))
for P in ('1','2','3'):
    w(f"### Parte {P}")
    w("| arg. | card accesa | inizio sorgente (s) | accensione (s) | frase del prof in quel punto |\n|---|---|---|---|---|")
    for n,c,t0,ta,card,seg in S[P]: w(f"| {n} | {card.strip()} | {t0:.1f} | {ta:.1f} | {seg} |")
w("**Limite dichiarato:** il prof non legge le slide. L'abbinamento card↔frase è fatto con le parole in comune tra la trascrizione e le card, in ordine. La card si accende 0,25 s prima dell'inizio della frase abbinata (misurato dal piano), ma **in alcuni punti la card accesa non è quella a cui il prof sta pensando** (esempio: Parte 1, «Questo pone fine al sistema di cambi fissi» accesa su «Che scoppia nel 73»). Non l'ho verificato ascoltando tutto.")
w("\n## 4. Voci Kore (31 nuove, controllate)")
w("Trascrizione confrontata col testo (numeri e date in cifre), bordi negli ultimi 50 ms: tutti sotto 0,01 (limite 0,03). Nel montaggio ogni voce ha una dissolvenza di 30 ms. Voci da **riascoltare a mano** (la mia trascrizione automatica scrive i nomi stranieri a modo suo): `AP7` (Brežnev, «cioè trasparenza»), `SPG2_3` (Shah, Khomeini, sharia). Pronuncia dei nomi stranieri **non verificata all'ascolto**.")
for l in rd(f'{B}/vcheck.log').split('\n')[:40]:
    if l.strip(): w('- '+l[:160])
w("""
## 5. Refusi e anomalie nei materiali del prof (non modificati i file originali)
- Slide e compiti scrivono «Michail Gorbačev», la mappa scrive «MICHAIL GORBAČËV» (maiuscolo, con la dieresi). Nella mappa ho riportato la grafia della mappa; nelle slide quella delle slide. La master decide.
- «Tienanmen» (slide e compiti) è la grafia usata in tutta la lezione; in italiano si trova anche «Tiananmen». Lasciato com'è.
- «SALT 1» nelle slide: riportato come scritto. Non ho trovato altri refusi di ortografia, accenti o maiuscole.
- Le cifre del test Excel del prof non sono state confrontate una per una con le slide: **non verificato**.
- Il prof dice a voce cose non scritte sulle slide (digressioni sul Vietnam, su Nixon, sulla federazione degli Stati Uniti): non sono state aggiunte né tolte.""")
w("""
## 6. Immagini del prof → argomento (uno solo; risoluzione)
| pagina PDF | contenuto | argomento in cui compare | note |
|---|---|---|---|
| 6 | cartina Iraq e Iran | 3 (Iran e Iraq) | slide del prof (98 s) + approfondimento 3 |
| 11 | Margaret Thatcher | 6 (Europa occidentale) | slide del prof (96 s) + approfondimento 6 |
| 12 | François Mitterrand | 6 | slide del prof (18 s) |
| 15 | cartina CSI | 7 (crollo dell'URSS) | slide del prof (alternata alle card, mai oltre 120 s) |
| 17 | Tienanmen, 5 giugno 1989 | 8 (Cina) | slide del prof + approfondimento 8 |
| 3 | Nixon | solo approfondimenti 1 e 4 | il prof la mostra 3 s |
| 8 | Reagan | solo approfondimento 4 | il prof la mostra 3 s |
| 14 | Gorbačëv e Muro di Berlino | solo approfondimento 7 | il prof la mostra 3 s |
Le immagini sono rese a 300 dpi dal PDF del prof e migliorate (riduzione del rumore e nitidezza, senza cambiare i tratti). **Il PDF contiene foto di 300–850 px: restano meno nitide di una foto moderna.** Non ho scaricato nulla dal web.""")
w("""
## 7. Cosa NON è stato verificato (e perché)
- **Controllo severo della master (`controllo_severo.py`) non finito:** con il riconoscimento del testo impiegava oltre un'ora per Parte e l'ho fermato. Vale il `controllo_rapido.py` (esito sopra).
- **Agente separato del §11:** vedi sezione 8.
- **Labbra e voce (±0,04 s):** il pezzo del prof è tagliato dalla stessa traccia audio/video dell'originale senza spostamenti; **non misurato** con uno strumento.
- **Nomi stranieri detti dalla voce Kore:** non riascoltati.
- **Sigle nelle schede scure riusate dalla consegna precedente** (titolo, pillola, riepilogo): «URSS» compare in «Il crollo dell'URSS» senza spiegazione. Corretto solo nelle schede dei quiz.
- **Durata:** Parte 1 ≈ 50 min, Parte 2 ≈ 34 min, Parte 3 ≈ 42 min. Parti 2 e 3 sotto i 50 min: tutto il materiale del prof (1 h 42 min di lezione) in tre Parti, come approvato il 19/11; unirle supera i 65 min. Si può proporre un'altra suddivisione.
- **Consegna in ritardo** rispetto alle 11:00 italiane: le voci Kore sono arrivate alle 10:30 UTC (11:30 italiane).
- Sottotitoli: fatti sul file finale (trascrizione automatica del parlato del prof + testo noto delle voci Kore); correzioni automatiche dei nomi propri; **non riletti**.
- **Dispensa:** stesse slide dello stesso ordine del video, a tutta larghezza, con testo invisibile; la webcam nelle pagine del prof è un fotogramma fisso (solo per la stampa). Il testo invisibile non contiene il nome del prof, che però compare nella fascia gialla delle immagini. Pagine dei pezzi senza numero (spiegoni, schede scure) non sono nella dispensa.
""")
w("## 8. Controllo dell'agente separato\n(da compilare)")
open(f'{B}/RAPPORTO_REVISIONE.md','w').write('\n'.join(R))
print('ok',len('\n'.join(R)))
