# Kit v4 (7/11/2026) · UN SOLO VIDEO PER PUNTATA

Regola: ogni puntata si codifica UNA volta sola, direttamente nel file da caricare su YouTube.
Niente più «master» pesante + «copia leggera»: dimezza il lavoro della macchina.

- tools/finale_a_pezzi.py lista.txt uscita.mp4
  Codifica finale del montaggio a gruppi di ~8 minuti (riprende da dove si è fermata se il lavoro viene interrotto).
  Video 2560×1440, x264 preset fast, CRF 20 (variabile CRF), maxrate 16M; audio AAC 192k 48 kHz codificato tutto insieme.
  lista.txt = la lista concat dei pezzi del montaggio (file '…' per riga). Controllo finale: fotogrammi.
  Per un montaggio a un'altra risoluzione cambiare lo scale nella riga di ffmpeg.
- tools/copia_yt.py master.mp4 uscita.mp4 CRF [maxrate]
  Solo per video GIÀ fatti con il master pesante: ne ricava il video da caricare a pezzi da 10 minuti.

Limiti da sapere:
- invio dei file a Sara: massimo 400 MB → il video finale deve stare sotto (se supera, CRF 21 o 22);
- un lavoro in background viene fermato dopo 2 ore → sempre lavori che riprendono da dove erano arrivati;
- la macchina ha 2 processori: un lavoro pesante alla volta.
