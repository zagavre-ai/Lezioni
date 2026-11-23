#!/bin/bash
cd /home/user/work/build
V=Storia_Lez11_Parte1_1080p.mp4
python3 verifica.py $V timeline_Parte1_full.json verifica.txt > verifica.log 2>&1 &
OMP_THREAD_LIMIT=1 python3 /home/user/work/controllo_rapido.py $V "L'URSS di Stalin (1924-1939)" > rapido.log 2>&1 &
wait
python3 pack.py > pack.log 2>&1
cp foglio_fotogrammi_*.jpg controllo_rapido_*.json consegna/ 2>/dev/null
python3 - <<'P'
import json,glob
for f in glob.glob('/home/user/work/build/controllo_rapido_*.json'):
    j=json.load(open(f));open('/home/user/work/build/severo.txt','w').write("controllo_rapido.py (kit/tools, 22/11) sul video finale: ESITO "+str(j.get('ESITO'))+"\nERRORI: "+json.dumps(j.get('ERRORI'),ensure_ascii=False)+"\nDA_GUARDARE: "+json.dumps(j.get('DA_GUARDARE'),ensure_ascii=False)[:1500]+"\n")
P
python3 rapporto.py >> pack.log 2>&1
cp consegna/RAPPORTO_REVISIONE.md . 2>/dev/null
touch post.fatto
