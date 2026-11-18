# RAPPORTO DI REVISIONE · Storia V · Lezione 6 · Il primo dopoguerra (1919-1925) (prof. Giorgio Mazzotti)
Chat «revisione v3» (18/11/2026). Etichette: **misurato** = misura sul file finale; **stima**; **non verificato**.

## 0. Punto di partenza
- Lezione rifatta **da zero** nel modello Spagnolo dal video originale del prof (`LEZIONE 6 ... .mp4`, 1092×614, 39 min 37 s), dalle slide (`LEZIONE 6.pdf`, 11 pagine), dal test e dai compiti. Le voci del 15-16/11 erano di un montaggio vecchio e non sono state riusate: **58 voci Kore nuove** (ramo `voci-storia-V-lez06`), tutte ricevute.
- **Mappe:** per la lezione 6 il prof non ha mappe. Le 8 mappe (una per argomento) sono costruite dalle intestazioni e dal testo delle sue card, senza aggiungere contenuti.
- **Una sola Parte**, 55:07. Otto argomenti, uno per slide di testo del prof (l’argomento 7 ha 3 card, gli altri 4).
- Ordine degli argomenti = ordine del parlato. Nell’argomento 2 il prof parla di Jugoslavia, Polonia, Ungheria, Austria: le card sono evidenziate in quest’ordine.
## 1. Misure sul video nuovo
[misurato] durata 55:07.5 (3307.5 s) | fotogrammi 99226 (attesi 99226) | peso 349.4 MB | 1920x1080 30/1
[misurato] audio aac 48000 Hz, durata audio 3307.53 s (video 3307.53 s)
[misurato] sha256 43cdf25a034faf5f9e58db0d2f39661de77c3503836b753d7e97e9691415bc0b
[misurato] LUFS integrato -16.0 | picco vero -1.4 dBTP
[misurato] LUFS parlato del prof, campione su 4 pezzi: [-16.1, -15.6, -15.3, -15.2]
[misurato] silenzi > 3 s (-55 dB): 0 []
[misurato] fermi del riquadro del prof >= 1 s dentro i pezzi del prof: 0 []
[misurato] jingle quiz 1: atteso 852.800 trovato 852.800 scarto +0.000 OK
[misurato] jingle quiz 2: atteso 1317.533 trovato 1317.533 scarto +0.000 OK
[misurato] jingle quiz 3: atteso 1779.700 trovato 1779.700 scarto +0.000 OK
[misurato] jingle quiz 4: atteso 2023.433 trovato 2023.433 scarto +0.000 OK
[misurato] jingle quiz 5: atteso 2303.767 trovato 2303.767 scarto -0.000 OK
[misurato] jingle quiz 6: atteso 2669.333 trovato 2669.333 scarto +0.000 OK
[misurato] jingle quiz 7: atteso 2863.467 trovato 2863.467 scarto -0.000 OK
[misurato] jingle quiz 8: atteso 3185.300 trovato 3185.300 scarto +0.000 OK

## 2. Confronto con Spagnolo Lez. 1
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
| 10 | Struttura: sigla → copertina → per argomento (titolo, prof, mappa del prof, pillola blu, schema guidato, scheda Quiz) → glossario → riepilogo → finale | OK (8 mappe: tutte costruite dalle sue slide, nessuna del prof). Approfondimenti animati: **non presenti** (non ci sono immagini aggiuntive nei materiali del prof) |
| 11 | PDF A4 orizzontale delle slide (identiche al video, senza riquadro) e delle mappe | OK, uno (una sola Parte) |
| – | Schede blu (titolo, pillola, Quiz, riepilogo) fatte con `schede_spagnolo.py` a scala 1.0 | OK (copia con fotogrammi JPEG per velocità e `--no-sandbox`; stesso disegno) |


