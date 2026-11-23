import cv2,glob,os
sr=cv2.dnn_superres.DnnSuperResImpl_create();sr.readModel('/tmp/claude-0/w/EDSR_x2.pb');sr.setModel('edsr',2)
os.makedirs('/tmp/claude-0/w/lez07/opere2',exist_ok=True)
for f in sorted(glob.glob('/tmp/claude-0/w/lez07/img/opere/*.png')):
    o='/tmp/claude-0/w/lez07/opere2/'+os.path.basename(f)
    if os.path.exists(o):continue
    im=cv2.imread(f);r=sr.upsample(im)
    cv2.imwrite(o,r);print(f,im.shape,r.shape,flush=True)
open('/tmp/claude-0/w/lez07/upscale.fatto','w').write('ok')
