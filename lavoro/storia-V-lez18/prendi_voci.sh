#!/bin/bash
# scarica le voci della master e rifà tutto
set -e
cd /home/user/Lezioni && git fetch -q origin voci-storia-V-lez18
for f in $(git ls-tree -r --name-only origin/voci-storia-V-lez18 | grep -E "scambio/storia-V-lez18/(vox/|img/|DALLA_MASTER)"); do mkdir -p /home/user/work18/$(dirname $f); git show origin/voci-storia-V-lez18:$f > /home/user/work18/$f; done
ls /home/user/work18/scambio/storia-V-lez18/vox | wc -l
