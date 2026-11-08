#!/bin/bash
set -e
cd /home/claude/lezioni/afm-inglese-triennio-lez01
python3 run_dark_ing.py; echo DK_OK
python3 po_ing.py; echo PO_OK
python3 an_ing.py GL1 RF1; echo AN_OK
touch .fase_b_ok
