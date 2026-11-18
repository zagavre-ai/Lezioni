#!/bin/bash
# normalizza una voce a -16 LUFS, 48k stereo
f=$1; b=$(basename $f .wav)
[ -f /tmp/w/vn/$b.wav ] && exit 0
ffmpeg -v error -y -i $f -af "loudnorm=I=-16:TP=-2:LRA=11,aresample=48000" -ac 2 -c:a pcm_s16le /tmp/w/vn/$b.wav
