# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 4 «Naturalismo e Verismo» — correzioni 22/11
Ramo `revisione-letteratura-V-lez04` · versione del 23/11 (dopo le due correzioni della master del 22/11 20:15 e 20:45). Ogni dato è etichettato **misurato** / **non verificato**.

## 0. Correzioni richieste dalla master il 22/11 (v5 respinta) — fatte nel VIDEO
1. **Piè di pagina**: tolto «Prof. Giorgio Mazzotti» da tutte le slide e animazioni del video (ora «LETTERATURA ITALIANA V» e «Pagina N»), dalla mappa animata e da entrambi i PDF (`pdftotext` sui due PDF: 0 occorrenze di «Mazzotti»). Il nome del docente resta solo nella fascia gialla.
2. **Pagina 16 «Émile Zola…» ferma 3,4 minuti senza card accesa**: il pezzo del prof D2 è diviso a fine frase («…così riuscite a seguire.», pausa di 0,5 s) in D2a e D2b, e in mezzo c'è l'approfondimento animato Kore «Intorno a Zola» (i Goncourt, già nella lezione) spostato lì. Le finestre a/b delle card sono state ridistribuite: pagina contigua più lunga 170 s; dopo l'approfondimento la card in corso segue il parlato (temi principali a 6:20 del pezzo D2b; card 1 a fine pezzo).
3. **Ripasso**: ogni argomento ha il suo schema di ripasso di 4–6 righe che si accendono con la voce Kore e il jingle `repaso.wav` (S1–S4, GL, RF): non servono le pillole blu del 18/11. La master non reinserisce pezzi: il video qui è già completo.
4. `controllo_rapido.py` (CLAUDE.md §11): **ESITO OK**, nessun errore (file `controllo_rapido_Letteratura_Lez4_Parte1_1080p.json`, foglio `foglio_fotogrammi_Letteratura_Lez4_Parte1_1080p.jpg`, guardato a vista: fondo bianco, schede blu a tutto schermo, piè di pagina senza nome, nessun DM Mono, card a 40 px, mappa a 40 px, titolo di copertina esatto).

