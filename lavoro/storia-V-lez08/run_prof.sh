#!/bin/bash
cd /home/user/Lezioni/lavoro/storia-V-lez08
O=/tmp/w/work/out; mkdir -p $O
p=3
for t in 1 2 3; do python3 build_prof.py $t $p $O > $O/D$t.log 2>&1; p=$(grep -o 'ultima pagina [0-9]*' $O/D$t.log | awk '{print $3}'); p=$((p+1)); done
p=3
for t in 4 5 6 7; do python3 build_prof.py $t $p $O > $O/D$t.log 2>&1; p=$(grep -o 'ultima pagina [0-9]*' $O/D$t.log | awk '{print $3}'); p=$((p+1)); done
touch $O/prof.fatto
