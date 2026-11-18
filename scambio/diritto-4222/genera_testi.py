# genera testi_voci.json dai contenuti (una chiave per frase: così ogni frase ha la sua durata e le animazioni vanno a tempo di voce)
import json,sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import contenuti as C
import re
SUB=[(r'\bCSRD\b','ci esse erre di'),(r'\bCSR\b','ci esse erre'),(r'\bRSI\b','erre esse i'),(r'\bERM\b','e erre emme'),(r'\bHR\b','acca erre'),(r'\bPMI\b','pi emme i'),(r'\bASL\b','a esse elle'),(r'\bUNI ISO\b','uni iso'),(r'know-how','know how'),(r'\bS\.p\.A\.','società per azioni'),(r'\bUE\b','Unione Europea')]
def vo(t):
    for a,b in SUB:t=re.sub(a,b,t)
    return t
T={}
T['W01']=[C.BENVENUTO]
for k,a in C.ANIM.items():
    for si,s in enumerate(a['slides'],1):
        for ii,i in enumerate(s['items'],1): T[f'{k}_s{si}_i{ii}']=[i['say']]
for n,t in C.PILLOLA_ANNUNCIO.items(): T[f'R{n}']=[t]
for n,rows in C.SCHEMI_VOCE.items():
    for i,t in enumerate(rows,1): T[f'S{n}_{i}']=[t]
for n,m in C.MAPPE.items():
    T[f'M{n}_0']=[m['intro']]
    for i,r in enumerate(m['rami'],1): T[f'M{n}_{i}']=[r[3]]
T['MF_0']=[C.MAPPA_FINALE['intro']]
for i,r in enumerate(C.MAPPA_FINALE['rami'],1): T[f'MF_{i}']=[r[3]]
for i,t in enumerate(C.RIEPILOGO_VOCE): T[f'F_{i}']=[t]
for i,t in enumerate(C.RIPASSO_P1): T[f'RP_{i}']=[t]
T={k:[vo(x) for x in v] for k,v in T.items()}
json.dump(T,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'testi_voci.json'),'w'),ensure_ascii=False,indent=1)
print(len(T),'frasi;',sum(len(' '.join(v).split()) for v in T.values()),'parole')
