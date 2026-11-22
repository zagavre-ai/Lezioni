# Dispensa A4 orizzontale identica al video + strato di testo invisibile; PDF delle mappe a parte con copertina «MAPPE»
import sys,os,json,re,glob
sys.path.insert(0,'/home/user/Lezioni/lez14')
from lib import *;import slide as S,spec
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
SL=json.load(open(W+'/slides.json'));WK=W+'/disp';os.makedirs(WK,exist_ok=True)
VT={x['nome']:x['testo'] for x in json.load(open(W+'/old/testi_voci.json'))}
KEYS=spec.KEYS
def pagina(parte,p,k):
    out=f'{WK}/p{parte}_{p:02d}.png';testo=''
    if k[0]=='c':
        pg,win=k[1],k[2];pars=SL[pg]['par']
        n=next(n for n in spec.ARG if any(sc[0]=='c' and sc[1]==pg and set(win)<=set(sc[2]) for sc in spec.ARG[n][3]))
        h=f'{WK}/p{parte}_{p:02d}.html'
        html=S.page(f'Argomento {n} · {spec.ARG[n][0]}',SL[pg]['titolo'],pars,list(win),None,None,p,KEYS[pg],cam=False)
        html=html.replace('mark{','#kw{top:150px!important}mark{',1).replace('class="c"','class="c" style="opacity:1"')
        html=html.replace('.c{','.c{opacity:1!important;',1)
        open(h,'w').write(html);shots([{'html':h,'out':out,'force':True}],f'jd{parte}{p}')
        testo=SL[pg]['titolo']+'\n'+'\n'.join(pars[i] for i in win)+'\n'+' · '.join(KEYS[pg])
    elif k[0]=='i':
        img,cap=spec.IMG[k[1]];n=next(n for n in spec.ARG if any(sc[0]=='i' and sc[1]==k[1] for sc in spec.ARG[n][3]))
        h=f'{WK}/p{parte}_{p:02d}.html'
        open(h,'w').write(S.page(f'Argomento {n} · {spec.ARG[n][0]}',cap,[],[],None,None,p,[],cam=False))
        shots([{'html':h,'out':out,'force':True}],f'jd{parte}{p}')
        b=Image.open(out).convert('RGB');im=Image.open(f'{W}/wk/{img}_hq.png' if os.path.exists(f'{W}/wk/{img}_hq.png') else f'{W}/img/{img}').convert('RGB')
        sc=min(1700/im.width,640/im.height);im=im.resize((int(im.width*sc),int(im.height*sc)),Image.LANCZOS)
        b.paste(im,((1920-im.width)//2,300));b.save(out);testo=cap
    elif k[0]=='PS':
        out=f'{W}/pezzi/PS{k[1]}_finale.png'
        testo='Schema di ripasso\n'+'\n'.join(VT.get(f'PR{k[1]}{j}','') for j in range(1,7))
    elif k[0]=='MAP':
        out=f'{W}/pezzi/MAP{ {1:1,6:2,7:3}[k[1]] }_finale.png'
        svg=open(out.replace('_finale.png','.svg')).read();testo=' '.join(re.findall(r'>([^<>]{2,})<',svg))
    return out,testo
def pdf(pagine,dest):
    c=canvas.Canvas(dest,pagesize=(841.89,595.28));Wp,Hp=841.89,595.28
    for img,testo in pagine:
        im=Image.open(img);h=Wp*im.height/im.width;y=(Hp-h)/2
        c.drawImage(ImageReader(im.convert('RGB')),0,y,Wp,h)
        t=c.beginText(30,Hp-40);t.setTextRenderMode(3);t.setFont('Helvetica',9)
        for line in testo.split('\n'):t.textLine(line)
        c.drawText(t);c.showPage()
    c.save()
if __name__=='__main__':
    num,el=spec.numeri_pagina();titolo='La guerra fredda (1945-1961)'
    for parte in (1,2):
        pag=[(f'{W}/pezzi/COVER{parte}.png',f'STORIA V · VIDEOLEZIONE · PARTE {parte}\n{titolo}')]
        for (pt,p,k) in el:
            if pt==parte:pag.append(pagina(parte,p,k))
        pdf(pag,f'/tmp/w/Storia_Lez14_Parte{parte}_dispensa.pdf');print('dispensa',parte,len(pag),'pagine')
