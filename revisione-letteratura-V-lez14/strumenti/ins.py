import json,re,sys,os,subprocess
sys.path.insert(0,'/tmp/w14');sys.path.insert(0,'/tmp/w14/build')
import gen
from evid import ricostruisci
E=gen.E
VOCI={x['nome']:x['testo'] for x in json.load(open('/tmp/w14/voci/scambio/letteratura-V-lez14/testi_voci.json'))}
norm=lambda w:re.sub(r'[^a-zàèéìòù]','',w.lower())
def sentences(t): return [s.strip() for s in re.split(r'(?<=[.?!])\s+',t.strip()) if s.strip()]
def reveal_html(eyebrow,title,items,k,pag=None,two=False):
    n=len(items);fs=30 if n<=4 else (27 if n<=6 else 24)
    body=f'<div style="position:absolute;left:80px;top:146px;width:1760px"><div class="lab">{E(eyebrow)}</div><div class="tit" style="margin-top:34px;font-size:{58 if len(title)>48 else 64}px">{E(title)}</div><div class="bar"></div>'
    body+=f'<div style="margin-top:40px;display:grid;grid-template-columns:{"1fr 1fr" if n>4 else "1fr"};gap:18px 24px">'
    for i,t in enumerate(items):
        if i<k:
            on=' on' if i==k-1 else ''
            body+=f'<div class="card nc{on}" style="font-size:{fs}px;padding-top:18px;padding-bottom:18px"><div class="n">{i+1}</div><div>{gen.rich(t,False)}</div></div>'
    body+='</div></div>'
    return gen.page(body,pag,prof=False)
def times(P,name,items):
    """tempi di comparsa (secondi relativi al pezzo) di ogni frase, dalle parole del video vecchio"""
    TL=json.load(open(f'/tmp/w14/tl{P}.json'));a,d=[(a,d) for n,a,d in TL if n==name][0]
    W=[(t-a,norm(w)) for t,w in ricostruisci(json.load(open(f'/tmp/w14/tr/P{P}.json'))) if a-0.2<=t<a+d+0.5]
    res=[];j=0
    for s in items:
        f=norm(s.split()[0])[:4];found=None
        for q in range(j,len(W)):
            if W[q][1][:4]==f: found=W[q][0];j=q+1;break
        res.append(found if found is not None else (res[-1]+3 if res else 1.0))
    return res,d
def build(P,name,vname,kind):
    txt=VOCI[vname];S=sentences(txt)
    if kind=='S':
        title=S[0].rstrip('.');i=[x for x,s in enumerate(S) if 'punti da ricordare' in s][0];items=S[i+1:];eyebrow='SCHEMA DI RIPASSO'
    elif kind=='GL':
        title='Il glossario della lezione';items=[s for s in S if ':' in s[:40] and not s.startswith('Ricorda')];eyebrow='PAROLE CHIAVE'
    else:
        title='Ricapitoliamo la lezione';items=[s for s in S if 'argomento:' in s[:20]];eyebrow='RIPASSO FINALE'
    if kind=='GL' or kind=='RF': pass
    t,d=times(P,name,items)
    return eyebrow,title,items,t,d
if __name__=='__main__':
    ENC=['-c:v','libx264','-preset','veryfast','-crf','19','-pix_fmt','yuv420p','-r','30','-an','-x264-params','keyint=60:scenecut=0','-threads','2']
    PAG={1:7,2:9};made=[]
    for P in (1,2):
        TL=json.load(open(f'/tmp/w14/tl{P}.json'));os.makedirs(f'/tmp/w14/new{P}',exist_ok=True)
        pg=PAG[P]
        for n,a,d in TL:
            if re.fullmatch(r'S\d',n): kind,vn='S',('' if P==1 else 'B')+n
            elif n=='GL1': kind,vn='GL',('' if P==1 else 'B')+'GL1'
            elif n=='RF1': kind,vn='RF',('' if P==1 else 'B')+'RF1'
            else: continue
            ey,ti,items,t,dd=build(P,n,vn,kind)
            nf=round((a+d)*30)-round(a*30);cum=0;parts=[]
            bounds=[0]+[round(x*30) for x in t]+[nf]
            # stati: 0 = solo titolo fino a t0; k = k carte
            for k in range(len(items)+1):
                f0=bounds[k];f1=bounds[k+1] if k<len(items) else nf
                if k<len(items): f1=bounds[k+1]
                nm=f'ins_{P}_{n}_{k}';gen.scrivi(nm,reveal_html(ey,ti,items,k,pg if k==len(items) else pg));parts.append((nm,max(f1-f0,0)))
            made.append((P,n,parts,nf,pg));pg+=1
    subprocess.run(['node','/tmp/w14/build/render.js','/tmp/w14/build/html','/tmp/w14/build/png'],check=True)
    for P,n,parts,nf,pg in made:
        out=f'/tmp/w14/new{P}/{n}.mp4';L=f'/tmp/w14/build/lins_{P}_{n}.txt';segs=[]
        for i,(nm,k) in enumerate(parts):
            if k<=0: continue
            po=f'/tmp/w14/build/ins_{P}_{n}_{i}.mp4'
            subprocess.run(['ffmpeg','-v','error','-y','-loop','1','-framerate','30','-t',f'{k/30:.4f}','-i',f'/tmp/w14/build/png/{nm}.png','-frames:v',str(k),*ENC,po],check=True);segs.append(po)
        open(L,'w').write(''.join(f"file '{s}'\n" for s in segs))
        subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',L,'-c','copy',out],check=True)
        print(P,n,[k for _,k in parts],sum(k for _,k in parts),nf,flush=True)
