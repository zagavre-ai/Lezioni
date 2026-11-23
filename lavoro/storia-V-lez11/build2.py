import sys,os,json
sys.path.insert(0,'/home/user/work/build')
from prof import *
from kit2 import *
r=R()
# ---------- pezzi a card con voce (senza docente)
def sent_cards(n):
    f=[cifre(x.rstrip('.')) if x.endswith('.') else cifre(x) for x in frasi(TXT[n])]
    return f
for k in range(1,19):
    f=sent_cards(f'AN{k}');t=((k-1)//3)+1
    PAGES[f'AN{k}']=dict(prof=False,kick=f'{t:02d} · Approfondimento',title=f[0],cards=f[1:],kws=[])
for t in range(1,7):
    n=len([x for x in TXT if re.fullmatch(f'SC{t}_\\d',x)])
    PAGES[f'SC{t}']=dict(prof=False,kick=f'{t:02d} · Pillola di ripasso',title=TOP[t-1]['t'],cards=[cifre(TXT[f'SC{t}_{i}']).rstrip('.') for i in range(1,n+1)],kws=[],n=n)
for g in ('GL1','GL2'):
    f=sent_cards(g);PAGES[g]=dict(prof=False,kick='Glossario',title=f[0],cards=f[1:],kws=[])
import json as _j
CP=_j.load(open(W+'/rev/revisione-storia-V-lez11/compiti.json'))['esercizi']
def cg(t): return t.replace('PCUS','PCUS (Partito Comunista dell\'Unione Sovietica)')
PAGES['CP3']=dict(prof=False,kick='Compiti',title='Ora tocca a te',cards=['Svolgi i compiti qui sotto e premi Consegna: arrivano al docente nel tuo quaderno dei compiti.'],kws=[])
PAGES['CP1']=dict(prof=False,kick='Compiti',title='Ora tocca a te',cards=[f"Esercizio {e['n']}: {cg(e['testo'])}" for e in CP[:2]],kws=[])
PAGES['CP2']=dict(prof=False,kick='Compiti',title='Ora tocca a te',cards=[f"Esercizio {e['n']}: {cg(e['testo'])}" for e in CP[2:]],kws=[])
GLS=[('NEP','NEP (Nuova politica economica)'),('Gulag','Gulag (campi di lavoro forzato)'),('Comintern','Comintern (Internazionale comunista)'),('Komsomol','Komsomol (organizzazione giovanile comunista)'),('kolchoz','kolchoz (cooperativa agricola)'),('sovchoz','sovchoz (azienda agricola pubblica)')]
def glossa(t):
    for k,v in GLS: t=re.sub(r'\b'+k+r'\b(?!\s*\()(?!:)(?!\s*,?\s*cio)',v,t)
    return t
import re
for k,Pg in list(PAGES.items()):
    if k.startswith(('AN','SC')): Pg['cards']=[glossa(c) for c in Pg['cards']];Pg['title']=glossa(Pg['title'])
# ---------- eventi dei pezzi a card: [(t_locale, attivo)]  (t relativo all'inizio della voce)
def ev_AN(k):
    tf=tempi_frasi(f'AN{k}',TXT[f'AN{k}'])
    return [(a,i) for i,(a,b,f) in enumerate(tf[1:],1)]   # card i attiva quando comincia la frase i
def ev_SC(t):
    n=PAGES[f'SC{t}']['n'];ev=[];x=0.7
    for i in range(1,n+1):
        d=dur(vpath(f'SC{t}_{i}'));ev.append((x,i,f'SC{t}_{i}',d));x+=d+0.4
    return ev,x+1.4
def windows_vc(key,events):
    hs,cy=get_meas(r,key);cur=None;out=[]
    for (t,act) in events:
        if act is None:
            w=[];n=len(hs)
            for i in range(1,n+1):
                if sum(hs[j-1] for j in w+[i])+16*len(w)<=960-cy and len(w)<3: w.append(i)
                else: break
        else: w=choose_window(hs,cy,act,cur)
        cur=w;out.append(w)
    return out
# ---------- finestre e numeri di pagina
def plan():
    wins=windows(r)                         # prof: (T,t)->finestra
    VC={}
    for k in range(1,19):
        key=f'AN{k}';ev=[(0,None)]+ev_AN(k);VC[key]=(ev,windows_vc(key,ev))
    for t in range(1,7):
        key=f'SC{t}';evs,end=ev_SC(t);ev=[(0,None)]+[(a,i) for a,i,nm,d in evs];VC[key]=(ev,windows_vc(key,ev))
    for g in ('GL1','GL2'):
        tf=tempi_frasi(g,TXT[g]);ev=[(0,None)]+[(a,i) for i,(a,b,f) in enumerate(tf[1:],1)];VC[g]=(ev,windows_vc(g,ev))
    for c in ('CP1','CP2','CP3'):
        ev=[(0,None)];VC[c]=(ev,windows_vc(c,ev))
    pn={};n=[1]
    def reg(key,w):
        if (key,tuple(w)) not in pn: n[0]+=1;pn[(key,tuple(w))]=n[0]
    reg('FOTO',[0])
    for t in range(1,7):
        ev=EV[f'T{t}'][2]
        for (tt,pg,act) in ev: reg(pg,wins[(f'T{t}',tt)])
        for k in range(3*t-2,3*t+1):
            for w in VC[f'AN{k}'][1]: reg(f'AN{k}',w)
        for w in VC[f'SC{t}'][1]: reg(f'SC{t}',w)
    for g in ('GL1','GL2','CP1','CP2','CP3'):
        for w in VC[g][1]: reg(g,w)
    return wins,VC,pn
def vc_seq(key,ev,wins,pn,t0,t_end):
    """sequenza stati per un pezzo a card: eventi con tempi locali (da t0) fino a t_end"""
    seq=[]
    for i,((t,act),w) in enumerate(zip(ev,wins)):
        s=t0+t;e=(t0+ev[i+1][0]) if i+1<len(ev) else t_end
        if e<=s: continue
        p=pn[(key,tuple(w))];P=PAGES[key]
        png=f'{B}/st/{key}_{"".join(map(str,w))}_{act}_{p}.png'
        if not os.path.exists(png):
            h,_=frame(P['kick'],P['title'],P['cards'],w,act,[],None,p,prof=False,wide=True,fs=46,dark=key.startswith('SC'));r.shot(h,png)
        seq.append([s,e,png])
    return seq
def enc_seq(seq,dur,out):
    fl=fade_list(seq,dur);cc=out+'.txt';write_concat(fl,cc)
    subprocess.run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',cc,'-vf','fps=30,format=yuv420p','-frames:v',str(nfr(dur)),'-c:v','libx264','-preset','veryfast','-crf','16',out],check=True)
