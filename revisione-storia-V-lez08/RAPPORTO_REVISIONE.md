# RAPPORTO DI REVISIONE · Storia V · Lezione 8 · «Il dopoguerra italiano (1919-1925) e il fascismo» (chat v3, rifacimento nel modello Spagnolo)
Ogni affermazione è etichettata **misurato / stima / non verificato**.

## 1 · Misure sul video nuovo (misurato)
- Parte 1: 52:48.2 · 3168.2 s · fotogrammi 95045 (attesi 95045) · 269.0 MB · sha256 `8e7f0079f41ff63563d25b908ebe230fb4d2fd2e776848a1640fcd1108e8f073`
- Parte 2: 56:57.3 · 3417.3 s · fotogrammi 102518 (attesi 102518) · 294.9 MB · sha256 `fad672ae8fb171080d928ea8cfd1bd7b9f999da04f926c7674f20426d9b1c0a1`
- 1920×1080, 30 fps, x264 veryfast CRF 19, maxrate 16 M, AAC 192 k. Parlato −16 LUFS (volume16). Esito `controllo_finale.py` e `controllo_jingle.py` nei file `controllo_P*.log` / `jingle_P*.log` (vedi sotto).
- Compiti, verifica finale e le due schede di servizio sono solo nella Parte 2 (t_verifica e t_compiti nella scheda di pubblicazione).

## 2 · Confronto col modello Spagnolo (punto per punto)
| Punto | Esito |
|---|---|
| Sigla 15 s + dissolvenza | **Segnaposto**: nel kit non esiste la sigla di Storia (`kit/sigle/Sigla_Storia_15s.mp4` assente). Uso una scheda blu di 15 s con l'avviso diritti in basso al centro (bianco, 24 px, senza riquadro) negli ultimi 2,2 s. |
| Copertina bianca: titolo esatto + card ARGOMENTI + voce di benvenuto | corretto |
| Titolo argomento (4a, blu animata, chip con parole chiave vere) | corretto (schede_spagnolo.py scala 1.0) |
| Docente + slide: fondo bianco, riquadro 4:3 con ombra grigia, fascia gialla «Giorgio Mazzotti / PROF. DI STORIA», piè di pagina | corretto (era azzurrino e con bordo blu) |
| Approfondimenti animati (4c) con voce Kore | presenti: 2 per argomento (circa 20–30 s ciascuno, 40–55 s per argomento: **sotto i 40–60 s richiesti per il singolo pezzo**, il testo è quello del prof) |
| Mappa del prof (4d) | **ridisegnata con `mappa.py`** (testo del prof, nodi a tempo con la voce). Il prof ha 3 mappe per 7 argomenti: ne metto solo 3, non ne invento. |
| Pillola: introduzione blu (4e) | presente per ogni argomento (voce Kore, didascalia = testo della voce) |
| Pillola: schema guidato bianco (4f) | presente per ogni argomento, 5–6 righe, una riga evidenziata alla volta con pausa di 2,5 s |
| Scheda Quiz (4g), 5 domande, soglia 80% | presente, scatto del jingle a 0,0 s |
| Glossario, Riepilogo finale (tutti gli argomenti), Finale | presenti |
| trans.wav + dissolvenza a ogni cambio di pezzo | presente (aggiunto a ogni transizione) |
| Font: solo Bricolage 800 e Figtree, niente DM Mono | rispettato |

## 3 · Problemi trovati nella consegna precedente e correzioni
Vedi `RAPPORTO` nella cartella: la consegna precedente (`consegna-storia-V-lez08`) aveva: slide con sfondo azzurrino e riquadro con bordo blu, fascia «Prof. … QUINTO ANNO», nessuna pillola/schema/mappa del prof, schede di servizio non nel modello, voce con data errata («6 novembre 1922» per il discorso del bivacco, che le slide danno al 16) e una voce con «6 aprile 1924» non presente nei materiali del prof: **entrambe rigenerate**. Corretti anche: ordine delle slide (il prof tratta Fiume prima delle elezioni del 1919: le slide seguono il parlato), titolo della copertina, sottotitoli (circa 130 correzioni di nomi e parole).

### Parte 1

