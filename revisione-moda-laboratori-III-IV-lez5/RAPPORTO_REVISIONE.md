# RAPPORTO DI REVISIONE · Laboratori tecnologici ed esercitazione · Lezione 5 «Industrializzazione» (Prof.ssa Piera Caputi)

Tag: moda-laboratori-III-IV-lez5 · ramo di consegna: revisione-moda-laboratori-III-IV-lez5 · modello: Spagnolo Lez. 1 (nuovo modello), metodo di Lezioni 1-2.
Docente NON contattata: le criticità sono tutte qui sotto.

## Misure (file finali, 1920x1080, 30 fps, H.264 veryfast crf 19, keyint 60, AAC)
| | Parte 1 (argomenti 1-7) | Parte 2 (argomenti 8-11) |
|---|---|---|
| Durata | 50:45,4 (3045,4 s) | 28:27,4 (1707,4 s) |
| Fotogrammi | 91362 = durata x 30 | 51221 = durata x 30 |
| Peso | 275,0 MB | 159,7 MB |
| Volume (EBU R128 integrato) | -16,2 LUFS | -16,2 LUFS |
| Picco (true peak) | -1,6 dBTP | -1,9 dBTP |
| Scatto jingle Quiz | 7 su 7 a +0,003 s | 4 su 4 a +0,003 s |
| Jingle titolo / ripasso | 14 su 14 a +0,003 s | 8 su 8 a +0,003 s |
| Sottotitoli | 736 blocchi, 0 sovrapposti | 411 blocchi, 0 sovrapposti |
| Tondo webcam fermo >= 1 s | solo la copertina (non ha la webcam: falso positivo) | 0 |

Sottotitoli: gli attacchi sono stati portati sui bordi di attacco reali dell'audio finale (310 e 198 blocchi spostati); i blocchi che partono da una pausa attaccano entro 0,3 s al 100% (446 e 241 verificati). Attenzione: questa misura usa lo stesso rilevatore dell'allineamento, non è del tutto indipendente; lo strumento di controllo_finale, su pochi punti verificabili, dà 84% (19 punti) e 80% (15 punti). Riletti circa 28 blocchi a campione: corretti 5 errori del riconoscimento vocale (line/linea, velociare, sull'sagome, dell'sagome); gli altri refusi non individuati possono restare.
Lo strumento controllo_finale dà «NO» alla risoluzione perché è tarato su 2560x1440: il file è 1920x1080 come da regola. Segnala anche molti «fermi immagine» nei pezzi della docente: sono le pagine del PDF ferme mentre lei parla; il tondo con la webcam si muove (misurato solo sul tondo, tondo_freeze.py).

## Voci
Tutte reali, consegnate dalla master (231 file sul ramo voci-moda-laboratori-III-IV-lez5): nessun segnaposto. Le voci MP (mappe) non sono montate: la docente non ha fornito mappe nel materiale (come in Lez. 2). ESITI e le voci dei compiti non usate: nessun compito nel materiale.

## Contenuto e struttura
11 argomenti dal PDF (32 pagine) e dalla lezione (59:00). 166 schede-testo dal PDF allineate col parlato (trascrizione automatica Parakeet), massimo 3 schede per slide. Figure del PDF ridisegnate in SVG con verifica a 4x (scarto mediano sul bordo circa 0,95 px a 4x, 95 percentile 2,3-5 px; vedi diag_svg/misure.json e confronto_cartamodelli/). Tabelle (codici p.5, scheda modello compilata p.23, scheda digitalizzata p.32) ribattute come testo vero. La foto p.32 resta immagine (non vettorializzabile). Webcam: tondo ritagliato dal sorgente a 1080p (la docente è un cerchio di 140 px: risoluzione bassa, sfuocatura leggera).

## Criticità (da leggere, docente non contattata)
1. Il PDF ha il titolo «Indusatrializzazione» (refuso); nel video e nelle schede è «Industrializzazione».
2. La figura di p.21 («Esempio grafico») nel video compare solo per circa 1,5 s: non è stata usata come figura ferma.
3. La docente parafrasa il PDF e non lo legge alla lettera: le schede-testo sono allineate al parlato dal riconoscimento automatico; lo scarto non è misurato su un campione indipendente.
4. Schede non lette dalla docente e quindi saltate: 27, 159, 160, 161, 162. La p.31 ripete contenuti della p.30.
5. Gli errori del riconoscimento vocale (sagome, cucirino, sbieco, ecc.) sono corretti nei sottotitoli con un dizionario; possono restare errori non previsti.
6. Le etichette dentro le figure ridisegnate sono forme, non testo vivo (eccetto le tabelle ribattute). fig20 (modulo): perse le linee tratteggiate e la riga magenta. fig22 (tabella teal) sostituita da tabella ribattuta.
7. Durata: Parte 1 50:45 (nei limiti), Parte 2 28:27 sotto i 50-60 minuti. La lezione contiene solo 11 argomenti (la docente parla 59 min in tutto): non è stato aggiunto riempitivo. Spostando argomenti dalla Parte 1 le parti si equilibrerebbero, ma lo split originale 7+4 è rimasto.
8. Nessun figurino nel materiale; nessun compito.
9. Nelle slide con una scheda la parte bassa dello schermo resta vuota (come nel modello).

