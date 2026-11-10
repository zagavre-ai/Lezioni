import sys,os,re,datetime as dt
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from dati_ESEMPIO_struttura import *  # sostituire con il file dati dell'alunno (tenuto FUORI dal repository)
from openpyxl import Workbook
from openpyxl.styles import Font,PatternFill,Alignment,Border,Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule,FormulaRule
FINE=dt.datetime(2026,11,8,23,59,59)   # fine settimana controllata
OGGI='10/11/2026 14:20'
QUOTA=3
MESI={'Ottobre':10,'Novembre':11}
def d(s):
    m=re.search(r'(\d{2}) (\w+), ore (\d{2}):(\d{2})',s or '')
    return dt.datetime(2026,MESI[m.group(2)],int(m.group(1)),int(m.group(3)),int(m.group(4))) if m else None
def f(x):return x.strftime('%d/%m/%Y %H:%M') if x else ''
A='Arial';NAVY='0B1530';BLU='2060AF'
H=Font(name=A,bold=True,color='FFFFFF',size=10);HF=PatternFill('solid',fgColor=NAVY)
N=Font(name=A,size=10);B=Font(name=A,size=10,bold=True);T=Font(name=A,size=14,bold=True,color=NAVY);S=Font(name=A,size=10,italic=True,color='5B6478')
thin=Side(style='thin',color='C9D0DC');BR=Border(left=thin,right=thin,top=thin,bottom=thin)
STF={'Svolta':'D9F2E3','A metà':'FFF4C2','Non svolta':'FBE0DE','Svolta in anticipo':'D9E8FB'}
wb=Workbook()
def foglio(nome,titolo,sotto,head,widths):
    ws=wb.create_sheet(nome);ws['A1']=titolo;ws['A1'].font=T;ws['A2']=sotto;ws['A2'].font=S
    for i,h in enumerate(head,1):
        c=ws.cell(4,i,h);c.font=H;c.fill=HF;c.alignment=Alignment(wrap_text=True,vertical='center');c.border=BR
    for i,w in enumerate(widths,1):ws.column_dimensions[get_column_letter(i)].width=w
    ws.row_dimensions[4].height=32;ws.freeze_panes='A5';return ws
def riga(ws,r,vals,wrap=()):
    for i,v in enumerate(vals,1):
        c=ws.cell(r,i,v);c.font=N;c.border=BR;c.alignment=Alignment(vertical='top',wrap_text=(i in wrap))
wb.remove(wb.active)
INTEST=f"Alunna: {ALUNNA['nome']} (ID {ALUNNA['id']}) · {ALUNNA['indirizzo']} · iscritta ai corsi dal {ALUNNA['iscrizione']}"
# ---------- piano della settimana controllata (ricostruito: prime QUOTA lezioni non svolte al 1/11) ----------
LEZ=[]
for c in CORSI:
    tutte=[]
    for a in c['att']:
        lid,tit,fr,test,tent,pun,pv,ul,comp,ses,sec,dl,vp,q=a
        tutte.append(dict(lid=lid,tit=tit,fr=fr,test=test,tent=tent,pun=pun,pv=d(pv),ul=d(ul),comp=d(comp),ses=ses,min=round(sec/60),dl=dl,vp=vp,q=q))
    for lid,tit in c['altre']:tutte.append(dict(lid=lid,tit=tit,fr=0,test='SI',tent=0,pun='-',pv=None,ul=None,comp=None,ses=0,min=0,dl=0,vp=0,q=[]))
    for i,l in enumerate(tutte):
        l['materia']=c['materia'];l['corso']=c['corso'];l['ord']=i+1;l['piano1']=i<QUOTA
        if l['comp'] and l['comp']<=FINE:l['st']='Svolta' if l['piano1'] else 'Svolta in anticipo'
        elif l['pv'] and l['pv']<=FINE:l['st']='A metà'
        else:l['st']='Non svolta'
        l['oggi']='Svolta' if l['comp'] else ('A metà' if l['pv'] else 'Non svolta')
    c['lez']=tutte;LEZ+=tutte
