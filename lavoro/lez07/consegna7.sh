#!/bin/bash
# Consegna della lezione 7 sul ramo consegna-afm-inglese-triennio-lez07: video a pezzi da 90 MiB + sha256 e tutti gli altri file.
set -e
cd /home/claude/w7
V=Inglese_Lez7_Parte1_1080p.mp4; BR=consegna-afm-inglese-triennio-lez07
python3 /home/claude/main/kit/tools/testo_youtube.py scheda_pubblicazione.json "Inglese · Triennio Amministrazione, Finanza e Marketing|Inglese AFM" "Prof.ssa Maria Vittoria Fontanesi" "Trade and commerce" 1 out_kore/timeline.json > testo_youtube.txt
rm -rf consegna && mkdir consegna
split -b 94371840 -d -a 2 $V consegna/$V.parte_
sha256sum $V > consegna/$V.sha256
cp Inglese_Lez7_Parte1.vtt Quiz_Inglese_Lez7.txt quiz_argomenti.json scheda_pubblicazione.json testo_youtube.txt Mappe_afm-inglese-triennio-lez07.pdf LEGGIMI.md consegna/
for f in Test_Inglese_Lez7.xlsx Test_Inglese_Lez7_PROPOSTA_DA_VALIDARE.xlsx compiti.json Compiti_Inglese_Lez7.pdf Dispensa_Inglese_Lez7.pdf; do [ -f $f ] && cp $f consegna/ || true; done
ls -la consegna
/home/claude/tools/push_files.sh $BR "consegna afm-inglese-triennio-lez07" . consegna/*
# verifica: i pezzi sul ramo ricompongono il video
cd /home/claude/lezioni && git fetch -q --depth 1 origin $BR:refs/remotes/origin/$BR
rm -rf /tmp/verifica7 && mkdir /tmp/verifica7 && cd /tmp/verifica7
for p in $(git -C /home/claude/lezioni ls-tree --name-only origin/$BR | grep "$V.parte_" | sort); do git -C /home/claude/lezioni cat-file -p origin/$BR:$p >> $V; done
git -C /home/claude/lezioni cat-file -p origin/$BR:$V.sha256 | sha256sum -c - && echo "VERIFICA SHA256 DAL RAMO: OK"
rm -rf /tmp/verifica7
