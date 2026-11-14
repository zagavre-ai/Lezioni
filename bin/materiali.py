import sys,json,random,openpyxl,shutil
sys.path.insert(0,'/home/claude/w/bin');from conf import CONF
NN=sys.argv[1];C=CONF[NN];N=C['N'];D=f'/home/claude/w/l{NN}/';O=D+'out/'
Q=json.load(open(D+'voci/quiz_argomenti.json'));random.seed(int(NN))
L=[f"QUIZ DI ARGOMENTO · Letteratura italiana · {C['titolo']}","STATO: approvati per delega alla master (Sara, 13/11: «approva tutto»); la master li ricontrolla",""]
for i,(k,q) in enumerate(Q.items(),1):
    L+=["",f"== Argomento {i} · {C['arg'][i-1]['t']} =="]
    for j,it in enumerate(q['items'],1):
        ops=[(it['a'],1)]+[(w,0) for w in it['w']];random.shuffle(ops)
        L.append(f"{j}. {it['p']}")
        for x,(t,g) in enumerate(ops):L.append(f"   {'ABCD'[x]}) {t}"+("  <-- giusta" if g else ""))
        L.append(f"   Spiegazione: {it['e']}")
open(O+f'Quiz_Letteratura_Lez{N}.txt','w').write('\n'.join(L)+'\n')
# test finale dall'Excel del docente, nel modello del kit
src=openpyxl.load_workbook(f'/home/claude/w/comune/Excel prova finale LETTERATURA ITALIANA V/DOMANDE LEZIONE {N}.xlsx').active
wb=openpyxl.load_workbook('/home/claude/lezioni/kit/docenti/Modello_test_finale.xlsx');ws=wb['Test']
for r in range(2,ws.max_row+1):
    for c in range(1,8):ws.cell(r,c).value=None
r=2
for row in src.iter_rows(min_row=2,values_only=True):
    if not row or not row[0]:continue
    for c,v in enumerate(row[:5],1):ws.cell(r,c).value=str(v).strip() if v is not None else None
    r+=1
wb.save(O+f'Test_Letteratura_Lez{N}.xlsx');print('quiz e test:',r-2,'domande nel test')