## 1. Cosa ho cambiato (rispetto alla consegna del 17/11)
- **Slide del prof a 40 px, interlinea 1,5**, al massimo 3 card, ogni card è una frase intera («Etichetta: testo»), card alte quanto il testo, bordo giallo e numero su pallino giallo **quando il prof inizia la frase** (tempi dalla trascrizione). Le altre card restano visibili attenuate. Titoli, etichette e piè di pagina invariati.
- **Nessuna schermata oltre 3 minuti**: le slide lunghe sono divise in due pagine («a» card 1–2, «b» card 2–3). Massimo misurato su pagina contigua: 165 s. Nessuna card sola.
- **Introduzione**: copertina con ARGOMENTI (testo 40 px) per 51 s con il prof che parla (video vivo); poi due slide «Di cosa parliamo» con gli argomenti in card che si accendono quando li nomina. Introduzione animata (35 s → 32 s) **senza riquadro del prof** e con voce nuova senza il nome del docente (voce `I2`).
- **Una sola mappa, quella del prof** (`MAPPE/LEZIONE 4.pdf`, «Il Verismo»), ridisegnata nel modello BES (pesca/celeste/paglierino/menta/lilla con legenda in alto a destra, frecce, testo 40 px): **si costruisce ramo per ramo** con la voce Kore (`M1`–`M9`), riquadro acceso in giallo mentre la voce parla, mappa intera ferma 4 s alla fine (con un sottofondo di jingle per non lasciare silenzio). Sta nell'argomento 3, prima della pillola. Stesse parole del prof (solo l'iniziale «Linguaggio» maiuscola). Nella mappa originale del prof (guardata a vista) non ci sono marchi né foto di autore: nessun marchio da togliere.
- **Niente «già visto»**: i rimbalzi del prof tra slide di altri argomenti (slide 2, 3, 4, 6 mostrate di nuovo a fine D3) sono sostituiti dalla slide dell'argomento in corso.
- **Voci**: tutte le voci già fatte riusate; nuove `M1`–`M9` (mappa) e `I2` (introduzione). Trascritte e confrontate con il testo (anno 1870 letto bene). Bordi sotto 0,03 (massimo 0,0124 su M7).
- **Audio**: −16,6 LUFS integrato, parlato del prof −16,8; picco −2,1 dBTP. Nessuna pausa oltre 2,5 s (schede titolo accorciate a 3 s, coda dell'introduzione tagliata, mappa con jingle sotto lo stacco finale). Timbro: vedi §2.
- **Sottotitoli** rigenerati sul video finale (664 blocchi, max 2 righe), grafia corretta dei nomi (nessuna forma fonetica).
- **Dispense A4 orizzontali con testo invisibile selezionabile**: `Letteratura_Lez4_slide.pdf` (66 pagine, copertina solo materia e titolo, piè di pagina «LETTERATURA ITALIANA V» + pagina, senza nome del docente) e `Letteratura_Lez4_mappe.pdf` (copertina con «MAPPE», poi la mappa del prof, vettoriale).
- Ripasso: la card «Madame Bovary (1857).» è ora la frase intera «Madame Bovary esce nel 1857.»; ritratto di Zola (slide 5 del prof, 624×850 px) migliorato (ingrandimento Lanczos, pulizia del rumore, nitidezza).

## 2. Controllo severo (`controllo_severo.py`) e controllo indipendente
**`controllo_severo.py` sul video corretto del 23/11: ESITO OK, zero errori** (file `severo_esito.json`), lanciato con 1 fotogramma ogni 60 s (con 10 s il programma non finisce in tempi ragionevoli su questa macchina). Nessuna slide con lo stesso titolo oltre 3 minuti, nessuna schermata identica oltre 3 minuti, nessuna «…», nessuna card sola oltre 60 s, −16,6 LUFS, nessuna pausa oltre 2,5 s; copertina 120 s secondo il campionamento a 60 s (reale 51 s). **`controllo_rapido.py`: ESITO OK.** Non verificato col passo da 10 s: card con iniziale minuscola e card spezzate sono controllate solo sui campioni. Pagina contigua più lunga calcolata sulla timeline: 170 s.


**Controllo con un agente separato** (non ha montato la lezione, lista §11): difetti trovati e corretti — (a) pagina 33, terza card vicina al piè di pagina → layout delle card rialzato (fondo massimo 946 px su 981); (b) ripasso con card «Madame Bovary (1857).» non frase intera → corretta; (c) ritratto di Zola sgranato → migliorato; (d) riquadro «Caratteri:» della mappa stretto → allargato; (e) pagina «Zola» ferma 175 s → divisa in due pagine con la ripresa su card 1. Segnalati e non cambiati: schede Quiz/Verifica/Compiti senza piè di pagina (sono schede di servizio con banda blu, come da decisione precedente); fascia gialla con «PROF. DI LETTERATURA ITALIANA» (richiesta dalla regola 000.6).

## 3. Misure sul video finale
- durata 48:53.2 (2933.2 s) | fotogrammi 87995 (attesi 87995) OK | peso 199.7 MB (190.4 MiB) OK | 1920x1080 OK
- quiz 4 scatto 0,0 s: OK
- fermi immagine nei pezzi del docente: nessuno OK
- volume del parlato (mediana dei pezzi del docente): -16.6 LUFS OK
- sottotitoli: 664 blocchi, sovrapposti 0, oltre la fine 0, attacco sulla voce entro 0,3 s: 93% di 14 verificabili OK
- foglio di miniature: Letteratura_Lez4_Parte1_1080p.mp4.miniature.jpg
- ESITO: TUTTO OK
- Jingle Quiz:
  Q1 atteso 734.233 trovato 734.238 scarto +0.005 OK
  Q2 atteso 1395.567 trovato 1395.572 scarto +0.005 OK
  Q3 atteso 2395.100 trovato 2395.105 scarto +0.005 OK
  Q4 atteso 2838.600 trovato 2838.604 scarto +0.005 OK
- Sincronia audio prof/originale (correlazione, ≤ 0,04 s richiesto):
  D1 scarto audio finale vs originale (s): [-0.02, -0.02, -0.02]
  D2a scarto audio finale vs originale (s): [-0.02, -0.02, -0.02]
  D2b scarto audio finale vs originale (s): [-0.02, -0.02, -0.02]
  D3 scarto audio finale vs originale (s): [-0.02, -0.02, -0.02]
  D4 scarto audio finale vs originale (s): [-0.02, -0.02, -0.02]

## 4. Tabella dei pezzi del prof (mai tagliato a metà frase)
| Pezzo | Minuto (nuovo) | Prime parole | Ultime parole | Frase intera |
|---|---|---|---|---|
| D1 | 0:50–8:59 | «Buongiorno e benvenuti alla lezione Naturalismo e Verismo» | «…sarà più incisivo, siamo anche nel secondo Ottocento» (0,78 s di silenzio dopo) | sì |
| D2a | 12:20–17:58 | «Va bene, quindi il vero caposcuola…» | «…perché si collega a Zola, così riuscite a seguire» (0,5 s di pausa dopo) | sì |
| D2b | 18:56–21:11 | «Accanto, come dicevo, a Zola operano i fratelli Edmond e Jules…» | «…molto personale di Zola, che però ha un certo seguito» (0,55 s dopo) | sì |
| D3 | 23:21–34:08 | «Va bene, ma oltre a che cosa abbiamo?» | «…è molto importante capirla e studiarla proprio perché si parla di Naturalismo» (1,05 s dopo) | sì |
| D4 | 40:01–45:17 | «Eh, se volete, come dire, delineare…» | «…nella prossima lezione affronteremo in ambiente italiano, o meglio siciliano, Verga» (1,64 s dopo) | sì |
Misurato sulla trascrizione con tempi; i 4 pezzi sono contigui nell'originale (0,351 → 1926,45 s). Nessuna pausa del prof tagliata (nessuna supera 2,5 s).

## 5. Secondi vecchi → nuovi
| Pezzo | secondo v2 (17/11) | secondo nuovo |
|---|---|---|
| T1 | 50.167 | 47.4 |
| T2 | 741.0 | 737.233 |
| T3 | 1403.333 | 1398.567 |
| T4 | 2412.7 | 2398.1 |
| Q1 | 737.5 | 733.733 |
| Q2 | 1399.833 | 1395.067 |
| Q3 | 2409.2 | 2394.6 |
| Q4 | 2853.7 | 2838.1 |
| AN10 | 2290.933 | 2285.167 |
| GL | 2857.2 | 2841.6 |
| RF | 2895.167 | 2879.567 |
| VERIFICA | 2928.933 | 2913.333 |
| COMPITI_INTRO | 2942.267 | 2926.667 |
| COMPITI | 2945.267 | 2929.667 |
| tolti | AN03, AN06, AN12, AN13 (schemi) | – |
Durata: v2 2948,8 s → nuovo 2933.2 s (48:53). `timeline.json` e `scheda_pubblicazione.json` sono rigenerati sul video finale: la master rigenera la pagina.

## 6. Cosa NON ho verificato
- **Ascolto umano**: nessuno ha riascoltato il video. Le trascrizioni automatiche di `M7` e `I2` leggono «Presentare» e «Contare» dove il testo dice «Rappresentare» e «Raccontare»: può essere un errore del riconoscitore o una sillaba mangiata dalla voce, **non verificato all'orecchio** → se la voce sbaglia la master la rigenera. Pronuncia di Zola, Taine, Rougon-Macquart, Flaubert non verificata all'orecchio.
- Sincronia labbra a vista (misurata solo l'audio, per costruzione stesso offset del video).
- Slide dell'ultima parte di D3: seguono i cambi slide della registrazione e il parlato, non una verifica del contenuto parola per parola.
- Webcam originale piccola (245×138 px) e testa del prof che in alcuni punti tocca il bordo alto già nell'originale: non correggibile.
- Mappe del prof per gli altri argomenti: non esistono (solo «Il Verismo»).
- Il controllo del timbro è quello di `controllo_severo.py` (6 campioni).

## 7. DA CONFERMARE
1. Esempi sul discorso indiretto libero in AN11 («Emma disse…»): frasi costruite da noi, con la scritta «ESEMPIO COSTRUITO PER SPIEGARE LA TECNICA».
2. Federico De Roberto compare solo nella mappa del prof, non nel parlato.
3. Durata 48:53 (sotto i 50 minuti, entro il limite 45–65 del controllo severo).
