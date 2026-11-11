set -e
cd /home/claude/lezioni/psicologia-I-II-lez01
rm -rf sv; python3 render_slides.py > render_sv.log 2>&1
python3 - <<'P'
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1920,'height':1080})
    pg.goto('file:///home/claude/lezioni/psicologia-I-II-lez01/slides_spoken.html');pg.wait_for_timeout(800)
    pg.evaluate("""()=>{const s=document.querySelectorAll('.sheet')[0];document.querySelectorAll('.sheet').forEach((x,i)=>x.style.display=i?'none':'');
    s.querySelector('.ey').textContent='Tecnologie dei materiali · Tecnico Sistema Moda';
    s.querySelector('.tt').textContent='Preparazione · parte I';
    s.querySelector('.bd').innerHTML='<p style="font-size:2cqw;line-height:1.45">Parleremo di classificazione generale delle fibre tessili e approfondiremo le caratteristiche, l\\'origine e i processi di lavorazione delle fibre naturali di origine animale: <b>lana</b> e <b>seta</b>.</p>';
    s.querySelector('.kw').style.display='none';s.querySelector('.ft span:last-child').textContent='';}""")
    pg.query_selector_all('.sheet')[0].screenshot(path='/home/claude/lezioni/psicologia-I-II-lez01/sv/s000_cover.png')
import json
P=json.load(open('/home/claude/lezioni/psicologia-I-II-lez01/sv_plan.json'))
L=["file '/home/claude/lezioni/psicologia-I-II-lez01/sv/s000_cover.png'","duration %.3f"%P['starts'][0]]
for f,d in P['plan']: L+=["file '%s'"%f,"duration %.3f"%d]
L.append("file '%s'"%P['plan'][-1][0])
open('/home/claude/lezioni/psicologia-I-II-lez01/sv_concat.txt','w').write('\n'.join(L)+'\n')
P
true
./comp.sh 0 4468 docente_slide_1080.mp4
echo FATTO
