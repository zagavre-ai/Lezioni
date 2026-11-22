# Slide divise per scene dal Word del docente (modello Telesio): una scena = una slide = un F9.
# uso: python3 scene_dal_word.py TESTO.docx "INGLESE" "Prof.ssa Nome Cognome" "Titolo della lezione" USCITA.pdf
# Esercizi e quiz NON vanno nelle slide: al loro posto una pagina gialla «STOP · ESERCIZIO» (solo per il docente).
# In fondo: pagina gialla «RIPASSO FINALE» e «Thank you». Mai il numero di lezione.
import json,html,base64,re,sys,os,tempfile
import docx
from docx.oxml.ns import qn
from playwright.sync_api import sync_playwright
W,MAT,DOC,TIT,OUT=sys.argv[1:6]
WD=tempfile.mkdtemp(prefix='scene_')
def blocchi(path):
    d=docx.Document(path);B=[];ni=0
    for el in d.element.body.iterchildren():
        if el.tag==qn('w:p'):
            p=docx.text.paragraph.Paragraph(el,d)
            for bl in el.iter(qn('a:blip')):
                rid=bl.get(qn('r:embed'))
                if rid and rid in d.part.related_parts:
                    ni+=1;f=f'img{ni}.png';open(os.path.join(WD,f),'wb').write(d.part.related_parts[rid].blob);B.append({'t':'img','f':f})
            x=p.text.strip()
            if not x:continue
            st=p.style.name if p.style is not None else 'Normal'
            li=el.find('.//'+qn('w:numPr')) is not None or 'List' in st
            B.append({'t':'li' if li and not st.startswith('Heading') else 'p','x':x,'s':st})
        elif el.tag==qn('w:tbl'):
            t=docx.table.Table(el,d);B.append({'t':'tbl','rows':[[c.text.strip() for c in r.cells] for r in t.rows]})
    return B
B=blocchi(W)
# salta la tabella «Come si compila» del modello
B=[b for b in B if not (b['t']=='tbl' and b['rows'] and b['rows'][0][0].startswith('Come si compila'))]
LBL={'Regola':'Rule','Esempi':'Examples','Spiegazione degli esempi':'Examples explained','Audio (se previsto)':'Listening','Ascolto e pronuncia':'Listening','Esercizio con soluzione':'Exercise'}
ESE=('Esercizio con soluzione',"Quiz dell'argomento")
esc=html.escape
# 1) struttura: (argomento, sezione, lingua, elementi)
S=[];topic=('','');sec='';lang='';i=0
while i<len(B) and not (B[i].get('s')=='Heading 1'):i+=1
intro=[];topics=[]
cur=None
for b in B[i:]:
    x=b.get('x','')
    if b['t']=='p' and b.get('s')=='Heading 1':
        if x.startswith('Introduzione'):topic=('00','Introduction')
        else:
            m=re.match(r'Argomento (\d+)\s*[—-]\s*(.+)',x);topic=('%02d'%int(m.group(1)),m.group(2));topics.append(topic)
            S.append({'k':'titolo','topic':topic})
        sec='';lang='';continue
    if b['t']=='p' and b.get('s')=='Heading 2':sec=x;lang='';continue
    if b['t']=='p' and x in('ENGLISH','ITALIANO'):lang=x;continue
    if b['t']=='p' and x=='ANSWER KEY':sec='Esercizio con soluzione';lang='KEY';continue
    S.append({'k':'el','topic':topic,'sec':sec,'lang':lang,'b':b})
# 2) raggruppa in scene
SC=[];buf=[];key=None;w=0
def flush():
    global buf,w
    if buf:SC.append({'topic':key[0],'sec':key[1],'lang':key[2],'items':buf})
    buf=[];w=0
def peso(b):
    if b['t'] in('img','tbl'):return 999
    import math;return (math.ceil(len(b['x'])/72)*46+20)/150
