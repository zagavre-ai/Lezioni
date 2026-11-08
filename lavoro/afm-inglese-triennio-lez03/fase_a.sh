#!/bin/bash
# Lez5 · fase A: slide (frasi dette), copertina del saluto, webcam composta con correzione colore
set -e
cd /home/claude/lezioni/afm-inglese-triennio-lez03
python3 - <<'P'
import json,sys;D='/home/claude/lezioni/afm-inglese-triennio-lez03/';sys.path.insert(0,D);import gen_moda as G
G.build(keep=set(json.load(open(D+'sync2.json'))['spoken']),path=D+'slides.html')
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
  b=p.chromium.launch();pg=b.new_page(viewport={'width':1920,'height':1080});pg.goto('file://'+D+'slides.html');pg.wait_for_timeout(1500)
  SL=pg.evaluate('window.SLIDES');json.dump(SL,open(D+'slides.json','w'));print(len(SL),'slide')
  print('piene',pg.evaluate("[...document.querySelectorAll('.sheet')].map((s,i)=>s.dataset.over?i+1:0).filter(x=>x)"))
P
cp slides.html slides_spoken.html
rm -rf sv && python3 render_slides.py > render_sv.log 2>&1
echo SV_OK
python3 - <<'P'
from playwright.sync_api import sync_playwright
import json
D='/home/claude/lezioni/afm-inglese-triennio-lez03/'
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1920,'height':1080})
    pg.goto('file://'+D+'slides_spoken.html');pg.wait_for_timeout(1200)
    pg.evaluate("""()=>{const s=document.querySelectorAll('.sheet')[0];document.querySelectorAll('.sheet').forEach((x,i)=>x.style.display=i?'none':'');
    s.querySelector('.ey').textContent='Tecnologie dei materiali · Tecnico Sistema Moda';
    s.querySelector('.tt').textContent='Tessitura · parte II';
    s.querySelector('.bd').innerHTML='<div style="background:#fff;border:.08cqw solid #DCE3EE;border-radius:1.1cqw;padding:1.8cqw 2.2cqw;font-size:2cqw;line-height:1.5;font-weight:500;box-shadow:0 .7cqw 2cqw rgba(11,21,48,.07)">Le tecnologie alternative di produzione dei tessuti, i metodi per il <b>controllo qualità</b> e l\\'analisi di laboratorio, le norme di <b>sicurezza</b> e il microclima negli ambienti di lavoro tessili.</div>';
    s.querySelector('.kw').style.display='none';const nk=s.querySelector('.nk');if(nk)nk.style.display='none';s.querySelector('.ft span:last-child').textContent='';}""")
    pg.query_selector_all('.sheet')[0].screenshot(path=D+'sv/s000_cover.png')
P=json.load(open(D+'sv_plan.json'))
L=["file '%ssv/s000_cover.png'"%D,"duration %.3f"%P['starts'][0]]
for f,d in P['plan']: L+=["file '%s'"%f,"duration %.3f"%d]
L.append("file '%s'"%P['plan'][-1][0])
open(D+'sv_concat.txt','w').write('\n'.join(L)+'\n')
P
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 orig/lez1.mp4)
./comp.sh 0 $DUR docente_slide_1080.mp4
echo FASEA_OK
