#!/bin/bash
# uso: runjob.sh NOME   (legge jobs/NOME.json, scrive sch/NOME.mp4)
cd /tmp/claude-0/w; export CHROME_BIN=/opt/pw-browsers/chromium-1243/chrome-linux64/chrome
[ -f sch/$1.mp4 ] && exit 0
rm -rf sch/$1; python3 schede_fast.py "$(cat jobs/$1.json)" sch/$1 1.0 > sch/$1.log 2>&1 && rm -rf sch/$1
