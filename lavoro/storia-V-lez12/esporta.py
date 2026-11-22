# -*- coding: utf-8 -*-
import json, sys, subprocess, openpyxl
sys.path.insert(0, '/home/user/Lezioni/lavoro/storia-V-lez12')
import contenuti as C
W = '/home/user/w12'; R = f'{W}/consegna'
import os; os.makedirs(R, exist_ok=True)
NOMI = {'sigla': 'SIGLA', 'cover_ben': 'COVERV', 'prof0': 'D0', 'argomenti': 'ARG', 'spiegone': 'SPIEGONE', 'glossario': 'GL', 'ripasso': 'RF', 'mappe_fin': 'MAPF', 'verifica': 'VF', 'sigla_fin': 'FINALE', 'compiti_intro': 'CI', 'compiti': 'CO'}
def nome(n):
    if n in NOMI: return NOMI[n]
    for p, q in (('tit', 'T'), ('prof', 'A'), ('app', 'AP'), ('mappa', 'MAP'), ('pil', 'PS'), ('quiz', 'Q')):
        if n.startswith(p) and n[len(p):].isdigit(): return q + n[len(p):]
    return n.upper()
tit_arg = {k: C.ARGOMENTI[k - 1][1] for k in range(1, 7)}
Q = {}
for k, L in C.QUIZ.items():
    Q[f'Q{k}'] = {'title': f'Quiz {k} · {tit_arg[k]}', 'items': [{'p': q, 'a': a[0], 'w': a[1:], 'e': f'Risposta corretta: {a[0]}.'} for q, a in L]}
json.dump(Q, open(f'{R}/quiz_argomenti.json', 'w'), ensure_ascii=False, indent=1)
ws = openpyxl.load_workbook(f'{W}/in/DOMANDE LEZIONE 12.xlsx').active; dom = []
for i, r in enumerate(list(ws.iter_rows(values_only=True))[1:], 1):
    if r[0]: dom.append({'n': i, 'p': r[0].strip(), 'a': r[1].strip(), 'w': [x.strip() for x in r[2:5]]})
json.dump({'titolo': "Storia V · Lezione 12 · Verifica finale", 'soglia_percento': 80, 'domande': dom}, open(f'{R}/verifica_finale.json', 'w'), ensure_ascii=False, indent=1)
json.dump({'titolo': 'Compiti · Storia V · Lezione 12', 'stato': 'compiti del prof (file «LEZIONE 12.pdf», release mazzotti-storia-V), testo invariato', 'compiti': [{'n': i + 1, 'tipo': 'risposta_aperta', 'testo': t} for i, t in enumerate(C.COMPITI)]}, open(f'{R}/compiti.json', 'w'), ensure_ascii=False, indent=1)
for n in (1, 2):
    tl = json.load(open(f'{W}/asm{n}/timeline.json'))['pezzi']
    json.dump([[nome(a), b, c] for a, b, c, d in tl], open(f'{R}/timeline_Parte{n}.json', 'w'))
    v = f'{W}/Storia_Lez12_Parte{n}_1080p.mp4'
    subprocess.run(['python3', '/home/user/Lezioni/tools/scheda_da_timeline.py', v, f'{R}/timeline_Parte{n}.json', f'{R}/quiz_argomenti.json',
                    f"Storia V · Lezione 12 · L'Europa e il mondo negli anni Trenta · Parte {n}", f'{R}/scheda_pubblicazione_Parte{n}.json', 'Storia'])
