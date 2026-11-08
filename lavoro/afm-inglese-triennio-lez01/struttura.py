# Struttura della lezione: argomenti, sottotitoli, unità (frasi) e tabelle aggiunte
import json,re
B=json.load(open('/home/claude/lezioni/afm-inglese-triennio-lez01/blocks.json'))
ARG=[ # (primo blocco, titolo argomento)
 (0,'Globalisation'),
 (35,'Technological advancement'),
 (48,'Diversity and inclusion'),
 (52,'World instability'),
 (63,'Environmental concerns'),
]
SUB=[ # (primo blocco, sottotitolo della slide)
 (0,'Global factors'),(9,'Globalisation'),(12,'Definition'),(18,'Key factors'),(29,'Good or bad?'),
 (35,'Technological advancement'),(37,'Industry 4.0'),(43,'Industry 4.0 technologies'),
 (48,'Diversity and inclusion'),
 (52,'World instability'),(54,'A wave of instability'),(59,'Covid-19'),
 (63,'Environmental concerns'),(64,'Climate change and business'),
]
INSERT_AFTER={}
SUPER=range(0)

def txt(runs): return ''.join(t for _,t in runs)
def split_runs(runs,maxlen=330):
    """divide un paragrafo in frasi mantenendo i grassetti"""
    s=txt(runs); cut=[0]
    for m in re.finditer(r'(?<! n)(?<!Lgs)(?<=[a-zàèéìòù0-9\)%”»"])\. (?=[A-ZÈÉ0-9L])',s): cut.append(m.end())
    cut.append(len(s))
    # unisci frasi troppo corte alla successiva
    segs=[(cut[i],cut[i+1]) for i in range(len(cut)-1)]
    out=[]
    for a,b in segs:
        if out and (b-a<60 or out[-1][1]-out[-1][0]<60) and (b-out[-1][0])<maxlen: out[-1]=(out[-1][0],b)
        else: out.append((a,b))
    res=[]
    for a,b in out:
        rr=[];pos=0
        for bo,t in runs:
            s0,s1=pos,pos+len(t);pos=s1
            x0,x1=max(a,s0),min(b,s1)
            if x1>x0: rr.append([bo,t[x0-s0:x1-s0]])
        rr[0][1]=rr[0][1].lstrip(); rr[-1][1]=rr[-1][1].rstrip()
        res.append(rr)
    return res
def units():
    U=[]
    ai=-1; si=-1
    for i,b in enumerate(B):
        na=[k for k,(s,_) in enumerate(ARG) if s<=i][-1]
        ns=[k for k,(s,_) in enumerate(SUB) if s<=i][-1]
        if i in SUPER:
            m=re.match(r"super (\d+)'s, con un diametro massimo delle fibre di ([\d,]+) micron",txt(b['runs']))
            if U and U[-1]['t']=='super': U[-1]['rows'].append([f"super {m.group(1)}'s",m.group(2)+' micron'])
            else: U.append({'t':'super','rows':[[f"super {m.group(1)}'s",m.group(2)+' micron']],'a':na,'s':ns,'b':i,'pg':b['pg'],
                            'txt':'super 80 90 100 110 120 130 140 150 160 170 180 190 200 210 220 230 240 250 diametro massimo micron'})
            continue
        parts=split_runs(b['runs']) if b['t']=='p' or len(txt(b['runs']))>330 else [b['runs']]
        for k,r in enumerate(parts):
            U.append({'t':b['t'] if k==0 else ('cont' if b['t']=='li' else 'p'),'runs':r,'a':na,'s':ns,'b':i,'pg':b['pg'],'txt':txt(r),'par0':k==0})
        for T in INSERT_AFTER.get(i,[]):
            d=dict(T); d.update({'a':na,'s':ns,'b':i,'pg':b['pg'],'txt':' '.join(' '.join(r) for r in T['rows'])}); U.append(d)
    return U
if __name__=='__main__':
    U=units(); print(len(U)); import collections
    print(collections.Counter(u['t'] for u in U))
    print(max(len(u['txt']) for u in U if u['t'] in('p','li','cont')))
    json.dump(U,open('/home/claude/lezioni/afm-inglese-triennio-lez01/units.json','w'),ensure_ascii=False)
