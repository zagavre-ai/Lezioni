import sys,os,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import build_prof as B
O='/tmp/w/work/out'
# numerazione pagine come prima: P1 da 3, P2 da 3 (le pagine dei pezzi non rifatti restano nei json)
pag={1:3}
for g,p0 in [([1,2,3],3),([4,5,6,7],3)]:
    p=p0
    for t in g:
        if t in (1,2,3,4,6):
            d,pl=B.build(t,p,O); print('D',t,d,pl,flush=True)
        else:
            st,pl=B.stati_topic(t,p)
        p=pl+1
open(O+'/prof2.fatto','w').close()
