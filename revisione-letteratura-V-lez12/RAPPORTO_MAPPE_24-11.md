# Lezione 12 · rifacimento delle sole mappe (24/11)

Cambiati solo i 6 tratti delle mappe. Audio Kore, parlato del prof, quiz, compiti, piè di pagina: invariati.

## Cosa è stato fatto
- 6 tratti rifatti: mappa 1 (8:26), 2 (16:38), 3 (26:37), 4 (37:46), 5 (50:25), 6 finale (52:05). Tempi nel video di 55:28.
- Mappa del professore: stesse parole, stessa struttura, stesse 3 frecce (titolo→superamento positivismo; titolo→antieroe; antieroe→spazio e tempo). Mappa unica, costruita ramo per ramo: ogni riquadro (con la sua freccia) compare quando la voce lo nomina, ed è giallo finché la voce ne parla. La mappa 6 ricostruisce tutto da zero.
- Colori BES con legenda in alto a destra: pesca (titolo), paglierino (parole chiave), lilla (conseguenze), menta (autori e opere). Celeste non usato: la mappa non ha date né sequenze, la legenda mostra i 4 colori usati.
- Testo blu notte, 36 px (titolo 42 px), maiuscolo/minuscolo.
- Alla fine di ogni tratto la mappa (fin lì costruita) resta ferma senza giallo: 4,9 s, 4,2 s, 5,0 s, 4,6 s, 5,0 s. Nella mappa 6 resta ferma 9,2 s con la voce che parla.
- I tempi dei rami sono presi dalla trascrizione dell'audio Kore già presente (sherpa-onnx).

## Misure sul video nuovo
- Durata 3328,167 s e 99845 fotogrammi = come prima. 1920×1080, 30 fps, x264 veryfast CRF 19, 309 MB.
- Audio: copiato senza ricodifica, identico all'originale (stesso md5 della traccia). Volume −16,5 LUFS come prima.
- Una sola codifica finale del video (fuori dai tratti nuovi i fotogrammi sono quelli del video precedente, ricodificati una volta).

## Da guardare (importante)
1. **Il video sul ramo non è quello su Vimeo.** I pezzi del ramo durano 3328,17 s; `timeline.json`, `scheda_pubblicazione.json` e `.vtt` (commit 43789de del 18/11, «pillole di ripasso inserite, 14 s blu») sono per 3398,17 s: cioè 5 blocchi di 14 s prima di ogni ripasso, che nei pezzi del ramo non ci sono. Non ho quei blocchi. Per questo ho consegnato **due cose**: (a) il video intero rifatto sul file del ramo (`..._MAPPE_NUOVE`); (b) i 6 tratti da sostituire nel video pubblicato (`tratti/`), ognuno lungo come il tratto originale + 12 fotogrammi di dissolvenza verso la slide successiva. Nel video pubblicato le mappe cominciano a 505,667 s, 1011,933 s, 1625,367 s, 2308,533 s, 3081,333 s, 3195,100 s (durate 60,000 / 63,133 / 56,733 / 49,633 / 50,733 / 64,033 s). Dopo ogni tratto, i primi 12 fotogrammi della scheda di ripasso (o del glossario) sono già nel clip, e sono in dissolvenza dalla nuova mappa: nel video pubblicato, dopo la mappa c'è il blocco blu di 14 s e poi il ripasso, quindi va controllato lì il raccordo. Non ho potuto verificarlo.
2. **Piè di pagina** lasciato com'è, come chiesto: dice «Letteratura italiana V · Prof. Giorgio Mazzotti» (contro CLAUDE.md §2.9, difetto non bloccante).
3. **Refusi corretti nella mappa:** «RECHERCE» → «Recherche». Maiuscole del prof passate a maiuscolo/minuscolo. «Spazio, tempo perdono…» resta senza «e», come nella mappa del prof (la voce dice «spazio e tempo»).
4. Mappe senza il riquadro del prof, a tutta larghezza, come prima.
5. Non toccati: `Letteratura_Lez12_mappe.pdf` (PDF delle mappe, vecchia versione) e le slide PDF. Se vanno allineate, serve un altro passaggio.
6. Non ho potuto ascoltare le voci: la pronuncia di «Recherche» nelle voci Kore resta come prima.
7. Controllo separato (§11) non fatto: guardato solo il foglio dei fotogrammi `foglio_fotogrammi_mappe.jpg`; `controllo_rapido.py` non lanciato.
