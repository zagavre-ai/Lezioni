# Audio finale esatto: ogni pezzo decodificato e portato a frame*1600 campioni, poi unito e codificato AAC 192k 48 kHz.
import sys, re, subprocess, os, numpy as np
sys.path.insert(0,'/home/user/Lezioni/lavoro')
from mont import sh
def fatto(lista,out_m4a):
    P=re.findall(r"file '(.+)'",open(lista).read());parts=[]
    for p in P:
        n=int(sh(['ffprobe','-v','error','-count_packets','-select_streams','v:0','-show_entries','stream=nb_read_packets','-of','csv=p=0',p]).stdout.strip())
        x=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',p,'-vn','-ac','1','-ar','48000','-f','f32le','-'],capture_output=True).stdout,np.float32)
        N=n*1600
        x=x[:N] if len(x)>=N else np.concatenate([x,np.zeros(N-len(x),np.float32)])
        parts.append(x)
    y=np.concatenate(parts);tmp=out_m4a+'.raw'
    y.tofile(tmp)
    sh(['ffmpeg','-v','error','-y','-f','f32le','-ar','48000','-ac','1','-i',tmp,'-c:a','aac','-b:a','192k','-ar','48000',out_m4a]);os.remove(tmp)
    return len(y)/48000
if __name__=='__main__':
    print(fatto(sys.argv[1],sys.argv[2]))
