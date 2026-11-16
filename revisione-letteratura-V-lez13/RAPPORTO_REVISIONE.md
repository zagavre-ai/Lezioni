# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 13 (Svevo) · Prof. Giorgio Mazzotti
Chat di revisione 13 · 16/11/2026 · **Misurato** = ricavato da file/strumenti; **stima** = valutazione mia.

## 0. Stato onesto
- **Corretto:** riquadro del prof 4:3 con fascia gialla, sfondo bianco, piè di pagina «LETTERATURA ITALIANA V», sottotitoli sulla voce narrante, PDF slide A4, PDF mappe, schede.
- **NON corretto (serve una decisione o altro lavoro, vedi §3):** mappe inventate nel video, frasi ripetute della voce, apertura della Parte 2 con il ripasso (voci IN2/RIP già richieste alla master), refusi residui nei sottotitoli del prof, fettine delle pagine del libro tagliate a metà riga, testa del prof tagliata già nell'originale.
- Non ho rifatto il montaggio da zero: mancano i sorgenti (slide HTML, timeline). Ho lavorato sul video già montato con filtri.

## 1. Che cosa ho verificato e come
| Cosa | Come | Esito |
|---|---|---|
| Integrità del montato | ricomposti i pezzi, sha256 | OK (P1 3143,9 s; P2 3200,3 s) |
| Audio, tutta la lezione | trascrizione completa parola per parola (`trascrivi.py`), letta per intero | trovati i problemi #6–#10 |
| Volume del prof | `loudnorm` in sola misura su 170 s | **−16,2 LUFS** (misurato), picco −0,9 dBTP |
| Rumore del prof | livello nelle pause | **−62 dB** nel 5° percentile (misurato): audio già pulito, non l'ho ritoccato. Il modello arnndn del kit **non è nel repository**: non ho potuto riapplicare la catena. Ascolto a 3 punti: **non fatto** (non posso ascoltare) |
| Slide | contact sheet ogni 30 s + OCR di 111 slide (RapidOCR) | nessun refuso reale: le parole segnalate dall'OCR sono artefatti (accenti, spazi) |
| Sincronia slide–prof | confronto a campione dei contact sheet | slide e card evidenziate coerenti nei punti guardati; **non misurata** al secondo su tutta la lezione |
| Sottotitoli | controllo ortografico con dizionario italiano su tutti i cue | vedi #3, #4 |
| Compiti | confronto con `LEZIONE 13.pdf` | 4 esercizi, testo identico |
| Test finale | confronto con `DOMANDE LEZIONE 13.xlsx` | 10 domande, identiche |
| Quiz | lettura | 5 domande per argomento, 1 giusta + 3 sbagliate + spiegazione |
| Riquadro nuovo | allineamento audio con l'originale + riscontro con il vecchio tondo | vedi §4 |

## 2. Problemi trovati e come sono stati trattati
| # | Minuto | Tipo | Com'era | Esito |
|---|---|---|---|---|
| 1 | P1 e P2, pezzi del prof | visivo | prof nel **tondo**, nome nero sotto, niente fascia gialla | **CORRETTO**: riquadro 4:3 con angoli arrotondati, ombra grigia, fascia gialla −3° «Giorgio Mazzotti / PROF. DI LETTERATURA ITALIANA», ritaglio dall'originale allineato sull'audio, correzione immagine del kit (`hqdn3d`, `cas`, contrasto 1,04, saturazione 1,03). **Misura: 372×279 px a x 1468, y 146, non 410×308** (vedi §3-a) |
| 2 | ovunque | testo | piè di pagina «LETTERATURA ITALIANA · Prof. …» senza V | **CORRETTO** nelle schermate chiare (10 intervalli, ridisegnato in DM Mono) e nel PDF slide |
| 3 | P1 0:18–0:56, ripassi R/S, glossario, riepilogo, finale; P2 GL1, RF1, FIN1 | testo | **sottotitoli assenti** sulla voce narrante | **CORRETTO**: .vtt rifatti con i testi esatti delle voci (agganciati parola per parola alla trascrizione; 153 parole su 3162 interpolate). «Schopenauer/Nìce/Dottor Esse/milleottocento…» (scritture fonetiche per la voce) mostrati come «Schopenhauer/Nietzsche/Dottor S./1892…» |
| 4 | P1 e P2, parti del prof | testo | i sottotitoli del prof vengono da un riconoscimento vocale con errori (es. «ritoromandere», «esserse», «verniceatura», «ozzeno», «delinetto») | **PARZIALE**: corretti i nomi e i refusi sicuri (48 parole). **Restano circa 600 parole sospette** elencate con il minuto in `sottotitoli_da_riascoltare.txt`: non le ho cambiate a caso per non alterare il significato. **Va fatto un riascolto o una trascrizione migliore** |
| 5 | P2 0:00 | struttura | la Parte 2 non si apre con il ripasso della Parte 1 | **NON CORRETTO**: voci IN2 e RIP **richieste alla master** (aggiunte a `testi_voci.json` sul ramo voci-letteratura-V-lez13). Inserirle richiede un nuovo montaggio dell'apertura |
| 6 | P1 24:29 e 25:28 | audio | «Chi vince spesso si è solo adattato…» detto due volte | **NON CORRETTO**: la voce è dentro animazioni sincronizzate senza sorgenti |
| 7 | P1 38:42 e 39:36 | audio | «il narratore interviene per giudicare e smascherare» due volte | idem |
| 8 | P1 48:56 e 49:44 | audio | «Zeno interrompe la cura / il dottore pubblica per vendetta» due volte | idem |
| 9 | P1 39:58 | audio | «Il successo con il pubblico però non arriva» fuori contesto | **da verificare** |
| 10 | P2 49:37 | testo | «Il lettore resta con la mano in bocca» | **da verificare** sul testo del prof |
| 11 | animazioni «Mappa concettuale» (6) e `Mappe….pdf` consegnato | contenuto | mappe **nostre** (rami inventati per argomento). La mappa del prof è **una sola**, «ITALO SVEVO» | **PDF CORRETTO**: `Letteratura_Lez13_mappe.pdf` = mappa del prof, contenuto identico, nostra grafica (1 pagina). **Video NON corretto**: aspetto la tua decisione (§3-b) |
| 12 | P1, P2 | grafica | animazioni su fondo blu notte, diverse dal modello Spagnolo | **NON CORRETTO**: non ci sono i sorgenti; le animazioni restano come sono |
| 13 | P1, P2 | grafica | fondo delle slide grigio-azzurro (243,244,249), il modello è **bianco** | **CORRETTO**: sfondo reso bianco su tutto il video e nel PDF |
| 14 | P2 D4 (pagine del libro) | pagine | le «fettine» sono HD e leggibili (rigo ≈ 40 px), ma **alcune tagliano a metà riga** (es. T5, 15:00 circa: la domanda 2 del box laterale è tagliata) e non c'è evidenziazione della fettina in corso | **NON CORRETTO**. Tabella brano/pagina/minuto **non completata**. HD disponibili: `Lez13_ingrandita.zip`, 26 pagine (pp. 464–497) |
| 15 | PDF `Letteratura_Lez13_dispensa.pdf` consegnato | testo | 84 pagine **difettose**: piè di pagina sovrapposto al titolo, niente logo né numero di pagina, non coincide con il video | **CORRETTO**: sostituito da `Letteratura_Lez13_slide.pdf`, 111 pagine A4 orizzontale prese dai fotogrammi del video (senza riquadro né nome, sfondo bianco, piè di pagina corretto). Confronto con i fotogrammi: **per costruzione** (sono i fotogrammi). Una pagina per ogni stato di slide diverso (anche i passaggi progressivi dei ripassi) |
| 16 | scheda_P1/P2.json, testo_youtube | testo | titolo «Italo Svevo · Parte N» | **CORRETTO**: «Letteratura V · Lezione 13 · Italo Svevo · Parte N» + descrizione |
| 17 | P1 e P2, riquadro del prof | visivo | **la testa del prof è tagliata in alto già nell'originale** (la webcam inquadra la fronte al bordo) | **NON correggibile**: è nel video del prof; vale per tutta la lezione |

