# RAPPORTO DI REVISIONE · Storia V · Lezione 15 · La decolonizzazione (1945-1975) (prof. Giorgio Mazzotti)
Chat «revisione v3» (18/11/2026). Etichette: **misurato** = misura sul file finale; **stima**; **non verificato**.

## 0. Punto di partenza
- Nessuna consegna precedente (nessun ramo `consegna-storia-V-lez15`): lezione rifatta **da zero** nel modello Spagnolo dal video originale del prof (`LEZIONE 15 LA DECOLONIZZAZIONE (1945-1975).mp4`, 1092×614, 42 min 20 s), dalle slide (`LEZIONE 15.pdf`, 16 pagine), dal test e dai compiti. Le 25 voci del 16/11 erano di un montaggio vecchio e non sono state riusate: **71 voci Kore nuove** (ramo `voci-storia-V-lez15`), tutte ricevute.
- **Mappe:** la mappa del prof per la lezione 15 **non esiste** (come da indice). Le 10 mappe (una per argomento) sono costruite dalle intestazioni e dal testo delle sue card, senza aggiungere contenuti.
- **Una sola Parte**, 60:04 (la regola dell’8/11 ammette fino a circa 65 min in una Parte). Dieci argomenti, uno per slide di testo del prof.
- Ordine degli argomenti = ordine del parlato; «Le premesse» ecc. seguono le slide. Durante «L’Africa subsahariana» il prof torna alle colonie portoghesi (card di «Apartheid», mostrata) e alla carta del Nord Africa (mostrata con l’etichetta dell’argomento 5).

## 1. Misure sul video nuovo
[misurato] durata 60:04.4 (3604.4 s) | fotogrammi 108131 (attesi 108131) | peso 380.0 MB | 1920x1080 30/1
[misurato] audio aac 48000 Hz, durata audio 3604.37 s (video 3604.37 s)
[misurato] sha256 d2e50db53f3ad0d0aca4ee5eff0bf993b70a33aa533fea09c0c6a95a6236dbc6
[misurato] LUFS integrato -16.0 | picco vero -1.2 dBTP
[misurato] LUFS parlato del prof, campione su 4 pezzi: [-15.9, -14.8, -15.1, -14.9]
[misurato] silenzi > 3 s (-55 dB): 0 []
[misurato] fermi del riquadro del prof >= 1 s dentro i pezzi del prof: 0 []
[misurato] jingle quiz 1: atteso 564.000 trovato 564.000 scarto +0.000 OK
[misurato] jingle quiz 2: atteso 842.767 trovato 842.767 scarto -0.000 OK
[misurato] jingle quiz 3: atteso 1125.967 trovato 1125.967 scarto -0.000 OK
[misurato] jingle quiz 4: atteso 1457.067 trovato 1457.067 scarto -0.000 OK
[misurato] jingle quiz 5: atteso 1693.900 trovato 1693.900 scarto +0.000 OK
[misurato] jingle quiz 6: atteso 2125.000 trovato 2125.000 scarto +0.000 OK
[misurato] jingle quiz 7: atteso 2561.100 trovato 2561.100 scarto +0.000 OK
[misurato] jingle quiz 8: atteso 2929.567 trovato 2929.567 scarto -0.000 OK
[misurato] jingle quiz 9: atteso 3236.367 trovato 3236.367 scarto -0.000 OK
[misurato] jingle quiz 10: atteso 3477.933 trovato 3477.933 scarto +0.000 OK

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
| 10 | Struttura: sigla → copertina → per argomento (titolo, prof, mappa del prof, pillola blu, schema guidato, scheda Quiz) → glossario → riepilogo → finale | OK (6 mappe: 10 costruite dalle sue slide (nessuna del prof)). Approfondimenti animati: **non presenti** (non ci sono immagini aggiuntive nei materiali del prof) |
| 11 | PDF A4 orizzontale delle slide (identiche al video, senza riquadro) e delle mappe del prof | OK, uno (una sola Parte) |
| – | Schede blu (titolo, pillola, Quiz, riepilogo) fatte con `schede_spagnolo.py` a scala 1.0 | OK (copia con fotogrammi JPEG per velocità e `--no-sandbox`; stesso disegno) |


