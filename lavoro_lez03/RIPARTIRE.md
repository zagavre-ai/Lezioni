# Ripartire (se il contenitore è nuovo)
1. Scaricare con scambio/mazzotti/correzioni_22-11/estrai_da_release.py (release mazzotti-storia-arte-V): "LEZIONE 3 IL REALISMO" -> /tmp/w/src, "MAPPE LEZIONE 3.pdf", "SLIDE/LEZIONE 3.pdf" (-> /tmp/w/slide/s.pdf), "DOMANDE.LEZIONE.3.xlsx".
2. Copiare dati_prep/: words.json, env_db.npy, kI.json, testi_tutti.json in /tmp/w/b/; orig.json in /tmp/w/asr/; voxasr in /tmp/w/voxasr; *.json di consegna in /tmp/w/cons; immagini_migliorate.tgz estratto in /tmp/w (img2, mapimg).
3. Audio originale: ffmpeg -i video -vn -ac 1 -ar 16000 /tmp/w/orig.wav
4. Voci: scambio/storia-arte-V-lez03/vox/*.wav dal ramo voci-storia-arte-V-lez03 -> /tmp/w/vox
5. python3 lavoro_lez03/render_doc.py (pezzi del prof, ~25 min), poi python3 lavoro_lez03/finale.py 1 e 2.
