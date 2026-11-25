import os,re,json,math,difflib,subprocess,unicodedata,hashlib
from PIL import Image,ImageDraw,ImageFont,ImageFilter
W,H=1920,1080
NAVY=(11,21,48);BLUE=(32,96,175);YEL=(255,230,0);WHITE=(255,255,255)
GREY=(90,102,133)
FD='/home/user/Lezioni/kit/caratteri/'
def F(name,size): return ImageFont.truetype(FD+name,size)
BRI='BricolageGrotesque-ExtraBold.ttf'
FIG='Figtree-Regular.ttf';FIGM='Figtree-Medium.ttf';FIGB='Figtree-Bold.ttf';FIGSB='Figtree-SemiBold.ttf'
_fc={}
def font(n,s):
    k=(n,s)
    if k not in _fc:_fc[k]=F(n,s)
    return _fc[k]
LOGO_B=Image.open('/tmp/w/assets/logo_blu.png').convert('RGBA');LOGO_B=LOGO_B.resize((300,int(LOGO_B.height*300/LOGO_B.width)),Image.LANCZOS)
LOGO_W=Image.open('/tmp/w/assets/logo_bianco.png').convert('RGBA');LOGO_W=LOGO_W.resize((300,int(LOGO_W.height*300/LOGO_W.width)),Image.LANCZOS)
MAT='STORIA V'
def tw(d,t,f): return d.textlength(t,font=f)
def wrap(d,text,f,maxw):
    words=text.split();lines=[];cur=''
    for w in words:
        t=(cur+' '+w).strip()
        if tw(d,t,f)<=maxw or not cur: cur=t
        else: lines.append(cur);cur=w
    if cur:lines.append(cur)
    return lines
_dd=ImageDraw.Draw(Image.new('RGB',(10,10)))
def nlines(text,f,maxw): return len(wrap(_dd,text,f,maxw))
def shadow_rect(img,box,r=22,blur=14,off=(0,8),alpha=60):
    x0,y0,x1,y1=box
    pad=blur*3
    sh=Image.new('RGBA',(x1-x0+2*pad,y1-y0+2*pad),(0,0,0,0))
    ImageDraw.Draw(sh).rounded_rectangle((pad,pad,pad+x1-x0,pad+y1-y0),r,fill=(70,80,100,alpha))
    sh=sh.filter(ImageFilter.GaussianBlur(blur))
    img.paste(sh,(x0-pad+off[0],y0-pad+off[1]),sh)
# ---------- blue animated background
def blue_bg(t=0.0):
    s=Image.new('RGB',(960,540))
    px=Image.linear_gradient('L').resize((960,540))
    top=Image.new('RGB',(960,540),(9,18,44));bot=Image.new('RGB',(960,540),(22,52,112))
    s=Image.composite(bot,top,px)
    ov=Image.new('RGBA',(960,540),(0,0,0,0));d=ImageDraw.Draw(ov)
    for i,(cx,cy,r,col,a) in enumerate([(200,120,190,(255,230,0),22),(780,430,230,(70,130,220),48),(520,60,120,(255,230,0),14),(860,90,150,(70,130,220),36)]):
        x=cx+40*math.sin(t*0.35+i*1.7);y=cy+28*math.cos(t*0.28+i*2.3)
        d.ellipse((x-r,y-r,x+r,y+r),fill=col+(a,))
    ov=ov.filter(ImageFilter.GaussianBlur(10))
    s=s.convert('RGBA');s.alpha_composite(ov)
    return s.convert('RGB').resize((W,H),Image.BICUBIC)
def blue_frame(t=0.0,label=None,footer=True,page=None):
    im=blue_bg(t);d=ImageDraw.Draw(im)
    im.paste(LOGO_W,(56,34),LOGO_W)
    if label: d.text((64,150),label.upper(),font=font(FIGB,26),fill=YEL)
    if footer: d.text((56,1030),MAT,font=font(FIGB,20),fill=(200,214,240))
    if page: d.text((W-56,1030),f'Pagina {page}',font=font(FIGB,20),fill=(200,214,240),anchor='ra')
    return im
