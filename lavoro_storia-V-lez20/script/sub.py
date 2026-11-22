import sys,json,re
sys.path.insert(0,'/tmp/w/b')
from prof import S,mapper
from voicelib import *
import plan,content
part=int(sys.argv[1]);out=sys.argv[2]
META=json.load(open('/tmp/w/b/ch/meta.json'))
CORR=[(r'\bJugoslavi',"Iugoslavi"),(r'\b(Yelsin|Yeltsin|Elcin|Nielsen)\b',"Eltsin"),(r'\bMilosevi(ch|ci|c)?\b',"Milošević"),(r'\bGorbachev\b',"Gorbaciov"),(r'\bTenammen\b',"Tienanmen"),
 (r'\bURS\b',"URSS"),(r'\bNato\b',"NATO"),(r'\bAl Qaida\b',"Al-Qaeda"),(r'\bQaida\b',"Qaeda"),(r'\bPlurbo\b',"limbo"),(r'\bSadam\b',"Saddam"),(r'\bKiril\b',"Kirill"),
 (r'\bDegnemente\b',"Degnamente"),(r'\bGebe\b',"KGB"),(r'\bOrban\b',"Orbán"),(r'\bErdogan\b',"Erdoğan"),(r'\bKuit\b',"Kuwait"),(r'\bKuwait\b',"Kuwait"),(r'\bFukuyami\b',"Fukuyama"),(r'\bmanipulite\b',"Mani pulite"),(r'\bJugoslavia\b',"Iugoslavia")]
def fix(t):
    for a,b in CORR: t=re.sub(a,b,t)
    return t
TL=json.load(open(f'/tmp/w/b/timeline_P{part}.json'))
lead=0.8
cues=[]
def ts(t):
    h=int(t//3600);m=int(t%3600//60);s=t%60;return '%02d:%02d:%06.3f'%(h,m,s)
def wrap(t):
    # max 2 righe da 42 caratteri
    w=t.split();L=[];cur=''
    for x in w:
        if len(cur)+len(x)+1>42 and cur: L.append(cur);cur=x
        else: cur=(cur+' '+x).strip()
    L.append(cur);return '\n'.join(L)
def add(t0,t1,txt):
    txt=' '.join(txt.split())
    if len(txt)<=84: cues.append((t0,t1,wrap(txt)));return
    w=txt.split();chunks=[];cur=''
    for x in w:
        if len(cur)+len(x)+1>80 and cur: chunks.append(cur);cur=x
        else: cur=(cur+' '+x).strip()
    chunks.append(cur);tot=sum(len(c) for c in chunks);t=t0
    for c in chunks:
        d=(t1-t0)*len(c)/tot;cues.append((t,t+d,wrap(c)));t+=d
for name,start,dur_ in TL:
    key=name[1:] if name[0]=='D' and name[1:] in META else None
    if key:
        m=META[key];iv=[tuple(x) for x in m['iv']];f,_=mapper(iv)
        for i in range(m['i0'],m['i1']+1):
            seg=S[i];words=[];cur=None
            for t,tok in seg['parole']:
                if tok.startswith(' ') or cur is None: cur=[t,tok.strip()];words.append(cur)
                else: cur[1]+=tok
            # cue: <=84 caratteri, <=6 s
            blk=[];
            def flush():
                global blk
                if blk:
                    t0=start+lead+f(blk[0][0]);t1=start+lead+f(min(blk[-1][0]+0.5,seg['fine']))
                    t1=max(t1,t0+0.8);add(t0,t1,fix(' '.join(w[1] for w in blk)));blk=[]
            for w in words:
                if blk and (len(' '.join(x[1] for x in blk+[w]))>84 or w[0]-blk[0][0]>5.5): flush()
                blk.append(w)
                if re.search(r'[.?!]$',w[1]): flush()
            flush()
    else:
        voice=None
        # pezzi con voce Kore: sottotitoli dalle frasi
        pass
# voci Kore: leggiamo i pezzi dal piano
P=(plan.build_part1() if part==1 else plan.build_part2())[0]
for p in P:
    sub=getattr(p,'subtitle',None)
    if not sub: continue
    st=[x for x in TL if x[0]==p.name]
    if not st: continue
    start=st[0][1]
    for t0,t1,txt in sub: add(start+t0,start+t1,txt)
cues.sort()
# niente sovrapposizioni
for i in range(len(cues)-1):
    if cues[i][1]>cues[i+1][0]: cues[i]=(cues[i][0],cues[i+1][0]-0.02,cues[i][2])
open(out,'w').write('WEBVTT\n\n'+''.join(f'{ts(a)} --> {ts(b)}\n{t}\n\n' for a,b,t in cues if b>a))
print(len(cues),'cue')
