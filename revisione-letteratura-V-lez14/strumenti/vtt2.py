import json,re,sys,os
sys.path.insert(0,'/tmp/w14')
from evid import ricostruisci
P=int(sys.argv[1])
NT=json.load(open(f'/tmp/w14/as{P}/tl_new.json'))['tl']
PLN=json.load(open(f'/tmp/w14/dn{P}/plan.json'))['plan']
def words_of(name): return [(t,w) for t,w in ricostruisci(json.load(open(f'/tmp/w14/tr/{name}.json')))]
O=words_of('orig');OLD=words_of(f'P{P}')
W=[]
for name,ns,dur,os_ in NT:
    if name in PLN:
        s0=PLN[name]['s0']
        for t,w in O:
            if s0<=t<s0+dur: W.append((ns+t-s0,w))
    elif name=='R1':
        if os.path.exists('/tmp/w14/tr/R1.json'):
            for t,w in words_of('R1'): W.append((ns+0.4+t,w))
    else:
        for t,w in OLD:
            if os_<=t<os_+dur: W.append((ns+t-os_,w))
W.sort()
FIX=[(r'\bCiaola\b','Ciàula'),(r'\bciaola\b','Ciàula'),(r'\bCiaula\b','Ciàula'),(r'\bAdriano Mais\b','Adriano Meis'),(r'\bMais\b','Meis'),(r'\bPascale\b','Pascal'),(r'\bPascala\b','Pascal'),(r'\bMatia\b','Mattia'),(r"\b[Zz]iscarda\b","zi' Scarda"),(r'\bMuscarda\b','Moscarda'),(r'\bCasino\b','Casinò'),(r'\bcasino\b','casinò'),(r'\bGirgenti\b','Girgenti'),(r'\bpirandello\b','Pirandello'),(r'\bbelluca\b','Belluca')]
def fix(s):
    for a,b in FIX: s=re.sub(a,b,s)
    return s
cues=[];cur=[]
def flush():
    global cur
    if cur:
        txt=fix(' '.join(w for t,w in cur));cues.append([cur[0][0],cur[-1][0]+0.5,txt]);cur=[]
for i,(t,w) in enumerate(W):
    if cur:
        gap=t-cur[-1][0];chars=len(' '.join(x for _,x in cur))+1+len(w);dur=t-cur[0][0]
        if gap>0.8 or chars>80 or dur>6 or (cur[-1][1][-1] in '.?!' and chars>38 and dur>1.5):
            flush()
    cur.append((t,w))
flush()
def lines(s):
    if len(s)<=42: return s
    m=len(s)//2;l=s.rfind(' ',0,m+8);r=s.find(' ',m)
    k=min([x for x in (l,r) if x>0],key=lambda x:abs(x-m))
    return s[:k]+'\n'+s[k+1:]
def ts(x): return '%02d:%02d:%06.3f'%(x//3600,(x%3600)//60,x%60)
out=['WEBVTT\n']
for i,(a,b,t) in enumerate(cues):
    if i+1<len(cues): b=min(b,cues[i+1][0]-0.02)
    b=max(b,a+0.6)
    out.append(f'{ts(a)} --> {ts(b)}\n{lines(t)}\n')
open(f'/tmp/w14/out/Letteratura_Lez14_Parte{P}.vtt','w',encoding='utf-8').write('\n'.join(out))
print(P,len(cues),'cue',max(len(l) for c in cues for l in lines(c[2]).split('\n')),'max car/riga')
