#!/bin/sh
for k in 1 2 3 4 5 6 7 8 9 10; do
  [ -f /home/user/lav/lez01/bg/A$(printf %02d $k)/prof.ok ] && continue
  python3 prof_bg.py $k > /home/user/lav/lez01/bg_A$k.log 2>&1 && python3 prof_comp.py $k >> /home/user/lav/lez01/bg_A$k.log 2>&1 && touch /home/user/lav/lez01/bg/A$(printf %02d $k)/prof.ok
done
touch /home/user/lav/lez01/bg/batch.ok
