import sys,os
sys.path.insert(0,'/home/user/Lezioni/storia_s7')
from ins import *
from spec18 import *
W='/tmp/w18/w'
c=Ctx('l18',W,'/tmp/w18/scambio/storia-V-lez18/vox',{},{})
out={}
# sigla (15 s) e sigla finale (ultimi 5 s)
sig='/home/user/Lezioni/kit/sigle/Sigla_Storia_15s.mp4'
def enc(src,dst,ss=None,t=None):
    cmd=['ffmpeg','-y','-v','error']+(['-ss',str(ss)] if ss is not None else [])+['-i',src]+(['-t',str(t)] if t else [])+['-vf','fps=30,scale=1920:1080,format=yuv420p','-af','aresample=48000,apad','-c:v','libx264','-preset','veryfast','-crf','14','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-shortest',dst]
    run(cmd)
if not os.path.exists(W+'/pc/SIGLA.mp4'):
    enc(sig,W+'/pc/SIGLA.mp4');enc(sig,W+'/pc/SFIN.mp4',ss=10,t=5)
for n in ('SIGLA','SFIN'):out[n]=dur(f'{W}/pc/{n}.mp4')
r=build_pausa(c,'VER','Pausa del video · Verifica','Verifica finale',TITOLO,'Test finale della lezione','trans.wav');out['VER']=r[1]
r=build_pausa(c,'COMP','Pausa del video · Compiti','Compiti','Ora tocca a te','','trans.wav');out['COMP']=r[1]
p=c.png('l18_CINTRO',doc(f'''{logo(True)}<div class="abs kick" style="left:150px;top:380px">Storia · Quinto anno</div><h1 class="abs" style="left:150px;top:440px;font-size:140px">I compiti</h1><div class="abs" style="left:150px;top:640px;font-family:BG;font-weight:800;font-size:54px;color:#5DA3F0">Ora tocca a te</div>''','bg-d'))
r=c.piece('CINTRO',[(p,3.7)],[(SND+'trans.wav',0,0.7)],3.7);out['CINTRO']=r[1]
import json;json.dump(out,open('/tmp/w18/fixed_dur.json','w'));print(out)
c.S.close()
