#!/bin/bash
# da lanciare quando le 6 voci sono arrivate
set -e
cd /home/user/work/build
python3 voci_arrivate.py
for n in BENV1_R2 MP1 MP23 MP4 COMP1 COMP2 R3_R2 R4_R2 SC6_1_R2 SC6_2_R2 SC6_3_R2 SC6_4_R2; do [ -f /home/user/work/vc/scambio/storia-V-lez11/vox/$n.wav ] && python3 asr.py /home/user/work/vc/scambio/storia-V-lez11/vox/$n.wav; done
rm -f mp/M1.ok mp/M23.ok mp/M4.ok clips/COVER_A.mkv.ok clips/MAP1.mkv.ok clips/MAP23.mkv.ok clips/MAP4.mkv.ok clips/COMPITI_SL.mkv.ok
python3 maps.py
python3 make_vc.py
python3 make_misc.py
python3 run_final.py 19
