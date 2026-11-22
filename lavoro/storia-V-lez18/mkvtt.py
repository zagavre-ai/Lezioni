# sottotitoli .vtt dal video finale: parlato del prof (trascrizione) + voci Kore (testi)
import sys,json,re
sys.path.insert(0,'/home/user/work18/lib')
from part import *
from cuts import SEG
w=sys.argv[1]
tl=json.load(open(f'{W}/out/timeline_Storia_Lez18_Parte{w}.json'));vl=json.load(open(f'{W}/out/vl_parte{w}.json'))
T={n:(t,d) for n,t,d in tl}
import importlib.util
spec=importlib.util.spec_from_file_location('b18',W+'/build18.py');
FIX=[("Obrigatório",""),("Pietronelli","Pietro Nenni"),("Prebelli","Prebelliche"),("anquanta","anni Cinquanta"),("Comunastico","Comunque"),("d'accordo?",""),("  "," ")]
def clean(t):
    for a,b in FIX:t=t.replace(a,b)
    return re.sub(r'\s+',' ',t).strip()
def ts(t):
    h=int(t//3600);m=int(t%3600//60);s=t%60;return '%02d:%02d:%06.3f'%(h,m,s)
cues=[]
# pezzi del prof
sys.argv=['x'];from build18 import ARG_RANGE,AN_CUT,INTRO_S,A1S,fi
pieces=[(a,b,c) for a,b,c in json.load(open(f'{W}/out/pm_parte{w}.json'))]
for name,ps,pe in pieces:
    vt0=T[name][0];T0=fi(ps)/30
    for s in SEG:
        if s['inizio']>=T0-0.01 and s['fine']<=pe+0.3:
            t=clean(s['testo'])
            if len(t)<2:continue
            cues.append((vt0+s['inizio']-T0,vt0+max(s['fine'],s['inizio']+0.8)-T0,t))
# voci Kore
for t0,name in vl:
    S=sents(name);st=sent_times(name);vd=vdur(name)
    for i,sx in enumerate(S):
        a=t0+st[i];b=t0+(st[i+1] if i+1<len(S) else vd)
        cues.append((a,b,sx))
cues.sort()
out=['WEBVTT','']
for a,b,t in cues:
    words=t.split();lines=[];cur=''
    for x in words:
        if len(cur)+len(x)+1>44 and cur:lines.append(cur);cur=x
        else:cur=(cur+' '+x).strip()
    lines.append(cur)
    out+= [f'{ts(a)} --> {ts(max(b,a+0.6))}','\n'.join(lines),'']
open(f'{W}/out/Storia_Lez18_Parte{w}.vtt','w').write('\n'.join(out));print(len(cues),'cue')
