#!/bin/bash
# prepara la cartella di consegna /tmp/w/cons_out (video a pezzi, sha256, vtt, timeline, scheda, quiz, verifica, compiti, dispensa, mappe)
set -e
cd /home/user/Lezioni/lavoro
O=/tmp/w/cons_out; rm -rf $O; mkdir -p $O
for p in 1 2; do
  V=/tmp/w/out/Storia_Lez10_Parte${p}_1080p.mp4
  python3 sub_vtt.py $p /tmp/w/build/timeline_Parte$p.json $O/Storia_Lez10_Parte$p.vtt
  cp /tmp/w/build/timeline_Parte$p.json $O/timeline_Parte$p.json
  python3 ../kit/tools/scheda_da_timeline.py $V /tmp/w/build/timeline_Parte$p.json /tmp/w/cons/quiz_argomenti.json "La Germania da Weimar al nazismo · Parte $p" $O/scheda_pubblicazione_Parte$p.json "Storia"
  (cd $O && split -b 90M -d -a 2 $V Storia_Lez10_Parte${p}_1080p.mp4.part && sha256sum $V | sed "s#/tmp/w/out/##" > Storia_Lez10_Parte${p}_1080p.sha256 && sha256sum Storia_Lez10_Parte${p}_1080p.mp4.part* >> Storia_Lez10_Parte${p}_1080p.sha256)
done
cp /tmp/w/cons/quiz_argomenti.json /tmp/w/cons/compiti.json /tmp/w/cons/verifica_finale.json /tmp/w/cons/Verifica_finale_Storia_Lez10.xlsx /tmp/w/cons/Quiz_Storia_Lez10.txt $O/
cp /tmp/w/cons/Storia_Lez10_Parte1_slide.pdf /tmp/w/cons/Storia_Lez10_Parte2_slide.pdf /tmp/w/cons/Storia_Lez10_mappe.pdf $O/
python3 tabella_tagli.py > $O/tabella_tagli.md
ls -la $O
