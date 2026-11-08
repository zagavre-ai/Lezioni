#!/bin/bash
# Parte 1 v3 · fase A: slide nuova impaginazione (A+B) + webcam con correzione colore
set -e
cd /home/claude/lezioni/afm-inglese-triennio-lez03
python3 - <<'P'
import json,sys;sys.path.insert(0,'/home/claude/lezioni/afm-inglese-triennio-lez03');import gen_moda as G
G.build(keep=set(json.load(open('/home/claude/lezioni/afm-inglese-triennio-lez03/sync2.json'))['spoken']),path='/home/claude/lezioni/afm-inglese-triennio-lez03/slides.html')
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
  b=p.chromium.launch();pg=b.new_page(viewport={'width':1920,'height':1080});pg.goto('file:///home/claude/lezioni/afm-inglese-triennio-lez03/slides.html');pg.wait_for_timeout(1500)
  SL=pg.evaluate('window.SLIDES');json.dump(SL,open('/home/claude/lezioni/afm-inglese-triennio-lez03/slides.json','w'));print(len(SL),'slide')
  print('piene',pg.evaluate("[...document.querySelectorAll('.sheet')].map((s,i)=>s.dataset.over?i+1:0).filter(x=>x)"))
P
cp slides.html slides_spoken.html
rm -rf sv && python3 render_slides.py > render_sv.log 2>&1
echo SV_OK
python3 - <<'P'
from playwright.sync_api import sync_playwright
import json
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1920,'height':1080})
    pg.goto('file:///home/claude/lezioni/afm-inglese-triennio-lez03/slides_spoken.html');pg.wait_for_timeout(1200)
    pg.evaluate("""()=>{const s=document.querySelectorAll('.sheet')[0];document.querySelectorAll('.sheet').forEach((x,i)=>x.style.display=i?'none':'');
    s.querySelector('.ey').textContent='Tecnologie dei materiali · Tecnico Sistema Moda';
    s.querySelector('.tt').textContent='Preparazione · parte I';
    s.querySelector('.bd').innerHTML='<div style="background:#fff;border:.08cqw solid #DCE3EE;border-radius:1.1cqw;padding:1.8cqw 2.2cqw;font-size:2cqw;line-height:1.5;font-weight:500;box-shadow:0 .7cqw 2cqw rgba(11,21,48,.07)">Parleremo di classificazione generale delle fibre tessili e approfondiremo le caratteristiche, l\\'origine e i processi di lavorazione delle fibre naturali di origine animale: <b>lana</b> e <b>seta</b>.</div>';
    s.querySelector('.kw').style.display='none';const nk=s.querySelector('.nk');if(nk)nk.style.display='none';s.querySelector('.ft span:last-child').textContent='';}""")
    pg.query_selector_all('.sheet')[0].screenshot(path='/home/claude/lezioni/afm-inglese-triennio-lez03/sv/s000_cover.png')
P=json.load(open('/home/claude/lezioni/afm-inglese-triennio-lez03/sv_plan.json'))
L=["file '/home/claude/lezioni/afm-inglese-triennio-lez03/sv/s000_cover.png'","duration %.3f"%P['starts'][0]]
for f,d in P['plan']: L+=["file '%s'"%f,"duration %.3f"%d]
L.append("file '%s'"%P['plan'][-1][0])
open('/home/claude/lezioni/afm-inglese-triennio-lez03/sv_concat.txt','w').write('\n'.join(L)+'\n')
P
./comp.sh 0 2110 docente_slide_1080.mp4
echo COMP_OK
cd w2 && rm -f D*.mkv b_*.mkv x_*.mkv INTRO1.mkv S[1-5].mkv FIN1.mkv GL1.mkv RF1.mkv; cd ..
echo FASEA_OK
