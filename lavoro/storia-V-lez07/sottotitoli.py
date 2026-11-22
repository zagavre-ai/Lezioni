import sys,os,json,re
sys.path.insert(0,'/home/claude/w/b')
import vox
from scenes import digits
from data import *
from assemble import order
W='/home/claude/w'
SEG=json.load(open(W+'/trasc.json'))
CORR=[(r'\bmillenovecento\w*',None),(r'\banenti\b','anni Venti'),(r'\banti e anche gli anni 30 del 900','anni Venti e anche gli anni Trenta del Novecento'),
(r'\banni 20\b','anni Venti'),(r'\banni 30\b','anni Trenta'),(r'\banni 50\b','anni Cinquanta'),(r'\banni 60\b','anni Sessanta'),(r'\banni 40\b','anni Quaranta'),(r'\banni dieci\b','anni Dieci'),
(r'\bdel 900\b','del Novecento'),(r'\bottocento\b','Ottocento'),(r'\bKu Klux Clan\b','Ku Klux Klan'),(r'\bCux Clan\b','Ku Klux Klan'),(r'\bFlectors\b','flappers'),
(r'\bHarbert Coover\b','Herbert Hoover'),(r'\bCoover\b','Hoover'),(r'\bCar Mars\b','Karl Marx'),(r'\bsottamericano\b','sogno americano'),(r'\bsog americano\b','sogno americano'),
(r'\bpaino de Wis\b','piano Dawes'),(r'\bcobelante\b','cobelligerante'),(r'\bTeodo Roosevelt\b','Theodore Roosevelt'),(r'\bAdolf It\b','Adolf Hitler'),
(r'\bsocietà delle nazioni\b','Società delle Nazioni'),(r'\bprima guerra mondiale\b','Prima guerra mondiale'),(r'\bseconda guerra mondiale\b','Seconda guerra mondiale'),
(r'\bgrande depressione\b','Grande Depressione'),(r'\bgiovedì nero\b','Giovedì nero'),(r'\bmercoledì nero\b','Mercoledì nero'),(r'\bal Capone\b','Al Capone'),
(r'\bfordista\b','fordista'),(r'\bFordista\b','fordista'),(r'\btailorista\b','taylorista'),(r'\bborsa\b','Borsa'),(r'\bfilippine\b','Filippine'),(r'\bChichei\b','Chicago'),
(r'\bhawaii\b','Hawaii'),(r'\bpiano de\b','piano'),(r'\bimpero Ottomano\b','impero ottomano'),(r'\b900\b','Novecento'),(r'\bpercento\b','per cento')]
def correggi(t):
    for p,r in CORR:
        if r is None:
            t=re.sub(p,lambda m: '1929' if re.search(r'(ventinove|linove|vinove|ove)$',m.group(0)) else digits(m.group(0)),t,flags=re.I)
        else: t=re.sub(p,r,t,flags=re.I if p[0] not in '(' else 0) if p.lower()==p else re.sub(p,r,t)
    return re.sub(r'\s+',' ',t).strip()
