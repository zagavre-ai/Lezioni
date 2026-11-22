import re,sys
from PIL import Image,ImageDraw,ImageChops
def render(svg,width,color=(0x20,0x60,0xAF)):
    s=open(svg).read()
    vb=[float(x) for x in re.search(r'viewBox="([^"]+)"',s).group(1).split()]
    d=''.join(re.findall(r'\sd="([^"]+)"',s))
    sc=width*3/vb[2];W=int(vb[2]*sc);H=int(vb[3]*sc)
    toks=re.findall(r'[MLQCZHVmlqczhv]|-?\d+\.?\d*(?:e-?\d+)?',d)
    subs=[];cur=[];i=0;cmd=None;x=y=0
    def num():
        nonlocal i;v=float(toks[i]);i+=1;return v
    while i<len(toks):
        if re.match(r'[A-Za-z]',toks[i]):cmd=toks[i];i+=1
        if cmd=='M':
            if cur:subs.append(cur)
            x,y=num(),num();cur=[(x,y)];cmd='L'
        elif cmd=='L':x,y=num(),num();cur.append((x,y))
        elif cmd=='H':x=num();cur.append((x,y))
        elif cmd=='V':y=num();cur.append((x,y))
        elif cmd=='Q':
            cx,cy,ex,ey=num(),num(),num(),num()
            for k in range(1,9):
                t=k/8;cur.append(((1-t)**2*x+2*(1-t)*t*cx+t*t*ex,(1-t)**2*y+2*(1-t)*t*cy+t*t*ey))
            x,y=ex,ey
        elif cmd=='C':
            c1x,c1y,c2x,c2y,ex,ey=[num() for _ in range(6)]
            for k in range(1,9):
                t=k/8;cur.append(((1-t)**3*x+3*(1-t)**2*t*c1x+3*(1-t)*t*t*c2x+t**3*ex,(1-t)**3*y+3*(1-t)**2*t*c1y+3*(1-t)*t*t*c2y+t**3*ey))
            x,y=ex,ey
        elif cmd in('Z','z'):
            if cur:subs.append(cur);cur=[]
        else:raise SystemExit('cmd '+cmd)
    if cur:subs.append(cur)
    m=Image.new('1',(W,H),0)
    for p in subs:
        if len(p)<3:continue
        t=Image.new('1',(W,H),0);ImageDraw.Draw(t).polygon([(a*sc,b*sc) for a,b in p],fill=1);m=ImageChops.logical_xor(m,t)
    m=m.convert('L').resize((width,int(width*vb[3]/vb[2])),Image.LANCZOS)
    im=Image.new('RGBA',m.size,color+(0,));im.putalpha(m);return im
if __name__=='__main__':
    render(sys.argv[1],int(sys.argv[3])).save(sys.argv[2])
