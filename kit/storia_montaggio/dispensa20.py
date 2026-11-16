import sys,os,json,re
sys.path.insert(0,'/home/user/Lezioni/storia_s7')
os.environ['PLAYWRIGHT_BROWSERS_PATH']='/opt/pw-browsers'
from lib import *
from slides20 import SLIDES,sents
from spec20 import *
from pypdf import PdfWriter,PdfReader
W='/tmp/w20/w';OUT='/tmp/w20/out'
T={o['nome']:o['testo'] for o in json.load(open('/tmp/w20/scambio/storia-V-lez20/testi_voci.json'))}
ANN={k:'abc' for k in range(1,9)}
CSS2="""
@page{size:A4;margin:18mm 16mm}
body{background:#fff;color:#111;font-family:FG;font-size:12.5pt;line-height:1.45}
h1{font-family:BG;font-weight:800;font-size:26pt;margin:0 0 6mm;color:#0B1530}
h2{font-family:BG;font-weight:800;font-size:17pt;margin:7mm 0 3mm;color:#0B1530;border-bottom:2px solid #0B1530;padding-bottom:1mm}
h3{font-size:12.5pt;margin:4mm 0 1mm;color:#0B1530}
.cover{height:240mm;display:flex;flex-direction:column;justify-content:center}
.cover h1{font-size:38pt}.k{letter-spacing:.2em;text-transform:uppercase;font-weight:700;font-size:11pt}
.box{border:1.5pt solid #333;border-radius:3mm;padding:3mm 4mm;margin:2.5mm 0;break-inside:avoid}
.box b{color:#000}ul{margin:1mm 0 1mm 5mm;padding:0}li{margin:.8mm 0}
.pb{break-before:page}.small{font-size:10.5pt;color:#333}
.gl td{border:1pt solid #444;padding:2mm 3mm;vertical-align:top}.gl{border-collapse:collapse;width:100%;margin-top:3mm}
"""
def e(x):return html.escape(x)
def arg_html(k):
    t,kick,cards=SLIDES[k-1];a=ARGS[k-1][0]
    h=f'<div class="pb"></div><div class="k">Argomento {k}</div><h1>{e(a)}</h1>'
    h+='<h2>Le idee principali</h2>'+''.join(f'<div class="box"><b>{e(l)}:</b> {e(r)}</div>' for l,r in cards)
    h+='<h2>Approfondimenti</h2>' if any(f'AN{k}{x}' in AN for x in 'abc') else ''
    for x in ANN[k]:
        if f'AN{k}{x}' not in AN:continue
        s=AN[f'AN{k}{x}'];h+=f'<h3>{e(s["title"])}</h3><ul>'+''.join(f'<li><b>{e(i["h"])}</b>'+(f' — {e(i["s"])}' if i.get('s') else '')+'</li>' for i in s['items'])+'</ul>'
    h+='<h2>In breve</h2><p>'+e(T[f'R{k}'].replace('Ripasso. ','',1))+'</p>'
    return h
def gl_html():
    rows=''
    for n in ('GL1',):
        for s in sents(T[n]):
            if ':' in s:a,b=s.split(':',1);rows+=f'<tr><td><b>{e(a)}</b></td><td>{e(b.strip())}</td></tr>'
    return f'<div class="pb"></div><h1>Glossario</h1><table class="gl">{rows}</table>'
def pdf(html_body,path):
    with sync_playwright() as p:
        b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',args=['--no-sandbox','--allow-file-access-from-files'])
        pg=b.new_page();hf=path+'.html';open(hf,'w').write(f'<!doctype html><meta charset="utf-8"><style>{CSS}{CSS2}</style><body style="width:auto;height:auto;overflow:visible">{html_body}</body>');pg.goto('file://'+hf);pg.wait_for_timeout(400)
        pg.pdf(path=path,format='A4',margin={'top':'18mm','bottom':'18mm','left':'16mm','right':'16mm'},print_background=True);b.close()
def build():
    os.makedirs(W+'/dsp',exist_ok=True)
    pdf(f'<div class="cover"><div class="k">Storia · Quinto anno · Centro Studi Telesio</div><h1>{e(TITOLO)}</h1><p>Dispensa della videolezione del Prof. Giorgio Mazzotti</p><p class="small">Dentro trovi: la mappa della lezione, per ogni argomento le idee principali, gli approfondimenti, un breve ripasso e la mappa concettuale, e alla fine il glossario.</p></div>',W+'/dsp/cover.pdf')
    # mappa della lezione
    md=W+'/map/LEZ';os.makedirs(md,exist_ok=True)
    m={'materia':'Storia','docente':'Prof. Giorgio Mazzotti','titolo':'Anni Novanta','rami':[
      {'concetto':'Crollo dell\'URSS','parola':'1991','esempio':'fine del bipolarismo'},
      {'concetto':'Stati Uniti','parola':'unica superpotenza','esempio':'Guerra del Golfo'},
      {'concetto':'Ex Iugoslavia','parola':'guerre 1991-1995','esempio':'Kosovo 1999'},
      {'concetto':'Europa','parola':'Maastricht 1992','esempio':'riunificazione tedesca'},
      {'concetto':'Italia','parola':'Seconda Repubblica','esempio':'Mani pulite, Berlusconi'},
      {'concetto':'Resto del mondo','parola':'nuovi conflitti','esempio':'Medio Oriente, Africa, Asia'}]}
    json.dump(m,open(md+'/mappa.json','w'),ensure_ascii=False)
    run(['python3','/home/user/Lezioni/kit/tools/mappa.py',md+'/mappa.json','--out',md,'--solo-pdf'])
    w=PdfWriter()
    for p in PdfReader(W+'/dsp/cover.pdf').pages:w.add_page(p)
    for p in PdfReader(md+'/mappa_dispensa.pdf').pages:w.add_page(p)
    for k in range(1,9):
        pdf(arg_html(k),W+f'/dsp/a{k}.pdf')
        for p in PdfReader(W+f'/dsp/a{k}.pdf').pages:w.add_page(p)
        for p in PdfReader(W+f'/map/MAP{k}/mappa_dispensa.pdf').pages:w.add_page(p)
    pdf(gl_html(),W+'/dsp/gl.pdf')
    for p in PdfReader(W+'/dsp/gl.pdf').pages:w.add_page(p)
    w.write(OUT+'/Storia_Lez20_dispensa.pdf')
    print('pagine',len(w.pages))
build()
