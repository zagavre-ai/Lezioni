#!/bin/bash
# uso: push_files.sh RAMO MESSAGGIO DESTDIR file... (ramo orfano se non esiste; aggiunge/aggiorna i file in DESTDIR)
set -e
BR=$1; MSG=$2; DEST=$3; shift 3
R=/home/claude/lezioni; WT=/tmp/wt_$BR
git -C $R worktree remove --force $WT 2>/dev/null || true; rm -rf $WT
if git -C $R fetch -q --depth 1 origin $BR:refs/remotes/origin/$BR 2>/dev/null; then
  git -C $R worktree add -q --detach $WT origin/$BR
else
  git -C $R worktree add -q --detach $WT; git -C $WT checkout -q --orphan $BR; git -C $WT rm -rfq . >/dev/null 2>&1 || true
fi
mkdir -p $WT/$DEST
for f in "$@"; do cp "$f" $WT/$DEST/; done
git -C $WT add -A
git -C $WT -c commit.gpgsign=false commit -qm "$MSG" || echo "niente da fare"
git -C $WT -c push.negotiate=true push -q origin HEAD:refs/heads/$BR
git -C $R worktree remove --force $WT
echo "PUSH OK $BR"
