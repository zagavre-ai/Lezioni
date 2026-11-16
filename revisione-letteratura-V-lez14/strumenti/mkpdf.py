import json,sys,os,re,subprocess
sys.path.insert(0,'/tmp/w14');sys.path.insert(0,'/tmp/w14/build')
import gen,buildd,libro
from PIL import Image
for P in (1,2):
    pages=json.load(open(f'/tmp/w14/d{P}/plan.json'))['pages']
    order=sorted(pages.items(),key=lambda kv:kv[1])
    d=f'/tmp/w14/pdfhtml/p{P}';os.makedirs(d,exist_ok=True)
    for k,pag in order:
        nm=f'{pag:02d}'
        if k in('cover',):
            h=gen.cover(f'Luigi Pirandello · Parte {P}',buildd.ARGS[P],pag=1)
        elif k=='2':
            h=gen.page(f'<div style="position:absolute;left:80px;top:146px"><div class="lab">{gen.E(buildd.label(P,2,300))}</div><div class="tit" style="margin-top:34px">Luigi Pirandello</div><div class="bar"></div></div><div class="card" style="position:absolute;left:80px;top:420px;width:380px;height:520px;padding:0;overflow:hidden"><img src="file:///tmp/w14/slide2_crop.jpg" style="width:100%;height:100%;object-fit:cover;object-position:top"></div>',pag)
        elif k in('C','B'):
            sl=libro.SL[k][0];im=Image.open(f"/tmp/w14/ingr/Lez14/screen/Lez14_p{sl['p']}.png").convert('RGB')
            cr=im.crop((sl['x0'],sl['y0'],sl['x1'],sl['y1']));kk=min(1280/cr.width,690/cr.height);cr=cr.resize((int(cr.width*kk),int(cr.height*kk)),Image.LANCZOS)
            fn=f'/tmp/w14/pdfhtml/p{P}_{k}.jpg';cr.save(fn,quality=93)
            h=gen.page(f'<div style="position:absolute;left:80px;top:146px;width:1305px"><div class="lab">{gen.E(buildd.label(P,k,3500))}</div></div><div style="position:absolute;left:80px;top:230px;width:fit-content;max-width:1305px;border:5px solid #FFE600;border-radius:22px;padding:12px;background:#fff"><img src="file://{fn}" style="display:block;border-radius:12px"></div>',pag)
        else:
            s=int(k);tx=buildd.T[str(s)];tf=300 if P==1 else 3000
            if P==1 and s in(3,4): tf=300
            h=gen.cards(buildd.label(P,s,tf),tx[1],tx[2:-1],None,pag=pag)
        h=re.sub(r'<div class="box"></div><div class="band">.*?</div></div>','',h,flags=re.S)
        open(f'{d}/{nm}.html','w',encoding='utf-8').write(h)
