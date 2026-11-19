# RAPPORTO DI REVISIONE · Storia V · Lezione 4 · La Prima guerra mondiale (prof. Giorgio Mazzotti) — correzioni 19/11/2026
Etichette: **misurato** = misura sul file finale; **piano di montaggio** = ricavato dai pezzi montati; **non verificato** = non controllato.

## 0. Cosa è stato corretto (e cosa no)
- **Difetto principale: slide ferme.** Prima, per ogni argomento c'era una sola slide con 5 card per 8–16 minuti (solo il bordo giallo cambiava). Ora ogni slide del prof cambia **al massimo ogni 150 s**: slide con 2–3 card intere del PDF (mai spezzate, nessun «…», iniziale maiuscola, altezza del testo), in rotazione; le immagini/carte del prof restano come slide a sé e, se durano oltre 150 s, si alternano con «immagine + card». Nessuna slide con una card sola senza immagine.
- **Copertina/introduzione:** il prof parla 216 s sopra la copertina: ora copertina per 100 s e poi slide «Il percorso della lezione» (116 s). I titoli di copertina non sono stati toccati.
- **Mappe:** tutte e 11 **ridisegnate con `kit/tools/mappa.py`** (testo dalle mappe del prof per le 6 che esistono, dalle sue slide per le altre 5), ramo per ramo a tempo con la voce Kore già consegnata; niente più ritaglio dell'immagine del prof.
- **Non toccati (restano quelli della consegna 18/11):** audio (voci Kore, parlato del prof, jingle), titoli, pillole, schemi di ripasso (5 righe), quiz, glossario, riepilogo, sigle, sottotitoli .vtt (la timeline non cambia: tutti i pezzi hanno gli stessi fotogrammi; verificato dagli scatti dei jingle a 0,000 s).
- Metodo: stesso video, stesso audio (copiato senza ricodifica); rifatti solo i pezzi intro / prof / mappe e rimontati in blocchi con dissolvenza 0,4 s. Il resto del video è ricodificato una volta (x264 veryfast CRF 19).

## 1. Slide ferma più lunga di ogni Parte (richiesta del 19/11)
| Parte | slide ferma più lunga | dove | limite |
|---|---|---|---|
| 1 | **2,73 min** (164 s) | argomento 3 (card) | 3 min |
| 2 | **2,50 min** (150 s) | argomenti 4, 5, 7 | 3 min |
| 3 | **2,52 min** (152 s) | argomento 8 (carta p. 18) | 3 min |

Misura: dal piano di montaggio dei pezzi (identità della slide, ignorando il bordo giallo) e controllo a vista sul foglio `controllo_minuti_P1/2/3.jpg` (un fotogramma ogni 30 s). **Non** ho una misura automatica sui pixel del video finale.

