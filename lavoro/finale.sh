#!/bin/bash
# uso: finale.sh  -> monta le due Parti (assembla, audio esatto, codifica a gruppi)
cd /home/user/Lezioni/lavoro
python3 assembla.py 1 2 || exit 1
for p in 1 2; do
  O=/tmp/w/out/Storia_Lez10_Parte${p}_1080p.mp4
  rm -rf $O.gruppi $O; mkdir -p $O.gruppi
  python3 audio_esatto.py /tmp/w/build/lista_P$p.txt $O.gruppi/a.m4a && touch $O.gruppi/a.m4a.ok
  python3 ../kit/tools/finale_a_pezzi.py /tmp/w/build/lista_P$p.txt $O || exit 1
done
touch /tmp/w/finale.fatto
