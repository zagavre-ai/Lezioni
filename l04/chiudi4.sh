#!/bin/bash
# Lezione 4 v2: voci Kore arrivate -> rifà AN, montaggio unico, sottotitoli, controlli, consegna sullo stesso ramo
set -e
S=/tmp/claude-0/-home-user-Lezioni/aa838b16-be86-588f-84fd-78776ad6250d/scratchpad; Z=$S/lez4; L=$S/l04/consegna-letteratura-V-lez04
export PYTHONPATH=/home/user/Lezioni/kit/tools AOFF=0.082 CARDS=$Z/cards ANV=3
cd /home/user/Lezioni && git fetch -q origin voci-letteratura-V-lez04
mkdir -p /tmp/ripresa_04 $Z/vox && git archive origin/voci-letteratura-V-lez04 scambio/letteratura-V-lez04/vox | tar -x -C /tmp/ripresa_04
cp /tmp/ripresa_04/scambio/letteratura-V-lez04/vox/AN*.wav $Z/vox/
cd $Z && python3 render.py spec.py vox out
python3 assemble.py $L/L4.mp4 $L/timeline.json $L/x.vtt spec.py out wlavoro outfinale
python3 post.py
python3 /home/user/Lezioni/kit/tools/controllo_jingle.py outfinale/Letteratura_Lez4_Parte1_1080p.mp4 outfinale/timeline.json | tee outfinale/controllo_jingle.txt
python3 /home/user/Lezioni/kit/tools/controllo_finale.py outfinale/Letteratura_Lez4_Parte1_1080p.mp4 outfinale/timeline.json outfinale/Letteratura_Lez4_Parte1.vtt | tee outfinale/controllo_finale.txt
echo FATTO
