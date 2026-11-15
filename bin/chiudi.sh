#!/bin/bash
# uso: chiudi.sh NN  — codifica finale, sottotitoli, controlli, scheda, stato PRONTA, consegna (dopo ripresa.sh + lista)
set -e
NN=$1; N=$((10#$NN)); T=letteratura-V-lez$NN; L=/home/claude/w/l$NN; F=$L/fin; V=Letteratura_Lez${N}_Parte1_1080p.mp4
export PYTHONPATH=/home/user/Lezioni/kit/tools; K=/home/user/Lezioni/kit/tools; S=/tmp/claude-0/-home-user-Lezioni/aa838b16-be86-588f-84fd-78776ad6250d/scratchpad
mkdir -p $F; cd $L
python3 /home/claude/w/bin/carte.py $NN lista
[ -f $F/$V ] || python3 $K/finale_a_pezzi.py $L/lista.txt $F/$V
python3 /home/claude/w/bin/sub2.py $F/$V timeline.json $F/Letteratura_Lez${N}_Parte1.vtt $L/fix.json
python3 $K/controllo_jingle.py $F/$V timeline.json | tee $F/controllo_jingle.txt
python3 $K/controllo_finale.py $F/$V timeline.json $F/Letteratura_Lez${N}_Parte1.vtt | tee $F/controllo_finale.txt
cp $L/out/Letteratura_Lez${N}_dispensa_A4_mappe.pdf $L/out/Dispensa_Letteratura_Lez${N}.pdf
python3 /home/claude/w/bin/compiti.py $NN
echo FATTO
