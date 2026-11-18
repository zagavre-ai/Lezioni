#!/bin/bash
# prepara_chat.sh NN — Letteratura V: sostituisce titoli, pillole, quiz e riepilogo con le schede di Spagnolo (programma originale)
# senza cambiare durata né tempi. Esegui dalla radice del repository (zagavre-ai/Lezioni). Serve: ffmpeg, python3, playwright+chromium, tesseract.
set -e
N=$1; M=$((10#$N)); BR=revisione-letteratura-V-lez$N; QUI=$(cd "$(dirname "$0")" && pwd); W=$HOME/spagnolo_lez$N; mkdir -p $W; cd $W
git -C "$QUI/../../.." fetch -q origin "+$BR:refs/remotes/origin/$BR" "+voci-letteratura-V-lez$N:refs/remotes/origin/voci-letteratura-V-lez$N" || true
R="git -C $QUI/../../.."
if [ ! -f orig.mp4 ]; then : > orig.mp4; for p in $($R ls-tree -r --name-only origin/$BR | grep "^$BR/.*1080p.mp4.parte_" | sort); do $R show "origin/$BR:$p" >> orig.mp4; done; fi
SHA=$($R show "origin/$BR:$($R ls-tree -r --name-only origin/$BR | grep "^$BR/.*1080p.mp4.sha256$" | head -1)" | cut -c1-64)
[ "$(sha256sum orig.mp4 | cut -c1-64)" = "$SHA" ] || { echo "SHA DIVERSO: riscarica"; rm -f orig.mp4; exit 1; }
$R show "origin/$BR:$($R ls-tree -r --name-only origin/$BR | grep "^$BR/.*timeline[^/]*json$" | head -1)" > tl.json
$R show "origin/$BR:$($R ls-tree -r --name-only origin/$BR | grep "^$BR/.*scheda_pubblicazione[^/]*json$" | head -1)" > sc.json
$R show "origin/voci-letteratura-V-lez$N:scambio/letteratura-V-lez$N/testi_voci.json" > tv.json 2>/dev/null || echo '{}' > tv.json
python3 $QUI/schede_lezione.py $N orig.mp4 tl.json tv.json sc.json schede | tail -3
rm -rf seg_tmp && python3 $QUI/fix_quiz.py orig.mp4 fix.mp4 schede/finestre.json | tail -2
a=$(ffprobe -v error -select_streams v -show_entries packet=pts_time -of csv=p=0 orig.mp4 | tr -d ',' | sort -n | md5sum); b=$(ffprobe -v error -select_streams v -show_entries packet=pts_time -of csv=p=0 fix.mp4 | tr -d ',' | sort -n | md5sum)
[ "$a" = "$b" ] || { echo "TEMPI DIVERSI: non consegnare"; exit 1; }
python3 - <<'PY'
import json,subprocess
W=json.load(open('schede/finestre.json')); ims=[]
for k,w in enumerate(W):
    t=w['a']+min(2.2,(w['b']-w['a'])*0.6); o=f'f_{k:02d}.png'
    subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{t:.2f}','-i','fix.mp4','-frames:v','1','-vf',f"scale=384:-1,drawtext=text='{w['pezzo']} {t:.1f}':x=4:y=4:fontsize=16:fontcolor=red",o]); ims.append(o)
n=len(ims); rows=(n+5)//6
subprocess.run(['ffmpeg','-v','error','-y',*sum([['-i',x] for x in ims],[]),'-filter_complex',''.join(f'[{i}]' for i in range(n))+f'concat=n={n}:v=1:a=0,tile=6x{rows}:padding=3:color=gray','-frames:v','1','foglio.png'])
PY
rm -f f_*.png; echo "PRONTA $N: guarda $W/foglio.png, poi consegna_chat.sh $N"
