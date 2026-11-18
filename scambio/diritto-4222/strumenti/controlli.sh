#!/bin/bash
# controlli.sh OUTDIR — sha256, LUFS/picco, freezedetect e fotogrammi per ogni Parte
cd $1
for p in 1 2; do f=Diritto_4222_Parte${p}_1080p.mp4
 sha256sum $f > $f.sha256
 ffmpeg -nostats -i $f -af ebur128=peak=true -f null - 2>&1 | grep -A14 "Summary" | grep -E "^ +I:|Peak:" | tr -s ' ' | tr '\n' ' ' > lufs$p.txt
 ffmpeg -nostats -i $f -vf freezedetect=n=-55dB:d=0.9 -an -f null - 2>&1 | grep -E "freeze_(start|duration)" | sed 's/.*: //' | paste - - > freeze$p.txt
 ffprobe -v error -count_packets -select_streams v:0 -show_entries stream=nb_read_packets:format=duration,size -of csv=p=0 $f > misura$p.txt
done
touch controlli.ok