## 3. Tabella dei pezzi (presente · minuto · durata misurata)
| pezzo |presente | minuto di inizio | durata misurata (s) |
|---|---|---|---|
| sigla | sì | 0:00.0 | 15.0 |
| cover | sì | 0:14.6 | 22.2 |
| intro | sì | 0:36.4 | 109.0 |
| titolo1 | sì | 2:25.0 | 4.0 |
| prof1 | sì | 2:28.6 | 321.2 |
| mappa1 | sì | 7:49.4 | 45.6 |
| pillola1 | sì | 8:34.6 | 13.1 |
| schema1 | sì | 8:47.2 | 36.7 |
| quiz1 | sì | 9:23.5 | 5.0 |
| titolo2 | sì | 9:28.1 | 4.0 |
| prof2 | sì | 9:31.7 | 187.7 |
| mappa2 | sì | 12:39.0 | 36.9 |
| pillola2 | sì | 13:15.6 | 11.9 |
| schema2 | sì | 13:27.1 | 35.6 |
| quiz2 | sì | 14:02.3 | 5.0 |
| titolo3 | sì | 14:06.9 | 4.0 |
| prof3 | sì | 14:10.5 | 207.9 |
| mappa3 | sì | 17:38.0 | 31.2 |
| pillola3 | sì | 18:08.8 | 9.9 |
| schema3 | sì | 18:18.2 | 27.6 |
| quiz3 | sì | 18:45.5 | 5.0 |
| titolo4 | sì | 18:50.1 | 4.0 |
| prof4 | sì | 18:53.7 | 240.8 |
| mappa4 | sì | 22:54.1 | 37.9 |
| pillola4 | sì | 23:31.6 | 9.8 |
| schema4 | sì | 23:40.9 | 36.0 |
| quiz4 | sì | 24:16.6 | 5.0 |
| titolo5 | sì | 24:21.2 | 4.0 |
| prof5 | sì | 24:24.8 | 147.2 |
| mappa5 | sì | 26:51.6 | 37.9 |
| pillola5 | sì | 27:29.0 | 10.3 |
| schema5 | sì | 27:39.0 | 34.8 |
| quiz5 | sì | 28:13.4 | 5.0 |
| titolo6 | sì | 28:18.0 | 4.0 |
| prof6 | sì | 28:21.6 | 334.2 |
| mappa6 | sì | 33:55.4 | 41.1 |
| pillola6 | sì | 34:36.1 | 10.3 |
| schema6 | sì | 34:46.0 | 38.9 |
| quiz6 | sì | 35:24.5 | 5.0 |
| titolo7 | sì | 35:29.1 | 4.0 |
| prof7 | sì | 35:32.7 | 346.7 |
| mappa7 | sì | 41:19.0 | 38.0 |
| pillola7 | sì | 41:56.6 | 11.0 |
| schema7 | sì | 42:07.2 | 33.8 |
| quiz7 | sì | 42:40.6 | 5.0 |
| titolo8 | sì | 42:45.2 | 4.0 |
| prof8 | sì | 42:48.8 | 274.5 |
| mappa8 | sì | 47:22.9 | 40.6 |
| pillola8 | sì | 48:03.1 | 11.3 |
| schema8 | sì | 48:14.0 | 35.5 |
| quiz8 | sì | 48:49.1 | 5.0 |
| titolo9 | sì | 48:53.7 | 4.0 |
| prof9 | sì | 48:57.3 | 220.4 |
| mappa9 | sì | 52:37.3 | 36.3 |
| pillola9 | sì | 53:13.2 | 11.2 |
| schema9 | sì | 53:24.0 | 32.3 |
| quiz9 | sì | 53:55.9 | 5.0 |
| titolo10 | sì | 54:00.5 | 4.0 |
| prof10 | sì | 54:04.1 | 145.6 |
| mappa10 | sì | 56:29.2 | 43.1 |
| pillola10 | sì | 57:12.0 | 10.2 |
| schema10 | sì | 57:21.7 | 36.1 |
| quiz10 | sì | 57:57.4 | 5.0 |
| glossario | sì | 58:02.0 | 94.5 |
| riepilogo | sì | 59:36.2 | 23.6 |
| finale | sì | 59:59.4 | 5.0 |