# ---------- white slide frame
def white_frame(label,title,page,prof=True,kw=None,profimg=None):
    im=Image.new('RGB',(W,H),WHITE);d=ImageDraw.Draw(im)
    im.paste(LOGO_B,(56,34),LOGO_B)
    d.text((64,150),label.upper(),font=font(FIGB,24),fill=BLUE)
    ft=font(BRI,64)
    ls=wrap(d,title,ft,1290)
    y=186
    for l in ls: d.text((60,y),l,font=ft,fill=NAVY);y+=74
    d.rectangle((60,y+4,128,y+10),fill=BLUE)
    d.text((56,1030),MAT,font=font(FIGB,20),fill=BLUE)
    d.text((W-56,1030),f'Pagina {page}',font=font(FIGB,20),fill=BLUE,anchor='ra')
    if prof:
        x,y0=1428,148
        shadow_rect(im,(x,y0,x+412,y0+309+78),r=6,blur=12)
        d.rectangle((x,y0,x+412,y0+309),fill=(235,238,244))
        d.rectangle((x,y0+309,x+412,y0+309+78),fill=YEL)
        d.text((x+20,y0+309+12),'Giorgio Mazzotti',font=font(BRI,34),fill=NAVY)
        d.text((x+20,y0+309+52),'PROF. DI STORIA',font=font(FIGB,20),fill=NAVY)
        if kw:
            ky=y0+309+78+50
            d.text((x,ky),'PAROLE CHIAVE',font=font(FIGB,22),fill=BLUE);ky+=42
            for k in kw[:5]:
                fk=font(FIGB,32)
                for j,l in enumerate(wrap(d,k,fk,392)):
                    d.text((x+30 if j==0 else x+30,ky),l,font=fk,fill=NAVY)
                    if j==0: d.ellipse((x+6,ky+14,x+20,ky+28),fill=YEL,outline=BLUE,width=3)
                    ky+=42
                ky+=10
    if not prof and kw:
        x=1428;ky=148
        d.text((x,ky),'PAROLE CHIAVE',font=font(FIGB,22),fill=BLUE);ky+=42
        for k in kw[:5]:
            d.ellipse((x+6,ky+14,x+20,ky+28),fill=YEL,outline=BLUE,width=3);d.text((x+30,ky),k,font=font(FIGB,32),fill=NAVY);ky+=52
    return im
CARDW=1290;CARDF=font(FIG,40);LH=60;PAD=26
def card_h(text,fnt=CARDF,w=CARDW,lh=LH): return nlines(text,fnt,w-2*PAD-30)*lh+2*PAD-8
def draw_card(im,x,y,text,active,fnt=CARDF,w=CARDW,lh=LH,dark=False,plain=False):
    d=ImageDraw.Draw(im)
    lines=wrap(d,text,fnt,w-2*PAD-30);h=len(lines)*lh+2*PAD-8
    if dark:
        base=(24,44,92) if not active else (22,40,86)
        col=WHITE if active else (160,176,210)
        bor=YEL if active else (60,86,140)
    else:
        base=(255,255,255) if active else (244,246,250)
        col=NAVY if active else (110,121,150)
        bor=YEL if active else (222,228,238)
    if plain: base=(255,255,255);col=NAVY;bor=(214,222,236)
    if not dark: shadow_rect(im,(x,y,x+w,y+h),r=22,blur=10,off=(0,6),alpha=45 if active else 25)
    d.rounded_rectangle((x,y,x+w,y+h),22,fill=base,outline=bor,width=7 if (active and not plain) else 2)
    if active and not plain:
        d.ellipse((x+22,y+PAD+8,x+40,y+PAD+26),fill=YEL,outline=(200,170,0) if not dark else YEL,width=2)
    ty=y+PAD-6
    for l in lines:
        d.text((x+PAD+30,ty),l,font=fnt,fill=col);ty+=lh
    return y+h
def slide_state(label,title,page,cards,active,kw=None):
    im=white_frame(label,title,page,True,kw)
    y=300
    for i,c in enumerate(cards):
        y=draw_card(im,60,y,c,i==active)+26
    return im
def fits(cards,limit=1000-300):
    return sum(card_h(c) for c in cards)+26*(len(cards)-1)<=limit
# ---------- text utils
def norm(s):
    s=unicodedata.normalize('NFD',s.lower());s=''.join(c for c in s if unicodedata.category(c)!='Mn')
    return re.sub(r"[^a-z0-9]+",' ',s).split()
