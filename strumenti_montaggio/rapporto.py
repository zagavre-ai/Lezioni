#!/usr/bin/env python3
import sys, os, json, re, glob
sys.path.insert(0,'/home/claude/w/code')
from lesson import *
from extras import RIP, GLOS
from kore import _fonte, voce
from tabella_fine import tabella
W_='/home/claude/w';D=f'{W_}/consegna'
def voci_usate():
    nomi=['BEN1','BEN2','FZ1_R3','FIN1','COMPI','MF_0','RF1']+[f'SP_{x}' for x in ('0','1','2','3')]+['COMPITI']+GLOS+['LG0']+[r for _,r in RIP]
    for n in range(1,8):
        nomi+=[f'PI{n}']+SCN[n]+[v for v,_ in ARG[n-1]['ap']]
    for m in MAPS.values():
        nomi+=[s[0] for s in m['steps']]
    res=[]
    for n in dict.fromkeys(nomi):
        src,f,real=_fonte(n);res.append((n,f,real))
    return res
def controlli(part):
    f=f'{D}/controllo_rapido_Storia_Lez21_Parte{part}_1080p.json'
    return 'controllo_rapido.py: '+open(f).read() if os.path.exists(f) else '(mancante)'
def main():
    vu=voci_usate();prov=[x for x in vu if not x[2]]
    cv=json.load(open(f'{W_}/check_voci.json')) if os.path.exists(f'{W_}/check_voci.json') else {}
    L=[]
    L.append('# RAPPORTO DI REVISIONE · Storia V · «Il mondo dal 2001 ad oggi» (storia-V-lez21)\n')
    L.append('Correzioni 22/11 fatte. Chat di produzione: ramo `claude/blissful-bell-9eelfr`. Consegna sul ramo `revisione-storia-V-lez21`.\n')
    L.append('## 1. Struttura e durate')
    L.append('- **Parte 1** = argomenti 1–3 (USA dopo l\'11 settembre · Medio Oriente e Nord Africa · crisi economica, Obama e Trump). **Parte 2** = argomenti 4–7 (mondo multipolare · Europa · Italia · questioni aperte) + glossario, ripasso finale, mappa finale, verifica di sbarramento, sigla finale, compiti.')
    for p in (1,2):
        tl=json.load(open(f'{W_}/timeline_Parte{p}.json'));tot=tl[-1][1]+tl[-1][2]
        L.append(f'- Parte {p}: {int(tot//60)}:{tot%60:04.1f}')
    L.append('- ⚠️ **Durata**: il materiale del prof (53 min di parlato dopo le pause tolte) più le nostre aggiunte dà circa 94 minuti in totale: due Parti. Dividendo solo a fine argomento, la Parte 1 resta sotto i 45 minuti. Non è stato allungato né inventato nulla (CLAUDE.md §3.6). Alternativa possibile, se la master la preferisce: Parte 1 = argomenti 1–4 (circa 57 min) e Parte 2 = argomenti 5–7 (circa 36 min).')
    L.append('- Il prof introduce la lezione per 1:45 (sotto i 3 minuti), poi si passa agli argomenti.\n')
    L.append('## 2. Cosa è stato fatto rispetto alle regole')
    L.append('- Il prof: tagli solo nelle pause e a fine frase, pause oltre 2,5 s accorciate a circa 1 s, filtri leggeri (passa-alto 80 Hz, riduzione rumore leggera), timbro invariato, riquadro 4:3 (412×309 in x=1428, y=148), fascia gialla con nome e materia.')
    L.append('- Tolti dal parlato (con elenco): sillabe/brontolii isolati («Um», «Uh», «Okay», «Yeah», «All right»), balbettii isolati riconosciuti come parole inglesi, e 3 passaggi di **navigazione delle slide** senza contenuto storico, nel file originale a 760–779 s («andiamo pure avanti… spostiamoci sulla presidenza Obama»), 2332–2353 s («E adesso vediamo…», con la lettura del titolo della slide Europa) e 2483–2486 s («Questa Merkel. Bene.»). Nessun riassunto, nessun riempitivo.')
    L.append('- Slide: card intere del prof (max 3), testo 40 px con interlinea 1,5, bordo giallo quando comincia la frase (tempi dalla trascrizione), finestre che cambiano almeno ogni 3 minuti con foto o approfondimenti, parole chiave (max 5) nella colonna destra, nessun nome del prof tranne nella fascia gialla.')
    L.append('- Introduzione animata (copertina e argomenti): senza riquadro del prof; il riquadro compare solo quando comincia a parlare.')
    L.append('- Approfondimenti Kore: 12, solo dal materiale del prof; nessuno dice o scrive il nome del prof.')
    L.append('- Mappe: **solo quelle del prof** (4), ridisegnate nel modello BES (colori e legenda), costruite riquadro per riquadro con una voce per riquadro; la mappa 4 (Europa e Italia) è divisa in «1 di 2» e «2 di 2» perché non entra in una schermata a 36 px. Gli argomenti 1, 5 e 7 non hanno una mappa del prof e chiudono con la pillola (risposta della master 22/11).')
    L.append('- **Titoli-domanda scritti da noi con le parole del prof** (le mappe del prof non hanno la domanda): «Come cambiano gli USA dopo l\'attentato dell\'11 settembre 2001?», «Quali sono i nuovi Stati emergenti a partire dal 2000?», «Che cosa accade in Medio Oriente e Nord Africa?», «Come l\'Europa e l\'Italia affrontano la crisi del 2008?».')
    L.append('- Sigle rispiegate sullo schermo: USA, BRICS, ISIS, NATO, COVID-19, UE, MES, PNRR (note sotto le mappe, i quiz e nelle card).')
    L.append('- Parte 2 si apre con lo **spiegone** della Parte 1 (voce Kore, foto e mappe della Parte 1).')
    L.append('- Quiz: per ogni argomento, 5 domande, scatto del jingle a +0,5 s della scheda. Quiz 1–4 e 7 dal file della master (`quiz.json`). **Argomenti 5 e 6**: la master aveva 5 domande in totale (Q5) per i due argomenti; ne ho divise 3+2 e **proposto 5 nuove domande da approvare** (2 per l\'Europa, 3 per l\'Italia, scritte con le card del prof).')
    L.append('- Verifica di sbarramento: le 10 domande dell\'Excel del prof, soglia 80% (8/10); compiti: le 4 domande del prof, con intro «Compiti».\n')
    L.append('## 3. Refusi corretti (nelle nostre slide, dispense e mappe; da ricontrollare)')
    L.append('- «Al-Queda» → **Al-Qaeda** (slide argomento 1).')
    L.append('- «Seconda guerra del golfo» → **Seconda guerra del Golfo** (slide e verifica).')
    L.append('- «CoViD-19» → **COVID-19** (slide argomento 7).')
    L.append('- «Paesi emergenti» (maiuscola a metà frase) → **paesi emergenti** (slide argomento 4).')
    L.append('- «Make America great again» → **Make America Great Again** (verifica di sbarramento).')
    L.append('- Nella didascalia della slide: «Barack» (il prof scrive «Barack Obama»; nella sua mappa è «BARACK OBAMA»: riportato come lui). Nessun numero o contenuto modificato.')
    L.append('- Contenuti che il prof dice a voce in modo diverso dalle slide: il prof dice «Al Qaeda/Al-Qaida», «Gaddafi/Geddafi» (trascrizione automatica incerta): nei sottotitoli sono scritti **Al-Qaeda** e **Gheddafi**.')
    L.append('- Anomalie da portare a Sara: nel parlato il prof dice «2020-2024» per la presidenza Biden e che la guerra in Siria è durata «dal 2011 al 2024» (12 anni): riportato come lo dice. La slide dell\'argomento 7 ha una card sulla guerra in Ucraina che il prof non commenta in quel punto (l\'aveva trattata nell\'argomento 4): la card è presente e resta spenta.\n')
    L.append('## 4. Immagini')
    L.append('Tutte dal materiale del prof (PDF delle slide), ritagliate senza la didascalia incorporata (riscritta come testo) e **ingrandite** (Lanczos ×2–×4, riduzione del rumore, nitidezza) senza cambiare i tratti delle persone: WTC, Bush, Obama, Trump, Putin, Gheddafi, mappa della Siria, Merkel, Renzi/Letta, mappa Ucraina. Sorgente piccola (da 256×357 a 860×812 px): dopo l\'ingrandimento restano meno nitide di una foto originale. **Nessuna immagine da Wikimedia**, nessuna foto scaricata dal web.\n')
    L.append('## 5. Voci Kore')
    L.append(f'- Voci usate nel montaggio: {len(vu)}; **ancora provvisorie (espeak): {len(prov)}** — {", ".join(x[0] for x in prov) or "nessuna"}.')
    L.append('- Voci già ricevute e controllate con trascrizione (confronto parola per parola, numeri e date compresi, bordi): vedi `check_voci.json`. Rifatte su mia richiesta: LG1 (manca «2001»), SC7_2 (c\'è anche «Terzo,» in coda), PI1 (pronuncia dubbia), AP3_0, AP3_1, AP3_3, AP5_1 (dicevano «il prof»), SC3_1–SC3_4 (ordine «Primo/Quarto» sbagliato), BEN1 e BEN2 (dicevano il nome del prof).')
    L.append('- Montaggio: ogni voce senza silenzi in testa, dissolvenza 30–40 ms, 0,14 s di silenzio in coda (ultimi 50 ms sotto 0,03).\n')
    L.append('## 6. Tabella dei tagli del docente (fine di ogni pezzo)')
    L.append('Minuto = fine del pezzo nel video finale. Parole = ultime 8 della trascrizione automatica (può contenere errori di ascolto). «Frase finita» verificato leggendo la trascrizione prima e dopo il taglio.\n')
    L.append('| Parte | Pezzo | Fine (min:s) | Ultime parole | Frase finita |\n|---|---|---|---|---|')
    for p in (1,2):
        for nome,fine,parole,ok in tabella(p):
            L.append(f'| {p} | {nome} | {fine} | …{parole} | {ok} |')
    L.append('\n## 7. Controlli automatici (sul video finale)')
    for p in (1,2):
        L.append(f'### Parte {p}\n```\n{controlli(p)[:3500]}\n```')
    L.append('## 8. Cosa NON è stato verificato')
    L.append('- Non ho potuto **ascoltare** le voci né il montaggio: i controlli sono tutti strumentali (trascrizione, misure, frequenze).')
    L.append('- Il sincronismo labbra/voce è garantito dal taglio simultaneo di video e audio sull\'originale (scarto misurato ≤ 0,03 s) ma non l\'ho visto a occhio.')
    L.append('- Pronuncia dei nomi stranieri nelle voci provvisorie e in quelle nuove: da ascoltare dalla master.')
    L.append('- L\'agente di controllo separato ha spuntato la lista §11 (vedi sotto).')
    open(f'{D}/RAPPORTO_REVISIONE.md','w').write('\n'.join(L)+'\n')
    print('rapporto scritto',len('\n'.join(L)))
if __name__=='__main__': main()
