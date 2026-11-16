#!/bin/bash
cd /home/claude/w7b && MODE=kore python3 main7.py > main_kore2.log 2>&1 && bash fine7v2.sh > fine7v2.log 2>&1; touch /home/claude/w7b/fine7v2.fatto
cd /home/claude/w10b && MODE=kore python3 main10.py > main_kore2.log 2>&1 && bash fine10v2.sh > fine10v2.log 2>&1; touch /home/claude/w10b/fine10v2.fatto
