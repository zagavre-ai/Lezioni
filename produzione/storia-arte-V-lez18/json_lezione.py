import sys, json, shutil, openpyxl
sys.path.insert(0, '/home/user/w18')
from dati import *
O = '/home/user/w18/consegna/'
# quiz per argomento
Q = {}
for i, (a, tit) in enumerate(ARGOMENTI, 1):
    Q[f'Q{i}'] = {'title': f'Quiz {i} · {tit}', 'items': [{'p': p, 'a': c, 'w': w} for p, c, w in QUIZ[a]]}
json.dump(Q, open(O + 'quiz_argomenti.json', 'w'), ensure_ascii=False, indent=1)
# verifica finale = Excel del prof (10 domande)
ws = openpyxl.load_workbook('/home/user/w18/DOMANDE LEZIONE 18.xlsx').active
dom = []
for n, r in enumerate(list(ws.iter_rows(values_only=True))[1:], 1):
    r = [str(x).strip() for x in r if x is not None]
    dom.append({'n': n, 'p': r[0], 'a': r[1], 'w': r[2:5]})
json.dump({'titolo': "Storia dell'arte V · Verifica finale", 'soglia': 0.8, 'domande': dom}, open(O + 'verifica_finale.json', 'w'), ensure_ascii=False, indent=1)
shutil.copy('/home/user/w18/DOMANDE LEZIONE 18.xlsx', O + 'Test_StoriaArte_Lez18.xlsx')
# compiti
json.dump({'titolo': "Compiti · Storia dell'arte V · Postmodernità e globalizzazione", 'esercizi': [{'n': i + 1, 'tipo': 'aperta', 'testo': t} for i, t in enumerate(COMPITI)]},
          open(O + 'compiti.json', 'w'), ensure_ascii=False, indent=1)
print(len(Q), len(dom), len(COMPITI), [len(v['items']) for v in Q.values()])
