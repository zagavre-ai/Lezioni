import sys,json,os,re
sys.path.insert(0,'/home/claude/lezioni/afm-inglese-triennio-lez03/an');sys.path.insert(0,'/home/claude/lezioni/afm-inglese-triennio-lez03/voci')
import render_an as R
from playwright.sync_api import sync_playwright
TV=json.load(open('/home/claude/lezioni/afm-inglese-triennio-lez03/voci/testi_voci.json'))
ARGT=['Production and sectors of production','Economies of scale','Quality control and smart manufacturing','Relocation of business operations','Focus: the circular economy']
RFB=[["Goods and services · needs and wants","Land · labour · capital · entrepreneurship","Five sectors linked by the supply chain"],
["More production = lower unit cost","Internal and external economies","Diseconomies of scale: when costs grow"],
["QC: quality and safety before the sale","Industry 4.0: interconnected machines","AI · human-machine interaction · digital twins"],
["Why relocate: resources, labour, rules, markets","Offshoring and outsourcing","Reshoring: back to the country of origin"],
["Reuse · repair · recycle","Circular vs linear economy","Technical cycle and biological cycle"]]
GL=[["Goods","physical products, durable or non-durable","beni"],["Services","non-physical products, actions that help other people","servizi"],
["Added value","the difference between the cost of production and the selling price","valore aggiunto"],["Supply chain","from raw materials to finished goods and services","catena di approvvigionamento"],
["Unit cost","the money spent to produce, store and sell one unit","costo unitario"],["Economies of scale","the benefits of an increase in production","economie di scala"],
["Quality control","checks that products meet standards of quality and safety","controllo qualità"],["Offshoring","moving business operations to other countries","delocalizzazione"],
["Outsourcing","contracting work out to external organisations","esternalizzazione"],["Reshoring","bringing production back to the country of origin","rilocalizzazione"],
["Circular economy","reusing and recycling materials to reduce waste","economia circolare"]]
REP=[('Industry four point zero','Industry 4.0'),('three D printing','3D printing')]
def cap(s):
    for a,b in REP:s=s.replace(a,b)
    return s
TIT={'GL1':'Key words','RF1':'Final review'}
EY={'GL1':'Glossary · Glossario','RF1':'Final review · Ripasso finale'}
def spec(k):
    ph=TV[k];mp=[f for f in [os.path.join('/home/claude/lezioni/afm-inglese-triennio-lez03/voci/wav',x) for x in os.listdir('/home/claude/lezioni/afm-inglese-triennio-lez03/voci/wav') if x.startswith('meta_')] if k in json.load(open(f))];mp=mp[0] if mp else '/nonexistent'
    if os.path.exists(mp): m=json.load(open(mp))[k];P=[p+0.8 for p in m['phrases']];dur=m['dur']+0.8+2.5
    else:
        P=[];t=0.8
        for p in ph:P.append(round(t,2));t+=len(p.split())/2.4+0.7
        dur=t+2.5
    sp={'id':k,'title':TIT[k],'ey':EY[k],'P':P,'caps':[cap(p) for p in ph],'dur':round(dur,2)}
    if k=='GL1':sp['gl']=GL
    if k=='RF1':sp['rf']=[[ARGT[i],RFB[i]] for i in range(5)];sp['rfstep']=1
    return sp
if __name__=='__main__':
    for k in sys.argv[1:]:
        sp=spec(k)
        if os.environ.get('SHOT'):
            ts=[float(x) for x in os.environ['SHOT'].split(',')]
            with sync_playwright() as p:
                b=p.chromium.launch(args=["--allow-file-access-from-files"]);pg=b.new_page(viewport={'width':1920,'height':1080})
                errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
                pg.goto('file:///home/claude/lezioni/afm-inglese-triennio-lez03/an/anim.html');pg.evaluate("document.fonts.ready");pg.wait_for_timeout(300);pg.evaluate("a=>init(a)",sp)
                for f in ts:
                    t=sp['P'][int(f)]+0.9 if f>=0 else sp['dur']-1;pg.evaluate("t=>draw(t)",t);pg.screenshot(path=f'{k}_{int(f)}.png')
                print(k,sp['dur'],errs)
        else: R.render(sp,k);print(k,sp['dur'],flush=True)
