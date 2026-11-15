import json,re,difflib,sys
sys.path.insert(0,'.')
from content5 import ARG
R=json.load(open('tr5_fine.json'))
R=[x for x in R if x['t'] and len(x['t'])>2]
SW=set("the and for that with from this have they their are was were which what when where into more than also such each other only most been being them these those will would should could about because there while whose over under between during through often usually even just like make made".split())
def words(t): return [w for w in re.findall(r"[a-zà-ú]+",t.lower()) if len(w)>=4 and w not in SW]
segw=[words(x['t']) for x in R]
def sc(iw,j):
    s=0
    ws=segw[j]+(segw[j+1] if j+1<len(segw) else [])
    for w in set(iw):
        if any(w==v or (len(w)>5 and difflib.SequenceMatcher(None,w,v).ratio()>=0.82) for v in ws): s+=1
    return s/ (len(set(iw))**0.5+1e-9)
items=[];
for a in ARG:
    for si,s in enumerate(a['slides']):
        for ii,it in enumerate(s['items']): items.append((a['n'],si,ii,words(re.sub(r'\*\*','',it))))
N=len(items);M=len(R)
import numpy as np
S=np.array([[sc(it[3],j) for j in range(M)] for it in items])
# DP monotona: best[i][j]=max over j'<=j
NEG=-1e9;best=np.full((N,M),NEG);arg=np.zeros((N,M),int)
best[0]=S[0]
for i in range(1,N):
    run=NEG;ra=0
    for j in range(M):
        if best[i-1][j]>run: run=best[i-1][j];ra=j
        best[i][j]=run+S[i][j]-0.02*0;arg[i][j]=ra
j=int(np.argmax(best[N-1]));path=[0]*N
for i in range(N-1,-1,-1):
    path[i]=j;j=arg[i][j] if i>0 else j
out={};
for i,(n,si,ii,w) in enumerate(items):
    out[f'A{n}.S{si}.I{ii}']={'t':R[path[i]]['s'],'score':round(float(S[i][path[i]]),2),'heard':R[path[i]]['t'][:70]}
json.dump(out,open('align5.json','w'),ensure_ascii=False,indent=1)
for k,v in out.items(): print(k,round(v['t']),v['score'],v['heard'])
