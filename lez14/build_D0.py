import sys;sys.path.insert(0,'/home/user/Lezioni/lez14')
from montaggio import *
import json
B=confine(60)[0];A=0.4
K=keep(A,B);ted,tot=tmap(K);nf=round(tot*FPS)
layer=WK+'/D0_layer.mp4'
sh(['ffmpeg','-v','error','-y','-loop','1','-framerate','30','-i','/tmp/w/pezzi/COVER1_prof.png','-frames:v',str(nf),'-vf','format=yuv420p','-c:v','libx264','-preset','ultrafast','-crf','12',layer])
info=dict(K=K,layer=layer,nf=nf,tot=tot)
componi_D(info,'/tmp/w/pezzi/D0.mkv');json.dump({'durata_s':tot,'orig':[A,B],'K':K},open('/tmp/w/pezzi/D0.json','w'));print('D0',tot)
