import json,sys,os,subprocess,hashlib
sys.path.insert(0,'/tmp/w14');sys.path.insert(0,'/tmp/w14/build')
import piano,gen
from PIL import Image,ImageDraw
FPS=30
T=json.load(open('/tmp/w14/pptx_text.json'))
ARGS={1:['Pirandello e la crisi del primo Novecento',"La visione del mondo e l'umorismo",'Il fu Mattia Pascal','Uno, nessuno e centomila'],
 2:['Il teatro grottesco e Il giuoco delle parti',"Sei personaggi in cerca d'autore",'Enrico IV',"L'ultima produzione e le ultime novelle",'Ciàula scopre la luna','Il treno ha fischiato']}
def label(P,slide,tf):
    """etichetta '01 · NOME' dall'argomento della slide (tf = tempo nel video della parte)"""
    if P==1:
        if slide in (2,3,4): n=1 if tf<1289.133 else 2
        elif slide==46 or slide==47: n=3
        else: n=4
    else:
        n={49:1,50:2,51:3,52:4,53:4,'C':5,'B':6}.get(slide,1)
    return f'{n:02d} · {ARGS[P][n-1].upper()}'
def pngname(key):
    return hashlib.md5(json.dumps(key,sort_keys=True).encode()).hexdigest()[:12]
def ensure_png(key,P,pages):
    kind=key['k'];nm=pngname(key);hp=f'/tmp/w14/build/html/{nm}.html'
    if os.path.exists(f'/tmp/w14/build/png/{nm}.png'): return nm
    if kind=='cover': h=gen.cover(f'Luigi Pirandello · Parte {P}',ARGS[P],pag=1)
    elif kind=='cards':
        s=key['s'];tx=T[str(s)];h=gen.cards(key['lab'],tx[1],tx[2:-1],key['c'],pag=key['pag'])
    elif kind=='foto':
        h=gen.page(f'<div style="position:absolute;left:80px;top:146px"><div class="lab">{gen.E(key["lab"])}</div><div class="tit" style="margin-top:34px">Luigi Pirandello</div><div class="bar"></div></div><div class="card" style="position:absolute;left:80px;top:420px;width:380px;height:520px;padding:0;overflow:hidden"><img src="file:///tmp/w14/slide2_crop.jpg" style="width:100%;height:100%;object-fit:cover;object-position:top"></div>',key['pag'])
    if kind=='libro':
        import libro
        from PIL import Image
        sl=libro.SL[key['n']][key['i']];im=Image.open(f"/tmp/w14/ingr/Lez14/screen/Lez14_p{sl['p']}.png").convert('RGB')
        cr=im.crop((sl['x0'],sl['y0'],sl['x1'],sl['y1']));k=min(1280/cr.width,690/cr.height);cr=cr.resize((int(cr.width*k),int(cr.height*k)),Image.LANCZOS)
        fn=f'/tmp/w14/build/libro_{nm}.jpg';cr.save(fn,quality=93)
        h=gen.page(f'<div style="position:absolute;left:80px;top:146px;width:1305px"><div class="lab">{gen.E(key["lab"])}</div></div><div style="position:absolute;left:80px;top:230px;width:fit-content;max-width:1305px;border:5px solid #FFE600;border-radius:22px;padding:12px;background:#fff;box-shadow:0 14px 40px rgba(11,21,48,.08)"><img src="file://{fn}" style="display:block;border-radius:12px"></div>',key['pag'])
    open(hp,'w',encoding='utf-8').write(h)
    return nm
def compose(P,name,fin_start,dur,off,s0,f0,f1,pages,trim_s,out):
    st=piano.stati(s0,s0+(f1-f0)/FPS)
    # durate in fotogrammi, somma esatta
    segs=[];cum=0
    for i,(a,b,s,c) in enumerate(st):
        end=f1-f0 if i==len(st)-1 else round((b-s0)*FPS)
        n=max(end-cum,0);segs.append((a,s,c,n));cum+=n
    if cum!=f1-f0: raise Exception('somma')
    lst=[];used=[]
    for a,s,c,n in segs:
        if n==0: continue
        tf=a-off
        if P==2 and s==48: s=1
        if s==1:
            pages.setdefault('cover',1);key={'k':'cover'}
        elif s==2: key={'k':'foto','lab':label(P,2,tf),'pag':pages.setdefault(2,len(pages)+1)}
        elif s in ('C','B'): key={'k':'libro','n':s,'i':c,'lab':label(P,s,tf),'pag':pages.setdefault(s,len(pages)+1)}
        else: key={'k':'cards','s':s,'c':c,'lab':label(P,s,tf),'pag':pages.setdefault(s,len(pages)+1)}
        nm=ensure_png(key,P,pages);lst.append((nm,n));used.append((a,s,c,n))
    return lst,used
if __name__=='__main__':
    pass
