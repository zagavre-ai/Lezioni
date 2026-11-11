#!/bin/bash
# $1 = inizio, $2 = durata, $3 = uscita (video senza audio). Webcam rettangolare 413x232 (ritaglio 242x135 dall'originale 1092x614)
SS=$1; DUR=$2; OUT=$3
ffmpeg -v error -y -threads 2 -f concat -safe 0 -i sv_concat.txt -ss $SS -i orig/lez1.mp4 -loop 1 -i cam_mask.png -loop 1 -i cam_ring.png \
 -filter_complex "[0:v]fps=30,trim=start=$SS:duration=$DUR,setpts=PTS-STARTPTS,format=yuv420p[s];\
[1:v]fps=30,trim=duration=$DUR,setpts=PTS-STARTPTS,crop=242:135:849:345,normalize=blackpt=black:whitept=white:smoothing=30:independence=0.6:strength=0.7,scale=413:232:flags=lanczos,hqdn3d=2:2:3:3,unsharp=5:5:0.8,eq=contrast=1.05:saturation=1.1:gamma=1.04,format=rgba[c];\
[2:v]format=gray,trim=duration=$DUR[m];[c][m]alphamerge[cm];[s][cm]overlay=1428:149:shortest=1[a];[a][3:v]overlay=1428:149:shortest=1,format=yuv420p[v]" \
 -map "[v]" -t $DUR -c:v libx264 -preset veryfast -crf 20 -r 30 $OUT
