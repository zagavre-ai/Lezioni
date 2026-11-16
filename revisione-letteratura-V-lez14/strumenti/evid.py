import json,re,collections
W=json.load(open('tr/orig.json'))
def ricostruisci(W):
    out=[];cur=None
    for sg in W:
        for t,w in sg['parole']:
            if w.startswith(' ') or cur is None:
                if cur: out.append(cur)
                cur=[t,w.strip()]
            else: cur[1]+=w
    out.append(cur);return out
words=[(t,x) for t,w in ricostruisci(W) for x in re.split(r"['’]",w)]
norm=lambda w:re.sub(r'[^a-zàèéìòù]','',w.lower())
STOP=set('della delle degli dello dalla dalle quello quella questo questa sono anche perch quindi allora cosa cose molto ancora senza dopo prima sempre fatto tutti tutto essere stato stata'.split())
words=[(t,norm(w)[:5]) for t,w in words if len(norm(w))>=5 and norm(w)[:5] not in STOP]
T=json.load(open('pptx_text.json'))
def cardsof(i): return T[str(i)][2:-1] if i in(3,4) or i>=46 else []
def stems(c):
    lead=c.split(':')[0] if ':' in c[:90] else ''
    return {norm(x)[:5]:(4.0 if w in lead.split() else 1.0) for w in c.split() for x in re.split(r"['’]",w) if len(norm(x))>=5 and norm(x)[:5] not in STOP}
def evidenzia(slide,a,b,win=7,lam=6.0):
    C=cardsof(slide);K=[stems(c) for c in C];cnt=collections.Counter(s for k in K for s in k)
    n=len(K);ts=[a+x for x in range(0,int(b-a)+1)]
    S=[[sum(k[s]/cnt[s] for tt,s in words if t-win<=tt<=t+win and s in k) for k in K] for t in ts]
    # DP monotona: stato k=0..n-1, ammessi solo salti in avanti con penalita lam
    NEG=-1e9;best=[[NEG]*n for _ in ts];bp=[[0]*n for _ in ts]
    for k in range(n): best[0][k]=S[0][k]-(0 if k==0 else lam)
    for i in range(1,len(ts)):
        for k in range(n):
            c=[(best[i-1][k],k)]+[(best[i-1][q]-lam,q) for q in range(k)]
            v,q=max(c);best[i][k]=v+S[i][k];bp[i][k]=q
    k=max(range(n),key=lambda x:best[-1][x]);path=[k]
    for i in range(len(ts)-1,0,-1):
        k=bp[i][k];path.append(k)
    path=path[::-1]
    iv=[]
    for t,v in zip(ts,path):
        if iv and iv[-1][2]==v: iv[-1][1]=t+1
        else: iv.append([t,t+1,v])
    iv[-1][1]=b;iv[0][0]=a
    return iv
if __name__=='__main__':
    TR=json.load(open('slidetrack_raw.json'))
    for slide,a,b in [(3,193.5,530.5),(4,530.5,810),(3,905.5,1324.5),(46,1324.5,1764),(48,1764,2029)]:
        print(slide,a,b,[(round(x,0),round(y,0),v) for x,y,v in evidenzia(slide,a,b)])
