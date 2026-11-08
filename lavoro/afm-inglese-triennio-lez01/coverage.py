import json,sys,difflib
sys.argv=['x']
import align as AL
A=json.load(open('align.json')); U=AL.U
T=[a["t"] for a in A]+[3732]
TW=AL.TW; TS=AL.TS
def near(k,s):
    if s==k: return True
    if len(k)>=5 and (s.startswith(k[:5]) or k.startswith(s[:5])) and len(s)>=5: return True
    return difflib.SequenceMatcher(None,k,s).ratio()>=0.8
cov=[]
for i,u in enumerate(U):
    ks=[k for k in dict.fromkeys(AL.keys(u['txt'])) if AL.df.get(k,0)<=AL.N*0.01 or True]
    ks=[k for k in ks if not k.isdigit()] or ks
    lo,hi=T[i]-25,T[i+1]+25
    win=set(TS[j] for j in range(len(TS)) if lo<=TW[j]<=hi)
    m=sum(1 for k in ks if any(near(k,s) for s in win))
    cov.append(m/max(1,len(ks)))
json.dump(cov,open('coverage.json','w'))
if __name__=='__main__':
    for i,c in enumerate(cov):
        if c<0.35: print(i,U[i]['pg'],'%.2f'%c,U[i]['txt'][:80])
