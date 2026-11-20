#!/bin/bash
k=$1
python3 - <<P
import json,subprocess
s=json.load(open('/tmp/L18/cards_specs.json'))['$k']
subprocess.run(['python3','/tmp/L18/str/schede_spagnolo.py',json.dumps(s,ensure_ascii=False),'/tmp/L18/cards/$k','1.0'],check=True)
P
rm -rf /tmp/L18/cards/$k; [ -f /tmp/L18/cards/$k.mp4 ] && touch /tmp/L18/cards/$k.ok
