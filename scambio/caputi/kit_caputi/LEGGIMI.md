# Kit Caputi · modello approvato «Gonna» (21/11/2026)

## Cosa c'è
- **`modello_gonna/Anteprima_Laboratori_Gonna_nuovo_modello_v2.mp4`**: l'anteprima approvata da Sara (4:47). **Guardala tutta prima di cominciare**: è il livello di qualità richiesto.
- **`modello_gonna/s*.png`**: un fotogramma per scena (copertina, figurino, cartamodello, mappa, quiz).
- **`modello_gonna/scene/`**: i sorgenti delle scene. Riusali come base; si cambiano i contenuti, non lo stile.
  - `base.css`: caratteri, etichetta in alto, riga, piè di pagina, card con alone giallo, legenda.
  - `scena.py`: rende una scena HTML in mp4 con le voci.
    - La scena espone `render(t)` e `setSteps(passi)`.
    - `fai(html, voci, out, lead, gap, coda, pause, trasparente, scatto)` crea il piano dalle durate delle voci, rende i fotogrammi a 30 fps, mixa le voci con dissolvenza di 20–40 ms e scrive `.steps.json`.
    - **Prima di usarlo** cambia `D` (la cartella delle voci: `D/voci/vox/NOME.wav`).
  - `s3_prof.html`: sovrapposizione **trasparente** (qtrle ARGB) sopra il tratto della prof: card che entrano a tempo mentre lei parla. È il modo per mettere grafiche **sopra la sua voce senza tagliarla**.
  - `s4_cartamodello.html`: costruzione vettoriale passo per passo, con card del passaggio a destra e chip delle misure.
  - `s5_mappa.html`: mappa con i colori BES e la legenda, un nodo alla volta.
  - `s6_quiz.html`, `s7_fine.html` («Ora torniamo dalla professoressa…»).
- **Caratteri:** copia `kit/tools/mappa_font/*.ttf` (ramo main) in `/root/.fonts/` (base.css li cerca lì), poi `fc-cache -f`.
- **`esempi_acquerello/`**: lo stile delle illustrazioni. Il figurino della Gonna è il riferimento approvato. La lana e la seta sono prove per Tecnologie lez01.
- **`sigle/`**: `Sigla_Chimica_moda_15s.mp4` e `Sigla_Tecnologie_moda_15s.mp4`.
- **`estrai_da_release.py`**: scarica dalla release **solo** i file che ti servono, anche dagli zip grandi di Chimica. Riprende da dove si è fermato.
  ```
  python3 estrai_da_release.py moda-chimica-III-IV --elenca
  python3 estrai_da_release.py moda-chimica-III-IV "Lezione 3/" /home/claude/lez03
  ```
  Prova del 22/11: un video di 290 MB estratto in 22 secondi.

## Illustrazioni ad acquerello (le fa la master)
Le chat non hanno la chiave. Nel tuo ramo `voci-<tag>` carica `scambio/<tag>/immagini.json`:
```json
[{"nome": "IMG_A2_follatura", "descrizione": "la follatura della lana: ...", "riferimento": "scambio/<tag>/rif/foto_prof_p12.png"}]
```
- `descrizione`: cosa disegnare, in italiano, concreta e fedele a quello che dice la prof (oggetti, processo, ordine da sinistra a destra). Lo stile lo aggiunge la master: acquerello da stilista, soggetto intero con margine, nessuna scritta, carta bianca.
- `riferimento` (facoltativo): un'immagine della prof (pagina del PDF ritagliata, disegno tecnico) da cui partire. Va caricata nello stesso ramo.
- La master risponde in `scambio/<tag>/img/NOME.png` con `ESITI.txt` (OK oppure DA CONTROLLARE). Al massimo 12 immagini per giro, circa 30 s l'una.
- **Le scritte si mettono tu, sopra, in HTML** (testo vero, nitido, parole esatte della prof). Mai chiedere scritte dentro l'acquerello.
- Controlla ogni immagine: soggetto intero, niente di tagliato, corrisponde a quello che dice la prof. Se no, cambia la descrizione e usa un nome nuovo (`..._v2`).
