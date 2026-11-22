#!/bin/sh
# uso: batch2.sh "1 2 3 ..."   (ordine); ogni argomento è preso una sola volta (lock con mkdir)
for k in $1; do
  n=$(printf %02d $k)
  mkdir /home/user/lav/lez01/bg/lock_$n 2>/dev/null || continue
  python3 prof_bg.py $k > /home/user/lav/lez01/bg_A$k.log 2>&1 && python3 prof_comp.py $k >> /home/user/lav/lez01/bg_A$k.log 2>&1 && touch /home/user/lav/lez01/bg/A$n/prof.ok
done
