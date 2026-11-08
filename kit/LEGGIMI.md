# Kit sempre aggiornato (ramo main, cartella kit/)
Al posto degli zip: `cd /home/claude/lezioni && git pull -q origin main && cp kit/tools/*.py tools/`
Prima di iniziare leggi kit/REGOLE.md. Le novità sono in fondo a questo file.

## Novità
- 8/11: tools/stato.py (stato alla master, sostituisce il blocco incollato da Sara); voci_auto.py non cancella mai le voci ricevute.
- 8/11 pomeriggio: tools/controllo_finale.py (TUTTI i controlli in un comando, aggiorna anche lo stato: aggiungi --tag TAG --parte N --voci kore --invia); tools/volume16.py (porta il parlato a -16 LUFS rifacendo solo l'audio, senza ricodificare il video).
- Se `git pull` non funziona (modifiche locali): `git fetch -q origin main && git checkout origin/main -- kit && cp kit/tools/*.py tools/`
