# sottotitoli .vtt del docente dalla trascrizione (Whisper base), nomi corretti. uso: subs.py LEZ_DIR PARTE
import sys,os,json,re,glob,difflib,importlib.util
sys.path.insert(0,'/home/user/lav/tools')
from lib import pulisci
import pdfplumber
L=os.path.abspath(sys.argv[1]);P=int(sys.argv[2]);O=L+'/p%d/'%P
TL=json.load(open(O+'timeline.json'));DM=json.load(open(O+'docmap.json'));R=json.load(open(L+'/asr12.json'))
spec=importlib.util.spec_from_file_location('dati',L+'/lav/dati.py');dati=importlib.util.module_from_spec(spec);spec.loader.exec_module(dati)
txt=' '.join((pg.extract_text() or '') for pg in pdfplumber.open(glob.glob(L+'/LEZIONE*.pdf')[0]).pages)
for v in dati.ARG.values():txt+=' '+v[0]+' '.join(c[0] for c in v[2])
VOC=set(w for w in re.findall(r"[A-Za-zÀ-ú'’-]+",txt) if len(w)>=4)
low={w.lower():w for w in VOC}
FIX={'autone':'Ottone','autoni':'Ottoni','ottoni':'Ottoni','fragmentazione':'frammentazione','renascita':'rinascita','promano':'romano','regenerà':'rigenera','viscovi':'vescovi','vescovi':'vescovi','vesco':'vescovo','unghari':'Ungari','ungari':'Ungari','fèudi':'feudi','feutatario':'feudatario','fedotari':'feudatari','bizzantina':'bizantina','bizantino':'bizantino','byzantino':'bizantino','crisonità':'cristianità'}
def corr(t):
    t=pulisci(t);t=re.sub(r"\b8 ?(tonne|toni|tone)\b","Ottone",t);t=re.sub(r"\b(\d{3,4})\.000\b",r"\1",t)
    out=[]
    for w in t.split(' '):
        m=re.match(r"^([^A-Za-zÀ-ú]*)([A-Za-zÀ-ú'’-]+)(.*)$",w)
        if m and len(m.group(2))>=7 and "'" not in m.group(2):
            a,c,z=m.groups();k=c.lower()
            if k in FIX:c=FIX[k]
            elif k not in low:
                mt=difflib.get_close_matches(k,low.keys(),1,0.86)
                if mt:c=low[mt[0]]
            w=a+c+z
        out.append(w)
    return ' '.join(out)
def ts(t):h=int(t//3600);m=int(t%3600//60);s=t%60;return '%02d:%02d:%06.3f'%(h,m,s)
def blocks(a,b,t):
    w=t.split();out=[];cur=[]
    for x in w:
        if len(' '.join(cur+[x]))>38 and cur:out.append(cur);cur=[]
        cur.append(x)
    if cur:out.append(cur)
    # coppie di righe -> un blocco
    bl=[out[i:i+2] for i in range(0,len(out),2)];n=sum(len(' '.join(l)) for g in bl for l in g) or 1
    res=[];t0=a
    for g in bl:
        L_=sum(len(' '.join(l)) for l in g);d=(b-a)*L_/n
        res.append((t0,t0+d,'\n'.join(' '.join(l) for l in g)));t0+=d
    return res
import numpy as np,pk_asr
X=pk_asr.load(L+'/doc.wav');H=320
EN=np.array([np.sqrt(np.mean(X[i:i+H]**2)+1e-12) for i in range(0,len(X)-H,H)]);THR=max(np.percentile(EN,60)*1.0,0.006)
def trim(a,b):
    i0,i1=int(a/0.02),int(b/0.02);v=np.where(EN[i0:i1]>THR)[0]
    if len(v)==0:return a,b
    return a+max(0,v[0]-1)*0.02,a+(v[-1]+1)*0.02
def onsets(a,b):
    i0,i1=int(a/0.02),int(b/0.02);v=EN[i0:i1]>THR;o=[];sil=0
    for j in range(len(v)):
        if v[j]:
            if sil>=6:o.append(a+j*0.02)
            sil=0
        else:sil+=1
    return o
lines=['WEBVTT','']
cues=[]
for name,st,d in TL:
    if name not in DM:continue
    s0,s1=DM[name]
    for a,b,t in R:
        if a>=s0-0.01 and a<s1 and t.strip():
            ta,tb=trim(a,min(b,s1));fa=st+(ta-s0);fb=min(st+(tb-s0),st+d)
            bl=blocks(fa,fb,corr(t));on=[o-0.04 for o in onsets(ta,tb)];on=[st+(o+0.04-s0) for o in on]
            for k,(x,y,tx) in enumerate(bl):
                if k>0 and on:
                    n=min(on,key=lambda o:abs(o-x))
                    if abs(n-x)<=1.3:x=n
                cues.append([x,y,tx])
            for k in range(len(bl)-1):
                pass
for i in range(len(cues)):
    x,y,tx=cues[i];y=max(y,x+0.5)
    if i+1<len(cues):y=min(y,cues[i+1][0]-0.04)
    if y>x:lines+=[ts(x)+' --> '+ts(y),tx,'']
open(O+'sottotitoli.vtt','w').write('\n'.join(lines));print(len(lines)//3,'blocchi')
