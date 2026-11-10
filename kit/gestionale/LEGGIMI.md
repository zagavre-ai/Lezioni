# Kit gestionale · controllo settimanale degli alunni (SoluzioneFAD)

Leggi le regole complete nell'avvio della chat gestionale (`AVVIO_chat_gestionale.md`). In breve:

- **parser_xls_browser.js** — `parseXLS(Uint8Array)` legge i .xls della piattaforma, cioè i report BIFF8. Va eseguito nel browser, dentro una scheda della piattaforma (javascript_tool), e restituisce le righe come array di stringhe.
- **parser_xls_node.js** — lo stesso parser per node, per le prove: `node parser_xls_node.js file.xls`.
- **zip_browser_modello.js** — crea uno ZIP non compresso (CRC32) a partire da più file.
- **crea_excel_controllo.py** — genera l'Excel del controllo settimanale con 5 fogli: Riepilogo, Piano, Dettaglio, Compiti caricati, Report genitori. È il modello della prova inviata alla direzione il 10/11/2026.
- **dati_ESEMPIO_struttura.py** — mostra la struttura dei dati che crea_excel legge. Nel repository non vanno MAI dati personali reali degli alunni.

Come generare un report attività (si legge e basta, non si modifica niente):
1. dalla scheda dell'alunno (Utenti → Studenti → alunno) si prendono i link `course/users/<corso>?id_user_course=<ID>`;
2. si fa una POST `/API/userCourse/createReport` con il corpo `id=<ID>` e l'header `X-Requested-With: XMLHttpRequest`;
3. si scarica il file indicato in `params.path` (un .xls) e lo si legge con `parseXLS`.
