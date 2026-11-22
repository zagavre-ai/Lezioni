import sys, json, os
sys.path.insert(0,'/home/user/Lezioni/lavoro')
import mont, piani, kore_pezzi
from build_prof import P, ST
done=f'{mont.B}/prof_ok';os.makedirs(done,exist_ok=True)
def build(pid):
    p=P[pid]
    if pid in ('D0','DI'):
        c,d=kore_pezzi.D0_DI_slides();png=c if pid=='D0' else d
        st=[(p['s0'],png)];g=mont.misura_gain(p['ranges'])
        return mont.pezzo_prof(pid,p['ranges'],st,f'{mont.B}/{pid}.mkv',g)
    n=p['arg'];g=mont.misura_gain(p['ranges'])
    st=[(t,f"/tmp/w/sl/{k}.png") for t,k in ST[str(n)] if t<p['s1']]
    before=[x for x in st if x[0]<=p['s0']];st=[x for x in st if x[0]>p['s0']]
    st.insert(0,(p['s0'],before[-1][1] if before else st[0][1]))
    return mont.pezzo_prof(pid,p['ranges'],st,f'{mont.B}/{pid}.mkv',g)
if __name__=='__main__':
    ids=sys.argv[1:] or list(P)
    for pid in ids:
        if os.path.exists(f'{done}/{pid}'): continue
        d=build(pid);open(f'{done}/{pid}','w').write(str(d));print(pid,round(d,1),flush=True)
