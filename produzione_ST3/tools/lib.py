# Libreria di montaggio Storia III (chat ST3). Solo schede, scene e utilità.
import re,os,json,subprocess,html,wave,numpy as np
FONT='/home/user/Lezioni/kit/tools/mappa_font/'
LOGO_B=open('/home/user/lav/tools/Telesio_logo_blu.svg').read()
LOGO_W=open('/home/user/lav/tools/Telesio_logo_bianco.svg').read()
FPS=30
# ---------- numeri parlati -> cifre ----------
U=['','uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
T10=['','','venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
def w99(n):
    if n<20:return [U[n]]
    t,u=divmod(n,10);b=T10[t]
    if u==0:return [b]
    if u in(1,8):return [b[:-1]+U[u]]
    return [b+U[u]]
def words(n):
    out=[]
    if n>=1000:
        m,r=divmod(n,1000);base='mille' if m==1 else U[m]+'mila'
        rest=[''] if r==0 else words(r)
        return [base+x for x in rest]
    h,r=divmod(n,100)
    if h==0:return w99(r)
    hw='cento' if h==1 else U[h]+'cento'
    if r==0:return [hw]
    res=[]
    for x in w99(r):
        res.append(hw+x)
        if x[0]=='o':res.append(hw[:-1]+x)
    return res
NUM={}
for n in range(1,2100):
    for w in words(n):NUM.setdefault(w,n)
NUMRE=re.compile(r'\b('+'|'.join(sorted([w for w in NUM if len(w)>=5],key=len,reverse=True))+r')\b',re.I)
ROM={'primo':'I','secondo':'II','terzo':'III','nono':'IX','decimo':'X','undicesimo':'XI','dodicesimo':'XII'}
FIX=[('Chiersì','Quierzy'),('Constitùtio','Constitutio'),('fèudis','feudis'),('Privilègium Otònis','Privilegium Othonis'),('renovàzio impèrii','renovatio imperii'),('Renovàzio impèrii','Renovatio imperii'),('Lèchfeld','Lechfeld'),('Ug Capè','Ugo Capeto'),('Orleàn','Orléans'),('corvé','corvée'),('Corvé','Corvée'),('Silvestro secondo','Silvestro II'),('Giovanni dodicesimo','Giovanni XII'),('Corrado secondo','Corrado II'),('Enrico primo','Enrico I'),('Ottone primo','Ottone I'),('Ottone terzo','Ottone III'),('Carlo il Calvo','Carlo il Calvo'),('Ottone secondo','Ottone II'),('Chiersì','Quierzy')]
def pulisci(s):
    for a,b in FIX:s=s.replace(a,b)
    s=re.sub(r'\b(decimo|undicesimo|nono|dodicesimo) secolo',lambda m:ROM[m.group(1)]+' secolo',s)
    s=re.sub(r'\b(il|l\')(decimo|undicesimo)\b',lambda m:m.group(1)+('' if m.group(1)=="l'" else ' ')+ROM[m.group(2)],s)
    s=NUMRE.sub(lambda m:str(NUM[m.group(1).lower()]),s)
    s=re.sub(r'\b(\d{4})\b',lambda m:m.group(1),s)
    return s
# ---------- HTML ----------
def css():
    return '''@font-face{font-family:'Bricolage Grotesque';src:url('file://%sBricolageGrotesque-ExtraBold.ttf');font-weight:800}
@font-face{font-family:'Figtree';src:url('file://%sFigtree-Regular.ttf');font-weight:400}
@font-face{font-family:'Figtree';src:url('file://%sFigtree-SemiBold.ttf');font-weight:600}
@font-face{font-family:'Figtree';src:url('file://%sFigtree-Bold.ttf');font-weight:700}
*{box-sizing:border-box;margin:0;padding:0}body{width:1920px;height:1080px;overflow:hidden;font-family:Figtree,sans-serif;position:relative}
.logo{position:absolute;left:70px;top:44px;height:62px}.logo svg{height:62px;width:auto}
.kick{position:absolute;left:80px;top:140px;font-weight:700;font-size:30px;letter-spacing:4px;color:#2060AF;text-transform:uppercase}
.tit{position:absolute;left:80px;top:190px;width:1330px;font:800 66px/1.05 'Bricolage Grotesque';color:#0B1530}
.bar{position:absolute;left:80px;width:90px;height:7px;background:#2060AF;border-radius:4px}
.card{position:absolute;left:80px;width:1330px;background:#fff;border-radius:26px;border:6px solid #E4E8F0;padding:30px 40px;font-size:40px;line-height:1.3;color:#0B1530;box-shadow:0 8px 28px rgba(11,21,48,.08);display:flex;gap:26px;align-items:center}
.card.on{border-color:#FFE600;box-shadow:0 0 0 6px rgba(255,230,0,.35),0 8px 28px rgba(11,21,48,.12)}
.card.off{opacity:.55}
.card .n{flex:none;width:58px;height:58px;border-radius:50%%;background:#2060AF;color:#fff;font:800 32px/58px 'Bricolage Grotesque';text-align:center}
.card .lead{font-weight:700;color:#2060AF}
.foot{position:absolute;left:80px;right:80px;bottom:36px;border-top:3px solid #C9D0DC;padding-top:14px;font-weight:700;font-size:26px;letter-spacing:3px;color:#2060AF}
.camframe{position:absolute;left:1496px;top:60px;width:392px;height:228px;border:6px solid #2060AF;border-radius:20px;background:#0B1530}
.tag{position:absolute;left:1512px;top:276px;background:#FFE600;color:#0B1530;padding:12px 22px;border-radius:10px;transform:rotate(-2deg);font:800 32px 'Bricolage Grotesque'}
.tag small{display:block;font:700 26px Figtree;letter-spacing:2px}
.kw{position:absolute;left:1496px;top:430px;width:392px;border-top:5px solid #2060AF;padding-top:16px}
.kw b{display:block;font-size:26px;letter-spacing:3px;color:#2060AF;margin-bottom:10px}
.kw span{display:block;font-size:30px;font-weight:600;color:#0B1530;padding:9px 0;border-bottom:2px solid #C9D0DC}
.img{position:absolute;left:80px;border-radius:20px;overflow:hidden;border:6px solid #E4E8F0}
.img img{display:block;width:100%%}
.dark{background:radial-gradient(circle at 22%% 30%%,#1d4f9a 0,#0B1530 55%%,#050a1a 100%%)}
.band{position:absolute;left:0;width:1920px;height:60px;background:#2060AF}
''' % (FONT,FONT,FONT,FONT)
def esc(s):return html.escape(s)
def cardhtml(txt,top,h,cls,num,left,width,fs):
    t=esc(txt)
    if ':' in t and t.index(':')<34:a,b=t.split(':',1);t='<span class="lead">%s:</span>%s'%(a,b)
    n='<div class="n">%s</div>'%num if num else ''
    return '<div class="card %s" style="top:%dpx;left:%dpx;width:%dpx;min-height:%dpx;font-size:%dpx">%s<div>%s</div></div>'%(cls,top,left,width,h,fs,n,t)
def layout_cards(cards,active,start,left,width,fs,gap=22):
    import math
    out='';top=start;cpl=max(20,(width-12-80-90)/(fs*0.50))
    for i,c in enumerate(cards):
        lines=max(1,math.ceil(len(c)/cpl));h=max(110,int(lines*fs*1.32)+64)
        out+=cardhtml(c,top,h,'on' if i==active else 'off',i+1 if len(cards)>1 else None,left,width,fs);top+=h+gap
    return out
def page_light(kicker,title,cards=None,active=0,cam=False,kws=None,img=None,top=345,foot='STORIA · Prof. Giorgio Mazzotti',extra='',wide=False):
    h='<html><head><meta charset="utf-8"><style>%s</style></head><body style="background:#EEF0F4">'%css()
    if wide:h+='<style>.tit{width:1760px}</style>'
    h+='<div class="logo">%s</div>'%LOGO_B
    h+='<div class="kick">%s</div><div class="tit">%s</div>'%(esc(kicker),esc(title))
    if img:import base64;h+='<div class="img" style="top:%dpx;width:%dpx"><img src="data:image/png;base64,%s"></div>'%(img[1]+60,img[2],base64.b64encode(open(img[0],'rb').read()).decode())
    if cards:
        if img:
            left=img[2]+130;h+=layout_cards(cards,active,top,left,1410-left+80,36)
        elif wide:h+=layout_cards(cards,active,top,80,1760,46)
        else:h+=layout_cards(cards,active,top,80,1330,42)
    if cam:
        h+='<div class="camframe"></div><div class="tag">Prof. Giorgio Mazzotti<small>STORIA · TERZO ANNO</small></div>'
        if kws:h+='<div class="kw"><b>PAROLE CHIAVE</b>%s</div>'%''.join('<span>%s</span>'%esc(k) for k in kws[:5])
    h+=extra+'<div class="foot">%s</div></body></html>'%esc(foot)
    return h
def page_dark(kicker,title,sub='',bands=True,play=True,small=''):
    h='<html><head><meta charset="utf-8"><style>%s</style></head><body class="dark">'%css()
    h+='<div class="logo" style="left:80px;top:60px">%s</div>'%LOGO_W
    h+='<div style="position:absolute;left:120px;top:330px;font:700 30px Figtree;letter-spacing:7px;color:#7fa8de">%s</div>'%esc(kicker)
    h+='<div style="position:absolute;left:120px;top:390px;width:1250px;font:800 100px/1.05 \'Bricolage Grotesque\';color:#fff">%s</div>'%esc(title)
    if sub:h+='<div style="position:absolute;left:120px;top:690px;width:1250px;font:700 44px Figtree;color:#FFE600">%s</div>'%esc(sub)
    if small:h+='<div style="position:absolute;left:120px;top:850px;font:600 34px Figtree;color:#b6c6e0">%s</div>'%esc(small)
    if play:h+='<div style="position:absolute;left:1480px;top:400px;width:280px;height:280px;border-radius:50%;border:6px solid rgba(255,255,255,.35)"></div><div style="position:absolute;left:1570px;top:480px;width:0;height:0;border-left:110px solid #FFE600;border-top:60px solid transparent;border-bottom:60px solid transparent"></div>'
    if bands:h+='<div class="band" style="top:0"></div><div class="band" style="bottom:0"></div>'
    return h+'</body></html>'
# ---------- rendering ----------
class R:
    def __init__(s):
        from playwright.sync_api import sync_playwright
        s.p=sync_playwright().start();s.b=s.p.chromium.launch();s.pg=s.b.new_page(viewport={'width':1920,'height':1080})
    def png(s,html_,out):
        if os.path.exists(out):return out
        s.pg.set_content(html_);s.pg.wait_for_timeout(60);s.pg.screenshot(path=out);return out
    def close(s):s.b.close();s.p.stop()
# ---------- audio / ffmpeg ----------
def sh(c,**k):
    r=subprocess.run(c,capture_output=True,text=True,**k)
    if r.returncode:raise RuntimeError('rc=%s '%r.returncode+' '.join(map(str,c))[:300]+'\n'+r.stderr[-800:])
    return r
def dur(f):return float(sh(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]).stdout)
def nf(sec):return int(round(sec*FPS))
def concat_file(path,items):
    """items: [(png, frames)] -> file concat con durate esatte (ultimo fotogramma ripetuto)"""
    with open(path,'w') as f:
        for p,n in items:
            while n>0:
                m=min(n,150);f.write("file '%s'\nduration %.6f\n"%(p,m/FPS));n-=m
        f.write("file '%s'\n"%items[-1][0])
VENC=['-c:v','libx264','-preset','ultrafast','-crf','15','-pix_fmt','yuv420p','-r','30']
AENC=['-c:a','pcm_s16le','-ar','48000','-ac','2']
def piece(out,items,audio,frames=None,vf=None):
    """items [(png,frames)], audio: lista di input audio gia' pronti o filtergraph; crea pezzo mkv"""
    pass