## 3. Decisioni e scelte da conoscere
a) **Riquadro 372×279 invece di 410×308.** Le card e le pagine del libro del montato arrivano fino a x = 1468; con il riquadro a 410 px (x 1428) copriva il bordo destro delle fettine e tagliava il testo delle domande laterali. Ho scelto di non coprire testo.
b) **Mappe nel video:** togliere le 6 mappe inventate porterebbe la Parte 1 a circa 49 min (sotto i 50). Le ho lasciate. Attendo la tua decisione.
c) **Sottotitoli del prof:** servono un riascolto o la trascrizione fatta dal prof (§2 #4).

## 4. Controlli sui video nuovi
| Controllo | P1 | P2 |
|---|---|---|
| Risoluzione / codec | 1920×1080, x264 veryfast CRF 19, AAC 48 kHz ≈189 kb/s (audio copiato senza ricodifica) | idem |
| Durata (misurata) | 3143,9 s = 52:23,9 | 3200,3 s = 53:20,3 |
| Fotogrammi (misurati) | 94 318 (attesi 94 317: **+1 fotogramma**, 33 ms, invariato nell'ultimo secondo) | 96 010 (attesi 96 010) |
| Peso | 218,1 MB (<400) | 239,1 MB (<400) |
| sha256 dei pezzi | ricomposti e verificati (P1; P2 calcolato alla creazione) | |
| Fotogrammi guardati a vista | cover 100 s, slide 400 s, animazione blu 1400 s | slide libro 900 s, 2000 s |

**Non eseguiti (dichiaro):** `controllo_finale.py` e `controllo_jingle.py` (scatto dei Quiz a 0,0 s); ascolto a 3 punti; misura della sincronia labbra sul nuovo riquadro (il ritaglio è allineato all'audio con gli stessi offset del kit, ma non ho rifatto `verifica_sync`); confronto fotogramma per fotogramma con il modello Spagnolo sui punti 1–11. Stato dei punti (a vista): 
1 sigla → invariata · 2 copertina → **diversa dal modello** (riga «LETTERATURA ITALIANA · QUINTO ANNO», lista a card; non rifatta) · 3 slide → sfondo bianco corretto · 4 piè di pagina → corretto · 5 riquadro 4:3 → **corretto, 372×279** · 6 fascia gialla → corretta (su tutte le schermate col prof) · 7 slide senza prof → invariate · 8 font → invariati, non ricontrollati · 9 finale → invariato, non ricontrollato · 10 struttura → **manca l'apertura Parte 2** · 11 PDF → rifatti.
Piccolo difetto residuo: sotto la fettina del libro a x≈1470–1476, y≈575 resta un minuscolo gradino bianco dove finisce la copertura del vecchio riquadro.

## 5. Consegna
`Letteratura_Lez13_Parte{1,2}_1080p.mp4.parte_00…` + `.sha256` (unire con `cat … > file.mp4`), `.vtt`, `Letteratura_Lez13_slide.pdf`, `Letteratura_Lez13_mappe.pdf`, quiz, test, compiti, schede, testo YouTube, timeline, `sottotitoli_da_riascoltare.txt`. Il `controllo_minuti.jpg` (1 fotogramma ogni 30 s) è incluso se la generazione è finita prima del push.
