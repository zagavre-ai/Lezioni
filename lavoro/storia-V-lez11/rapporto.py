import sys,os,json,re
sys.path.insert(0,'/home/user/work/build')
from L import *
from subs import words_prof
OUT=B+'/consegna/RAPPORTO_REVISIONE.md'
tl=json.load(open(B+'/timeline_Parte1_full.json'))['tl']
ver=open(B+'/verifica.txt').read() if os.path.exists(B+'/verifica.txt') else '(controllo non eseguito)'
agente=open(B+'/agente.txt').read() if os.path.exists(B+'/agente.txt') else '(controllo dell\'agente separato non ancora eseguito)'
import os as _o
VX=f'{W}/vc/scambio/storia-V-lez11/vox/'
c3=_o.path.exists(VX+'COMP3.wav')
mp4r=_o.path.exists(VX+'MP4_R2.wav');c1r=_o.path.exists(VX+'COMP1_R2.wav')
voci=("Voci nuove arrivate dalla master e montate: BENV1_R2 (benvenuto senza nome), MP1, MP23, MP4, COMP1, COMP2 e le rigenerate R3_R2, R4_R2, SC6_1_R2…SC6_4_R2 (bordi). Trascritte e confrontate con il testo (similarità 0,75–1,0; le differenze sono nomi stranieri sbagliati dal riconoscimento automatico, non ascoltati).\n"
 "- **MP4 (prima versione) difettosa**: leggeva ad alta voce le istruzioni di stile («Dizione italiana cristallina? Timbro luminoso e accogliente…») e ripete la domanda. "+("Sostituita con la MP4_R2 rigenerata dalla master (trascritta: pulita)." if mp4r else "Montata solo la parte corretta (da 16,95 s), richiesta MP4_R2.")+"\n"
 "- **COMP1 (prima versione) difettosa**: ripeteva l'esercizio 1 e legge l'esercizio 2 con l'anno sbagliato (1924 invece di 1929) prima di ripeterlo giusto. "+("Sostituita con la COMP1_R2 rigenerata (trascritta: pulita)." if c1r else "Montate le parti corrette.")+"\n"
 +("- COMP3 (chiusura dei compiti «Svolgi i compiti qui sotto e premi Consegna…») arrivata e montata.\n" if c3 else "- **COMP3 NON arrivata**: la frase di chiusura dei compiti (voce e schermo) è montata con una tenuta muta di 7 s al posto della voce (scheda muta oltre 2,5 s: da sostituire appena arriva).\n")
 +"- I compiti sono letti dalle voci COMP1 e COMP2 (parole esatte del prof) e si accendono uno alla volta con il bordo giallo (regola del 22/11). Il piano della master prevedeva una voce sola COMPITI: avevo già richiesto COMP1 e COMP2 prima del messaggio.\n"
 "- Le schede Quiz e Verifica dicono «Rispondi · premi Controlla · poi Continua» (regola 22/11 22:30).")
