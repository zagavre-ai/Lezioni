# fettine dalle pagine HD: righe OCR -> blocchi tagliati su righe bianche
import json,re
from PIL import Image
o=json.load(open('/tmp/w14/ocr_hd.json'))
NOV={'C':[526,527,528,529,530,531],'B':[533,534,535,536,537,538]}
def lines(p):
    v=o[f'Lez14_p{p}.png'];L=[]
    for b,t in v:
        xs=[q[0] for q in b];ys=[q[1] for q in b]
        L.append((min(ys),max(ys),min(xs),max(xs),t))
    L.sort();return L
def slices(p,maxh=620):
    im=Image.open(f'/tmp/w14/ingr/Lez14/screen/Lez14_p{p}.png');W,H=im.size
    L=[l for l in lines(p) if 150<l[0]<H-130 and (l[3]-l[2])>200 and (l[1]-l[0])>=36]   # via intestazione e piede
    # righe della colonna principale: cerco i salti verticali piu grandi
    out=[];cur=[]
    for l in L:
        if cur and (l[0]-cur[-1][1]>34 and l[1]-cur[0][0]>maxh*0.55 or l[1]-cur[0][0]>maxh): out.append(cur);cur=[]
        cur.append(l)
    if cur: out.append(cur)
    S=[]
    for c in out:
        y0=max(0,min(l[0] for l in c)-14);y1=min(H,max(l[1] for l in c)+14)
        xs=[(l[2],l[3]) for l in c if l[3]-l[2]>300]
        if not xs: continue
        x0=min(a for a,b in xs)-30;x1=max(b for a,b in xs)+30
        if p>=533 and len(S)+len(out)>=0: pass
        S.append({'p':p,'y0':int(y0),'y1':int(y1),'x0':int(max(0,x0)),'x1':int(min(W,x1)),'testo':' '.join(l[4] for l in c)})
    return S
if __name__=='__main__':
    for n,ps in NOV.items():
        tot=0
        for p in ps:
            s=slices(p);tot+=len(s);print(n,p,len(s),[ (x['y1']-x['y0']) for x in s])
