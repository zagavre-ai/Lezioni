#!/bin/bash
# v2 lezione 7: dopo il montaggio Kore (main7.py), codifica, controlli, PDF, rapporto, consegna, stato
set -e
cd /home/claude/w7b
OUT=Inglese_Lez7_Parte1_1080p.mp4; VTT=Inglese_Lez7_Parte1.vtt; K=/home/claude/main/kit/tools; T=afm-inglese-triennio-lez07
[ -f $OUT ] || CRF=19 python3 /home/claude/tools/finale_cache.py out_kore/lista.txt $OUT /home/claude/w7b/cache_finale
python3 mksub7.py out_kore/timeline.json $VTT
python3 /home/claude/tools/vttsnap.py $OUT $VTT; python3 /home/claude/tools/vttsnap.py $OUT $VTT
python3 $K/controllo_finale.py $OUT out_kore/timeline.json $VTT > controllo_finale.log 2>&1 || true
python3 $K/controllo_jingle.py $OUT out_kore/timeline.json > controllo_jingle.log 2>&1 || true
python3 $K/scheda_da_timeline.py $OUT out_kore/timeline.json quiz_argomenti.json "Trade and commerce · Parte 1" scheda_pubblicazione.json Inglese
python3 syncchk7.py $OUT out_kore/timeline.json 6 2>/dev/null | grep -v sandbox > sincronia.txt
python3 /home/claude/tools/pdf_slide.py pagine_pdf.json ${T}_slide.pdf
ffmpeg -v error -y -i $OUT -vf "fps=1/30,scale=320:-1,tile=10x15" -frames:v 1 controllo_minuti.jpg
echo FATTO
