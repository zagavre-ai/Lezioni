import sys;sys.path.insert(0,'/home/user/Lezioni/lez14')
from montaggio import *
import spec
n=int(sys.argv[1])
b=[confine(spec.ARG[k][1])[0] for k in sorted(spec.ARG)]+[confine(4300)[0] if False else 4310]
A=b[n-1];B=b[n]
K=keep(A,B);ted,tot=tmap(K)
print('A,B',A,B,'tot',round(tot),'intervalli',len(K))
ev=stati_argomento(n,A,B,K)
inv=lambda tm:next((a+(tm-o) for a,b2,o in [(a,b2,sum(y-x for x,y in K[:i])) for i,(a,b2) in enumerate(K)] if tm<=o+(b2-a)),0)
def prima(t):
    for s in SEG:
        if s['inizio']>=t-0.5:return s['testo'][:70]
for t,k in ev:
    to=inv(t)
    print('%6.1f orig %6.1f'%(t,to),k[:1],k[1:] if k[0]=='c' else k[1], '|',prima(to) )
