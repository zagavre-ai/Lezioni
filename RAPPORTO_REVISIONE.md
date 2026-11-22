# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 7 · correzioni 22/11
**Il romanzo nell'Europa e nell'Italia del Decadentismo** · rifatto il 22/11/2026. Etichette: **[misurato]**, **[stima]**, **[non verificato]**.

## 1. Cosa ho cambiato (rispetto alla consegna del 17/11)
- **Una sola mappa, quella del prof** (`MAPPE/LEZIONE 7.pdf`): tolte le 5 mappe nostre (una per argomento + finale). La mappa è ridisegnata nel modello BES approvato (pesca = concetto centrale, paglierino = parole chiave, lilla = conseguenza, menta = esempi e opere, legenda in alto a destra), con le **stesse parole e frecce del prof**, costruita ramo per ramo con voci Kore nuove P1–P10 (riquadro giallo finché la voce parla, mappa intera ferma 4 s); una volta sola, prima del glossario (min. 47:25.97). Testo 36–50 px. Mappa originale senza marchio e senza foto dell'autore (nessuna nel file del prof) [misurato].
- **Slide del prof ridisegnate**: testo delle card a **40 px**, interlinea 1,5, **al massimo 3 card (qui 1–2)**, ogni card è la frase intera del prof (etichetta + frase, mai «…»); slide divise «(1/2)», «(2/3)»; la card si accende a inizio frase (tempi dalla trascrizione). Nessun titolo di slide dura più di 180 s (massimo 174 s) e nessuna card sola dura più di 60 s [misurato sul piano di montaggio].
- **Animazioni e ripassi** rifatti con lo stesso testo a 40 px, pagine da 2–3 card numerate 1–3, mai una card sola quando evitabile; etichette con iniziale maiuscola.
- **Ritratti**: tolti da sotto il riquadro del prof; resta il ritratto di Wilde nella slide dedicata (27:55, quando il prof dice «Eccolo qua, Oscar Wilde») e quello di Huysmans sotto la sua unica card. Il ritratto di Deledda non compare più (nel file del prof è piccolo, 698×850).
- **Compiti dentro il video**: due slide con i 4 compiti del prof (testo identico al suo PDF), 28 s. Piè di pagina senza nome del docente (resta solo nella fascia gialla); la dispensa è identica al video.
- **Pezzi del prof** ricomposti a fine frase, senza tagli di pause interni tranne 1,5 s in D4 tra due frasi; nessun rallentamento né pausa stirata (tolti i silenzi lunghi del 17/11).
- Audio: parlato del prof rifatto dall'originale (highpass 80, arnndn, normalizzazione), volume totale **−16,3 LUFS**, picco **−1,4 dBTP**; jingle quiz a +0,005 s; titolo/ripasso/transizioni/finale inseriti [misurato per quiz e volume].
- Durata ora **51:34,3 (3094,3 s)** (92 829 fotogrammi): tolte le mappe inventate; `timeline.json`, `scheda_pubblicazione.json` (inizio/quiz di ogni argomento), `testo_youtube.txt`, `.vtt` (rifatto sul video finale) e PDF rigenerati.

