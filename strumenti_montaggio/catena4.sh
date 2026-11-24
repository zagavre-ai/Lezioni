#!/bin/bash
cd /home/claude/w/code
python3 finalize.py 2 > fin2.log 2>&1
for n in 1 2; do python3 subs.py ../out/Storia_Lez21_Parte${n}_1080p.mp4 ../consegna/Storia_Lez21_Parte${n}.vtt > subs$n.log 2>&1; done
python3 package.py > package.log 2>&1
for n in 1 2; do python3 /home/user/Lezioni/kit/tools/controllo_rapido.py ../out/Storia_Lez21_Parte${n}_1080p.mp4 "Il mondo dal 2001 ad oggi" ../consegna > rapido$n.log 2>&1; done
echo ok > ../catena.ok
