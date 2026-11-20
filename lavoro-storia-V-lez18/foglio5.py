import json,subprocess,sys
from PIL import Image,ImageDraw,ImageFont
P=int(sys.argv[1]);V=sys.argv[2];OUT=sys.argv[3]
TL=json.load(open(f'/tmp/L18/timeline_P{P}.json'));T={n:(s,d) for n,s,d in TL}
FONT=ImageFont.truetype('/tmp/L18/str/font/Figtree-Bold.ttf',26)
ks=range(1,5) if P==1 else range(5,10)
items=[]
if P==2:items.append(('Ripasso Parte 1 (intro)',T['RIP'][0]+1.2));items.append(('Ripasso Parte 1 (didascalia)',T['RIP'][0]+T['RIP'][1]*0.4))
for k in ks:items.append((f'Titolo {k}',T[f'T{k}'][0]+3.2))
for k in ks:
    s,d=T[f'P{k}'];items+= [(f'Pillola {k} · intro',s+1.2),(f'Pillola {k} · didascalia',s+d*0.55)]
for k in ks:items.append((f'Quiz {k}',T[f'Q{k}'][0]+3.5))
s,d=T[f'RIEP{P}'];items.append(('Riepilogo · ultimo fotogramma',s+d-0.9))
ims=[]
for i,(l,t) in enumerate(items):
    p=f'/tmp/L18/fg_{i}.jpg';subprocess.run(['ffmpeg','-y','-v','error','-ss',f'{t:.3f}','-i',V,'-frames:v','1','-vf','scale=640:-1',p],check=True);ims.append((l,Image.open(p)))
cols=4;w,h=640,360;rows=(len(ims)+cols-1)//cols
S=Image.new('RGB',(cols*w,rows*(h+40)),'white');d=ImageDraw.Draw(S)
for i,(l,im) in enumerate(ims):
    x=(i%cols)*w;y=(i//cols)*(h+40);S.paste(im,(x,y+40));d.text((x+8,y+6),l,fill='#B00020',font=FONT)
S.save(OUT);print(len(ims))
