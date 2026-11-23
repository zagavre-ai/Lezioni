# Storia dell'arte V · Lezione 13 · strumenti di montaggio (chat storia-arte-V-lez13)
Percorso di lavoro: /tmp/claude-0/w (materiali in mat*, trascrizione trasc.json, script in prod/).
Ricostruzione: 1) estrai.py scarica video/slide/mappe/domande dalla release mazzotti-storia-arte-V (senza token);
2) trascrivi.py sul video -> trasc.json (già qui); 3) pdfimages -> im/ (già qui, ingrandite Lanczos+nitidezza);
4) voci in prod/vox/ (Kore, dalla master) o provvisorie (tts.py, Piper); 5) render_all.py -> assemble.py --all -> subs.py -> dispensa.py -> misure.py -> controllo_rapido -> pack.py.
Un'unica codifica finale x264 CRF 19 (assemble.py: pezzi intermedi CRF 10, poi una sola codifica).
