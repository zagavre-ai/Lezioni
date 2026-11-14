# -*- coding: utf-8 -*-
# Dispensa A4: copertina, Mappa della lezione, per ogni argomento testo + mappa. Testo vero, leggibile in bianco e nero.
import sys,os,html,importlib,subprocess
sys.path.insert(0,'/home/user/work/build')
S=importlib.import_module(sys.argv[1]);W=os.path.abspath(sys.argv[2])+'/'
from pypdf import PdfReader,PdfWriter
A='/home/user/work/assets/';E=html.escape
CSS="""@font-face{font-family:'Bricolage Grotesque';src:url('file://%sBricolageGrotesque-ExtraBold.ttf');font-weight:800}
@font-face{font-family:'Figtree';src:url('file://%sFigtree-Regular.ttf');font-weight:400}
@font-face{font-family:'Figtree';src:url('file://%sFigtree-SemiBold.ttf');font-weight:600}
@font-face{font-family:'Figtree';src:url('file://%sFigtree-Bold.ttf');font-weight:700}
@page{size:A4;margin:18mm 18mm 20mm 18mm}
body{font-family:Figtree;font-size:12.5pt;line-height:1.45;color:#0B1530}
h1{font-family:'Bricolage Grotesque';font-weight:800;font-size:26pt;margin:0 0 6mm;border-bottom:2pt solid #0B1530;padding-bottom:3mm}
h2{font-family:'Bricolage Grotesque';font-weight:800;font-size:15pt;margin:7mm 0 2mm;page-break-after:avoid}
ul{margin:1mm 0 3mm 5mm;padding-left:4mm}li{margin:0 0 1.5mm}
.k{font-weight:700;letter-spacing:.08em;font-size:10pt;text-transform:uppercase}
.sec{page-break-before:always}
.foot{position:running(foot)}
.cop{height:240mm;display:flex;flex-direction:column;justify-content:center}
.cop .t{font-family:'Bricolage Grotesque';font-weight:800;font-size:44pt;line-height:1.05;margin:6mm 0}
.cop .s{font-size:15pt}
.gl dt{font-weight:700}.gl dd{margin:0 0 2mm 0}
"""%((A,)*4)
def pdf(html_s,out,landscape=False):
    from playwright.sync_api import sync_playwright
    open(out+'.html','w').write('<!doctype html><meta charset="utf-8"><style>'+CSS+'</style>'+html_s)
    with sync_playwright() as p:
        b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',args=['--no-sandbox']);pg=b.new_page()
        pg.goto('file://'+out+'.html');pg.wait_for_timeout(300);pg.pdf(path=out,format='A4',print_background=True,margin=dict(top='18mm',bottom='20mm',left='18mm',right='18mm'),display_header_footer=True,
            header_template='<span></span>',footer_template='<div style="font-size:8pt;width:100%%;text-align:center;font-family:Figtree">%s · %s · pagina <span class="pageNumber"></span></div>'%(E(S.MATERIA),E(S.DOCENTE)))
        b.close()
    os.remove(out+'.html')
os.makedirs(W+'dis',exist_ok=True)
w=PdfWriter();parti=[]
cop='<div class="cop"><div class="k">Centro Studi Telesio</div><div class="t">%s</div><div class="s">%s<br>%s</div></div>'%(E(S.TITOLO),E(S.MATERIA),E(S.DOCENTE))
pdf(cop,W+'dis/cop.pdf');parti.append(W+'dis/cop.pdf')
parti.append(W+'mp/MF1/mappa_dispensa.pdf')   # Mappa della lezione
for a in S.ARGS:
    h='<div class="k">Argomento %d</div><h1>%s</h1>'%(a['n'],E(a['titolo']))
    for sl in a['slides']:
        h+='<h2>%s</h2><ul>%s</ul>'%(E(sl['t']),''.join('<li>%s</li>'%E(c) for c in sl['c']))
    h+='<h2>Per ripassare</h2><p>%s</p>'%E(a['ripasso'])
    pdf(h,W+'dis/a%d.pdf'%a['n']);parti.append(W+'dis/a%d.pdf'%a['n']);parti.append(W+'mp/MP%d/mappa_dispensa.pdf'%a['n'])
h='<div class="k">Glossario</div><h1>Le parole chiave</h1><dl class="gl">%s</dl>'%''.join('<dt>%s</dt><dd>%s</dd>'%(E(t),E(d[0].upper()+d[1:])) for t,d in S.GLOSSARIO)
pdf(h,W+'dis/gl.pdf');parti.append(W+'dis/gl.pdf')
for p in parti:
    for pg in PdfReader(p).pages:w.add_page(pg)
w.add_metadata({'/Title':'%s · dispensa'%S.TITOLO})
out=W+'Dispensa_%s.pdf'%S.FILE;w.write(out);print(out,len(w.pages),'pagine')
