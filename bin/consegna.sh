#!/bin/bash
# uso: consegna.sh NN  (dopo codifica e controlli OK)
set -e
NN=$1; N=$((10#$NN)); T=letteratura-V-lez$NN; L=/home/claude/w/l$NN; F=$L/fin; V=Letteratura_Lez${N}_Parte1_1080p.mp4
cd $L
TIT=$(python3 -c "import sys;sys.path.insert(0,'/home/claude/w/bin');from conf import CONF;print(CONF['$NN']['titolo'])")
python3 /home/claude/lezioni/kit/tools/scheda_da_timeline.py $F/$V timeline.json voci/quiz_argomenti.json "$TIT · Parte 1" $F/scheda_pubblicazione.json "Letteratura italiana (V)" >/dev/null
python3 /home/claude/lezioni/kit/tools/testo_youtube.py $F/scheda_pubblicazione.json "Letteratura italiana (V anno)|Letteratura" "Prof. Giorgio Mazzotti" "$TIT" 1 timeline.json > $F/testo_youtube.txt
W=/home/claude/w/wt_c$NN; cd /home/claude/lezioni; git worktree remove --force $W 2>/dev/null || true
git worktree add -q --detach $W; cd $W; git checkout -q --orphan consegna-$T; git rm -rfq . ; D=consegna-$T; mkdir -p $D
split -b 90M -d -a 2 $F/$V $D/$V.parte_
(cd $F && sha256sum $V) > $D/$V.sha256
cp $F/Letteratura_Lez${N}_Parte1.vtt $F/scheda_pubblicazione.json $F/testo_youtube.txt $L/voci/quiz_argomenti.json $L/out/* $D/
cp $L/timeline.json $D/timeline.json
git add -A; git commit -qm "Consegna $T Parte 1 (chat D2)"; timeout 300 git push -q --force origin HEAD:refs/heads/consegna-$T 2>&1 | grep -iv 'moved\|location\|^remote: *$\|pull request\|github.com\|acknowledg\|negotiation' || true
cd /home/claude/lezioni; git worktree remove --force $W
git ls-remote origin refs/heads/consegna-$T
