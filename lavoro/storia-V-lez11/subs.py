import sys,os,json,re
sys.path.insert(0,'/home/user/work/build')
from kit2 import *
CORR=[
 (r"\bL'?[Uu][Rr][Ss]{1,2}\b","L'URSS"),(r"\b(?:l'|L')?[Uu]rs\b","URSS"),(r"\bURS\b","URSS"),(r"\bLURS\b","L'URSS"),
 (r"\bYo(?:s|sh)if\b","Iosif"),(r"\bYosef\b","Iosif"),(r"\bYoshif\b","Iosif"),(r"La scesa di Stalin","L'ascesa di Stalin"),
 (r"\bTroz(?:zi|ki|ky|k|kij|ski)\b","Trockij"),(r"\bLe Trockij","Lev Trockij"),(r"\bLe Trozki","Lev Trockij"),
 (r"\bNikolai\b","Nikolaj"),(r"\bBu?ca?rin\b","Bucharin"),(r"\bBukharin\b","Bucharin"),(r"\bBucarin\b","Bucharin"),
 (r"\bZinov e Kamenev\b","Zinov'ev e Kamenev"),(r"\bCosplom\b","Gosplan"),(r"\bGosplom\b","Gosplan"),
 (r"\b[Dd]e?culac\w*","dekulakizzazione"),(r"\b[Cc]ula(?:ki|chi|ci|k)\b","kulaki"),(r"\bkulakki\b","kulaki"),
 (r"\bi Colcoats\b","i kolchoz"),(r"\bColcoats\b","kolchoz"),(r"\bi soft\b","i sovchoz"),(r"\bsoftcoats\b","sovchoz"),
 (r"\b[Oo]lodomor\b","Holodomor"),(r"\bHolodomor\b","Holodomor"),(r"\bAlexei\b","Aleksej"),(r"\bstacanov\w*","stachanov"),
 (r"\bKomsomon\b","Komsomol"),(r"\bFurer\b","Führer"),(r"\bMalotovri e Trump\b","Molotov-Ribbentrop"),
 (r"\bMolotovry\b","Molotov-Ribbentrop"),(r"\bMolotov\b(?!-)","Molotov-Ribbentrop"),(r"\bPalm(?:in|ir)o Togliatti\b","Palmiro Togliatti"),
 (r"\bPalmin Togliatti\b","Palmiro Togliatti"),(r"\bStalino\b","Stalin"),(r"\bil cosiddetto PC\b","il cosiddetto PCUS"),
 (r"\bmillovecentotrentaquattro\b","1934"),(r"\bnell'?Unione sovietica\b","nell'Unione Sovietica"),
 (r"\bsociet[àa] delle nazioni\b","Società delle Nazioni"),(r"\bBukarin\b","Bucharin"),(r"\bBolshevico\b","bolscevico"),
 (r"\bUN\b","URSS"),
 (r"per estremazi di sintesi","per estrema sintesi"),(r"meno male delle tracce su un possibile erete","meno male delle tracce su un possibile erede"),(r"poteva anche inquorare molti","poteva anche inquietare molti"),(r"lo disignò il rete di Lenin e lui assunse le guida alle redini","lo designò erede di Lenin e lui assunse le redini"),(r"l'Un Sovietica","l'Unione Sovietica"),(r"per Antonomasi è diventati i Gulag","per antonomasia sono diventati i Gulag"),(r"mi possono fare le scale","mi possono fare le scarpe"),(r"dopo le Purg\b","dopo le purghe"),(r"il nostro Salima","il nostro Stalin"),(r"il pattoresse un anno","il patto durò un anno"),(r"una settimana dopo scopia","una settimana dopo scoppia"),(r"Per Stridovsk","Per Brest-Litovsk"),(r"scopia anche perché Italsi si sente forte","scoppia anche perché l'Italia si sente forte"),(r"\b(?:Uh|Um|Mm|Hmm)\b[.,]?",""),
]
def corr(s):
    for a,b in CORR: s=re.sub(a,b,s)
    s=re.sub(r"\s+"," ",s).strip()
    return s
def words_prof():
    segs=json.load(open(B+'/../trasc_orig.json'));W=[]
    for s in segs:
        cur=None
        for t,tok in s['parole']:
            if tok.startswith(' ') or cur is None:
                if cur: W.append(cur)
                cur=[t,tok.strip()]
            else: cur[1]+=tok
        if cur: W.append(cur)
        W.append([s['fine'],None])   # marcatore fine segmento
    return W
