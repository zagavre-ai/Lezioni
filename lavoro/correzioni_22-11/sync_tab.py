import sys,json,random;sys.path.insert(0,'/home/work/build')
import plan as PL, prof
random.seed(17)
PARTI={1:[1,2,3],2:[4,5],3:[6,7,8]}
out={}
for P in (1,2,3):
    rows=[]
    for n in PARTI[P]:
        asg=PL.assign(n);cards=PL.CARDS[n]['cards'];prev=-9
        for t0,t1,c in asg:
            if c!=prev and c>=0:
                seg=[s for s in PL.S if abs(s['inizio']-t0)<0.02][0]['testo'][:70]
                rows.append((n,c,t0,t0-0.25,(cards[c]['lead']+' '+cards[c]['text'])[:55],seg))
            prev=c
    random.shuffle(rows);out[P]=sorted(rows[:10],key=lambda r:r[2])
json.dump(out,open('/home/work/build/sync_tab.json','w'),ensure_ascii=False)
for P in out:
    print(P)
    for r in out[P][:3]:print(r)
