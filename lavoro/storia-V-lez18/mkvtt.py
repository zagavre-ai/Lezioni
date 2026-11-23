# sottotitoli .vtt dal video finale: parlato del prof (trascrizione) + voci Kore (testi)
import sys,json,re
sys.path.insert(0,'/home/user/work18/lib')
from part import *
from cuts import SEG,level,WAV
import numpy as _np
w=sys.argv[1]
tl=json.load(open(f'{W}/out/timeline_Storia_Lez18_Parte{w}.json'));vl=json.load(open(f'{W}/out/vl_parte{w}.json'))
T={n:(t,d) for n,t,d in tl}
import importlib.util
spec=importlib.util.spec_from_file_location('b18',W+'/build18.py');
FIX=[("Cidio De","Alcide De"),("Fanfanni","Fanfani"),("Fanfan ","Fanfani "),("Crusoff","Chruščëv"),("Crush of","Chruščëv"),("Morodi","Moro di"),("Le cruciali lezioni","Le cruciali elezioni"),("Viene fondato la MSI","Viene fondato il MSI"),("Obrigatório",""),("Pietronelli","Pietro Nenni"),("Prebelli","Prebelliche"),("anquanta","anni Cinquanta"),("Comunastico","Comunque"),("d'accordo?",""),("  "," ")]
import difflib,glob
_texts=[]
for f in glob.glob(W+'/cards/arg*.json'):
    for fin in json.load(open(f))['finestre']:_texts+=[c['testo'] for c in fin['card']]
_texts+=list(TXT.values())+[x for v in json.load(open(W+'/scambio/storia-V-lez18/quiz.json')).values() for it in v['items'] for x in [it['p'],it['a'],it.get('e',''),*it['w']]]
_texts+=[x for it in json.load(open(W+'/verifica_finale.json')) for x in [it['p'],it['a'],*it['w']]]+[open(W+'/compiti.txt').read()]
_vocab=set();_names=set()
for t in _texts:
    toks=re.findall(r"[A-Za-zÀ-ÿ'’-]+",t)
    for i,tk in enumerate(toks):
        _vocab.add(tk.lower())
        if tk[0].isupper() and i>0 and len(tk)>=4:_names.add(tk)
_names-= {n for n in _names if n.lower() in {x for x in _vocab if x[0:1] and False}}
_namel={n.lower():n for n in _names}
NF=[("Gaspi","Gasperi"),("Pemirio","Palmiro"),("Cidele","Alcide"),("Isria","Istria"),("Naudi al Curinale","Einaudi al Quirinale"),("Molore Terzo","Vittorio Emanuele Terzo"),("catrizzare","cicatrizzare"),("anessanta","anni Cinquanta"),("faleva sulla DC","fa leva sulla DC"),("Giorgio Meloni","Giorgia Meloni"),("Aldomoro","Aldo Moro"),("bubo economico","boom economico"),("Fan Fanni","Fanfani"),("Cide De Gasperi","Alcide De Gasperi"),("Fanfanni","Fanfani")]
def fuzzy(t):
    for a,b in NF:t=t.replace(a,b)
    def f(m):
        w=m.group(0)
        if len(w)<5 or w.lower() in _vocab:return w
        c=difflib.get_close_matches(w.lower(),list(_namel),n=1,cutoff=0.84)
        return _namel[c[0]] if c else w
    return re.sub(r"[A-Za-zÀ-ÿ]+",f,t)
def clean(t):
    for a,b in FIX:t=t.replace(a,b)
    t=re.sub(r'\bMS\b','MSI',t);t=re.sub(r'\bPC\b','PCI',t);t=fuzzy(t)
    return re.sub(r'\s+',' ',t).strip()
