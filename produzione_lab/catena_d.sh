#!/bin/bash
cd /home/user/work/build
for L in "spec_lez02 /home/user/work/lez02" "spec_lez5 /home/user/work/lez5"; do
  set -- $L; python3 montaggio.py $1 $2 D > $2/mont_d.log 2>&1; touch $2/d.fatto
done
