# Kit sempre aggiornato (ramo main, cartella kit/)
Al posto degli zip: `cd /home/claude/lezioni && git pull -q origin main && cp kit/tools/*.py tools/`
Prima di iniziare leggi kit/REGOLE.md. Le novità sono in fondo a questo file.

## Novità
- 8/11: tools/stato.py (stato alla master, sostituisce il blocco incollato da Sara); voci_auto.py non cancella mai le voci ricevute.
- 8/11 pomeriggio: tools/controllo_finale.py (TUTTI i controlli in un comando, aggiorna anche lo stato: aggiungi --tag TAG --parte N --voci kore --invia); tools/volume16.py (porta il parlato a -16 LUFS rifacendo solo l'audio, senza ricodificare il video).
- Se `git pull` non funziona (modifiche locali): `git fetch -q origin main && git checkout origin/main -- kit && cp kit/tools/*.py tools/`
- 8/11 sera: scheda_da_timeline.py prende la materia come 6° argomento (prima era fissa «Tecnologie»); tools/testo_youtube.py (testo per YouTube con capitoli). Scheda Quiz: titoli lunghi su 2 righe, non sotto l icona play.
- 8/11 notte: kit/sigle/Sigla_Inglese_15s.mp4 (sigla d Inglese, stessa famiglia di Letteratura; sostituisce il segnaposto).
- 18/11: kit/sigle/Sigla_Diritto_15s.mp4 (sigla di Diritto ed economia, stessa famiglia di Storia: linea del tempo 1942 Codice civile → 2002 Euro, titolo, barra gialla, logo; musica della sigla di Storia).
- 18/11: kit/sigle/Sigla_Chimica_moda_15s.mp4 (Chimica applicata e nobilitazione dei materiali per i prodotti della moda, Prof.ssa Caputi; famiglia delle sigle Moda: anello esagonale, TINTURA · STAMPA · FINISSAGGIO, titolo su 3 righe, barra viola, [TECNICO SISTEMA MODA]; musica della sigla Moda).
- 8/11 notte: stato.py e controllo_finale.py accettano --scheda scheda_pubblicazione.json (e la timeline): la master prepara da sola il testo YouTube con i capitoli. Quando una Parte è PRONTA rifai: python3 tools/stato.py <tag> --parte N --scheda <scheda.json> --timeline <timeline.json> --invia
