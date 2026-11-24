import sys, os, json, pickle, shutil, subprocess, re
sys.path.insert(0,'/home/claude/w/code')
from lesson import *
from dispensa import *
from finalize import load_ctx
DEL=f'{W}/consegna';os.makedirs(DEL,exist_ok=True)
def covers(rend):
    items=lambda extra: ([dict(id='m',html='<div class=k2 style="font-size:60px;letter-spacing:.3em">MAPPE</div>',x=160,y=120,t_in=0)] if extra else [])
    for nm,extra in (('cover_dispensa',False),('cover_mappe',True)):
        it=[dict(id='k',html='<div class=k2>Storia V · Videolezione</div>',x=160,y=330 if not extra else 410,t_in=0),
            dict(id='t',html='<div class=big style="width:1500px;font-size:110px">Il mondo<br>dal 2001 ad oggi</div>',x=160,y=390 if not extra else 470,t_in=0),
            dict(id='b',html='<div style="width:260px;height:10px;background:#FFE600;border-radius:5px"></div>',x=160,y=700 if not extra else 780,t_in=0)]+items(extra)
        h=dark_page(it)
        still(rend,h,5.0,f'{SL}/{nm}.png')
def senza_prof(png):
    """pagina per la dispensa: senza riquadro e fascia del docente (come nel modello Spagnolo); le parole chiave salgono"""
    from PIL import Image
    out=png[:-4]+'_D.png'
    im=Image.open(png).convert('RGB');kw=im.crop((1400,625,1870,900))
    from PIL import ImageDraw
    ImageDraw.Draw(im).rectangle((1380,135,1880,960),fill='white')
    im.paste(kw,(1400,150));im.save(out)
    if os.path.exists(png+'.txt'): open(out+'.txt','w').write(open(png+'.txt').read().replace('Giorgio Mazzotti','').replace('PROF. DI STORIA',''))
    return out
def build_pdfs(rend):
    covers(rend)
    for part in (1,2):
        c=load_ctx(part)
        pages=[(f'{SL}/cover_dispensa.png','Storia V. Videolezione. Il mondo dal 2001 ad oggi.',None)]
        for png,testo,num in c.dispensa:
            b=os.path.basename(png)
            if re.match(r'(a\d_win_|a\d_photo_|intro)',b): png=senza_prof(png)
            pages.append((png,read_txt(png) or testo,num))
        # copertina senza numero
        out=f'{DEL}/Storia_Lez21_Parte{part}_dispensa.pdf'
        # la prima pagina e' la copertina: niente piè di pagina numerato
        pdf_pages=[]
        from reportlab.pdfgen import canvas
        pdf(pages,out,f'Storia V · Il mondo dal 2001 ad oggi · Parte {part}')
        print('dispensa',out,len(pages))
    # mappe
    mp=[(f'{SL}/cover_mappe.png','MAPPE. Storia V. Videolezione. Il mondo dal 2001 ad oggi.',None)]
    for k,m in enumerate(['M1','M2','M3','M4A','M4B'],1):
        mp.append((f'{SL}/{m}.png',read_txt(f'{SL}/{m}.png'),k))
    pdf(mp,f'{DEL}/Storia_Lez21_mappe.pdf','Storia V · MAPPE · Il mondo dal 2001 ad oggi')
def json_files():
    Q={f'Q{n}':dict(title=f"Quiz {n} · {ARG[n-1]['tit']}",items=QZ[n]) for n in range(1,8)}
    json.dump(Q,open(f'{DEL}/quiz_argomenti.json','w'),ensure_ascii=False,indent=1)
    shutil.copy(f'{W}/verifica.json',f'{DEL}/verifica_sbarramento.json') if os.path.exists(f'{W}/verifica.json') else None
    comp=[dict(n=k+1,testo=t) for k,t in enumerate(json.load(open(f'{W}/compiti_prof.json')))]
    json.dump(comp,open(f'{DEL}/compiti.json','w'),ensure_ascii=False,indent=1)
if __name__=='__main__':
    r=R();build_pdfs(r);json_files();r.close()
