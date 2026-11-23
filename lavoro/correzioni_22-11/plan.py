# -*- coding: utf-8 -*-
import json, re, math, unicodedata, numpy as np, collections
S=json.load(open('/home/work/tr/lez17.json'))
CARDS={int(k):v for k,v in json.load(open('/home/work/build/cards.json')).items()}
# indici dei segmenti d'inizio argomento (verificati sulla trascrizione e sui cambi di pagina del prof)
START={1:29,2:222,3:301,4:412,5:586,6:669,7:733,8:901}
END_T=6130.0
STOP=set("il lo la le li gli un una uno di a da in con su per tra fra che e ed o ma non si ci ne come poi anche piu pero quindi cioe ecco bene va questo questa questi queste quello quella sono era erano stato stata essere ha hanno ho hai c'e del dello della dei degli delle al allo alla ai agli alle nel nello nella nei negli nelle sul sulla dal dalla dai dalle capite d'accordo perche quando dove vi molto tutto tutti tutte cui suo sua suoi sue loro".split())
def norm(w):
    w=unicodedata.normalize('NFD',w.lower());w=''.join(c for c in w if unicodedata.category(c)!='Mn');return re.sub(r"[^a-z0-9]","",w)
def stems(t):
    out=[]
    for w in re.split(r"[\s'’]+",t):
        w=norm(w)
        if len(w)>=4 and w not in STOP: out.append(w[:5])
        elif re.fullmatch(r'(19)?\d\d',w): out.append(w[-2:])
    return out
def topic_segs(n):
    i0=START[n];i1=START.get(n+1,len(S));return list(range(i0,i1))
def topic_bounds(n):
    i0=START[n];a=S[i0]['inizio']-0.35
    b=S[START[n+1]-1]['fine']+0.45 if n<8 else END_T
    return round(a,3),round(b,3)
def intro_bounds(): return 0.6,round(S[START[1]-1]['fine']+0.45,3)
def assign(n):
    cards=CARDS[n]['cards'];K=len(cards)
    cs=[collections.Counter(stems(c['lead']+' '+c['text'])) for c in cards]
    df=collections.Counter(s for c in cs for s in c)
    ids=topic_segs(n);M=len(ids)
    E=np.zeros((M,K+1))
    for a,i in enumerate(ids):
        ss=collections.Counter(stems(S[i]['testo']))
        nb=collections.Counter(stems((S[i-1]['testo'] if i>0 else '')+' '+(S[i+1]['testo'] if i+1<len(S) else '')))
        for j,c in enumerate(cs):
            sc=sum(math.log(1+K/df[s])*1.0 for s in ss if s in c)+0.3*sum(math.log(1+K/df[s]) for s in nb if s in c)
            E[a,j+1]=sc-2.5*abs(a/max(1,M-1)-(j+0.5)/K)
    Tm=np.full((K+1,K+1),-40.0)
    for k in range(K+1):
        Tm[k,k]=0
        if k+1<=K:Tm[k,k+1]=-0.8
        if k+2<=K:Tm[k,k+2]=-2.2
        for j in range(k+3,K+1):Tm[k,j]=-4.5
    dp=np.zeros((M,K+1));bp=np.zeros((M,K+1),int)
    dp[0]=E[0]+np.array([0]+[-1.5-0.8*j for j in range(K)])
    for a in range(1,M):
        c=dp[a-1][:,None]+Tm;bp[a]=c.argmax(0);dp[a]=c.max(0)+E[a]
    k=int(dp[-1].argmax());path=[k]
    for a in range(M-1,0,-1):k=bp[a,k];path.append(int(k))
    path=path[::-1]
    return [(round(S[i]['inizio'],2),round(S[i]['fine'],2),p-1) for i,p in zip(ids,path)]
if __name__=='__main__':
    import sys
    n=int(sys.argv[1])
    a=assign(n);cards=CARDS[n]['cards'];prev=None
    for t0,t1,c in a:
        if c!=prev:print(round(t0),c,(cards[c]['lead']+' '+cards[c]['text'])[:60] if c>=0 else '-');prev=c
    print('bounds',topic_bounds(n))
