# RAPPORTO DI REVISIONE · Letteratura italiana V · Lezione 26 · Italo Calvino (Prof. Giorgio Mazzotti)
**Correzioni 22/11 fatte** · ramo `revisione-letteratura-V-lez26` · stato `REVISIONATA`

## Cosa ho cambiato il 22/11 (secondo `PROMPT_Letteratura_correzioni_22-11.md` e `REGOLE_BLINDATE.md`)
- **Una sola mappa, quella del prof** (`MAPPE/LEZIONE 26.pdf`, «Italo Calvino 1923-1985»): tolte le 5 mappe per argomento e la mappa finale inventate da noi. Ridisegnata in vettoriale nel **modello BES approvato**: stessa struttura (vita, pensiero, saggista, opere con caratteristica e 5 famiglie di opere), stesse parole, stesse frecce, 5 colori BES con legenda in alto a destra (pesca, celeste, paglierino, menta, lilla), testo 34–50 px. Si costruisce **riquadro per riquadro con la voce Kore** (10 voci `MP1–MP10`, riquadro acceso in giallo mentre la voce parla), alla fine resta ferma 4 s. Compare **una volta sola**, prima del glossario. **Tolti il marchio «Mappe per la scuola» e la foto dell'autore** (decisione di Sara). Anni in lettere nel testo delle voci, in cifre sullo schermo.
- **Testo a 40 px**, interlinea 1,5, in tutte le card (slide del prof, schede opera, confronti, ripassi, riepilogo, compiti); glossario (tabella) a 34/32 px. Quando due card non entrano insieme la slide si divide.
- **Slide del prof:** al massimo 2 card per pagina, ogni card è una frase intera del prof (mai «…», mai iniziale minuscola); una pagina nuova a ogni frase in corso, con bordo giallo e pallino giallo quando il prof la comincia. Nessuna pagina oltre 3 minuti (la card più lunga, 182 s, è divisa in due pagine con la parte in corso evidenziata). Nessuna card sola oltre 60 s. Ripassi e riepilogo a pagine di massimo 3 righe.
- **Copertina:** titolo «Italo Calvino» intero; il riquadro del prof compare solo da 0:44, quando parla davvero; introduzione 30 s.
- **Dentro il video, come da regole blindate:** scheda «Verifica finale» (10 domande, 80%) e **compiti del prof** (intro con jingle + 4 esercizi letti da Kore, `CP1–CP4`), poi sigla finale con avviso dei diritti. Tolta la scheda «Fine della lezione».
- **Pause mute > 2,5 s:** accorciate (schede quiz −0,8 s, attacco del pezzo 3 −1,1 s) o spezzate con `trans.wav`; nessuna pausa muta oltre 2,3 s.
- **Audio:** −16,0 LUFS, picco −1,4 dBTP; jingle quiz a +0,5 s (scarto ≤ 0,004 s, `controllo_jingle.txt`); `trans.wav` e dissolvenze (0,3 s tra pagine, 0,6 s tra slide e schede, 0,4 s verso la sigla finale).
- **Durata:** 53:03 (3182,9 s), 95.486 fotogrammi = durata × 30; peso 199 MB.
- File rigenerati sul video finale: `.vtt` (766 cue), `timeline_Parte1.json`, `scheda_pubblicazione(_Parte1).json` (titolo «Letteratura V · Lezione 26 · Italo Calvino»), `quiz_argomenti.json` con `quiz_s`, `verifica_finale.json`, `testo_youtube.txt`.
- **Dispense A4 orizzontali** identiche al video, con testo vero selezionabile: `Letteratura_Lez26_slide.pdf` (68 pagine, copertina con solo materia e titolo, piè di pagina senza nome del docente) e `Letteratura_Lez26_mappe.pdf` (copertina con «MAPPE» + mappa).

## Tabella dei pezzi del prof (inizio e fine, dalla trascrizione corretta; minuti del video nuovo)
| Pezzo | Inizio | Prime parole | Inizio pulito | Fine | Ultime parole | Frase finita |
|---|---|---|---|---|---|---|
| 1 | 0:44 | «Buongiorno e benvenuti alla lezione su Italo Calvi…» | sì | 7:29 | «…anche dello sfondo storico, ma ci atteniamo all'autore.» | sì |
| 2 | 10:41 | «Allora, io proseguirei, come dire, anche con le sl…» | sì | 14:54 | «…ondizione dell'uomo contemporaneo, diviso e incompleto.» | sì |
| 3 | 19:34 | «Continua, visto che c'è una teleologia, dobbiamo a…» | sì | 26:11 | «…Sancice e la definitiva chiusura della fase realistica.» | sì |
| 4 | 30:55 | «E poi il secondo Calvino, questo era un po' il pri…» | sì | 34:46 | «…La buona strada.» | sì |
| 5 | 39:08 | «Parliamo anche del meta-romanzo Se una notte d'inv…» | sì | 43:13 | «…piuttosto diverso da come lo trattano altri.» | sì |
Il pezzo 4 parte dopo la pausa (prima iniziava con «…al vino.», coda mozzata). Sincronia misurata (16/11, ancora valida: pezzi e offset non sono cambiati): scarto audio ↔ originale max 0,003 s; nessun fermo immagine ≥ 1 s nel riquadro del prof.

