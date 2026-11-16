# Prof dal tondo al rettangolo (strumenti della master, 16/11/2026)

Sostituisce il prof nel **tondo** con il prof nel **rettangolo 394×218** (angoli arrotondati raggio 14), preso dal **video originale del prof** e allineato sull'audio. Copre il tondo con il colore dello sfondo.

```
python3 rettangolo.py <finale.mp4> <originale.mp4> <timeline.json> <uscita.mp4>
python3 verifica_sync.py <finale.mp4> <uscita.mp4> <cartella_uscita>/pezzi.json   # «minimo» deve essere ≥ 0,75
```
- `timeline.json` della lezione (se non c'è, passa un file inesistente: lo ricava dal video).
- Variabili utili:
  - `GEO=cx,cy,r` se il tondo non viene trovato (es. lezione 2: `GEO=1700,400,150`);
  - `TOLLERA=1` se in qualche punto il «tondo» trovato non è il prof (es. ripasso/glossario finali): quei punti restano come sono.
- Controlli obbligatori dopo: numero di fotogrammi uguale all'originale montato; `verifica_sync.py` ≥ 0,75; guarda 5 fotogrammi (niente bianco intorno, nome sotto leggibile).
- Lascia sempre l'audio così com'è (`-c:a copy`).
