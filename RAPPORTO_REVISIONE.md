# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 7 · PRIMA VERSIONE (16/11/2026)
Stato: **IN REVISIONE**. Verifica A+B+C+D **non ancora finita**: sotto c'è solo ciò che è stato **misurato** finora. Nessuna correzione consegnata.

## Cosa è stato fatto davvero
- Scaricato il video montato (2 pezzi) → ricomposto → **sha256 OK**. Misurato: 1920×1080, 30 fps, **3350,6 s (55:50,6)**, 100 518 fotogrammi (= 3350,6×30), 185 MB.
- Scaricati dalla release: originale `Letteratura_Lez7.mp4` (**1092×614**, 21:19), slide del prof (14 slide), mappa del prof `MAPPE/LEZIONE 7.pdf` (1 pagina). Gli zip «ingrandita» per la lez. 7 non esistono (corretto: la 7 non ha pagine del libro, punto B-bis non applicabile).
- Visti i contact sheet a 1 fotogramma ogni 30 s per i primi ~30 minuti; confronto con `kit/modello_spagnolo/`.
- Trascrizione dell'audio (Whisper small via sherpa-onnx; il sito dei modelli abituali è bloccato nell'ambiente): **in corso**, finora solo i primi 5 min. L'audio quindi **non è ancora verificato**.

## Problemi trovati (misurati)
| # | Minuto | Tipo | Com'è | Correzione prevista |
|---|---|---|---|---|
| 1 | tutto | visivo | **Grafica diversa dal modello Spagnolo (punto 000)**: banda laterale blu notte a destra con il prof e logo (Sara: «niente bande»; il brief dice fondo bianco), prof piccolo senza riquadro 4:3 né ombra, **nessuna fascia gialla** (solo «Prof. Giorgio Mazzotti» in piccolo), nessuna riga «01 · ARGOMENTO» (c'è «ARGOMENTO 1 · …» in piccolo), piè di pagina diverso | rifare tutte le slide nel modello; riquadro 4:3 ≈410×308 a x1428 y146; fascia gialla −3° su due righe |
| 2 | 0:00–0:45 | visivo | Sigla: poi copertina con dissolvenza che mostra **testo sovrapposto** (titolo doppio, ~0:30) e titolo in due stili; la copertina non ha logo in alto a sinistra né card «ARGOMENTI» come Spagnolo | rifare copertina |
| 3 | 3:00–5:30 circa | visivo | Titolo slide sovrapposto in dissolvenza (frame sfocato/«nuvola» al passaggio); animazioni su fondo **blu notte** (schede, linea del tempo, parole chiave, schema di ripasso) invece di fondo bianco | rifare le animazioni su bianco, dissolvenze morbide |
| 4 | 10:30–10:45 e 21:00 | visivo | Mappa concettuale: nodi **diversi da quelli della mappa del prof** (il prof ha: rottura con la tradizione / nuovi temi ideologici / sensazioni nuove e rare / opere e autori fondamentali: Controcorrente-Huysmans, Dorian Gray-Wilde, Deledda). Il video ha «i due pilastri», «la psicologia», «la trama»: **contenuto inventato** | rifare con i nodi del prof, grafica matrice v3 |
| 5 | slide fisse | visivo | Slide con grande vuoto in basso (metà schermo) e scritta «Pagina N» che non corrisponde | impaginare come modello |
| 6 | vtt | testo | Sottotitoli con frasi senza senso: «Giusto perché…», «simbolismo in **giudanale**», «lezione **injustamente isolandola**» (0:46–1:15) | rifare dall'audio e rileggere |
| 7 | file | testo | `compiti.json` nel formato sbagliato (chiave `compiti`, senza `titolo`/`esercizi`/`tipo`) | convertire |
| 8 | file | testo | `scheda_pubblicazione.json`: titolo «Il romanzo nell'Europa e nell'Italia del Decadentismo · Parte 1»; deve essere «Letteratura V · Lezione 7 · Titolo» | correggere |
| 9 | file | testo | `Test_Letteratura_Lez7.xlsx` ha ~38 righe; la verifica finale deve essere di **10 domande** dall'Excel del prof | rifare dall'Excel del prof |
| 10 | file | testo | Dispensa A4 attuale (21 pagine) è la vecchia grafica | rifare identica alle nuove slide |

## Non ancora verificato (lo dico chiaramente)
Ascolto A (sincronia voce/immagini, silenzi, LUFS, rumore), sincronia slide–prof B1 punto per punto, OCR di tutte le slide (C1), quiz (D1), pulizia audio del prof con la catena del kit, lunghezza dei tagli nel prof.

## Punto 000 · confronto con il modello (stato)
1 sigla/dissolvenza: da rifare · 2 copertina: da rifare · 3 slide: da rifare · 4 piè di pagina: da rifare · 5 riquadro 4:3: da rifare dall'originale (**attenzione: l'originale è solo 1092×614**, il riquadro finale è ~410×308: la qualità basta) · 6 fascia gialla: da fare · 7 slide senza prof: da rifare · 8 font: i font del kit (Bricolage, Figtree) ci sono, DM Mono da procurare · 9 finale: da controllare · 10 struttura: presente (sigla, intro, 4 argomenti, ripasso, quiz, glossario, riepilogo, finale) · 11 PDF: da rifare.

## Piano e tempo stimato (stima, non misura)
La lezione va **ricostruita nel modello Spagnolo** (non è una correzione di pezzi): rigenerazione di tutte le slide, animazioni, copertina, mappe del prof, montaggio con riquadro 4:3 e fascia, sottotitoli, PDF. Stima realistica: **6–8 ore**, oltre le 4 previste. Le voci Kore esistenti (ramo `voci-letteratura-V-lez07`) si riusano.
