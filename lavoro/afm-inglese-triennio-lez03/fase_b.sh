#!/bin/bash
# Lez5 · fase B: schemi, animazioni, glossario, ripasso finale, schede R/FIN, jingle (dopo le voci)
set -e
cd /home/claude/lezioni/afm-inglese-triennio-lez03
SC=1 python3 po_moda.py S1 S2 S3 S4 S5 S6 S7; echo PO_OK
( cd an && python3 render_l5.py AN1 AN2 AN3 AN4 AN5 && python3 render_extra.py GL1 RF1 ); echo AN_OK
python3 run_dark2.py R1 R2 R3 R4 R5 R6 R7 FIN1; echo DK_OK
python3 make_sting.py; echo STING_OK
