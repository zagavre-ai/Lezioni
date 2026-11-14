# Sincronia: assegna ogni segmento di parlato alla frase della slide (Viterbi con penalità di cambio).
import re,math,unicodedata,json
def norm(s):
    s=unicodedata.normalize('NFD',s.lower());s=''.join(c for c in s if unicodedata.category(c)!='Mn')
    return re.findall(r'[a-z0-9]+',s)
STOP=set('della delle degli dello nella nelle negli sono come anche questo questa quella quelli ancora perche quindi dopo molto tutti tutto sulla suoi loro dell'.split())
def stems(s,k=5):
    return {w[:k] for w in norm(s) if len(w)>=4 and w not in STOP}
def assegna(segs,units,pen=2.2,start=0):
    """segs=[{s,e,t}], units=[(card,fraseIdx,testo)] -> lista di indici unità per segmento"""
    U=[stems(u[2]+' '+(u[3] if len(u)>3 else '')) for u in units]
    df={}
    for u in U:
        for w in u:df[w]=df.get(w,0)+1
    N=len(U)
    idf=lambda w:math.log(1+N/df.get(w,1))
    em=[]
    for sg in segs:
        S=stems(sg['t'])
        row=[]
        for u in U:
            inter=S&u
            row.append(sum(idf(w) for w in inter)/math.sqrt(len(S)+2))
        em.append(row)
    n=len(segs)
    if n==0:return []
    NEG=-1e9
    best=[[NEG]*N for _ in range(n)];bp=[[0]*N for _ in range(n)]
    for j in range(N):best[0][j]=em[0][j]-(0 if j==start else pen*0.8)
    for i in range(1,n):
        for j in range(N):
            c=[]
            for k in range(N):
                p=0 if k==j else (pen*0.5 if j==k+1 else pen)
                c.append(best[i-1][k]-p)
            k=max(range(N),key=lambda x:c[x]);best[i][j]=c[k]+em[i][j];bp[i][j]=k
    j=max(range(N),key=lambda x:best[n-1][x]);path=[j]
    for i in range(n-1,0,-1):j=bp[i][j];path.append(j)
    return path[::-1]
def intervalli(segs,path,t0,t1):
    """[(t_inizio,t_fine,unità)] fusi, coprono esattamente [t0,t1]"""
    out=[]
    for sg,u in zip(segs,path):
        if out and out[-1][2]==u:out[-1][1]=sg['e']
        else:out.append([sg['s'],sg['e'],u])
    if not out:return [[t0,t1,0]]
    out[0][0]=t0;out[-1][1]=t1
    for a,b in zip(out,out[1:]):b[0]=a[1]
    return out
