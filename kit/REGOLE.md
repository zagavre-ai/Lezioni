# REGOLE DELLE CHAT · Videolezioni Centro Studi Telesio (versione 8/11/2026)

Valgono per tutte le chat e tutte le lezioni. Se una regola manca o non è chiara, chiedi alla master con stato.py (punto 9). Non chiedere a Sara.

## 1. Chi decide
- Sara decide: contenuti (quiz, titoli, docenti), soldi, «mi piace / non mi piace» dopo un ascolto o una visione.
- La master decide tutto il resto: formati, codifiche, strumenti, ordine dei lavori.
- A Sara non si fanno domande tecniche.

## 2. Struttura e durata
- Ogni Parte dura tra 50 e 60 minuti, regola del 7/11.
- Una lezione lunga fino a circa 65 minuti resta in una sola Parte (decisione dell'8/11).
- Se la lezione è più lunga, va divisa in due Parti, tagliando alla fine di un argomento. La Parte 2 si apre con il ripasso della Parte 1.
- Ordine dentro ogni Parte:
  1. sigla e benvenuto;
  2. per ogni argomento: titolo, docente con slide sincronizzate, eventuali animazioni, ripasso breve, scheda Quiz;
  3. glossario, ripasso finale, chiusura, sigla finale.
- Le aggiunte si prendono solo dal materiale del docente. Mai tagliare parole del docente, mai riempitivi.

## 3. Quiz e test
- Ogni argomento ha un quiz di 5 domande scritte da noi: 1 risposta giusta, 3 sbagliate e una spiegazione.
- La scheda Quiz dice «5 domande · per continuare almeno l'80%».
- Il test finale si prende dall'Excel del docente. Se manca, se ne propone uno con la scritta «PROPOSTA_DA_VALIDARE».

## 4. Voci
- Unica voce: Kore. Le genera SOLO la master.
- Mai voci locali, mai Vox Studio, mai la chiave nelle chat.
- I testi si mandano quando sono definitivi: scambio/<tag>/testi_voci.json nel ramo voci-<tag>.
- La master risponde nello stesso ramo, in scambio/<tag>/vox/NOME.wav, con un file ESITI.txt.
- Le voci ricevute si importano con voci_auto.py (kit/tools), che non le cancella mai.

## 5. File finali
- Video:
  - nome Materia_LezN_ParteN_1440p.mp4;
  - 2560×1440, 30 fotogrammi al secondo;
  - x264 fast, CRF 20, audio AAC 192k a 48 kHz;
  - una sola codifica, con tools/finale_a_pezzi.py;
  - sotto i 400 MB: se li supera, CRF 21 o 22.
- Sottotitoli: Materia_LezN_ParteN.vtt, fatti con tools/sub_finale.py sul video FINALE, con i termini corretti dal PDF.
- Altri file: dispensa A4 in PDF, quiz in .txt, test in .xlsx, scheda_pubblicazione.json (tools/scheda_da_timeline.py).

## 6. Controlli obbligatori sul file finale
- Scatto dei Quiz a 0,0 s, con tools/controllo_jingle.py.
- La docente o il docente non resta mai fermo sullo stesso fotogramma. I fermi sulle schede statiche vanno bene.
- Fotogrammi = durata × 30.
- Peso sotto i 400 MB.
- Parlato del docente a circa −16 LUFS.
- Sincronia: in almeno 4 punti presi qua e là, la frase che si sente deve essere la riga illuminata sulla slide.
- Sottotitoli: un controllo a campione sul video finale.

## 7. Stato per la master (sostituisce il blocco «PER LA MASTER»)
- Ogni volta che cambia fase, aggiorna lo stato:
  `python3 tools/stato.py <tag> --parte N --stato IN_MONTAGGIO|IN_CODIFICA|PRONTA|FERMA --video ... --vtt ... --voci kore --quiz_ok si --fermi_ok si --sub_ok si --invia`
- Durata, fotogrammi e peso li misura da solo il programma.
- Se un controllo manca, la Parte non può risultare PRONTA.
- Domande di contenuto per Sara: `--domanda_sara "..."`. Richieste alla master: `--serve_master "..."`.
- Quando una Parte è PRONTA, manda a Sara in chat, in un solo messaggio: video, .vtt, quiz, test, dispensa, scheda.

## 7-bis. Messaggi dalla master
- A ogni cambio di fase guarda kit/LEGGIMI.md su main (novità del kit) e il file scambio/<tag>/DALLA_MASTER.txt nel tuo ramo voci-<tag>: lì la master ti scrive istruzioni e file nuovi, senza passare da Sara.

## 8. Macchina e sicurezza
- I lavori lunghi devono poter ripartire: un lavoro in background viene fermato dopo 2 ore. Usa i marcatori .ok/.fatto.
- Scrivi i log con `> log && touch .fatto`, mai con `| tail`.
- Disco: cancella i pezzi intermedi appena la Parte è controllata.
- Mai chiavi o password in file, documenti o GitHub.
- Mai video o file grandi sul ramo main.
- Mai nomi di strumenti o programmi nei materiali per la scuola.
- Mai foto scaricate di personaggi pubblici.

## 9. Miglioramento ogni 3 giorni (regola di Sara)
- Se trovi un modo per fare prima, scrivilo con `--serve_master "MIGLIORAMENTO: ..."`.
- La master lo valuta e lo porta in tutte le chat.
