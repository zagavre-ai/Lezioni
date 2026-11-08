#!/bin/bash
# Slide sincronizzate + riquadro della docente (orig/lez1.mp4 già ritagliato e condensato) nel box in alto a destra.
# $1 = inizio, $2 = durata, $3 = uscita (video senza audio, 1920x1080)
cd /home/claude/lezioni/afm-inglese-triennio-lez03
SS=$1; DUR=$2; OUT=$3
ffmpeg -v error -y -f concat -safe 0 -i sv_concat.txt -ss $SS -i orig/lez1.mp4 -loop 1 -i doc_mask.png \
 -filter_complex "[0:v]fps=30,trim=start=$SS:duration=$DUR,setpts=PTS-STARTPTS,format=yuv420p[s];\
[1:v]fps=30,trim=duration=$DUR,setpts=PTS-STARTPTS,scale=412:310:flags=lanczos,eq=contrast=1.04:saturation=1.06,unsharp=5:5:0.5,format=rgba[c];\
[2:v]format=gray,trim=duration=$DUR[m];[c][m]alphamerge[cm];[s][cm]overlay=1429:149:shortest=1,format=yuv420p[v]" \
 -map "[v]" -t $DUR -c:v libx264 -preset veryfast -crf 18 -r 30 $OUT