| Pezzo | Nome | Presente | Minuto | Durata (misurata) |
|---|---|---|---|---|
| 1 · Sigla | SIGLA | sì | 0:00.0 | 16.3 s |
| 3 · Copertina + benvenuto (voce) | BENV | sì | 0:17.9 | 33.5 s |
| 3 · Introduzione del prof | D0 | sì | 0:53.0 | 222.4 s |
| 4a · Titolo argomento | T1 | sì | 4:36.8 | 4.0 s |
| 4b · Docente + slide | D1 | sì | 4:42.1 | 765.9 s |
| 4c · Approfondimento animato | AN1 | sì | 17:29.6 | 29.8 s |
| 4c · Approfondimento animato | AN2 | sì | 18:01.0 | 23.9 s |
| 4e · Pillola: introduzione blu | R1 | sì | 18:26.3 | 21.0 s |
| 4f · Pillola: schema guidato bianco | S1 | sì | 18:48.9 | 33.9 s |
| 4g · Scheda Quiz | Q1 | sì | 19:24.1 | 5.0 s |
| 4a · Titolo argomento | T2 | sì | 19:30.4 | 4.0 s |
| 4b · Docente + slide | D2 | sì | 19:35.7 | 823.9 s |
| 4c · Approfondimento animato | AN3 | sì | 33:21.2 | 20.8 s |
| 4c · Approfondimento animato | AN4 | sì | 33:43.6 | 25.1 s |
| 4d · Mappa del prof | MAP1 | sì | 34:10.3 | 26.3 s |
| 4e · Pillola: introduzione blu | R2 | sì | 34:38.0 | 26.5 s |
| 4f · Pillola: schema guidato bianco | S2 | sì | 35:06.1 | 41.9 s |
| 4g · Scheda Quiz | Q2 | sì | 35:49.4 | 5.0 s |
| 4a · Titolo argomento | T3 | sì | 35:55.7 | 4.0 s |
| 4b · Docente + slide | D3 | sì | 36:01.0 | 789.8 s |
| 4c · Approfondimento animato | AN5 | sì | 49:12.4 | 21.6 s |
| 4c · Approfondimento animato | AN6 | sì | 49:35.5 | 23.5 s |
| 4d · Mappa del prof | MAP2 | sì | 50:00.6 | 18.8 s |
| 4e · Pillola: introduzione blu | R3 | sì | 50:20.8 | 29.7 s |
| 4f · Pillola: schema guidato bianco | S3 | sì | 50:52.1 | 38.8 s |
| 4g · Scheda Quiz | Q3 | sì | 51:32.3 | 5.0 s |
| 5 · Glossario | GL1 | sì | 51:38.6 | 37.4 s |
| 6 · Riepilogo finale | RF1 | sì | 52:17.4 | 22.9 s |
| 7 · Finale (sigla di chiusura) | SFIN | sì | 52:41.9 | 6.3 s |

### Parte 2

| Pezzo | Nome | Presente | Minuto | Durata (misurata) |
|---|---|---|---|---|
| 1 · Sigla | SIGLA | sì | 0:00.0 | 16.3 s |
| 4e · Pillola: introduzione blu | RP1 | sì | 0:17.9 | 24.8 s |
| 4a · Titolo argomento | T4 | sì | 0:44.3 | 4.0 s |
| 4b · Docente + slide | D4 | sì | 0:49.6 | 522.0 s |
| 4c · Approfondimento animato | AN7 | sì | 9:33.2 | 33.5 s |
| 4c · Approfondimento animato | AN8 | sì | 10:08.3 | 21.0 s |
| 4e · Pillola: introduzione blu | R4 | sì | 10:30.7 | 26.6 s |
| 4f · Pillola: schema guidato bianco | S4 | sì | 10:58.9 | 38.9 s |
| 4g · Scheda Quiz | Q4 | sì | 11:39.2 | 5.0 s |
| 4a · Titolo argomento | T5 | sì | 11:45.5 | 4.0 s |
| 4b · Docente + slide | D5 | sì | 11:50.8 | 989.0 s |
| 4c · Approfondimento animato | AN9 | sì | 28:21.4 | 20.5 s |
| 4c · Approfondimento animato | AN10 | sì | 28:43.6 | 19.7 s |
| 4e · Pillola: introduzione blu | R5 | sì | 29:04.6 | 18.3 s |
| 4f · Pillola: schema guidato bianco | S5 | sì | 29:24.5 | 37.3 s |
| 4g · Scheda Quiz | Q5 | sì | 30:03.2 | 5.0 s |
| 4a · Titolo argomento | T6 | sì | 30:09.5 | 4.0 s |
| 4b · Docente + slide | D6 | sì | 30:14.8 | 623.4 s |
| 4c · Approfondimento animato | AN11 | sì | 40:39.8 | 19.7 s |
| 4c · Approfondimento animato | AN12 | sì | 41:01.1 | 28.8 s |
| 4e · Pillola: introduzione blu | R6 | sì | 41:31.3 | 16.7 s |
| 4f · Pillola: schema guidato bianco | S6 | sì | 41:49.6 | 36.4 s |
| 4g · Scheda Quiz | Q6 | sì | 42:27.3 | 5.0 s |
| 4a · Titolo argomento | T7 | sì | 42:33.6 | 4.0 s |
| 4b · Docente + slide | D7 | sì | 42:38.9 | 625.1 s |
| 4c · Approfondimento animato | AN13 | sì | 53:05.7 | 16.8 s |
| 4c · Approfondimento animato | AN14 | sì | 53:24.1 | 25.5 s |
| 4d · Mappa del prof | MAP3 | sì | 53:51.1 | 25.5 s |
| 4e · Pillola: introduzione blu | R7 | sì | 54:18.0 | 22.6 s |
| 4f · Pillola: schema guidato bianco | S7 | sì | 54:42.2 | 37.7 s |
| 4g · Scheda Quiz | Q7 | sì | 55:21.4 | 5.0 s |
| 5 · Glossario | GL2 | sì | 55:27.7 | 35.2 s |
| 6 · Riepilogo finale | RF2 | sì | 56:04.3 | 23.0 s |
| Scheda Verifica finale | VER | sì | 56:28.9 | 5.0 s |
| 7 · Finale (sigla di chiusura) | SFIN | sì | 56:35.5 | 6.3 s |
| Intro compiti (voce) | CINTRO | sì | 56:43.4 | 6.0 s |
| Scheda Compiti | COMP | sì | 56:51.0 | 6.3 s |