# ---------- 1. Riepilogo ----------
ws=foglio('Riepilogo','Controllo settimanale · settimana 2–8 novembre 2026',INTEST+' · dati della piattaforma letti il '+OGGI,
 ['Materia','Corso (nome sulla piattaforma)','Lezioni del corso','Lezioni nel piano 2–8/11','Svolte','A metà','Non svolte','Svolte in anticipo','Test superati (punteggio medio)','Compiti caricati nella cartella','Live di verifica da chiedere al docente','Lezioni da recuperare nel piano 9–15/11'],
 [20,46,10,12,9,9,10,11,16,22,40,14])
r=5
for c in CORSI:
    m=c['materia'];fatte=[l for l in c['lez'] if l['st'] in('Svolta','Svolta in anticipo')]
    pun=[int(l['pun'].rstrip('%')) for l in fatte if l['pun'].endswith('%')]
    cart=c.get('cartella');comp=('nessuna cartella' if not cart else ('7 fogli (3, 4 e 7/11): 3 completi, 4 con parti non svolte o dubbi; non corretti dal docente' if cart=='MATEMATICA' else 'cartella vuota'))
    haE=bool(cart and CARTELLE.get(cart))
    live=('Sì: '+'; '.join(l['tit'].title() for l in fatte)) if (fatte and haE) else ('Non ancora: test superati, ma esercizi non caricati' if fatte else '—')
    rg=f"Dettaglio!$A$5:$A$400"
    riga(ws,r,[m,c['corso'],TOT_LEZ[c['id']],
      f'=COUNTIFS(Dettaglio!$A$5:$A$400,A{r},Dettaglio!$F$5:$F$400,"Sì")',
      f'=COUNTIFS(Dettaglio!$A$5:$A$400,A{r},Dettaglio!$G$5:$G$400,"Svolta")',
      f'=COUNTIFS(Dettaglio!$A$5:$A$400,A{r},Dettaglio!$G$5:$G$400,"A metà",Dettaglio!$F$5:$F$400,"Sì")',
      f'=COUNTIFS(Dettaglio!$A$5:$A$400,A{r},Dettaglio!$G$5:$G$400,"Non svolta",Dettaglio!$F$5:$F$400,"Sì")',
      f'=COUNTIFS(Dettaglio!$A$5:$A$400,A{r},Dettaglio!$G$5:$G$400,"Svolta in anticipo")',
      f"{len(pun)} ({round(sum(pun)/len(pun))}%)" if pun else '—',comp,live,
      f'=F{r}+G{r}'],wrap=(2,10,11))
    r+=1
riga(ws,r,['TOTALE','',f'=SUM(C5:C{r-1})',f'=SUM(D5:D{r-1})',f'=SUM(E5:E{r-1})',f'=SUM(F5:F{r-1})',f'=SUM(G5:G{r-1})',f'=SUM(H5:H{r-1})','','','',f'=SUM(L5:L{r-1})'])
for i in range(1,13):ws.cell(r,i).font=B
r+=2
NOTE=['Come si legge',
 '• Svolta = lezione completata dalla piattaforma entro domenica 8/11 alle 23:59 (c\'è la «Data completamento»).',
 '• A metà = lezione aperta entro l\'8/11 ma non completata (test non fatto o non superato).',
 '• Non svolta = nessuna visualizzazione entro l\'8/11.',
 f'• Piano 2–8/11: non era registrato sulla piattaforma; per la prova è ricostruito con le prime {QUOTA} lezioni di ogni materia (da sostituire con il piano vero).',
 '• Live di verifica: si chiede al docente quando, per gli argomenti della settimana, l\'alunna ha svolto il test E caricato gli esercizi. Se gli esercizi mancano, la live non si chiede ancora.',
 '• Compiti: fogli caricati dall\'alunna nell\'Archivio file, letti uno per uno (foglio «Compiti caricati»); nessuna correzione dei docenti presente.']
