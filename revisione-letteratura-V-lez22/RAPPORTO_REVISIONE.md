# RAPPORTO REVISIONE · Letteratura italiana V · Lezione 22 · Elsa Morante
Revisione del 16/11/2026. Video corretto: `Letteratura_Lez22_Parte1_1080p.mp4` (a pezzi `.parte_00…02`, sha256 nel file `.sha256`; unito e controllato).
Etichette: **misurato** = misurato con uno strumento · **stima** = dedotto · **non verificato** = non ho potuto.

## 1. Misure sul video nuovo (misurato)
| Controllo | Risultato |
|---|---|
| Formato | 1920×1080, 30 fps, x264 veryfast (sigle e schede CRF 17-18, pezzi col prof CRF 20), AAC 192k 48 kHz |
| Durata / fotogrammi | 51:04,6 (3064,6 s) · **91 938 fotogrammi = identici al montaggio vecchio**. La somma dei 65 pezzi è uguale (controllata pezzo per pezzo) |
| Peso | 280,2 MB |
| Volume | −16,3 LUFS integrato (LRA 5,8 LU). Picco (true peak) **−1,2 dBTP** (richiesto ≤ −1) |
| Scatto dei Quiz | `controllo_jingle.py` sul video nuovo: Q1…Q5 a **0,000 s** di scarto. Il file del jingle l'ho trovato in `Telesio_kit_produzione_v5_aggiunta.zip` (`home/claude/v5/snd/quiz.wav`) |
| Posizione di quiz, verifica, compiti | **invariata**: Quiz a 11:28 · 21:34 · 33:10 · 42:30 · 48:41; verifica 50:40; compiti 50:56 (come prima, i link Vimeo restano validi) |
| Fermi immagine del prof (riquadro, ≥ 1,5 s, dentro i pezzi D1–D5) | **nessuno** (misurato con `freezedetect`, scansione completa dei 51 minuti: 115 fermi, tutti sulle slide senza prof). L'unico fermo del prof è l'introduzione 0:15–0:49 (voce di benvenuto con la foto del prof, come prima) |
| PDF | slide: **85 pagine** A4 orizzontale; mappe: 1 pagina A4 orizzontale |
| Sottotitoli | 828 cue, **max 2 righe**, nessuna sovrapposizione; scarto mediano rispetto al parlato 0,25 s (90° percentile 0,39 s) misurato su 771 cue |

