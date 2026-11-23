#!/bin/bash
cd /home/user/Lezioni/w/lav
python3 job_prof.py 1 > out/job1.err 2>&1 &
python3 job_prof.py 2 > out/job2.err 2>&1
wait
bash chiudi.sh > out/chiudi.log 2>&1
cd out; export OMP_THREAD_LIMIT=1
for p in 1 2; do python3 /home/user/Lezioni/tools/controllo_severo.py Storia_Lez9_Parte${p}_1080p.mp4 "L’Italia del regime fascista (1925-1938)" 15 > sev$p.json 2> sev$p.err; done
echo RIFATTO > rifatto.done
