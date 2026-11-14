#!/bin/bash
# finale.sh SPEC WORKDIR PARTE   -> video finale 1080p, volume, controlli (in background, con marcatori)
SPEC=$1; W=$2; P=$3; B=/home/user/work/build; K=/home/user/Lezioni/kit/tools
cd $W
FILE=$(python3 -c "import sys;sys.path.insert(0,'$B');import $SPEC as S;print(S.FILE)")
V=$W/${FILE}_Parte${P}_1080p.mp4
python3 $B/assembla.py $SPEC $W lista $P || exit 1
[ -f $V.codificato ] || { python3 $K/finale_a_pezzi.py $W/lista$P.txt $V > $W/finale$P.log 2>&1 && touch $V.codificato; }
[ -f $V.codificato ] || { echo "CODIFICA FALLITA"; exit 2; }
python3 $K/volume16.py $V > $W/volume$P.log 2>&1
echo FINE_FINALE > $W/finale$P.fatto
