# Kit sempre aggiornato (ramo main, cartella kit/)
Al posto degli zip: `cd /home/claude/lezioni && git pull -q origin main && cp kit/tools/*.py tools/`
Prima di iniziare leggi kit/REGOLE.md. Le novità sono in fondo a questo file.

## Novità
- 8/11: tools/stato.py (stato alla master, sostituisce il blocco incollato da Sara); voci_auto.py non cancella mai le voci ricevute.
- 8/11 pomeriggio: tools/controllo_finale.py (TUTTI i controlli in un comando, aggiorna anche lo stato: aggiungi --tag TAG --parte N --voci kore --invia); tools/volume16.py (porta il parlato a -16 LUFS rifacendo solo l'audio, senza ricodificare il video).
- Se `git pull` non funziona (modifiche locali): `git fetch -q origin main && git checkout origin/main -- kit && cp kit/tools/*.py tools/`
- 8/11 sera: scheda_da_timeline.py prende la materia come 6° argomento (prima era fissa «Tecnologie»); tools/testo_youtube.py (testo per YouTube con capitoli). Scheda Quiz: titoli lunghi su 2 righe, non sotto l icona play.
- 8/11 notte: kit/sigle/Sigla_Inglese_15s.mp4 (sigla d Inglese, stessa famiglia di Letteratura; sostituisce il segnaposto).
- 8/11 notte: stato.py e controllo_finale.py accettano --scheda scheda_pubblicazione.json (e la timeline): la master prepara da sola il testo YouTube con i capitoli. Quando una Parte è PRONTA rifai: python3 tools/stato.py <tag> --parte N --scheda <scheda.json> --timeline <timeline.json> --invia