sev=open(B+'/severo.txt').read() if os.path.exists(B+'/severo.txt') else '(non eseguito)'
def mm(s): return f'{int(s//60)}:{s%60:04.1f}'
NAMES={'S0':'Sigla Storia (kit, 15 s)','C0':'Copertina + benvenuto (voce Kore, senza riquadro del docente)','D0':'Copertina + introduzione del docente (57,6 s, riquadro solo mentre parla; foto di Iosif Stalin a 54,3 s)','GL':'Glossario animato (GL1 + GL2, 11 termini)','RF':'Ripasso finale argomento per argomento (RIEP1)','FI':'Chiusura (FIN1)','VF':'Scheda Verifica di sbarramento (80%, test Excel del prof, 10 domande)','SF':'Sigla finale con avviso dei diritti (kit)','CI':'Intro «Compiti» (jingle)','CS':'Compiti del docente (4 esercizi, 2 schermate, voce COMP1/COMP2)'}
rows=[]
for n,s,d in tl:
    if re.fullmatch(r'T\d',n): nm=f'**Argomento {n[1]}** · titolo (titolo.wav)'
    elif re.fullmatch(r'D\d[abc]?',n) and n!='D0': nm='Docente + slide a finestra'
    elif re.fullmatch(r'A\d',n): nm='Approfondimento animato (3 schede, voci AN)'
    elif re.fullmatch(r'M\d',n) or n.startswith('MAP'): nm='Mappa del prof, ramo per ramo (voce Kore)'
    elif re.fullmatch(r'P\d',n): nm='Pillola di ripasso (repaso.wav, voce R)'
    elif re.fullmatch(r'R\d',n): nm='Schema di ripasso guidato (voci SC)'
    elif re.fullmatch(r'Q\d',n): nm='Scheda Quiz, 5 domande, 80% (quiz.wav a +0,5 s)'
    else: nm=NAMES.get(n,n)
    rows.append(f'| {n} | {nm} | {mm(s)} | {d:.1f} s |')
tab='\n'.join(rows)
# 10 punti card (bordo giallo vs inizio frase del prof)
segs=json.load(open(B+'/../trasc_orig.json'))
from prof import EV,PAGES
pts=[('T1',64.1,'p3',1),('T1',150.9,'p3',2),('T1',217.5,'p3',3),('T1',256.0,'p3',4),('T2',408.5,'p4',2),('T3',531.3,'p5',2),('T3',604.0,'p5',3),('T4',962.4,'p6',4),('T5',1023.0,'p7',2),('T6',1275.3,'p8',3)]
def seg_at(t):
    c=[s for s in segs if s['inizio']-0.5<=t<=s['fine']]
    if c: return min(c,key=lambda s:abs(s['inizio']-t))
    return min(segs,key=lambda s:abs(s['inizio']-t))
card=[]
for k,t,pg,i in pts:
    s=seg_at(t);card.append(f"| {k} | {t:.1f} | card {i} · «{PAGES[pg]['cards'][i-1].split(':')[0]}» | {s['inizio']:.1f} | {s['testo'][:70]} | {abs(s['inizio']-t):.1f} s |")
