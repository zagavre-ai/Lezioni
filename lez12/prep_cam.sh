#!/bin/bash
cd /home/user/Lezioni/lavoro
SRC="in/video/LEZIONE 12 DADAISMO E SURREALISMO.mp4"
# webcam 4:3 (412x309) con posizione variabile nel tempo (A: 0-1226.3 e 1922.45-2880.6; B: 1226.3-1922.45; C: dopo 2880.6)
X="if(lt(t,1226.3),847,if(lt(t,1922.45),804,if(lt(t,2880.6),847,275)))"
Y="if(lt(t,1226.3),324,if(lt(t,1922.45),50,if(lt(t,2880.6),324,254)))"
ffmpeg -y -v error -i "$SRC" -an -vf "crop=184:138:x='$X':y='$Y',scale=412:310:flags=lanczos,eq=contrast=1.04:saturation=1.03,hqdn3d=1.5:1.5:3:3,cas=0.35,format=yuv420p" -r 30 -c:v libx264 -preset veryfast -crf 12 prep/cam.mp4 && touch prep/cam.ok
