import json,re,collections,datetime as dt
R=json.load(open('registri2.json'))
MESI={m:i for i,m in enumerate(['gennaio','febbraio','marzo','aprile','maggio','giugno','luglio','agosto','settembre','ottobre','novembre','dicembre'],1)}
H1T={1:'_stud',2:'_mat',3:'_doc',4:'dir',5:'1.0.tit',6:'1.0.arg',7:'1.1.tit',8:'1.1.arg',9:'1.2.tit',10:'1.2.arg',11:'2.0.mat',12:'2.0.pag',13:'2.1.mat',14:'2.1.pag',
     15:'3.0.arg',16:'3.0.lib',17:'3.0.sca',18:'3.1.arg',19:'3.1.lib',20:'3.1.sca',21:'4.0.tit',22:'4.0.con'}
ATT=['Studio','Ripasso','Approfondimento','Svolgere gli esercizi caricati'];TIP3=['Esercizi','Problemi','Questionario','Altro']
H1C={1:'1.0.ok',2:'1.1.ok',3:'1.2.ok',8:'2.0.ok',13:'2.1.ok'}
for i,o in enumerate(ATT): H1C[4+i]=('2.0.att',o); H1C[9+i]=('2.1.att',o)
for i,o in enumerate(TIP3): H1C[14+i]=('3.0.tip',o); H1C[18+i]=('3.1.tip',o)
for i,o in enumerate(['Quaderno','Libro/dispensa','Documento digitale','Piattaforma','In diretta','Altro']): H1C[22+i]=('3.ex.cons',o)
for i,o in enumerate(['Tema','Riassunto','Relazione','Ricerca','Traduzione','Progetto','Altro']): H1C[28+i]=('4.0.tip',o)
H1A={1:'3.ex.consA'}
H2T={1:'5.0.arg',2:'5.0.pag',3:'5.0.dat',4:'5.1.arg',5:'5.1.pag',6:'5.1.dat',7:'5.ex.dom',8:'6.0.att',9:'6.0.str',10:'6.0.mod',11:'6.0.sca',12:'7.0.arg',13:'7.0.dat',14:'7.0.not',
     15:'9.0.cor',16:'9.0.esi',17:'10.0.x',18:'10.1.x',19:'10.2.x'}
H2C={}
for i,o in enumerate(['Ripasso','Esposizione','Interrogazione']): H2C[1+i]=('5.0.tip',o); H2C[4+i]=('5.1.tip',o)
for i,o in enumerate(['Definizioni e concetti fondamentali','Regole, formule e procedimenti','Date, eventi e collegamenti','Esempi e applicazioni pratiche','Capacità di esposizione e argomentazione','Altro']): H2C[7+i]=('5.ex.asp',o)
for i,o in enumerate(['Orale','Scritta','Pratica','Test','Simulazione','Altro']): H2C[13+i]=('7.0.tip',o)
for i,o in enumerate(['Tutte da svolgere','Completate','Consegnate','Da recuperare']): H2C[19+i]=('8.ex.st',o)
H2A={1:'5.ex.aspA',2:'8.ex.rec'}
DATE_ALT={'dir':None,'3.0.sca':'3.0.lib','3.1.sca':'3.1.lib','5.0.dat':'5.0.pag','5.1.dat':'5.1.pag','6.0.sca':'6.0.mod','7.0.dat':'7.0.not'}
def iso_da(s,anno=2026):
    m=re.search(r'(\d{1,2})\s*[/.-]\s*(\d{1,2})(?:\s*[/.-]\s*(\d{2,4}))?',s)
    if m:
        y=int(m.group(3)) if m.group(3) else anno; y=y+2000 if y<100 else y
        try: return dt.date(y,int(m.group(2)),int(m.group(1))).isoformat()
        except: return None
    m=re.search(r'(\d{1,2})\s+(%s)'%'|'.join(MESI),s.lower())
    if m: return dt.date(anno,MESI[m.group(2)],int(m.group(1))).isoformat()
    return None
def giorno_iso(g):
    m=re.search(r'(\d+) (\w+) (\d{4})',g); return dt.date(int(m.group(3)),MESI[m.group(2).lower()],int(m.group(1))).isoformat()
VOCI=collections.OrderedDict(); PROBLEMI=[]; COPERTINE={}
for k,pages in R.items():
    cov={re.sub(r'^p\d+_','',w[0]):w[1] for p in pages if p['i']==0 for w in p['w']}
    stud=cov.get('testo1','').strip(); mat=re.split(r'MAZZOTTI|\n',cov.get('testo4',''))[0].strip(); doc=cov.get('testo5','').split('\n')[0].strip()
    if not stud: stud=re.sub(r'\.pdf$','',k.split('/')[1]); PROBLEMI.append((k,'copertina senza nome alunno'))
    COPERTINE[k]=dict(stud=stud,mat=mat,doc=doc,cla=cov.get('testo3',''),ind=cov.get('testo2',''))
    for p in pages:
        if not p['giorno'] or not p['w']: continue
        g=giorno_iso(p['giorno']); key=(stud.upper(),mat.upper(),g)
        d=VOCI.setdefault(key,{'stud':stud,'mat':mat,'doc':doc,'giorno':g,'file':set(),'dati':{}})
        d['file'].add(k.split('/')[1]); D=d['dati']
        T,Cx,A=(H1T,H1C,H1A) if p['meta']=='1' else (H2T,H2C,H2A)
        for nm,val,rect in p['w']:
            m=re.match(r'p\d+_(testo|casella|altro)(\d+)$',nm)
            if not m: PROBLEMI.append((k,'campo sconosciuto '+nm)); continue
            t,n=m.group(1),int(m.group(2))
            if t=='testo':
                f=T.get(n)
                if not f: PROBLEMI.append((k,'testo senza posto '+nm)); continue
                if f.startswith('_'): continue
                v=val.strip()
                if f in DATE_ALT:
                    iso=iso_da(v,int(g[:4]))
                    if iso: D[f]=iso
                    elif DATE_ALT[f]: D[DATE_ALT[f]]=(D.get(DATE_ALT[f],'')+' · '+v).strip(' ·')
                    continue
                D[f]=(D[f]+' · '+v) if D.get(f) and D[f]!=v else v
            elif t=='casella':
                f=Cx.get(n)
                if not f: PROBLEMI.append((k,'casella senza posto '+nm)); continue
                if isinstance(f,tuple):
                    l=D.setdefault(f[0],[])
                    if f[1] not in l: l.append(f[1])
                else: D[f]=True
            else:
                f=A.get(n)
                if f: D[f]=val.strip()
OUT=[]
for d in VOCI.values():
    if not d['dati']: continue
    d['file']=sorted(d['file']); OUT.append(d)
json.dump(OUT,open('registri_voci.json','w'),ensure_ascii=False)
print('giorni da inserire',len(OUT),'alunni',len({(x['stud'].upper()) for x in OUT}),'materie',collections.Counter(x['mat'].upper() for x in OUT).most_common())
print('problemi',len(PROBLEMI),PROBLEMI[:8])
print(json.dumps(OUT[0],ensure_ascii=False)[:600])
print(sorted({x['stud'] for x in OUT}))
