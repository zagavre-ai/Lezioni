# Approfondimenti animati (voce Kore): sfondo blu animato, opera che si avvicina lentamente, parole che compaiono con la voce
import sys,re,subprocess;sys.path.insert(0,'/home/user/Lezioni/lavoro_lez03')
from kore import *
import montaggio as M
import numpy as np
WIN_=(100,190,1160,900)  # finestra dell'immagine
def frasi(t):return [x.strip() for x in re.split(r'(?<=[.!?])\s+',t) if x.strip()]
def viz_text(righe,sub=None):
    """grafica senza opera: parole grandi su fondo blu-celeste"""
    w,h=WIN_[2]-WIN_[0],WIN_[3]-WIN_[1]
    im=Image.new('RGB',(w,h),(18,38,86));d=ImageDraw.Draw(im)
    for i in range(0,h,8):
        a=i/h;d.line((0,i,w,i),fill=(int(18+20*a),int(38+30*a),int(86+50*a)))
    n=len(righe);bh=h//(n+1)
    y=bh//2+20
    for i,r in enumerate(righe):
        f=F('t',92 if len(r)<16 else 70 if len(r)<26 else 54)
        L=wrap_plain(d,r,f,w-120);th=len(L)*f.size*1.1
        for j,l in enumerate(L):d.text((60,y+j*f.size*1.1),l,font=f,fill=GIALLO if i==0 else (255,255,255))
        y+=max(bh,th+20)
    return im
def beat_layer(img_caption,chips_shown,titolo_beat,show_window=True):
    L=rgba();d=ImageDraw.Draw(L)
    x0,y0,x1,y1=WIN_
    # ombra e cornice attorno alla finestra (l'interno resta trasparente)
    sh=Image.new('RGBA',(W,H),(0,0,0,0));ImageDraw.Draw(sh).rectangle((x0-8,y0-8+12,x1+8,y1+8+12),fill=(0,0,0,120));sh=sh.filter(ImageFilter.GaussianBlur(18))
    L.alpha_composite(sh)
    d=ImageDraw.Draw(L);d.rectangle((x0-10,y0-10,x1+10,y1+10),fill=(255,255,255,255));d.rectangle((x0,y0,x1,y1),fill=(0,0,0,0))
    blue_logo(L);d=ImageDraw.Draw(L)
    d.text((100,128),'APPROFONDIMENTO',font=F('b',28),fill=GIALLO)
    if img_caption:
        for i,l in enumerate(wrap_plain(d,img_caption,F('m',26),1160)):d.text((100,y1+24+i*34),l,font=F('m',26),fill=(205,216,240))
    xx=1240;yy=190
    for l in wrap_plain(d,titolo_beat,F('t',54),600):
        d.text((xx,yy),l,font=F('t',54),fill=(255,255,255));yy+=62
    yy+=24
    for c in chips_shown:
        lines=wrap_plain(d,c,F('b',36),540);h=len(lines)*46+30
        d.rounded_rectangle((xx,yy,xx+600,yy+h),18,fill=(255,255,255,255))
        d.rectangle((xx,yy+10,xx+10,yy+h-10),fill=GIALLO)
        for j,l in enumerate(lines):d.text((xx+30,yy+15+j*46),l,font=F('b',36),fill=NOTTE)
        yy+=h+16
    return L
def zoom_frames(src,nfr,pan=(0,0)):
    """generatore di finestre (PIL) con avvicinamento lento"""
    w,h=WIN_[2]-WIN_[0],WIN_[3]-WIN_[1]
    s=max(w/src.size[0],h/src.size[1])*1.0
    big=src.resize((round(src.size[0]*s*1.0),round(src.size[1]*s*1.0)),Image.LANCZOS)
    bw,bh=big.size
    for f in range(nfr):
        z=1.0+0.10*f/max(1,nfr-1)
        cw,ch=bw/z,bh/z
        cx=bw/2+pan[0]*(bw-cw)/2*(1-f/max(1,nfr-1)*0)+ (pan[0]*(bw-cw)/2*(f/max(1,nfr-1)*2-1)*0)
        cy=bh/2
        box=(cx-cw/2,cy-ch/2,cx+cw/2,cy+ch/2)
        yield big.resize((w,h),Image.BILINEAR,box=box) if (bw,bh)!=(w,h) or True else big
def ap_piece(nome,beats,jingle=None,tag=''):
    """beats: [dict(s=(i0,i1) frasi, img=nome|PIL|None, chips=[..], titolo='..', didasc=..., pan=)]"""
    vp,vd,vera=voce(nome);fr=frasi(TESTI[nome]);tm=frasi_tempi(nome,fr)
    V0=0.5;N=M.nfr(V0+vd+1.3)
    # intervalli dei beat in fotogrammi
    bt=[]
    for i,b in enumerate(beats):
        a=V0+tm[b['s'][0]] if i>0 else 0.0
        e=(V0+tm[beats[i+1]['s'][0]]) if i+1<len(beats) else N/30
        bt.append((M.nfr(a) if i>0 else 0,M.nfr(e) if i+1<len(beats) else N))
    key=M.key_of('ap',nome,beats,bt,vera,tag)
    v=f'{M.OUT}/pezzi/{nome}_{key}.mp4';a=f'{M.OUT}/pezzi/{nome}_{key}.wav'
    if os.path.exists(v) and os.path.exists(a):return dict(v=v,a=a,n=N,first=None,last=None,name=nome,beats=bt)
    M.wav_events([(vp,V0,1.0)],N,a)
    enc=M._enc(v,N);bgp=subprocess.Popen(['ffmpeg','-v','error','-stream_loop','-1','-i',make_bg(),'-vf','fps=30,scale=1920:1080:flags=bicubic','-an','-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
    FB=1920*1080*3;x0,y0,x1,y1=WIN_
    for (fa,fb),b in zip(bt,beats):
        n=fb-fa;im=b.get('img')
        if isinstance(im,str):src=Image.open(IMG+im+'.png').convert('RGB')
        else:src=im
        zf=zoom_frames(src,n);chips=b['chips'];caps=b.get('didasc')
        # istante di comparsa di ogni chip: distribuiti nella durata del beat
        appear=[int(n*(0.12+0.72*i/max(1,len(chips)))) for i in range(len(chips))]
        layers={}
        for f in range(n):
            shown=[c for c,ap in zip(chips,appear) if f>=ap]
            kk=len(shown)
            if kk not in layers:
                if len(layers)>4:layers.clear()
                L=beat_layer(caps,shown,b['titolo']);al=np.array(L)[...,3:4].astype(np.uint16);layers[kk]=((np.array(L)[...,:3].astype(np.uint16)*al//255),255-al)
            fg,inv=layers[kk]
            bgf=np.frombuffer(M._rd(bgp,FB),np.uint8).reshape(1080,1920,3).copy()
            win=np.array(next(zf))
            bgf[y0:y1,x0:x1]=win
            out=(bgf.astype(np.uint16)*inv//255+fg).astype(np.uint8)
            enc.stdin.write(out)
    enc.stdin.close();enc.wait();bgp.kill()
    return dict(v=v,a=a,n=N,first=None,last=None,name=nome,beats=bt)
