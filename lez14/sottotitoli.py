import sys,os,json,re
sys.path.insert(0,'/home/user/Lezioni/lez14')
from lib import *
PZ=W+'/pezzi'
VT={x['nome']:x['testo'] for x in json.load(open(W+'/old/testi_voci.json'))}
try:
    for x in json.load(open(W+'/voci_nuove.json')):VT[x['nome']]=x['testo']
except Exception:pass
COR=[(r'\b(Bretton Hoods|Berton Foods|Battle Woods|Bretton Foods)\b','Bretton Woods'),(r'McCartney','McCarthy'),(r'\b(Crushov|Khrushchev|Khrushver|Krusciov|Krusciòv)\b','Chruščëv'),
(r'Sigjević Kruša\.?',''),(r'\bNato\b','NATO'),(r'\bUngaria\b','Ungheria'),(r'Euroton','Euratom'),(r'\bWison\b','Winston'),(r'\bTogi\b','Tokyo'),(r'la Shah\b','la Shoah'),
(r'\bPetin\b','Pétain'),(r'delle Naz,','delle Nazioni Unite,'),(r'\b(Hen|Henry) Truman','Harry Truman'),(r'\bCurchin\b','Churchill'),(r'\bPankov\b','Pankow'),(r'\bUcraine\b','Ucraina'),
(r'della CE del 1957','della CEE del 1957'),(r'\bURS\b','URSS'),(r'\bi shake\b','Chiang Kai-shek'),(r'Stalinazione','stalinizzazione'),(r'Berlino-est','Berlino Est'),(r'Berlino-Ovest','Berlino Ovest'),(r'\bOvest\b','Ovest')]
def corr(t):
    for a,b in COR:t=re.sub(a,b,t)
    return re.sub(r'\s+',' ',t).strip()
U={'zero':0,'uno':1,'due':2,'tre':3,'quattro':4,'cinque':5,'sei':6,'sette':7,'otto':8,'nove':9,'dieci':10,'undici':11,'dodici':12,'tredici':13,'quattordici':14,'quindici':15,'sedici':16,'diciassette':17,'diciotto':18,'diciannove':19}
T={'venti':20,'trenta':30,'quaranta':40,'cinquanta':50,'sessanta':60,'settanta':70,'ottanta':80,'novanta':90}
def numero(w):
    s=w.lower();n=0
    if s.startswith('mille'):n+=1000;s=s[5:]
    elif s.startswith('duemila'):n+=2000;s=s[7:]
    m=re.match(r'^(\w*?)cento',s)
    if m and s!='cento':
        pre=m.group(1);c=U.get(pre,1 if pre=='' else None)
        if c is None:return None
        n+=c*100;s=s[m.end():]
    elif s.startswith('cento'):n+=100;s=s[5:]
    for t,v in sorted(T.items(),key=lambda a:-len(a[0])):
        stem=t[:-1]
        if s.startswith(t):n+=v;s=s[len(t):];break
        if s.startswith(stem) and len(s)>len(stem) and s[len(stem)] in 'aeiou':
            n+=v;s=s[len(stem):];break
    if s=='':return n if n else None
    if s in U:return n+U[s]
    if s in('tre','tré'):return n+3
    return None
def cifre(t):
    def r(m):
        w=m.group(0);v=numero(w)
        return str(v) if v is not None and v>=10 and (len(w)>6 or v>=1000) else w
    return re.sub(r'\b[a-zàèéìòù]{6,}\b',r,t)
def ts(t):
    h=int(t//3600);m=int(t%3600//60);s=t%60;return '%02d:%02d:%06.3f'%(h,m,s)
def cues_testo(t0,t1,testo):
    fr=[x.strip() for x in re.split(r'(?<=[.?!])\s+',testo) if x.strip()]
    if not fr:return []
    L=sum(len(x) for x in fr);out=[];t=t0
    for x in fr:
        d=(t1-t0)*len(x)/L
        # spezza in cue da max ~84 caratteri
        parts=[];cur=''
        for w in x.split():
            if len(cur)+len(w)+1>84:parts.append(cur);cur=w
            else:cur=(cur+' '+w).strip()
        if cur:parts.append(cur)
        dd=d/len(parts)
        for p in parts:out.append((t,t+dd,p));t+=dd
    return out
def vtt(timeline,out,durate):
    SEG=json.load(open(W+'/asr/orig.json'));cues=[]
    for (nome,start,_),d in zip(timeline,durate):
        sc=PZ+f'/{nome}.json'
        info=json.load(open(sc)) if os.path.exists(sc) else {}
        if nome.startswith('D') and 'K' in info:
            K=info['K'];acc=0;m=[]
            for a,b in K:m.append((a,b,acc));acc+=b-a
            def f(t):
                for a,b,o in m:
                    if a-0.01<=t<=b+0.01:return o+max(0,t-a)
                return None
            for s in SEG:
                a=f(s['inizio']);b=f(s['fine'])
                if a is None or b is None:continue
                tx=corr(s['testo']);
                if len(tx)<2 or re.fullmatch(r'(Um|Mm|Eh|Uh|Eh uh)[.,]?',tx):continue
                cues+=cues_testo(start+a,start+max(b,a+0.6),tx)
        else:
            voci=info.get('voci') or []
            VX=W+'/vox/scambio/storia-V-lez14/vox/'
            def vd(v):
                p=VX+v+'.wav'
                return dur(p) if os.path.exists(p) else None
            on=info.get('tempi_voci') or []
            t=0.3
            for i,v in enumerate(voci):
                dv=vd(v)
                if i<len(on):t=on[i]
                if dv is None:
                    dv=max(2.0,(d-0.9)/max(1,len(voci)))
                if VT.get(v):cues+=cues_testo(start+t,start+min(t+dv,d-0.3),cifre(VT[v]))
                t=t+dv+0.6
    with open(out,'w') as F:
        F.write('WEBVTT\n\n')
        for i,(a,b,t) in enumerate(cues):F.write(f'{ts(a)} --> {ts(max(b,a+0.4))}\n{t}\n\n')
    return len(cues)
if __name__=='__main__':
    print(cifre('nel millenovecentoquarantacinque e millenovecentocinquantatré, cinquanta milioni, quattrocentoventisette giorni'))
