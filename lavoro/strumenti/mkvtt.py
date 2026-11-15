# VTT del docente nei tempi del video finale. uso: mkvtt.py raw.json timeline.json bounds.json dispensa.txt out.vtt
import sys,json,re,difflib
raw,tlf,bf,disp,out=sys.argv[1:6]
R=json.load(open(raw));TL=json.load(open(tlf));B=json.load(open(bf))
D={n:t for n,t,l in TL if re.fullmatch(r'D\d+',n)}
TERMS=sorted({w for w in re.findall(r"[A-Za-z][A-Za-z\-]{5,}",open(disp).read())},key=str.lower)
low={t.lower():t for t in TERMS}
def fix(txt):
    o=[]
    for w in txt.split():
        m=re.match(r"^(\W*)([A-Za-zà-ù\-']+)(\W*)$",w)
        if m and len(m.group(2))>=6:
            c=difflib.get_close_matches(m.group(2).lower(),list(low),1,0.84)
            if c and c[0]!=m.group(2).lower(): w=m.group(1)+low[c[0]]+m.group(3)
        o.append(w)
    return ' '.join(o)
def fin(x):
    for k in range(len(B)-1):
        if B[k]<=x<B[k+1] and f'D{k}' in D: return D[f'D{k}']+(x-B[k])
    return None
def split(txt,mx=42):
    ws=txt.split();L=[];cur=''
    for w in ws:
        if len(cur)+len(w)+1>mx and cur: L.append(cur);cur=w
        else: cur=(cur+' '+w).strip()
    if cur: L.append(cur)
    return L
cues=[]
for r in R:
    t=fix(r['t']);a=fin(r['s']);b=fin(min(r['e'],r['s']+60))
    if not t or a is None or len(t)<3: continue
    if b is None or b<=a: b=a+max(1.5,len(t)/15)
    lines=split(t);groups=[lines[i:i+2] for i in range(0,len(lines),2)]
    tot=sum(len(' '.join(g)) for g in groups);cur=a
    for g in groups:
        d=(b-a)*len(' '.join(g))/tot
        cues.append((cur,cur+d,'\n'.join(g)));cur+=d
def ts(x): return '%02d:%02d:%06.3f'%(x//3600,x%3600//60,x%60)
with open(out,'w') as f:
    f.write('WEBVTT\n\n')
    prev=0
    for i,(a,b,t) in enumerate(cues):
        a=max(a,prev);b=max(b,a+0.8);f.write(f'{i+1}\n{ts(a)} --> {ts(b)}\n{t}\n\n');prev=b
print(len(cues),'cue')
