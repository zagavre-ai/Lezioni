#!/bin/bash
set -e
D=/home/claude/lezioni/afm-inglese-triennio-lez01
cd $D
[ -f sv/.ok ] || { rm -rf sv && python3 render_slides.py > render_sv.log 2>&1 && touch sv/.ok; }
python3 - <<'P'
from playwright.sync_api import sync_playwright
import json
D='/home/claude/lezioni/afm-inglese-triennio-lez01/'
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1920,'height':1080})
    pg.goto('file://'+D+'slides_spoken.html');pg.wait_for_timeout(1200)
    pg.evaluate("""()=>{const s=document.querySelectorAll('.sheet')[0];document.querySelectorAll('.sheet').forEach((x,i)=>x.style.display=i?'none':'');
    s.querySelector('.ey').textContent='Inglese · Amministrazione, Finanza e Marketing';
    s.querySelector('.tt').textContent='Global Factors';
    s.querySelector('.bd').innerHTML='<div style="background:#fff;border:.08cqw solid #DCE3EE;border-radius:1.1cqw;padding:1.8cqw 2.2cqw;font-size:2cqw;line-height:1.5;font-weight:500;box-shadow:0 .7cqw 2cqw rgba(11,21,48,.07)">Five external factors that influence business:<br><b>Globalisation</b> · <b>Technological advancement</b> · <b>Diversity and inclusion</b> · <b>World instability</b> · <b>Environmental concerns</b><div style="margin-top:.6cqw;font-size:1.4cqw;color:#5A6B85">Cinque fattori esterni che influenzano il mondo del lavoro e dell’economia.</div></div>';
    s.querySelector('.kw').style.display='none';const nk=s.querySelector('.nk');if(nk)nk.style.display='none';s.querySelector('.ft span:last-child').textContent='';}""")
    pg.query_selector_all('.sheet')[0].screenshot(path=D+'sv/s000_cover.png')
P=json.load(open(D+'sv_plan.json'))
L=["file '%ssv/s000_cover.png'"%D,"duration %.3f"%P['starts'][0]]
for f,d in P['plan']: L+=["file '%s'"%f,"duration %.3f"%d]
L.append("file '%s'"%P['plan'][-1][0])
open(D+'sv_concat.txt','w').write('\n'.join(L)+'\n')
P
touch .fase_a_slide
