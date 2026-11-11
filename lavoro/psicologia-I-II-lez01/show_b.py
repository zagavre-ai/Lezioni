import json,sys
D=json.load(open('align_s.json'));U=json.load(open('units.json'));S=D['S']
lo,hi=float(sys.argv[1]),float(sys.argv[2])
for o in D['align']:
    if not lo<=o['t']<=hi: continue
    j=o['sent'][0] if o['sent'] else None
    pv=S[j-1]['txt'][:70] if j else ''
    cu=S[j]['txt'][:80] if j is not None else '(con la successiva)'
    print(f"#{o['i']:<3}{o['t']:7.1f} PDF «{U[o['i']]['txt'][:45]}»\n      prima: {pv}\n      ORA:   {cu}")