## 2. Misure sul video finale (misurato)
### Parte 1
- [misurato] durata 43:48.1 (2628.1 s) | fotogrammi 78842 (attesi 78842) | peso 342.4 MB | 1920x1080 30/1
- [misurato] audio aac 48000 Hz, durata audio 2628.07 s (video 2628.07 s)
- [misurato] sha256 44b7c07b3cf2b432392fbb5cff1fa004653429f7c22ddb967400950f014e3800
- [misurato] LUFS integrato -16.0 | picco vero -1.3 dBTP
- [misurato] LUFS parlato del prof, campione su 4 pezzi: [-16.2, -16.2, -15.6, -16.7]
- [misurato] silenzi > 3 s (-55 dB): 0 []
- [misurato] fermi del riquadro del prof >= 1 s dentro i pezzi del prof: 0 []
- [misurato] jingle quiz 1: atteso 833.967 trovato 833.967 scarto -0.000 OK
- [misurato] jingle quiz 2: atteso 1504.367 trovato 1504.367 scarto -0.000 OK
- [misurato] jingle quiz 3: atteso 2564.967 trovato 2564.967 scarto -0.000 OK
### Parte 2
- [misurato] durata 35:46.3 (2146.3 s) | fotogrammi 64390 (attesi 64390) | peso 289.7 MB | 1920x1080 30/1
- [misurato] audio aac 48000 Hz, durata audio 2146.33 s (video 2146.33 s)
- [misurato] sha256 413d5878184f440517a81e4a8f844b950e587a88553daf467429d3a2414dfdae
- [misurato] LUFS integrato -16.0 | picco vero -1.7 dBTP
- [misurato] LUFS parlato del prof, campione su 3 pezzi: [-16.0, -14.4, -16.1]
- [misurato] silenzi > 3 s (-55 dB): 0 []
- [misurato] fermi del riquadro del prof >= 1 s dentro i pezzi del prof: 0 []
- [misurato] jingle quiz 4: atteso 665.433 trovato 665.433 scarto +0.000 OK
- [misurato] jingle quiz 5: atteso 1539.967 trovato 1539.967 scarto -0.000 OK
- [misurato] jingle quiz 6: atteso 2100.133 trovato 2100.133 scarto +0.000 OK
### Parte 3
- [misurato] durata 44:19.9 (2659.9 s) | fotogrammi 79796 (attesi 79796) | peso 363.9 MB | 1920x1080 30/1
- [misurato] audio aac 48000 Hz, durata audio 2659.87 s (video 2659.87 s)
- [misurato] sha256 890148dde65d0b0089fc25547b15d5da689ef1027b22212dd8694df6810398a8
- [misurato] LUFS integrato -16.0 | picco vero -1.6 dBTP
- [misurato] LUFS parlato del prof, campione su 4 pezzi: [-15.3, -15.7, -15.6, -16.2]
- [misurato] silenzi > 3 s (-55 dB): 0 []
- [misurato] fermi del riquadro del prof >= 1 s dentro i pezzi del prof: 0 []
- [misurato] jingle quiz 7: atteso 875.233 trovato 875.233 scarto +0.000 OK
- [misurato] jingle quiz 8: atteso 1535.233 trovato 1535.233 scarto +0.000 OK
- [misurato] jingle quiz 9: atteso 2012.000 trovato 2012.000 scarto +0.000 OK
- [misurato] jingle quiz 10: atteso 2195.167 trovato 2195.167 scarto -0.000 OK
- [misurato] jingle quiz 11: atteso 2598.267 trovato 2598.267 scarto -0.000 OK

Nota: nella Parte 2 il LUFS del parlato campionato su un pezzo è −14,4 (il resto −16,0/−16,1): è l'audio della consegna 18/11, non modificato.

## 3. Sincronia delle card (10 punti a caso per Parte, con la trascrizione)
La card si accende nell'istante in cui inizia la frase del prof che la riguarda. Sui 30 punti: lo scarto tra accensione e prima parola della frase è tra −0,9 s e 0 s (card accesa fino a 0,9 s prima) nei punti in cui la card cambia. I valori positivi (+2…+11 s) nei campioni sono **cambi di slide con la stessa card già accesa**, non accensioni in ritardo. Tabella completa in `lavoro/correzioni_19-11/sync_campioni.txt`. Limite: la trascrizione automatica ha errori (es. «sburgico»); il testo delle card viene sempre dal PDF del prof, mai dalla trascrizione.

## 4. Da sapere / non verificato
- Le slide del prof hanno solo 5 card per argomento: per rispettare i 3 minuti le stesse card ricompaiono in gruppi diversi (2–3 per slide). Il PDF `*_slide.pdf` riporta tutte le slide mostrate (pagine uguali ai numeri nel video; la pagina 2 non esiste perché la numerazione parte da 1 e 3).
- **Approfondimento animato (40–60 s con voce Kore) per argomento: NON aggiunto.** Servono nuove voci Kore dalla master e non c'erano nella consegna precedente; restano mappa animata (23–33 s) + pillola + schema con voce (38–47 s). Da decidere alla master.
- Parte 2: 35:46 (sotto i 50 min), come già segnalato il 18/11; decide Sara.
- Voce PI10: segnalata «DA CONTROLLARE» dalla master il 18/11, non riascoltata.
- Non verificato: lettura a vista di ogni singola slide; controllati i fotogrammi ogni 30 s e un campione di slide.
- Pesi: 342 / 290 / 364 MB (sotto i 400).
