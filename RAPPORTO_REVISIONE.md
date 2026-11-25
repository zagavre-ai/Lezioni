# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 7 · correzioni 22/11
**Il romanzo nell'Europa e nell'Italia del Decadentismo** · rifatto il 22/11/2026. Etichette: **[misurato]**, **[stima]**, **[non verificato]**.

## 1. Cosa ho cambiato (rispetto alla consegna del 17/11)
- **Una sola mappa, quella del prof** (`MAPPE/LEZIONE 7.pdf`): tolte le 5 mappe nostre (una per argomento + finale). La mappa è ridisegnata nel modello BES approvato (pesca = concetto centrale, paglierino = parole chiave, lilla = conseguenza, menta = esempi e opere, legenda in alto a destra), con le **stesse parole e frecce del prof**, costruita ramo per ramo con voci Kore nuove P1–P10 (riquadro giallo finché la voce parla, mappa intera ferma 4 s); una volta sola, prima del glossario (min. 45:55.69). Testo 36–50 px. Mappa originale senza marchio e senza foto dell'autore (nessuna nel file del prof) [misurato].
- **Slide del prof ridisegnate**: testo delle card a **40 px**, interlinea 1,5, **al massimo 3 card (qui 1–2)**, ogni card è la frase intera del prof (etichetta + frase, mai «…»); slide divise «(1/2)», «(2/3)»; la card si accende a inizio frase (tempi dalla trascrizione). Nessun titolo di slide dura più di 180 s (massimo 174 s) e nessuna card sola dura più di 60 s [misurato sul piano di montaggio].
- **Animazioni e ripassi** rifatti con lo stesso testo a 40 px, pagine da 2–3 card numerate 1–3, mai una card sola quando evitabile; etichette con iniziale maiuscola.
- **Ritratti**: tolti da sotto il riquadro del prof; resta il ritratto di Wilde nella slide dedicata (27:55, quando il prof dice «Eccolo qua, Oscar Wilde») e quello di Huysmans sotto la sua unica card. Il ritratto di Deledda non compare più (nel file del prof è piccolo, 698×850).
- **Compiti dentro il video**: slide a card che compaiono una alla volta (voce COMPITI in arrivo) con i 4 compiti del prof (testo identico al suo PDF), 28 s. Piè di pagina senza nome del docente (resta solo nella fascia gialla); la dispensa è identica al video.
- **Pezzi del prof** ricomposti a fine frase, senza tagli di pause interni tranne 1,5 s in D4 tra due frasi; nessun rallentamento né pausa stirata (tolti i silenzi lunghi del 17/11).
- Audio: parlato del prof rifatto dall'originale (highpass 80, arnndn, normalizzazione), volume totale **−16,3 LUFS**, picco **−1,6 dBTP**; jingle quiz a +0,005 s; titolo/ripasso/transizioni/finale inseriti [misurato per quiz e volume].
- Durata ora **50:38 (3037,9 s)** (91 141 fotogrammi): tolte le mappe inventate; `timeline.json`, `scheda_pubblicazione.json` (inizio/quiz di ogni argomento), `testo_youtube.txt`, `.vtt` (rifatto sul video finale) e PDF rigenerati.

