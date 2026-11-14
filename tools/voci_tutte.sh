#!/bin/bash
# Voci mancanti delle lezioni 5, 4, 3 (salta quelle già fatte: ogni file OK resta in voci/vox)
cd /home/claude/lezioni
python3 tools/voci_auto.py moda-tecnologie-III-lez05 INTRO1 R1 R2 R3 R4 R5 R6 R7 S1 S2 S3 S4 S5 S6 S7 AN1 AN2 AN3 AN4 AN5 GL1 RF1 FIN1 >> voci_l5.log 2>&1 || exit 3
python3 tools/voci_auto.py moda-tecnologie-III-lez04 INTRO1 R1 R2 R3 R4 R5 R6 S1 S2 S3 S4 S5 S6 GL1 RF1 FIN1 >> voci_l4.log 2>&1 || exit 3
python3 tools/voci_auto.py moda-tecnologie-III-lez03 INTRO1 R1 R2 R3 R4 R5 S1 S2 S3 S4 S5 AN1 AN2 GL1 RF1 FIN1 IN2 RIP R6 R7 R8 R9 R10 S6 S7 S8 S9 S10 AN3 AN4 GL2 RF2 FIN2 >> voci_l3.log 2>&1 || exit 3
echo TUTTE_OK
