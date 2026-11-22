import json,sys
sys.path.insert(0,'/tmp/claude-0/w')
from dati import *
for P in (1,2,3):
    for pos,n in enumerate(PARTI[P],1):
        g=pos+POFF[P];a=ARG[n-1];L=RIGHE[n]
        m=max(len(x) for x in L);fs=128 if m<=22 else max(84,int(128*22/m))
        json.dump({"type":"title","num":f"{g:02d}","total":11,"lines":L,"ex":a['chip'],"fs":fs,"lineY":720,"dur":3.4},open(f'jobs/P{P}T{pos}.json','w'),ensure_ascii=False)
        t=a['nome'];tfs=84 if len(t)<=30 else max(52,int(84*30/len(t)))
        json.dump({"type":"quiz","act":f"Quiz {g}","tfs":tfs,"topic":t,"pts":"5 domande · per continuare almeno l'80%","dur":4.9},open(f'jobs/P{P}Q{pos}.json','w'),ensure_ascii=False)
