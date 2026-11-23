# numerazione pagine nella Parte (ordine di apparizione nel video)
import sys,json,re;sys.path.insert(0,'/home/work/build')
import prof
PARTI={1:[1,2,3],2:[4,5],3:[6,7,8]}
MAPDOPO={1:1,6:2,7:3}
def n_sent(t): return len([x for x in re.split(r'(?<=[\.\!\?])\s+',t.strip()) if x])
def layout(P):
    V={v['nome']:v['testo'] for v in json.load(open('/home/work/new/testi_voci_nuovi.json'))}
    nxt=3 if True else 3   # cover=1, Di cosa parliamo=2
    L={};plans={}
    for n in PARTI[P]:
        pl=prof.plan_topic(n);plans[n]=pl
        keys=[]
        for k,v,f in pl['states']:
            if (k,v) not in keys:keys.append((k,v))
        L[n]=dict(prof=nxt,nprof=len(keys));nxt+=len(keys)
        L[n]['ap']=nxt;na=n_sent(V[f'AP{n}']);L[n]['nap']=na;nxt+=na
        L[n]['map']=nxt if n in MAPDOPO else None
        if n in MAPDOPO:nxt+=1
        L[n]['schema']=nxt;nxt+=1
    L['gloss']=nxt;nxt+=1;L['end']=nxt
    return L,plans
if __name__=='__main__':
    for P in (1,2,3):
        L,_=layout(P);print(P,json.dumps({str(k):v for k,v in L.items()}))
