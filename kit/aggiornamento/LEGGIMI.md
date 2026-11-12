# Aggiornamento del mattino (registro + report)

Script senza dati personali. I dati stanno solo nel container di lavoro (/root/report_privato), mai qui.

1. Piattaforma (Chrome di Sara, sola lettura, 1 richiesta ogni 3 s): report `createReport` dei corsi attivi, salvati man mano in IndexedDB `claude_rep` del dominio della piattaforma; registri `getLiveRegistry` delle lezioni con «Registro elettronico: Compilato».
2. Dati portati nel container con link firmati del cassetto «quaderno».
3. `python3 crea_report.py` (report Excel), `python3 analisi_ott.py`, `python3 genera_attivita.py` (attivita_registro.json).
4. Cifratura per alunno nella scheda «Registro compiti · Coordinamento» (elenco `L` già aperto con il codice di Sara): file `attivita/<sha('attivita|'+codice)[:16]>.enc`, chiave `sha256('telesio-attivita|'+codice)`, AES-GCM. I codici non escono dal browser.
5. Commit dei file cifrati su gh-pages `registro-compiti/attivita/`.
