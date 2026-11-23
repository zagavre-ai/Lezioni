import subprocess,numpy as np,json,sys
src=sys.argv[1]; W,H=1092,614
p=subprocess.Popen(['ffmpeg','-v','error','-i',src,'-vf','fps=4,format=gray','-f','rawvideo','-'],stdout=subprocess.PIPE,bufsize=W*H*8)
prev=None;out=[];i=0
while True:
    b=p.stdout.read(W*H)
    if len(b)<W*H:break
    f=np.frombuffer(b,np.uint8).reshape(H,W).astype(np.int16)
    if prev is not None:
        d=np.abs(f-prev)>10
        tot=d.mean()
        cols=d.sum(axis=0);rows=d.sum(axis=1)
        cx=np.where(cols>6)[0];cy=np.where(rows>6)[0]
        out.append([round(i/4,2),round(float(tot),4),int(cx.min()) if len(cx) else -1,int(cx.max()) if len(cx) else -1,int(cy.min()) if len(cy) else -1,int(cy.max()) if len(cy) else -1])
    prev=f;i+=1
json.dump(out,open('camtrack.json','w'))
