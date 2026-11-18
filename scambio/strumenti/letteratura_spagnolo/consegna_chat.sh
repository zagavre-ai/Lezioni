#!/bin/bash
# consegna_chat.sh NN — spinge il video con le schede di Spagnolo sul ramo spagnolo-letteratura-V-lezNN (la master verifica e carica su Vimeo)
set -e
N=$1; M=$((10#$N)); W=$HOME/spagnolo_lez$N; QUI=$(cd "$(dirname "$0")" && pwd); R=$(cd "$QUI/../../.." && pwd); B=spagnolo-letteratura-V-lez$N
T=$(mktemp -d)/wt; git -C $R worktree add -q --detach $T; cd $T; git checkout -q --orphan $B; git rm -rqf . ; mkdir $B; cd $B
split -b 90M -d -a 2 $W/fix.mp4 Letteratura_Lez${M}_Parte1_1080p.mp4.parte_
sha256sum $W/fix.mp4 | cut -c1-64 > Letteratura_Lez${M}_Parte1_1080p.mp4.sha256; cp $W/foglio.png $W/schede/finestre.json .
cd $T; git add -A; git -c user.name="Sara Zagarese" -c user.email="responsabiletecnicaegraficacst@gmail.com" commit -qm "Letteratura V lezione $M: schede come Spagnolo"
git push -q -f origin $B; cd $R; git worktree remove --force $T; echo "CONSEGNATA $N su $B"
