#!/bin/bash
# Pubblica il pacchetto su revisione-storia-V-lez11 (sostituisce la consegna del 19/11). Uso: push_rev.sh
set -e
B=/home/user/work/build
REPO=/home/user/Lezioni
WT=/home/user/work/rev_push
git -C $REPO fetch -q origin revisione-storia-V-lez11
git -C $REPO worktree remove --force $WT 2>/dev/null || true
git -C $REPO worktree add -q --detach $WT origin/revisione-storia-V-lez11
D=$WT/revisione-storia-V-lez11
# togli i file della vecchia consegna
git -C $WT rm -q -r --ignore-unmatch revisione-storia-V-lez11 >/dev/null
mkdir -p $D
V=Storia_Lez11_Parte1_1080p.mp4
cp $B/$V $D/
(cd $D && sha256sum $V > $V.sha256 && split -b 90M -d -a 2 $V $V.parte_ && rm $V)
cp $B/consegna/* $D/
cp $B/verifica.txt $D/controllo_finale_misure.txt
cd $WT
git add -A revisione-storia-V-lez11
git commit -qm "lez11 correzioni 22/11: consegna (video, sottotitoli, dispensa, mappe, rapporto)"
git push -q origin HEAD:refs/heads/revisione-storia-V-lez11
echo PUSH_OK
git -C $REPO worktree remove --force $WT
