#!/bin/bash
# $1 = inizio, $2 = durata, $3 = uscita (video senza audio). Webcam a tutto schermo → riquadro 4:3 con angoli tondi
SS=$1; DUR=$2; OUT=$3
ffmpeg -v error -y -f concat -safe 0 -i sv_concat.txt -ss $SS -i orig/lez1.mp4 -loop 1 -i cam_mask.png \
 -filter_complex "[0:v]fps=30,trim=start=$SS:duration=$DUR,setpts=PTS-STARTPTS,format=yuv420p[s];\
[1:v]fps=30,trim=duration=$DUR,setpts=PTS-STARTPTS,crop=1200:900:400:30,scale=413:310:flags=lanczos,normalize=blackpt=black:whitept=white:smoothing=30:independence=0.6:strength=0.5,hqdn3d=1.5:1.5:3:3,unsharp=5:5:0.5,eq=contrast=1.05:saturation=1.1:gamma=1.04,format=rgba[c];\
[2:v]format=gray,trim=duration=$DUR[m];[c][m]alphamerge[cm];[s][cm]overlay=1428:149:shortest=1,format=yuv420p[v]" \
 -map "[v]" -t $DUR -c:v libx264 -preset veryfast -crf 18 -r 30 -an $OUT
