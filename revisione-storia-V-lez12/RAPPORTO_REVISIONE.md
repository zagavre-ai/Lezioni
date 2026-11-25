# RAPPORTO DI REVISIONE · Storia V · «L'Europa e il mondo negli anni Trenta» · correzioni 22/11 (Prof. del materiale)
23/11/2026 · ramo `revisione-storia-V-lez12` · sostituisce la consegna precedente · 2 Parti. Etichette: **M** misurato, **S** letto a vista, **NV** non verificato.

## 1. Struttura e misure
- 6 argomenti, uno per pagina di slide del prof. **Parte 1** (sigla, copertina, intro del prof 168,6 s, «Di cosa parliamo», argomenti 1-4): 41,2 min, 362 MB. **Parte 2** (sigla, copertina, **spiegone** della Parte 1, argomenti 5-6, glossario, ripasso finale, mappe, verifica, sigla finale, compiti): 30,0 min, 265 MB. Divisione scelta con la master (69,6 min > 65): **nessuna Parte arriva a 50 min, il materiale del prof non basta (M)**.
- Formato (M): 1920×1080, 30 fps, x264 veryfast CRF 19, AAC 192k 48 kHz. Volume P1 -16.5 LUFS, P2 -16.4 LUFS; picchi -2.3 e -2.5 dBTP.
- `controllo_rapido.py` della master: **ESITO OK (P1), OK (P2)**; fogli e json accanto ai video. `controllo_severo.py`: tutte le voci a posto tranne la durata < 45 min (M, vedi sopra).
- Scatto del jingle di ogni scheda Quiz (`controllo_jingle.py`, M): Q1-Q6 scarto +0,009…+0,011 s (accettato ≤ 0,05).
- Nessuna pausa muta oltre 2,5 s (M, silencedetect −45 dB). Dissolvenza 0,5 s + `trans.wav` a ogni cambio di pezzo.
- Voce del prof (M): rapporto energia > 4 kHz / > 100 Hz = −16,6 dB nell'originale, −16,3 dB (P1) e −17,2 dB (P2) nel montato: timbro intatto (limiti −9/−20). Solo filtro dei bassi (70 Hz) e riduzione leggera del rumore; originale mai modificato.
- Sincronia labbra/voce: webcam e audio escono dallo stesso file originale con gli stessi tagli a fotogrammi interi (scarto teorico 0 s, **NV** non misurato con strumento).
- Webcam (S): nell'originale è solo 185×138 px (riquadro 246×139 in un video 1092×614): è ingrandita 2,2× nel 4:3 e resta morbida. Limite del file del prof.
- Fermi immagine del prof ≥ 1 s: nessuno (S, `freezedetect` dell'agente separato ≥ 20 s: nessuno).

## 2. Tabella delle fine dei pezzi del prof (frase finita, trascrizione)

**Parte 1**

| Pezzo | Inizio (min) | Fine (min) | Ultime parole del prof | Frase finita |
|---|---|---|---|---|
| prof0 | 0:22.1 | 3:10.7 | …osì, un'espansione sempre più solida del fascismo in Europa. | sì |
| prof1 | 3:47.3 | 13:04.2 | …e, portarono alla fine delle esperienze del fronte popolare. | sì |
| prof2 | 14:43.9 | 23:07.1 | …era per quello, però anche per espandere l'impero. | sì |
| prof3 | 25:12.0 | 26:54.0 | …E adesso spostiamoci. | sì |
| prof4 | 28:22.5 | 39:18.3 | …uesto punto le varie zone contese crollano tutte, d'accordo? | sì |

**Parte 2**

| Pezzo | Inizio (min) | Fine (min) | Ultime parole del prof | Frase finita |
|---|---|---|---|---|
| prof5 | 2:00.0 | 7:28.0 | …Bene. | sì |
| prof6 | 8:54.0 | 24:02.4 | …Da una parte e dall'altra. Ma lo faremo! | sì |

I pezzi cominciano 0,25-0,9 s prima della frase, nel silenzio. Pause oltre 2,5 s accorciate a ~1 s. L'**ultima parte dell'introduzione** del prof (169,6-196,0 s dell'originale, 27 s) non entra nei 3 minuti sopra la copertina: passa all'inizio dell'argomento 1, sulla slide dell'argomento (la prima card si accende alla prima frase sui fatti del Regno Unito).

## 3. Scelte e punti da far confermare alla master
1. **Mappe** (prompt 22/11 e risposte della master): solo le 3 mappe del prof (Autoritarismo, Guerra civile spagnola, Hitler), ridisegnate in vettoriale, colori BES con legenda, costruite ramo per ramo con la voce Kore, mappa intera ferma 4 s. Gli argomenti 1, 3 e 5 non hanno mappa e si chiudono con la pillola di ripasso. **La mappa 3 non ha titolo-domanda: «Che cosa fa Hitler prima della guerra?» è scritto da me con le parole del prof (dichiarato).** Mappa finale della lezione: le 3 mappe del prof in sequenza (il prof non ne ha una unica).
2. **Anomalie del materiale del prof** (riportate come le dice lui): la mappa dice «i Sudeti (1939)», slide e voce dicono 1938; etichetta «Patto di ferro italo-tedesco» ma testo «Patto d'acciaio»; titolo «il fallimento di Locarno» ma il testo non cita Locarno; «Austria (Dollfuss)» elencata tra i Balcani; la carta del libro dice «circa 12.000 km» per la Lunga marcia, slide e voce dicono 10.000; la slide cita «URSS» (nelle nostre card: «URSS, cioè l'Unione Sovietica»); «Comintern» spiegato sulla mappa e a voce.
3. **Refusi corretti nelle nostre slide** (la master li ricontrolla): iniziali maiuscole all'inizio di ogni card, «Jugoslavia/Iugoslavia» come nelle slide e nella mappa; nessun altro refuso trovato nelle slide (nomi: Piłsudski, Horthy, Béla Kun, Salazar, Estado Novo, Getúlio Vargas, Guomindang, Chiang Kai-shek, Manchukuo, Shaanxi, alzamiento, Appeasement, Anschluss).
4. **Immagini del prof → argomento (una sola)**: carta «Lunga marcia» (Asia) → arg. 3; foto di Franco e carta della guerra di Spagna → arg. 4. La carta dell'espansione tedesca (pagina 11 del PDF) non è mai mostrata dal prof nel video: compare solo nell'approfondimento dell'arg. 6. Le immagini sono state ingrandite 3× con pulizia e nitidezza leggere (S: restano della qualità del PDF del prof, ≤ 806 px: ingrandimento, non nuova risoluzione). Le miniature dentro agli approfondimenti mostrano la pagina intera del prof (con il suo QR) e sono piccole: **limite noto**, già segnalato dall'agente separato.
5. **Card**: max 3 per slide, intere, iniziale maiuscola, 40 px, interlinea 1,45; finestre che cambiano ogni ≤ 165 s con numero di pagina nuovo; nel secondo argomento (Dittature) la «digressione» del prof sulla Spagna 1931-36 (990-1126 s) è mostrata con la card «Le premesse» (compare solo qui). Card «Appeasement» nell'argomento 5 perché il prof ne parla lì.
6. **Quiz**: 5 domande per argomento scritte da me dal materiale del prof (`quiz_argomenti.json`), **da approvare dalla master**; verifica finale = le 10 domande dell'Excel del prof con gli spazi iniziali/finali tolti (refuso); compiti = 4 del prof, testo invariato. Schede con «Rispondi · premi Controlla · poi Continua».
7. Voci: Kore della master (ramo `voci-storia-V-lez12`). Difetti trovati nelle voci consegnate e **corretti con taglio a bordo frase**: A2 (leggeva ad alta voce le istruzioni di stile prima del testo: tagliati i primi 19,2 s), A1 e A6 (frase iniziale ripetuta: tagliati 3,55 s e 3,2 s), I1 (due frasi in più rispetto al testo approvato: tenuta solo la prima, 5,7 s). **Aggiornamento 25/11: arrivate `I3_BENVENUTO2` (benvenuto della Parte 2) e `C3_COMPITI_CHIUSURA`; montate. La scheda compiti ora legge con la voce Kore i 4 compiti (uno alla volta, bordo giallo) e chiude con «Svolgi i compiti qui sotto e premi Consegna: arrivano al docente nel tuo quaderno dei compiti.» a voce e sullo schermo. Parte 2 rifatta e `controllo_rapido.py` rilanciato su entrambe le Parti: OK, OK.** A1 dura 60,5 s (limite 60 s, tolleranza di 0,5 s).
8. Sottotitoli: prof da trascrizione automatica con correzioni dei termini principali (Mosley, appeasement, Anschluss, Béla Kun, Primo de Rivera, numeri); **NV: non riletti per intero, possibili altri errori di riconoscimento**. Voci Kore: testo noto, tempi per frase.

## 4. Voci Kore: confronto con il testo (trascrizione automatica, M)
| Voce | Durata (s) | Somiglianza con il testo | Bordo finale (max, <0,03) | Differenze principali (trascrizione automatica) |
|---|---|---|---|---|
| I1_BENVENUTO | 5.7 | 0.692 | 0.002 | videolezione → video lezione; mondo negli → mondi; trenta → 30 |
| I3_BENVENUTO2 | 5.7 | 0.692 | 0.002 | videolezione → video lezione; mondo negli → mondi; trenta → 30 |
| I2_ARGOMENTI | 32.0 | 0.945 | 0.000 | quarto → ; millenovecentotrentasei → 1936; millenovecentotrentanove quinto → 1939 |
| A1_APPROF | 60.5 | 0.956 | 0.000 | millenovecentotrentuno → 1931; domini → dominia; millenovecentoventinove → millovecentoventi nove |
| A2_APPROF | 51.6 | 0.912 | 0.001 | in → ; millenovecentoventisei → 1926; j zef pi sudski → jozef pilski |
| A3_APPROF | 50.8 | 0.918 | 0.001 | millenovecentotrentuno → 1931; manchukuo → manciuko; millenovecentotrentasette → 1937 |
| A4_APPROF | 52.1 | 0.947 | 0.001 | millenovecentotrentasei → 1936; è → ; alzamiento → alziamento |
| A5_APPROF | 47.5 | 0.964 | 0.001 | millenovecentotrentatré → millovecentrenta; millenovecentotrentacinque → 1935; millenovecentotrentasei → 1936 |
| A6_APPROF | 54.8 | 0.946 | 0.000 | le tappe → ; millenovecentotrentotto → 1938; è → e |
| P1_PILLOLA | 28.3 | 0.932 | 0.000 | millenovecentotrentuno → 1931; quarto → ; millenovecentotrentasei → millovecentrentaisei |
| P2_PILLOLA | 31.9 | 0.821 | 0.001 | millenovecentoventisei pi sudski → 1926 piulsudzki; horthy → horti; regimi → negimi |
| P3_PILLOLA | 26.7 | 0.857 | 0.001 | millenovecentotrentuno → 1931; manchukuo → manciuquo; millenovecentotrentasette → 1937 |
| P4_PILLOLA | 28.4 | 0.892 | 0.000 | millenovecentotrentuno → 1931; millenovecentotrentasei → 1936; terzo →  |
| P5_PILLOLA | 27.6 | 0.914 | 0.000 | millenovecentotrentatré → 1933; millenovecentotrentacinque → 1935; quarto →  |
| P6_PILLOLA | 29.1 | 0.851 | 0.000 | millenovecentotrentotto → 1938; sudeti → sudi; millenovecentotrentanove → 1939 |
| M2_MAPPA | 25.7 | 0.957 | 0.001 | iugoslavia → jugoslavia; comintern → cominter |
| M4_MAPPA | 17.0 | 1.0 | 0.001 | — |
| M6_MAPPA | 24.8 | 0.947 | 0.002 | che → ; millenovecentotrentotto → 1938; millenovecentotrentanove → 1939 |
| G1_GLOSSARIO | 57.9 | 0.854 | 0.002 | glossario → glussario; millenovecentotrentuno → 1931; estado novo → è stato nuovo |
| R1_RIPASSO_FINALE | 48.9 | 0.912 | 0.001 | dittature → ; manciuria → manchuria; dal colpo →  |
| F1_MAPPE_FINALE | 9.9 | 1.0 | 0.000 | — |
| V1_VERIFICA | 7.4 | 0.857 | 0.001 | ottanta per cento → 80 |
| C1_COMPITI_INTRO | 1.2 | 1.0 | 0.004 | — |
| C2_COMPITI | 86.6 | 0.943 | 0.001 | riforme introdotte → rifor introdot; millenovecentotrentasei → 1936; descrivi → scrivi |
| S1_SPIEGONE | 88.7 | 0.916 | 0.001 | millenovecentotrentasei → 1936; léon → lyon; quaranta → 40 |

Le differenze «cifre vs lettere» (1936 / millenovecentotrentasei) sono la trascrizione automatica, non errori. **NV: non ho ascoltato le voci (neanche per la pronuncia di Piłsudski, Estado Novo, Manchukuo, Léon Blum, Croix de Feu: la trascrizione automatica li ha sentiti come «piulsudzki/jozef pilski», «è stato nuovo», «manciuko/manciuquo», «lyon», quindi la pronuncia di questi nomi va ascoltata da una persona)**: pronuncia di nomi stranieri (Piłsudski, Estado Novo, Manchukuo, Léon Blum, Croix de Feu, Guernica…) e che nessuna voce dica il nome del prof (nei testi inviati non compare mai). Bordi finali tutti sotto 0,03 (M); dissolvenza di 30-40 ms in montaggio.

## 5. Controllo dell'agente separato (non ha montato la lezione)
Verificati e a posto: nome del prof solo nella fascia gialla (nessun «Mazzotti/Giorgio» in sottotitoli, dispensa, mappe); 1920×1080, 30 fps, fotogrammi = durata×30, < 400 MB; copertina col titolo esatto; intro del prof 168,6 s; sigla finale con avviso; mappe uguali per struttura e parole a quelle del prof (confronto col PDF); card intere e accensioni a campione (scarto ≤ ~1 s); nessun fermo ≥ 20 s.
Difetti segnalati e **non corretti (tempo)**: (a) 3:47-4:55 di P1 slide dell'arg. 1 mentre il prof finisce l'introduzione; (b) filler «Um» all'inizio del pezzo dell'arg. 4 (0,8 s); (c) miniature piccole nelle schede di approfondimento (AP3, AP4, AP6, spiegone) e AP1 senza immagine; (d) titoli che vanno a capo «extra-/Europa», «(1936-/1939)»; (e) tail silenzioso di ~1,7 s nei titoli e ~2 s nei quiz dopo il jingle (< 2,5 s); (f) copertina della dispensa e del PDF mappe senza l'elenco ARGOMENTI (regola §9: solo materia e titolo). Corretti dopo il controllo: sottotitoli (termini).
**NV**: ascolto delle voci, sincronia labbra misurata, glossario/ripasso/pillole nel dettaglio, ogni sigla rispiegata, «già visto» a occhio.

## 6. Dispensa e mappe
`Storia_Lez12_Parte{1,2}_dispensa.pdf` (A4 orizzontale, stesse slide del video senza riquadro e senza nome del prof, numero di pagina del video, strato di testo invisibile verificato con pdftotext) e `Storia_Lez12_mappe.pdf` (copertina «MAPPE» + 3 mappe). Piè di pagina: solo «STORIA» e «Pagina N».

## 7. File
Video a pezzi da 90 MB con `.sha256`; `.vtt`; `timeline_ParteN.json`; `scheda_pubblicazione_ParteN.json` (rigenerati sul video finale); `quiz_argomenti.json`, `verifica_finale.json`, `compiti.json`; dispense e mappe; fogli dei fotogrammi e json del controllo rapido.
Ricomporre: `cat Storia_Lez12_ParteN_1080p.mp4.parte_* > Storia_Lez12_ParteN_1080p.mp4` e `sha256sum -c`.
