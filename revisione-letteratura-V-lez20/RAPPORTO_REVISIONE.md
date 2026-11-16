# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 20 · Gadda · PRIMA VERSIONE (16/11/2026)
Stato: **IN REVISIONE** — verifica fatta in gran parte; **correzione NON ancora fatta**. Piano e blocchi in fondo.

## Cosa ho verificato e come (M = misurato, S = stima/visione)
- M: video ricomposto dai 2 pezzi, sha256 identico; 54:50,4 (3290,4 s), 1920×1080.
- M: 110 fotogrammi di controllo (1 ogni 30 s, `controllo_minuti_1-4.jpg`) guardati tutti + fotogrammi singoli a pieno formato.
- M: silenzi > 3 s (silencedetect −45 dB); confronto durata originale del prof / pezzi D.
- M: confronto compiti, test, mappa del prof con quelli consegnati.
- S: lettura del `.vtt` (350 blocchi).
- **NON verificato:** ascolto/trascrizione Whisper (il modello non si scarica: `huggingface.co` è bloccato dalla rete della chat; `pip`/`apt` per OCR e Whisper non disponibili). Quindi niente controllo parola per parola voce↔immagine né rifacimento dei sottotitoli. Anche niente OCR automatico: ho letto le slide a vista.
- Il video originale del prof è 1092×614, 25:36 (1536 s): è una registrazione di PowerPoint con il prof in un riquadro piccolo (≈245×140 px) in basso a destra. **Slide del prof (`_videodispensa.pptx`) per la lezione 20: NON sono nella release** (ci sono solo 1–17 e 26).
- Pagine del libro: la lezione 20 non ne ha (B-bis non si applica).

## Confronto con il modello Spagnolo (punto 000)
| # | Punto | Esito |
|---|---|---|
|1|Sigla → dissolvenza → copertina|Sigla nera 16 s «ANALISI TESTUALE» (da confrontare con `kit/sigle/Sigla_Letteratura_15s.mp4`), poi copertina scura: **da rifare**|
|2|Copertina (logo, riga DM Mono, titolo, card ARGOMENTI)|**NO**: fondo blu scuro, nessun «LETTERATURA ITALIANA V · VIDEOLEZIONE»; la card elenca **solo 3 argomenti su 6**|
|3|Slide fondo bianco, «01 · NOME», titolo+barretta blu|**NO**: fondo grigio, etichetta «ARGOMENTO 1 · LA VITA» (modello «01 · LA VITA»), barretta gialla, card diverse|
|4|Piè di pagina «LETTERATURA ITALIANA V · Prof. …» + «Pagina N» a destra|**NO**: manca la «V», «Pagina N» attaccato a sinistra|
|5|Riquadro 4:3 ≈410×308, ombra morbida, niente bordo blu|**NO**: rettangolo 16:9 ≈396×221 con **bordo blu**|
|6|Fascia gialla inclinata con 2 righe|**NO**: nome bianco su banda blu, nessuna fascia|
|7|Slide senza prof, testo grande|**NO**: approfondimenti, ripassi, glossario, riepilogo, compiti sono su fondo blu scuro|
|8|Font|Bricolage/Figtree/DM Mono: probabilmente OK (a vista)|
|9|Finale 5 s col kit|Da verificare: dopo i compiti (≈54:44) non vedo la sigla finale nera con avviso diritti|
|10|Struttura|Presenti: sigla, presentazione, 6 argomenti con approfondimenti, ripasso, quiz, glossario, riepilogo, verifica, compiti. Da controllare: ordine e finale|
|11|PDF A4|Dispensa 11 pag. e Mappe 7 pag. A4 orizzontale, ma nella grafica vecchia: **da rifare**|

## Problemi trovati
| Minuto | Tipo | Com'era | Correzione prevista |
|---|---|---|---|
|tutto|visivo|banda blu a destra, rettangolo 16:9 con bordo, nome senza fascia|riquadro 4:3 + fascia gialla su fondo bianco|
|0:18–0:54|visivo/testo|presentazione con **3 argomenti su 6**|card ARGOMENTI con tutti e 6|
|tutte le slide|visivo|etichetta «ARGOMENTO N · …», piè «LETTERATURA ITALIANA» senza «V»|«01 · …», piè e «Pagina N» come modello|
|approfondimenti, ripassi, glossario, riepilogo, compiti|visivo|fondo blu scuro|fondo bianco|
|1:54, 8:27, 9:41, 11:30, 19:20, 20:45, 22:32, 26:36|audio|silenzi tra 3 e 3,7 s (a 11:30/22:32 è il quiz; gli altri sono fine/inizio approfondimento)|riempire con voce o accorciare le pause|
|mappe (video e PDF)|testo|7 mappe costruite da noi con nodi **non nella mappa del prof** (es. «Giornale di guerra», «Eros e Priapo», «Accoppiamenti giudiziosi» come nodi)|la mappa del prof (`MAPPE/LEZIONE 20.pdf`, 1 pagina, 9 riquadri) impaginata identica, senza inventare|
|sottotitoli|testo|il parlato del prof è pieno di errori di trascrizione («Gadda»→«gabbiana/Gabbiana», «Carlo Milogato», «ultratutto fotografico», «sveviana» ecc.)|**da riscrivere tutti**: serve la trascrizione (vedi blocchi)|
|test (xlsx)|testo|le 10 domande coincidono con l'Excel del prof, ma resta il foglio «Istruzioni» del modello (parla di 15 domande)|togliere il foglio e le righe vuote|
|compiti|testo|4 domande = identiche al PDF del prof|OK|
|schede di comparsa|sync|(nota del montatore) tempi stimati dalla trascrizione, non per parola|ricontrollo a campione: nei fotogrammi la card gialla segue l'ordine 1-2-3 e nessuna slide resta ferma >60 s (OK a vista)|

## Piano e tempi (stima)
1. **Sbloccare la trascrizione** (serve alla master: modello Whisper `small` o equivalente raggiungibile, oppure la trascrizione dei pezzi del prof): senza non posso né correggere i `.vtt` né fare il controllo A.
2. Ricostruire la grafica al modello Spagnolo: è un **rifacimento di tutte le slide** (≈ 6 argomenti × 3 card + 17 approfondimenti + 6 ripassi + glossario + riepilogo + mappe) e dell'impaginazione del prof (4:3 dal video originale 1092×614). Stima **4–5 ore** dopo lo sblocco. Attenzione: il prof nell'originale è molto piccolo (≈245×140 px): il riquadro 4:3 sarà ingrandito ≈ ×1,7, quindi meno nitido del modello (limite del file originale).
3. Rifare audio dei pezzi del prof con la catena del kit, PDF slide/mappe, scheda, test.