def cue_split(items,maxc=84):
    """items: [(t,parola)]; ritorna cues [(t0,t1,testo)]"""
    cues=[];cur=[]
    def flush():
        nonlocal cur
        if cur:
            cues.append([cur[0][0],cur[-1][0]+0.5,' '.join(w for _,w in cur)]);cur=[]
    for i,(t,w) in enumerate(items):
        if w is None: flush();continue
        if cur:
            txt=' '.join(x for _,x in cur)+' '+w
            if len(txt)>maxc or t-cur[0][0]>6.0 or t-cur[-1][0]>1.4 or (cur[-1][1][-1:] in '.?!' and len(txt)>30): flush()
        cur.append((t,w))
    flush()
    for k in range(len(cues)-1):
        cues[k][1]=min(cues[k][1],cues[k+1][0]-0.04)
    return cues
def wrap(t,w=42):
    words=t.split();lines=[];cur=''
    for x in words:
        if len(cur)+len(x)+1>w and cur: lines.append(cur);cur=x
        else: cur=(cur+' '+x).strip()
    lines.append(cur);
    if len(lines)>2: lines=[' '.join(lines[:len(lines)//2+len(lines)%2]),' '.join(lines[len(lines)//2+len(lines)%2:])]
    return '\n'.join(lines)
def ts(s):
    h,r=divmod(s,3600);m,r=divmod(r,60);return '%02d:%02d:%06.3f'%(h,m,r)
def make_vtt(tl,out):
    starts={n:(s,d) for n,s,d in tl}
    cues=[]
    W=words_prof()
    PROF={'D0':(0.0,57.6),'D1':(57.6,357.35),'D2':(357.35,471.7),'D3':(471.7,874.25),'D4':(874.25,1022.85),'D5':(1022.85,1145.55),'D6a':(1145.55,1322.3),'D6b':(1322.3,1413.8),'D6c':(1413.8,1506.13)}
    for nm,(a,b) in PROF.items():
        if nm not in starts: continue
        vs=starts[nm][0]
        it=[(t,w) for t,w in W if a-0.01<=t<b]
        for c0,c1,tx in cue_split(it):
            cues.append((vs+c0-a,vs+min(c1,b)-a,corr(tx)))
    # voci Kore
    def kv(name,t0):
        txt=TXT[name];p=vpath(name)
        for a,b,f in tempi_frasi(name,txt):
            cues.append((t0+a,t0+b+0.2,cifre(f)))
    def S(n): return starts[n][0]
    if 'COVER_A' in starts: kv('BENV1_R2',S('COVER_A')+0.5)
    for t in range(1,7):
        n=f'AN_T{t}'
        if n in starts:
            o=0.5
            for k in range(3*t-2,3*t+1):
                kv(f'AN{k}',S(n)+o);o+=dur(vpath(f'AN{k}'))+0.7
        for mp,nm,v in (('MAP1',1,'MP1'),('MAP23',3,'MP23'),('MAP4',4,'MP4')):
            if nm==t and mp in starts: kv(v,S(mp)+1.0)
        if f'PIL{t}' in starts: kv(f'R{t}',S(f'PIL{t}')+1.0)
        if f'SCH_T{t}' in starts:
            x=0.7
            for i in range(1,len([k for k in TXT if re.fullmatch(f'SC{t}_\\d',k)])+1):
                kv(f'SC{t}_{i}',S(f'SCH_T{t}')+x);x+=dur(vpath(f'SC{t}_{i}'))+0.4
    if 'GLOSS' in starts:
        o=0.5
        for g in ('GL1','GL2'): kv(g,S('GLOSS')+o);o+=dur(vpath(g))+0.8
    for nm,v,t0 in (('FINALE','RIEP1',1.0),('FINE','FIN1',1.0),('COMP_INTRO','COMPI',0.9)):
        if nm in starts: kv(v,S(nm)+t0)
    if 'COMPITI_SL' in starts:
        o=0
        for v in ('COMP1','COMP2'): kv(v,S('COMPITI_SL')+o+0.6);o+=dur(vpath(v))+1.4
    cues.sort()
    # niente sovrapposizioni
    out_l=[]
    for i,(a,b,t) in enumerate(cues):
        if i+1<len(cues): b=min(b,cues[i+1][0]-0.03)
        if b-a<0.3: continue
        out_l.append((a,b,t))
    with open(out,'w') as f:
        f.write('WEBVTT\n\n')
        for i,(a,b,t) in enumerate(out_l,1): f.write(f'{i}\n{ts(a)} --> {ts(b)}\n{wrap(t)}\n\n')
    return len(out_l)
