# RAPPORTO REVISIONE · Letteratura V · Lezione 17 (PRIMA VERSIONE, 16/11/2026)
Stato: **IN REVISIONE** — verifica parziale, correzione NON ancora fatta.

## Misurato
- Video montato ricomposto dai 3 pezzi: **sha256 corretto**. 1920×1080, 30 fps, **51:37 (3096,97 s)**. Originale del prof: 39:17.
- Materiali scaricati dalla release: originale, `_videodispensa.pptx`, zip HD (8 pagine, p703–p735), mappe (LEZIONE 17.pdf), compiti (LEZIONE 17.pdf), Excel (DOMANDE LEZIONE 17.xlsx).
- Contact sheet visivi guardati: minuti 0–30 circa.

## Problemi trovati
| Minuto | Tipo | Com'era | Correzione prevista |
|---|---|---|---|
| 1:49–1:59 | visivo/audio | Il **prof** dice «ecco la fotografia di Giuseppe Ungaretti in tarda età»; sullo schermo c'è ancora la slide degli argomenti. **Non è la voce narrante**: è il prof, quindi la frase non si taglia. La foto **esiste** nella sua slide 2 (`image1.jpg`, ritaglio della linea del tempo del libro) | Mettere la foto sullo schermo a 1:49 ±3 s |
| tutto il video | visivo | Prof in **tondo** (circa 290 px) con nome «Prof. Giorgio Mazzotti» in testo semplice | 4:3 ≈410×308, ombra grigia, fascia gialla inclinata a due righe (punto 000) |
| tutto il video | visivo | Fondo **grigio-azzurro** (non bianco) | Fondo bianco |
| fine | struttura | Nel video ci sono VF (5 s) e compiti brevi (CMP 5 s): verifica finale (10 domande) e compiti del prof non ci sono davvero | Aggiungere i pezzi fuori dal video / `compiti.json` |
| minuti 11–16 (Veglia, Mattina, Fratelli) | visivo | Fettine HD del libro: da controllare che siano leggibili (rigo ≥ 26–30 px) e a tempo | da verificare |

## NON verificato (motivo)
- **Trascrizione Whisper dell'audio: NON fatta.** Il download del modello (`huggingface.co`) è bloccato dalla rete di questa sessione (403). Ho usato solo il `.vtt` esistente e i testi delle voci: non è un ascolto indipendente.
- Volume/rumore (−16 LUFS, arnndn), silenzi > 3 s: analisi lanciata, risultato non ancora letto.
- Sincronia labbra, OCR di tutte le slide, quiz, mappe, PDF A4: non ancora.

## Cosa serve per correggere
1. **Il generatore delle slide/grafica** (matrice v3, copertina, card, PDF A4): non è nel repository (`kit/` ha solo mappa.py e strumenti di montaggio). Senza di esso non posso rifare le slide col fondo bianco e il piè di pagina. Mi serve il programma o il ramo della lezione con i sorgenti.
2. **Accesso a `huggingface.co`** (o un modello Whisper già scaricato) per la trascrizione.
3. Stima: con 1 e 2 risolti, circa 4–5 ore di lavoro (lezione di 52 min con 8 pagine del libro).

Nota: `kit/tools/stato.py` non funziona qui (cerca `/home/claude/lezioni`): lo stato **non** è stato inviato alla master.
