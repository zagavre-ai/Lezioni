#!/bin/bash
# Prepara una lezione nuova (Metodo v2 «lezioni dal PDF»): audio pulito, trascrizione, testo del PDF, domande
# uso (dalla cartella della lezione): ./prepara_lezione.sh      — richiede orig/lez1.mp4, lez1.pdf, lez1.xlsx
set -e
D=$(cd "$(dirname "$0")" && pwd); cd "$D"
mkdir -p audio voci/wav an es po dk sv w2 consegna anteprima fr
[ -f orig/lez1.mp4 ] || { echo "manca orig/lez1.mp4"; exit 1; }
echo "durata: $(ffprobe -v error -show_entries format=duration -of csv=p=0 orig/lez1.mp4) s"
# 1. audio pulito (versione B approvata): filtro dei bassi + riduzione del rumore + volume -16 LUFS
ffmpeg -v error -y -i orig/lez1.mp4 -vn -af "highpass=f=80,arnndn=m=/home/claude/kit/02_Video/sh.rnnn,loudnorm=I=-16:TP=-1.5:LRA=11" -ar 48000 -ac 1 audio/audio_B_full.wav
# 2. trascrizione con parole e tempi (Parakeet)
ffmpeg -v error -y -i orig/lez1.mp4 -vn -ac 1 -ar 16000 audio16.wav
( cd /home/claude/asr_pk && python3 pk.py "$D/audio16.wav" "$D/pk.jsonl" 0 )
# 3. testo del PDF della docente
python3 estrai_pdf.py lez1.pdf
python3 build_blocks.py > blocks.txt
echo "PREPARA_OK · ora: struttura.py (argomenti/sottotitoli), estrai_quiz.py, align.py, coverage.py, sync.py, align_s.py"
