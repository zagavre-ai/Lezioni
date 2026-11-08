#!/bin/bash
# Lez5 · resto della fase B (dopo l'interruzione): glossario, riepilogo, schede R/FIN, schede Quiz (5 domande), jingle
set -e
cd /home/claude/lezioni/afm-inglese-triennio-lez03
( cd an && python3 render_extra.py GL1 RF1 ); echo AN_OK
python3 run_dark2.py R1 R2 R3 R4 R5 R6 R7 FIN1; echo DK_OK
python3 run_dark_moda.py Q1 Q2 Q3 Q4 Q5 Q6 Q7; echo Q_OK
python3 make_sting.py; echo STING_OK
