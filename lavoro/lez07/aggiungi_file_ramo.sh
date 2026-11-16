#!/bin/bash
# Aggiunge/aggiorna file in un ramo SENZA scaricare i file grandi del ramo (solo la struttura). uso: aggiungi_file_ramo.sh RAMO MESSAGGIO file...
set -e
BR=$1; MSG=$2; shift 2; R=/home/claude/lezioni; cd $R
git fetch -q --depth 1 --filter=blob:none origin $BR:refs/remotes/origin/$BR
export GIT_INDEX_FILE=/tmp/idx_$BR; rm -f $GIT_INDEX_FILE
git read-tree origin/$BR
for f in "$@"; do b=$(git hash-object -w "$f"); git update-index --add --cacheinfo 100644,$b,$(basename "$f"); done
T=$(git write-tree); C=$(echo "$MSG" | git commit-tree $T -p origin/$BR)
git -c push.negotiate=true push -q origin $C:refs/heads/$BR
rm -f $GIT_INDEX_FILE; echo "PUSH OK $BR $C"
