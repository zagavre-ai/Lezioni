# sottotitoli .vtt sul video finale: docente (trascrizione, con i termini corretti) + voci narranti (testo di riferimento)
import sys,os,json,re
sys.path.insert(0,'/tmp/claude-0/w/prod')
import build_lez as B
from eng import *
B.build();IT=B.ITEMS
S=json.load(open(W+'/fin/starts.json'))['start']
FIX=[(r'\bGiacomatte\b','Giacomo Matteotti'),(r'\bgiacomatte\b','Giacomo Matteotti'),(r'\bassassino del deputato','assassinio del deputato'),
 (r'\b[Dd]e [Kk]irch\w*','de Chirico'),(r'\b[Dd]e [Kk]irr\w*','de Chirico'),(r'\bDe Chirico\b','de Chirico'),(r'\b[Cc]arrat\b','Carrà'),(r'\bCarrà\b','Carrà'),
 (r'\bTerrani\b','Terragni'),(r'\bPeter Ragni\b','Giuseppe Terragni'),(r'\bpirranni\b','Terragni'),(r'\bcasa di fascia\b','Casa del Fascio'),(r'\b[Cc]asa del fascio\b','Casa del Fascio'),
 (r'\bcolosso quadrato\b','Colosseo quadrato'),(r'\bColosso quadrato\b','Colosseo quadrato'),(r'\b[Pp]alazzo della civiltà del lavoro\b','Palazzo della Civiltà del Lavoro'),
 (r'\bpiazza della Vittoria\b','piazza della Vittoria'),(r'\bpatti lateranensi\b','Patti Lateranensi'),(r'\bApollo del bel vedere\b','Apollo del Belvedere'),(r'\bl\'apollo del bel vedere\b',"l'Apollo del Belvedere"),(r'\bpollo del bel vedere\b','Apollo del Belvedere'),
 (r'\bPiacentini\b','Piacentini'),(r'\bBorgo Pi\b','Borgo Pio'),(r'\bmarcia su Roma\b','Marcia su Roma'),(r'\bMarzo su Roma\b','Marcia su Roma'),(r'\bMars Roma\b','Marcia su Roma'),
 (r'\bSarfatti\b','Sarfatti'),(r'\bMartini\b','Martini'),(r'\bsvuotamenti\b','sventramenti'),(r'\bdi svuotamenti\b','di sventramenti'),(r'\bgolgie\b','Corrente'),
 (r'\bCanto d\'amore\b',"Canto d'amore"),(r'\bmuse inquietanti\b','Muse inquietanti'),(r'\bEur\b','EUR'),(r'\bE 42\b','E42'),(r'\bGiorgio Chiri\b','Giorgio de Chirico'),
 (r'\bGuerrini, Ernesto Bruno, la Padula\b','Guerrini, Ernesto Bruno La Padula'),(r'\bTreccani\b','Treccani'),(r'\bDa Mir\b','MIAR')]
def fix(t):
    for a,b in FIX:t=re.sub(a,b,t)
    return t
def ts(t):
    h=int(t//3600);m=int(t%3600//60);s=t%60;return '%02d:%02d:%06.3f'%(h,m,s)
cues=[]
def split_cue(txt,t0,t1):
    # taglia in cue di al massimo ~84 caratteri alle virgole/spazi
    words=txt.split();parts=[];cur=[]
    for w in words:
        cur.append(w)
        if len(' '.join(cur))>=70 and (w.endswith((',',';','.','?','!')) or len(' '.join(cur))>=84):parts.append(' '.join(cur));cur=[]
    if cur:parts.append(' '.join(cur))
    tot=sum(len(p) for p in parts);t=t0;out=[]
    for p in parts:
        d=(t1-t0)*len(p)/tot;out.append((t,t+d,p));t+=d
    return out
def wrap(p):
    if len(p)<=42:return p
    k=p.rfind(' ',0,len(p)//2+8);k=k if k>10 else p.find(' ');return p[:k]+'\n'+p[k+1:]
for i,it in enumerate(IT):
    t0=S[i]/FPS
    if it.kind=='prof':
        iv,good=keep(it.src_a,it.src_b);fr=frames_ranges(iv);cum=0.0;mp=[]
        for (s,n) in fr:mp.append((s,s+n/FPS,cum));cum+=n/FPS
        def ot(t):
            for s,e,c in mp:
                if s-0.001<=t<=e+0.001:return t0+0.4+c+(t-s)
            return None
        for seg,_ in good:
            a=ot(seg['inizio']+0.01);b=ot(seg['fine']-0.01)
            if a is None:continue
            if b is None or b<=a:b=a+max(1.0,len(seg['testo'])/16)
            for (x,y,p) in split_cue(fix(seg['testo']),a,b):cues.append((x,y,p))
    elif it.audio:
        for (t,p,g) in it.audio:
            if '/vox' not in p:continue
            n=os.path.basename(p)[:-4]
            for (s,a,b) in sent_times(n):
                for (x,y,pp) in split_cue(digits(s),t0+t+a,t0+t+b-0.05):cues.append((x,y,pp))
cues.sort()
with open(W+'/fin/Storia_arte_Lez13_Parte1.vtt','w') as f:
    f.write('WEBVTT\n\n')
    for x,y,p in cues:f.write(f'{ts(x)} --> {ts(max(y,x+0.4))}\n{wrap(p)}\n\n')
print(len(cues),'cue')
