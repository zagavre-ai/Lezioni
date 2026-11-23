import cv2,os,glob,sys
cv2.setNumThreads(3)
sr=cv2.dnn_superres.DnnSuperResImpl_create(); sr.readModel('/tmp/sr/EDSR_x4.pb'); sr.setModel('edsr',4)
for f in sorted(glob.glob('/tmp/w/l6s/img/i-*.jpg')):
    n=os.path.basename(f)[:-4]; o=f'/tmp/w/up/{n}.png'
    if os.path.exists(o): continue
    im=cv2.imread(f); out=sr.upsample(im); cv2.imwrite(o+'.tmp.png',out); os.rename(o+'.tmp.png',o); print(n,out.shape,flush=True)
open('/tmp/w/up/.fatto','w').close()
