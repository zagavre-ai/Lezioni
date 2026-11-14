#!/bin/bash
# consegna.sh SPEC WORKDIR PARTE  -> prepara e pubblica il ramo consegna-<tag>
SPEC=$1; W=$2; P=$3; B=/home/user/work/build
cd $W
read FILE TAG < <(python3 -c "import sys;sys.path.insert(0,'$B');import $SPEC as S;print(S.FILE,S.TAG)")
V=${FILE}_Parte${P}_1080p.mp4
D=$W/consegna_$P; mkdir -p $D
split -b 90M -d -a 2 $V $D/$V.parte_
(cd $D && for f in $V.parte_*; do :; done)
sha256sum $V | sed "s# .*# $V#" > $D/$V.sha256
for f in ${FILE}_Parte${P}.vtt Quiz_${FILE}_Parte${P}.txt quiz_argomenti$P.json scheda_pubblicazione$P.json testo_youtube_$P.txt timeline$P.json Dispensa_${FILE}.pdf; do [ -f $f ] && cp $f $D/; done
cp Lezione.*.xlsx $D/Test_finale_${FILE}.xlsx 2>/dev/null
ls -la $D
