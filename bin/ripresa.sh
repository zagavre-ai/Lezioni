#!/bin/bash
# uso: ripresa.sh NN  (voci Kore arrivate): scarica, importa, rifà AN e pezzi con voce, lista
set -e
NN=$1; T=letteratura-V-lez$NN; L=/home/claude/w/l$NN; export PYTHONPATH=/home/user/Lezioni/kit/tools
cd /home/user/Lezioni && git fetch -q origin voci-$T
mkdir -p $L/voci/kore $L/vox
git archive origin/voci-$T scambio/$T/vox 2>/dev/null | tar -x -C /tmp/ripresa_$NN 2>/dev/null || (mkdir -p /tmp/ripresa_$NN && git archive origin/voci-$T scambio/$T/vox | tar -x -C /tmp/ripresa_$NN)
cp /tmp/ripresa_$NN/scambio/$T/vox/*.wav $L/voci/kore/ 2>/dev/null || true
cp /tmp/ripresa_$NN/scambio/$T/vox/AN*.wav $L/vox/ 2>/dev/null || true
cd $L && python3 /home/claude/w/bin/importa2.py $NN
