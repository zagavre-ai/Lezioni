# Aggiornamenti per tutte le chat di produzione (leggere a ogni nuova lezione)

## 14/11 sera
- **TRASCRIZIONE (Whisper):** Hugging Face è bloccato (403) e il servizio Gemini ha un tetto di 100 richieste: **non usarlo**. Il modello Whisper «base» (sherpa-onnx int8) è sul ramo `modelli-whisper-base` di questo repository: leggi `LEGGIMI.md` di quel ramo (git fetch, ricomponi il decoder, `pip install sherpa-onnx`).
- **Storia V · compiti del prof (lezioni 1–21):** release `mazzotti-storia-V`, zip `STORIA.V.-20261114T220649Z-1-001.zip`, file «LEZIONE N.pdf». Inseriscili nella scheda «Compiti» e in `compiti.json` della consegna. Per le lezioni già consegnate: aggiungi `compiti.json` sul ramo `consegna-<tag>` (nessuna ricodifica).
- **Storia V · test finali (lezioni 1–21):** zip `STORIA.V-20261114T194325Z-1-001.zip`, file «DOMANDE LEZIONE N.xlsx».
- **Letteratura V · compiti del prof (lezioni 1–26):** release `mazzotti-letteratura-V`, zip `LETTERATURA.ITALIANA.V.-20261114T221058Z-1-001.zip`, file «LEZIONE N.pdf». Stessa cosa: scheda «Compiti» + `compiti.json` (per le già consegnate, solo `compiti.json` sul ramo di consegna).
- **Mappe:** strumento `kit/tools/mappa.py` su main (obbligatorio). Se nella release ci sono mappe del docente, partire da quelle.
- **Velocità:** nessuna anteprima intera, una sola codifica finale 1080p veryfast CRF 19, lavoro a catena (mentre codifica, prepari la lezione dopo).
