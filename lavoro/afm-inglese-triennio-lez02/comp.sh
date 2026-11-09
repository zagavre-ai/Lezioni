#!/bin/bash
# slide (sv_concat.txt) + docente nel riquadro in alto a destra (docente_c.mkv, già 412x310 con correzione colore)
cd /home/claude/lezioni/afm-inglese-triennio-lez02
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 /home/claude/ing2/docente_c.mkv)
ffmpeg -v error -y -f concat -safe 0 -i sv_concat.txt -i /home/claude/ing2/docente_c.mkv -loop 1 -i /home/claude/ing2/cam_mask.png \
 -filter_complex "[0:v]fps=30,format=yuv420p,trim=duration=$DUR,setpts=PTS-STARTPTS[s];[1:v]fps=30,format=rgba[c];[2:v]format=gray,trim=duration=$DUR[m];[c][m]alphamerge[cm];[s][cm]overlay=1429:149:shortest=1,format=yuv420p[v]" \
 -map "[v]" -t $DUR -c:v libx264 -preset veryfast -crf 18 -r 30 docente_slide_1080.mp4 && touch comp.ok
