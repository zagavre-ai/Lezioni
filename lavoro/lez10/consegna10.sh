#!/bin/bash
# Consegna della lezione 7 sul ramo consegna-afm-inglese-triennio-lez10: video a pezzi da 90 MiB + sha256 e tutti gli altri file.
set -e
cd /home/claude/w10
V=Inglese_Lez10_Parte1_1080p.mp4; BR=consegna-afm-inglese-triennio-lez10
python3 /home/claude/main/kit/tools/testo_youtube.py scheda_pubblicazione.json "Inglese · Triennio Amministrazione, Finanza e Marketing|Inglese AFM" "Prof.ssa Maria Vittoria Fontanesi" "Work today" 1 out_kore/timeline.json > testo_youtube.txt
rm -rf consegna && mkdir consegna
split -b 94371840 -d -a 2 $V consegna/$V.parte_
for f in consegna/$V.parte_*; do mv "$f" "consegna/$V.parte_$(basename $f | sed 's/.*parte_//')"; done
sha256sum $V > consegna/$V.sha256
cp Inglese_Lez10_Parte1.vtt Quiz_Inglese_Lez10.txt quiz_argomenti.json scheda_pubblicazione.json testo_youtube.txt Mappe_afm-inglese-triennio-lez10.pdf LEGGIMI.md consegna/
for f in Test_Inglese_Lez10.xlsx Test_Inglese_Lez10_PROPOSTA_DA_VALIDARE.xlsx compiti.json Compiti_Inglese_Lez10.pdf Dispensa_Inglese_Lez10.pdf; do [ -f $f ] && cp $f consegna/ || true; done
ls -la consegna
/home/claude/tools/push_files.sh $BR "consegna afm-inglese-triennio-lez10" . consegna/*
# verifica: i pezzi sul ramo ricompongono il video
cd /home/claude/lezioni && git fetch -q --depth 1 origin $BR:refs/remotes/origin/$BR
rm -rf /tmp/verifica7 && mkdir /tmp/verifica7 && cd /tmp/verifica7
for p in $(git -C /home/claude/lezioni ls-tree --name-only origin/$BR | grep "$V.parte_" | sort); do git -C /home/claude/lezioni cat-file -p origin/$BR:$p >> $V; done
git -C /home/claude/lezioni cat-file -p origin/$BR:$V.sha256 | sha256sum -c - && echo "VERIFICA SHA256 DAL RAMO: OK"
rm -rf /tmp/verifica7
