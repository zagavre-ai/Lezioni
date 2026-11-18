#!/bin/bash
# uso: runcard.sh nome  (specs/nome.json -> cards/nome.mp4)
cd /tmp/w/build
[ -f ../cards/$1.mp4 ] && exit 0
python3 /tmp/w/tools/schede_spagnolo.py "$(cat specs/$1.json)" /tmp/w/cards/$1 1.0 > /tmp/w/build/log_$1.txt 2>&1 && rm -rf /tmp/w/cards/$1
