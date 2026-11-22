#!/bin/sh
W=/home/user/lav/wt_voci01;B=scambio/moda-tecnologie-III-lez01
mkdir -p /home/user/lav/lez01/vox /home/user/lav/lez01/img
prev=""
while true; do
  cd $W && timeout 100 git fetch -q origin voci-moda-tecnologie-III-lez01 2>/dev/null && git merge -q --no-edit FETCH_HEAD >/dev/null 2>&1
  nv=$(ls $W/$B/vox 2>/dev/null | grep -c wav); ni=$(ls $W/$B/img 2>/dev/null | grep -c png)
  [ "$nv" -gt 0 ] && cp -n $W/$B/vox/*.wav /home/user/lav/lez01/vox/ 2>/dev/null
  [ "$ni" -gt 0 ] && cp -n $W/$B/img/*.png /home/user/lav/lez01/img/ 2>/dev/null
  cur="voci:$nv immagini:$ni"
  [ "$cur" != "$prev" ] && echo "$cur" && prev="$cur"
  [ "$nv" -ge 188 ] && [ "$ni" -ge 20 ] && echo "TUTTO ARRIVATO" && break
  sleep 120
done
