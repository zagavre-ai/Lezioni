# Compito: sotto-slide a card per UN argomento di Storia V lez18 (Prof. Mazzotti, L'Italia repubblicana)
Materiali (sola lettura): /home/user/work18/lavoro-storia-V-lez18/asr18.txt (trascrizione «secondi_originale|frase» del prof, riconoscimento automatico, con errori e incespicamenti),
/home/user/work18/lavoro-storia-V-lez18/slides18.json (testo delle slide del prof), /home/user/work18/lavoro-storia-V-lez18/trasc18.json (stessa trascrizione, con parole e tempi).
Il video del prof dura 4274 s. Argomenti (secondi dell'originale): intro 0-187 (copertina) · arg1 187-879 · arg2 879-2030 · arg3 2030-2098 · arg4 2098-~2940 · arg5 ~2940-3552 · arg6 3552-4274.
I confini esatti si fissano sulla trascrizione: ogni argomento comincia/finisce a inizio/fine di una frase completa. Il prof ha slide con 3 paragrafi per argomento ma parla 10-19 minuti: servono molte sotto-slide.

## Cosa produrre: un file JSON /home/user/work18/cards/<nome>.json
{"arg":N,"t0":sec_inizio,"t1":sec_fine,
 "kw":["parola chiave 1",... max 5 in tutto per l'argomento, brevi, in italiano],
 "finestre":[{"t0":..,"t1":..,"kw_on":[indici in kw accesi],"card":[{"t":sec_inizio_frase,"testo":"..."}, ... da 1 a 3 card]}, ...],
 "pausa_AN":sec (fine di una frase, tra il 40% e il 60% dell'argomento, dove inserire l'approfondimento animato),
 "note":"anomalie, dubbi, nomi/numeri che non tornano"}
Regole (vincolanti, dal CLAUDE.md del progetto):
1. Le finestre coprono l'argomento senza buchi (t1 di una = t0 della successiva) e **ogni finestra dura al massimo 140 s**. Al massimo 3 card per finestra (2-3 di norma; 1 sola solo se la frase è lunga).
2. **Ogni card è UNA FRASE INTERA detta dal prof** (o un punto intero detto da lui, anche unendo due pezzi contigui della stessa frase), con le sue parole: togli solo incespicamenti, ripetizioni e riempitivi («cioè», «diciamo così», «d'accordo?», «ecco»), correggi ortografia, accenti, maiuscole dei nomi propri e le parole mal riconosciute. Mai riassunti, mai parole tue, mai «…», mai iniziale minuscola. Una card si legge da sola: frase compiuta, con soggetto chiaro. **Massimo 150 caratteri per card** (se la frase del prof è più lunga scegli la frase più corta che esprime il punto, non tagliarla a metà).
3. «t» = secondo (dell'originale, dalla trascrizione) in cui il prof COMINCIA quella frase. Le card di una finestra sono in ordine di tempo, e i t cadono dentro la finestra. Una finestra comincia (t0) un po' prima della prima card (0-3 s) e finisce dove finisce la sua ultima card/frase seguente.
4. Scegli le frasi che portano contenuti storici (fatti, nomi, date, numeri) e che il prof dice davvero; evita aneddoti confusi. Numeri e nomi come li dice il prof (non fare calcoli; se qualcosa non torna con la storia reale, tienilo come lo dice e scrivilo in «note»).
5. Sigle: ogni volta che compare una sigla nella card (DC, PCI, PSI, CLN, NATO, CECA, ENEL, INA-Casa, ecc.) va rispiegata nella card stessa («DC, cioè Democrazia Cristiana»); se non entra nei 150 caratteri usa il nome per esteso senza sigla.
6. Niente nome del docente. Niente numero di lezione.
7. kw_on: gli indici delle parole chiave pertinenti alla finestra (0-2 per finestra).
Consegna: scrivi il file, poi rispondi con 3 righe: file, numero finestre, anomalie principali. Non scrivere altro in chat.
