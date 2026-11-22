import sys,math
sys.path.insert(0,'/home/claude/w/b')
import vox
from data import *
def nwin(n,per=3): return max(1,math.ceil(n/per))
def plan():
    """pagine della dispensa nell'ordine del video: (tipo, id, indice)"""
    P=[('cover','cover',0),('dic','dic',0)]
    for a in range(1,6):
        ev=[(t0,'sub',n) for n,(arg,ci,t0,anc) in enumerate(SUB) if arg==a]+[(t,'an',nm) for nm,t in AN[a]]
        ev.sort(key=lambda x:x[0])
        for t,k,x in ev:
            if k=='sub': P.append(('sub',x,0))
            else:
                S=vox.sentences(vox.T[x])[1:]
                for w in range(nwin(len(S))): P.append(('an',x,w))
        P.append(('sch',a,0))
    S=vox.sentences(vox.T['GL1'])[1:]
    for w in range(nwin(len(S))): P.append(('glos','GL1',w))
    for a in range(1,6):
        S=vox.sentences(vox.T[f'R{a}']); S=S[1:] if S[0].lower().startswith('ripassiamo') else S
        for w in range(nwin(len(S))): P.append(('rip',a,w))
    P+= [('compi','compi',0),('compi','compi',1)]
    return P
def pagenum(kind,x,w=0):
    for i,p in enumerate(plan()):
        if p==(kind,x,w): return i+1
if __name__=='__main__':
    P=plan();print(len(P)); print([ (i+1,)+p for i,p in enumerate(P)][:30])
