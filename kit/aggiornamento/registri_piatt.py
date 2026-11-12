import json,re,datetime as dt,collections,unicodedata
from openpyxl import Workbook
from openpyxl.styles import Font,PatternFill,Alignment,Border,Side
from openpyxl.utils import get_column_letter
D=json.load(open('registri_piattaforma.json'));R,I=D['reg'],D['ids']
S=json.load(open('stud_iuc.json'))['STUD']
def nn(s): return unicodedata.normalize('NFD',s).encode('ascii','ignore').decode().upper()
STU=[(u,nn(v['nome']).split()) for u,v in S.items() if u not in ('50','312')]
MES={'Gen':1,'Feb':2,'Mar':3,'Apr':4,'Mag':5,'Giu':6,'Lug':7,'Ago':8,'Set':9,'Ott':10,'Nov':11,'Dic':12}
def data(s):
    m=re.match(r'(\d+) (\w+) (\d{4}) · (\d+):(\d+)',s or ''); return dt.datetime(int(m[3]),MES[m[2]],int(m[1]),int(m[4]),int(m[5])) if m else None
def chi(tit,parts):
    if parts:
        out=[]
        for p in parts:
            m=re.match(r'ID (\d+) - (.*)',p[0] or '')
            if m and m[1] in S: out.append(m[1])
        if out: return out
    m=re.search(r'\bcon (.+?)(?: - \d|$)',tit)
    if not m: return []
    seg=re.split(r',| e |\s-\s',m[1]); out=[]
    for s in seg:
        t=[x for x in re.split(r'[\s.]+',nn(s)) if x]
        if not t: continue
        cand=[u for u,toks in STU if t[0] in toks and (len(t)==1 or any(x.startswith(t[1]) for x in toks if x!=t[0]))]
        if len(cand)==1: out.append(cand[0])
    return out
def materia(tit):
    m=re.search(r'(?:Lezione \d+ - |lezione di )(.+?) con ',tit,re.I); return m[1].strip() if m else ''
def voto(t):
    v=re.findall(r'[Vv]ot[oi][^.]{0,60}?(\d+(?:[.,]\d+)?)\s*/\s*10',t or ''); return ', '.join(x+'/10' for x in v)
def compiti(t):
    fr=re.split(r'(?<=[.!?])\s+',t or ''); return ' '.join(f for f in fr if re.search(r'assegn|compit|per casa|esercizi da|da svolgere|studiare',f,re.I))
INI=dt.datetime(2026,10,1);FIN=dt.datetime(2026,11,12,23,59)
rows=[]
for k,x in R.items():
    d=data(x['data']); tit=I.get(k) or x['les']
    if not d or not (INI<=d<=FIN): continue
    al=chi(x['les'] or tit,x['p']); fb=' '.join(p[2] or '' for p in x['p'])
    rows.append(dict(id=k,d=d,doc=x['doc'],tit=x['les'] or tit,mat=materia(x['les'] or tit),al=al,arg=x['arg'],fb=fb,voto=voto(fb),comp=compiti(x['arg']+' '+fb),
        assente=bool(re.search(r'non si è presentat|assente|non era present|non ha partecipat',x['arg']+' '+fb,re.I))))
rows.sort(key=lambda r:r['d'])
A='Arial';NAVY='0B1530';th=Side(style='thin',color='C9D0DC');BR=Border(left=th,right=th,top=th,bottom=th)
H=Font(name=A,bold=True,color='FFFFFF',size=10);HF=PatternFill('solid',fgColor=NAVY);N=Font(name=A,size=10);T=Font(name=A,size=14,bold=True,color=NAVY);SB=Font(name=A,size=10,italic=True,color='5B6478')
def sheet(wb,nm,tit,sub,head,w):
    ws=wb.create_sheet(nm[:31]);ws['A1']=tit;ws['A1'].font=T;ws['A2']=sub;ws['A2'].font=SB
    for i,h in enumerate(head,1):
        c=ws.cell(4,i,h);c.font=H;c.fill=HF;c.border=BR;c.alignment=Alignment(wrap_text=True,vertical='center')
    for i,x in enumerate(w,1): ws.column_dimensions[get_column_letter(i)].width=x
    ws.freeze_panes='A5';ws.row_dimensions[4].height=30;return ws
