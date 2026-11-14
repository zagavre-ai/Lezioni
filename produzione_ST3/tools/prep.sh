#!/bin/bash
# prep.sh DIR : doc.wav (16k), doc48.wav (-16 LUFS), asr12.json
cd "$1"; V=$(ls LEZIONE*.mp4 | head -1)
[ -f doc.wav ] || ffmpeg -v error -y -i "$V" -vn -ac 1 -ar 16000 doc.wav
[ -f doc48.wav ] || /home/user/lav/tools/norm_doc.sh "$V" doc48.wav > norm.log 2>&1
[ -f asr12.json ] || python3 /home/user/lav/tools/trascrivi_corto.py doc.wav asr12.json > asr12.log 2>&1
touch prep.fatto
