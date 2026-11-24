#!/bin/bash
# Sostituisce le voci provvisorie con quelle Kore arrivate, rifa' solo le schede con voce, ricodifica e fa i controlli.
set -x
cd /home/user/Lezioni && git fetch -q origin voci-storia-V-lez21 && git checkout origin/voci-storia-V-lez21 -- scambio/storia-V-lez21 2>&1 | tail -n 1
cd /home/claude/w/code
python3 asr_voci.py /home/user/Lezioni/scambio/storia-V-lez21/vox /home/claude/w/voci_asr > asr_voci2.log 2>&1
python3 check_voci.py > check_voci.log 2>&1
cd /home/claude/w/clips
rm -f p*_AP*.mkv* p*_M[0-9]*.mkv* p*_pill* p*_glos* p*_ripf* p*_cop.mkv* p*_spieg* p*_mapfin* p*_compi* p*_fine* j*
rm -f ../slides/AP* ../slides/M[0-9]* ../slides/pill* ../slides/glos* ../slides/ripf* ../slides/cop* ../slides/spieg* ../slides/compi* ../slides/fine*
rm -f ../consegna/*_asr.* ../consegna/controlli* ../catena.ok
# gli approfondimenti cambiano durata: i pezzi del docente restano, ma le pagine/slide AP si rifanno
cd /home/claude/w/code && ./catena2.sh