for t in NOTE:ws.cell(r,1,t).font=B if t==NOTE[0] else N;r+=1
# ---------- 2. Piano 9–15 ----------
ws=foglio('Piano 9-15 novembre','Piano didattico · settimana 9–15 novembre 2026',INTEST+f' · prima le lezioni da recuperare, poi le nuove (massimo {QUOTA} per materia)',
 ['Materia','N.','Tipo','ID lezione','Titolo della lezione (nome sulla piattaforma)','Attività e test associati','Stato al 8/11','Aggiornamento al 10/11'],[20,5,13,10,60,46,12,22])
r=5
for c in CORSI:
    rec=[l for l in c['lez'] if l['piano1'] and l['st']!='Svolta']
    nuove=[l for l in c['lez'] if not l['piano1'] and l['st']=='Non svolta'][:max(0,QUOTA-len(rec))]
    if not rec and not nuove:continue
    for k,l in enumerate(rec+nuove,1):
        tipo='Da recuperare' if l in rec else 'Nuova'
        att='Videolezione + test della lezione (soglia della piattaforma)'+('; carichi gli esercizi nella cartella '+c['cartella'] if c.get('cartella') else '')
        agg=('completata il '+f(l['comp'])[:5]) if l['comp'] else (('iniziata il '+f(l['pv'])[:5]) if l['pv'] else '')
        riga(ws,r,[c['materia'],k,tipo,l['lid'],l['tit'],att,l['st'] if tipo=='Da recuperare' else '—',agg],wrap=(5,6))
        ws.cell(r,3).fill=PatternFill('solid',fgColor='FFF4C2' if tipo=='Da recuperare' else 'FFFFFF');r+=1
    fatte=[l for l in c['lez'] if l['st'] in('Svolta','Svolta in anticipo')]
    if fatte and c.get('cartella') and CARTELLE.get(c['cartella']):
        riga(ws,r,[c['materia'],'',"Live di verifica",'',"Lezione live con il docente su: "+'; '.join(l['tit'].title() for l in fatte),"Da chiedere al docente: verificare che gli argomenti svolti siano chiari"+(" (portare i 5 punti con dubbi degli esercizi)" if c['materia']=='Matematica' else ''),'—',''],wrap=(5,6))
        ws.cell(r,3).fill=PatternFill('solid',fgColor='D9E8FB');r+=1
    if c['materia']=='Matematica':
        riga(ws,r,['Matematica','',"Compiti",'',"Completare gli esercizi rimasti aperti delle lezioni 254 (n. 1, 2, 3, 8) e 256 (n. 2) e caricarli nella cartella MATEMATICA","Docente: correggere e valutare gli esercizi delle lezioni 253, 254 e 256 (7 fogli caricati il 4 e il 7/11); controllare il testo degli esercizi in cui l'alunna segnala una parentesi mancante",'—',''],wrap=(5,6))
        ws.cell(r,3).fill=PatternFill('solid',fgColor='FBE0DE');r+=1
r+=1;ws.cell(r,1,'Legenda tipo: giallo = lezione da recuperare dalla settimana precedente; bianco = lezione nuova; azzurro = live di verifica da chiedere al docente; rosso = compiti da completare e da correggere.').font=S;r+=1
ws.cell(r,1,'Nota: «Aggiornamento al 10/11» mostra le lezioni già svolte dopo la fine della settimana (lunedì e martedì): restano nel piano perché non erano state fatte nei tempi.').font=S
# ---------- 3. Dettaglio ----------
ws=foglio('Dettaglio','Dettaglio lezione per lezione',INTEST+' · dal «Report attività utente» di ogni corso',
 ['Materia','N.','ID lezione','Titolo della lezione','Corso','Nel piano 2–8/11','Stato al 8/11','Stato al 10/11','Prima visualizzazione','Data completamento','Test','Tentativi','Punteggio','Visualizzazioni registrate','Minuti di visione (dai log)','Download materiale','Verifiche presenza','Esiti dei questionari'],
 [18,5,9,52,30,10,12,12,16,16,6,8,9,12,11,10,10,44])
