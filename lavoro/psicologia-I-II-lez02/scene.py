import subprocess,numpy as np,json
# titolo della slide (fascia alta) a 1 fps → istanti di cambio slide
r=subprocess.run(['ffmpeg','-v','error','-i','orig/lez1.mp4','-vf','fps=1,crop=1092:90:0:0,scale=273:22,format=gray','-f','rawvideo','-'],capture_output=True)
a=np.frombuffer(r.stdout,np.uint8).reshape(-1,22,273).astype(float)
d=np.abs(np.diff(a,axis=0)).mean(axis=(1,2))
ch=[(i+1,round(x,1)) for i,x in enumerate(d) if x>3]
print(ch)
json.dump(ch,open('scene.json','w'))
