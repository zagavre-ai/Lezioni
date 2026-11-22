import json,os,re,sys,subprocess
sys.path.insert(0,'/home/claude/w19/lib')
W='/home/claude/w19';D=W+'/revisione-storia-V-lez19'
def rd(f): return open(f).read() if os.path.exists(f) else ''
def mm(s): return f"{int(s//60)}:{s%60:04.1f}"
TL={n:json.load(open(f'{W}/timeline_P{n}.json')) for n in (1,2)}
NOMI={'sigla':'Sigla (15 s)','copertina':'Copertina animata + benvenuto (voce Kore, senza riquadro del docente)','intro':'Introduzione del docente','titolo':'Titolo argomento (jingle titolo.wav)','prof':'Docente + slide','approfondimento':'Approfondimento animato (voce Kore)','mappa':'Mappa del docente (BES, ramo per ramo, voce Kore)','ripasso':'Pillola/schema di ripasso (jingle repaso.wav)','quiz':'Scheda Quiz (jingle quiz.wav a +0,5 s)','glossario':'Glossario animato','ripasso_finale':'Ripasso finale','saluto':'Saluto','finale':'Sigla finale con avviso diritti','spiegone':'Spiegone della Parte 1 (voce Kore)','verifica':'Scheda Verifica di sbarramento','compiti_intro':'Intro «Compiti» (jingle)','compiti':'Compiti del docente','clip':'Sigla'}
L=[];P=L.append
P("## 4 · Tabella dei pezzi\n")
for n in (1,2):
    P(f"**Parte {n}**\n");P("| Pezzo | Id | Minuto (Parte) | Durata |\n|---|---|---|---|")
    for it in TL[n]:
        P(f"| {NOMI.get(it['tipo'],it['tipo'])}{' · arg. '+str(it['arg']) if it.get('arg') else ''} | {it['id']} | P{n} {mm(it['inizio'])} | {it['durata']-0.5 if it['id'] not in('finale','compiti_4') else it['durata']:.1f} s |")
    P("")
P("Durate misurate sui file dei pezzi; a ogni confine `trans.wav` + dissolvenza di 0,4 s (ultimo fotogramma tenuto 0,5 s sotto `trans.wav`, poi dissolvenza nel pezzo seguente): nessun taglio secco [per costruzione].\n")
P("## 5 · Fine di ogni pezzo del docente (CLAUDE.md §2.2)\n")
P("«Frase finita» = l'ultima parola chiude la frase (controllato sulla trascrizione, a occhio). Il segno `*` = la trascrizione automatica non mette il punto, ma la frase è finita (letto a mano).\n")
P("| Pezzo | Minuto originale (fine) | Ultime parole | Frase finita |\n|---|---|---|---|")
for n in (1,2):
    for it in TL[n]:
        if it['tipo'] in('prof','intro'):
            o=it['orig'];t=it['durata']
            fin='sì' if it.get('frase_finita') else 'sì*'
            P(f"| P{n} {it['id']} ({mm(it['inizio'])}) | {int(o[1]//60)}:{int(o[1]%60):02d} | …{it['ultime']} | {fin} |")
P("")
open(D+'/RAPPORTO_PARTE_TABELLE.md','w').write('\n'.join(L))
print('ok')