## 4 · Immagini del prof mostrate (misurato dalla trascrizione, tempi sulla lezione originale)
- guardie rosse a Torino (settembre 1920), ≈ 15:46 · veterani mutilati in piazza Colonna ≈ 20:05 · squadristi di Lucca (1922) ≈ 40:10 · carta del nord-est dopo Rapallo ≈ 47:20.
- Foto del PDF non mostrate dal prof (Gran consiglio del 1924, Matteotti): non inserite.

## 5 · Cosa NON ho verificato (non verificato)
- Non ho **ascoltato** la lezione per intero: ho controllato audio via trascrizione (Parakeet) e misure (LUFS, jingle, fermi).
- **Slide ferme > 3 minuti**: restano alcune card su cui il prof parla a lungo (≈ 3–7 minuti) perché il PDF non ha più testo da mostrare; ho diviso i paragrafi in frasi (max 3 card per slide, cambio slide almeno ogni 170 s dove possibile: 43 slide) ma non ho inventato contenuti. Restano 6 slide oltre i 3 minuti (la più lunga 6,8 min): elenco in `slide_lunghe.txt`.
- Sincronia card/voce: controllata su 10 punti a caso con la trascrizione parola per parola: 3 punti trovati entro ±0,3 s; 4 punti non verificabili perché il prof parafrasa; 2 punti ancora in anticipo di 7–13 s (paragrafi in cui il prof riprende l'argomento più avanti).
- Sincronia labbra ≤ 0,04 s: non misurata.
- Sottotitoli: riletti con elenco automatico di parole sospette; restano alcune frasi dove la trascrizione automatica è incerta (es. «già in carata», «a salarcon», «fosserati temporaneamente»): **da riascoltare**.
- Nelle prime 3 s dopo la sigla l'avviso diritti non compare (la copertina è bianca e il testo bianco non si vedrebbe).

## 6 · Come ho verificato (misurato)
Trascrizione parola per parola (Whisper base + Parakeet), `controllo_finale.py`, `controllo_jingle.py`, `foglio.png` (un fotogramma di ogni scheda blu + didascalie delle pillole), `controllo_minuti_P*.jpg` (un fotogramma ogni 30 s), confronto fotogramma per fotogramma delle schede con `MODELLO_Spagnolo_schede.jpg`.

## DA CONFERMARE COL PROF
- Compiti: nel PDF del prof la quarta domanda è numerata «3» per errore (qui è la 4).
- Nel video il prof cita «Natale di sangue», «scissione di Livorno», «Patto Gentiloni» (non nelle slide): usati nelle schede solo dove detti dal prof.
- Dalla slide 10 (carta di Rapallo): il prof la mostra per pochi secondi.

## Tabella secondo vecchio → nuovo (quiz)
Vedi `scheda_pubblicazione_Parte*.json` (`inizio_s`, `quiz_s`). Vecchia consegna: Parte 1 quiz a 1112,4 · 1981,3 · 2929,0 s; Parte 2 a 687 · 1615 · 2138 · 3141 s.
