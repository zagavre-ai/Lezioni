import sys,json,os,re
sys.path.insert(0,'/home/claude/lezioni/psicologia-I-II-lez01/an');sys.path.insert(0,'/home/claude/lezioni/psicologia-I-II-lez01/voci')
import render_an as R, estese_P1 as X
from playwright.sync_api import sync_playwright
ARGT=['Le fibre tessili','Le proprietà delle fibre','Il mercato delle fibre','Le fibre animali e la lana','La fibra di lana']
RFB=[["Fibra tessile: elemento di base, allungato, flessibile e sottile","Naturali (vegetali, animali) · chimiche (artificiali, sintetiche)","Fibre in mischia: uniscono i pregi"],
["Fondamentali per scegliere il materiale","Morfologiche: com'è fatta · chimiche: sostanze chimiche","Fisico-meccaniche: la forza · fisiologiche: corpo e ambiente"],
["Domanda di fibre ×8 dal 1950","Chimiche oltre le naturali · poliestere · Cina","Sporcabilità ≠ pulibilità"],
["Bulbo pilifero o secrezioni ghiandolari","Merino · incrociate · indigene","Tosatura → cernita → lavaggio → asciugatura"],
["80% cheratina · cuticola con squame","Valore: razza, finezza, morbidezza, ondulazione, lunghezza, colore, provenienza","Finezza in micron: da extrafine (fino a 20) a ordinaria (fino a 100)"]]
REP=[('millenovecentocinquanta','1950'),('fino a venti micron','fino a 20 micron'),('fino a cento','fino a 100'),('quattro, sei o otto mesi','4, 6 o 8 mesi'),('otto volte','8 volte'),('cinque argomenti','5 argomenti')]
def cap(s):
    for a,b in REP:s=s.replace(a,b)
    return s
TIT={'GL1':'Le parole chiave','RF1':'Ripasso finale · Parte 1'}
EY={'GL1':'Glossario','RF1':'Ripasso finale'}
def spec(k):
    ph=X.F[k];mp='/home/claude/lezioni/psicologia-I-II-lez01/voci/wav/meta_GL1.json'
    if os.path.exists(mp): m=json.load(open(mp))[k];P=[p+0.8 for p in m['phrases']];dur=m['dur']+0.8+2.5
    else:
        P=[];t=0.8
        for p in ph:P.append(round(t,2));t+=len(p.split())/2.4+0.7
        dur=t+2.5
    sp={'id':k,'title':TIT[k],'ey':EY[k],'P':P,'caps':[cap(p) for p in ph],'dur':round(dur,2)}
    if k=='GL1':sp['gl']=[[a,cap(b)] for a,b in X.GL]
    if k=='RF1':sp['rf']=[[ARGT[i],RFB[i]] for i in range(5)]
    return sp
if __name__=='__main__':
    for k in sys.argv[1:]:
        sp=spec(k)
        if os.environ.get('SHOT'):
            ts=[float(x) for x in os.environ['SHOT'].split(',')]
            with sync_playwright() as p:
                b=p.chromium.launch(args=["--allow-file-access-from-files"]);pg=b.new_page(viewport={'width':1920,'height':1080})
                errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
                pg.goto('file:///home/claude/lezioni/psicologia-I-II-lez01/an/anim.html');pg.evaluate("document.fonts.ready");pg.wait_for_timeout(300);pg.evaluate("a=>init(a)",sp)
                for f in ts:
                    t=sp['P'][int(f)]+0.9 if f>=0 else sp['dur']-1;pg.evaluate("t=>draw(t)",t);pg.screenshot(path=f'{k}_{int(f)}.png')
                print(k,sp['dur'],errs)
        else: R.render(sp,k);print(k,sp['dur'],flush=True)
