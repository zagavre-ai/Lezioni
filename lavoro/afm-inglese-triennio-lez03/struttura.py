# Struttura della lezione: argomenti, sottotitoli, unità (frasi) e tabelle aggiunte
import json,re
B=json.load(open('/home/claude/lezioni/afm-inglese-triennio-lez03/blocks.json'))
# correzioni del testo estratto (righe sovrapposte nel PDF, refusi evidenti: segnalati nel report)
FIX={
 24:[[True,'Primary sector'],[False,': industries acquiring '],[True,'raw materials '],[False,'to make other products (agriculture, forestry, fishing, mining, oil industries).']],
 25:[[True,'Secondary sector'],[False,': industries converting raw materials into '],[True,'semi-finished or finished goods '],[False,'(manufacturing, building, clothing, food, furnishing industries).']],
}
REPL={50:('governments offers','governments offer'),51:('costs increases','costs increase'),53:('that is has','that it has'),93:('It consists is ','It consists in ')}
for i,r in FIX.items(): B[i]['runs']=r
for i,(a,b) in REPL.items():
    for r in B[i]['runs']: r[1]=r[1].replace(a,b)
for b in B:
    b['runs']=[r for r in b['runs'] if r[1]]
    b['runs'][0][1]=b['runs'][0][1].lstrip()
SKIP={65,75,81,87}   # titoli di sezione letti come elenco
ARG=[ # (primo blocco, titolo argomento)
 (0,'Production and sectors of production'),
 (33,'Economies of scale'),
 (58,'Quality control and smart manufacturing'),
 (72,'Relocation of business operations'),
 (93,'Focus: the circular economy'),
]
SUB=[ # (primo blocco, sottotitolo della slide)
 (0,'Production'),(6,'Production and sectors of production'),(10,'What is production?'),(17,'Economic resources'),
 (23,'Sectors of production'),(29,'The supply chain'),
 (33,'Economies of scale'),(35,'Economies of scale'),(41,'Internal and external economies'),(51,'Diseconomies of scale'),
 (58,'Quality control and smart manufacturing'),(60,'Quality control'),(66,'Smart manufacturing'),
 (72,'Relocation of business operations'),(76,'Why relocate?'),(82,'Offshoring vs. reshoring'),(88,'Reshoring'),
 (93,'The circular economy'),
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
        if i in SKIP: continue
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
    json.dump(U,open('/home/claude/lezioni/afm-inglese-triennio-lez03/units.json','w'),ensure_ascii=False)
