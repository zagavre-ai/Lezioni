import json,sys
sys.path.insert(0,'/home/claude/lezioni/psicologia-I-II-lez01')
import gen_moda as G
SP=json.load(open('/home/claude/lezioni/psicologia-I-II-lez01/sync2.json'))['spoken']
G.build(keep=set(SP),path='/home/claude/lezioni/psicologia-I-II-lez01/slides.html')
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1920,'height':1080});pg.goto('file:///home/claude/lezioni/psicologia-I-II-lez01/slides.html');pg.wait_for_timeout(1500)
    SL=pg.evaluate('window.SLIDES');json.dump(SL,open('/home/claude/lezioni/psicologia-I-II-lez01/slides.json','w'));print(len(SL),'slide',[s['ids'] for s in SL])
    print('piene',pg.evaluate("[...document.querySelectorAll('.sheet')].map((s,i)=>s.dataset.over?i+1:0).filter(x=>x)"))
    for i,e in enumerate(pg.query_selector_all('.sheet')): e.screenshot(path='/home/claude/lezioni/psicologia-I-II-lez01/fr/sl%02d.png'%(i+1))