## 2. Confronto col modello Spagnolo (punto 000)
| # | Punto | Esito |
|---|---|---|
| 1 | Sigla 15 s → dissolvenza → copertina | **corretto**: sigla del kit (invariata) + dissolvenza di 0,4 s (era un taglio) |
| 2 | Copertina (logo, «LETTERATURA ITALIANA V · VIDEOLEZIONE», titolo, card ARGOMENTI su 2 colonne) | **corretto** (era titolo + elenco) |
| 3 | Slide: fondo bianco, «01 · ARGOMENTO», titolo + barretta, card | **corretto** (era fondo azzurrino, card a bordo giallo). Tabelle: non ce ne sono in questa lezione |
| 4 | Piè di pagina «LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti» + «Pagina N» | **corretto** (mancava la «V»; ripassi avevano «RIPASSO» al posto del numero) |
| 5 | Riquadro 4:3 con ombra grigia, niente bordo | **corretto**: 412×309 px, x=1428 y=148, angoli r=18 (era un tondo di ≈150 px) |
| 6 | Fascia gialla −3°, due righe | **corretto**: «Giorgio Mazzotti» / «PROF. DI LETTERATURA ITALIANA», sempre visibile sulle slide col prof |
| 7 | Slide senza prof | **corretto**: approfondimenti, linee del tempo, parole chiave, schede, ripassi, glossario, riepilogo, Quiz, Verifica, Compiti, Fine rifatti su fondo bianco, giallo solo sulla parola o frase in corso |
| 8 | Font | Bricolage Grotesque 800 (titoli), Figtree (testo ed etichette, Bold maiuscolo spaziato). DM Mono non usato, come da correzione della master. A vista, confrontato con `slide_1080p_esempio.png` |
| 9 | Finale 5 s con avviso diritti | **OK**: uso direttamente `Sigla_finale_5s_con_avviso_diritti.mp4` (prima l'avevo trovata ricostruita) |
| 10 | Struttura | OK: sigla → presentazione → 5 argomenti (titolo, prof, approfondimenti, mappa, ripasso, schema, quiz) → glossario → riepilogo → verifica → fine → sigla finale → compiti. Nota: «Verifica finale» e «Compiti» restano nel video come schede di servizio (stessi secondi di prima) |
| 11 | PDF slide + mappe A4 orizzontale | consegnati. Confronto fatto su 10 pagine del PDF contro il fotogramma del video: differenza media 1,8–4,5 su 255 (solo la card gialla in corso) |

## 3. Problemi trovati e correzioni
| Minuto (video) | Tipo | Com'era | Correzione |
|---|---|---|---|
| tutto | visivo | prof in un tondo; fondo azzurrino; grafica diversa dal modello | tutto rifatto nel modello (punti 1-8) |
| 6:39 (D1→AN1) e 11:37 | **audio** | il pezzo del prof si interrompeva **nel mezzo di una frase**: «Nel frattempo lei continua [stacco di 5 min] a scrivere. Il debutto…» (parole «a scrivere» spostate dopo l'inserto) | il taglio passa ora dopo «a scrivere.» (orig. 346,93 s). Compensato togliendo 1,13 s di pausa all'inizio di AN1 e aggiungendoli all'inizio di AN2: **quiz e tutto il resto restano agli stessi secondi** (misurato) |
| 10:30 e 20:00, 31:30, 41:00, 47:30, 49:00 | visivo/contenuto | 6 «mappe concettuali» disegnate da noi (nodi inventati, p.es. «La famiglia / La voce narrante») | sostituite con **la mappa del prof** (`LEZIONE 22.pdf`, release), nodi identici, nostra grafica. I 5 rami per argomento mostrano i nodi del prof relativi; la mappa finale la mostra intera. La voce è nuova (MM1–MM5, MMF, Kore, generate dalla master) perché la vecchia descriveva nodi inventati |
| 10:30–11:30 | audio | voce MP1 vecchia diceva «Quinto ramo… racconti», «Ultimo ramo: malattia e morte» ecc. non presenti nella mappa del prof | vedi riga sopra |
| MM4, MM5 | audio | le voci nuove durano 31,6 s e 32,5 s per slot da 43 s: sarebbero rimasti 10 s di silenzio | pause fra le frasi allungate (≤ 1,6 s ciascuna); MMF (55,2 s per uno slot da 52,2) accelerata del 7,8 % |
| D1…D5 | sincronia | evidenziazione delle card «a occhio»; pagine cambiavano fino a 33 s dopo il parlato (p. «Il matrimonio» da orig. 270 s invece di 237 s; «Poesia e racconti» 433,8 s invece di 426 s; «Ida, Nino e Useppe» 1192 s invece di 1176 s) | pagine e card accese dal **parlato del prof** (trascrizione con tempi parola per parola), ±1,5 s (stima: i tempi delle card li ho fissati leggendo la trascrizione; **non ho ricontrollato ogni card all'ascolto**) |
| D1 0:54–2:23 | visivo | nessuna slide ferma >60 s col prof passato ad altro | controllato: la copertina con gli argomenti resta 88 s mentre il prof presenta la lezione (è il suo parlato introduttivo); la prima slide di contenuto parte a 2:23 |
| fine | consegna | schede «Quiz», «Verifica finale», «Compiti», «Fine» con bande blu laterali e fondo scuro | rifatte nel modello (bianche, senza bande) |
| 50:56 | consegna | compiti: `compiti.json` con la chiave `compiti` e tipo `risposta_aperta` | formato `{"titolo","esercizi":[{"n","tipo":"aperta","testo"}]}`; testo uguale al PDF del prof (confrontato: 4/4 identici) |
| scheda | testo | titolo «Elsa Morante» | «Letteratura V · Lezione 22 · Elsa Morante» |
| vtt | testo | 606 cue; es. «una belle poche scrittrici», «El Samorante», «menzogni e sortileggio», «Aracivi/Aracelli», «Guseppe», «Raamundo», «Gerate», «Vilheim», «le lotto operai», «ti spetti» | 828 cue riscritti: parlato del prof dalla trascrizione con ≈60 correzioni di nomi e termini; voce narrante dal testo esatto (cifre in numeri). Tempi riallineati |
| audio prof | audio | l'audio del prof non era dimostrabilmente pulito | rifatto **dall'originale** con `aresample 48000, highpass 80, arnndn (sh.rnnn del kit), loudnorm, alimiter`, poi −2,4 dB: −16,3 LUFS finali, picco −1,2 dBTP; stessi offset |
| verifica | consegna | non c'era `verifica_finale.json` | creato dalle 10 domande dell'Excel del prof (`DOMANDE LEZIONE 22.xlsx`), copiato l'xlsx |
| quiz | contenuto | — | riletti i 25 quiz contro le slide del prof: coerenti, 5 per argomento, 1 giusta e 3 sbagliate. Invariati |

## 4. Pagine del libro in alta risoluzione (B-bis)
La lezione 22 non ha pagine del libro (elenco di regola 1.B-bis): **non applicabile**.

## 5. Cosa NON ho verificato / limiti
- **Ascolto umano: non ho ascoltato nulla.** Non verificati all'orecchio: fruscio, ronzio, «metallico» dopo la pulizia; la pronuncia della voce Kore (confronto trascrizione↔testo: nessuna differenza oltre ai nomi propri che la trascrizione automatica sbaglia di per sé, ma **non è una prova**); i punti d'attacco fra voce e musica. Da ascoltare in almeno 3 punti: 12:00, 25:00, 47:00 (prof) e 10:40, 20:20, 49:10 (voci nuove).
- **Sincronia labbra:** non verificata (webcam 247×139 px nell'originale).
- **Testa tagliata:** la webcam originale (247×139) è ritagliata in 4:3 (185×139) e ingrandita 2,2×: l'immagine è morbida. Nell'originale i capelli toccano il bordo alto in diversi punti (es. orig. 1:40, 4:00): **non risolvibile**.
- **Evidenziazioni delle card e fettine automatiche:** calcolate con la trascrizione automatica (Parakeet); scarto atteso ±1–2 s; **non ricontrollate card per card all'ascolto**. Le evidenziazioni nei pezzi voce+schede (approfondimenti, ripassi, schemi, mappe) vengono dalla voce e dai tempi del video vecchio (1 s di risoluzione).
- **Testi degli approfondimenti (linee del tempo, parole chiave, schede):** letti dal video vecchio con OCR e riletti a vista solo in parte (circa 10 pagine su 28); alcuni testi li ho corretti a mano, altri **non confrontati parola per parola** con il prof.
- **Sottotitoli del prof: non riletti cue per cue contro l'audio.** Ho riletto tutto il testo contro la trascrizione e corretto nomi e termini evidenti. Rimangono cue dubbi (parola non decifrabile, lasciata com'è): 6:34 «passano insieme velità» (forse «vent'anni»); 6:07–6:12 «è rimando… corso di storia»; 23:35 «in un'isolita»; 34:47 «Roma diata»; 35:54 «Tupro»; 37:40 «questa effecta»; 42:46 «il coe»; 26:08 «Medium età». Il testo del prof è fedele al parlato (esitazioni «Mm/Um» tolte, il resto no).
- **Mappa del prof nel video:** l'ho inserita **senza cambiare la durata** (decisione della sez. 5: se la durata resta uguale la si inserisce). Il prof ha dato **una sola mappa** per la lezione: i 5 «rami» per argomento mostrano la stessa mappa con i nodi relativi in evidenza. Decisione a Sara se preferisce un'unica mappa a fine lezione.
- **Controllo fettine:** n/a (nessuna pagina del libro).

### DA CONFERMARE COL PROF
- **Separazione da Moravia:** il prof nel parlato dice «1962»; la sua **mappa** dice «1961». Nel video, linea del tempo e slide dicono 1962 (come il parlato); la mappa e la voce MM1 dicono 1961 (come la mappa). Lasciato così: decide il prof.
- **«Pro o contro la bomba atomica»:** nel parlato «volume uscito postumo… del 1987»; nelle slide «1965» è l'anno dell'intervento. Non in conflitto, ma la card p. 20 lo può far credere.
- **Alibi (1958) e Il mondo salvato dai ragazzini (1968):** coincidono tra parlato e mappa. Nessuna differenza.

## 6. Come ho verificato
Trascrizione completa (Parakeet TDT via `trascrivi.py`) dell'originale (292 segmenti) e del video vecchio e di quello nuovo (671 segmenti); 3065 fotogrammi a 1/s sul video vecchio e OCR (rapidocr + tesseract); piano di montaggio contiguo (65 pezzi = 91 938 fotogrammi, identico al vecchio); 103 fotogrammi a 1/30 s sul video nuovo (`controllo_minuti.jpg`); `ebur128` per volume e picco; `silencedetect` (silenzi > 2,5 s: solo schede di servizio e cartelli di argomento da 5 s — Quiz, T1…T5, Verifica, Compiti — **invariati rispetto al montaggio vecchio**; sono silenzi di 3–4 s e non li ho accorciati per non spostare i secondi dei quiz); `controllo_jingle.py`; confronto PDF slide ↔ video su 10 pagine.
Correzione del confine D1/D2 verificata sull'energia del segnale: parlato a 399,2–399,5 s («continua») e 400,2–400,6 s («a scrivere») del video nuovo; poi attacca la voce narrante a 401,0 s.
