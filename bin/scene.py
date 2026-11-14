import sys,subprocess,numpy as np,json
src,out=sys.argv[1],sys.argv[2]
W,H=160,90
p=subprocess.run(['ffmpeg','-v','error','-i',src,'-vf','fps=2,crop=800:614:0:0,scale=%d:%d,format=gray'%(W,H),'-f','rawvideo','-'],capture_output=True)
a=np.frombuffer(p.stdout,np.uint8).reshape(-1,H,W).astype(np.int16)
d=np.abs(np.diff(a,axis=0)).mean(axis=(1,2))
ch=[(round((i+1)/2,1),round(float(v),1)) for i,v in enumerate(d) if v>6]
json.dump(ch,open(out,'w'));print(len(a),ch)
