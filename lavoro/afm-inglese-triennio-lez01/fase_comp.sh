#!/bin/bash
# docente + slide su tutta la lezione, a pezzi da 540 s (riprende dai .ok)
set -e
cd /home/claude/lezioni/afm-inglese-triennio-lez01
mkdir -p ds; TOT=3731.5; : > ds/lista.txt
for i in 0 1 2 3 4 5 6; do
  S=$((i*540)); D=540; [ $i -eq 6 ] && D=$(python3 -c "print($TOT-$S)")
  [ -f ds/p$i.ok ] || { ./comp.sh $S $D ds/p$i.mp4 && touch ds/p$i.ok; }
  echo "file 'p$i.mp4'" >> ds/lista.txt
done
ffmpeg -v error -y -f concat -safe 0 -i ds/lista.txt -c copy docente_slide_1080.mp4
touch .comp_ok
