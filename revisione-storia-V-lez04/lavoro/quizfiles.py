import sys,json
sys.path.insert(0,'/tmp/claude-0/w')
from dati import *
from quiz import Q
W='/tmp/claude-0/w';OUT=W+'/out'
allq={};txt=["QUIZ DI FINE ARGOMENTO · STORIA V · La Prima guerra mondiale (Prof. Giorgio Mazzotti)","Domande scritte solo dal materiale del docente. La risposta giusta è segnata con ✓.",""]
g=0
for P in (1,2):
    for n in PARTI[P]:
        g+=1;a=ARG[n-1]
        items=[{"p":p,"a":ai,"w":w,"e":e} for p,ai,w,e in Q[n]]
        allq[f'Q{g}']={"title":f"Quiz {g} · {a['nome']}","items":items}
        txt+=["="*60,f"Quiz {g} · {a['nome']}","="*60]
        for i,it in enumerate(items,1):
            txt+=[f"{i}. {it['p']}",f"   ✓ {it['a']}"]+[f"   – {x}" for x in it['w']]+[f"   Spiegazione: {it['e']}",""]
json.dump(allq,open(OUT+'/quiz_argomenti.json','w'),ensure_ascii=False,indent=1)
open(OUT+'/Quiz_Storia_Lez4.txt','w').write('\n'.join(txt))
print(len(allq),'quiz')
