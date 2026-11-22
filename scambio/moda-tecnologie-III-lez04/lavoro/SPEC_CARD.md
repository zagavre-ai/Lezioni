# Specifica: card e materiali per UN argomento della lezione (Prof.ssa Piera Caputi, Tessitura pt.1)

Sei un redattore. NON montare video. Produci SOLO i file indicati sotto, leggendo:
- `/home/claude/prod/lez04/frasi_auto.json` (frasi della prof con tempi t0/t1 in secondi del VIDEO SORGENTE; il testo è una trascrizione automatica CON ERRORI)
- `/home/claude/lez04/trascr.txt` (stessa trascrizione per segmenti, con tempi)
- `/home/claude/lez04/pdf.txt` (il PDF della prof: fonte di verità per termini, nomi, misure, ortografia)
- Esempio di formato card: `/home/claude/prod/a1_cards.py` (argomento 1, già fatto). Leggilo.
- Regole: `/home/user/Lezioni/scambio/caputi/REGOLE_BLINDATE.md` (§2, §4, §5, §6, §8) e `/home/user/Lezioni/scambio/caputi/PROMPT_Caputi.md` (§3).

## 1. Card (file `/home/claude/prod/lez04/topics/A{N}.py`, variabile `S` come in a1_cards.py)
- Ogni slide: 'title' (breve, ≤45 caratteri, una riga), 'chips' (≤5 parole chiave DELLA PROF), 'cards': lista di (t_sorgente_inizio_frase, html). **Al massimo 3 card per slide.** Una slide dura finché la prof parla delle sue 3 card: una nuova slide ogni ~25-60 s di parlato, MAI più di 90 s senza cambio di slide.
- Ogni card = UNA frase intera di quello che dice la prof, ripulita: via riempitivi («diciamo», «in ogni caso», «ovviamente», «in realtà», «comunque», «appunto»), via ripetizioni e incespicamenti; errori della trascrizione corretti con il PDF (es. brille→briglie, jacard→Jacquard, saglia→saia). **Non aggiungere nulla che la prof non dica. Non riassumere cambiando il senso. Misure e numeri come li dice lei, senza calcoli.** Frasi complete, mai spezzate con «…», mai iniziali minuscole che continuano la card prima. Una card = 1–2 righe (≤ 150 caratteri).
- Parole importanti in `<b>…</b>`. Niente altri tag.
- Il tempo di ogni card è l'INIZIO della frase parlata (±1 s): verificalo su frasi_auto/trascr.txt. I tempi devono crescere.
- **Ogni sigla o termine tecnico si spiega ogni volta che compare**, sullo schermo: es. «UE, cioè Unione Europea», «R.G.T., cioè Rappresentazione Grafica Tremelloni», «E, cioè finezza inglese». Usa solo spiegazioni che vengono dal PDF/dalla prof.
- Niente numero di lezione; niente parole straniere nelle grafiche salvo termini tecnici del PDF (taffetas, satin, jacquard, jersey…).
- Frasi di riempimento puro, esitazioni e frammenti senza contenuto («Good.», «Foi.», «Quindi») NON diventano card.

## 2. Altri materiali (file `/home/claude/prod/lez04/topics/A{N}_extra.json`)
```
{
 "T0": inizio_s, "T1": fine_s,          // estremi del pezzo della prof per questo argomento, in secondi del sorgente, scelti TRA due frasi (mai a metà frase); cerca il confine giusto in frasi_auto
 "tecniche": [ {"t":sec_sorgente, "durata":sec, "cosa":"descrizione precisa dell'animazione da mostrare SOPRA la voce della prof, fatta solo di quello che lei dice in quel momento (es. 'ordito verticale e trama orizzontale che si intrecciano, con navetta')", "parole":"le sue parole esatte in quel punto"} ],  // 2-5 momenti tecnici/complicati dell'argomento: processi, strutture, macchine, classificazioni
 "quiz": [ {"d":"domanda","giusta":"...","sbagliate":["...","...","..."],"spiegazione":"..."} ],   // ESATTAMENTE 5 domande sull'argomento, solo dal PDF/prof; 1 giusta e 3 sbagliate plausibili ma chiaramente errate; risposte di lunghezza simile; non copiare le domande di /home/claude/lez04/Lezione.4.-.Tessitura.pt.1.xlsx (quello è il test finale)
 "mappa": {"domanda":"titolo = domanda tipo 'Che cosa …?'", "centro":"concetto centrale", "rami":[{"nome":"…","tipo":"sequenza|parola|esempio|conseguenza","figli":[{"nome":"…","tipo":"…"}]}], "voce":"testo per la voce Kore che legge la mappa ramo per ramo (60-110 parole, numeri in LETTERE, solo parole della prof)"},
 "glossario": [ {"termine":"…","def":"definizione dal PDF/prof, ≤ 25 parole"} ],   // 4-8 termini dell'argomento
 "discrepanze": ["tutto ciò che la prof dice di diverso dal PDF, refusi del PDF, numeri dubbi, con tempo e testo esatto"],
 "tagli_proposti": ["SOLO proposte (decide Sara): ripetizioni lunghe/fuori tema, con minuto e motivo; NON toglierle dalle card"]
}
```
Colori mappa (disciplinare BES, al massimo 5): centro=concetto centrale (pesca), sequenza=date e sequenze (celeste), parola=parole chiave (paglierino), esempio=esempi e opere (menta), conseguenza=conseguenze (lilla). Una mappa unica per argomento, massimo ~12 riquadri, testi brevi con le parole della prof.

Numeri e anni nel campo "voce" in lettere. Nomi stranieri come si pronunciano (Jacquard → «Giaccàr»).

## 3. Controllo finale che devi fare tu
Ricarica il tuo .py (`python3 -c "import runpy;S=runpy.run_path(...)['S']"`) e verifica: ≤3 card per slide, tempi crescenti, nessuna slide >90 s senza cambio, ogni card termina con punteggiatura, nessun termine con ortografia diversa dal PDF. Poi rispondi con UN breve riepilogo (≤15 righe): file scritti, T0/T1, numero slide/card, discrepanze principali. Non incollare i file nella risposta.