def row(ws,r,v,fill=None):
    for i,x in enumerate(v,1):
        c=ws.cell(r,i,x);c.font=N;c.border=BR;c.alignment=Alignment(vertical='top',wrap_text=True)
        if isinstance(x,dt.datetime): c.number_format='DD/MM/YYYY HH:MM'
        if fill: c.fill=PatternFill('solid',fgColor=fill)
nome=lambda u:S[u]['nome'].title()
SUB='Registro elettronico della piattaforma (Lezioni → «Visualizza registro») · lezioni live dal 01/10 al 12/11/2026 · letto il 12/11/2026'
wb=Workbook();wb.remove(wb.active)
per=collections.defaultdict(list)
for r in rows:
    for u in r['al'] or ['?']: per[u].append(r)
q=sheet(wb,'Quadro','Registro della piattaforma · 1 ottobre – 12 novembre 2026',SUB,['Alunno','Indirizzo','Lezioni live con registro','Docenti','Materie','Assenze scritte nel registro','Voti','Lezioni con compiti assegnati'],[24,32,11,22,30,11,24,12])
r_=5
for u in sorted(per,key=lambda u:nome(u) if u!='?' else 'zzz'):
    L=per[u]
    row(q,r_,[nome(u) if u!='?' else '(alunno non riconosciuto)',S[u]['ind'] if u!='?' else '',len(L),', '.join(sorted({x['doc'] for x in L})),', '.join(sorted({x['mat'] for x in L if x['mat']})),sum(x['assente'] for x in L),', '.join(f"{x['d']:%d/%m} {x['voto']}" for x in L if x['voto']),sum(1 for x in L if x['comp'])]);r_+=1
# alunni attivi senza registro
senza=[u for u,_ in STU if u not in per]
r_+=1;q.cell(r_,1,'Alunni senza nessun registro compilato in piattaforma nel periodo:').font=Font(name=A,bold=True,size=10)
q.cell(r_,3,', '.join(sorted(nome(u) for u in senza))).font=N
e=sheet(wb,'Tutti i registri','Tutti i registri compilati · 1/10 – 12/11/2026',SUB,['Data e ora','Docente','Lezione','Materia','Alunno','Argomento trattato','Giudizio sull\'alunno','Voto','Compiti / indicazioni','Assenza scritta'],[14,16,30,14,18,60,60,8,40,9])
r_=5
for x in rows:
    row(e,r_,[x['d'],x['doc'],x['tit'],x['mat'],', '.join(nome(u) for u in x['al']) or '?',x['arg'],x['fb'],x['voto'],x['comp'],'Sì' if x['assente'] else ''],fill=('FBE0DE' if x['assente'] else None));r_+=1
for u in sorted([u for u in per if u!='?'],key=nome):
    ws=sheet(wb,nome(u),nome(u),S[u]['ind']+' · '+SUB,['Data e ora','Docente','Materia','Argomento trattato','Giudizio','Voto','Compiti / indicazioni'],[14,16,14,55,55,8,40])
    for i,x in enumerate(per[u],5): row(ws,i,[x['d'],x['doc'],x['mat'],x['arg'],x['fb'],x['voto'],x['comp']],fill=('FBE0DE' if x['assente'] else None))
out='finale/Registro_piattaforma_1ott-12nov.xlsx';wb.save(out)
print(out,len(rows),collections.Counter(x['doc'] for x in rows),'alunni',len([u for u in per if u!='?']),'non ric',len(per.get('?',[])),'senza',len(senza),'voti',sum(1 for x in rows if x['voto']),'assenze',sum(x['assente'] for x in rows),'comp',sum(1 for x in rows if x['comp']))
for x in per.get('?',[])[:8]: print('?',x['tit'])