## Controllo severo
`controllo_severo.py` lanciato sul video finale (passo 20 s) ma **non ha finito entro la consegna** (OCR lento su questa macchina): **esito non disponibile**. Misure equivalenti fatte a mano: slide per pagina ≤ 182 s (una sola, divisa in due pagine), nessuna schermata identica oltre 3 min (campionamento ogni 10–20 s da agente separato), nessuna card con «…» o iniziale minuscola, copertina con titolo «Italo Calvino» intero e di 30 s, LUFS −16,0, nessuna pausa muta oltre 2,3 s, durata 53:03, voce del prof non rielaborata.

**Controllo di un agente separato** (non ha montato la lezione; solo vista, senza ascolto): esiti OK su slide non ferme oltre 3 min, card intere (nessuna «…» né minuscola), copertina senza riquadro del prof (compare da 0:41–0:44, video vivo; i «fermi» segnalati dallo script erano falsi positivi: zone con tabelle o card scure), mappa una sola volta e costruita per riquadri con legenda, glossario, 5 quiz, verifica e compiti nel video, sigla finale con avviso dei diritti, `.vtt` e JSON coerenti con i secondi del video. Difetti trovati e **corretti**: copertina dei PDF (ora solo materia e titolo, con «MAPPE» nel PDF mappe); nel PDF mappe lo stile della mappa non era applicato e un testo usciva in un font di ripiego (rifatto, frecce comprese). Segnalazioni **non confermate**: testo piccolo nelle schede opera/glossario (il testo è 38–40 px nelle schede e 34/32 px nel glossario, tabella; non misurato dall'agente); mappa «ferma 70 s» (dopo il 7° riquadro cambiano solo piccole parti e l'evidenziazione: la mappa intera resta ferma 4 s); piè di pagina con il nome del docente nel **video** (come nel modello Spagnolo; nei PDF è tolto).

## Voci nuove (MP1–MP10, CP1–CP4): controllo
Trascritte tutte con `trascrivi.py` e confrontate con il testo: corrispondenza completa (numeri letti correttamente); bordi: ampiezza negli ultimi 50 ms < 0,03 in tutte. **Da riascoltare** (il riconoscimento ha capito diversamente): MP1 «Ecco la mappa» (capito «Con la mappa»), CP4 «Quarto esercizio» (capito «Tu esercizio»), MP8 «dimezzato» e MP7 «Marcovaldo» (capiti «di Mezzato» / «Marco Valdo»), MP9 «cosmicomiche». Il servizio ha segnato MP1, MP7, MP9 «durata fuori misura» (voce lenta, nessun taglio). Se la master le sente sbagliate: rigenerare con `_R2` e rimontare.

## Refusi / anomalie del materiale del prof (da non correggere, per Sara)
- «Siena nel 1983» detto dal prof (morte nel 1985, come nella sua mappa); slide del prof «Muore a Siena nel 1983».
- *La speculazione edilizia*: 1957 nella slide, **1963 nella mappa** del prof: la mappa è riportata com'è.
- Nella mappa del prof compare «Marcovaldo … 1963».

## Cosa NON ho potuto verificare
- **Ascolto**: non posso ascoltare audio. Le sincronie voce-schermo sono derivate dalle pause misurate; i sottotitoli del prof sono corretti per contesto (non ascoltati); le voci nuove sono verificate solo con trascrizione automatica.
- Rumore/timbro della voce del prof: audio del pezzo come già approvato (alto-passa 80 Hz presente); il timbro (−9…−20 dB sopra 4 kHz) non l'ho rimisurato dopo la ricodifica.
- Tempi dei sottotitoli delle voci Kore (benvenuto, ripassi, glossario, mappa, compiti): stima dalle pause (±0,3–0,5 s).
- Immagine del ritratto di Calvino a 1:07–1:14: viene dalla slide 2 del prof (editoriale, miglioramento non applicato).
- Nel video la mappa dura 2:23 (10 voci); il confronto delle parole con la mappa del prof è fatto a mano, riga per riga.