## 2. Esito del controllo severo e del controllo indipendente
- `controllo_severo.py` sulla versione precedente (stessa grafica a 40 px non ancora applicata): **non ha finito** (OCR troppo lento, interrotto dopo 40 min). Sulla versione finale: sostituito dal `controllo_rapido.py` della master (vedi sotto).
- **Controllo indipendente** (agente che non ha montato) sulla versione precedente: trovati 9 punti; corretti: ritratti sotto il riquadro, compiti non dentro il video, nome del docente nel piè di pagina del video, card sola con iniziale minuscola, rapporto non allineato. Non erano difetti: avviso diritti (c'è nei primi 4 s della sigla finale del kit, poi sfuma), mappe (ora una sola per regola). **Restano**: card «L'estetismo» (slide 3, argomento 1) con Wilde — è nella slide del prof, che ne parla più avanti; sigla 16,3 s (15 s del kit + 1,3 s di dissolvenza).

## 3. Tabella dei pezzi del prof (inizio e fine)
| Pezzo | Minuto video | Prime parole | Ultime parole | Frase finita |
|---|---|---|---|---|
| D0 | 0:42.10–2:05.60 | «Buongiorno e benvenuti alla lezione…» | «…del decadente, dell'esteta piuttosto che del simbolista.» | sì |
| D1 | 2:09.80–4:53.80 | «Allora. Iniziamo quindi in questo modo…» | «…o uno sfondo sociale storicamente definito.» | sì |
| D2 | 9:37.81–12:37.34 | «D'accordo, il testo si risolve…» | «…poi abbiamo la poesia di Verlaine e Rimbaud.» | sì |
| D3 | 18:49.99–28:08.46 | «Spostiamoci, come detto, in Inghilterra…» | «…Qua e, soprattutto, chi è e cosa scrive.» | sì |
| D4 | 36:24.35–41:15.32 | «Allora, spostando lo sguardo al contesto italiano…» | «…sempre in letteratura italiana, con Italo Svevo.» | sì |
Controllato sulla trascrizione dell'originale [misurato].

## 4. Misure sul video finale
- Durata 50:38, **91 141 fotogrammi** = durata×30, 1920×1080 30 fps, 181,9 MB, 2 parti da 90 MB + sha256 [misurato].
- Volume **−16,3 LUFS**, picco **−1,6 dBTP**; jingle Quiz a +0,000/+0,005 s [misurato].
- **`controllo_rapido.py`**: tutti i controlli OK (formato, peso, volume, piè di pagina senza nome del docente, nessuna schermata ferma oltre 3 min) **tranne** una pausa muta: **49:24 (73 s) = i compiti, in attesa della voce Kore COMPITI** (testo pushato su `voci-letteratura-V-lez07`); appena arriva la inserisco. «titolo in copertina 6/7 parole»: segnalato dalla master come falso allarme.
- Pause mute dell'elenco della master (7:04, 9:09, 19:32, 37:35, 47:22, 48:35, 50:42, 50:50, 51:08): schede e gap accorciati (gap tra pezzi 0,6 s, schede titolo 3 s, verifica 4 s, scene tagliate a 1 s dopo la voce); le ultime 5 pause residue di 2,6–3,4 s sono coperte da un breve suono di transizione a basso volume (`trans.wav`, −6 dB) [misurato: il controllo non le vede più]. Foglio dei fotogrammi e json del controllo sul ramo.

## 5. Cosa NON ho verificato
- Silenzi oltre 2,5 s: restano quelli delle schede di titolo/quiz/verifica/compiti (3–4 s) e la coda di alcune voci; non accorciati [misurato: vedi misure].
- **Ascolto umano delle voci**: pronuncia di Huysmans («Uismans»), Wilde («Uàild»), Dorian Gray («Dòrian Grèi») scritte foneticamente nelle voci P7–P8; la trascrizione automatica le riconosce, ma non le ho sentite. Le altre voci Kore (animazioni) non sono state riascoltate né ripronunciate: restano da controllare per i nomi stranieri.
- Timbro del prof (−9/−20 dB), fermi immagine del prof e sincronia delle labbra ricontrollati solo per costruzione (stesso istante dell'originale, scarto audio 0,015 s misurato sulla versione precedente) [non rimisurati].
- Quiz e verifica (10 domande del prof, `verifica_finale.json`) letti, non provati nella pagina. La scheda «Verifica» è la pausa del video: le domande stanno nella pagina.
- Sottotitoli corretti sul senso e sui nomi, non riascoltati; tratti non decifrabili omessi (circa 218,8–219,9 s, 225–233 s, 358–362 s dell'originale).
- Alta risoluzione: il ritratto di Wilde (641×850) e di Huysmans (667×850) sono piccoli e non migliorati.
- Confronto pagina per pagina dispensa/video non fatto su tutte le 84 pagine.

## DA CONFERMARE COL PROF
- Slide 3: card «L'estetismo» detta più avanti.
- Nome del pittore «Basil» nelle animazioni.

## Correzione urgente 25/11 · voci tagliate ai passaggi tra i pezzi
- Causa trovata: le voci Kore di AN1…AN23, S1–S4 e RF1 partivano 0,6–1,4 s PRIMA della loro scheda (finivano sopra il pezzo precedente) e le schede erano più corte della voce di 1–2 s: il cambio di pezzo cadeva dentro la voce. In D2, D3, D4 la coda del docente era coperta dalla voce successiva.
- Rifatto il montaggio solo di questi punti, partendo dal video consegnato: ogni voce Kore (da `vox/`) è montata INTERA, con 0,7 s di silenzio prima e dopo e dissolvenza di 30 ms; la scheda animata è rallentata del 3,3–6,2 % per contenerla (nessun fermo immagine). Tra i pezzi: silenzio, dissolvenza video 0,4 s e `trans.wav` (24 passaggi indicati + AN1→AN2, AN3→AN4, AN4→S1). Code del docente D2, D3, D4 tagliate nel silenzio, dopo la fine della frase (controllato sull'originale: il docente tace da 0,7–1,4 s prima del taglio). D1 era già finita nel silenzio.
- Sigla finale (SFIN) e jingle VER e Compiti riposizionati sulla loro scheda (l'audio anticipava di circa 1 s).
- Tolto «e ci vediamo alla prossima lezione» dalla scheda finale (testo) e dalla voce FIN1 (voce Kore tagliata nella pausa dopo «attenzione»). La master può generare `FIN1_R2` con il solo testo «Fine della lezione. Grazie per l'attenzione.» se vuole la chiusura naturale.
- Durata nuova 51:23 (3082,67 s), 92480 fotogrammi; sottotitoli, timeline e scheda rigenerati con i nuovi tempi (i sottotitoli sono i precedenti spostati sui nuovi tempi, non ritrascritti). Volume −16,1 LUFS, picco −1,6 dBTP.
- `controllo_rapido.py`: tutto OK TRANNE la pausa muta 50:09 (73 s) = compiti, in attesa della voce Kore COMPITI (nota già nel rapporto precedente, non è in `vox/`). ESITO DA CORREGGERE solo per questo.
- NON verificato: la trascrizione ripetuta dei bordi di ogni voce sul video nuovo; la sincronia fine delle card con la voce dopo il rallentamento (±1 s al massimo); l'ascolto di ogni passaggio. Controllo da parte di un agente separato non fatto per il tempo.
