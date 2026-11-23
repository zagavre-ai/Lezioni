#!/bin/bash
# uso: consegna.sh  (dopo la codifica finale e i controlli)
set -e
V=StoriaArteV_Lez12_Parte1_1080p.mp4
C=/home/user/Lezioni/lavoro/consegna
R=/home/user/Lezioni/revisione-storia-arte-V-lez12
mkdir -p $R
cd $C
sha256sum $V > $V.sha256
split -b 90M -d -a 2 $V $V.parte_
mv $V.parte_* $R/ ; cp $V.sha256 $R/
for f in *.vtt *.json *.pdf *.md *.jpg *.xlsx; do [ -f "$f" ] && cp "$f" $R/ || true; done
ls -la $R | head -40
