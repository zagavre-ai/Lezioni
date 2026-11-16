# Sottotitoli .vtt dal parlato del docente (Whisper base), nomi/date/luoghi corretti dalle slide. uso: subs18.py parte
import sys,json,re,difflib,unicodedata,subprocess,numpy as np
sys.path.insert(0,'/home/user/Lezioni/storia_s7')
from slides20 import SLIDES
PARTE=int(sys.argv[1])
W=[]
for l in open('/tmp/w20/pk20.jsonl'):
    for t,w in json.loads(l)['w']:W.append((t,w))
SN=json.load(open('/tmp/w20/cuts.json'))
TL={n:(t,d) for n,t,d in json.load(open(f'/tmp/w20/out/timeline_Parte{PARTE}.json'))}
VOC={}
def addtxt(t):
    for m in re.finditer(r"(?<![.!?:]\s)(?<!^)\b([A-ZÀ-Ý][A-Za-zÀ-ÿ']{4,}|[A-Z]{3,})\b",t):
        w=m.group(1)
        k=re.sub(r"'","",unicodedata.normalize('NFD',w.lower()));k=''.join(c for c in k if unicodedata.category(c)!='Mn')
        VOC.setdefault(k,w)
for _,_,cards in SLIDES:
    for l,r in cards:addtxt(l+' '+r)
V={o['nome']:o['testo'] for o in json.load(open('/tmp/w20/scambio/storia-V-lez20/testi_voci.json'))}
for t in V.values():addtxt(t)
def nrm(w):
    k=unicodedata.normalize('NFD',w.lower());return ''.join(c for c in k if unicodedata.category(c)!='Mn' and c.isalnum())
KEYS=list(VOC)
PHR=[(r"\b(dei|de|di|del|dal)\s*g[ao]s?p[ae]r[iy]e?\b","De Gasperi"),(r"\bdegasperi\b","De Gasperi"),(r"\bGaspiri\b","Gasperi"),(r"\btogliatico\b","Togliatti"),(r"\bTogliati\b","Togliatti"),
 (r"\b[Cc]on?stitu[a-z]*ente\b","Costituente"),(r"\b[Cc]ostituzione\b","Costituzione"),(r"\b[Cc]onstituzione\b","Costituzione"),(r"\b[Cc]osituente\b","Costituente"),(r"\b[Cc]ostit?uente\b","Costituente"),
 (r"\b[Rr]epublica\b","Repubblica"),(r"\bfampani\b","Fanfani"),(r"\bFampani\b","Fanfani"),(r"\bbubo\b","boom"),(r"\bBubo\b","Boom"),(r"\bmilimoro\b","Moro"),(r"\bparri\b","Parri"),(r"\bPlan\s*Marshal+\b","Piano Marshall"),(r"\bnato\b","NATO"),(r"\bcec[ao]\b","CECA"),(r"\benel\b","ENEL"),(r"\bpiano solo\b","Piano Solo")]
def fix(t):
    for a,b in PHR:t=re.sub(a,b,t)
    return t
def fixword(w):
    core=re.sub(r"[^\wÀ-ÿ']","",w)
    if len(core)<5 or core[0].isdigit():return w
    k=nrm(core)
    if k in VOC:return w
    m=difflib.get_close_matches(k,KEYS,n=1,cutoff=0.88) if core[0].isupper() else []
    if m:
        new=VOC[m[0]]
        if core[0].isupper() or new[0].isupper() and False:new=new[0].upper()+new[1:]
        return w.replace(core,new if not core[0].isupper() else new[0].upper()+new[1:])
    return w
x=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i','/tmp/w20/a20.wav','-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout,np.float32)
en=np.convolve(x**2,np.ones(480)/480,'same');thr=np.percentile(en,55)
def onset(t):
    i0=int(max(0,t-0.6)*16000);i1=int((t+0.2)*16000);seg=en[i0:i1:160]
    if not len(seg):return t
    k=np.argmax(seg>thr*0.6) if (seg>thr*0.6).any() else None
    return t if k is None else i0/16000+k*0.01
out=[]
for k in range(9):
    nm=f'D{k}'
    if nm not in TL:continue
    a,b=SN[k],SN[k+1];P,d=TL[nm]
    ws=[(t,fix(w)) for t,w in W if a-0.01<=t<b-0.05]
    ws=[(t,fixword(w)) for t,w in ws]
    # blocchi
    blocks=[];cur=[]
    def flush():
        global cur
        if cur:blocks.append(cur);cur=[]
    for i,(t,w) in enumerate(ws):
        if cur:
            txt=' '.join(x[1] for x in cur);gap=t-ws[i-1][0]
            if len(txt)+1+len(w)>84 or t-cur[0][0]>5.5 or (gap>1.2 and len(txt)>12) or (re.search(r'[.?!]$',cur[-1][1]) and len(txt)>25):flush()
        cur.append((t,w))
    flush()
    for bi,bl in enumerate(blocks):
        s=onset(bl[0][0]);txt=' '.join(w for _,w in bl)
        e=(blocks[bi+1][0][0]-0.05) if bi+1<len(blocks) else b-0.1
        e=min(e,s+max(1.2,0.075*len(txt)),s+6.0);e=min(e,b-0.05)
        if e<=s+0.3:continue
        # due righe da max 42
        if len(txt)>42:
            ws_=txt.split();best=None
            for j in range(1,len(ws_)):
                l1,l2=' '.join(ws_[:j]),' '.join(ws_[j:])
                if len(l1)<=42 and len(l2)<=42 and not l1.endswith("'"):
                    sc=abs(len(l1)-len(l2))
                    if best is None or sc<best[0]:best=(sc,l1+'\n'+l2)
            txt=best[1] if best else txt[:42]+'\n'+txt[42:84]
        out.append((P+(s-a),P+(e-a),txt))
# aggancio all'attacco reale della voce sul video finale (stessa misura del controllo finale)
SR8=8000
xf=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',f'/tmp/w20/fin/Storia_Lez20_Parte{PARTE}_1080p.mp4','-ac','1','-ar',str(SR8),'-f','s16le','-'],capture_output=True).stdout,np.int16).astype(float)
ef=np.convolve(xf**2,np.ones(400)/400,'same');thf=np.percentile(ef,60)
fixed=0
for i,(a_,b_,t_) in enumerate(out):
    i0=int(max(0,a_-0.8)*SR8);seg=ef[i0:int((a_+0.8)*SR8)]
    if len(seg)>int(0.5*SR8) and seg[:int(0.5*SR8)].mean()<thf*0.5 and (seg>thf).any():
        on=i0/SR8+int(np.argmax(seg>thf))/SR8
        if abs(on-a_)>0.05:out[i]=(max(0,on-0.04),b_,t_);fixed+=1
print('agganciati',fixed)
# niente sovrapposizioni
for i in range(1,len(out)):
    if out[i][0]<out[i-1][1]:out[i-1]=(out[i-1][0],max(out[i-1][0]+0.3,out[i][0]-0.02),out[i-1][2])
def ts(s):return '%02d:%02d:%06.3f'%(s//3600,s%3600//60,s%60)
open(f'/tmp/w20/out/Storia_Lez20_Parte{PARTE}.vtt','w').write('WEBVTT\n\n'+''.join(f'{ts(a)} --> {ts(b)}\n{t}\n\n' for a,b,t in out))
print('blocchi',len(out))
