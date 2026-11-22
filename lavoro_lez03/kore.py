# Schede con la voce Kore: copertina, argomenti, titoli, approfondimenti, pillole, quiz, mappe, glossario, ripassi, compiti
import os,json,re,subprocess,difflib,math
import numpy as np
from PIL import Image,ImageDraw,ImageFilter
from lib import *
import montaggio as M
VOX='/tmp/w/vox';PROV='/tmp/w/vox_prov';ASR='/tmp/w/voxasr'
os.makedirs(PROV,exist_ok=True)
TESTI={v['nome']:v['testo'] for v in json.load(open('/tmp/w/b/testi_tutti.json'))}
def est_dur(t):return len(t.split())/2.3+0.6
def voce(nome):
    """(percorso wav, durata, vera?) : la voce vera se c'è, altrimenti silenzio provvisorio della durata stimata"""
    p=f'{VOX}/{nome}.wav'
    if os.path.exists(p):
        d=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout)
        return p,d,True
    d=est_dur(TESTI[nome]);q=f'{PROV}/{nome}.wav'
    if not os.path.exists(q):M.sh(['ffmpeg','-v','error','-y','-f','lavfi','-i','anullsrc=r=24000:cl=mono','-t',f'{d:.2f}',q])
    return q,d,False
def _norm(w):return re.sub(r'[^a-zàèéìòù0-9]','',w.lower())
def voce_words(nome):
    j=f'{ASR}/{nome}.json'
    if not os.path.exists(j):return None
    S=json.load(open(j));S=S if isinstance(S,list) else S['segmenti'];out=[]
    for s in S:
        cur=None
        for t,tok in s['parole']:
            if tok.startswith(' ') or cur is None:
                if cur:out.append(cur)
                cur=[t,tok.strip()]
            else:cur[1]+=tok
        if cur:out.append(cur)
    return out
def frasi_tempi(nome,frasi):
    """inizio (s) di ogni frase nella voce: dalla trascrizione se c'è, altrimenti proporzionale ai caratteri"""
    p,d,vera=voce(nome);W=voce_words(nome)
    if W and vera:
        toks=[_norm(w[1]) for w in W];res=[];start=0
        for f in frasi:
            ft=[_norm(x) for x in f.split() if _norm(x)][:4];best=(-1,start)
            for j in range(start,len(toks)):
                sc=sum(1 for a,b in zip(ft,toks[j:j+4]) if a==b or difflib.SequenceMatcher(None,a,b).ratio()>0.8)/max(1,len(ft))
                if sc>best[0]+0.01:best=(sc,j)
                if sc>=1:break
            res.append(W[best[1]][0]);start=best[1]+1
        return res
    T=TESTI[nome];res=[];last=0.0
    for f in frasi:
        i=T.find(f[:18]);
        t=(d*0.02+d*0.94*i/len(T)) if i>=0 else last+0.5
        res.append(max(t,last));last=res[-1]
    return res
# ---------------- sfondo blu animato
BG=M.OUT+'/bluebg.mp4'
def make_bg():
    if os.path.exists(BG):return BG
    w,h=480,270;n=300
    yy,xx=np.mgrid[0:h,0:w].astype(np.float32);cmd=['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{w}x{h}','-r','30','-i','-','-c:v','libx264','-crf','14','-pix_fmt','yuv420p',BG]
    pr=subprocess.Popen(cmd,stdin=subprocess.PIPE)
    base=np.zeros((h,w,3),np.float32);g=(xx/w*0.5+yy/h*0.5)
    for c,(a,b) in enumerate(zip((9,17,40),(22,44,96))):base[...,c]=a+(b-a)*g
    for i in range(n):
        t=i/n*2*math.pi;fr=base.copy()
        for k,(cx,cy,r,ph,amp) in enumerate([(0.2,0.3,0.35,0,1),(0.75,0.25,0.3,1.7,1),(0.5,0.85,0.4,3.1,1),(0.9,0.8,0.28,4.6,1),(0.1,0.9,0.3,2.4,1)]):
            x=(cx+0.07*math.sin(t+ph))*w;y=(cy+0.07*math.cos(t*1+ph))*h
            d=np.sqrt((xx-x)**2+(yy-y)**2)/(r*w);a=np.clip(1-d,0,1)**2*38
            fr[...,0]+=a*0.45;fr[...,1]+=a*0.8;fr[...,2]+=a*1.4
        pr.stdin.write(np.clip(fr,0,255).astype(np.uint8).tobytes())
    pr.stdin.close();pr.wait();return BG
def rgba():return Image.new('RGBA',(W,H),(0,0,0,0))
def tbox(d,xy,text,font,fill,maxw=None,lh=1.25,anchor='l'):
    x,y=xy
    L=wrap_plain(d,text,font,maxw) if maxw else [text]
    for i,l in enumerate(L):
        xx=x if anchor=='l' else x-d.textlength(l,font=font)/2
        d.text((xx,y+i*font.size*lh),l,font=font,fill=fill)
    return y+len(L)*font.size*lh
def blue_logo(img):logo(img,70,38,190,bianco=True)
def scheda_titolo(label,titolo,sub=None,num=None):
    img=rgba();blue_logo(img);d=ImageDraw.Draw(img)
    d.text((140,360),label.upper(),font=F('b',32),fill=GIALLO)
    y=tbox(d,(140,420),titolo,F('t',92),(255,255,255),maxw=1500,lh=1.12)
    d.rectangle((140,y+20,140+220,y+30),fill=GIALLO)
    if sub:tbox(d,(140,y+56),sub,F('m',40),(205,216,240),maxw=1500)
    return img
def pillola(titolo,righe,active,nsub='RIPASSO'):
    img=rgba();blue_logo(img);d=ImageDraw.Draw(img)
    d.text((140,150),nsub.upper(),font=F('b',30),fill=GIALLO)
    y=tbox(d,(140,196),titolo,F('t',66),(255,255,255),maxw=1640,lh=1.1)+34
    for i,r in enumerate(righe):
        if i>active:break
        on=(i==active)
        L=wrap_plain(d,r,F('b' if on else 'm',44),1500);h=len(L)*66+34
        if on:
            d.rounded_rectangle((120,y,1800,y+h),22,fill=(255,255,255,255),outline=GIALLO,width=8)
            d.ellipse((1750,y+14,1778,y+42),fill=GIALLO)
            col=NOTTE
        else:
            d.rounded_rectangle((120,y,1800,y+h),22,fill=(255,255,255,40),outline=(255,255,255,70),width=3);col=(215,224,244)
        for j,l in enumerate(L):d.text((170,y+16+j*66),l,font=F('b' if on else 'm',44),fill=col)
        y+=h+18
    return img
def quiz_card(k,titolo,n=5):
    img=rgba();blue_logo(img);d=ImageDraw.Draw(img)
    d.text((140,330),'QUIZ',font=F('t',150),fill=GIALLO)
    y=tbox(d,(140,520),f'Argomento {k}: {titolo}',F('t',60),(255,255,255),maxw=1500,lh=1.12)
    tbox(d,(140,y+30),f'{n} domande. Per continuare serve almeno l\'80% di risposte esatte.',F('m',38),(205,216,240),maxw=1500)
    return img
def png(img):return M.save_png(img)