def split_sentences(t):
    t=t.strip()
    out=[];cur=''
    toks=re.split(r'(?<=[.!?])\s+',t)
    for p in toks:
        if cur and re.search(r'\b[A-Z]\.$',cur): cur+=' '+p
        else:
            if cur: out.append(cur)
            cur=p
    if cur:out.append(cur)
    return out
def asr_words(name,d='/tmp/w/trvox'):
    j=json.load(open(f'{d}/{name}.json'));ws=[]
    for t,tok in j['parole']:
        if tok.startswith(' ') or not ws: ws.append([t,tok.strip()])
        else: ws[-1][1]+=tok
    return ws,j['dur']
def align(name,sentences,d='/tmp/w/trvox'):
    """returns list of (start,end) per sentence, from ASR words of the voice"""
    ws,dur=asr_words(name,d)
    A=[norm(w[1]) for w in ws]
    ta=[];idx=[]
    for i,a in enumerate(A):
        for x in a: ta.append(x);idx.append(i)
    sc=[];sidx=[]
    for si,s in enumerate(sentences):
        for x in norm(s): sc.append(x);sidx.append(si)
    sm=difflib.SequenceMatcher(None,sc,ta,autojunk=False)
    m={}
    for a,b,n in sm.get_matching_blocks():
        for k in range(n): m[a+k]=idx[b+k]
    first={}
    for k,si in enumerate(sidx):
        if k in m and si not in first: first[si]=m[k]
    starts=[];last=0.0
    for si in range(len(sentences)):
        if si in first: t=ws[first[si]][0]
        else: t=last+0.5
        t=max(t,last);starts.append(t);last=t
    if starts: starts[0]=0.0
    ends=starts[1:]+[dur]
    # sentence starts a little before first word
    st=[max(0,s-0.12) if i>0 else 0 for i,s in enumerate(starts)]
    en=st[1:]+[dur]
    return list(zip(st,en)),dur,sm.ratio()
def lufs(path):
    r=subprocess.run(['ffmpeg','-hide_banner','-i',path,'-af','ebur128','-f','null','-'],capture_output=True,text=True).stderr
    m=re.findall(r'I:\s+(-?[\d.]+) LUFS',r)
    return float(m[-1]) if m else -23.0

_U={'uno':1,'un':1,'due':2,'tre':3,'tré':3,'quattro':4,'cinque':5,'sei':6,'sette':7,'otto':8,'nove':9,'dieci':10,'undici':11,'dodici':12,'tredici':13,'quattordici':14,'quindici':15,'sedici':16,'diciassette':17,'diciotto':18,'diciannove':19}
_T={'venti':20,'trenta':30,'quaranta':40,'quaranta':40,'cinquanta':50,'sessanta':60,'settanta':70,'ottanta':80,'novanta':90}
def _p99(s):
    if not s: return 0
    for k in sorted(_U,key=len,reverse=True):
        if s==k: return _U[k]
    for tn,v in _T.items():
        stem=tn[:-1]
        if s.startswith(stem):
            r=s[len(stem):]
            if r.startswith(tn[-1]): r=r[1:]
            if r=='' : return v
            if r in _U: return v+_U[r]
    return None
def it2year(w):
    w=w.lower()
    if not w.startswith('mille'): return None
    r=w[5:];n=1000
    m=re.match(r'(otto|nove|sette|sei|cinque|quattro|tre|due)?cento',r)
    if m:
        n+=100*({'otto':8,'nove':9,'sette':7,'sei':6,'cinque':5,'quattro':4,'tre':3,'due':2,None:1}[m.group(1)]);r=r[m.end():]
    p=_p99(r)
    if p is None: return None
    return n+p
def digits(t):
    def y(m):
        v=it2year(m.group(0));return str(v) if v else m.group(0)
    t=re.sub(r'\b[Mm]ille\w+',y,t)
    t=re.sub(r'\bsei milioni\b','6 milioni',t);t=re.sub(r'\bdue milioni\b','2 milioni',t)
    t=re.sub(r'\bun miliardo e mezzo\b','1,5 miliardi',t);t=re.sub(r'\botto ore\b','8 ore',t)
    t=t.replace('Tredicesimo','XIII');t=re.sub(r'\bCGL\b','CGL (Confederazione generale del lavoro)',t)
    return t
