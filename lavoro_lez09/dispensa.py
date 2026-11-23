# Dispensa A4 orizzontale: stesse pagine del video (senza riquadro del prof), testo invisibile selezionabile. uso: python3 dispensa.py PARTE
import sys,os,json,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from lezione import *
from assemble import spiegone_states
from prof import seq_pagine,build,build_riep
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
H=1357
def a4(h):
    h=h.replace('top:981px','top:1258px').replace('top:998px','top:1275px').replace('bottom:24px','bottom:34px')
    h=h.replace('html,body{background:#fff;overflow:hidden;','html,body{')
    return h.replace('width:1920px;height:1080px','width:1920px;height:1357px')
def pages(parte):
    PG=plan_pagine(parte);out=[];args=[1,2,3,4,5] if parte==1 else [6,7,8,9,10]
    maps={2:['M1a','M1b']} if parte==1 else {6:['M2'],8:['M3'],10:['M4']}
    def card_page(kicker,title,texts,pag,bold=False,size=40):
        body=''.join(f'<div class="card" style="font-size:{size}px"><span class=n>{i+1}</span>{G.esc(t)}</div>' for i,t in enumerate(texts))
        inner=f'<div style="position:absolute;left:80px;top:300px;width:1760px;display:flex;flex-direction:column;gap:22px">{body}</div>'
        return hdoc(inner,kicker,title,260,pag,False)
    if parte==2:
        sp=spiegone_states(PG['SPIEGONE'])
        for n,vn in enumerate(['SP2_1','SP2_2','SP2_3','SP2_4','SP2_5'],1):
            sents=[x for x in re.split(r'(?<=\.)\s+',cifre(TESTI[vn]))]
            out.append((PG['SPIEGONE']+n-1,card_page('RIPASSO · PRIMA PARTE',ARGT[n],sents,PG['SPIEGONE']+n-1,size=36)))
    out.append((PG['COVERV'],cover_html(None,False,parte,PG['COVERV'])))
    out.append((PG['DP'],dp_states(f'DP{parte}',parte,PG['DP'])[0]['html']))
    for n in args:
        d=build(n,0,'x');seq,pe=seq_pagine(d,PG[f'A{n}']);seen=set()
        for t,kind,ks,on,fn,tb,pg in seq:
            if pg in seen or kind=='focus':continue
            seen.add(pg)
            if kind=='img':
                h=G.doc(f'<img class="img" src="file:///home/user/Lezioni/w/imgs/{fn}" style="left:80px;top:290px;height:900px;max-width:1700px">',f'ARGOMENTO {n}',IMMCAP.get(fn,''),259,pg,False,None)
            else:
                inner,bar=G.pagina(d['title'],[d['cards'][k] for k in ks],None,None)
                inner=inner.replace('width:1290px','width:1760px');h=G.doc(inner,f'ARGOMENTO {n}',d['title'],bar,pg,False,None)
            out.append((pg,h))
        vs=[APR.get(f'AP{n}_{i}',f'AP{n}_{i}') for i in (1,2,3,4)]
        out.append((PG[f'AP{n}'],card_page('APPROFONDIMENTO',ARGT[n],[cifre(TESTI[v]) for v in vs],PG[f'AP{n}'],size=38)))
        for mk in maps.get(n,[]):
            m=MAPPE[mk];out.append((PG[f'MAP_{mk}'],map_html(m,[x[0] for x in m['nodi']],None,{(a,b) for a,b,_ in m['archi']},pag=PG[f'MAP_{mk}'])))
        vp=[f'PS{n}_{i}' for i in range(1,7) if f'PS{n}_{i}' in TESTI]
        out.append((PG[f'PS{n}'],card_page('RIPASSO',ARGT[n],[cifre(TESTI[v]) for v in vp],PG[f'PS{n}'],size=38)))
    if parte==2:
        d=build_riep();seq,pe=seq_pagine(d,PG['A11']);seen=set()
        for t,kind,ks,on,fn,tb,pg in seq:
            if pg in seen or kind=='focus':continue
            seen.add(pg);inner,bar=G.pagina(d['title'],[d['cards'][k] for k in ks],None,None);inner=inner.replace('width:1290px','width:1760px')
            out.append((pg,G.doc(inner,'RIEPILOGO',d['title'],bar,pg,False,None)))
    items=[(a,b) for a,b in [(x.split(': ',1)[0],cifre(x.split(': ',1)[1])) for x in [y.strip() for y in re.split(r'(?<=\.)\s+',TESTI[f'GL{parte}'])][1:]]]
    out.append((PG['GL'],card_page('GLOSSARIO','Le parole da ricordare',[f'{a}: {b}' for a,b in items],PG['GL'])))
    sents=[cifre(x.strip()) for x in re.split(r'(?<=\.)\s+',TESTI[f'RF{parte}'])][1:]
    out.append((PG['RF'],card_page('RIPASSO FINALE',f'Parte {parte}',sents,PG['RF'])))
    out.sort(key=lambda x:x[0]);return out
def main(parte):
    P=pages(parte);D=W+f'/disp{parte}';os.makedirs(D,exist_ok=True)
    pdfmetrics.registerFont(TTFont('Fig','/root/.fonts/Figtree-Regular.ttf'))
    pdf=canvas.Canvas(W+f'/Storia_Lez9_Parte{parte}_dispensa.pdf',pagesize=(841.92,594.96));pdf.setTitle(f'Storia V · {TIT_ESATTO} · Parte {parte}')
    with G.R() as r:
        r.pg.set_viewport_size({'width':1920,'height':H})
        for pg,h in P:
            h=a4(h);r.set(h);p=f'{D}/p{pg:03d}.jpg';r.pg.screenshot(path=p,type='jpeg',quality=92)
            txt=r.pg.evaluate("document.body.innerText")
            pdf.drawImage(p,0,0,841.92,594.96)
            t=pdf.beginText(20,570);t.setFont('Fig',8);t.setTextRenderMode(3)
            for line in txt.split('\n'):
                if line.strip():t.textLine(line.strip())
            pdf.drawText(t);pdf.showPage()
    pdf.save();print('pagine',len(P))
if __name__=='__main__':main(int(sys.argv[1]))
