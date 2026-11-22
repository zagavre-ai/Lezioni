#!/bin/bash
# Rifacimento finale dopo l'arrivo delle voci: uso: bash final.sh
set -e
cd /tmp/claude-0/l15; export VOXDIR=/tmp/claude-0/l15/vox48
cp /work/voci/scambio/storia-V-lez15/vox/*.wav vox/ 2>/dev/null || true
for f in vox/*.wav.prov; do [ -e "$f" ] || continue; b=${f%.prov}; [ -s /work/voci/scambio/storia-V-lez15/vox/$(basename $b) ] && rm -f $f; done
python3 vox_prep.py
python3 asr_times.py $(ls vox48 | grep -E "^(AN|DP).*wav$" | sed 's/.wav//')
