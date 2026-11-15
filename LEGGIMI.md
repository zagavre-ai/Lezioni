# Letteratura V · chat R1 · copia di lavoro
Lezione 4 (rifacimento v2): l04/spec.py = 13 approfondimenti (AN01-AN13); render.py li disegna; assemble.py taglia il video consegnato ai confini dei segmenti e li inserisce (AOFF=0.082 per lo scatto del jingle); post.py fa timeline, vtt, scheda, dispensa con mappe, compiti.json.
Mancano solo le voci Kore vera (vox/AN01..AN13.wav): con segnaposto la durata e' 52:09 (misurata), con le voci vere va rimisurata.
bin/asr.py = trascrizione con Gemini a tempi di frase; trasc/ = trascrizioni lezioni 14, 20, 25.
bin/mappa_font_base64.py = mappa.py con font incorporati (con file:// i font non si caricano).

## 15/11 notte
- Lezione 20 (Gadda): montaggio completo con segnaposto (53:03 stimati). Pronta, attende voci Kore (ramo voci-letteratura-V-lez20, 27 voci). Ripresa: bin/ripresa.sh 20, poi bin/chiudi.sh 20.
- Lezione 4: l04/chiudi4.sh dopo le voci AN01-AN13.
- Il controllo del montaggio con segnaposto mostra: bande blu su Quiz/Verifica/Compiti, compiti del prof (4 domande aperte), mappe per argomento + finale anche in dispensa.

## 15/11 sera
- Lezione 20 (Gadda) PRONTA 54:50, lezione 25 (Pasolini) PRONTA 45:19: consegnate. Script in bin/ (ripresa.sh, chiudi.sh, consegna.sh, snapvtt.py per agganciare i sottotitoli all'attacco della voce).
- Lezione 14 (Pirandello): da fare in 2 Parti (taglio prima della produzione teatrale, circa 33:50 del parlato). Struttura del parlato: intro/vita 0-9:30; visione e trappola 9:30-21:50; Il fu Mattia Pascal 22:30-29:30; Uno nessuno 30-33:30; teatro 34-45; novelle 45-47:30; Ciaula 47:40-52:30; Belluca 52:45-60; chiusura 60-64. Testi antologici = pagine di libro come immagini (slide 5-45 del pptx).
