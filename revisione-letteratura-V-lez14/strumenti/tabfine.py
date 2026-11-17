import json,sys
sys.path.insert(0,'/tmp/w14')
from evid import ricostruisci,W
words=ricostruisci(W)
def mm(x): return '%d:%02d'%(x//60,x%60)
rows=[]
for P in (1,2):
    NT={n:(s,d) for n,s,d,o in json.load(open(f'/tmp/w14/as{P}/tl_new.json'))['tl']}
    PL=json.load(open(f'/tmp/w14/dn{P}/plan.json'))['plan']
    for n,p in PL.items():
        s0,s1=p['s0'],p['s1'];ns,d=NT[n]
        before=[w for t,w in words if t<s1][-8:];after=[w for t,w in words if t>=s0][:6]
        fine=before[-1][-1] in '.?!'
        first=[w for t,w in words if t>=s0][:6]
        prevw=[w for t,w in words if t<s0][-1:] 
        inizio_ok = (not prevw) or prevw[0][-1] in '.?!'
        rows.append(f"| P{P} {n} | {mm(ns)} | «{' '.join(first)}…» | {'sì' if inizio_ok else 'no'} | {mm(ns+d)} | «…{' '.join(before)}» | {'sì' if fine else 'no'} |")
print('| Pezzo | Inizio | Prime parole | Inizia a inizio frase | Fine | Ultime parole | Frase finita |\n|---|---|---|---|---|---|---|');print('\n'.join(rows))
