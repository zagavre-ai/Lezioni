import json
S=json.load(open('../trasc_V.json'))
M=[(0.15,45.933,96.0),(96.15,148.133,150.5),(245.65,623.333,150.433),(395.56,1128.466,181.0),(575.82,1665.067,335.166),(910.17,2405.599,331.2)]
def build():
    out=[]
    for O,V,d in M:
        for s in S:
            if V-0.01<=s['inizio']<V+d:
                out.append({'a':s['inizio']-V+O,'b':min(s['fine'],V+d)-V+O,'testo':s['testo'],'parole':[(t-V+O,w) for t,w in s['parole']]})
    out.sort(key=lambda x:x['a'])
    ded=[]
    for u in out:
        if ded and u['a']<ded[-1]['b']-0.2 and u['testo'][:20]==ded[-1]['testo'][:20]: continue
        ded.append(u)
    return ded
if __name__=='__main__':
    U=build();json.dump(U,open('../orig_trans.json','w'),ensure_ascii=False);print(len(U),U[-1]['b'])
