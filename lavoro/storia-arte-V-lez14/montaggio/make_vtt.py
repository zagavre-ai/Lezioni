import sys,re,json;sys.path.insert(0,'/tmp/w/build')
import plan
from engine import *
tl=plan.build();segs=tl.segs
off=0;offs=[]
for s in segs:offs.append(off);off+=s['n']
from fixes import REP,DROP,fix
NUM=[("millenovecentoventisette","1927"),("millenovecentoventotto","1928"),("millenovecentotrentasette","1937"),("millenovecentotrentatré","1933"),("millenovecentotrentasei","1936"),("millenovecentoventinove","1929"),
 ("millenovecentodieci","1910"),("millenovecentoventicinque","1925"),("millenovecentoquarantaquattro","1944"),("millenovecentoquaranta","1940"),("ventisei aprile","26 aprile"),("quattro giugno","4 giugno"),("ottanta per cento","80%"),("Dieci domande","10 domande"),("cinque domande","5 domande")]
def numfix(t):
    for a,b in NUM:t=t.replace(a,b)
    return t
cues=[]
def addcue(t0,t1,text):
    # max 2 righe da 42 caratteri
    words=text.split();lines=[];cur=''
    for w in words:
        if len((cur+' '+w).strip())>42 and cur:lines.append(cur);cur=w
        else:cur=(cur+' '+w).strip()
    if cur:lines.append(cur)
    chunks=[lines[i:i+2] for i in range(0,len(lines),2)]
    tot=sum(len(' '.join(c)) for c in chunks) or 1;t=t0
    for c in chunks:
        d=(t1-t0)*len(' '.join(c))/tot;cues.append((t,t+d,'\n'.join(c)));t+=d
# docente
for i,s in enumerate(segs):
    if s['spec']['k']!='prof' or not s['name'].startswith('D'):continue
    x0=s['spec']['f0'];x1=x0+s['n'];o=offs[i]
    for g in plan.SEG:
        a=g['inizio']*FPS;b=g['fine']*FPS
        if b<x0 or a>=x1:continue
        t=g['testo'].strip()
        if DROP.match(t):continue
        t=fix(t)
        if not t:continue
        ta=(max(a,x0)-x0+o)/FPS;tb=(min(b,x1)-x0+o)/FPS
        if tb-ta<0.3:tb=ta+0.5
        addcue(ta,tb,t)
# voci Kore
for (idx,name,L) in plan.VC:
    v,starts,sents,prov=plan.voice(name,plan.TESTI);o=offs[idx]/FPS
    for k,sn in enumerate(sents):
        ta=o+L+starts[k];tb=o+L+(starts[k+1]-0.1 if k+1<len(starts) else len(v)/SR)
        addcue(ta,tb,numfix(sn))
cues.sort()
def ts(t):return '%02d:%02d:%06.3f'%(t//3600,(t%3600)//60,t%60)
out=['WEBVTT','']
for a,b,t in cues:out+= [f'{ts(a)} --> {ts(b)}',t,'']
open('/tmp/w/build/Storia_arte_Lez14_Parte1.vtt','w').write('\n'.join(out))
print(len(cues),'sottotitoli')