def fmt(t):
    h=int(t//3600);m=int(t%3600//60);s=t%60; return f'{h:02d}:{m:02d}:{s:06.3f}'
def chunks(text,t0,t1,maxc=84):
    w=text.split(); 
    if not w: return []
    # tempi per parola proporzionali ai caratteri
    tot=sum(len(x)+1 for x in w); cum=0; wt=[]
    for x in w: wt.append(t0+(t1-t0)*cum/tot); cum+=len(x)+1
    wt.append(t1)
    out=[];cur=[];st=0
    for i,x in enumerate(w):
        cur.append(x)
        s=' '.join(cur)
        brk=(len(s)>=maxc-8) or (x[-1] in '.?!' and len(s)>30) or (x[-1] in ',;:' and len(s)>60)
        if brk or i==len(w)-1:
            out.append((wt[st],wt[i+1],s)); cur=[];st=i+1
    return out
def lines(s):
    if len(s)<=42: return s
    w=s.split(); best=None
    for k in range(1,len(w)):
        a=' '.join(w[:k]);b=' '.join(w[k:])
        sc=abs(len(a)-len(b))
        if len(a)<=44 and len(b)<=44 and (best is None or sc<best[0]): best=(sc,a+'\n'+b)
    return best[1] if best else s
def build(tl,out):
    pos={n:t for n,t,l in tl}
    cues=[]
    for name,src,trans in order():
        if name not in pos: continue
        T0=pos[name]
        if name.startswith('Dprof') or name=='Dintro':
            pn=os.path.basename(src)[:-4]; J=json.load(open(src+'.json')); iv=J['iv']
            def tp(t):
                acc=0
                for x,y in iv:
                    if t<=x: return acc
                    if t<=y: return acc+(t-x)
                    acc+=y-x
                return acc
            for s in SEG:
                if s['inizio']>=iv[0][0]-0.05 and s['fine']<=iv[-1][1]+0.05:
                    tx=s['testo'].strip()
                    if tx.strip('.?!, ').lower() in ('um','yeah','you know','mm','mmm','so'): continue
                    for a,b,c in chunks(correggi(tx),T0+tp(s['inizio']),T0+tp(s['fine'])): cues.append([a,b,c])
        else:
            vn={'cover1':['BENV1_R2'],'dic':['DIC1'],'GL1':['GL1'],'FIN1':['FIN1'],'compiti_intro':['COMPI']}.get(name)
            if name.startswith('an'): a,i=name[2:].split('_'); vn=[AN[int(a)][int(i)][0]]
            if name.startswith('r') and name[1:].isdigit(): vn=[f'P{name[1:]}']
            if name.startswith('RF'): vn=[f'R{name[2:]}']
            if name.startswith('sch'): a=int(name[3:]); vn=[f'SC{a}_{k}_R2' if f'SC{a}_{k}_R2' in vox.T else f'SC{a}_{k}' for k in range(1,7) if f'SC{a}_{k}' in vox.T]
            if name.startswith('M') and name[1:].isdigit(): vn=None
            if name in ('compiti1','compiti2'): vn=['CP'+name[-1]]
            if name in ('M1','M2','M3'):
                import scenes; d=scenes.map_scene(int(name[1:])); 
                for bid,vname,t0,t1 in d['steps']: cues.append([T0+t0,T0+t1,correggi(digits(vox.T[vname]))]); 
                continue
            if not vn: continue
            # offset di partenza voce nel pezzo: 0.3-0.7 (le scene mettono la voce a +0.3..0.6)
            off={'cover1':0.6,'dic':0.3,'GL1':0.4,'FIN1':0.5,'compiti_intro':0.5,'compiti1':0.3,'compiti2':0.3}.get(name,0.4 if name.startswith(('an','RF')) else 0.4)
            if name.startswith('sch'):
                t=0.9
                for nm in vn:
                    v=vox.info(nm); t0=t+0.2; cues.append([T0+t0,T0+t0+v['dur'],correggi(digits(v['text']))]); t=t0+v['dur']+0.35
                continue
            for nm in vn:
                v=vox.info(nm)
                for a,b,s in v['sent']:
                    for x,y,c in chunks(correggi(digits(s)),T0+off+a,T0+off+b): cues.append([x,y,c])
    cues.sort()
    # niente sovrapposizioni, durata 1-6 s
    for i,c in enumerate(cues):
        nx=cues[i+1][0] if i+1<len(cues) else 1e9
        c[1]=min(c[1],nx-0.02,c[0]+6.0); 
        if c[1]-c[0]<0.8: c[1]=min(c[0]+0.8,nx-0.02)
    with open(out,'w') as f:
        f.write('WEBVTT\n\n')
        for a,b,c in cues:
            if b<=a: continue
            f.write(f'{fmt(a)} --> {fmt(b)}\n{lines(c)}\n\n')
    return len(cues)
if __name__=='__main__':
    tl=json.load(open(sys.argv[1])); print(build(tl,sys.argv[2]),'blocchi')
