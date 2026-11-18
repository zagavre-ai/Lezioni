# RAPPORTO DI REVISIONE · Storia V · Lezione 4 · La Prima guerra mondiale (prof. Giorgio Mazzotti)
Chat «revisione v3» (18/11/2026). Etichette: **misurato** = misura fatta sul file finale; **stima** = calcolo non verificato sul file; **non verificato** = non controllato.

## STATO: NON CONSEGNABILE ANCORA — mancano le voci Kore (87 testi inviati, nessuna voce ricevuta)
- I testi di tutte le voci (benvenuto, mappe, pillole, schemi di ripasso, glossario, riepilogo: **87 voci**) sono nel ramo `voci-storia-V-lez04` (`scambio/storia-V-lez04/testi_voci.json`, push 12:22 e 12:31). **Alle 14:20 il ramo non contiene nessun file `vox/*.wav`**: la master non le ha ancora generate (l'ultima voce generata su un ramo `voci-*` risale al 16/11). Ho chiesto la generazione con `stato.py --serve_master` e a Sara.
- Per non perdere il lavoro ho montato **entrambe le Parti con le voci sostituite da silenzio** della durata stimata (14,7 caratteri/s, misurata su voci Kore della lezione 5). Questi file si chiamano `…_ANTEPRIMA_senza_voci_…` e **non vanno caricati**: servono a controllare grafica, sincronia delle card, schede blu, transizioni, misure di livello e di fermi. Le misure di silenzio (> 3 s) comprendono quindi i tratti in cui la voce Kore dovrà parlare.
- **Quando arrivano le voci** basta rieseguire il montaggio (`lavoro/RIPRESA.md`, circa 40 minuti, tutto già provato): le pillole e il riepilogo sono già disegnati con durate stimate e vengono ridisegnati solo se la voce vera li smentisce (> 1 s); schemi, mappe e glossario si rifanno sui tempi veri.
- **Durata delle Parti:** Parte 1 = 53:46; Parte 2 = 67:24 (stima con voci a 14,7 car/s). **La Parte 2 supera i 60 minuti (di 7)**: la lezione dura 104 min di parlato (+ ~20 min di pezzi di ripasso) e non è divisibile in due Parti da 50–60 min alla fine di un argomento. Alternative: dividere l’argomento 5 (Italia 1915, 13 min) in due argomenti (Parte 1 ≈ 59 min, Parte 2 ≈ 62 min; servirebbero 12 voci nuove), oppure accettare 67 min. **Decide la master/Sara.**
- Peso: Parte 1 ≈ 387 MB, Parte 2 ≈ 506 MB (CRF 23 sui pezzi del prof; 192 kbit/s audio). La Parte 2 supera i 400 MB della regola dell’8/11.


## 0. Punto di partenza
- Per questa lezione **non esisteva nessuna consegna precedente** (nessun ramo `consegna-storia-V-lez04`) **e nessuna voce** (nessun ramo `voci-storia-V-lez04`). Ho quindi costruito la lezione **da zero** nel modello Spagnolo, partendo dal video originale del prof (release `mazzotti-storia-V`, `LEZIONE.4.LA.PRIMA.GUERRA.MONDIALE.mp4`, 1092×614, 104 min 07 s), dalle slide del prof (`LEZIONE 4.pdf`, 24 pagine), dalle sue mappe (`MAPPE LEZIONE 4.pdf`, 6 mappe), dal test (`DOMANDE LEZIONE 4.xlsx`) e dai compiti (`LEZIONE 4.pdf`).
- La lezione dura 104 minuti di parlato: **esce in 2 Parti**. Ho diviso alla fine di un argomento. Parte 1 = presentazione del prof + argomenti 1–4; Parte 2 = argomenti 5–11.
- **Ordine degli argomenti = ordine del parlato.** Il prof parla della «guerra totale» (3619–4093 s) *prima* delle «grandi battaglie» (4094–4849 s) e del «bilancio umano» (5831–5924 s) *prima* dei «trattati di pace» (5925–6246 s), cioè in ordine diverso dalle slide. Il video segue ciò che dice. Gli 11 argomenti sono scelti sui titoli delle slide del prof.

## 1. Misure sul video nuovo
### Parte 1
[misurato] durata 53:46.3 (3226.3 s) | fotogrammi 96760 (attesi 96790) | peso 386.7 MB | 1920x1080 30/1
[misurato] audio aac 48000 Hz, durata audio 3226.33 s (video 3226.33 s)
[misurato] sha256 e665cc72621dcb4019a648d0a2abfe1ede2143c5a066d7d8ca19cf3a1d527ac5
[misurato] LUFS integrato -16.0 | picco vero -1.8 dBTP
[misurato] LUFS parlato del prof, campione su 4 pezzi: [-16.4, -16.9, -15.8, -16.9]
[misurato] silenzi > 3 s (-55 dB): 13 [(15, 22.9), (762, 9.2), (772, 43.7), (1402, 26.7), (1431, 9.0), (1441, 46.2), (2480, 16.5), (2498, 8.3), (2507, 45.7), (3102, 9.1), (3112, 46.6), (3163, 37.9), (3202, 18.4)]
[misurato] fermi del riquadro del prof >= 1 s dentro i pezzi del prof: 0 (un falso allarme di 16,8 s a 2479,7 s: è la mappa 2, senza prof, subito dopo il pezzo del prof)
[misurato] jingle quiz 1: atteso 815.967 trovato 815.967 scarto -0.000 OK
[misurato] jingle quiz 2: atteso 1487.467 trovato 1487.467 scarto -0.000 OK
[misurato] jingle quiz 3: atteso 2553.567 trovato 2553.567 scarto -0.000 OK
[misurato] jingle quiz 4: atteso 3158.667 trovato 3158.667 scarto -0.000 OK

### Parte 2
[misurato] durata 67:25.3 (4045.3 s) | fotogrammi 121329 (attesi 121359) | peso 505.9 MB | 1920x1080 30/1
[misurato] audio aac 48000 Hz, durata audio 4045.30 s (video 4045.30 s)
[misurato] sha256 29d60f505dfde96df8dd54cda0a1b03b55da39bd8a6ffd6127c7b292bf1ecc65
[misurato] LUFS integrato -16.0 | picco vero -1.9 dBTP
[misurato] LUFS parlato del prof, campione su 4 pezzi: [-14.5, -16.4, -15.5, -16.0]
[misurato] silenzi > 3 s (-55 dB): 21 [(15, 24.4), (832, 20.6), (854, 8.6), (864, 47.2), (1395, 8.1), (1404, 44.0), (2214, 8.8), (2223, 44.1), (2857, 23.4), (2883, 8.3), (2892, 39.0), (3338, 23.7), (3364, 8.7), (3373, 41.5), (3519, 8.7), (3528, 47.4), (3903, 21.0), (3926, 8.2), (3935, 44.4), (3982, 36.4), (4019, 20.4)]
[misurato] fermi del riquadro del prof >= 1 s dentro i pezzi del prof: 0 (due falsi allarmi: a 2857,1 s e 3903,2 s iniziano le mappe 4 e 6, senza prof, subito dopo il pezzo del prof)
[misurato] jingle quiz 5: atteso 911.300 trovato 911.300 scarto +0.000 OK
[misurato] jingle quiz 6: atteso 1448.433 trovato 1448.433 scarto +0.000 OK
[misurato] jingle quiz 7: atteso 2267.700 trovato 2267.700 scarto +0.000 OK
[misurato] jingle quiz 8: atteso 2931.167 trovato 2931.167 scarto -0.000 OK
[misurato] jingle quiz 9: atteso 3415.200 trovato 3415.200 scarto +0.000 OK
[misurato] jingle quiz 10: atteso 3576.167 trovato 3576.167 scarto -0.000 OK
[misurato] jingle quiz 11: atteso 3980.100 trovato 3980.100 scarto +0.000 OK

## 2. Confronto con Spagnolo Lez. 1 (punti 1–11 del modello + schede blu)
Confronto punto per punto con `scambio/mazzotti/MODELLO_Spagnolo_*` e con la scheda tecnica (esito: OK / corretto / diverso, con il perché). Controllo a vista sui fotogrammi del video nuovo.

| # | punto del modello | esito |
|---|---|---|
| 1 | Sigla 15 s (`Sigla_Storia_15s.mp4`), avviso diritti negli ultimi 2 s e nei primi 3 s dopo | OK (avviso come nel finale del kit). **Diverso:** la dissolvenza sigla→copertina è di 0,4 s come tutte le altre (la scheda dice 1,0–1,8 s) |
| 2 | Copertina bianca: logo, «STORIA V · VIDEOLEZIONE», titolo, card «ARGOMENTI», voce di benvenuto Kore, riquadro del prof solo mentre parla | OK nella grafica; **voce Kore: vedi stato** |
| 3 | Slide bianche «0N · NOME ARGOMENTO», titolo Bricolage 800, card con bordo giallo sulla frase in corso | OK. **Diverso:** titolo a 50 px (non 64) e testo delle card a 28 px, perché le slide del prof hanno 5 paragrafi di 3 righe; il testo è quello del PDF del prof |
| 4 | Piè «STORIA V · Prof. Giorgio Mazzotti» e «Pagina N» | OK (N = pagina del PDF slide della Parte) |
| 5 | Riquadro 4:3 ~410×308, ombra morbida, correzione immagine del kit | OK (412×310 a x 1428, y 148; hqdn3d 1.5:1.5:3:3, eq 1.04/1.03, cas 0.35). Limite: sorgente 246×138 px, ingrandita 2,2× |
| 6 | Fascia gialla inclinata −3° «Giorgio Mazzotti / PROF. DI STORIA», sempre visibile col prof | OK |
| 7 | Slide senza prof: schema di ripasso, glossario, mappe | OK, fondo bianco, piè con la sola materia |
| 8 | Font Bricolage 800 + Figtree (Bold per etichette), niente DM Mono | OK (nelle slide). La sigla del kit usa un carattere monospazio: è il file del kit, non modificato |
| 9 | Finale 5 s del kit | OK |
| 10 | Struttura: sigla → copertina → per argomento (titolo, prof, mappa del prof, pillola blu, schema guidato, scheda Quiz) → glossario → riepilogo → finale | OK (6 mappe del prof, nessuna per gli altri argomenti: il prof non le ha mandate). Approfondimenti animati: **non presenti** (non ci sono immagini aggiuntive nei materiali del prof) |
| 11 | PDF A4 orizzontale delle slide (identiche al video, senza riquadro) e delle mappe del prof | OK, uno per Parte |
| – | Schede blu (titolo, pillola, Quiz, riepilogo) fatte con `schede_spagnolo.py` a scala 1.0 | OK (copia con fotogrammi JPEG per velocità e `--no-sandbox`; stesso disegno) |

## 3. Tabella dei pezzi (sezione C della scheda tecnica): presente · minuto · durata misurata
### Parte 1
| pezzo |presente | minuto di inizio | durata misurata (s) |
|---|---|---|---|
| sigla | sì | 0:00.0 | 15.0 |
| cover | sì | 0:14.6 | 23.9 |
| intro | sì | 0:38.1 | 216.0 |
| titolo1 | sì | 4:13.8 | 4.0 |
| prof1 | sì | 4:17.4 | 503.0 |
| pillola1 | sì | 12:39.9 | 11.6 |
| schema1 | sì | 12:51.1 | 44.7 |
| quiz1 | sì | 13:35.5 | 5.0 |
| titolo2 | sì | 13:40.1 | 4.0 |
| prof2 | sì | 13:43.7 | 578.5 |
| mappa1 | sì | 23:21.8 | 27.7 |
| pillola2 | sì | 23:49.1 | 11.4 |
| schema2 | sì | 24:00.1 | 47.3 |
| quiz2 | sì | 24:47.0 | 5.0 |
| titolo3 | sì | 24:51.6 | 4.0 |
| prof3 | sì | 24:55.2 | 984.6 |
| mappa2 | sì | 41:19.3 | 17.5 |
| pillola3 | sì | 41:36.4 | 10.7 |
| schema3 | sì | 41:46.8 | 46.7 |
| quiz3 | sì | 42:33.1 | 5.0 |
| titolo4 | sì | 42:37.7 | 4.0 |
| prof4 | sì | 42:41.3 | 539.0 |
| pillola4 | sì | 51:39.8 | 11.5 |
| schema4 | sì | 51:50.9 | 47.7 |
| quiz4 | sì | 52:38.2 | 5.0 |
| glossario | sì | 52:42.8 | 39.0 |
| riepilogo | sì | 53:21.3 | 19.4 |
| finale | sì | 53:40.3 | 5.0 |

### Parte 2
| pezzo |presente | minuto di inizio | durata misurata (s) |
|---|---|---|---|
| sigla | sì | 0:00.0 | 15.0 |
| cover | sì | 0:14.6 | 25.4 |
| titolo5 | sì | 0:39.6 | 4.0 |
| prof5 | sì | 0:43.2 | 788.3 |
| mappa3 | sì | 13:51.1 | 21.6 |
| pillola5 | sì | 14:12.3 | 11.0 |
| schema5 | sì | 14:22.9 | 48.3 |
| quiz5 | sì | 15:10.8 | 5.0 |
| titolo6 | sì | 15:15.4 | 4.0 |
| prof6 | sì | 15:19.0 | 474.7 |
| pillola6 | sì | 23:13.3 | 10.5 |
| schema6 | sì | 23:23.3 | 45.0 |
| quiz6 | sì | 24:07.9 | 5.0 |
| titolo7 | sì | 24:12.5 | 4.0 |
| prof7 | sì | 24:16.1 | 755.9 |
| pillola7 | sì | 36:51.7 | 11.2 |
| schema7 | sì | 37:02.5 | 45.1 |
| quiz7 | sì | 37:47.2 | 5.0 |
| titolo8 | sì | 37:51.8 | 4.0 |
| prof8 | sì | 37:55.4 | 581.7 |
| mappa4 | sì | 47:36.7 | 24.4 |
| pillola8 | sì | 48:00.7 | 10.7 |
| schema8 | sì | 48:11.0 | 40.0 |
| quiz8 | sì | 48:50.7 | 5.0 |
| titolo9 | sì | 48:55.3 | 4.0 |
| prof9 | sì | 48:58.9 | 399.0 |
| mappa5 | sì | 55:37.5 | 24.7 |
| pillola9 | sì | 56:01.8 | 11.1 |
| schema9 | sì | 56:12.5 | 42.6 |
| quiz9 | sì | 56:54.7 | 5.0 |
| titolo10 | sì | 56:59.3 | 4.0 |
| prof10 | sì | 57:02.9 | 94.5 |
| pillola10 | sì | 58:37.0 | 11.1 |
| schema10 | sì | 58:47.7 | 48.4 |
| quiz10 | sì | 59:35.7 | 5.0 |
| titolo11 | sì | 59:40.3 | 4.0 |
| prof11 | sì | 59:43.9 | 319.3 |
| mappa6 | sì | 65:02.8 | 22.0 |
| pillola11 | sì | 65:24.4 | 10.6 |
| schema11 | sì | 65:34.6 | 45.4 |
| quiz11 | sì | 66:19.6 | 1.0 |
| glossario | sì | 66:20.2 | 38.4 |
| riepilogo | sì | 66:58.3 | 21.4 |
| finale | sì | 67:19.3 | 5.0 |

## 4. Immagini e carte del prof mostrate (tabella immagine · Parte · minuto nel video)
Le immagini sono quelle delle slide del prof (`LEZIONE 4.pdf`); compaiono quando il prof le mostra nel suo video (riconosciute confrontando i fotogrammi con le pagine del PDF) e restano finché le commenta. Risoluzione nativa del PDF (circa 800 px di larghezza): **ingrandite, quindi morbide** (limite del materiale).
| immagine | Parte | argomento | da (min:s) | a (min:s) |
|---|---|---|---|---|
| Carta: i Balcani 1911–1913 (p. 4 del PDF) | 1 | 2. Le crisi coloniali e i Balcani | 20:31 | 22:23 |
| Carta: i Balcani 1911–1913 (p. 4 del PDF) | 1 | 2. Le crisi coloniali e i Balcani | 22:48 | 23:15 |
| Carta: fronte occidentale 1914–1916 (p. 8 del PDF) | 1 | 3. 1914: il casus belli | 34:00 | 36:32 |
| Carta: fronte occidentale 1914–1916 (p. 8 del PDF) | 1 | 4. I fronti di guerra e la trincea | 46:24 | 48:07 |
| Carta: fronte orientale e balcanico 1914 (p. 9 del PDF) | 1 | 4. I fronti di guerra e la trincea | 48:07 | 51:40 |
| Vignetta «Sport… bellico 1914» (l’Italia contesa) (p. 11 del PDF) | 2 | 5. 1915: l'Italia in guerra | 12:59 | 13:51 |
| Carta: fronte italiano 1915–1916 (p. 13 del PDF) | 2 | 7. Le battaglie di logoramento | 35:41 | 36:14 |
| Carta: fronte occidentale/orientale 1916 (p. 14 del PDF) | 2 | 7. Le battaglie di logoramento | 36:14 | 36:31 |
| Carta: fronte mediorientale 1915–1916 (p. 16 del PDF) | 2 | 7. Le battaglie di logoramento | 36:34 | 36:52 |
| Carta: fronte italiano 1917 (Caporetto) (p. 18 del PDF) | 2 | 8. 1917: crisi e svolta | 45:05 | 47:37 |
| Grafico: perdite militari per Paese (p. 24 del PDF) | 2 | 10. Il bilancio del conflitto | 57:17 | 58:37 |
| Carta: l’Europa dopo la guerra (1920) (p. 21 del PDF) | 2 | 11. I trattati di pace | 63:13 | 65:03 |

Le pagine 6 (foto dell’attentato) e 22–23 del PDF non vengono mostrate dal prof nel suo video: nel video nuovo non compaiono.

## 5. Problemi trovati e correzioni (minuto = nel video originale del prof)
| minuto (orig.) | tipo | com’era | correzione |
|---|---|---|---|
| 0:00–3:36 | visivo | titolo e presentazione su slide nera di PowerPoint, senza elenco degli argomenti | copertina nel modello (logo, «STORIA V · VIDEOLEZIONE», card «ARGOMENTI») col prof nel riquadro 4:3 |
| tutto | visivo | prof in un riquadro 246×138 px nell’angolo, con logo del Centro e slide senza grafica del modello | ritaglio 4:3 centrato sul volto, ingrandito a 412×310 px con correzione immagine del kit, fascia gialla col nome, pannello «PAROLE CHIAVE» |
| tutto | visivo | slide del prof lunghe (5 paragrafi di 3–4 righe) senza evidenziazione | slide rifatte dal testo del PDF, card della frase in corso evidenziata (da parole-guida del parlato, controllo a campione ±1,5 s) |
| 1:00:19–1:04:40 e 1:15:10–1:17:50 | visivo | il prof parla di un argomento mentre la slide mostrata è quella di un altro (es. «guerra totale» a slide delle battaglie; genocidio degli armeni a slide «guerra totale») | il video mostra la slide dell’argomento di cui si parla; durante l’inciso sul genocidio degli armeni compare la slide «La guerra totale» |
| 0:08:34, 0:08:48, 0:18:29, 0:30:33, 1:43:21 | audio | 5 pause del prof > 3 s (3,1–4,1 s) | ridotte a 1,6 s (tagli solo in pausa, mai dentro una frase) |
| tutto | audio | parlato a livello variabile, rumore di fondo | catena del kit: `aresample 48000, highpass 80, arnndn (sh.rnnn), loudnorm −16, alimiter` dall’originale |
| sottotitoli | testo | trascrizione automatica con errori sui nomi (es. «Salievo», «Tirpiz», «Asazia e Lorena», «millovecentotto», «la cina» per «la cartina») | corretti ~100 errori certi su nomi e date (elenco in `corr.py`); il parlato non è stato riscritto |

## 6. DA CONFERMARE COL PROF
- 1:35:28 circa: «l’imperatore **Carlo II**» → l’ultimo imperatore d’Austria-Ungheria è Carlo **I** (IV d’Ungheria). Nel sottotitolo ho lasciato quello che dice il prof.
- 1:43:06 circa: riparazioni «**132 mila miliardi** di marchi oro» → la cifra corretta è 132 **miliardi**. Lasciato come detto.
- 0:59:41 circa: «Vittorio Emanuele **II**» detto/trascritto per il sovrano del 1915 (è Vittorio Emanuele **III**): nel sottotitolo corretto in III.
- 1:35:37 circa: le slide e la mappa danno «armistizio (4 novembre 1918)»; il prof dice «firmato il 3 novembre, in vigore il 4»: coerente, nessuna correzione.
- 1:15:43 circa, Lusitania: il prof dice «oltre 100 cittadini statunitensi», la cifra storica è 128: lasciato come detto.

## 7. Cosa NON ho verificato
- **Ascolto umano:** nessun passaggio è stato riascoltato da una persona; le misure di tempi e livelli sono automatiche.
- **Sincronia delle card:** la card in corso è scelta da parole-guida nel parlato; controllata a campione su 6 punti, non su tutta la lezione. Dove il prof parla di argomenti non presenti sulla slide la card resta quella dell’ultimo punto trattato.
- **Voci Kore:** pronuncia di nomi e termini (Tirpitz, Schlieffen, Sarajevo, Versailles…) da ascoltare.
- **Testa del prof:** nell’originale la webcam è 246×138 px: ingrandita ~2,2× resta morbida; quando il prof si china in avanti la testa tocca il bordo alto del riquadro (limite dell’originale, non risolvibile).
- **Sottotitoli:** corretti nomi, date e termini certi; ci sono ancora frasi spezzate del parlato libero del prof («Sclamo pure…», «gli schiamenti») che richiedono un riascolto.
- **Quiz e verifica:** domande dal materiale del prof (slide, mappe); la verifica finale è l’Excel del prof, non modificato.

## 8. Come ho verificato
- Trascrizione completa con tempi parola per parola (`kit/tools/trascrivi.py`, Parakeet TDT, 1026 segmenti) e rilettura integrale del testo.
- Riconoscimento della slide mostrata dal prof: confronto di 1 fotogramma/s con le 24 pagine del PDF (distanza media su miniature 160×118); verifica a vista su 29 fotogrammi.
- Misure sul video finale: ffprobe (durata, fotogrammi), ffmpeg `ebur128` (LUFS, picco), `silencedetect`, `freezedetect` sul riquadro del prof, correlazione dei jingle Quiz, sha256.

