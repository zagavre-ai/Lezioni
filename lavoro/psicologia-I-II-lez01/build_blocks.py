import json,re
P=json.load(open('pdf_lines.json'))
blocks=[]
for pi,lines in enumerate(P):
    if pi==0: continue
    for l in lines:
        txt=''.join(t for b,t in l['runs'])
        if not txt.strip(): continue
        if l['size']<14: continue          # testi delle tabelle-immagine
        isb=re.match(r'^\s*-\s',txt) is not None
        runs=[list(r) for r in l['runs']]
        if isb and blocks and blocks[-1]['t']=='li' and re.match(r'^\s*-\s+[a-zàèéìòù]',txt) and ''.join(t for b,t in blocks[-1]['runs']).rstrip()[-1:] not in ';.:':
            for r in runs:
                if r[1].strip():
                    r[1]=re.sub(r'^\s*-\s*','',r[1],count=1); break
            blocks[-1]['runs'].append([False,' ']); blocks[-1]['runs']+=runs; continue
        if isb:
            for r in runs:
                if r[1].strip():
                    r[1]=re.sub(r'^\s*-\s*','',r[1],count=1); break
            blocks.append({'t':'li','runs':runs,'pg':pi+1}); continue
        prev=blocks[-1] if blocks else None
        ptxt=''.join(t for b,t in prev['runs']).rstrip() if prev else ''
        newpar=prev is None or (l['x']<16 and ptxt[-1:] in '.:;' and not re.match(r'^[a-zàèéìòù]',txt))
        if prev and prev['t']=='li' and l['x']>40: newpar=False
        if prev and prev['t']=='li' and l['x']<16: newpar=True
        if newpar: blocks.append({'t':'p','runs':runs,'pg':pi+1})
        else:
            prev['runs'].append([False,'' if ptxt.endswith("'") else ' ']); prev['runs']+=runs
for b in blocks:
    m=[]
    for bo,t in b['runs']:
        if m and m[-1][0]==bo: m[-1][1]+=t
        else: m.append([bo,t])
    b['runs']=[[bo,re.sub(r'\s+',' ',t)] for bo,t in m]
    b['runs'][0][1]=b['runs'][0][1].lstrip(); b['runs'][-1][1]=b['runs'][-1][1].rstrip()
json.dump(blocks,open('blocks.json','w'),ensure_ascii=False,indent=0)
print(len(blocks))