## Correzioni dopo il controllo della master (16/11)
1. **Slide vuote:** la scheda «Il visconte dimezzato» (e tutte le altre slide senza prof: schede opera, linee del tempo, confronti, analisi, parole chiave) restava a solo titolo fino alla prima card. Ora la prima card/punto/riga è presente dal primo fotogramma; nei ripassi, nel glossario e nel riepilogo tutte le righe sono presenti sbiadite e si accendono a tempo con la voce; le mappe partono con centro + primo ramo. Controllo: nessuna pagina ha uno stato senza contenuto (misurato su tutte le 45 pagine).
2. **Font delle etichette:** Figtree Bold maiuscolo spaziato (anche nelle etichette gialle delle card e nei PDF; il pallino dell'elenco della copertina ora è disegnato, non un carattere).
3. **Picco audio:** limitatore sul parlato, picco vero −1,5 dBTP, −16,1 LUFS; stesso numero di fotogrammi (94.626).

## Da chiarire con il prof / da riascoltare (non sono stati modificati o sono dubbi)
1. **Anni:** il prof dice «Siena nel 1983» (a 42:37 nel video nuovo): la sua mappa dice 1985 (morte); la sua slide dice 1983. La speculazione edilizia è «1957» nella slide e nel quiz, «1963» nella **mappa del prof**: nelle mappe ho lasciato 1963 (contenuto identico) e la voce lo dice («segnate entrambe con l'anno 1963»). Il sottotitolo riporta ciò che il prof dice. Sara: confermare con il prof.
2. **Ordine in apertura:** la card «ARGOMENTO 01» (0:40–0:44) compare prima del benvenuto del prof. Non l'ho spostata per non rompere le sigle audio.
3. **Frase del narratore** AN4c (≈ 38:23 nel video nuovo): «Le città invisibili, con una mappa e una piccola analisi guidata»: a schermo non c'è una mappa. Frase di 3 s da tagliare dalla voce o riscrivere (serve la master).
4. **Testa nell'originale:** in alcuni momenti il capo tocca il bordo alto della webcam dell'originale (es. originale 5:00, nel video nuovo 5:44): non è recuperabile.
5. **Voci M2 e M3**: il servizio le ha segnate «DA CONTROLLARE» (parole diverse 4/6 e 5/5); velocità di lettura normale (2,0–2,3 parole/s). Non le ho ascoltate.

## Cosa NON ho potuto verificare
- **Ascolto vero e proprio.** Whisper non è scaricabile dalla rete della chat (modello bloccato) e io non posso ascoltare l'audio. Ho quindi usato: il `.vtt` esistente (fatto da Whisper sul video finale), i testi delle voci Kore, misure ffmpeg (volume, silenzi, offset) e l'allineamento audio. I sottotitoli del prof sono corretti **per contesto** (slide del prof, testi, nomi); i passaggi dubbi sono nell'elenco sopra. La master deve riascoltare 3 punti: 0:50, 25:00, 42:30.
- **Rumore del prof:** il parlato ha già il passa-alto a 80 Hz (energia < 60 Hz −9,6 dB rispetto all'originale), ma il modello `arnndn` citato nelle regole non è nel kit e non ho potuto fare un ascolto: non ho rifatto l'audio del prof.
- **Tempi dei sottotitoli di voci Kore** (benvenuto, ripassi, glossario, mappe): calcolati sul parlato reale (pause misurate) ma non con allineamento forzato: stima ±0,3–0,5 s.
- **Tempi di apparizione** delle card negli approfondimenti: presi dal video vecchio (eventi di cambio immagine), stima ±1 s.
- Pagine del libro: **la lezione 26 non ne ha** (B-bis non si applica).

## Come è stato rifatto (breve)
Audio: lo stesso del video approvato (voci Kore e prof già a −16 LUFS), con le 6 voci nuove delle mappe (normalizzate a −16 LUFS) e il finale del kit. Video: 45 pagine nuove generate in grafica Spagnolo, sincronizzate agli stessi istanti (scene vecchie solo per sigla e schede quiz/titolo, con dissolvenze); prof dall'originale (`Letteratura_Lez26.mp4`, release `mazzotti-letteratura-V`), 5 pezzi continui allineati sull'audio.

## File consegnati
`Letteratura_Lez26_Parte1_1080p.mp4.parte_00..02` + `.sha256` · `Letteratura_Lez26_Parte1.vtt` · `Letteratura_Lez26_slide.pdf` · `Letteratura_Lez26_mappe.pdf` · `Quiz_Letteratura_Lez26.txt` · `quiz_argomenti.json` · `Verifica_finale_Letteratura_Lez26.xlsx` · `compiti.json` · `scheda_pubblicazione.json` · `testo_youtube.txt` · `controllo_minuti.jpg` (1 fotogramma ogni 30 s). Ricomporre: `cat Letteratura_Lez26_Parte1_1080p.mp4.parte_* > Letteratura_Lez26_Parte1_1080p.mp4 && sha256sum -c Letteratura_Lez26_Parte1_1080p.mp4.sha256`.