## 3. Tabella dei pezzi (presente · minuto · durata misurata)
| pezzo |presente | minuto di inizio | durata misurata (s) |
|---|---|---|---|
| sigla | sì | 0:00.0 | 15.0 |
| cover | sì | 0:14.6 | 26.3 |
| intro | sì | 0:40.5 | 87.4 |
| titolo1 | sì | 2:07.5 | 4.0 |
| prof1 | sì | 2:11.1 | 585.7 |
| mappa1 | sì | 11:56.4 | 85.5 |
| pillola1 | sì | 13:21.4 | 11.7 |
| schema1 | sì | 13:32.7 | 40.0 |
| quiz1 | sì | 14:12.3 | 5.0 |
| titolo2 | sì | 14:16.9 | 4.0 |
| prof2 | sì | 14:20.5 | 369.5 |
| mappa2 | sì | 20:29.6 | 39.3 |
| pillola2 | sì | 21:08.5 | 11.5 |
| schema2 | sì | 21:19.6 | 37.9 |
| quiz2 | sì | 21:57.0 | 5.0 |
| titolo3 | sì | 22:01.6 | 4.0 |
| prof3 | sì | 22:05.2 | 368.9 |
| mappa3 | sì | 28:13.7 | 41.1 |
| pillola3 | sì | 28:54.4 | 10.7 |
| schema3 | sì | 29:04.7 | 34.9 |
| quiz3 | sì | 29:39.2 | 5.0 |
| titolo4 | sì | 29:43.8 | 4.0 |
| prof4 | sì | 29:47.4 | 153.2 |
| mappa4 | sì | 32:20.2 | 38.4 |
| pillola4 | sì | 32:58.2 | 10.6 |
| schema4 | sì | 33:08.3 | 35.0 |
| quiz4 | sì | 33:42.9 | 5.0 |
| titolo5 | sì | 33:47.5 | 4.0 |
| prof5 | sì | 33:51.1 | 189.7 |
| mappa5 | sì | 37:00.5 | 38.6 |
| pillola5 | sì | 37:38.7 | 10.7 |
| schema5 | sì | 37:49.0 | 34.7 |
| quiz5 | sì | 38:23.3 | 5.0 |
| titolo6 | sì | 38:27.9 | 4.0 |
| prof6 | sì | 38:31.5 | 274.1 |
| mappa6 | sì | 43:05.1 | 40.6 |
| pillola6 | sì | 43:45.3 | 11.8 |
| schema6 | sì | 43:56.7 | 32.5 |
| quiz6 | sì | 44:28.8 | 5.0 |
| titolo7 | sì | 44:33.4 | 4.0 |
| prof7 | sì | 44:37.0 | 120.8 |
| mappa7 | sì | 46:37.4 | 30.3 |
| pillola7 | sì | 47:07.3 | 10.5 |
| schema7 | sì | 47:17.4 | 26.0 |
| quiz7 | sì | 47:43.0 | 5.0 |
| titolo8 | sì | 47:47.6 | 4.0 |
| prof8 | sì | 47:51.2 | 227.1 |
| mappa8 | sì | 51:37.8 | 40.5 |
| pillola8 | sì | 52:18.0 | 11.0 |
| schema8 | sì | 52:28.5 | 36.7 |
| quiz8 | sì | 53:04.8 | 5.0 |
| glossario | sì | 53:09.4 | 91.4 |
| riepilogo | sì | 54:40.4 | 22.5 |
| finale | sì | 55:02.5 | 5.0 |

## 4. Immagini e carte del prof mostrate
| immagine | argomento | da | a |
|---|---|---|---|
| Carta/immagini del prof (p. 4) | 1. L'Europa centro-orientale | 7:59 | 11:56 |
| Carta/immagini del prof (p. 4) | 2. Regimi autoritari dell'Est | 14:20 | 14:30 |
| Carta/immagini del prof (p. 4) | 2. Regimi autoritari dell'Est | 18:43 | 20:25 |
| Carta/immagini del prof (p. 9) | 6. Il Medio Oriente e la Turchia | 41:32 | 43:05 |
| Carta/immagini del prof (p. 9) | 7. I movimenti anticoloniali | 44:37 | 45:29 |
Immagini a risoluzione nativa del PDF, ingrandite: morbide (limite del materiale).

## 5. Problemi trovati e correzioni
| tipo | com’era | correzione |
|---|---|---|
| visivo | slide nere/bianche di PowerPoint con webcam 246×138 px | modello Spagnolo: riquadro 4:3, fascia gialla, pannello «PAROLE CHIAVE», card in corso evidenziata dal parlato |
| audio | livello variabile e rumore | catena del kit dall’originale: −16,0 LUFS misurato |
| testo | trascrizione con errori sui nomi («Abrizar», «Balfur», «Pizzucsky», «Rur», «Puc di Monaco», «Goming Ta», «Shankai Shek»…) | ~35 correzioni certe nei sottotitoli |
| audio | pause del prof > 3 s | ridotte a 1,6 s (solo in pausa) |
| struttura | slide in ordine diverso dal parlato | mostrata la slide di ciò di cui si parla |

## 6. DA CONFERMARE COL PROF
- ~0:33:00: nel parlato il prof dà alla Cina la rottura dell’alleanza Guomintang-comunisti nel **1927**, la slide dice **1926**: nel quiz ho seguito la slide. Da confermare.
- ~0:27:00: il prof parla di «grandi scioperi industriali del 1925», la slide dice «scioperi dei minatori del 1926»: nel quiz ho seguito la slide.
- «Rif» in Marocco, «Piłsudski» e «Horthy» corretti nei sottotitoli dal contesto; da riascoltare.

## 7. Cosa NON ho verificato
- Ascolto umano; pronuncia delle voci Kore (le voci **BEN, MAPN2, MAPN6, MAPN7, MAPN8, GL8** sono segnate «DA CONTROLLARE» dalla master); sincronia delle card controllata a campione; frasi del parlato libero nei sottotitoli da riascoltare.
- Il glossario dura 91 s (la scheda tecnica indica 40–70 s): 8 termini; le mappe durano 30–41 s.
- Testa del prof: sorgente piccola, ingrandita 2,2×.

## 8. Come ho verificato
- Trascrizione parola per parola (Parakeet), rilettura integrale; riconoscimento slide mostrata (1 fotogramma/s vs 16 pagine); ffprobe/ebur128/silencedetect/freezedetect/correlazione jingle/sha256 sul file finale.