## Difetti residui noti
- Sottotitoli non riletti per intero.
- Confronto frame con Spagnolo: confronto_Spagnolo_vs_Lez5.png (sopra il modello, sotto Lez. 5); foglio.png = un fotogramma per tipo di scheda blu con didascalie a pillola (max 2 righe, chip non tagliati).
- Slide A4 di Parte 1/2 e schede di pubblicazione: generate dalla timeline, non riviste a mano.

## Pezzi Parte 1 (nome, inizio s, durata s)
| pezzo | inizio | durata |
|---|---|---|
| SIG | 0.0 | 15.0 |
| COV | 15.0 | 41.6 |
| T1 | 56.6 | 4.0 |
| D1 | 60.6 | 206.0 |
| AN1 | 266.6 | 23.5 |
| P1 | 290.0 | 17.5 |
| SC1 | 307.5 | 43.5 |
| Q1 | 351.0 | 5.0 |
| T2 | 356.0 | 4.0 |
| D2 | 360.0 | 437.7 |
| AN2 | 797.7 | 20.2 |
| P2 | 817.9 | 17.8 |
| SC2 | 835.8 | 46.9 |
| Q2 | 882.6 | 5.0 |
| T3 | 887.6 | 4.0 |
| D3 | 891.6 | 360.3 |
| AN3 | 1252.0 | 20.4 |
| P3 | 1272.4 | 14.7 |
| SC3 | 1287.1 | 40.3 |
| Q3 | 1327.4 | 5.0 |
| T4 | 1332.4 | 4.0 |
| D4 | 1336.4 | 323.9 |
| AN4 | 1660.3 | 20.4 |
| P4 | 1680.7 | 14.6 |
| SC4 | 1695.3 | 49.4 |
| Q4 | 1744.8 | 5.0 |
| T5 | 1749.8 | 4.0 |
| D5 | 1753.8 | 261.7 |
| AN5 | 2015.5 | 20.4 |
| P5 | 2035.9 | 14.1 |
| SC5 | 2050.0 | 41.8 |
| Q5 | 2091.8 | 5.0 |
| T6 | 2096.8 | 4.0 |
| D6 | 2100.8 | 428.8 |
| AN6 | 2529.6 | 19.6 |
| P6 | 2549.2 | 13.7 |
| SC6 | 2562.9 | 44.0 |
| Q6 | 2606.9 | 5.0 |
| T7 | 2611.9 | 4.0 |
| D7 | 2615.9 | 267.3 |
| AN7 | 2883.2 | 20.4 |
| P7 | 2903.6 | 13.5 |
| SC7 | 2917.1 | 44.4 |
| Q7 | 2961.5 | 5.0 |
| GLO | 2966.5 | 37.7 |
| RIE | 3004.1 | 36.3 |
| FIN | 3040.4 | 5.0 |

## Pezzi Parte 2
| pezzo | inizio | durata |
|---|---|---|
| SIG | 0.0 | 15.0 |
| COV | 15.0 | 17.5 |
| RCP | 32.5 | 35.2 |
| T8 | 67.8 | 4.0 |
| D8 | 71.8 | 293.2 |
| AN8 | 365.0 | 18.1 |
| P8 | 383.1 | 14.2 |
| SC8 | 397.4 | 45.7 |
| Q8 | 443.1 | 5.0 |
| T9 | 448.1 | 4.0 |
| D9 | 452.1 | 314.7 |
| AN9 | 766.8 | 21.2 |
| P9 | 787.9 | 14.9 |
| SC9 | 802.9 | 46.3 |
| Q9 | 849.2 | 5.0 |
| T10 | 854.2 | 4.0 |
| D10 | 858.2 | 187.7 |
| AN10 | 1045.8 | 20.9 |
| P10 | 1066.8 | 16.0 |
| SC10 | 1082.7 | 35.5 |
| Q10 | 1118.2 | 5.0 |
| T11 | 1123.2 | 4.0 |
| D11 | 1127.2 | 430.8 |
| AN11 | 1558.0 | 18.9 |
| P11 | 1576.9 | 13.2 |
| SC11 | 1590.1 | 47.0 |
| Q11 | 1637.1 | 5.0 |
| GLO | 1642.1 | 37.3 |
| RIE | 1679.3 | 23.0 |
| FIN | 1702.4 | 5.0 |
