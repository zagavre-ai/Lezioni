"""Prepara le immagini delle mappe in img/*.jpg (nitide, ritagliate dalle didascalie)."""
import os,sys
import numpy as np
from PIL import Image, ImageFilter
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from crops import photo_blocks
HERE=os.path.dirname(os.path.abspath(__file__)); OUT=f'{HERE}/img'; os.makedirs(OUT,exist_ok=True)
SL='/tmp/w/l6s/img'; UP='/tmp/w/up'
def trim(im,th=236):
    a=np.array(im.convert('RGB')); m=(a.min(axis=2)<th)
    rows=np.where(m.mean(axis=1)>0.5)[0]; cols=np.where(m.mean(axis=0)>0.5)[0]
    if len(rows)==0 or len(cols)==0: return im
    return im.crop((cols[0]+1,rows[0]+1,cols[-1],rows[-1]))
def enhance(im,maxside=1400):
    s=min(maxside/max(im.size),4.0)
    im=im.resize((max(1,int(im.width*s)),max(1,int(im.height*s))),Image.LANCZOS)
    return im.filter(ImageFilter.UnsharpMask(radius=2,percent=60,threshold=2))
def from_slide(num,block):
    """block = indice del blocco foto in photo_blocks; usa la versione EDSR 4x se pronta, altrimenti Lanczos."""
    p=f'{SL}/i-{num}.jpg'; b=photo_blocks(p)[block]; up=f'{UP}/i-{num}.png'
    if os.path.exists(up):
        im=Image.open(up).convert('RGB'); k=4; src='EDSR 4x'
        im=im.crop((b[0]*k+8,b[1]*k+8,b[2]*k-8,b[3]*k-8))
        im.thumbnail((1400,1400),Image.LANCZOS); return im,src
    im=Image.open(p).convert('RGB').crop((b[0]+2,b[1]+2,b[2]-2,b[3]-2)); return enhance(im),'Lanczos'
def from_raw(n):
    im=trim(Image.open(f'{HERE}/raw_{n}.png').convert('RGB')); return enhance(im),'Lanczos (da raster della mappa)'
SPEC={'metro':lambda:from_slide('008',0),'palsec':lambda:from_slide('015',0),'bacio':lambda:from_slide('017',0),
      'sagrada':lambda:from_slide('025',1),
      'guell':lambda:from_raw('guell'),'stoclet':lambda:from_raw('stoclet'),'adele':lambda:from_raw('adele'),
      'toulouse':lambda:from_raw('toulouse'),'mucha':lambda:from_raw('mucha'),'morris':lambda:from_raw('morris')}
if __name__=='__main__':
    for k,f in SPEC.items():
        im,src=f(); im.save(f'{OUT}/{k}.jpg',quality=93); print(k,im.size,src)