r=5
for l in LEZ:
    riga(ws,r,[l['materia'],l['ord'],l['lid'],l['tit'],l['corso'],'Sì' if l['piano1'] else 'No',l['st'],l['oggi'],f(l['pv']),f(l['comp']),l['test'],l['tent'],l['pun'],l['ses'],l['min'],l['dl'],l['vp'],'; '.join(l['q'])],wrap=(4,18))
    for col in(7,8):ws.cell(r,col).fill=PatternFill('solid',fgColor=STF[ws.cell(r,col).value])
    r+=1
dv=DataValidation(type='list',formula1='"Svolta,A metà,Non svolta,Svolta in anticipo"',allow_blank=True);ws.add_data_validation(dv);dv.add(f'G5:G{r-1}')
ws.auto_filter.ref=f'A4:R{r-1}'
ws.cell(r+1,1,'Nota: per Diritto ed economia e per i corsi non ancora iniziati sono elencate solo le prime lezioni del corso (quelle che servono per il piano); Storia, Matematica e Italiano sono complete.').font=S
# ---------- 4. Compiti caricati ----------
ws=foglio('Compiti caricati','Compiti nella cartella dell\'alunna (Archivio file → COGNOME NOME ID)',INTEST+' · letti uno per uno il 10/11',
 ['Cartella','File','Caricato il','Data scritta sul foglio','Lezione collegata','Contenuto','Svolgimento','Dubbi segnati dall\'alunna','Corretto dal docente','Voto / giudizio'],[13,30,11,11,34,30,26,40,14,14])
CMP=[('MATEMATICA','MATEMATICA_ESERCIZIO_1.jpeg','04/11/2026','03/11/2026','253 · I NUMERI NATURALI E LE OPERAZIONI FONDAMENTALI','Esercizio 1: tre espressioni con i numeri naturali','completo, 3 risultati riquadrati (10, 31, 12)','—'),
 ('MATEMATICA','MATEMATICA_ESERCIZIO_2.jpeg','04/11/2026','—','254 · ESPRESSIONI, PROPRIETÀ DELLE OPERAZIONI E DELLE POTENZE','Esercizio 2 (seguito): espressione n. 3 e proprietà delle potenze n. 4–7','parziale','n. 3: risultato «22 − 202 = ?» non concluso'),
 ('MATEMATICA','MATEMATICA_ESERCIZIO_2_ - Copia.jpeg','04/11/2026','—','254 · ESPRESSIONI, PROPRIETÀ DELLE OPERAZIONI E DELLE POTENZE','Esercizio 2: espressione n. 8','non svolto','n. 8: «manca parentesi?» (dubbio sul testo)'),
 ('MATEMATICA','MATEMATICA_ESERCIZIO_2_.jpeg','04/11/2026','—','254 · ESPRESSIONI, PROPRIETÀ DELLE OPERAZIONI E DELLE POTENZE','Esercizio 2: espressioni n. 1–2','parziale','n. 1: risultato 2,125 con «?»; n. 2: interrotto con «?»'),
 ('MATEMATICA','ESERCIZI_LEZIONE_4.jpeg','07/11/2026','—','256 · I NUMERI RELATIVI','Esercizi n. 4, 5, 6 con i numeri relativi','completo, 3 risultati riquadrati (+7, −13, −1)','—'),
 ('MATEMATICA','ESERCIZI_LEZIONE_4_ - Copia.jpeg','07/11/2026','—','256 · I NUMERI RELATIVI','Esercizio n. 7','completo, risultato riquadrato (+2)','—'),
 ('MATEMATICA','ESERCIZI_LEZIONE_4_.jpeg','07/11/2026','07/11/2026','256 · I NUMERI RELATIVI','«Esercizio 4»: espressioni n. 2–3','n. 3 completo (−2); n. 2 non svolto','n. 2: «manca una parentesi?» (dubbio sul testo)')]
