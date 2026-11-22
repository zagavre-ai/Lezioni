import sys,os,json,subprocess,hashlib
sys.path.insert(0,'/tmp/w/b')
import lib
lib.NOCAM=True
import plan
from plan import *
from pypdf import PdfWriter,PdfReader
from PIL import Image
def cover_disp(label=None):
    h="<img class='logo' src='file://%s/assets/logo.png'><div class='hr'></div><div class='hr2'></div>"%B
    h+="<div class='foot' style='left:80px'>STORIA</div>"
    h+=f"<div class='eyebrow'>STORIA · VIDEOLEZIONE</div>"
    h+=f"<div class='title' style='top:230px;width:1700px;font-size:104px;color:#2060AF;line-height:1.06'>GLI ANNI NOVANTA:<br>IL MONDO POST-BIPOLARE</div><div class='bar' style='top:490px'></div>"
    if label: h+=f"<div style='position:absolute;left:80px;top:540px;font-family:Bricolage Grotesque;font-weight:800;font-size:84px;color:#0B1530;letter-spacing:.04em'>{label}</div>"
    return pagina(h)
def make_pdf(pages_html,out):
    os.makedirs('/tmp/w/b/dp',exist_ok=True);jobs=[];pdfs=[]
    for i,hh in enumerate(pages_html):
        f=f'/tmp/w/b/dp/{os.path.basename(out)}_{i:02d}.html';p=f[:-5]+'.pdf';open(f,'w').write(hh);jobs.append({'html':f,'pdf':p});pdfs.append(p)
    json.dump(jobs,open('/tmp/w/b/dp/jobs.json','w'));subprocess.run(['node','/tmp/w/b/pdfmaker.js','/tmp/w/b/dp/jobs.json'],check=True,cwd='/tmp/w')
    w=PdfWriter()
    for p in pdfs:
        for pg in PdfReader(p).pages:w.add_page(pg)
    w.write(out);print(out,len(pdfs))
def pages_for(reg,part):
    H=[cover_disp()]
    if part==1: H.append(argomenti_slide(None,cam=False))
    for key in sorted(reg.d,key=lambda k:reg.d[k]):
        n=reg.d[key]
        if key[0]=='slide':
            A=ARGS[key[1]-1];pg=pages(A['cards'])[key[2]]
            H.append(slide_state(key[1],pg,key[3],n,focus=True) if key[4] else slide_state(key[1],pg,None,n))
        elif key[0]=='img':
            cap,arg=IMG_ARG[key[1]];p=f'{B}/img/{key[1]}.png';w,h=Image.open(p).size
            H.append(image_state(arg,p,ST.IMG[key[1]][0],n,w,h))
    return H
IMG_ARG={'cecenia':(0,1),'kuwait':(0,2),'iugoslavia':(0,3),'ue':(0,4),'ritratti':(0,5)}
if __name__=='__main__':
    part=int(sys.argv[1]);out=sys.argv[2]
    P,reg=(plan.build_part1() if part==1 else plan.build_part2())
    make_pdf(pages_for(reg,part),out)