for s in S:
    if s['k']=='titolo':flush();key=None;SC.append({'titolo':s['topic']});continue
    b=s['b'];k=(s['topic'],s['sec'],s['lang'])
    if k!=key:flush();key=k
    if b['t'] in('img','tbl'):
        cap=[x for x in buf if x['t']=='p' and len(x['x'])<90 and x['x'].endswith(':')]
        rest=[x for x in buf if x not in cap]
        buf=rest;flush();key=k;buf=cap+[b];flush();key=k;continue
    ex=s['sec'] in ESE and s['lang']!='KEY'
    if ex:
        q=re.match(r'^\d+\.\s',b['x']) or (b['t']=='p' and b['x'].endswith('?'))
        lim=6.5 if s['topic'][0] in('01','04') else 6
        op=b['t']=='li' or re.match(r'^[A-Da-d]\.\s',b['x'])
        if ((q and w+peso(b)>4.0) or (not op and w+peso(b)>4.8)) and buf:flush();key=k
    else:
        if w+peso(b)>4.8 and buf:flush();key=k
    buf.append(b);w+=peso(b)
flush()
# 3) html
def logo():return 'data:image/svg+xml;base64,'+base64.b64encode(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','docenti','Telesio_logo_inchiostro.svg'),'rb').read()).decode()
L=logo()
CSS='''@page{size:1920px 1080px;margin:0}*{box-sizing:border-box}body{margin:0}
.s{width:1920px;height:1080px;position:relative;overflow:hidden;background:#fff;font-family:Figtree,sans-serif;color:#0B1530;page-break-after:always}
.hd{position:absolute;left:76px;top:44px;right:76px;height:70px;display:flex;align-items:center;gap:28px;border-bottom:2px solid #EEF0F4}
.hd img{height:52px}.hd .r{font:500 22px "DM Mono";letter-spacing:.12em;color:#2060AF}
.sc{position:absolute;right:76px;top:58px;font:600 22px "DM Mono";color:#0B1530;background:#FFE600;padding:6px 14px;border-radius:6px}
.cam{position:absolute;left:1490px;top:150px;width:354px;height:266px;border:2px dashed #C9D0DC;border-radius:14px;display:flex;align-items:center;justify-content:center;font:500 20px "DM Mono";color:#9AA3B5;text-align:center}
.ar{position:absolute;left:76px;top:150px;width:1384px;bottom:110px}
h1{font:800 54px "Bricolage Grotesque";margin:0 0 6px;line-height:1.05}.bar{width:108px;height:6px;background:#2060AF;margin:14px 0 34px}
.lab{font:500 22px "DM Mono";letter-spacing:.1em;color:#2060AF;margin-bottom:10px}
p{font-size:34px;line-height:1.38;margin:0 0 20px}
ul{margin:0;padding:0;list-style:none}li{font-size:32px;line-height:1.34;margin:0 0 14px;padding-left:34px;position:relative}li:before{content:"";position:absolute;left:4px;top:15px;width:12px;height:12px;border-radius:50%;background:#2060AF}
.op li:before{display:none}.op li{padding-left:18px;font-size:29px;margin-bottom:8px}
img.f{max-width:1384px;max-height:700px;display:block;border:1px solid #EEF0F4;border-radius:8px}
table{border-collapse:collapse;width:100%;font-size:26px}td,th{border:1px solid #C9D0DC;padding:10px 14px;vertical-align:top;text-align:left}th{background:#EEF0F4}
.ft{position:absolute;left:76px;right:76px;bottom:40px;border-top:2px solid #EEF0F4;padding-top:14px;font:500 20px "DM Mono";letter-spacing:.08em;color:#5B6478}
.tt{background:#0B1530;color:#fff}.tt h1{color:#fff;font-size:96px}.tt .r{color:#FFE600}
.cue{background:#FFE600}.cue .cam{display:none}.cue .sc{background:#0B1530;color:#FFE600}
.big{position:absolute;left:76px;top:330px;width:1384px}.num{font:800 160px "Bricolage Grotesque";color:#FFE600;line-height:1}
'''
def frame(n,riga,body,extra=''):
    return f'<div class="s {extra}"><div class="hd"><img src="{L}"><span class="r">{esc(riga)}</span></div><div class="sc">SCENA {n}</div><div class="cam">riquadro<br>docente</div><div class="ar">{body}</div><div class="ft">{MAT} · {DOC}</div></div>'
P=[];n=0
def add(riga,body,extra=''):
    global n;n+=1;P.append(frame(n,riga,body,extra))
# copertina
add(MAT,f'<div style="margin-top:140px"><div class="lab">VIDEOLEZIONE</div><h1 style="font-size:88px">{esc(TIT)}</h1><div class="bar"></div><div class="lab">{MAT} · {DOC}</div><ul style="margin-top:30px">'+''.join(f'<li>{esc(t[1])}</li>' for t in topics)+'</ul></div>')
CUE='<div style="margin-top:40px"><div class="lab" style="color:#0B1530">INDICAZIONE PER LEI · QUESTA PAGINA NON VA NEL VIDEO</div><h1 style="font-size:84px">{t}</h1><div class="bar" style="background:#0B1530"></div><p style="font-size:38px">{d}</p></div>'
fatti=set()
for sc in SC:
    if sc.get('sec') in ESE:
        nn=sc['topic'][0]
        if nn in fatti:continue
        fatti.add(nn)
        add(f'{MAT} · {nn} · {sc["topic"][1].upper()}',CUE.format(t='STOP · ESERCIZIO',d='Fine dell’argomento '+str(int(nn))+'. Introduca l’esercizio con una frase, ad esempio: <b>«Now let’s check what you have learned with a short exercise.»</b><br><br>Poi si fermi. Non legga domande né soluzioni: l’esercizio lo inseriamo noi in montaggio. Alla scena successiva riparte con l’argomento nuovo.'),'cue');continue
    if 'titolo' in sc:
        nn,tt=sc['titolo'];add(f'{MAT} · {nn}',f'<div class="big"><div class="num">{nn}</div><h1>{esc(tt)}</h1><div class="bar"></div></div>');continue
    nn,tt=sc['topic'];riga=f'{MAT} · {nn} · {tt.upper()}' if nn!='00' else f'{MAT} · INTRODUCTION'
    lab=LBL.get(sc['sec'],'')+(' · '+('English' if sc['lang']=='ENGLISH' else 'Italiano') if sc['lang'] in('ENGLISH','ITALIANO') else '')+(' · Answer key' if sc['lang']=='KEY' else '')
    h=f'<div class="lab">{esc(lab.upper())}</div>' if lab else ''
    ex=sc['sec'] in ESE and sc['lang']!='KEY'
    ul=False
    for b in sc['items']:
        if b['t']=='img':h+=f'<img class="f" src="file://{WD}/{b["f"]}">';continue
        if b['t']=='tbl':
            r=b['rows'];h+='<table>'+''.join('<tr>'+''.join((f'<th>{esc(c)}</th>' if i==0 else f'<td>{esc(c)}</td>') for c in row)+'</tr>' for i,row in enumerate(r))+'</table>';continue
        x=esc(b['x'])
        opt=ex and (re.match(r'^[A-Da-d]\.\s',b['x']) or (b['t']=='li' and not b['x'].endswith('?')))
        if b['t']=='li' or opt:
            if not ul:h+='<ul class="'+('op' if opt else '')+'">';ul=True
            h+=f'<li>{x}</li>'
        else:
            if ul:h+='</ul>';ul=False
            h+=f'<p{" style=\"font-weight:700\"" if ex else ""}>{x}</p>'
    if ul:h+='</ul>'
    add(riga,h)
add(MAT,CUE.format(t='RIPASSO FINALE',d='Riassuma a voce, in 1-2 minuti, i 5 argomenti della lezione: SWOT Analysis, Job Adverts, CV and Cover Letter, Job Interview, Elevator Pitch.<br><br>Parli liberamente, senza leggere. Poi passi alla scena successiva per i saluti.'),'cue')
add(MAT,'<div style="margin-top:220px"><h1 style="font-size:88px">Thank you</h1><div class="bar"></div><p>Fine della lezione · Grazie per l\'attenzione</p></div>')
open(os.path.join(WD,'scene.html'),'w').write('<!doctype html><html><head><meta charset="utf-8"><style>'+CSS+'</style></head><body>'+''.join(P)+'</body></html>')
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1920,'height':1080});pg.goto('file://'+WD+'/scene.html');pg.wait_for_timeout(800)
    # controllo: contenuto che esce dall'area
    over=pg.evaluate('''()=>[...document.querySelectorAll('.ar')].map((a,i)=>[i+1,a.scrollHeight>a.clientHeight+2]).filter(x=>x[1]).map(x=>x[0])''')
    pg.pdf(path=OUT,width='1920px',height='1080px',print_background=True);b.close()
print(n,'scene; troppo piene:',over)
