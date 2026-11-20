import sys,json,subprocess,os
sys.path.insert(0,'/tmp/L18/lib')
from assemble import *
PH={1:[(2,"il governo provvisorio"),(2,"i soviet"),(3,"il rientro di Lenin")],2:[(2,"la pace immediata"),(2,"la distribuzione della terra"),(2,"caratteri autoritari")],3:[(1,"le armate bianche"),(1,"l'Armata rossa"),(2,"comunismo di guerra")],4:[(2,"vendere parte del prodotto"),(2,"imprese private"),(2,"risultati positivi")]}
for m in (1,2,3,4):
    nm=f'MA{m}';v=dur(vn(nm));st,_=align_(nm);ss=sents(nm);t0=0.9;T=[]
    for si,ph in PH[m]:
        a=st[si][0];b=st[si+1][0] if si+1<len(st) else v;idx=ss[si].lower().find(ph.lower());T.append(t0+a+(b-a)*idx/len(ss[si])-0.25)
    T=[max(T[i],(T[i-1]+1.2) if i else 1.0) for i in range(len(T))]
    tot=t0+v+1.5
    r=subprocess.run(['python3',W+'/mappa.py',f'{W}/mp2/m{m}.json','--out',f'{W}/mp2/o{m}','--durata',f'{tot:.3f}','--tempi',','.join(f'{x:.2f}' for x in T)],capture_output=True,text=True);print(r.stdout[-160:],r.stderr[-300:])
