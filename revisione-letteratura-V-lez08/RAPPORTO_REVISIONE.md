# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 8 · «Gabriele d'Annunzio» (Prof. Giorgio Mazzotti)
**Versione 1 (prima ora) · 16/11/2026 · stato: IN REVISIONE**

## Cosa ho verificato (e come)
- **Misurato:** video ricomposto dai 4 pezzi, sha256 uguale a quello dichiarato. 1920×1080, 30 fps, 4014,0 s (66:54), 120 420 fotogrammi (= durata × 30), peso 306,6 MB.
- **Misurato:** un fotogramma ogni 2 s (2007 fotogrammi), contact sheet per minuto, guardati: 0:00–1:00, 5:00–6:00, 20:00–21:00, 52:00–53:00, 64:00–67:00. Contact sheet ogni 30 s: `controllo_minuti.jpg`.
- **Misurato:** quiz di argomento letti; `Test_…xlsx` confrontato con `DOMANDE LEZIONE 8.xlsx` della release: 10 domande, **identiche**.
- **Misurato:** compiti del prof (PDF «LEZIONE 8», 4 domande aperte) presenti nella release.
- **NON ho potuto fare:** la trascrizione Whisper di tutto l'audio. Il modello non si scarica (huggingface.co bloccato dalla rete di questa chat). Ho usato il `.vtt` esistente come trascrizione. **Non ho ancora ascoltato** i 3 punti di rumore né misurato i LUFS. Serve il modello Whisper dalla master (`serve_master`).
- **Non ancora fatto:** OCR di tutte le slide, confronto delle slide con la dispensa PDF, controllo a vista dell'allineamento del prof sul parlato.

## Problemi trovati (tabella)
| Minuto | Tipo | Com'è | Correzione prevista |
|---|---|---|---|
| tutta la lezione (es. 0:54–66:20) | visivo | Prof in **tondo** (≈ 100 px) in alto a destra, bordo scuro; sotto solo il testo piccolo «Prof. Giorgio Mazzotti» | Riquadro **4:3 ≈ 410×308** a x≈1428 y≈146, angoli arrotondati, ombra grigia morbida, tutta testa e spalle, dal video originale (release), correzione immagine del kit |
| tutta la lezione | visivo | **Manca la fascia gialla** inclinata con «Giorgio Mazzotti / PROF. DI LETTERATURA ITALIANA» | Aggiungere, sempre visibile dove c'è il prof |
| tutte le slide | visivo | **Manca il logo Telesio** in alto a sinistra (modello Spagnolo: c'è). La riga blu in alto ha un formato diverso dal modello | Rifare le slide col modello (`slide_1080p_esempio.png`) |
| 0:16–0:54 | visivo | Copertina: titolo + elenco argomenti presenti, ma il prof compare solo dopo ~38 s; l'elenco è su una colonna, riga «LETTERATURA ITALIANA · QUINTO ANNO» invece di «… V · VIDEOLEZIONE»; card «ARGOMENTI» da confrontare col modello | Rifare copertina come modello |
| 0:16–0:26 | visivo | Dissolvenza sigla→copertina: da guardare a 30 fps per escludere il lampo | Controllo a vista |
| 64:20–65:40 | visivo | Pillola/riepilogo finale: **onde audio in alto a destra al posto del riquadro**, ok per slide senza prof, ma stile diverso dal modello | Allineare |
| 66:20–66:36 | visivo/struttura | «Verifica finale» e «Fine della lezione» come schede blu, poi finale nero «GRAZIE PER L'ATTENZIONE» | Il finale deve essere `Sigla_finale_5s_con_avviso_diritti.mp4` (controllare che sia quello) |
| 66:42–66:54 | struttura | Scheda **«Compiti» dentro il video** (con «Consegne»), ma i compiti non sono nel video né in `compiti.json`: **manca `compiti.json`** | Creare `compiti.json` dal PDF del prof (4 esercizi, testo identico) |
| consegna | testo | Mancano `…_slide.pdf` (A4 orizzontale, slide identiche al video) e `…_mappe.pdf`. Esiste solo `dispensa.pdf` (46 pag.) | Generare i due PDF |
| consegna | testo | `.vtt` con errori evidenti: «letturatura», «troppo 900», «tard 800», frasi senza senso (es. 1:12) | Rileggere tutto, correggere nomi e frasi, allineare ±0,3 s |
| consegna | pagina | Pagine del libro nel video (es. 52:00–53:00 «La sera fiesolana»): da controllare che siano la «fettina» dallo screen HD. Nella release ci sono 8 screen HD (p239–265) + `Lez08_docente.pdf` | Confronto per brano, tabella brano·pagina·file·minuto nella v2 |
| consegna | mappe | Mappa del prof (`LEZIONE 8.pdf`, 1 pagina, solo immagine): va impaginata con la grafica v3, una per argomento + finale: **il prof ne ha mandata una sola** | Scrivo a Sara: la mappa è una sola; non invento le altre |
| consegna | durata | 66:54: oltre i 60 min della regola del 7/11 e oltre i 65 tollerati dall'8/11 | Da decidere con la master |

## Piano e tempi stimati (da ora)
1. Whisper dalla master → trascrizione e controllo sincronia voce/immagine (30 min).
2. Rifare le slide con il modello Spagnolo, stessi testi (OCR/ricostruzione: 1 h 30).
3. Ritaglio 4:3 + fascia gialla sul parlato del prof dall'originale (1,2 GB), audio con catena del kit, ricodifica con `finale_a_pezzi.py` (1 h 30).
4. `.vtt`, PDF slide + mappe, compiti, scheda (45 min).
5. Controlli finali (30 min). **Totale ≈ 4,5 h** (entro il limite di 5 h per la lezione 8).

## Richieste
- **Master:** modello Whisper `small` (da qui huggingface.co è bloccato); eventuale sorgente delle slide del video (i file con cui sono state generate).
- **Sara:** mappe concettuali: per la lezione 8 il prof ne ha mandata **una sola**.
