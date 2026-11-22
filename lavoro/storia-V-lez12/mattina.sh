#!/bin/bash
# Quando arrivano le voci Kore: scarica, importa, ricostruisce le schede con voce, riassembla, rifà sottotitoli e controlli.
set -e
cd /home/user/Lezioni
git fetch -q origin voci-storia-V-lez12
mkdir -p /home/user/w12/vox_raw /tmp/vx && rm -rf /tmp/vx/* 
git archive origin/voci-storia-V-lez12 scambio/storia-V-lez12/vox | tar -x -C /tmp/vx
python3 - <<'P'
import sys, shutil, os, glob
sys.path.insert(0,'/home/user/Lezioni/lavoro/storia-V-lez12')
import contenuti as C
n=0
for nome in C.VOCI:
    f=f'/tmp/vx/scambio/storia-V-lez12/vox/{nome}.wav'
    if os.path.exists(f): shutil.copy(f,f'/home/user/w12/vox_raw/{nome}.wav'); n+=1
print('voci nuove trovate:',n,'su',len(C.VOCI))
P
cd lavoro/storia-V-lez12
python3 importa_voci.py | tee /home/user/w12/importa.log
