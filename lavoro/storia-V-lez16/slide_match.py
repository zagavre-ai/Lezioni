import subprocess, numpy as np, fitz, json
from PIL import Image
W,H=96,54
raw=subprocess.run(['ffmpeg','-v','error','-i','orig.mp4','-vf',f'fps=1,scale={W}:{H}:flags=area,format=gray','-f','rawvideo','-'],capture_output=True).stdout
F=np.frombuffer(raw,np.uint8).reshape(-1,H,W).astype(np.float32)
d=fitz.open('mat/slide/LEZIONE 16.pdf')
P=[]
for p in d:
    pm=p.get_pixmap(dpi=40); im=Image.frombytes('RGB',(pm.width,pm.height),pm.samples).convert('L').resize((W,H),Image.BOX); P.append(np.asarray(im,np.float32))
mask=np.ones((H,W),bool); mask[int(H*.50):,int(W*.70):]=False   # webcam+logo
res=[]
for t,f in enumerate(F):
    e=[np.abs(f[mask]-p[mask]).mean() for p in P]
    res.append((int(np.argmin(e))+1,float(min(e))))
# compress
out=[];cur=None
for t,(pg,e) in enumerate(res):
    if cur is None or pg!=cur[0]: 
        if cur: out.append(cur)
        cur=[pg,t,t,e]
    else: cur[2]=t; cur[3]=max(cur[3],e)
out.append(cur)
for o in out: print('pag',o[0],o[1],'-',o[2],'err max %.1f'%o[3])
json.dump(res,open('out/slidematch.json','w'))
