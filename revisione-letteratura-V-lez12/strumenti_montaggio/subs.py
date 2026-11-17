import json,re,sys
sys.path.insert(0,'.')
import plan
J=json.load(open('states.json'));START=J['START'];FPS=30
U=json.load(open('../orig_trans.json'))
FIX=[(r'\bMer?cel P(?:ro)?[ou]st\w*',"Marcel Proust"),(r'\bMarcel Proustanella\b',"Marcel Proust, nella"),(r'\bP[ou]st\b',"Proust"),(r'\bFust\b',"Proust"),(r'\bPust\b',"Proust"),(r'\bBerk?son\b',"Bergson"),(r'\bBerson\b',"Bergson"),
(r'\b(?:Cow |Mc )?(?:Wulf|Wolf|Wool|Vicina Woolf|vicina Woolf)\b',"Woolf"),(r'\bJod(?:ith|it)\b',"Judith"),(r'\bstranamento\b',"straniamento"),(r'\bCafe\b|\bGafka\b|\bCaf(?:ka|e)\b',"Kafka"),(r'\bSams\b',"Samsa"),(r'\boblivo\b',"oblio"),(r'\blinetto\b',"l'inetto"),(r"\bD'Anzio\b","D'Annunzio"),(r'\bscarafante\b',"scarafaggio"),(r'\bsagistica\b',"saggistica"),(r'\bfalsarica\b',"falsariga"),(r'\bfalsa riga\b',"falsariga"),(r'\bDevo\b',"Svevo"),(r'\bsvevo\b',"Svevo"),(r'\bUlyssis\b',"Ulisse"),(r'\bFrance Kafka\b',"Franz Kafka"),(r'\bperdu\b|\bper due\b',"perduto"),(r'\bPriamo\b',"Prima"),(r"\bposti\b","posti")]
def fix(t):
    for a,b in FIX: t=re.sub(a,b,t)
    return t
def words(u):
    out=[];cur=None
    for t,p in u['parole']:
        if p.startswith(' ') or cur is None:
            if cur: out.append(cur)
            cur=[t,p.strip()]
        else: cur[1]+=p
    if cur: out.append(cur)
    return out
cues=[]
for Dk,(o0,o1) in plan.DSEG.items():
    base=START[Dk]/FPS
    ws=[]
    for u in U:
        for t,w in words(u):
            if o0<=t<o1 and w: ws.append((t-o0+base,w))
    # raggruppa: max 2 righe x 42 car, 1-6 s, spezza su pause >0.5 s e punteggiatura
    cur=[];start=None
    def flush():
        global cur,start
        if not cur: return
        txt=' '.join(w for _,w in cur);txt=re.sub(r'\s+([.,;:!?])',r'\1',txt)
        cues.append((start,cur[-1][0]+0.45,txt));cur=[];start=None
    for i,(t,w) in enumerate(ws):
        if cur and (t-cur[-1][0]>0.8 or (t-start>5.5) or len(' '.join(x for _,x in cur))>70):
            flush()
        if not cur: start=t
        cur.append((t,w))
        if w[-1] in '.?!' and len(' '.join(x for _,x in cur))>22: flush()
    flush()
# correzione e righe
def wrap(t):
    t=fix(t)
    t=t.strip()
    if len(t)<=42: return t
    w=t.split(' ');best=None
    for i in range(1,len(w)):
        a=' '.join(w[:i]);b=' '.join(w[i:]);d=abs(len(a)-len(b))
        if best is None or d<best[0]: best=(d,a,b)
    return best[1]+'\n'+best[2]
def ts(x): h=int(x//3600);m=int(x%3600//60);s=x%60;return '%02d:%02d:%06.3f'%(h,m,s)
out=['WEBVTT\n']
prev_end=0
for n,(a,b,t) in enumerate(cues,1):
    a=max(a,prev_end+0.01);b=max(b,a+0.8)
    if n<len(cues): b=min(b,cues[n][0]-0.02) if cues[n][0]>a+0.8 else b
    out.append(f'{n}\n{ts(a)} --> {ts(b)}\n{wrap(t)}\n');prev_end=b
open('prof_cues.vtt','w').write('\n'.join(out))
print(len(cues))
