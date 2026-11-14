#!/bin/bash
cd /home/user/work/build
for L in "spec_lez02 /home/user/work/lez02" "spec_lez5 /home/user/work/lez5"; do
  set -- $L; nice -n 5 python3 montaggio.py $1 $2 ALTRI > $2/mont_altri.log 2>&1; touch $2/altri.fatto
done
