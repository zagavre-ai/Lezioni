import sys,os,subprocess
sys.path.insert(0,'/home/user/Lezioni/tools'); sys.path.insert(0,'/home/user/Lezioni/lez12')
import tts_prov
from voci import VOCI
for k,v in VOCI.items():
    o=f'vox_prov/{k}.wav'
    if os.path.exists(o): continue
    d=tts_prov.sintetizza(v.replace('«','').replace('»',''),f'/tmp/{k}_raw.wav',speed=1.0)
    subprocess.run(['ffmpeg','-v','error','-y','-i',f'/tmp/{k}_raw.wav','-ar','48000','-ac','1',o],check=True)
    print(k,round(d,1),flush=True)