def ts(t):
    h=int(t//3600);m=int(t%3600//60);s=t%60;return '%02d:%02d:%06.3f'%(h,m,s)
x16=_np.fromfile(W+'/a/prof_clean.f32',dtype=_np.float32).reshape(-1,2).mean(1)[::3].copy()
E=_np.convolve(x16**2,_np.ones(400)/400,'same');THR=_np.percentile(E,60)
cues=[]
# pezzi del prof
sys.argv=['x'];from build18 import fi
pieces=[(a,b,c) for a,b,c in json.load(open(f'{W}/out/pm_parte{w}.json'))]
CARD=[]
for n_ in range(1,7):
    d_=json.load(open(f'{W}/cards/arg{n_}.json'))
    for fin in d_['finestre']:
        cs_=fin['card']
        for j_,c in enumerate(cs_):
            nxt=cs_[j_+1]['t'] if j_+1<len(cs_) else fin['t1']
            CARD.append((c['t'],min(nxt,c['t']+len(c['testo'])*0.075+0.6),c['testo']))
CARD.append((2928.9,2940.0,"Il Piano INA-Casa, cioè il piano per far costruire case, serve a ripartire l'Italia e a costruire le case distrutte dalla guerra."))
CARD.append((2940.8,2958.0,"Il piano aiuta le famiglie a trovare casa e a uscire da situazioni di fortuna, come grotte, cantine, solai e abitazioni distrutte."))
for name,ps,pe in pieces:
    vt0=T[name][0];T0=fi(ps)/30
    for s in SEG:
        if s['inizio']>=T0-0.01 and s['fine']<=pe+0.3:
            mid=(s['inizio']+s['fine'])/2
            if any(a<=mid<b for a,b,_ in CARD):continue
            t=clean(s['testo'])
            if len(t)<2:continue
            st_=s['inizio']
            i0=int(max(0,st_-0.8)*16000);seg=E[i0:int((st_+0.8)*16000)]
            if len(seg) and seg[:int(0.5*16000)].mean()<THR*0.5:
                on=int(_np.argmax(seg>THR));st_=i0/16000+on/16000
            cues.append((vt0+st_-T0,vt0+max(s['fine'],st_+0.8)-T0,t))
    for a,b,tx in CARD:
        if a>=T0-0.01 and b<=pe+0.3:
            cues.append((vt0+a-T0,vt0+b-T0,xs(disp(tx)) if False else tx))
# voci Kore
for t0,name in vl:
    S=sents(name);st=sent_times(name);vd=vdur(name)
    for i,sx in enumerate(S):
        a=t0+st[i];b=t0+(st[i+1] if i+1<len(S) else vd)
        cues.append((a,b,disp(sx)))
def split(a,b,t,mx=84):
    if len(t)<=mx:return [(a,b,t)]
    w=t.split();ch=[];cur=''
    for x in w:
        if len(cur)+len(x)+1>mx and cur:ch.append(cur);cur=x
        else:cur=(cur+' '+x).strip()
    ch.append(cur);L=sum(len(c) for c in ch);out=[];tt=a
    for c in ch:
        d=(b-a)*len(c)/L;out.append((tt,tt+d,c));tt+=d
    return out
cues=[y for (a,b,t) in cues for y in split(a,b,t)]
cues.sort()
cues=[(a,min(b,cues[i+1][0]-0.01) if i+1<len(cues) and b>cues[i+1][0] else b,t) for i,(a,b,t) in enumerate(cues)]
mg=[]
for a,b,t in cues:
    if mg and a-mg[-1][0]<0.1:mg[-1]=(mg[-1][0],max(mg[-1][1],b),mg[-1][2]+' '+t)
    else:mg.append((a,b,t))
cues=mg
out=['WEBVTT','']
for ci,(a,b,t) in enumerate(cues):
    nx=cues[ci+1][0] if ci+1<len(cues) else 1e9
    words=t.split();lines=[];cur=''
    for x in words:
        if len(cur)+len(x)+1>44 and cur:lines.append(cur);cur=x
        else:cur=(cur+' '+x).strip()
    lines.append(cur)
    out+= [f'{ts(a)} --> {ts(min(max(b,a+0.6),nx-0.01) if nx-0.01>a+0.05 else a+0.05)}','\n'.join(lines),'']
open(f'{W}/out/Storia_Lez18_Parte{w}.vtt','w').write('\n'.join(out));print(len(cues),'cue')
