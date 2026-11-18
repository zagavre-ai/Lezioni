#!/bin/bash
# prepara_tratti.sh VIDEO OUTDIR — i tratti interi della prof, 852x480 -> 1920x1080 (solo colore e nitidezza), audio con la catena del kit
set -e; V=$1; O=$2; Q=$(cd "$(dirname "$0")" && pwd); mkdir -p $O
VF="fps=30,scale=1920:1080:flags=lanczos,hqdn3d=1.5:1.5:3:3,eq=contrast=1.04:saturation=1.03,cas=0.35,format=yuv420p"
AF="aresample=48000,highpass=f=80,arnndn=m=$Q/sh.rnnn,loudnorm=I=-16:TP=-1.5:LRA=11,alimiter=limit=0.89,aresample=48000"
cut(){ # nome inizio fine [filtro extra video]
  [ -f $O/$1.ok ] && return
  ffmpeg -y -v error -ss $2 -to $3 -i $V -vf "${4:+$4,}$VF" -af "$AF" -c:v libx264 -preset veryfast -crf 14 -c:a pcm_s16le $O/$1.mkv && touch $O/$1.ok; echo "$1 fatto"; }
cut C0 0 9.6
cut T1 139 508
cut T2 543 1400
cut T3 1410 1469
cut T4 1474 1653
cut T5 1658 2001
cut T6 2011 2387
cut T7 2482 2604 "delogo=x=30:y=443:w=210:h=33"
touch $O/tutti.ok
