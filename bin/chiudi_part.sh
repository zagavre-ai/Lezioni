#!/bin/bash
# uso: chiudi_part.sh NN PARTE   (es. 14 1 / 14b 2)
set -e
NN=$1; P=$2; N=14; L=/home/claude/w/l$NN; F=$L/fin; V=Letteratura_Lez${N}_Parte${P}_1080p.mp4
export PYTHONPATH=/home/user/Lezioni/kit/tools; K=/home/user/Lezioni/kit/tools
mkdir -p $F; cd $L
python3 /home/claude/w/bin/carte.py $NN lista
[ -f $F/$V ] || python3 $K/finale_a_pezzi.py $L/lista.txt $F/$V
python3 /home/claude/w/bin/sub2.py $F/$V timeline.json $F/Letteratura_Lez${N}_Parte${P}.vtt $L/fix.json
python3 /home/claude/w/bin/snapvtt.py $F/$V $F/Letteratura_Lez${N}_Parte${P}.vtt
python3 $K/controllo_jingle.py $F/$V timeline.json | tee $F/controllo_jingle.txt
python3 $K/controllo_finale.py $F/$V timeline.json $F/Letteratura_Lez${N}_Parte${P}.vtt | tee $F/controllo_finale.txt
echo FATTO
