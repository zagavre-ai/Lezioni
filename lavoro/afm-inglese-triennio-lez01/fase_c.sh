#!/bin/bash
# montaggio + codifica finale unica (riprende dai marcatori)
set -e
cd /home/claude/lezioni/afm-inglese-triennio-lez01
while [ ! -f .comp_ok ] || [ ! -f .fase_b_ok ]; do sleep 20; done
[ -f .asm_ok ] || { python3 asm_ing.py && touch .asm_ok; }
mkdir -p consegna
python3 /home/claude/lezioni/tools/finale_a_pezzi.py lista_finale.txt consegna/Inglese_Lez1_Parte1_1440p.mp4
touch .finale_ok