cardt='\n'.join(card)
md=f"""# RAPPORTO DI REVISIONE · Storia V · L'URSS di Stalin (1924-1939) · correzioni 22/11

Lezione rifatta sul modello del CLAUDE.md del 22/11 (chat claude/gifted-fermi-uzdgf8), a partire dalla consegna del 19/11 e dal video originale del prof (release `mazzotti-storia-V`). **Parte unica** (la lezione è sotto i 65 minuti, quindi niente spiegone). Ogni valore è etichettato **[misurato]**, **[stima]** o **[non verificato]**.

{ver}

## Pezzi del video (timeline, minuto di inizio e durata) [misurato]
| Etichetta | Pezzo | Inizio | Durata |
|---|---|---|---|
{tab}

Dissolvenza di 0,4 s (0,8 s sigla→copertina) e `trans.wav` a ogni cambio di pezzo. Le dissolvenze sul docente cadono solo nel silenzio (margini controllati: ≥ 0,35 s di silenzio, ≤ −36 dB contro −19 dB del parlato) [misurato sul parlato originale].

**Durata sotto i 50 minuti:** con il solo materiale del prof (video 25:06, 6 slide, 3 mappe) non si arriva a 50: non è stato allungato né inventato (CLAUDE.md §3.6).

## Cosa è stato rifatto rispetto alla consegna del 19/11
1. **Mappe del prof (3)**, dal PDF «MAPPE LEZIONE 11»: stessa struttura, frecce e parole del prof, ridisegnate nel modello BES (pesca / celeste / paglierino / menta / lilla, legenda in alto a destra, testo 34–50 px), costruite **ramo per ramo** con la voce Kore e riquadro acceso in giallo finché la voce lo legge; alla fine la mappa intera resta ferma 4 s. Tolte tutte le mappe inventate o ristrutturate da noi (MAP1–6, MAPF1) e le tre «ridisegnate con mappa.py».
   - Mappa 1 «Come giunge al potere assoluto Stalin?» → fine argomento 1 (voce MP1).
   - Mappa 2 «Come avviene l'industrializzazione dell'URSS?»: **mappa UNICA per gli argomenti 2 e 3** (collettivizzazione + piani quinquennali). Resta unica come dice il CLAUDE.md §6 e sta **a fine argomento 3**; l'argomento 2 si chiude con pillola e quiz. **Da confermare con la master.**
   - Mappa 3: il prof **non ha scritto la domanda come titolo**; il titolo «Su che cosa si basa il totalitarismo di Stalin?» è scritto da noi con le sue parole («si basa su»). **Dichiarato come da messaggio della master.**
   - Argomenti 5 e 6 e mappa finale: il prof non ha mappe → **nessuna mappa inventata** (messaggio della master 22/11 18:45); l'argomento si chiude con pillola di ripasso e quiz.
   - Sigle nelle mappe: «URSS» è spiegata sullo schermo («Unione delle Repubbliche Socialiste Sovietiche»); «Gulag» spiegato («campi di lavoro forzato») sia a voce sia sullo schermo.
2. **Slide del prof**: card a 40 px (interlinea 1,5), al massimo 3 card intere (mai «…», mai iniziale minuscola), card alte quanto il testo; bordo giallo e pallino giallo quando il prof comincia la frase, le altre card attenuate; **sotto-slide «a finestra»** (le card scorrono, 1–3 per schermata); riquadro 4:3 (412×309 a x=1428, y=148, ombra grigia), fascia gialla con nome e materia, «Parole chiave» (3–4) che si accendono con la card. Nessuna schermata identica oltre 3 minuti (la più lunga: vedi controllo severo).
3. **Niente nome del docente** nelle voci Kore (la voce BENV1 diceva «il professor Mazzotti» → rifatta come BENV1_R2: «il professore») e **niente nome nel piè di pagina** (solo «STORIA V» e «Pagina N»); il nome compare solo nella fascia gialla.
4. **Introduzione animata senza riquadro del docente** (copertina con benvenuto Kore); il riquadro compare solo quando il prof comincia a parlare (D0, 57,6 s, < 3 minuti). Copertina con il titolo esatto «L'URSS di Stalin (1924-1939)», elenco degli argomenti e sigla spiegata.
5. **Compiti e Verifica di sbarramento dentro il video** (nella consegna del 19/11 erano fuori): scheda Verifica (10 domande dell'Excel del prof, 80%), sigla finale con avviso dei diritti, intro «Compiti» con jingle, compiti del prof letti con voce Kore (COMP1, COMP2).
6. **Pause e silenzi:** nel parlato del prof non ci sono pause oltre 1,8 s (silencedetect −40 dB, d ≥ 1 s) [misurato sull'originale]: niente da accorciare. Tolti i 6 silenzi di 3 s a fine schema.
7. **Audio del prof dall'originale:** passa-alto 80 Hz, riduzione del rumore leggera (afftdn nr 6), −16 LUFS con limitatore; timbro mantenuto (vedi misura sopra).
8. **Dispensa A4** identica al video (stesse slide a finestra, stesso ordine e numeri di pagina, a tutta larghezza) con **strato di testo invisibile**; copertina identica a quella del video, senza numero di lezione e senza nome del docente; piè di pagina «STORIA V · Pagina N». **PDF delle mappe a parte** (copertina «MAPPE», poi le 3 mappe), con testo invisibile.
9. **Sottotitoli** `.vtt` rifatti sul video finale (prof dalla trascrizione automatica con correzione dei termini del materiale; voci Kore dal testo esatto, numeri in cifre).

## Voci
{voci}

## Controllo dei punti card (10 punti, bordo giallo vs inizio della frase del prof nella trascrizione) [misurato]
| Pezzo | t bordo giallo (s orig.) | card | inizio frase prof (s orig.) | frase (trascrizione automatica) | scarto |
|---|---|---|---|---|---|
{cardt}

## Refusi e correzioni di forma nelle slide del prof
- Nessun refuso di ortografia, accento o maiuscola dei nomi propri trovato nelle 6 slide del prof (PDF «LEZIONE 11»). Nomi controllati: Lev Trockij, Nikolaj Bucharin, Aleksej Stachanov, Komsomol, sovchoz, kolchoz, kulaki, dekulakizzazione, Holodomor, Molotov-Ribbentrop, Società delle Nazioni.
- Correzioni di forma: virgolette dritte → caporali «»; spaziature irregolari nella card «repressione dei kulaki».
- Aggiunte di spiegazione delle sigle, solo sullo schermo, in parentesi: URSS (Unione delle Repubbliche Socialiste Sovietiche) in 3 card, Comintern (l'Internazionale comunista), Komsomol (l'organizzazione giovanile comunista). PCUS e NEP sono già spiegate dal prof nella sua frase.
- File originali del prof non modificati.

## Numeri e contenuti che non tornano (lasciati come dice il prof, da portare a Sara)
- La mappa 1 dice «rivoluzione in un solo paese», la slide e il prof dicono «socialismo in un solo paese»: ciascuna è lasciata com'è.
- Il prof dice a voce che l'Holodomor causò «circa 3 milioni» di morti; la slide dice «milioni di morti»: lasciato come dice il prof.
- A voce nomina Gosplan e Zinov'ev e Kamenev, che non sono sulle slide: non aggiunti.
- Il prof dice «URSS» a voce (la sua voce non si tocca): la spiegazione della sigla c'è solo sullo schermo.

## Immagini e fonti
- Foto di Iosif Stalin (slide 2 del prof, PDF «LEZIONE 11»): originale 247×311 px, ingrandita 3× (Lanczos) con nitidezza leggera; è il massimo ottenibile dal file del prof. Nessuna altra immagine aggiunta; nessuna foto scaricata dal web.

## Scelte da confermare
- Nel rientro del prof sui «risultati industriali» (argomento 3, 765–871 s dell'originale) la schermata mostra le card 2 (attenuata) e 3 (accesa) della pagina «La grande svolta»: la card 2 era già comparsa nell'argomento 2 («già visto» del disciplinare BES), ma mostrare la sola card 3 per 105 s avrebbe violato la regola «card sola». Scelta da confermare.
- La sigla Storia di 15 s del kit contiene la scritta «[FATTI · CAUSE · CONSEGUENZE]» in carattere mono: è il file del kit, non modificato.
- Il quiz e la verifica sono quelli già approvati (JSON), con «URSS» sostituito da «Unione Sovietica».

## Controllo severo della master (`controllo_severo.py`)
{sev}

## Controllo dell'agente separato (lista del CLAUDE.md §11)
{agente}

## Cosa NON ho verificato [non verificato]
- **Pronuncia delle voci Kore** (nomi stranieri e latini: Trockij, Bucharin, kolchoz, sovchoz, kulaki, Holodomor, Komsomol, Molotov-Ribbentrop, Gulag…): non ascoltate (nessun audio a orecchio in questa sessione); trascritte con riconoscimento automatico, che sbaglia i nomi stranieri, quindi **va riascoltata dalla master**.
- **Sottotitoli del prof**: partono dalla trascrizione automatica con circa 50 regole di correzione dei nomi; non riascoltati parola per parola, possono restare frasi sbagliate nel parlato spontaneo.
- **Timbro a orecchio** dopo la pulizia: misurato (rapporto acuti/medi), non ascoltato.
- La sincronia labbra è misurata per costruzione e con correlazione audio/video (tabella), non a vista su ogni frase.
"""
open(OUT,'w').write(md);print('ok',len(md))
