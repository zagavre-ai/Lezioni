# Storia V · Lez. 18 · note sulle card (20/11)

**Stato: card scritte e controllate, lezione NON montata.** Il montaggio non si è potuto fare in questa chat: mancano il video del prof (4274 s), il PDF, le slide/carte estratte e gli strumenti di render (`/tmp/L18`, `schede_spagnolo.py`, font, `prof5.mp4`). Chi monta riparte da `cards_prof18.json`.

## Cosa c'è
- `cards_prof18.py`: dati + controlli. `python3 -I cards_prof18.py` verifica e riscrive `cards_prof18.json` e `CARD_LEZ18.md`.
- `cards_prof18.json`: 40 segmenti da 0 a 4274 s senza buchi: copertina, «Di cosa parliamo», 35 slide con card, 3 immagini. Ogni card ha inizio/fine, titolo, parola chiave (per «PAROLE CHIAVE» a destra) e testo.
- `CARD_LEZ18.md`: lo stesso in forma leggibile, per rivedere i testi.
- Totale 81 card: 2–3 per slide, slide più lunga 163 s (limite 180), ogni card finisce con un punto. Controllato dallo script.

## Tagli e scelte (da confermare)
- **Parte 1** = 0–2129,7 s (intro + argomenti 1-3, 16 slide), **Parte 2** = 2129,7–4274 s (argomenti 4-6, 19 slide). Taglio a fine argomento 3, a inizio frase.
- **Intro**: copertina 0–113 s, poi «Di cosa parliamo» con i 6 argomenti fino a 187,7 s (regola 05:25: dopo ~100 s, a inizio frase).
- **Immagini** (card sola solo con immagine): De Gasperi 848–880,9 · INA-Casa 2926,6–2969,6 · Fanfani e Moro 3815–3833,1 (finestre un po' più larghe di quelle del prof, che mostrava le immagini 6–24 s: coprono tutta la frase che le commenta). Carta del confine orientale 2208–2478 su due slide con 3+2 card; inserto De Gasperi 2238–2246.
- I titoli degli argomenti restano quelli di `cards_specs.json` (anche «Il Centrosinistra (1953-1963)», che copre in realtà gli anni 1958-1964).
- Le card sono scritte dalle sue parole (ripulite dal parlato). Non ci sono voci né dati che il prof non dica.

## Da guardare prima di montare
1. **Errori di parlato corretti nella card**: «Vittorio Emanuele II» (1779 s) → card dice III.
2. **Dato non messo**: «60% delle case distrutte» (≈377 s): il prof stesso dice che le stime sono incerte. Nella card resta solo il 20% delle industrie.
3. **Data del MSI non messa**: il prof dice «dicembre del 48… del 45» (fu dicembre 1946). La card non ha data.
4. **Omessi dalle card, restano nell'audio**: il paragone dell'Uomo Qualunque con il Movimento 5 Stelle (1455–1485 s) e il collegamento MSI → Fratelli d'Italia con nomi di politici attuali (1581–1620 s). La card dice solo «il nucleo di quelle idee confluirà in formazioni successive». Decide Sara se tenerli come card o se serve altro (sono nell'audio del prof: non si taglia).
5. Anche «fondato da un comico» (Uomo Qualunque) non è nella card: il prof lo dice ma il nome è illeggibile nella trascrizione.
6. La trascrizione ha errori di riconoscimento (es. «Cide De Gasperi», «Rodi e il Dodecaneso»): i termini nelle card sono scritti a mano; i sottotitoli finali vanno comunque corretti dal PDF.

## Per montare
- Ogni card è evidenziata (bordo giallo) da `a` a `b`; la slide mostra titolo + 2-3 card + riquadro prof + parole chiave (una per card).
- Il cambio di slide segue `a`/`b` della slide, non più quelli del PDF del prof.
- Resto del piano invariato: `LEGGIMI_PASSAGGIO.md` (6 argomenti, 2 Parti, voci già nel ramo `voci-storia-V-lez18`).
