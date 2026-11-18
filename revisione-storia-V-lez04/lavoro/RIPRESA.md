# Come riprendere la lezione 4 di Storia V quando arrivano le voci Kore
Cartella di lavoro: tutti gli script sono in questa cartella; i percorsi interni usano `/tmp/claude-0/w` (cambiarli con `sed` se serve).
Ingressi grandi da riscaricare (release `mazzotti-storia-V`): video `LEZIONE.4.LA.PRIMA.GUERRA.MONDIALE.mp4` → `dl/v.mp4`; zip slide/mappe/test/compiti (vedi indice); kit (`kit/` su main).
1. Voci: ramo `voci-storia-V-lez04`, file `scambio/storia-V-lez04/vox/NOME.wav` (87 nomi in `testi_voci.json`) → copiare in `vox/`.
2. `python3 build_prof.py 1; python3 build_prof.py 2` (pezzi del prof, ~25 min con due processi in parallelo; richiede `fr/D.npy` = `D_pagine.npy`, `tr/lez04.json` = `trascrizione_prof.json`).
3. Per ogni Parte P (1, 2): `python3 finish.py P voci && python3 finish.py P schede && python3 finish.py P pezzi && python3 finish.py P monta` (pillole e riepilogo sono già disegnate con durate stimate a 14,7 car/s: la fase `schede` le ridisegna solo se la voce vera le smentisce).
4. `python3 docs.py P` (sottotitoli, scheda, YouTube, timeline), `python3 controlli.py P` (misure e foglio), `python3 pdfs.py`, `python3 rapporto_corpo.py; python3 rapporto.py`.
