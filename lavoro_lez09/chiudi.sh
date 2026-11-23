#!/bin/bash
# uso: bash chiudi.sh   (dopo che i pezzi del prof sono pronti)  -> assembla, codifica, sottotitoli, dispense
cd /home/user/Lezioni/w/lav
git -C /home/user/Lezioni/w/wt_voci pull -q --no-edit origin voci-storia-V-lez09 2>&1 | tail -n 1
for P in 1 2; do python3 assemble.py $P > out/asm$P.log 2>&1 || { echo "assemble $P fallito"; exit 1; }; done
for P in 1 2; do python3 final.py $P 19 > out/final$P.log 2>&1 || { echo "final $P fallito"; exit 1; }; python3 sub.py $P >> out/final$P.log 2>&1; done
python3 dispensa.py 1 > out/disp1.log 2>&1; python3 dispensa.py 2 > out/disp2.log 2>&1; python3 mappe_pdf.py > out/mappe.log 2>&1
echo CHIUSO
