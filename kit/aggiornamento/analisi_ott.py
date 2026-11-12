import re,json,datetime as dt
src=open('crea_report.py').read().split('# ---------- stile ----------')[0]
ns={}; exec(src,ns)
S,REP,leggi,materia,norm=ns['S'],ns['REP'],ns['leggi_report'],ns['materia'],ns['norm']
from openpyxl import Workbook
from openpyxl.styles import Font,PatternFill,Alignment,Border,Side
from openpyxl.utils import get_column_letter
INI=dt.datetime(2026,10,1); FIN=dt.datetime(2026,11,12,23,59)
nel=lambda x: bool(x and INI<=x<=FIN)
ESCL={'50','312'}
uid_of={}
for uid,iucs in S['IUC'].items():
    for cid,iuc in iucs: uid_of[str(iuc)]=uid
dati={}  # uid -> materia -> dict
corsi_live={}
for iuc,rows in REP.items():
    uid=uid_of.get(iuc)
    if not uid or uid in ESCL: continue
    R=leggi(rows); c=R['corso'].strip()
    live=bool(re.search(r'DIRETTA|LIVE',c,re.I))
    mat=materia(c)
    d=dati.setdefault(uid,{}).setdefault((mat,'Lezioni in diretta' if live else 'Videolezioni'),dict(corsi=set(),viste=0,iniziate=0,complete=0,test=0,ses=0,lez=[]))
    d['corsi'].add(c)
    for l in R['lez']:
        att = nel(l['pv']) or nel(l['ul']) or nel(l['comp'])
        if not att: continue
        d['viste']+=1
        if nel(l['comp']): d['complete']+=1
        else: d['iniziate']+=1
        if l['test']=='SI' and nel(l['comp']): d['test']+=1
        d['lez'].append((l['pv'] if nel(l['pv']) else (l['ul'] or l['comp']),c,l['tit'],'Completata' if nel(l['comp']) else 'Iniziata, non completata',l['pun'] if l['test']=='SI' else '',l['comp'] if nel(l['comp']) else None))
A='Arial';NAVY='0B1530';thin=Side(style='thin',color='C9D0DC');BR=Border(left=thin,right=thin,top=thin,bottom=thin)
H=Font(name=A,bold=True,color='FFFFFF',size=10);HF=PatternFill('solid',fgColor=NAVY);N=Font(name=A,size=10);B=Font(name=A,size=10,bold=True);T=Font(name=A,size=14,bold=True,color=NAVY);SB=Font(name=A,size=10,italic=True,color='5B6478')
def sheet(wb,name,tit,sub,head,w):
    ws=wb.create_sheet(name[:31]);ws['A1']=tit;ws['A1'].font=T;ws['A2']=sub;ws['A2'].font=SB
    for i,h in enumerate(head,1):
        c=ws.cell(4,i,h);c.font=H;c.fill=HF;c.border=BR;c.alignment=Alignment(wrap_text=True,vertical='center')
    for i,x in enumerate(w,1): ws.column_dimensions[get_column_letter(i)].width=x
    ws.freeze_panes='A5';ws.row_dimensions[4].height=32;return ws
def row(ws,r,v,fill=None,bold=False):
    for i,x in enumerate(v,1):
        c=ws.cell(r,i,x);c.font=B if bold else N;c.border=BR;c.alignment=Alignment(vertical='top',wrap_text=True)
        if isinstance(x,dt.datetime): c.number_format='DD/MM/YYYY'
        if fill: c.fill=PatternFill('solid',fgColor=fill)
wb=Workbook();wb.remove(wb.active)
SUB='Periodo 01/10/2026 – 12/11/2026 · dati della piattaforma letti il 12/11/2026 mattina · conta le lezioni con attività nel periodo'
q=sheet(wb,'Quadro','Materie seguite e videolezioni · 1 ottobre – 12 novembre 2026',SUB,
 ['Alunno','Indirizzo','Materie con videolezioni seguite','Videolezioni con attività','di cui completate','di cui iniziate e non finite','Lezioni in diretta con attività','Materie iscritte senza nessuna videolezione nel periodo'],[26,34,40,13,12,13,13,44])
