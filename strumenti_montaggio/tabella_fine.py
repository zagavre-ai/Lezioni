import sys,json,re
sys.path.insert(0,'/home/claude/w/code')
from lesson import *
from profpieces import snap
def last_words(i,n=8):
    w=re.findall(r"\S+",SEGS[i]['testo']);return ' '.join(w[-n:])
def pezzi():
    """{nome_timeline: (seg_ultimo, seg_primo)}"""
    res={}
    a0=dict(segs=[(0,17)]);B0=snap(build(a0));res['D0_1']=(B0['sl'][-1],B0['sl'][0])
    for a in ARG:
        B=snap(build(a));cuts=ap_cuts(a,B)
        bounds=[B['sl'][0]]+[c[1] for c in cuts]+[B['sl'][-1]]
        # primo seg di ogni pezzo: il successivo valido dopo il taglio
        for k in range(len(bounds)-1):
            first=B['sl'][0] if k==0 else [i for i in B['sl'] if i>cuts[k-1][1]][0]
            last=cuts[k][1] if k<len(cuts) else B['sl'][-1]
            res[f"D{a['n']}_{k+1}"]=(last,first)
    return res
def tabella(part):
    tl=json.load(open(f'{W}/timeline_Parte{part}.json'));P=pezzi();rows=[]
    for nome,t,d in tl:
        if nome in P:
            last,first=P[nome];end=t+d
            rows.append((nome,f'{int(end//60)}:{end%60:04.1f}',last_words(last),'sì'))
    return rows
if __name__=='__main__':
    for p in (1,2):
        for r in tabella(p):print(p,r)
