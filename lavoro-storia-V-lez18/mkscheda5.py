import json
q=json.load(open('/tmp/L18/out/quiz_argomenti.json'))
NOMI={1:"La crisi della Russia zarista",2:"La Rivoluzione di Febbraio (1917)",3:"Dualismo di potere e Lenin",4:"Dalle giornate di luglio a Ottobre",5:"I primi provvedimenti bolscevichi",6:"Brest-Litovsk e la guerra civile",7:"Il «Comunismo di guerra»",8:"La Nuova Politica Economica (NEP)",9:"La nascita dell'URSS e la successione"}
for p,ks in ((1,range(1,5)),(2,range(5,10))):
    TL={n:(s,d) for n,s,d in json.load(open(f'/tmp/L18/timeline_P{p}.json'))}
    sc={"materia":"Storia V","titolo":f"Storia V · Lezione 5 · La Rivoluzione russa e la nascita dell'URSS (1917-1922) · Parte {p}","descrizione":"Videolezione del prof. Giorgio Mazzotti sulla Rivoluzione russa: dalla crisi dello zarismo alla nascita dell'URSS." if p==1 else "Seconda parte della videolezione del prof. Giorgio Mazzotti: dai primi provvedimenti bolscevichi alla guerra civile, dalla NEP alla nascita dell'URSS.","durata_s":round(max(s+d for s,d in TL.values()),3),
    "argomenti":[{"n":k,"titolo":NOMI[k],"inizio_s":round(TL[f'T{k}'][0],3),"quiz_s":round(TL[f'Q{k}'][0],3)} for k in ks],"quiz":{f'Q{k}':q[f'Q{k}'] for k in ks}}
    json.dump(sc,open(f'/tmp/L18/out/scheda_pubblicazione_Parte{p}.json','w'),ensure_ascii=False,indent=1);print(p,sc['durata_s'],[(a['inizio_s'],a['quiz_s']) for a in sc['argomenti']])
