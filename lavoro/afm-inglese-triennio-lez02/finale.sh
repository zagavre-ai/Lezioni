set -e
cd /home/claude/lezioni/afm-inglese-triennio-lez02
[ -f timeline.json ] && [ -f asm.ok ] || { python3 asm.py > asm.log 2>&1; touch asm.ok; }
python3 /home/claude/lezioni/tools/finale_a_pezzi.py Inglese_Lez2_Parte1_1440p.mp4.txt Inglese_Lez2_Parte1_1440p.mp4 > finale.log 2>&1
echo FINALE_OK >> finale.log
