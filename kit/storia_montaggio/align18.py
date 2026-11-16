import sys,json,math,collections
sys.path.insert(0,'/home/user/Lezioni/storia_s7')
from sync import *
from slides18 import *
tr=json.load(open('/tmp/w18/tr18.json'))
W=words_with_times(tr,'/tmp/w18/a18.wav')
# idf sulle finestre di trascrizione
docs=[set(stem(norm(w)) for w in s['t'].split()) for s in tr]
df=collections.Counter(x for d in docs for x in d)
idf={k:math.log((len(docs)+1)/(v+1))+0.3 for k,v in df.items()}
CUTS=[0,187.1,662.95,1820.8,2186.85,3176.0,3500.7,4274.4]   # D0 | D1..D6
res=[]
for k,(title,kick,cards) in enumerate(SLIDES):
    a,b=CUTS[k+1],CUTS[k+2]
    ev=[]
    for ci,(lead,rest) in enumerate(cards):
        t0,s0=best_start(lead+' '+rest,W,a,b,idf)
        ss=sents(rest);prev=t0 or a
        for si,sn in enumerate(ss):
            t,s=best_start(sn,W,prev if si else (t0 or a),b,idf,win=max(8,int(len(sn.split())*1.3)))
            ev.append(dict(card=ci,sent=si,t=t,score=round(s,2)))
            if t and s>=0.3:prev=t
        res.append(None)
    out=dict(arg=k+1,a=a,b=b,events=ev)
    json.dump(out,open(f'/tmp/w18/al_{k+1}.json','w'))
    print('== ARG',k+1,title,a,b)
    for e in ev:
        print(' card',e['card'],'sent',e['sent'],'t',e['t'],'score',e['score'])
