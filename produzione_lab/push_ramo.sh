#!/bin/bash
# push_ramo.sh RAMO "messaggio" SRC=DEST [SRC=DEST...]   (ramo orfano o esistente, solo i file indicati)
set -e
BR=$1; MSG=$2; shift 2
R=/home/user/Lezioni; W=/tmp/wt_$BR; rm -rf $W; git -C $R worktree prune
if git -C $R ls-remote --exit-code --heads origin $BR >/dev/null 2>&1; then
  git -C $R fetch -q origin $BR:refs/remotes/origin/$BR; git -C $R worktree add -q --detach $W origin/$BR
else
  git -C $R worktree add -q --detach $W HEAD; git -C $W checkout -q --orphan $BR; git -C $W rm -rfq . >/dev/null 2>&1 || true
fi
for p in "$@"; do s=${p%%=*}; d=${p#*=}; mkdir -p $W/$(dirname $d); cp "$s" "$W/$d"; done
git -C $W add -f . ; git -C $W commit -qm "$MSG" || true
for i in 1 2 3 4; do git -C $W push -q origin HEAD:refs/heads/$BR && break || sleep 5; done
git -C $R worktree remove --force $W; echo pushed $BR
