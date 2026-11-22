import sys, json, os
sys.path.insert(0,'/home/user/Lezioni/lavoro')
import mont, piani
ST=json.load(open('/tmp/w/stati.json'))['stati']
P={p['id']:p for p in piani.pezzi()}
def build(pid,gain=0.0):
    p=P[pid];n=p['arg'];out=f"{mont.B}/{pid}.mkv"
    if pid=='D0' or pid=='DI': raise SystemExit('D0/DI: pezzi speciali')
    st=[(t,f"/tmp/w/sl/{k}.png") for t,k in ST[str(n)] if t<p['s1']]
    # stato attivo a s0
    before=[x for x in st if x[0]<=p['s0']]
    st=[x for x in st if x[0]>p['s0']]
    st.insert(0,(p['s0'],before[-1][1] if before else st[0][1]))
    return mont.pezzo_prof(pid,p['ranges'],st,out,gain), out
if __name__=='__main__':
    d,o=build(sys.argv[1]);print(o,d)
