import json,openpyxl,re,os
OUT='/tmp/w/dati/';os.makedirs(OUT,exist_ok=True)
q=json.load(open('/home/user/Lezioni/lavoro/lez01/quiz_vecchio.json'))
def conv(z,i):
    return {"title":z['titolo'],"items":[{"p":d['p'],"a":d['a'],"w":d['w'],"ref":d['e']} for d in z['domande']]}
Q={}
for i in range(4):Q[f'Q{i+1}']=conv(q[i],i)
d5=q[4]['domande'];d6=q[5]['domande']
sel=[d5[0],d5[1],d5[3],d6[0],d6[2]]
Q['Q5']={"title":"Quiz 5 · La pittura: David e Ingres","items":[{"p":d['p'],"a":d['a'],"w":d['w'],"ref":d['e']} for d in sel]}
for k in Q:assert len(Q[k]['items'])==5,k
json.dump(Q,open(OUT+'quiz_argomenti.json','w'),ensure_ascii=False,indent=1)
w=openpyxl.load_workbook('/tmp/w/src/DOMANDE LEZIONE 1.xlsx').active
V=[]
for r in list(w.iter_rows(values_only=True))[1:]:
    if not r[0]:continue
    c=[(x or '').strip() for x in r]
    V.append({"p":c[0],"a":c[1],"w":c[2:5]})
json.dump({"titolo":"Verifica finale · Il Neoclassicismo","soglia":80,"domande":V},open(OUT+'verifica_finale.json','w'),ensure_ascii=False,indent=1)
import sys;sys.path.insert(0,'/home/user/Lezioni/lavoro/lez01')
import voci
json.dump({"titolo":"Compiti · Il Neoclassicismo","esercizi":[{"testo":t} for t in voci.COMPITI]},open(OUT+'compiti.json','w'),ensure_ascii=False,indent=1)
print(len(V),'domande verifica; quiz',[len(Q[k]['items']) for k in Q])
