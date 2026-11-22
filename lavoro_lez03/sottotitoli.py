# Sottotitoli .vtt sul video finale: voce del prof (dalla trascrizione, nomi corretti con il materiale) e voci Kore (testo noto)
import sys,json,re;sys.path.insert(0,'/home/user/Lezioni/lavoro_lez03')
W=json.load(open('/tmp/w/b/words.json'))
SUB=[(r'\b(Osmond|Osman|Osmant|Osmans|Osmann)\b','Haussmann'),(r'\b(Berlizon|Bervison|Darwison|Barbison|Bad Bison)\b','Barbizon'),(r'\b(Goubet|Courbe)\b','Courbet'),
 (r'\b(Dumier|Dumi|Dunier|Domier)\b','Daumier'),(r'\bCorrot\b','Corot'),(r'\b[Cc]hisa\b','ghisa'),(r'\b[Mm]olla [Aa]ntonelliana\b','Mole Antonelliana'),
 (r'\ben plane air\b','en plein air'),(r'\bChac Garnier\b','Charles Garnier'),(r'\bMiller\b','Millet'),(r'\bBrighton Pavillon\b','Brighton Pavilion')]
def fix(t):
    for a,b in SUB:t=re.sub(a,b,t)
    return t
def ts(t):
    h=int(t//3600);m=int(t%3600//60);s=t%60;return '%02d:%02d:%06.3f'%(h,m,s)
def cues_prof(info):
    out=[]
    for n,d in info.items():
        t0=d['t'];subs=d['subs'];acc=[]
        c=0.0
        for x,y in subs:acc.append((x,y,c));c+=y-x
        def tr(t):
            for x,y,c0 in acc:
                if x-0.05<=t<=y+0.05:return t0+c0+max(0,t-x)
            return None
        ws=[w for w in W if subs[0][0]<=w[0]<=subs[-1][1]]
        cur=[];st=None
        def flush():
            nonlocal cur,st
            if cur:
                txt=fix(' '.join(x[2] for x in cur));e=tr(cur[-1][1])
                if st is not None and e is not None:out.append((st,max(e+0.25,st+0.8),txt))
            cur=[];st=None
        for w in ws:
            t=tr(w[0])
            if t is None:continue
            if st is None:st=t
            cur.append(w)
            L=len(' '.join(x[2] for x in cur))
            if L>78 or (tr(w[0])-st>5.5) or (w[3] and L>25):flush()
        flush()
    return sorted(out)
def lines(t):
    if len(t)<=42:return t
    w=t.split();a='';i=0
    while i<len(w) and len(a+' '+w[i])<=42:a=(a+' '+w[i]).strip();i+=1
    return a+'\n'+' '.join(w[i:])
def scrivi(info,path):
    c=cues_prof(info);prev_end=0
    with open(path,'w') as f:
        f.write('WEBVTT\n\n')
        for i,(s,e,t) in enumerate(c):
            if i+1<len(c):e=min(e,c[i+1][0]-0.02)
            f.write(f'{i+1}\n{ts(s)} --> {ts(e)}\n{lines(t)}\n\n')
    return len(c)
if __name__=='__main__':
    print(scrivi(json.load(open(sys.argv[1])),sys.argv[2]),'cue')
