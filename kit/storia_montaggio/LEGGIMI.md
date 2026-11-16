# Montaggio Storia V (chat S7, 16/11)
Script usati per le lezioni 18 e 20 (video 1092x614 con riquadro del docente 394x218, slide Telesio, inserti con voci Kore).
Ordine: trascrizione (Parakeet via /tmp/kit/.../pk.py) -> ancore (anchors*.py) -> ins.py/run_ins*.py (inserti) -> build_d*.py (pezzi del docente)
-> assemble*.py (pezzi .mov con audio PCM esatto) -> finale_a_pezzi.py -> subs*.py -> controllo_finale.py -> consegna*.py.
Attenzione: le immagini ferme lunghe nel concat vanno spezzate a 1 s (altrimenti ffmpeg usa decine di GB di memoria); la codifica va fatta in due passaggi (sfondo, poi riquadro).
Audio dei pezzi in PCM: con AAC ogni pezzo aggiunge ~10 ms e l'audio sfasa di oltre mezzo secondo a fine Parte.
