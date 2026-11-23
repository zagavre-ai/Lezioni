#!/usr/bin/env python3
# ingrandimento di qualità x4 (EDSR) + pulizia leggera: migliora.py in_dir out_dir
import sys,os,glob,cv2
cv2.setNumThreads(2)
sr=cv2.dnn_superres.DnnSuperResImpl_create(); sr.readModel('/tmp/EDSR_x4.pb'); sr.setModel('edsr',4)
os.makedirs(sys.argv[2],exist_ok=True)
for f in sorted(glob.glob(sys.argv[1]+'/*.png')):
    o=os.path.join(sys.argv[2],os.path.basename(f))
    if os.path.exists(o): continue
    im=cv2.imread(f); out=sr.upsample(im); cv2.imwrite(o,out); print(o,out.shape,flush=True)
