# assegna, per ogni segmento del prof, la card (e la slide) di cui sta parlando, dalla trascrizione
import json,re,sys
S=json.load(open('../trasc_V.json'))
P=json.load(open('../pptx.json'))
STOP=set("che non per una con della delle dello degli sono come anche questo questa quindi allora dunque quello quella molto ecco cioè cioe perché perche essere hanno viene alla alle nell nella nelle nello negli suo sua suoi sue tutto tutti dove quando più piu fra tra però pero ancora già gia proprio diciamo insomma d'accordo accordo".split())
def toks(s):
    s=s.lower().replace("'"," ").replace("’"," ")
    return [w[:6] for w in re.findall(r"[a-zàèéìòù]{4,}",s) if w not in STOP]
def cards_of(slides):
    out=[]
    for n in slides:
        d=P[n-1]; paras=[p for nm,l in d['raw'] if nm.startswith('Text 6') for p in l]
        for p in paras:
            lead,_,rest=p.partition(': ')
            out.append({'slide':n,'lead':lead,'text':rest,'toks':set(toks(p))})
    return out
def units(a,b):
    return [(s['inizio'],s['fine'],s['testo']) for s in S if s['inizio']>=a-0.01 and s['inizio']<b]
def assign(cards,us,pen=1.2):
    n=len(cards);INF=-1e9
    sc=[[len(set(toks(t))&c['toks'])+(2 if c['lead'].lower().split()[0][:5] in t.lower() else 0) for c in cards] for _,_,t in us]
    # viterbi, monotone non-decreasing
    dp=[[INF]*n for _ in us];bk=[[0]*n for _ in us]
    for j in range(n): dp[0][j]=sc[0][j]-(pen*j if j else 0)*0
    for i in range(1,len(us)):
        for j in range(n):
            best=INF;arg=0
            for k in range(j+1):
                v=dp[i-1][k]-(pen if k!=j else 0)
                if v>best: best=v;arg=k
            dp[i][j]=best+sc[i][j];bk[i][j]=arg
    j=max(range(n),key=lambda x:dp[-1][x]);path=[j]
    for i in range(len(us)-1,0,-1): j=bk[i][j];path.append(j)
    return path[::-1]
if __name__=='__main__':
    spec={'D1':([2,3],148.133,298.633),'D2':([4,5],623.333,773.766),'D3':([6],1128.466,1309.466),'D4':([8,10],1665.067,2000.233),'D5':([11,13,14],2405.599,2736.8)}
    for k,(sl,a,b) in spec.items():
        cs=cards_of(sl);us=units(a,b);p=assign(cs,us)
        print('==',k,[c['lead'] for c in cs])
        last=None
        for (t0,t1,tx),j in zip(us,p):
            if j!=last: print('  %.1f -> card %d (%s) | %s'%(t0-a,j,cs[j]['lead'][:20],tx[:70]));last=j
