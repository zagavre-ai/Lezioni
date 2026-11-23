import sys,os,re,json,subprocess;sys.path.insert(0,'/tmp/w/build')
import plan,tpl
from contents import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,landscape
tl=plan.build()
os.makedirs(f'{plan.B}/disp',exist_ok=True)
def cover(titolo,mappe=False):
    lab='MAPPE' if mappe else ''
    body=tpl.head()+f'<div class=kick style="top:226px">{tpl.esc(tpl.MATERIA)}</div>'
    if mappe:body+=f'<div style="position:absolute;left:80px;top:290px;font:800 40px Bri;letter-spacing:.2em;color:{tpl.BLU}">MAPPE</div>'
    ty=340 if mappe else 290
    body+=f'<div class=tit style="top:{ty}px;font-size:92px;line-height:1.05;width:1500px">{tpl.esc(titolo)}</div><div class=bar style="top:{ty+130}px;width:110px;height:8px"></div>'
    return tpl.doc(body+tpl.foot(1))
pages=[];jobs=[]
cv=f'{plan.B}/disp/cover.html';open(cv,'w').write(cover(TITOLO));jobs.append(dict(html=cv,out=f'{plan.B}/disp/cover.png'))
pages.append(('cover',tpl.MATERIA+'. '+TITOLO))
seen=set()
for html,pg in sorted([d for d in plan.DISP if not str(d[0]).startswith('MAPPA:')],key=lambda d:d[1]):
    if pg==1:continue
    key=(pg,len(html))
    p=f'{plan.B}/disp/p{pg:03d}_{len(html)}.html';open(p,'w').write(html)
    jobs.append(dict(html=p,out=p.replace('.html','.png')))
    txt=re.sub(r'<style>.*?</style>','',html,flags=re.S);txt=re.sub(r'<[^>]+>',' ',txt);txt=re.sub(r'\s+',' ',txt).strip()
    pages.append((p.replace('.html','.png'),txt))
# mappe
mj=[];mp=[('mcover',tpl.MATERIA+'. MAPPE. '+TITOLO)]
mc=f'{plan.B}/disp/mcover.html';open(mc,'w').write(cover(TITOLO,True));jobs.append(dict(html=mc,out=f'{plan.B}/disp/mcover.png'))
for mk in ['M2','M1','M3']:
    M=MAPPE[mk];allb=set(M['boxes'])|set(M['arrows'])
    h=tpl.mappa(M['title'],M['boxes'],M['arrows'],allb,None,1)
    p=f'{plan.B}/disp/map_{mk}.html';open(p,'w').write(h);jobs.append(dict(html=p,out=p.replace('.html','.png')))
    mp.append((p.replace('.html','.png'),M['title']+' '+' '.join(re.sub(r'<[^>]+>','',b[5]).replace('**','') for b in M['boxes'].values())))
json.dump(jobs,open(f'{plan.B}/jobs_pdf.json','w'))
r=subprocess.run(['node',f'{plan.B}/render.js',f'{plan.B}/jobs_pdf.json'],env=dict(os.environ,NODE_PATH='/opt/node22/lib/node_modules'),capture_output=True,text=True);print(r.stderr[-300:])
def mkpdf(out,items,title):
    W,H=landscape(A4);c=canvas.Canvas(out,pagesize=(W,H));c.setTitle(title)
    for i,(img,txt) in enumerate(items):
        if img=='cover':img=f'{plan.B}/disp/cover.png'
        if img=='mcover':img=f'{plan.B}/disp/mcover.png'
        c.setFillColorRGB(1,1,1);c.rect(0,0,W,H,fill=1,stroke=0)
        h=W*1080/1920;c.drawImage(img,0,(H-h)/2,W,h)
        t=c.beginText(20,H-40);t.setTextRenderMode(3);t.setFont('Helvetica',8)
        for ln in re.findall(r'.{1,150}(?:\s|$)',txt)[:40]:t.textLine(ln.strip())
        c.drawText(t);c.showPage()
    c.save()
nm='StoriaArte_Lez14'
mkpdf(f'{plan.B}/{nm}_dispensa_A4.pdf',pages,'Storia dell\'arte V · I nuovi realismi')
mkpdf(f'{plan.B}/{nm}_mappe_A4.pdf',mp,'Storia dell\'arte V · Mappe · I nuovi realismi')
print(len(pages),'pagine dispensa;',len(mp),'pagine mappe')
