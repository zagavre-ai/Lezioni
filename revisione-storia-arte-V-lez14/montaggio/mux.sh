#!/bin/bash
# normalizza l'audio (loudnorm a due passate) e lo unisce al video gia' codificato (video copiato, non ricodificato)
cd /tmp/w/build
M=$(ffmpeg -hide_banner -nostats -i audio.wav -af loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json -f null - 2>&1)
get(){ echo "$M" | grep "\"$1\"" | sed 's/.*: "\(.*\)".*/\1/'; }
ffmpeg -v error -y -i audio.wav -af "loudnorm=I=-16:TP=-1.5:LRA=11:measured_I=$(get input_i):measured_TP=$(get input_tp):measured_LRA=$(get input_lra):measured_thresh=$(get input_thresh):offset=$(get target_offset):linear=true,alimiter=limit=0.89:level=disabled" -ar 48000 -c:a pcm_s16le audio_ln.wav
ffmpeg -v error -y -i video_solo.mp4 -i audio_ln.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -ar 48000 -ac 2 -movflags +faststart "$1"
