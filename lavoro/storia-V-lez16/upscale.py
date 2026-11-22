import cv2,sys
sr=cv2.dnn_superres.DnnSuperResImpl_create();sr.readModel('/home/user/w/models/EDSR_x4.pb');sr.setModel('edsr',4)
for n in sys.argv[1:]:
    im=cv2.imread(n);o=sr.upsample(im)
    # nitidezza leggera
    b=cv2.GaussianBlur(o,(0,0),1.2);o=cv2.addWeighted(o,1.35,b,-0.35,0)
    cv2.imwrite(n.replace('.png','_x4.png'),o);print(n,im.shape,'->',o.shape,flush=True)
