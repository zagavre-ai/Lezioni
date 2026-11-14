# Dispensa A4 (orizzontale) con testo vero e mappe concettuali. uso: dispensa.py LEZ_DIR USCITA.pdf
import sys,os,json,glob,importlib.util,subprocess,html,re
sys.path.insert(0,'/home/user/lav/tools')
import pdfplumber,pypdf
from lib import FONT,pulisci
from playwright.sync_api import sync_playwright
L=os.path.abspath(sys.argv[1]);OUT=sys.argv[2]
spec=importlib.util.spec_from_file_location('dati',L+'/lav/dati.py');dati=importlib.util.module_from_spec(spec);spec.loader.exec_module(dati)
W=L+'/disp/';os.makedirs(W,exist_ok=True)
pdf=pdfplumber.open(glob.glob(L+'/LEZIONE*.pdf')[0])
CSS='''@font-face{font-family:'Bricolage Grotesque';src:url('file://%sBricolageGrotesque-ExtraBold.ttf');font-weight:800}
@font-face{font-family:'Figtree';src:url('file://%sFigtree-Regular.ttf');font-weight:400}
@font-face{font-family:'Figtree';src:url('file://%sFigtree-Bold.ttf');font-weight:700}
@page{size:297mm 210mm;margin:0}*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Figtree,sans-serif;color:#0B1530;width:297mm;height:210mm;padding:16mm 18mm;position:relative}
h1{font:800 30pt/1.1 'Bricolage Grotesque';color:#0B1530}h2{font:800 20pt/1.15 'Bricolage Grotesque';margin-bottom:6mm}
.k{font-weight:700;letter-spacing:2px;font-size:10pt;color:#2060AF;margin-bottom:3mm}
.c{border:1.2pt solid #0B1530;border-left:6pt solid #2060AF;padding:3.5mm 5mm;margin-bottom:3.5mm;font-size:13.5pt;line-height:1.35;border-radius:2mm}
.t{font-size:10.5pt;line-height:1.4;margin-top:5mm;border-top:1pt solid #C9D0DC;padding-top:4mm;column-count:2;column-gap:10mm;max-height:58mm;overflow:hidden}
.kw{margin-top:4mm;font-size:12pt}.kw b{border:1pt solid #0B1530;border-radius:3mm;padding:1mm 3mm;margin-right:2mm;display:inline-block;margin-bottom:2mm}
.f{position:absolute;left:18mm;right:18mm;bottom:9mm;border-top:1pt solid #C9D0DC;padding-top:2mm;font-size:9pt;font-weight:700;letter-spacing:1.5px;color:#2060AF}
'''%(FONT,FONT,FONT)
def page(body):return '<html><head><meta charset="utf-8"><style>%s</style></head><body>%s<div class="f">STORIA · Prof. Giorgio Mazzotti · Dispensa</div></body></html>'%(CSS,body)
E=html.escape
PAG={1:[1],2:[2],3:[3],4:[4],5:[5],6:[6,7],7:[9],8:[9]}
def testo(k):
    return ' '.join(' '.join((pdf.pages[i].extract_text() or '').split()) for i in dati.DISP[k])
pages=[]
pages.append(('cover',page('<div style="margin-top:55mm"><div class="k">CENTRO STUDI TELESIO · STORIA · TERZO ANNO</div><h1>%s</h1><p style="margin-top:12mm;font-size:16pt">Prof. Giorgio Mazzotti</p><p style="margin-top:4mm;font-size:12pt">Dispensa della lezione con mappe concettuali</p></div>'%E(dati.TITOLO_LEZ))))
args=sorted(dati.ARG)
for k in args:
    tit,kws,cards=dati.ARG[k]
    b='<div class="k">ARGOMENTO %d</div><h2>%s</h2>'%(k,E(tit))
    b+=''.join('<div class="c">%s</div>'%E(c[0]) for c in cards)
    b+='<div class="kw"><i>Parole chiave:</i> '+''.join('<b>%s</b>'%E(x) for x in kws)+'</div>'
    t=testo(k)
    if t.strip():b+='<div class="t">%s</div>'%E(t[:1500])
    pages.append(('arg%d'%k,page(b)))
with sync_playwright() as p:
    br=p.chromium.launch();pg=br.new_page()
    for nm,h in pages:
        pg.set_content(h);pg.wait_for_timeout(600);pg.pdf(path=W+nm+'.pdf',width='297mm',height='210mm',print_background=True)
    br.close()
# mappe (solo pdf)
def mappa_pdf(key):
    tit,rami=dati.MAPPE[key];od=W+key+'/';os.makedirs(od,exist_ok=True)
    js=dict(materia="Storia",docente="Prof. Giorgio Mazzotti",titolo=tit,rami=[dict(concetto=c,parola=p,esempio=e) for c,p,e,_ in rami])
    json.dump(js,open(od+'mappa.json','w'),ensure_ascii=False)
    if not os.path.exists(od+'mappa_dispensa.pdf'):subprocess.run(['python3','/home/user/Lezioni/kit/tools/mappa.py',od+'mappa.json','--out',od,'--solo-pdf'],check=True,capture_output=True)
    return od+'mappa_dispensa.pdf'
w=pypdf.PdfWriter()
def app(f):
    for pgx in pypdf.PdfReader(f).pages:w.add_page(pgx)
app(W+'cover.pdf');app(mappa_pdf(dati.MAPPA_LEZ))
for k in args:
    app(W+'arg%d.pdf'%k);app(mappa_pdf('CM%d'%k))
w.write(OUT);print(OUT,len(w.pages),'pagine')