r=5;mat_ws=[]
nomi=sorted([(S['STUD'][u]['nome'],u) for u in dati])
for nome,uid in nomi:
    D=dati[uid]
    vid={m:d for (m,t),d in D.items() if t=='Videolezioni'}; liv={m:d for (m,t),d in D.items() if t!='Videolezioni'}
    seg=sorted(m for m,d in vid.items() if d['viste']); nos=sorted(m for m,d in vid.items() if not d['viste'])
    tv=sum(d['viste'] for d in vid.values()); tc=sum(d['complete'] for d in vid.values()); ti=sum(d['iniziate'] for d in vid.values()); tl=sum(d['viste'] for d in liv.values())
    row(q,r,[nome.title(),S['STUD'][uid]['ind'],', '.join(seg) or '—',tv,tc,ti,tl,', '.join(nos) or '—'],fill=('FBE0DE' if tv==0 else None));r+=1
    mat_ws.append((nome,uid,D))
# matrice materie
mats=sorted({m for _,_,D in mat_ws for (m,t) in D if t=='Videolezioni'})
mx=sheet(wb,'Alunni x materie','Videolezioni con attività per materia · 1/10 – 12/11/2026','Numero = videolezioni con attività nel periodo (completate + iniziate) · vuoto = non iscritto · 0 = iscritto ma nessuna attività',['Alunno']+mats,[24]+[9]*len(mats))
r=5
for nome,uid,D in mat_ws:
    v=[nome.title()]
    for m in mats:
        d=D.get((m,'Videolezioni')); v.append(d['viste'] if d else None)
    row(mx,r,v)
    for i,m in enumerate(mats,2):
        d=D.get((m,'Videolezioni'))
        if d and d['viste']==0: mx.cell(r,i).fill=PatternFill('solid',fgColor='FBE0DE')
        elif d: mx.cell(r,i).fill=PatternFill('solid',fgColor='D9F2E3')
    r+=1
mx.row_dimensions[4].height=90
for i in range(2,len(mats)+2): mx.cell(4,i).alignment=Alignment(text_rotation=90,vertical='bottom',horizontal='center')
# fogli alunno
for nome,uid,D in mat_ws:
    ws=sheet(wb,nome.title()[:31],nome.title(),f"{S['STUD'][uid]['ind']} · "+SUB,['Data','Materia','Tipo','Corso','Lezione','Stato','Punteggio test','Completata il'],[11,16,13,34,40,18,10,12])
    r=5;L=[]
    for (m,t),d in D.items():
        for x in d['lez']: L.append((x[0],m,t)+x[1:])
    for x in sorted(L,key=lambda y:(y[0] or dt.datetime(2000,1,1))):
        row(ws,r,list(x),fill=('D9F2E3' if x[5]=='Completata' else 'FFF4C2'));r+=1
    if not L: row(ws,5,['—','Nessuna attività nel periodo','','','','','',''])
    r+=1; ws.cell(r,1,'Materie iscritte (videolezioni) senza attività nel periodo:').font=B
    ws.cell(r,4,', '.join(sorted(m for (m,t),d in D.items() if t=='Videolezioni' and not d['viste'])) or '—').font=N
out='finale/Analisi_materie_videolezioni_1ott-12nov.xlsx';wb.save(out)
tv=sum(d['viste'] for _,_,D in mat_ws for (m,t),d in D.items() if t=='Videolezioni')
tc=sum(d['complete'] for _,_,D in mat_ws for (m,t),d in D.items() if t=='Videolezioni')
zero=[n for n,u,D in mat_ws if not sum(d['viste'] for (m,t),d in D.items() if t=='Videolezioni')]
print(out,len(mat_ws),tv,tc,zero)
