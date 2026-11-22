import json,sys,os,re,glob,shutil,subprocess
sys.path.insert(0,'/tmp/w14');sys.path.insert(0,'/tmp/w14/build')
import gen,buildd,libro
from PIL import Image
shutil.rmtree('/tmp/w14/pdfq',ignore_errors=True)
STRIP=lambda h:re.sub(r'<div class="box"></div><div class="band">.*?</div></div>','',h,flags=re.S).replace('&nbsp;·&nbsp; Prof. Giorgio Mazzotti','')
for P in (1,2):
    pages=json.load(open(f'/tmp/w14/dq{P}/plan.json'))['pages'];d=f'/tmp/w14/pdfq/p{P}';os.makedirs(d,exist_ok=True)
    for k,pag in pages.items():
        if k=='cover': h=gen.cover(f'Luigi Pirandello · Parte {P}',buildd.ARGS[P],pag=1)
        elif k in('dcpA','dcpB'):
            pr=0 if k=='dcpA' else 1;its=buildd.ARGS[P][0:2] if pr==0 else buildd.ARGS[P][2:4]
            h=gen.cards('LETTERATURA ITALIANA V · VIDEOLEZIONE','Di cosa parliamo',its,None,pag=pag,start=0 if pr==0 else 2)
        elif k=='2':
            h=gen.page(f'<div style="position:absolute;left:80px;top:146px"><div class="lab">{gen.E(buildd.label(P,2,300))}</div><div class="tit" style="margin-top:34px">Luigi Pirandello</div><div class="bar"></div></div><div class="card" style="position:absolute;left:80px;top:420px;width:380px;height:520px;padding:0;overflow:hidden"><img src="file:///tmp/w14/slide2_crop.jpg" style="width:100%;height:100%;object-fit:cover;object-position:top"></div>',pag)
        elif k in('C','B'):
            sl=libro.SL[k][0];im=Image.open(f"/tmp/w14/ingr/Lez14/screen/Lez14_p{sl['p']}.png").convert('RGB')
            cr=im.crop((sl['x0'],sl['y0'],sl['x1'],sl['y1']));kk=min(1280/cr.width,690/cr.height);cr=cr.resize((int(cr.width*kk),int(cr.height*kk)),Image.LANCZOS)
            fn=f'/tmp/w14/pdfq/p{P}_{k}.jpg';cr.save(fn,quality=93)
            h=gen.page(f'<div style="position:absolute;left:80px;top:146px;width:1305px"><div class="lab">{gen.E(buildd.label(P,k,3500))}</div></div><div style="position:absolute;left:80px;top:230px;width:fit-content;max-width:1305px;border:5px solid #FFE600;border-radius:22px;padding:12px;background:#fff"><img src="file://{fn}" style="display:block;border-radius:12px"></div>',pag)
        else:
            s,pt=k.split('_');s=int(s);pt=int(pt);tx=buildd.T[str(s)];its=tx[2:-1];sub=its[0:2] if pt==0 else its[2:3]
            h=gen.cards(buildd.label(P,s,300 if P==1 else 3000),tx[1],sub,None,pag=pag,start=0 if pt==0 else 2)
        open(f'{d}/{pag:02d}.html','w',encoding='utf-8').write(STRIP(h))
    best={}
    for f in glob.glob(f'/tmp/w14/build/html/ins_{P}_*.html')+glob.glob(f'/tmp/w14/build/html/an_{P}_*.html'):
        b=os.path.basename(f)[:-5];m=re.match(r'(ins|an)_(\d)_(\w+)_(\d+)$',b);key=(m.group(1),m.group(3));k=int(m.group(4))
        if key not in best or k>best[key][0]: best[key]=(k,f)
    for key,(k,f) in best.items():
        t=open(f,encoding='utf-8').read();pg=int(re.search(r'Pagina (\d+)',t).group(1));open(f'{d}/{pg:02d}.html','w',encoding='utf-8').write(STRIP(t))
