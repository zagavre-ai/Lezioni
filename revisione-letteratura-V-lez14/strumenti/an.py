import json,re,sys,os,subprocess,math,collections
sys.path.insert(0,'/tmp/w14');sys.path.insert(0,'/tmp/w14/build')
import gen
from rapidocr_onnxruntime import RapidOCR
E=gen.E
# vocabolario dal materiale della lezione
txt=' '.join(x['testo'] for x in json.load(open('/tmp/w14/voci/scambio/letteratura-V-lez14/testi_voci.json')))
for v in json.load(open('/tmp/w14/pptx_text.json')).values(): txt+=' '+' '.join(v)
for n in('orig','P1','P2'): txt+=' '+' '.join(s['testo'] for s in json.load(open(f'/tmp/w14/tr/{n}.json')))
txt+=' '+open('/tmp/w14/disp1.txt',encoding='utf-8').read()+open('/tmp/w14/disp2.txt',encoding='utf-8').read()
def nn(w): return re.sub(r'[^a-z]','',w.lower().replace('à','a').replace('è','e').replace('é','e').replace('ì','i').replace('ò','o').replace('ù','u'))
cnt=collections.Counter();surf={}
for w in re.findall(r"[A-Za-zÀ-ÿ]+",txt):
    k=nn(w);cnt[k]+=1
    if k not in surf or (any(c in w for c in 'àèéìòù') and not any(c in surf[k] for c in 'àèéìòù')): surf[k]=w.lower() if not w[0].isupper() else w
tot=sum(cnt.values())
def seg(s):
    s0=nn(s);n=len(s0);best=[(0,0)]+[(1e9,0)]*n
    for i in range(1,n+1):
        for j in range(max(0,i-22),i):
            w=s0[j:i]
            if w in cnt: c=best[j][0]-math.log(cnt[w]/tot)
            elif len(w)==1 and w in 'aeoiu': c=best[j][0]+9
            else: c=best[j][0]+14+3*len(w)
            if c<best[i][0]: best[i]=(c,j)
    out=[];i=n
    while i>0: j=best[i][1];out.append(s0[j:i]);i=j
    return list(reversed(out))
def fixtok(t):
    # token: lettere con eventuale punteggiatura attaccata
    m=re.match(r"^([^A-Za-zÀ-ÿ]*)([A-Za-zÀ-ÿ']+)([^A-Za-zÀ-ÿ]*)$",t)
    if not m: return t
    a,w,b=m.groups()
    if "'" in w:
        p=w.split("'");return a+"'".join(fixtok(x) if x else x for x in p)+b
    k=nn(w)
    if k in cnt and len(k)<=14: return a+(w if re.search('[àèéìòù]',w) else surf.get(k,w) if w.islower() else w)+b
    parts=seg(w)
    pr=[surf.get(p,p) for p in parts]
    if w[0].isupper(): pr[0]=pr[0][:1].upper()+pr[0][1:]
    return a+' '.join(pr)+b
def fixline(l): return ' '.join(fixtok(t) for t in l.split())
if __name__=='__main__':
    o=RapidOCR();res={}
    for P in (1,2):
        TL=json.load(open(f'/tmp/w14/tl{P}.json'))
        for n,a,d in TL:
            if not re.fullmatch(r'AN\d\d',n): continue
            if (P==1 and n in('AN03','AN06','AN09','AN11','AN12')) or (P==2 and n in('AN02','AN04','AN06','AN08','AN10','AN12','AN13')): continue
            scr=[]
            for k in (0,1):
                f=f'/tmp/w14/ocr/{P}_{n}_{k}.jpg'
                r,_=o(f);L=[(int(b[0][0]),int(b[0][1]),int(b[2][1]-b[0][1]),t) for b,t,c in r]
                title=[t for x,y,h,t in L if y<200 and 'APPROF' not in t][0]
                cols=collections.defaultdict(list)
                for x,y,h,t in L:
                    if y>=250: cols[round(x/500)].append((y,h,t))
                cards=[]
                for c in sorted(cols):
                    ls=sorted(cols[c]);label=ls[0][2];rest=ls[1:]
                    hs=[h for y,h,t in rest]
                    th=max(hs) if hs else 0
                    tt=[t for y,h,t in rest if h>=th*0.85 and h>=40][:3]
                    bd=[t for y,h,t in rest if not(h>=th*0.85 and h>=40)]
                    cards.append({'label':fixline(label.title() if label.isupper() else label).upper(),'title':fixline(' '.join(tt)),'body':fixline(' '.join(bd))})
                scr.append({'title':fixline(title),'cards':cards})
            res[f'{P}_{n}']=scr
            print(P,n,scr[0]['title'],'|',[c['title'] for c in scr[0]['cards']],'|',[c['title'] for c in scr[1]['cards']],flush=True)
    json.dump(res,open('/tmp/w14/an_cards.json','w'),ensure_ascii=False,indent=1)
