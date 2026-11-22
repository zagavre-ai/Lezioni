# Regole blindate delle videolezioni

Valgono per **tutte le materie e tutte le lezioni**. Raccolgono le decisioni di Sara dal 29/10 al 22/11/2026. Non si discutono e non si chiedono più. Se una regola nuova contraddice una vecchia, vale la più recente, scritta in questo documento.

## 1. Chi decide e come si lavora
- **Sara** (Prof.ssa Sara Zagarese, Coordinatrice Didattica) decide i contenuti (quiz, titoli, docenti), i soldi e il «mi piace / non mi piace» dopo una visione. **Sui tagli delle parti dei docenti decide Sara.**
- **La master** decide tutto il resto: formati, codifiche, strumenti, ordine dei lavori. Approva al posto di Sara quiz e testi delle voci.
- **Le chat non fanno domande a Sara.** Scrivono alla master con `stato.py --serve_master "..."`. A Sara arriva solo lo stato.
- **Nessuno parte in automatico su cose nuove:** la master spiega a Sara cosa vuole fare e aspetta il suo sì.
- Nel dubbio non si inventa e non si stima: ci si ferma e si scrive alla master.
- **Mai contattare i docenti**, in particolare la Prof.ssa Caputi.
- Nei testi per docenti, alunni, famiglie e direzione Sara si scrive sempre «**Prof.ssa Sara Zagarese, Coordinatrice Didattica**».

## 2. Il docente: voce, parole, immagine
1. **Le parole del docente non si toccano.** Si tolgono solo pause lunghe, inizi e fini a vuoto, ripetizioni e incespicamenti. Mai riassunti, mai riempitivi.
2. **Mai tagliare il docente a metà frase.** Ogni pezzo del docente comincia e finisce su una frase intera, controllata sulla trascrizione. I tagli cadono nelle pause, 0,15 s prima della frase che segue. Le dissolvenze cadono solo nel silenzio. Nel rapporto va una tabella con la fine di ogni pezzo: minuto, ultime 6–8 parole, frase finita sì/no.
3. **Mai il docente fermo:** nessun fermo immagine di 1 s o più. In copertina il riquadro del docente c'è solo se parla davvero. Mai la sua foto fissa.
4. **Audio pulito ma con la sua voce:** filtro dei bassi, riduzione leggera del rumore, −16 LUFS (picco ≤ −1 dBTP). Pause oltre 2,5 s accorciate a circa 1 s. **La pulizia non deve cambiare il timbro.** Si misura: acuti sopra i 4 kHz meno volume sopra i 100 Hz tra −9 e −20 dB. Sotto −25 dB la voce è rovinata («grugnito», come Storia V lez04 e lez06) e la lezione non si consegna.
5. **Labbra e voce in sincrono**, scarto massimo 0,04 s per ogni pezzo, misurato sull'originale.
6. **Webcam:**
   - Prof. Mazzotti: riquadro 4:3 (412×309 a x=1428, y=148), ombra grigia.
   - Prof.ssa Caputi: **il suo tondo ripulito**, nella colonna destra, al massimo circa 2 volte il tondino originale, con la fascia gialla del nome e della materia.
   - Correzione colore leggera, niente sfocature dello sfondo. La sorgente è quella che è: non ci si ferma.
7. **I dati e i materiali dei docenti non si modificano mai.** Errori nelle loro slide o nei loro testi si segnalano alla master. Decide Sara.

## 3. Struttura della lezione
1. **Sigla della materia** (15 s, sempre la stessa, senza numero di lezione).
2. **Copertina** con il titolo **esatto** della lezione e gli argomenti, con voce di benvenuto. L'introduzione del docente sopra la copertina dura al massimo 3 minuti, poi si passa alla slide degli argomenti.
3. **Per ogni argomento:**
   - titolo dell'argomento, con jingle `titolo.wav`;
   - docente con slide sincronizzate alla sua voce;
   - **almeno un approfondimento animato** (40–60 s, voce narrante), solo dal materiale del docente;
   - **mappa dell'argomento** (sezione 6);
   - pillola o schema di ripasso, 4–6 righe che si accendono con la voce, jingle `repaso.wav`;
   - **quiz di 5 domande**: per continuare serve almeno l'80%. Lo scatto del jingle `quiz.wav` cade a +0,5 s dall'inizio della scheda, scarto 0,0 s.
