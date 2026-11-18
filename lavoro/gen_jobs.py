import sys,os,json
sys.path.insert(0,'/tmp/claude-0/l06')
from dati import *
from extra import split_caps, voice_texts
T=voice_texts();CPS=14.7
for P,order in PARTI.items():
    for pos,n in enumerate(order,1):
        g=pos+POFF[P];a=ARG[n-1];L=RIGHE[n];m=max(len(x) for x in L);fs=min(128,int(128*20/m))
        json.dump({"type":"title","num":f"{g:02d}","total":len(GLOBAL_ORDER),"lines":L,"ex":a['chip'],"fs":fs,"lineY":720,"dur":4},open(f'jobs/P{P}T{pos}.json','w'),ensure_ascii=False)
        t=a['nome'];tfs=84 if len(t)<=30 else max(52,int(84*30/len(t)))
        json.dump({"type":"quiz","act":f"Quiz {g}","topic":t,"tfs":tfs,"pts":"5 domande · per continuare almeno l'80%","dur":5},open(f'jobs/P{P}Q{pos}.json','w'),ensure_ascii=False)
        d=len(T[f'PI{n}'])/CPS;caps=split_caps(T[f'PI{n}'],d)
        json.dump({"type":"repaso","kicker":"Pillola di storia","big":"RIPASSO","topic":t,"tfs":tfs,"caps":caps,"dur":round(caps[-1][1]+1.2+2.0,1)},open(f'jobs/P{P}R{pos}.json','w'),ensure_ascii=False)
    d=len(T[FIN[P]])/CPS
    json.dump({"type":"final","kicker":"Storia V","l1":"RIEPILOGO","l2":"FINALE","items":[[ARG[n-1]['nome'],""] for n in order],"sub":"Ripassiamo insieme ciò che abbiamo imparato.","dur":round(d+1.7+3.0,1)},open(f'jobs/P{P}F.json','w'),ensure_ascii=False)
print(len(os.listdir('jobs')))
