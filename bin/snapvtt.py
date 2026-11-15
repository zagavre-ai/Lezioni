import sys,re,subprocess,numpy as np
V,P=sys.argv[1:3];SR=8000
x=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',V,'-vn','-ac','1','-ar','8000','-f','s16le','-'],capture_output=True).stdout,np.int16).astype(float)
e=np.convolve(x**2,np.ones(400)/400,'same');thr=np.percentile(e,60)
def ts(s):h,m,r=s.split(':');return int(h)*3600+int(m)*60+float(r)
def fm(t):return '%02d:%02d:%06.3f'%(t//3600,t%3600//60,t%60)
t=open(P).read();out=[];prev_end=0
cues=re.findall(r'(\S+) --> (\S+)\n(.+?)\n\n',t+'\n',re.S)
res=['WEBVTT','']
for a,b,tx in cues:
    a=ts(a);b=ts(b)
    i0=int(max(0,a-0.8)*SR);seg=e[i0:int((a+0.8)*SR)]
    if len(seg) and seg[:int(0.5*SR)].mean()<thr*0.5 and (seg>thr).any():
        a=max(i0/SR+np.argmax(seg>thr)/SR,prev_end+0.01)
    b=max(b,a+0.8);res+=[f'{fm(a)} --> {fm(b)}',tx,''];prev_end=b
open(P,'w').write('\n'.join(res))
print(len(cues))
