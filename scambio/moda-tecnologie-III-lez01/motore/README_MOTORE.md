# Motore di montaggio TEC-A (modello Gonna) · moda-tecnologie-III-lez01

Scritto il 22/11 dalla chat TEC-A. I percorsi nei file sono `/home/user/lav/...` (prod/, tools/, lez01/): ricrea quella struttura (copia `prod/`, `tools/`, `cont/` -> `lez01/cont/`, `dati/*` -> `lez01/`) oppure sostituisci i percorsi con `sed`.

## Preparazione (una volta)
- `pip install playwright sherpa-onnx pymupdf reportlab openpyxl numpy pillow --break-system-packages` (Chromium già in `/opt/pw-browsers/chromium`: il codice lo usa con `executable_path`).
- Caratteri: `cp kit/tools/mappa_font/*.ttf /root/.fonts/ && fc-cache -f` (base.css li cerca lì).
- Jingle: `Telesio_kit_produzione_v1.zip` -> `/home/user/lav/kit/home/claude/v5/snd/*.wav`.
- Trascrizione: `python3 kit/tools/trascrivi.py VIDEO.mp4 lez01/trasc` (modello da GitHub, circa 10 min ogni ora di audio).

## Flusso
1. **Pagine -> minuti**: `tools/pagine.py PDF trasc.json allinea.json` (allineamento monotono pagina/parlato).
2. **Frasi del PDF -> tempi**: `tools/frasi.py` (divide il PDF in frasi intere) + `tools/allinea_parole.py` (`allinea_frasi`: allinea parola per parola dentro la finestra di ogni pagina; salva `frasi_w.json` con `t0` e `cop` = copertura del parlato). Usa solo le frasi con `cop >= 0.2`.
3. **Confini dei pezzi della prof**: a mano in `tools/piani.py` (`PEZZI`): inizio/fine di ogni argomento su un silenzio vero (`silenzi.json`, rilevato con RMS a 10 ms, soglia -33 dB), frase intera, 0,15 s prima della frase che segue. Pause oltre 1,2 s dopo fine frase accorciate a 0,6 s (`intervalli`, `Mappa`).
4. **Audio della prof**: `lez01/pulisci.sh` (highpass 80 Hz, afftdn nr=8, alimiter, loudnorm -16 LUFS a due passate lineari). Timbro con `tools/timbro.py` (originale -9,4 dB, dopo -10,7 dB: nei limiti -9/-20).
5. **Pezzo della prof**: `prod/prof_bg.py K` (card sincronizzate, rende solo gli stati distinti) poi `prod/prof_comp.py K` (tondo misurato: centro 810,438 raggio 30 px sul video 852x480, ingrandito 2x, maschera tonda, colore leggero, voce pulita). Parallelo: `prod/batch2.sh "1 2 3"` e `batch2.sh "10 9 8"`.
6. **Contenuti**: `cont/aNN.py` (mappa BES, ripasso, quiz, approfondimento) + `cont/approf.py` (box e immagine dell'approfondimento).
7. **Voci Kore**: `tools/build_voci.py` + `tools/build_voci2.py` generano `testi_voci.json` (numeri in lettere, controllo cifre); la master risponde in `vox/NOME.wav`.
8. **Scene Kore**: `prod/costruisci.py` (titolo, approfondimento, mappa, ripasso, quiz, glossario, verifica, compiti; sincronia con `tools/sync.py`: trascrive la voce e allinea con difflib i nodi/righe/termini). HTML in `prod/*.html`; protocollo `setData/setSteps/render(t)`; `prod/scene.py` rende solo i fotogrammi distinti.
9. **Parte**: `prod/parte.py N` (ordine delle scene, timeline) + `prod/assembla.py` (dissolvenze 0,4 s, trans.wav, mix audio, una sola codifica x264 CRF 19 + AAC 192k).
10. **Dispensa e mappe**: `prod/dispensa.py` (A4, copertina senza nome, piè materia+pagina, testo invisibile; mappe in PDF a parte).

## Cose da sapere
- Il `-loop 1` della maschera senza `-t` e senza `overlay=shortest=1` fa durare l'uscita all'infinito (già corretto in `prof_comp.py`).
- Il modello di trascrizione si estrae in `/tmp/asr`: non lanciare due `trascrivi.py` finché la prima estrazione non è finita.
- Regole di Sara del 22/11 già applicate: nome docente solo nella fascia gialla; Kore per tutto ciò che creiamo; refusi corretti (`prof_bg.CORREZ`) ed elencati in `info.json` -> `refusi`.
