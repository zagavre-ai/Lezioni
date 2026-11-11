import json,sys
W=[]
for l in open('pk.jsonl'): W+=json.loads(l)['w']
a,b=float(sys.argv[1]),float(sys.argv[2])
cur=None;line=[]
for t,w in W:
    if a<=t<=b:
        if not line:cur=t
        line.append(w)
        if w[-1] in '.?!':print('%7.2f'%cur,' '.join(line));line=[]
if line:print('%7.2f'%cur,' '.join(line))
