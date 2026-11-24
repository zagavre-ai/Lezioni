#!/bin/bash
# uso: controlli.sh N   (N = numero Parte)  -> consegna/controlli_ParteN.txt
N=$1;W=/home/claude/w;V=$W/out/Storia_Lez21_Parte${N}_1080p.mp4;T=$W/timeline_Parte${N}.json;S=$W/consegna/Storia_Lez21_Parte${N}.vtt
O=$W/consegna/controlli_Parte${N}.txt;mkdir -p $W/consegna;: > $O
echo "== controllo_finale" >> $O
python3 /home/user/Lezioni/kit/tools/controllo_finale.py $V $T $S >> $O 2>&1
echo "== controllo_jingle" >> $O
python3 /home/user/Lezioni/kit/tools/controllo_jingle.py $V $T >> $O 2>&1
echo "== timbro (acuti >4kHz rispetto a >100Hz, dB)" >> $O
python3 $W/code/timbro.py $V >> $O 2>&1
echo "== controllo_severo" >> $O
OMP_THREAD_LIMIT=1 python3 $W/controllo_severo.py $V "Il mondo dal 2001 ad oggi" 10 >> $O 2>&1
echo FATTO >> $O