## 2. Esito del controllo severo e del controllo indipendente
- `controllo_severo.py` sulla versione precedente (stessa grafica a 40 px non ancora applicata): **non ha finito** (OCR troppo lento, interrotto dopo 40 min). Sulla versione finale: **non completato**: l'OCR del controllo (tesseract installato da me) non è finito nei tempi per due volte su questa macchina lenta; **esito non ottenuto, non so se sarebbe OK**. Da rilanciare dalla master.
- **Controllo indipendente** (agente che non ha montato) sulla versione precedente: trovati 9 punti; corretti: ritratti sotto il riquadro, compiti non dentro il video, nome del docente nel piè di pagina del video, card sola con iniziale minuscola, rapporto non allineato. Non erano difetti: avviso diritti (c'è nei primi 4 s della sigla finale del kit, poi sfuma), mappe (ora una sola per regola). **Restano**: card «L'estetismo» (slide 3, argomento 1) con Wilde — è nella slide del prof, che ne parla più avanti; sigla 16,3 s (15 s del kit + 1,3 s di dissolvenza).

## 3. Tabella dei pezzi del prof (inizio e fine)
| Pezzo | Minuto video | Prime parole | Ultime parole | Frase finita |
|---|---|---|---|---|
| D0 | 0:45.77–2:09.27 | «Buongiorno e benvenuti alla lezione…» | «…del decadente, dell'esteta piuttosto che del simbolista.» | sì |
| D1 | 2:15.47–4:59.47 | «Allora. Iniziamo quindi in questo modo…» | «…o uno sfondo sociale storicamente definito.» | sì |
| D2 | 10:02.30–13:01.84 | «D'accordo, il testo si risolve…» | «…poi abbiamo la poesia di Verlaine e Rimbaud.» | sì |
| D3 | 19:35.74–28:54.20 | «Spostiamoci, come detto, in Inghilterra…» | «…Qua e, soprattutto, chi è e cosa scrive.» | sì |
| D4 | 37:38.47–42:29.44 | «Allora, spostando lo sguardo al contesto italiano…» | «…sempre in letteratura italiana, con Italo Svevo.» | sì |
Controllato sulla trascrizione dell'originale [misurato].

## 4. Misure sul video finale
- Durata 51:34,3, **92 829 fotogrammi** = durata×30, 1920×1080 30 fps, **188,4 MB**, x264 veryfast CRF 19, AAC 192k, 2 parti da 90 MB + sha256 [misurato].
- Volume totale **−16,3 LUFS**, picco **−1,4 dBTP** [misurato].
- Jingle Quiz: Q1 +0,000 s, Q2–Q4 +0,005 s dall'attacco atteso, OK [misurato, `controllo_jingle.py`].
- **Silenzi oltre 2,5 s: 9 [misurato] — NON a posto.** Sono le schede di titolo/quiz (3,2–4,8 s), il glossario (4,8 s), la verifica (3,7 s) e soprattutto le **2 slide dei compiti, 26 s senza voce** (a 51:08): servirebbe una voce Kore che le legga (non richiesta in tempo alla master). Da correggere.
- Slide: nessun titolo oltre 180 s (max 174 s), nessuna card sola oltre 60 s [misurato sul piano]; non rifatto il controllo con OCR sul video.
- Sincronia audio/originale: scarto 0,015 s misurato sulla versione del 17/11 (stessa catena audio); non rimisurato [non verificato].

## 5. Cosa NON ho verificato
- Silenzi oltre 2,5 s: vedi §4 (non risolti).
- **Ascolto umano delle voci**: pronuncia di Huysmans («Uismans»), Wilde («Uàild»), Dorian Gray («Dòrian Grèi») scritte foneticamente nelle voci P7–P8; la trascrizione automatica le riconosce, ma non le ho sentite. Le altre voci Kore (animazioni) non sono state riascoltate né ripronunciate: restano da controllare per i nomi stranieri.
- Timbro del prof (−9/−20 dB), fermi immagine del prof e sincronia delle labbra ricontrollati solo per costruzione (stesso istante dell'originale, scarto audio 0,015 s misurato sulla versione precedente) [non rimisurati].
- Quiz e verifica (10 domande del prof, `verifica_finale.json`) letti, non provati nella pagina. La scheda «Verifica» è la pausa del video: le domande stanno nella pagina.
- Sottotitoli corretti sul senso e sui nomi, non riascoltati; tratti non decifrabili omessi (circa 218,8–219,9 s, 225–233 s, 358–362 s dell'originale).
- Alta risoluzione: il ritratto di Wilde (641×850) e di Huysmans (667×850) sono piccoli e non migliorati.
- Confronto pagina per pagina dispensa/video non fatto su tutte le 84 pagine.

## DA CONFERMARE COL PROF
- Slide 3: card «L'estetismo» detta più avanti.
- Nome del pittore «Basil» nelle animazioni.
