import sys,subprocess,os
sys.path.insert(0,'/home/claude/w/b')
from lib import *
NOTE="© Centro Studi Telesio. Tutti i contenuti riprodotti in questa videolezione (testi, grafiche, animazioni, voci e registrazioni) sono di\nproprietà del Centro Studi Telesio. È vietata la riproduzione, anche parziale, senza autorizzazione scritta."
open(B+'/avviso.txt','w').write(NOTE)
ff('-i',KIT+'/sigle/Sigla_Storia_15s.mp4','-c:v','libx264','-preset','veryfast','-crf','14','-pix_fmt','yuv420p','-r','30','-c:a','pcm_s16le','-ar','48000','-ac','2',B+'/sc/sigla.mkv')
L=NOTE.split("\n")
for i,l in enumerate(L): open(B+f"/av{i}.txt","w").write(l)
vf="drawbox=x=150:y=850:w=1620:h=140:color=black:t=fill"+"".join(f",drawtext=fontfile=/root/.fonts/Figtree-Regular.ttf:textfile={B}/av{i}.txt:fontcolor=white:fontsize=24:x=(w-text_w)/2:y={895+i*36}" for i in range(2))
ff('-i',KIT+'/sigle/Sigla_finale_5s_con_avviso_diritti.mp4','-vf',vf,'-c:v','libx264','-preset','veryfast','-crf','14','-pix_fmt','yuv420p','-r','30','-c:a','pcm_s16le','-ar','48000','-ac','2',B+'/sc/sigla_fin.mkv')
print('ok')
