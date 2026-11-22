# Numerazione unica delle pagine: stessa nel video e nella dispensa (una numerazione per Parte)
import sys, json
sys.path.insert(0,'/home/user/Lezioni/lavoro')
import struttura as S, piani
from piani import ARGS, B, END, stati_arg, spec_key
def windows(n):
    a=ARGS[n];t0=B[f'a{n}'];t1=B[f'a{n+1}'] if n<8 else END
    seen=[]
    for t,s in stati_arg(n,t0,t1):
        if s[0]=='i': k=f'i{n}_{s[1]}'
        else: k=spec_key(n,s).rsplit('_',2)[0]
        if k not in seen: seen.append(k)
    return seen
def numera():
    P={}
    for parte,args in ((1,S.PARTE1),(2,S.PARTE2)):
        n=2
        P[('cover',parte)]=1
        P[('di' if parte==1 else 'spg',parte)]=n;n+=1
        for a in args:
            for k in windows(a): P[k]=n;n+=1
            P[f'AP{a}']=n;n+=1;P[f'PS{a}']=n;n+=1
        P[f'GL{parte}']=n;n+=1;P[f'RIEP{parte}']=n;n+=1
        if parte==2:
            for k in (1,2,3,4): P[f'COMPITO{k}']=n;n+=1
    return {str(k):v for k,v in P.items()}
if __name__=='__main__':
    P=numera();json.dump(P,open('/tmp/w/pagine.json','w'),indent=1);print(len(P),max(P.values()))
