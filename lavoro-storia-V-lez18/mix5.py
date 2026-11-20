import json,subprocess,numpy as np,os,sys
import sys;P=sys.argv[1]
W='/tmp/L18';SR=48000
SEG=json.load(open(W+'/seg_P'+P+'.json'))
tot=sum(s['frames'] for s in SEG)/30.0
A=np.zeros((int(tot*SR)+SR,2),np.float32)
def load(p):
    r=subprocess.run(['ffmpeg','-v','error','-i',p,'-f','f32le','-ac','2','-ar',str(SR),'-'],capture_output=True,check=True).stdout
    return np.frombuffer(r,np.float32).reshape(-1,2)
cache={}
t=0.0
for s in SEG:
    st=s['start']
    for tr,p,g in s['aud']:
        if p not in cache:cache[p]=load(p)
        x=cache[p];o=int(round((st+tr)*SR))
        if o<0:x=x[-o:];o=0
        n=min(len(x),len(A)-o)
        # i campioni oltre la fine del segmento (+3 s) restano: servono alle code dei jingle
        A[o:o+n]+=x[:n]*g
n=int(tot*SR);A=A[:n]
print('picco prima del limiter',20*np.log10(np.abs(A).max()))
open(W+'/audio_raw_'+P+'.f32','wb').write(A.tobytes())
subprocess.run(['ffmpeg','-y','-v','error','-f','f32le','-ar',str(SR),'-ac','2','-i',W+'/audio_raw_'+P+'.f32','-af','alimiter=limit=0.89:level=false:attack=5:release=50','-ac','2',W+'/audio_full_'+P+'.wav'],check=True)
print('totale',tot)
