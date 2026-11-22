import json,re
D=json.load(open('/tmp/w/trasc.json'))
def seg_text(i): return D[i]['testo']
# lista parole con tempo
W=[]
for si,s in enumerate(D):
    cur=None
    for t,tok in s['parole']:
        if tok.startswith(' ') or cur is None:
            if cur: W.append(cur)
            cur=[t,tok.strip(),si]
        else: cur[1]+=tok
    if cur: W.append(cur)
def mmss(t): return f"{int(t//60)}:{t%60:04.1f}"
def find(rx,t0=0,t1=1e9,ctx=60):
    txt=' '.join(w[1] for w in W);out=[]
    idx=[];p=0
    for w in W: idx.append(p);p+=len(w[1])+1
    for m in re.finditer(rx,txt,re.I):
        k=max(i for i,x in enumerate(idx) if x<=m.start())
        t=W[k][0]
        if t0<=t<=t1: out.append((t,mmss(t),txt[m.start():m.start()+ctx]))
    return out
if __name__=='__main__':
    import sys
    for r in find(sys.argv[1],float(sys.argv[2]) if len(sys.argv)>2 else 0,float(sys.argv[3]) if len(sys.argv)>3 else 1e9): print(r)
