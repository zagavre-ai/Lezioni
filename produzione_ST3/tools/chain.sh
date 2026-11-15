#!/bin/bash
# chain.sh : rimonta e codifica lez02 (2 parti) e lez03 (1 parte)
T=/home/user/lav/tools
for spec in "02 1" "02 2" "03 1"; do set -- $spec; n=$1; p=$2; D=/home/user/lav/l$n
  rm -f $D/p$p/pezzi/CM*.ok $D/p$p/pezzi/GL*.ok
  python3 $T/build.py $D $p > $D/build$p.log 2>&1
  python3 $T/subs.py $D $p > /dev/null 2>&1
  mkdir -p $D/fin
  python3 /home/user/Lezioni/kit/tools/finale_a_pezzi.py $D/p$p/lista.txt $D/fin/Storia_III_Lez${n#0}_Parte${p}_1080p.mp4 > $D/fin/enc$p.log 2>&1
  touch $D/fin/enc$p.fatto
done
touch /home/user/lav/chain.fatto
