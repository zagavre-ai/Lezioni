# RAPPORTO DI REVISIONE · Storia V · «Il Novecento, il secolo delle masse» (2 Parti)
Etichette: **M** misurato · **S** stima/lettura a vista · **NV** non verificato.

## 1. Misure (M)
| | Parte 1 | Parte 2 |
|---|---|---|
| Durata | 57:41.8 (3461.83 s) | 53:01.1 (3181.07 s) |
| Fotogrammi | 103855 = durata×30 | 95432 = durata×30 |
| Peso | 297 MB | 238 MB |
| Volume | −16,2 LUFS, picco −1,3 dBTP | −16,1 LUFS, picco −1,2 dBTP |
| Pause mute > 2,5 s | nessuna | nessuna |
| Jingle Quiz (controllo_jingle) | Q1–Q5 scarto +0,004/+0,005 s | Q6–Q11 +0,005 s |
| Sincronia audio prof vs originale | max 6 ms (15 punti) | max 6 ms (15 punti) |
| Timbre (alti/bassi) vs originale | scarto max 0,7 dB; valori −13,9…−21,1 dB | scarto max 1,3 dB; valori −13,8…−24,8 dB (il punto a −24,8 è tale anche nell'originale) |
| controllo_rapido.py | **ESITO OK** | **ESITO OK** |
Formato 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192k 48 kHz; 4+3 pezzi da 90 MB con .sha256. Il foglio dei fotogrammi di ogni Parte è in `controllo_rapido/`; ho guardato quello della Parte 1 (S) e, in una versione precedente, quello della Parte 2.

## 2. Struttura
Parte 1: sigla, copertina con voce di benvenuto (senza riquadro del prof), introduzione del prof (2 min) con slide degli argomenti, argomenti 1–5 (titolo+jingle, prof, approfondimento, ripasso, quiz; mappa 1 all'argomento 3), glossario, ripasso finale, fine, verifica, sigla finale, intro «Compiti», compiti letti da Kore.
Parte 2: sigla, spiegone della Parte 1 (voce Kore), argomenti 6–11 (mappa 2 all'argomento 7, mappa 3 al 9), poi come la Parte 1. **Scelta mia:** verifica e compiti in fondo a entrambe le Parti (come nella consegna vecchia).

## 3. Tagli del prof (M, dalla trascrizione)
| Pezzo | Inizio (orig., min:s) | Prime parole | Ultime parole | Frase finita |
|---|---|---|---|---|
| D0 | 0:00.0 | «Buongiorno e benvenuti…» | «…, vediamo se tutto è chiaro.» | sì |
| D1 | 2:01.3 | «Allora. Periodo a caval…» | «…innovazioni tecnologiche.» | sì |
| D2 | 18:52.2 | «Senza precedenti. L'en…» | «…. Pensate solo. sul futuro.» | sì |
| D3 | 27:15.8 | «Ma poi non è finita, il…» | «…a robustirsi in questo senso.» | sì |
| D4 | 36:24.4 | «Fenomeno appunto di urban…» | «…tutto prenderà una piega diversa.» | sì |
| D5 | 39:25.1 | «Da parte della Germania almeno…» | «…venivi punito a livello penale.» | sì |
| D6 | 46:35.2 | «Questo era il mondo, quindi dove…» | «…neri e di ingenti capitali.» | sì |
| D7 | 54:36.6 | «ecco appunto le conseguenze…» | «…ià nell'ottocento questo.» | sì |
| D8 | 60:36.4 | «le piazze hanno un impatto…» | «…ye inodor di utopia.» | sì |
| D9 | 67:51.0 | «E poi, come già vi sp…» | «…ta di niente e venne concesso.» | sì |
| D10 | 75:24.5 | «Concludendo, spostiamo…» | «…. Queste spinte culturali.» | sì |
| D11 | 77:30.6 | «È l'applicazione distor…» | «…primo conflitto mondiale.» | sì |
Pezzi continui dall'originale, nessun taglio interno; i cambi cadono in una pausa, 0,15 s prima della frase che segue. Pausa del prof > 2,5 s: nessuna nell'originale, quindi nessun accorciamento. Il pezzo D7 comincia con «ecco appunto le conseguenze della catena di montaggio» (la trascrizione non ha il punto ma c'è una pausa di 1,1 s).

## 4. Mappe (S)
Il prof ha **3 mappe** (non 11): ridisegnate in vettoriale con le sue stesse parole, colori BES e legenda, costruite riquadro per riquadro con la voce Kore, mappa intera ferma 4 s. Le voci CM1–CM11 e CMF1–CMF2 (mappe inventate il 14/11) **non usate**; nessuna mappa finale. La mappa 3 non ha la domanda nel PDF: titolo scritto da me con le sue parole («Quali trasformazioni avvengono nella politica all'inizio del secolo?»). Assegnazione dei colori BES (concetto centrale pesca; parole chiave = riquadri in grassetto del prof; esempi = riquadri semplici; conseguenze = ultimo livello) fatta da me: **da ricontrollare**. Argomenti senza mappa: chiusi con la pillola di ripasso.

## 5. Cose da sapere / non verificato
- **Card del prof (difetto probabile):** scelte in automatico dalla trascrizione del suo parlato (frasi intere, 40 px, max 3 per slide, bordo giallo all'inizio della frase). Il parlato è colloquiale e il riconoscimento sbaglia qualche parola: alcune card sono poco significative o hanno refusi non corretti. Alcune card restano accese 60–80 s (non bloccante). **NV** la lettura card per card.
- Immagini: nessuna immagine nelle schede (il prof non ne ha); approfondimenti solo con testo animato semplice.
- Sigla CGL: spiegata a voce (R8_R2, AN4_R2) e sullo schermo; «Trade Unions» lasciato in inglese. Numeri e anni sullo schermo in cifre, a voce in lettere.
- Le voci Kore sono state trascritte e confrontate: differenze solo di riconoscimento (cifre/lettere, accenti); **non ascoltate a orecchio** (pronuncia di Époque, Rerum Novarum, Deauville, Ellis Island: NV).
- Sottotitoli (.vtt): prof dalla trascrizione con correzioni minime dei termini, voci Kore dai testi; non rivisti riga per riga (NV).
- Dispensa A4 (98 pagine): slide del video senza riquadro e senza evidenziazione, con strato di testo invisibile; copertina con solo materia e titolo. PDF mappe con copertina «MAPPE». Non riaperti a occhio uno per uno (NV).
- Materia scritta «STORIA V» nel piè di pagina; nella scheda «Storia (V)»: da confermare.
- Non fatto: agente separato del §11 (nessun secondo agente a disposizione in questa sessione); i controlli sono stati fatti dalla stessa chat.
- Tempo: oltre le 2 ore e mezza per l'attesa delle 10 voci.
- Rifatti i controlli dopo la correzione delle pause mute sulle mappe (4 s di mappa ferma con suono).
