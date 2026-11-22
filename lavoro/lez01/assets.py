# Ritaglia e migliora le immagini del PDF del prof (alta risoluzione possibile: ingrandimento Lanczos + nitidezza leggera)
import sys,os,json
sys.path.insert(0,os.path.dirname(__file__))
from PIL import Image,ImageFilter,ImageDraw
SRC='/tmp/w/img/'
OUT='/tmp/w/asset/'
os.makedirs(OUT,exist_ok=True)
# nome: (file, box, [rettangoli da coprire di bianco prima del ritaglio])
IMG={
'goethe':('p-003.jpg',(0,1,700,535),[]),
'salotto':('p-007.jpg',(7,16,384,488),[]),
'newton':('p-010.jpg',(8,14,735,570),[]),
'pantheon':('p-013.jpg',(22,0,756,762),[]),
'palazzo_reale':('p-016.jpg',(0,28,851,379),[]),
'scala':('p-017.jpg',(195,11,762,374),[]),
'kedleston_aerea':('p-018.jpg',(0,0,810,372),[]),
'marble_hall':('p-020.jpg',(90,6,453,402),[]),
'saloon':('p-020.jpg',(464,6,683,402),[]),
'kedleston':('p-022.jpg',(1,0,962,295),[]),
'brandeburgo':('p-023.jpg',(16,0,1010,380),[]),
'walhalla_int':('p-025.jpg',(9,10,432,347),[]),
'walhalla_est':('p-025.jpg',(9,395,432,781),[]),
'winckelmann':('p-028.jpg',(208,33,635,637),[]),
'amore_psiche':('p-031.jpg',(30,100,717,655),[]),
'paolina':('p-033.jpg',(75,48,745,472),[]),
'tre_grazie':('p-035.jpg',(10,14,421,680),[]),
'maria_cristina':('p-037.jpg',(67,241,781,801),[(60,235,215,340)]),
'orazi':('p-040.jpg',(9,9,774,612),[]),
'pallacorda':('p-042.jpg',(0,50,563,433),[]),
'marat':('p-044.jpg',(9,18,470,600),[]),
'napoleone':('p-046.jpg',(12,14,572,686),[]),
'giove_teti':('p-049.jpg',(252,8,706,574),[]),
'odalisca':('p-051.jpg',(146,9,888,423),[]),
}
def run():
    for k,(f,box,cover) in IMG.items():
        im=Image.open(SRC+f).convert('RGB')
        d=ImageDraw.Draw(im)
        for c in cover:d.rectangle(c,fill='white')
        im=im.crop(box)
        s=max(1.0,min(3.0,1500/max(im.width,im.height)))
        if s>1.05:
            im=im.resize((int(im.width*s),int(im.height*s)),Image.LANCZOS)
            im=im.filter(ImageFilter.UnsharpMask(radius=2,percent=60,threshold=2))
        im.save(OUT+k+'.png');
        print(k,Image.open(SRC+f).crop(box).size,'->',im.size)
if __name__=='__main__':run()