4. **Fine:**
   - **glossario animato** (c'è in tutte le lezioni);
   - ripasso finale argomento per argomento;
   - mappa finale della lezione;
   - **verifica di sbarramento** con il test Excel del docente, soglia 80%, sempre dentro il video;
   - sigla finale con l'avviso dei diritti, in basso al centro, bianco, 24 px;
   - intro «Compiti» di circa 3,5 s con jingle, poi i **compiti del docente** dentro il video.
5. **Transizioni:** `trans.wav` più una dissolvenza di 0,3–1 s a **ogni** cambio di pezzo. Mai un taglio secco, mai una scheda in silenzio.
6. **Durata:**
   - ogni Parte dura 50–60 minuti; fino a circa 65 resta una sola Parte;
   - oltre i 65 si divide alla fine di un argomento, e la Parte 2 si apre con il ripasso della Parte 1;
   - una lezione più corta di 50 minuti con il solo materiale suo **va bene**: non si allunga e non si inventa.
7. **Le aggiunte vengono solo dal materiale della lezione stessa:** niente argomenti di altre lezioni, niente fonti esterne, niente foto di personaggi pubblici scaricate.

## 4. Le slide (modello: Spagnolo lez01 con le aggiunte approvate)
- **Al massimo 3 card per slide.** Ogni card è **una frase intera** del docente: mai spezzata con «…», mai con l'iniziale minuscola perché continua quella prima. Le card sono alte quanto il loro testo.
- La card della frase in corso si accende con bordo giallo e pallino giallo **quando il docente comincia la frase** (±1 s). Le altre card restano visibili, attenuate.
- **Nessuna schermata identica per più di 3 minuti** (per Caputi vale la regola del Ritmo, più severa: sezione 8).
- **Niente muri di testo.** Testo di almeno 28–30 px a 1080p, mai rimpicciolito: se non entra, la slide si divide in due.
- **Tabelle mai spezzate**, né su due slide né su due pagine.
- **Colonna destra riservata** al docente, alla fascia gialla e alle «Parole chiave» (massimo 5). Niente sotto il riquadro del docente, nessuna sovrapposizione. Il titolo non deve mai finire sotto il riquadro: se è lungo va su 2 righe.
- **Grafica:**
  - fondo **bianco puro**, mai crema;
  - blu notte #0B1530 per il testo, blu Telesio #2060AF per i titoli, giallo #FFE600 solo per evidenziare;
  - Bricolage Grotesque 800 per i titoli, Figtree per il testo, Figtree Bold per le etichette (mai DM Mono);
  - ombre grigie e morbide, mai nere;
  - schede di titolo, pillola, quiz e riepilogo in blu scuro animato, come Spagnolo.
- **Niente numero di lezione** in nessun materiale per lo studente. Niente nomi di programmi o strumenti. Niente parole straniere nelle grafiche, salvo citazioni e lingua della lezione.
- **Le immagini corrispondono esattamente a quello che dice il docente in quel momento.** Mai immagini di repertorio o di un altro argomento.

## 5. Disciplinare BES (vale anche nei controlli della master)
- **Niente «già visto»:** una slide o un'immagine del docente compare in un solo argomento. Una pagina con immagini di argomenti diversi si divide. Gli approfondimenti animati sono esclusi.
- **Ogni sigla o abbreviazione si rispiega ogni volta che compare**, a voce e sullo schermo. Esempio: «UA, cioè unità antropometrica, = 21 cm».
- Il colore non è mai l'unico segnale. Niente lampi o sfarfallii.
- Testo leggibile, frasi brevi, una cosa alla volta: «deve essere chiarissimo».
- **Sottotitoli** attivabili, spenti all'avvio, fatti sul video **finale** con i termini corretti presi dal materiale del docente.

## 6. Mappe concettuali
- **Le mappe sono quelle del docente:** stessa struttura, stesse frecce, **stesse parole**. Se il docente ha fatto una mappa unica, resta unica. Il titolo è la domanda del docente.
- **Si ridisegnano nitide**, in vettoriale e grandi, identiche alla sua ma leggibili. Mai il ritaglio dell'immagine del docente.
- **Colori del disciplinare BES**, al massimo 5, sempre con la legenda in alto a destra:
  - pesca: concetto centrale;
  - celeste: date e sequenze;
  - paglierino: parole chiave;
  - menta: esempi e opere;
  - lilla: conseguenze.
- Riempimenti pastello, testo blu notte, bordi pieni colorati, frecce blu notte. Testo in maiuscolo e minuscolo, 34–50 px.
- **Nel video si costruisce ramo per ramo:** un riquadro alla volta, con la sua freccia, mentre la voce lo legge, e il riquadro acceso in giallo finché la voce parla. Alla fine la mappa intera resta ferma 4 secondi.
- Se il docente non ha una mappa per un argomento, la mappa si costruisce **con le sue parole** e lo si dichiara nel rapporto.

## 7. Voci narranti
- Unica voce: **Kore**. La genera **solo la master**: le chat mandano `testi_voci.json` sul ramo `voci-<tag>`. Mai chiavi nelle chat.
- Testi **solo dal materiale del docente**.
- **Numeri e anni si scrivono in lettere** nel testo per la voce; sullo schermo restano in cifre. I nomi stranieri o latini si scrivono come si pronunciano (per esempio «Aracèli»).
- Ogni voce si **trascrive e si confronta** parola per parola, numeri e date compresi. Si controllano i bordi: negli ultimi 50 ms l'ampiezza deve stare sotto 0,03. Nel montaggio ogni voce ha una dissolvenza di 20–40 ms. **Nessuna voce troncata.**

## 8. Prof.ssa Caputi (Chimica, Tecnologie, Laboratori): regole in più
- ⚠️ **Docente molto esigente: controllo doppio** su nomi, misure, numeri, sigle, nome esatto della materia e refusi. Misure e numeri si riportano **come li dice lei**, senza calcoli aggiunti.
- **Modello approvato:** l'anteprima «Gonna» del 21/11, cioè sigla, introduzione con figurino, prof nel tondo, cartamodello passo per passo, mappa BES, quiz e il ritorno «ora torniamo dalla professoressa…».
- **Ritmo** (Sara, 22/11): la materia è pesante, quindi oltre a insegnare bisogna **intrattenere**.
  - La prof resta nel suo tondo ripulito.
  - **Quando spiega le parti tecniche o più complicate**, sopra la sua voce entrano animazioni fatte bene, grafiche e piccoli video che mostrano quello che dice. La sua voce non si taglia.
  - **Mai più di 90 secondi con lo schermo fermo.**
  - Pause della prof oltre 1,2 s accorciate a 0,6 s, solo tra due frasi.
  - Voce narrante vivace; curiosità «Lo sapevi?» solo con fatti del PDF della prof.
- **Illustrazioni ad acquerello**, nello stile del figurino della Gonna («come il disegno di uno stilista»), tutte della stessa qualità.
  - **Mai tagliate:** il soggetto è intero, con margine.
  - Niente campioni di colore, niente scritte, carta portata a bianco puro.
  - Le genera la master con `immagini.json`.
- **Cartamodelli, schemi e formule:** si rifanno **in vettoriale, con controllo al millesimo**. Il controllo lo fa una sessione diversa da chi ha disegnato: confronto a 4× su tutta la figura, rette entro 1,5 px, curve entro 2 px, tutte le scritte presenti e identiche. Nel rapporto: difetti trovati, corretti e residui.
- I tagli delle parti della prof li **propone** la chat. **Decide Sara.**

## 9. Dispensa A4
- **Identica a quello che si vede nel video:** stesse slide, stesso ordine, stessa grafica, a tutta larghezza. Per l'accessibilità si aggiunge solo uno **strato di testo invisibile**, selezionabile e leggibile dalla sintesi vocale, senza cambiare l'aspetto.
- A4 orizzontale, copertina «DISPENSA DIDATTICA» **senza numero di lezione**, piè «MATERIA · Prof./Prof.ssa Nome Cognome · Pagina N», mappe incluse, tabelle mai spezzate, accenti giusti.

## 10. File, consegna, sicurezza
- **Video:**
  - `Materia_LezN_ParteN_1080p.mp4`, 1920×1080, 30 fotogrammi al secondo;
  - x264 veryfast, CRF 19, AAC 192k a 48 kHz;
  - una sola codifica, sotto i 400 MB.
- **Consegna sul ramo `revisione-<tag>`:**
  - video a pezzi da 90 MB con sha256;
  - `.vtt`;
  - `timeline_ParteN.json` e `scheda_pubblicazione_ParteN.json` rigenerati sul video **finale**;
  - `RAPPORTO_REVISIONE.md` con le misure.
  - Lo stato diventa `REVISIONATA`. La master controlla e carica su Vimeo.
- **Repository pubblico:**
  - mai dati di alunni, mai chiavi o password;
  - commit senza firma;
  - mai video sul ramo `main`.
- **Piattaforma SoluzioneFAD:** solo lettura, salvo un ok esplicito di Sara.

## 11. Controlli obbligatori prima di consegnare (se uno non torna, non si consegna)
Il controllo lo fa **un agente separato**, che non ha montato la lezione. I difetti si correggono e il controllo si ripete finché non ne resta nessuno.

- [ ] Nessun taglio a metà frase del docente (tabella inizio e fine di ogni pezzo).
- [ ] Voce del docente non alterata: timbro tra −9 e −20 dB in ogni Parte, confrontato con l'originale.
- [ ] Labbra e voce entro 0,04 s; nessun fermo immagine del docente.
- [ ] Nessuna schermata identica oltre 3 minuti (Caputi: oltre 90 secondi).
- [ ] Card intere, al massimo 3 per slide, bordo giallo all'inizio della frase (10 punti controllati con la trascrizione).
- [ ] Mappe del docente, colori BES con legenda, costruite ramo per ramo con la voce.
- [ ] Ogni sigla rispiegata; niente «già visto».
- [ ] Glossario presente; quiz da 5 domande con scatto a 0,0 s; verifica di sbarramento e compiti dentro il video.
- [ ] Voci intere: trascritte, numeri giusti, bordi sotto 0,03.
- [ ] Copertina con titolo esatto; introduzione del docente al massimo 3 minuti; nessun titolo sotto il riquadro.
- [ ] Volume −16 LUFS ±1; fotogrammi = durata × 30; peso sotto 400 MB.
- [ ] Nessun numero di lezione, nessun nome di programma, fondo bianco.
- [ ] Dispensa identica al video, con il testo invisibile; sottotitoli fatti sul video finale.
- [ ] Il rapporto dice cosa è stato verificato e **cosa no**.

## 12. Il controllo severo della master (dopo la consegna)
La master ricontrolla ogni lezione prima di caricarla. Rimanda indietro se trova anche una sola di queste cose:
- schermate identiche troppo a lungo;
- voce alterata;
- glossario mancante;
- titoli o copertine sbagliati;
- docente tagliato;
- voci troncate;
- quiz fuori tempo.

Se tutto va bene, carica su Vimeo e aggiorna lo stato delle videolezioni.
