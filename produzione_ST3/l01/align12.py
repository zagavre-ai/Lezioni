import json,re,pdfplumber,numpy as np,sys
R=json.load(open('asr12.json'))
pdf=pdfplumber.open('LEZIONE.1.3.pdf')
SW=set('il lo la le gli i un una di a da in con su per tra fra e che del della dei delle degli al alla alle ai nel nella nei nelle sul sulla non si è sono come ma anche più ha hanno questo questa quello cui o se poi quindi ecco dunque allora ad ed l d all dell'.split())
def toks(s):
    w=re.findall(r"[a-zàèéìòù0-9]+",s.lower());return [x[:6] for x in w if x not in SW and len(x)>2]
pages=[0,1,2,3,4,5,6,7,8,9] # 0-index
txt=[(pdf.pages[i].extract_text() or '') for i in pages]
from collections import Counter
df=Counter();ts=[set(toks(t)) for t in txt]
for s in ts:df.update(s)
def score(seg,k):
    s=set(toks(seg));
    if not s or not ts[k]:return 0
    return sum(1/ (df[w]) for w in s&ts[k])/ (len(s)**0.5)
N=len(R);K=len(pages)
S=np.array([[score(R[i][2],k) for k in range(K)] for i in range(N)])
# DP monotona: pag 0..9 ordine, ammesso saltare (p9 mappa senza testo)
NEG=-1e9;D=np.full((N,K),NEG);B=np.zeros((N,K),int)
for k in range(K):D[0,k]=S[0,k] if k==0 else NEG
D[0,0]=S[0,0]
for i in range(1,N):
    for k in range(K):
        best=NEG;bk=k
        for j in range(max(0,k-2),k+1):
            if D[i-1,j]>best:best=D[i-1,j];bk=j
        D[i,k]=best+S[i,k]-0.02;B[i,k]=bk
k=int(np.argmax(D[N-1]));A=[0]*N
for i in range(N-1,-1,-1):A[i]=k;k=B[i,k]
json.dump([[R[i][0],R[i][1],R[i][2],int(A[i])+1] for i in range(N)],open('asr12_pag.json','w'),ensure_ascii=False)
prev=-1
for i in range(N):
    if A[i]!=prev:print('pag',A[i]+1,'da seg',i,'t=%.0f (%d:%02d)'%(R[i][0],R[i][0]//60,R[i][0]%60),R[i][2][:90]);prev=A[i]
