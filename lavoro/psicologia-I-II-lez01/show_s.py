import json,sys
D=json.load(open('align_s.json'));U=json.load(open('units.json'))
lo,hi=float(sys.argv[1]),float(sys.argv[2])
own={}
for o in D['align']:
    for j in o['sent']: own[j]=o['i']
starts={}
for o in D['align']: starts.setdefault(o['t'],[]).append(o['i'])
prev=None
for j,s in enumerate(D['S']):
    if not lo<=s['t']<=hi: continue
    i=own.get(j)
    if i!=prev:
        ids=[x for x in starts.get(s['t'],[]) ]
        print(f"   >>> #{','.join(map(str,ids)) or i}: {' | '.join(U[x]['txt'][:55] for x in ids) if ids else U[i]['txt'][:55]}")
    print(f"{s['t']:7.1f} {s['txt'][:120]}")
    prev=i
