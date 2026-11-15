# Letteratura V · chat R1 · copia di lavoro
Lezione 4 (rifacimento v2): l04/spec.py = 13 approfondimenti (AN01-AN13); render.py li disegna; assemble.py taglia il video consegnato ai confini dei segmenti e li inserisce (AOFF=0.082 per lo scatto del jingle); post.py fa timeline, vtt, scheda, dispensa con mappe, compiti.json.
Mancano solo le voci Kore vera (vox/AN01..AN13.wav): con segnaposto la durata e' 52:09 (misurata), con le voci vere va rimisurata.
bin/asr.py = trascrizione con Gemini a tempi di frase; trasc/ = trascrizioni lezioni 14, 20, 25.
bin/mappa_font_base64.py = mappa.py con font incorporati (con file:// i font non si caricano).

## 15/11 notte
- Lezione 20 (Gadda): montaggio completo con segnaposto (53:03 stimati). Pronta, attende voci Kore (ramo voci-letteratura-V-lez20, 27 voci). Ripresa: bin/ripresa.sh 20, poi bin/chiudi.sh 20.
- Lezione 4: l04/chiudi4.sh dopo le voci AN01-AN13.
- Il controllo del montaggio con segnaposto mostra: bande blu su Quiz/Verifica/Compiti, compiti del prof (4 domande aperte), mappe per argomento + finale anche in dispensa.
