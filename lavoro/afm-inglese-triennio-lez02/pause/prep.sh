set -e
cd /home/claude/ing2
[ -f orig/lez.ok ] || { ffmpeg -v error -y -f concat -safe 0 -i orig/concat.txt -c copy -movflags +faststart orig/lez.mp4 && touch orig/lez.ok; }
[ -f audio/B.ok ] || { ffmpeg -v error -y -i orig/lez.mp4 -vn -af "highpass=f=80,arnndn=m=/home/claude/kit/02_Video/sh.rnnn,loudnorm=I=-16:TP=-1.5:LRA=11" -ar 48000 -ac 1 audio/audio_B_full.wav && touch audio/B.ok; }
ffmpeg -v info -i audio/audio_B_full.wav -af silencedetect=noise=-42dB:d=0.9 -f null - 2> audio/silence.log
echo PREP_OK
