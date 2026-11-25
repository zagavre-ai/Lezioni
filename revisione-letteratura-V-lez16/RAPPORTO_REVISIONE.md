# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 16 · Umberto Saba — correzioni 22/11 fatte (consegna 23/11)
Video `Letteratura_Lez16_Parte1_1080p.mp4` in parti da 90 MB (`cat …parte_* > …mp4`, sha256 nel file `.sha256`). 1920×1080, 30 fps, durata 55:05, −16,3 LUFS, picco −1,1 dBTP (misurati da `controllo_rapido.py`).

## Correzioni della master (22/11 21:40) — stato
1. **Card sole troppo lunghe** (pag. 21 e pag. 48): unite alle slide vicine / card di contesto; nessuna schermata ferma oltre 3 min (controllo: lista vuota).
2. **Mappa**: testo a 36–38 px nelle 5 schermate (prima ~24), ognuna ferma 2,5 s più suono di passaggio (non 6,5 s).
3. **Finale**: sigla del kit con avviso dei diritti e il suo audio, poi intro «Compiti» con jingle; schede quiz/verifica con «Rispondi · premi Controlla · poi Continua».
4. **Pause lunghe** a 11:43, 12:53, 15:06, 26:41, 26:45, 42:39, 44:33, 48:23, 49:00, 52:10, 53:42 accorciate; ora le pause mute >2,5 s sono eliminate tranne la lettura dei compiti (vedi sotto).

## controllo_rapido.py
Nome del docente nel piè di pagina: nessuno · fasce gialle sulle schede: nessuna · schermate ferme >3 min: nessuna · titolo copertina 2/2 parole.
**ESITO: DA CORREGGERE per una sola voce** — `pause_mute: 53:30 (94,7 s)`: è la lettura dei compiti del prof. La voce Kore `COMPITI` (testo in `testi_voci.json` sul ramo voci-) non è ancora stata generata dalla master: le schermate dei compiti sono pronte, l'audio no. Appena arriva `COMPITI.wav` rigenero solo la coda (≈10 min). Per il controllo elastico del 23/11 12:50 è un difetto non bloccante (pausa muta).
Foglio fotogrammi e json allegati: `foglio_fotogrammi_*.jpg`, `controllo_rapido_*.json`.

## Non verificato
Pronuncia delle voci Kore non ascoltata a orecchio (solo controllo ASR; MB07 e MB26 incerte); tagli tra approfondimenti senza dissolvenza; foto di Saba leggermente morbida; sincronia misurata per correlazione sull'originale.

## DA CONFERMARE COL PROF
- Padre di Saba: «cristiano» nelle slide, «cattolico» nella mappa (restano come li dicono).
- «Ernesto»: la mappa dice 1975; le slide «scritto nel 1953 e pubblicato postumo».
- La mappa aggiunge fatti non nelle slide (1906 Firenze, 1908 libreria, 1909 Lina, 1955 clinica a Gorizia).

## Correzione 25/11 (urgente)
**1. Mappa (48:56–51:54, durata invariata 3305,37 s: timeline, scheda e .vtt restano validi).** Rifatta **una sola mappa intera** (niente più 5 schermate), con le stesse parole e la stessa struttura della mappa del prof (Umberto Saba → Vita / Pensiero / Opere → Poesie → 1921 Canzoniere; Prosa). Colori BES con legenda in alto a destra; scritte a **34 px** (misurate nel codice: 34 px in tutti i riquadri); costruita ramo per ramo con la voce Kore già in lezione, riquadro in giallo finché la voce lo legge (tempi presi dalle evidenziazioni del video precedente). Resta intera dopo l'ultimo ramo per 2,8 s (non 4: la durata non può cambiare senza rifare l'audio).
Ricodifica unica: x264 veryfast CRF 19, audio copiato senza toccarlo. Controllato il fotogramma a 50:25 e a 51:40: mappa completa.
Per far stare tutto a 34 px la mappa usa due colonne di foglie (il messaggio della master del 22/11 vietava colonne con testo piccolo: qui il testo non è piccolo). Il titolo è «Mappa · Umberto Saba», non la domanda del prof (non l'ho inventata).
**2. Riquadro del docente: DIFETTO TROVATO, NON CORRETTO.** Nelle slide con le card a tutta larghezza (voce del prof, card accese) il riquadro con la fascia gialla manca per lunghi tratti: circa 10:35–15:00, 21:23–26:43, 37:46–44:34 e nelle slide fino a 48:50 (dove è presente solo in 0:15–10:34, 15:09–21:22, 26:44–37:45, 44:35–46:10 circa). Controllo fatto con un campionamento a 1 fotogramma/s della fascia gialla; i tratti senza fascia che sono schede Kore (ripasso, titoli, quiz, mappa, glossario) sono normali. Per correggerlo serve il **video originale del prof**, che in questa chat non c'è: richiesto alla master.
## Controllo rapido (25/11)
ESITO: DA CORREGGERE per la stessa unica voce di prima: `pause_mute 53:30 (94,7 s)` = lettura dei compiti (voce Kore COMPITI non ancora generata dalla master). Nessun altro errore; foglio e json aggiornati.
## Non verificato
Voce della mappa non riascoltata; sincronia di ogni ramo con la voce affidata alle evidenziazioni del video precedente, non a una nuova trascrizione.
