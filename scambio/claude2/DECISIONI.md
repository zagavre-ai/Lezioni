# DECISIONI · CLAUDE 2 · MASTER
- 10/11/2026 · Le 14 lezioni già PRONTE senza la chiusura nuova non si rimontano: una sola chat «PRODUZIONE · CHIUSURE» aggiunge in coda Verifica 5 s → sigla → intro Compiti 3,5 s → Compiti 5 s, codificando solo la coda e unendo senza ricodificare il resto. Scrive t_verifica/t_compiti nello stato.
- 10/11/2026 · Peso: vale il limite di stato.py (419 MB decimali = 400 MiB). Inglese lez02 (404 MB) e Psicologia lez03 (405,6 MB) sono dentro.
- 10/11/2026 · Ordine ondate: 1) CHIUSURE + Letteratura lez03; 2) Ideazione lez01 + Storia III; 3) Storia V, Inglese lez03 (appena c'è il video), le altre.
- 10/11/2026 23:00 · Annullata la chat «CHIUSURE»: le 14 PRONTE non si ricodificano, verifica e compiti dalla pagina (nota master 1 22:40).
- 10/11/2026 23:00 · Stanotte 4 agenti sulla macchina Claude 2 (4 CPU): psicologia lez01, lez02, letteratura lez03, ideazione lez01. Codifica 1440p in fila (una alla volta, lock). Misurato: trascrizione ~5× tempo reale, codifica stimata 1–1,5 h per lezione.
- 10/11/2026 23:00 · Voci: si riusano SOLO le Kore già generate. Testi nuovi → testi_voci_NUOVI.json con segnaposto, approvazione di Sara domattina, poi una sola richiesta per lezione.
- 10/11/2026 23:00 · alb-alimentazione lez01 (58,7 min docente): UNA Parte (regola 8/11, fino a ~65 min), inserti compatti, nessun riempitivo.
- 11/11/2026 sera · ORDINE DI SARA: un solo agente alla volta, modello Sonnet, una lezione per volta fino a PRONTA, salvataggio su GitHub dopo ogni lezione. Ordine: 1) storia-arte-V-lez01 (voci Kore arrivate, sessione «Lezioni storia dell'arte V anno», solo lez01); 2) psicologia-I-II-lez01; 3) psicologia-I-II-lez02. Agenti locali (Letteratura, Ideazione) e sessioni Psicologia fermi: non riprendere finché non tocca a loro. Motivo: il limite di utilizzo scatta con più agenti in parallelo.
- 11/11/2026 sera · Voci: il servizio della master 1 è ripartito (11/11 16:00) e genera da solo da testi_voci.json nei rami voci-<tag>.
