# Tabella dei tagli del prof: per ogni pezzo, minuto d'uscita, ultime 7 parole, frase finita sì/no (dalla trascrizione)
import sys,json;sys.path.insert(0,'/home/user/Lezioni/lavoro_lez03')
from sorgente import *
def righe(timeline,pezzi):
    """timeline=[nome,start,dur]; pezzi={nome:(a,b) sorgente}"""
    out=[]
    for n,st,du in timeline:
        if n not in pezzi:continue
        a,b=pezzi[n];ia=sent_at(a+0.2);ib=sent_at(b-0.35)
        w0=SENT[ia][2];w1=SENT[ib][3]
        ult=' '.join(x[2] for x in W[max(w0,w1-7):w1+1]);ini=' '.join(x[2] for x in W[SENT[ia][2]:SENT[ia][2]+6])
        fin=W[w1][3]
        out.append((n,st+du,ini,ult,fin,a,b))
    return out
