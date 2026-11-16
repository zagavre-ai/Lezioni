# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 22 (Elsa Morante) · PRIMA VERSIONE (16/11, ora 1 circa)

Stato: **IN REVISIONE**. Non è ancora una consegna: qui c'è il primo esito della verifica e il piano.

## Che cosa ho MISURATO
- Video montato ricomposto dai pezzi: sha256 uguale a quello dichiarato. 1920×1080, H.264/AAC, **51:04 (3064,6 s)**, 91 938 fotogrammi.
- Originale del prof (release): 25:03. Le parti del prof nel montato (D1–D5) ne coprono tutta la durata.
- Fotogrammi ogni 30 s (102) guardati in 6 contact sheet; timeline.json letta (struttura sigla → intro → 5 argomenti → MPF → GL → RF → VF → FIN → SIGF).

## Confronto con il modello Spagnolo (punto 000)
| # | Punto | Esito | Com'è ora |
|---|---|---|---|
| 1 | Sigla 15 s → dissolvenza → copertina | da verificare/rifare | la sigla c'è; la copertina è una slide con titolo «Elsa Morante» + «GLI ARGOMENTI DI OGGI», non nel formato Spagnolo (manca riga «LETTERATURA ITALIANA V · VIDEOLEZIONE» e card ARGOMENTI) |
| 2 | Copertina | **da rifare** | logo piccolo ok, ma riga e card diverse dal modello |
| 3 | Slide su fondo bianco, riga «01 · ARGOMENTO», titolo+barretta, card | **da rifare** | fondo grigio-azzurrino, card con bordo giallo spesso, nessuna tabella con intestazione blu notte |
| 4 | Piè di pagina «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» + «Pagina N» | **da correggere** | c'è «LETTERATURA ITALIANA · PROF. GIORGIO MAZZOTTI» (manca la «V») |
| 5 | Riquadro 4:3 ≈410×308, ombra morbida | **NON conforme** | il prof è in un **tondo** ≈ 75 px a 480 px di larghezza (≈150 px a 1080p), con bordo |
| 6 | Fascia gialla due righe inclinata | **NON conforme** | nome in testo semplice «Prof. Giorgio Mazzotti» + riga piccola, nessuna fascia gialla |
| 7 | Slide senza prof | da rifare | le schede scure (approfondimenti, linea del tempo, parole chiave, schede) sono blu notte, non bianche con parole in giallo |
| 8 | Font | da verificare con OCR | a vista Bricolage/Figtree/DM Mono; il pill «10 domande…» sembra in un monospazio diverso (Courier) |
| 9 | Finale | da verificare | SIGF 5 s presente in timeline |
| 10 | Struttura | presente | sigla, intro, 5 argomenti con AN/AP/MP/R/S/Q, MPF, GL, RF, VF, FIN. Da verificare: il quiz da 5 domande per argomento e «verifica finale» **dentro** il video: le regole la mettono **fuori** dal video |
| 11 | PDF A4 | da rifare | esiste `Letteratura_Lez22_Dispensa.pdf` e `Mappe_letteratura-V-lez22.pdf`, ma non sono la coppia «slide identiche + mappe del prof» |

## Problemi trovati finora
| Minuto | Tipo | Com'era | Correzione prevista |
|---|---|---|---|
| tutto | visivo | prof nel tondo, grafica vecchia (non Spagnolo) | rifare le slide col modello e il riquadro 4:3 dall'originale |
| 0:48–25 ca | visivo | nome senza fascia gialla | fascia gialla 2 righe, −3° |
| ~3:00 e ~4:50 | visivo | (non misurato) schede scure al posto delle slide bianche | rifare in stile modello |
| 49:00 ca | visivo | schermata «VERIFICA FINALE» con bande blu laterali/alto-basso | fondo come Spagnolo, niente bande |
| tutto | visivo | in tutte le slide «Elsa Morante»: titolo e card in italiano corretto; contenuto da rileggere con OCR | OCR completo (vedi sotto) |
| 10:36 e 14:46 ca | visivo | «MAPPA CONCETTUALE» disegnata da noi (es. «La famiglia / La voce narrante → Menzogna e sortilegio») | **vanno sostituite con le mappe del prof** (zip `MAPPE-…` nella release, scaricato) |

## NON ho potuto verificare (e perché)
- **Ascolto (A):** non ho potuto trascrivere l'audio con Whisper: il download del modello è bloccato dal proxy (403 su Hugging Face). Quindi **non ho misurato**: sincronia voce/immagine, parole tagliate, volume, rumore. Serve che la master metta il modello `small` in un punto raggiungibile (es. release o ramo) o faccia lei la trascrizione.
- **OCR (C):** non ancora fatto sull'intero video; solo lettura a vista dei fotogrammi.
- **Sottotitoli `.vtt`:** non ancora riletti.
- **Compiti, Excel, quiz (D):** scaricati (compiti.zip, excel.zip), non ancora controllati.
- **Pagine del libro (B-bis):** la lezione 22 non ne ha (nell'elenco della regola).

## Piano e tempi (stime, non misure)
1. Ritrovare gli strumenti di montaggio del kit (`Telesio_kit_produzione_v3_aggiunta.zip`: `render_slides.py`, `build_blocks.py`, `comp.sh`) e il layout Spagnolo: 1 ora.
2. Rifare slide e riquadro 4:3 (prof dall'originale, allineato col kit `rettangolo/`): 1,5–2 ore.
3. Mappe del prof: 30 min. PDF A4 slide + mappe: 30 min.
4. Verifica A+B+C sul nuovo video: 1 ora.
Totale ≈ 4–5 ore dopo lo sblocco di Whisper. **Se Whisper non è disponibile non posso certificare il punto A** e lo scriverò nel rapporto finale.

## Blocchi da risolvere dalla master
1. Modello Whisper `small` non scaricabile da questa chat (proxy 403).
2. I font Bricolage Grotesque / Figtree / DM Mono non sono installati qui: servono per impaginare le slide.
