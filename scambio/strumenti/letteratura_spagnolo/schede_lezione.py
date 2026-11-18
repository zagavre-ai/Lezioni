# schede_lezione.py NN VIDEO TIMELINE.json TESTI_VOCI.json SCHEDA.json OUTDIR [solo=T1,R1,...]
# rende le schede blu di Spagnolo (titolo, pillola, quiz, riepilogo) per una lezione di Letteratura e scrive finestre.json
import sys,os,json,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from numeri_it import converti
from render_fast import render_many
from testo_scheda import testo as ocr_testo, ocr as ocr_grezzo, allinea
NN,V,TL,TV,SC,OUT=sys.argv[1:7]; SOLO=sys.argv[7].split(',') if len(sys.argv)>7 else None
os.makedirs(OUT,exist_ok=True)
tl=json.load(open(TL)); tv=json.load(open(TV)) if os.path.exists(TV) else {}; sc=json.load(open(SC))
if isinstance(tl,dict): tl=tl.get('pezzi') or tl.get('timeline') or [[k,v[0],v[1]] for k,v in tl.items()]
tl=[[str(x[0]),float(x[1]),float(x[2])] if isinstance(x,(list,tuple)) else [str(x.get('nome',x.get('id'))),float(x.get('inizio',x.get('start'))),float(x.get('durata',x.get('dur')))] for x in tl]
tl=[[re.sub(r'^RIP(\d+)$',r'R\1',k),a,d] for k,a,d in tl]
haR={int(m.group(1)) for k,_,_ in tl for m in [re.match(r'^R(\d+)$',k)] if m}
# lezioni senza pillola: la pillola blu va sui primi secondi dello schema S (la voce del ripasso c'è già)
tl2=[]
for k,a,d in tl:
    m=re.match(r'^S(\d+)$',k)
    if m and int(m.group(1)) not in haR and d>20:
        tl2.append([f'R{m.group(1)}',a,min(14.0,round(d*0.35,3))]); continue
    tl2.append([k,a,d])
tl=tl2
def testo(k):
    v=tv.get(k); 
    if v is None: return ''
    return ' '.join(v) if isinstance(v,list) else (v.get('testo','') if isinstance(v,dict) else str(v))
args=[a.get('titolo') or a.get('title') for a in sc['argomenti']]; NA=len(args)
lez=sc.get('titolo','').split('·')[-1].strip()
def righe(t):
    if len(t)<=16: return [t],150,600
    w=t.split(); best=None
    for i in range(1,len(w)):
        a,b=' '.join(w[:i]),' '.join(w[i:]); m=max(len(a),len(b))
        if best is None or m<best[0]: best=(m,[a,b])
    m=best[0]; fs=128 if m<=17 else (108 if m<=21 else 92)
    return best[1],fs,720
STOP=set('Sessanta Settanta Ottanta Novanta Ottocento Novecento Seicento Settecento Cinquecento Fiori Prima Seconda Poi Oggi Anche Così Infine Il Lo La I Gli Le Un Una Uno Nel Nella Con Per Dopo Tra Fra Ripasso Ecco Ma E In Al Alla Del Della Dal Dalla Da Si Su Sul Sulla Non È Questo Questa Primo Secondo Terzo Uno Due Tre Quattro'.split())
def chip(k):
    t=TESTI_R.get(k) or converti(testo(k)); out=[]
    for m in re.finditer(r"(?<![.!?]\s)(?<!^)\b([A-ZÀ-Ý][\wàèéìòù']+(?:\s[A-ZÀ-Ý][\wàèéìòù']+)?)",t):
        x=m.group(1)
        if x.split()[0] in STOP or x in out or len(x)<4: continue
        out.append(x)
        if len(out)==3: break
    return ' · '.join(out)
import unicodedata
def pulisci_voce(t):
    # i testi per la voce scrivono i nomi come si pronunciano (Bretón, Figarò): a schermo senza accenti di pronuncia
    def f(m):
        w=m.group(0)
        if len(w)>2 and w[0].isupper() and w not in ('È',):
            return ''.join(c for c in unicodedata.normalize('NFD',w) if unicodedata.category(c)!='Mn') if any(ch in w[1:] for ch in 'àèéìòóù') else w
        return w
    return re.sub(r"[A-Za-zÀ-ÿ]+",f,t)
def caps(text,dur,a0=0.9,b0=0.6):
    ss=[s.strip() for s in re.split(r'(?<=[.!?:])\s+',text) if s.strip()]
    tot=sum(len(s) for s in ss) or 1; t=a0; out=[]; span=max(1,dur-a0-b0)
    for s in ss:
        d=span*len(s)/tot; out.append([round(t,2),round(t+d,2),s]); t+=d
    return out
items=[];W=[];TESTI_R={}
for k,a,d in tl:
    if SOLO and k not in SOLO: continue
    m=re.match(r'^(T|R|Q)(\d+)$',k)
    if m:
        i=int(m.group(2)); tit=args[i-1] if i-1<len(args) else ''
        if m.group(1)=='T':
            l,fs,ly=righe(tit); sp={'type':'title','num':f'{i:02d}','total':NA,'lines':l,'ex':chip(f'R{i}') or tit,'fs':fs,'lineY':ly,'dur':d}; fps=30
        elif m.group(1)=='Q':
            sp={'type':'quiz','topic':tit,'tfs':(84 if len(tit)<=22 else max(54,int(84*22/len(tit)))),'act':f'Quiz {i}','pts':"5 domande · per continuare almeno l'80%",'dur':d}; fps=30
        else:
            vt=testo(k)
            if vt:
                og=' '.join(l.strip() for l in ocr_grezzo(V,a+d-0.6).split('\n') if l.strip())
                tx=allinea(converti(vt),og)
            else: tx=ocr_testo(V,a+d-0.6,'').strip()
            TESTI_R[k]=tx
            tx=re.sub(r'^[\W_]*(ripasso|riepilogo)\b[\s.:,;\-–—»«•*]*','',tx,flags=re.I).strip()
            tx=re.sub(r'^[«»•*\-–—\s]+','',tx)
            if k not in tv: tx=' '.join(re.split(r'(?<=[.!?])\s+',tx)[:2])
            sp={'type':'repaso','kicker':'Pillola di letteratura','big':'RIPASSO','topic':tit,'caps':caps(tx,d),'dur':d}; fps=15
    elif k in ('RF1','RF'):
        sp={'type':'final','kicker':'Letteratura italiana V','l1':'RIEPILOGO','l2':'FINALE','items':[[x,''] for x in args],
            'sub':'Ripassiamo insieme ciò che abbiamo imparato.','dur':d}; fps=15
    else: continue
    clip=f'{OUT}/{k}.mp4'
    if not os.path.exists(clip): items.append((sp,clip,fps))
    W.append({'a':round(a,3),'b':round(a+d,3),'clip':os.path.abspath(clip),'fin':0.3,'fout':0.3,'pezzo':k})
json.dump(W,open(f'{OUT}/finestre.json','w'),indent=1,ensure_ascii=False)
json.dump([[json.dumps(s,ensure_ascii=False),o,f] for s,o,f in items],open(f'{OUT}/specs.json','w'),ensure_ascii=False,indent=1)
print('pezzi',[w['pezzo'] for w in W]); render_many(items)
