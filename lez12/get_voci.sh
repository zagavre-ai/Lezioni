#!/bin/bash
# scarica le voci Kore dal ramo voci-storia-arte-V-lez12 in lavoro/vox/
cd /home/user/Lezioni
git fetch -q --depth=1 origin voci-storia-arte-V-lez12 && git checkout -q FETCH_HEAD -- scambio/storia-arte-V-lez12 2>&1 | tail -1
mkdir -p lavoro/vox; cp -n scambio/storia-arte-V-lez12/vox/*.wav lavoro/vox/ 2>/dev/null; ls scambio/storia-arte-V-lez12/ ; ls lavoro/vox | wc -l; cat scambio/storia-arte-V-lez12/ESITI*.txt 2>/dev/null | tail -30