## 4. Immagini e carte del prof mostrate
| immagine | argomento | da | a |
|---|---|---|---|
| Carta/immagini: Indocina e Sud-Est asiatico (p. 6) | 4. Asia e Indocina | 22:35 | 22:54 |
| Carta: Africa del Nord (p. 8) | 6. Africa subsahariana | 31:20 | 32:47 |
| Carta: l’Africa coloniale e indipendente (p. 11) | 7. Apartheid e Africa meridionale | 38:25 | 41:19 |
| Carta: Palestina (piano ONU) (p. 13) | 8. Il Medio Oriente e Israele | 46:12 | 47:23 |
| Carta: Palestina (piano ONU) (p. 13) | 9. Nasser e la crisi di Suez | 48:57 | 48:57 |
| Carta: Canale di Suez (p. 15) | 9. Nasser e la crisi di Suez | 52:24 | 52:33 |
Immagini a risoluzione nativa del PDF, ingrandite: morbide (limite del materiale).

## 5. Problemi trovati e correzioni
| tipo | com’era | correzione |
|---|---|---|
| visivo | slide nere/bianche di PowerPoint con webcam 246×138 px | modello Spagnolo: riquadro 4:3, fascia gialla, pannello «PAROLE CHIAVE», card in corso evidenziata dal parlato |
| audio | livello variabile e rumore | catena del kit dall’originale: −16,0 LUFS misurato |
| testo | trascrizione con errori sui nomi («Seylon», «Gana», «Yen Bien plus», «Jaharlal Neru», «Geddafi», «Gamad Hab / Hel nascer»…) | ~30 correzioni certe nei sottotitoli |
| audio | pause del prof > 3 s | ridotte a 1,6 s (solo in pausa) |
| struttura | slide in ordine diverso dal parlato | mostrata la slide di ciò di cui si parla |

## 6. DA CONFERMARE COL PROF
- ~0:30:34: «la Somalia passa sotto i francesi» (trascrizione incerta): dopo il 1947 la Somalia italiana fu in amministrazione fiduciaria italiana; da riascoltare.
- ~0:38:10: «dall’altra parte c’è l’Arabia Saudita» a proposito del Sinai/Suez: probabilmente Israele; da riascoltare.
- «Zaire» e altre date dette a voce coincidono con le slide (1951 Libia, 1956 Marocco e Tunisia, 1962 Algeria, 1960 «anno dell’Africa»).

## 7. Cosa NON ho verificato
- Ascolto umano; pronuncia delle voci Kore (la voce **MAPN4** «Asia e Indocina» è segnata «DA CONTROLLARE» dalla master: 11 parole diverse dal testo); sincronia delle card controllata a campione; frasi del parlato libero nei sottotitoli da riascoltare.
- Il glossario dura 94 s (la scheda tecnica indica 40–70 s): 8 termini; le mappe durano 24–30 s.
- Testa del prof: sorgente piccola, ingrandita 2,2×.

## 8. Come ho verificato
- Trascrizione parola per parola (Parakeet), rilettura integrale; riconoscimento slide mostrata (1 fotogramma/s vs 16 pagine); ffprobe/ebur128/silencedetect/freezedetect/correlazione jingle/sha256 sul file finale.
