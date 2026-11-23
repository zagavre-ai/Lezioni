#!/bin/bash
set -e
cd /home/user/Lezioni/lez12
python3 asm.py > ../lavoro/asm.log
cd ../lavoro
rm -rf consegna/StoriaArteV_Lez12_Parte1_1080p.mp4.gruppi consegna/StoriaArteV_Lez12_Parte1_1080p.mp4
python3 ../tools/finale_a_pezzi.py lista.txt consegna/StoriaArteV_Lez12_Parte1_1080p.mp4 > enc.log 2>&1
python3 -W ignore ../tools/controllo_rapido.py consegna/StoriaArteV_Lez12_Parte1_1080p.mp4 "Dadaismo e Surrealismo" consegna > cr.log 2>&1 || true
python3 ../lez12/misure.py > misure.log 2>&1
python3 ../lez12/sync.py consegna/StoriaArteV_Lez12_Parte1_1080p.mp4 consegna/timeline_Parte1.json > sync.log 2>&1
ffmpeg -y -v error -f concat -safe 0 -i lista.txt -vn -c:a pcm_s16le prep/all.wav
python3 ../tools/controllo_jingle_lez12.py prep/all.wav consegna/timeline_Parte1.json > jingle.log 2>&1 || true
python3 ../lez12/vtt.py consegna/timeline_Parte1.json consegna/StoriaArteV_Lez12_Parte1.vtt > vtt.log 2>&1
python3 ../tools/scheda_da_timeline.py consegna/StoriaArteV_Lez12_Parte1_1080p.mp4 consegna/timeline_Parte1.json consegna/quiz_argomenti.json "Storia dell'arte V · Lezione 12 · Dadaismo e Surrealismo" consegna/scheda_pubblicazione_Parte1.json "Storia dell'arte (V)" > schedapub.log 2>&1
python3 ../lez12/tagli.py consegna/timeline_Parte1.json > tagli.log 2>&1
python3 ../lez12/dispensa.py > dispensa.log 2>&1
touch final.fatto
