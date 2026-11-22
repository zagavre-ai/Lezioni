# Sottotitoli .vtt dal parlato del prof (trascrizione) mappati sul video finale + voci Kore (testi), con termini corretti.
import sys, re, json
sys.path.insert(0,'/home/user/Lezioni/lavoro')
import piani, kore
from trasc_util import D
CORR=[(r'\b(Dwissen|Dewis|Dis del 1924|Dawis|piano di Wis|pian di Wis|piano Dis|Dawis Dis|Deus)\b','Dawes'),
 (r'\b(Brian Kellogg|Brian Kellog|Bianchello|Brian)\b','Briand-Kellogg'),(r'\bBriunini\b','Brüning'),(r'\bBröning\b','Brüning'),
 (r'\b(Mind Kampf|Minecraft|Mainkamp|Meinkampf|Mank|Mind|Mein Kampf)\b','Mein Kampf'),(r'\b(pucci|puccio|Pucci|puccio)\b','putsch'),
 (r'\b(Rome|Rom|Roma)\b(?=,? (guidate|dell|dei|era|comand|il |che|è|fondat|fedel|da far|e anche|sparire|\.))','Röhm'),
 (r'\bAnche Rom\b','Anche Röhm'),(r'\bRum\b','Röhm'),(r'\b(Heidrich|Heinri Himmler)\b','Heydrich'),(r'\bHeinri\b','Heinrich'),(r'\b(Goering|Goring|Göring)\b','Göring'),
 (r'\b(Goebel|Goebels|Goebbels)\b','Goebbels'),(r'\b(Fuhrer|Fjurel|Fuar|Fuhrer)\b','Führer'),(r'\bHitlerjug\b','Hitlerjugend'),
 (r'\b(Macau|Duacao|Dachao)\b','Dachau'),(r'Marinus Fander Lübe','Marinus van der Lubbe'),(r'\b(Lindeburg|Hindeburg)\b','Hindenburg'),
 (r'\b(Font Apen|Von Papen|Von Papel|Font apen)\b','von Papen'),(r'\bLeni Riefstall\b','Leni Riefenstahl'),(r'\bBerthol Brecht\b','Bertolt Brecht'),
 (r'\bSigmund Freu\b','Sigmund Freud'),(r'\bS A\b','SA'),(r'\bS S\b','SS'),(r'\bMartin Niemüller\b','Martin Niemöller'),(r'\bDietrich von Hofer\b','Dietrich Bonhoeffer'),
 (r'\bpuccio\b','putsch'),(r'\bAction T4\b','Aktion T4'),(r'\bLiemens Brow\b','Lebensraum'),(r'\bLebensrau\b','Lebensraum'),(r'\bGleichschaltu\b','Gleichschaltung'),
 (r'\bLuftwaffe\b','Luftwaffe'),(r'\bTerzo Reich\b','Terzo Reich'),(r'\bKonigsberg\b','Königsberg')]
def pulisci(t):
    t=re.sub(r'\s+',' ',t).strip()
    for rx,r in CORR: t=re.sub(rx,r,t)
    return t
def ts(s):
    h=int(s//3600);m=int(s%3600//60);x=s%60;return f'{h:02d}:{m:02d}:{x:06.3f}'
def spezza(testo,t0,t1,maxc=42,maxr=2):
    """blocchi di max 2 righe x 42 caratteri, tempi proporzionali ai caratteri"""
    parole=testo.split(' ');righe=[];cur=''
    for w in parole:
        if cur and len(cur)+1+len(w)>maxc: righe.append(cur);cur=w
        else: cur=(cur+' '+w).strip()
    if cur: righe.append(cur)
    blocchi=[righe[i:i+maxr] for i in range(0,len(righe),maxr)]
    tot=sum(len(' '.join(b)) for b in blocchi) or 1;t=t0;out=[]
    for b in blocchi:
        d=(t1-t0)*len(' '.join(b))/tot;out.append((t,t+d,'\n'.join(b)));t+=d
    return out
def build(parte,tlpath,out):
    TL={n:(s,d) for n,s,d in json.load(open(tlpath))}
    P={p['id']:p for p in piani.pezzi()}
    cues=[]
    idmap={'D0':'D0','D0B':'DI'}|{f'D{n}':f'A{n}' for n in range(1,9)}
    for nome,pid in idmap.items():
        if nome not in TL or pid not in P: continue
        t_out0=TL[nome][0];acc=0.0
        for s0,s1 in P[pid]['ranges']:
            for sg in D:
                a,b=sg['inizio'],sg['fine']
                if b<=s0 or a>=s1: continue
                a2=max(a,s0);b2=min(b,s1);txt=pulisci(sg['testo'])
                if len(txt)<2 or re.fullmatch(r'(Mm-hmm|Yeah|Uh|Um|Hm|Mm|Yeah\.?)\.?',txt): continue
                # parte del testo che cade in [a2,b2]: proporzionale
                f0=(a2-a)/max(1e-6,b-a);f1=(b2-a)/max(1e-6,b-a)
                w=txt.split(' ');i0=int(round(f0*len(w)));i1=int(round(f1*len(w)))
                sub=' '.join(w[i0:i1])
                if not sub: continue
                for x0,x1,tx in spezza(sub,t_out0+acc+(a2-s0),t_out0+acc+(b2-s0)):
                    cues.append((x0,x1,tx))
            acc+=s1-s0
    cues.sort()
    # niente sovrapposizioni
    for i in range(len(cues)-1):
        if cues[i][1]>cues[i+1][0]-0.02: cues[i]=(cues[i][0],cues[i+1][0]-0.02,cues[i][2])
    with open(out,'w') as f:
        f.write('WEBVTT\n\n')
        for k,(a,b,t) in enumerate(cues,1):
            if b-a<0.3: continue
            f.write(f'{k}\n{ts(a)} --> {ts(b)}\n{t}\n\n')
    return len(cues)
if __name__=='__main__':
    print(build(int(sys.argv[1]),sys.argv[2],sys.argv[3]))
