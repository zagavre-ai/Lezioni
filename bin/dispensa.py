import sys,json,html,base64
sys.path.insert(0,'/home/claude/w/bin');from conf import CONF
NN=sys.argv[1];C=CONF[NN];N=C['N'];D=f'/home/claude/w/l{NN}/';E=html.escape
U=json.load(open(D+'unita.json'))
def URI(f):return 'data:image/jpeg;base64,'+base64.b64encode(open(f,'rb').read()).decode()
MAT='LETTERATURA ITALIANA';DOC='Prof. Giorgio Mazzotti'
css="""@page{size:297mm 210mm;margin:0}*{box-sizing:border-box;margin:0;padding:0}body{font-family:Figtree,sans-serif;color:#0B1530}
.pg{width:297mm;height:210mm;position:relative;page-break-after:always;background:#fff;overflow:hidden}
.k{font-family:'DM Mono',monospace;letter-spacing:3px;color:#2060AF;font-size:11pt}.t{font-family:'Bricolage Grotesque';font-weight:800}
.f{position:absolute;left:18mm;bottom:9mm;font-family:'DM Mono',monospace;font-size:9pt;color:#6b7590}
.c{background:#EEF0F4;border-left:5px solid #2060AF;border-radius:4mm;padding:5mm 6mm;font-size:13pt;line-height:1.4;margin-bottom:5mm}
.c b{color:#2060AF}"""
P=[f"""<div class=pg style="background:#0B1530;color:#fff"><div style="position:absolute;left:22mm;top:50mm;width:250mm">
<div class=k style="color:#5BD6F0">DISPENSA DIDATTICA · {MAT}</div><div class=t style="font-size:34pt;line-height:1.1;margin-top:8mm">{E(C['titolo'])}</div>
<div style="width:70mm;height:3mm;background:#FFE600;margin:8mm 0;border-radius:2mm"></div><div style="font-size:15pt;font-weight:600">{DOC}</div>
<div style="margin-top:10mm;font-size:13pt;line-height:1.7">{''.join(f'{i+1}. {E(a["t"])}<br>' for i,a in enumerate(C['arg']))}</div></div></div>"""]
n=1
for u in U:
    for j,pg in enumerate(u['pages']):
        n+=1;img=u['img']
        cards=''.join(f"<div class=c>{'<b>'+E(c['lab'])+'</b> ' if c['lab'] else ''}{E(c['txt'])}</div>" for c in pg)
        pic=f'<img src="{URI(D+"img/"+img)}" style="position:absolute;left:18mm;top:42mm;width:62mm;border-radius:3mm">' if img and j==0 else ''
        x=88 if pic else 18
        P.append(f"""<div class=pg><div class=k style="position:absolute;left:18mm;top:14mm">ARGOMENTO {u['k']} · {E(u['t'].upper())}</div>
<div class=t style="position:absolute;left:18mm;top:21mm;width:260mm;font-size:22pt">{E(pg[0]['tit'])}</div>
<div style="position:absolute;left:18mm;top:33mm;width:50mm;height:2mm;background:#FFE600"></div>{pic}
<div style="position:absolute;left:{x}mm;top:42mm;width:{279-x}mm">{cards}</div><div class=f>{MAT} · {DOC} · Pagina {n}</div></div>""")
H='<!doctype html><meta charset=utf-8><style>'+css+'</style>'+''.join(P)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page();pg.set_content(H);pg.evaluate('document.fonts.ready');pg.wait_for_timeout(200)
    pg.pdf(path=D+f'out/Letteratura_Lez{N}_dispensa_A4.pdf',width='297mm',height='210mm',print_background=True);b.close()
print('pagine',len(P))
