import json,re,sys
sys.path.insert(0,'/home/user/w/build')
from engine import *
from plan import CH
W='/home/user/w'
TL={n:(t,d) for n,t,d in json.load(open(W+'/out/timeline_edit.json'))}
VC=json.load(open(W+'/out/vc.json'))
cor={}
for f in 'ABC':
    for d in json.load(open(f'{W}/sub/corretta_{f}.json')):cor[d['i']]=d['testo'].strip()
FILL=re.compile(r"^(um|ehm?|yeah|on the|uh|mh)\W*$",re.I)
def ts(t):
    t=max(0,t);h=int(t//3600);m=int(t%3600//60);s=t%60
    return '%02d:%02d:%06.3f'%(h,m,s)
def split_text(txt,maxc=80):
    if len(txt)<=maxc:return [txt]
    parts=re.split(r'(?<=[,;:.?!])\s+',txt);out=[];cur=''
    for p in parts:
        if len(cur)+len(p)+1<=maxc:cur=(cur+' '+p).strip()
        else:
            if cur:out.append(cur)
            cur=p
            while len(cur)>maxc:
                k=cur.rfind(' ',0,maxc);out.append(cur[:k]);cur=cur[k+1:]
    if cur:out.append(cur)
    return out
def wrap2(t):
    if len(t)<=42:return t
    k=t.rfind(' ',0,len(t)//2+8)
    if k<=0:return t
    return t[:k]+'\n'+t[k+1:]
cues=[]
for c in CH:
    if c['nome'] not in TL:continue
    off,dd=TL[c['nome']];rr=chunk_ranges(c['s0'],c['s1']);m,D=build_map(rr)
    for i in range(c['s0'],c['s1']+1):
        txt=cor.get(i,S[i]['testo']).strip()
        if not txt or FILL.match(txt):continue
        a=off+to_edit(m,S[i]['inizio']);b=off+to_edit(m,S[i]['fine'])
        parts=split_text(txt);tot=sum(len(p) for p in parts);t=a
        for p in parts:
            d=(b-a)*len(p)/tot;cues.append((t,t+d,p));t+=d
for nome,a,b,txt in VC:
    if nome not in TL:continue
    off=TL[nome][0]
    parts=split_text(txt);tot=sum(len(p) for p in parts);t=off+a
    for p in parts:
        d=(b-a)*len(p)/tot;cues.append((t,t+d,p));t+=d
cues.sort()
tot=max(t+d for n,(t,d) in TL.items())
out=['WEBVTT','']
last=0
for a,b,p in cues:
    a=max(a,last);b=min(max(b,a+0.4),tot-0.05)
    if b<=a:continue
    out+=[f'{ts(a)} --> {ts(b)}',wrap2(p),''];last=b
open(sys.argv[1] if len(sys.argv)>1 else W+'/final/Storia_Lez16_Parte1.vtt','w').write('\n'.join(out))
print(len(cues),'cue')
