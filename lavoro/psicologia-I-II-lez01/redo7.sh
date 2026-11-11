#!/bin/bash
# Parte 1 con schemi estesi, glossario e ripasso finale (dopo proc_aggiunte.sh)
set -e
cd /home/claude/lezioni/psicologia-I-II-lez01
SC=1 python3 po_moda.py S1 S2 S3 S4 S5; echo PO_OK
python3 run_dark2.py FIN1 FIN2; echo DK_OK
( cd an && python3 render_extra.py GL1 RF1 ); echo AN_OK
cd w2; rm -f S[1-5].mkv b_*.mkv x_*.mkv FIN1.mkv GL1.mkv RF1.mkv; cd ..
rm -f Tecnologie_Lez1_Parte1_VIDEO.mp4
python3 asm_moda2.py 1; echo MONT1_OK
rm -rf consegna/Tecnologie_Lez1_Parte1
python3 build_player_moda.py 1
python3 /home/claude/lezioni/psicologia-I-II-lez01/test_player.py 1; echo PLAYER1_OK
F=Tecnologie_Lez1_Parte1_VIDEO.mp4; Dd=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $F); L=$(python3 -c "print($Dd/3)")
rm -f anteprima/*.mp4
for i in 0 1 2; do S=$(python3 -c "print($L*$i)"); ffmpeg -v error -ss $S -t $L -i $F -vf scale=1280:720 -c:v libx264 -preset veryfast -crf 32 -c:a aac -b:a 64k -ac 1 -movflags +faststart -y anteprima/Tecnologie_Lez1_Parte1_v3_$((i+1))di3.mp4; done
ls -la anteprima; echo PREV1_OK