r=5
for x in CMP:riga(ws,r,list(x)+['non risulta','—'],wrap=(2,5,6,7,8));r+=1
for cart in('ITALIANO','STORIA'):riga(ws,r,[cart,'(cartella vuota)','','','','','','','','']);r+=1
for x in('Diritto ed economia','Scienze della terra','Chimica','Tecnologie informatiche','Tecnologie e tecniche di rappresentazione grafica'):riga(ws,r,[x.upper(),'(nessuna cartella creata)','','','','','','','','']);r+=1
r+=1
for t in['Cosa risulta: 7 fogli di Matematica caricati dall\'alunna, che sono 7 pagine diverse (i file «Copia» non sono doppioni). Nessuna correzione del docente: non ci sono segni, voti né file di ritorno.',
 'Da chiedere al docente di Matematica: correzione e voto degli esercizi delle lezioni 253, 254 e 256.',
 'Da portare nella live di verifica di Matematica: i 5 punti in cui l\'alunna si è bloccata o ha segnato un dubbio (colonna «Dubbi»). In due casi segnala che nel testo dell\'esercizio manca una parentesi: va controllato il testo.',
 'I testi dei compiti del docente (i PDF da scaricare) non sono nella cartella: risultano solo i «Download del materiale didattico» dentro le lezioni.']:
    x=ws.cell(r,1,t);x.font=N;ws.merge_cells(start_row=r,start_column=1,end_row=r,end_column=10);x.alignment=Alignment(wrap_text=True);ws.row_dimensions[r].height=28;r+=1
# ---------- 5. Report genitori (bozza) ----------
ws=wb.create_sheet('Report genitori');ws.column_dimensions['A'].width=24;ws.column_dimensions['B'].width=95
ws['A1']='Report settimanale per la famiglia · 2–8 novembre 2026';ws['A1'].font=T
ws['A2']=f"Alunna: {ALUNNA['nome'].title()} · {ALUNNA['indirizzo']}";ws['A2'].font=S
r=4
for c in CORSI:
    fatte=[l for l in c['lez'] if l['st'] in('Svolta','Svolta in anticipo')];meta=[l for l in c['lez'] if l['piano1'] and l['st']=='A metà'];non=[l for l in c['lez'] if l['piano1'] and l['st']=='Non svolta']
    if fatte:
        t=f"Svolte {len(fatte)} lezioni: "+'; '.join(f"{l['tit'].title()} (test {l['pun']})" for l in fatte)+'.'
    else:t='Nessuna lezione svolta questa settimana.'
    if meta or non:t+=f" Da recuperare la prossima settimana: {len(meta)+len(non)} lezioni."
    ws.cell(r,1,c['materia']).font=B;x=ws.cell(r,2,t);x.font=N;x.alignment=Alignment(wrap_text=True,vertical='top');r+=1
r+=1;ws.cell(r,1,'Nota').font=B;x=ws.cell(r,2,'Bozza generata dai dati della piattaforma. Da completare con le valutazioni dei compiti corretti dai docenti e con l\'esito delle lezioni live di verifica.');x.font=S;x.alignment=Alignment(wrap_text=True)
for w in wb.worksheets:
    w.sheet_view.showGridLines=False
    w.page_setup.orientation='landscape';w.page_setup.fitToWidth=1;w.sheet_properties.pageSetUpPr.fitToPage=True;w.page_setup.fitToHeight=0
out='/home/claude/invio/Controllo_settimanale_ALUNNO.xlsx';wb.save(out);print(out)
