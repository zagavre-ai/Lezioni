#!/bin/bash
# Parte 1 v3 (voci nostre, schemi estesi, glossario, ripasso finale) + primi 15 minuti della Parte 2 (spiegone)
set -e
cd /home/claude/lezioni/psicologia-I-II-lez01
SC=1 python3 po_moda.py S1 S2 S3 S4 S5 S6; echo PO_OK
( cd an && python3 render_an.py 0 1 2 3 && python3 render_rip.py && python3 render_extra.py GL1 RF1 ); echo AN_OK
python3 run_dark2.py R1 R2 R3 R4 R5 R6 FIN1; echo DK_OK
# slide: la sincronia della Parte 2 è stata corretta → rifaccio le immagini e la parte 2040–2830 s
rm -rf sv && python3 render_slides.py > render_sv.log 2>&1
python3 - <<'P'
from playwright.sync_api import sync_playwright
import json
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1920,'height':1080})
    for name,tt,txt in [('s000_cover','Preparazione · parte I','Parleremo di classificazione generale delle fibre tessili e approfondiremo le caratteristiche, l’origine e i processi di lavorazione delle fibre naturali di origine animale: <b>lana</b> e <b>seta</b>.'),
                        ('s000_cover_P2','Preparazione · parte I — Parte 2','In questa seconda parte parleremo dei <b>trattamenti</b>, delle <b>proprietà</b> e della <b>cura della lana</b>, delle <b>lane speciali</b> e della <b>seta</b>.')]:
        pg.goto('file:///home/claude/lezioni/psicologia-I-II-lez01/slides_spoken.html');pg.wait_for_timeout(1200)
        pg.evaluate("""a=>{const s=document.querySelectorAll('.sheet')[0];document.querySelectorAll('.sheet').forEach((x,i)=>x.style.display=i?'none':'');
        s.querySelector('.ey').textContent='Tecnologie dei materiali · Tecnico Sistema Moda';s.querySelector('.tt').textContent=a.tt;
        s.querySelector('.bd').innerHTML='<div style="background:#fff;border:.08cqw solid #DCE3EE;border-radius:1.1cqw;padding:1.8cqw 2.2cqw;font-size:2cqw;line-height:1.5;font-weight:500;box-shadow:0 .7cqw 2cqw rgba(11,21,48,.07)">'+a.txt+'</div>';
        s.querySelector('.kw').style.display='none';const nk=s.querySelector('.nk');if(nk)nk.style.display='none';s.querySelector('.ft span:last-child').textContent='';}""",{'tt':tt,'txt':txt})
        pg.query_selector_all('.sheet')[0].screenshot(path=f'/home/claude/lezioni/psicologia-I-II-lez01/sv/{name}.png')
P=json.load(open('/home/claude/lezioni/psicologia-I-II-lez01/sv_plan.json'))
L=["file '/home/claude/lezioni/psicologia-I-II-lez01/sv/s000_cover.png'","duration %.3f"%P['starts'][0]]
for f,d in P['plan']: L+=["file '%s'"%f,"duration %.3f"%d]
L.append("file '%s'"%P['plan'][-1][0])
open('/home/claude/lezioni/psicologia-I-II-lez01/sv_concat.txt','w').write('\n'.join(L)+'\n')
P
./comp.sh 2040 790 docente_slide_P2.mp4; echo COMP2_OK
python3 make_sting.py; echo STING_OK
cd w2; rm -f INTRO1.mkv R[1-6].mkv S[1-6].mkv AN[1-4].mkv GL1.mkv RF1.mkv FIN1.mkv IN2.mkv RIP.mkv D*.mkv b_*.mkv x_*.mkv; cd ..
rm -f Tecnologie_Lez1_Parte1_VIDEO.mp4
python3 asm_moda2.py 1; echo MONT1_OK
rm -rf consegna/Tecnologie_Lez1_Parte1
python3 build_player_moda.py 1
python3 /home/claude/lezioni/psicologia-I-II-lez01/test_player.py 1; echo PLAYER1_OK
python3 make_scorm.py 1 hd; echo SCORM_OK
F=Tecnologie_Lez1_Parte1_VIDEO.mp4; Dd=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $F); L=$(python3 -c "print($Dd/3)")
mkdir -p anteprima; rm -f anteprima/*.mp4
for i in 0 1 2; do S=$(python3 -c "print($L*$i)"); ffmpeg -v error -ss $S -t $L -i $F -vf scale=1280:720 -c:v libx264 -preset veryfast -crf 32 -c:a aac -b:a 64k -ac 1 -movflags +faststart -y anteprima/Tecnologie_Lez1_Parte1_v3_$((i+1))di3.mp4; done
echo PREV1_OK
VIDF=docente_slide_P2.mp4 VOFF=2040 PREV15=1 python3 asm_moda2.py 2; echo MONT2_OK
ffmpeg -v error -i Tecnologie_Lez1_Parte2_VIDEO_prime15min.mp4 -vf scale=1280:720 -c:v libx264 -preset veryfast -crf 32 -c:a aac -b:a 64k -ac 1 -movflags +faststart -y anteprima/Tecnologie_Lez1_Parte2_primi15min.mp4
ls -la anteprima; echo TUTTO_OK
