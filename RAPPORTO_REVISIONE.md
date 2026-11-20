# RAPPORTO DI REVISIONE · Storia V · Lezione 17 · Le fasi conclusive della Guerra fredda (1969-1991) — correzioni 19/11/2026
Etichette: **misurato** = misura sul file finale; **piano di montaggio** = ricavato dai pezzi montati; **non verificato** = non controllato.

## 0. Cosa è stato corretto (e cosa no)
- **Slide ferme:** prima fino a 15–19 minuti con la stessa schermata. Ora ogni slide cambia **al massimo ogni ~160 s**: 2–3 card intere del PDF per slide (mai spezzate, nessun «…»), in rotazione; le carte del prof restano slide a sé. Nessuna slide con una card sola senza immagine.
- **Copertine P1, P2, P3:** nel ramo di consegna il titolo era ancora su 2 righe e coperto dalla card ARGOMENTI (la correzione della master era solo su Vimeo). Le ho rifatte con **lo stesso titolo «Le fasi conclusive della Guerra fredda» su una riga**, nella stessa posizione (in alto a sinistra), senza tagli e senza sovrapposizioni; invariati avviso diritti e card ARGOMENTI. Anche l'introduzione del prof (165,8 s, sotto i 3 minuti) usa la copertina corretta.
- **Mappe:** tutte e 8 **ridisegnate con `kit/tools/mappa.py`** (3 dalle mappe del prof: Kippur, neoliberismo, Gorbačev; 5 dalle sue slide), ramo per ramo a tempo con la voce Kore già consegnata.
- **Non toccati:** audio (voci Kore, parlato del prof, jingle), titoli, pillole, schemi, quiz, glossario, riepilogo, sigle, sottotitoli .vtt (stessa timeline: stessi fotogrammi di ogni pezzo; scatti dei jingle a 0,000 s).
- Metodo: stesso video e stesso audio (copiato); rifatti solo copertina / intro / pezzi del prof / mappe, rimontati in blocchi con dissolvenza 0,4 s; il resto è ricodificato una volta (x264 veryfast CRF 19). Trascrizione ripetuta con lo stesso programma: i pezzi del prof hanno esattamente gli stessi fotogrammi della consegna.

## 1. Slide ferma più lunga di ogni Parte
| Parte | slide ferma più lunga | dove | limite |
|---|---|---|---|
| 1 | **2,76 min** (166 s) | introduzione sulla copertina (le altre ≤ 2,7 min) | 3 min |
| 2 | **2,68 min** (161 s) | argomento 5 | 3 min |
| 3 | **2,63 min** (158 s) | argomento 7 | 3 min |

Misura dal piano di montaggio (identità della slide, ignorando il bordo giallo) e controllo a vista sul foglio `controllo_minuti_P1/2/3.jpg` (un fotogramma ogni 30 s). Nessuna misura automatica sui pixel del video finale.

## 2. Misure sul video finale (misurato)
### Parte 1
- [misurato] durata 48:55.7 (2935.7 s) | fotogrammi 88071 (attesi 88071) | peso 389.6 MB | 1920x1080 30/1
- [misurato] audio aac 48000 Hz, durata audio 2935.70 s (video 2935.70 s)
- [misurato] sha256 c741b84228ad6af1ddbc530d1139ec64f416d5ac202c9735357b62c9c34cb1d3
- [misurato] LUFS integrato -16.0 | picco vero -2.3 dBTP
- [misurato] LUFS parlato del prof, campione su 4 pezzi: [-15.7, -15.5, -15.5, -15.8]
- [misurato] silenzi > 3 s (-55 dB): 0 []
- [misurato] fermi del riquadro del prof >= 1 s dentro i pezzi del prof: 0 []
- [misurato] jingle quiz 1: atteso 1450.667 trovato 1450.667 scarto -0.000 OK
- [misurato] jingle quiz 2: atteso 2087.000 trovato 2087.000 scarto +0.000 OK
- [misurato] jingle quiz 3: atteso 2885.067 trovato 2885.067 scarto -0.000 OK
### Parte 2
- [misurato] durata 32:00.4 (1920.4 s) | fotogrammi 57611 (attesi 57611) | peso 262.0 MB | 1920x1080 30/1
- [misurato] audio aac 48000 Hz, durata audio 1920.37 s (video 1920.37 s)
- [misurato] sha256 fa9946f49f58520e9125b0bc113b882ad4f6d8cc1f8555c98f0e783abc385d3e
- [misurato] LUFS integrato -16.1 | picco vero -2.5 dBTP
- [misurato] LUFS parlato del prof, campione su 2 pezzi: [-15.6, -15.4]
- [misurato] silenzi > 3 s (-55 dB): 0 []
- [misurato] fermi del riquadro del prof >= 1 s dentro i pezzi del prof: 0 []
- [misurato] jingle quiz 4: atteso 1264.067 trovato 1264.067 scarto -0.000 OK
- [misurato] jingle quiz 5: atteso 1878.300 trovato 1878.300 scarto +0.000 OK
### Parte 3
- [misurato] durata 37:12.5 (2232.5 s) | fotogrammi 66975 (attesi 66975) | peso 312.9 MB | 1920x1080 30/1
- [misurato] audio aac 48000 Hz, durata audio 2232.50 s (video 2232.50 s)
- [misurato] sha256 da8e44d1b3ccbab2cc6ad9eaf5c4b4f914319ed2088d14efa6e7d9bb2bab4bb9
- [misurato] LUFS integrato -16.0 | picco vero -2.9 dBTP
- [misurato] LUFS parlato del prof, campione su 3 pezzi: [-16.2, -15.8, -15.5]
- [misurato] silenzi > 3 s (-55 dB): 0 []
- [misurato] fermi del riquadro del prof >= 1 s dentro i pezzi del prof: 0 []
- [misurato] jingle quiz 6: atteso 555.433 trovato 555.433 scarto +0.000 OK
- [misurato] jingle quiz 7: atteso 1789.500 trovato 1789.500 scarto +0.000 OK
- [misurato] jingle quiz 8: atteso 2178.700 trovato 2178.700 scarto +0.000 OK

## 3. Sincronia delle card (10 punti a caso per Parte)
La card si accende quando inizia la frase del prof che la riguarda: accensioni tra −0,7 s e +0,1 s dall'inizio della frase. I valori positivi più alti (+1,4…+8,1 s) sono cambi di slide con la stessa card già accesa. Tabella in `lavoro/correzioni_19-11/sync_campioni.txt`. Limite: l'abbinamento card↔frase usa parole-guida; in qualche punto la card accesa può essere quella vicina (es. P3 min 33:36). Il testo delle card viene sempre dal PDF del prof.

## 4. Da sapere / non verificato
- Il PDF del prof ha 3–4 card per argomento: per stare nei 3 minuti le stesse card ricompaiono in gruppi diversi (2–3 per slide). I PDF `*_slide.pdf` riportano le slide mostrate (pagine = numeri nel video; la pagina 2 non esiste).
- **Approfondimento animato (40–60 s con voce Kore) per argomento: NON aggiunto** (servono nuove voci dalla master). Restano mappa + pillola + schema con voce.
- Voce SC4_3: segnalata «DA CONTROLLARE» il 19/11, non riascoltata.
- Pesi: 390 / 262 / 313 MB (Parte 1 vicina al limite di 400).
