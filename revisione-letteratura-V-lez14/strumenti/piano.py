# piano dei pezzi del prof (D*) per le due parti: stati (slide, card attiva) su tempo originale
import json,re,sys
sys.path.insert(0,'/tmp/w14')
from evid import evidenzia
TR=json.load(open('/tmp/w14/slidetrack_raw.json'))
OFF=json.load(open('/tmp/w14/offsets.json'))
def sid(txt):
    t=txt.lower()
    if 'luigi pirandello' in t and 'crisi' not in t and len(t)<40: return 1
    if 'nasce' in t: return 2
    if 'trappola' in t: return 4
    if 'crisi del primo' in t: return 3
    if 'mattia' in t: return 46
    if 'uno, nessuno' in t: return 48
    if 'teatro grottesco' in t: return 49
    if 'rivoluzione' in t: return 50
    if 'enrico' in t: return 51
    if 'ultima produzione' in t: return 52
    if 'ultime novelle' in t: return 53
    if 'ciaula' in t: return 'C'
    if 'treno' in t: return 'B'
    raise Exception(txt)
SL=[(a,b,sid(t)) for a,b,t in TR]
# unisci consecutivi identici
M=[]
for a,b,s in SL:
    if M and M[-1][2]==s and abs(M[-1][1]-a)<0.5: M[-1][1]=b
    else: M.append([a,b,s])
def stati(s0,s1):
    """lista (t0,t1,slide,card) su tempo originale, tra s0 e s1"""
    out=[]
    for a,b,s in M:
        x0,x1=max(a,s0),min(b,s1)
        if x1-x0<=0.01: continue
        if s in (3,4,46,47,48,49,50,51,52,53):
            for u,v,c in evidenzia(s,a,b):
                y0,y1=max(u,x0),min(v,x1)
                if y1-y0>0.01: out.append([y0,y1,s,c])
        elif s in ('C','B'):
            import libro
            for u,v,k in libro.stato(s,a,b):
                y0,y1=max(u,x0),min(v,x1)
                if y1-y0>0.01: out.append([y0,y1,s,k])
        else: out.append([x0,x1,s,None])
    # unisci
    R=[]
    for x in out:
        if R and R[-1][2:]==x[2:] and abs(R[-1][1]-x[0])<0.05: R[-1][1]=x[1]
        else: R.append(x)
    return R
if __name__=='__main__':
    for x in stati(181.17,940.17): print([round(v,1) if isinstance(v,float) else v for v in x])
