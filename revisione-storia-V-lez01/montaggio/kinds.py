from pieces import *
def vpath(n): return VOX+n+'.wav'
def title_font_lines(d,text,size,maxw,fn=BRI):
    f=font(fn,size);return f,wrap(d,text,f,maxw)
def p_title(name,n,title):
    fr=[];dur=3.9
    for k in range(int(dur/0.5)+1):
        t=k*0.5;im=blue_frame(t,footer=False);d=ImageDraw.Draw(im)
        d.text((64,330),f'ARGOMENTO {n}',font=font(FIGB,40),fill=YEL)
        f,ls=title_font_lines(d,title,100,1700);y=400
        for l in ls: d.text((60,y),l,font=f,fill=WHITE);y+=116
        d.rectangle((64,y+14,224,y+24),fill=YEL)
        fr.append((im,min(0.5,dur-t)))
    return piece(name,fr,dur,[(TRANS,0.0,-6,'fx'),(JT,0.9,0,'fx')])
def p_quiz(name,n,title,verifica=False):
    fr=[];dur=4.0
    for k in range(8):
        t=k*0.5;im=blue_frame(t,footer=False);d=ImageDraw.Draw(im)
        if verifica:
            d.text((64,300),'VERIFICA FINALE',font=font(FIGB,40),fill=YEL)
            d.text((60,360),'Verifica di sbarramento',font=font(BRI,110),fill=WHITE)
            d.text((64,520),'10 domande sulla lezione · per continuare serve almeno l\'80%',font=font(FIG,44),fill=(215,226,247))
        else:
            d.text((64,300),f'ARGOMENTO {n} · {title}'.upper(),font=font(FIGB,36),fill=YEL)
            d.text((60,360),'Quiz',font=font(BRI,170),fill=WHITE)
            d.text((64,580),'5 domande · per continuare serve almeno l\'80%',font=font(FIG,48),fill=(215,226,247))
        fr.append((im,0.5))
    return piece(name,fr,dur,[(JQ,0.5,0,'fx')])
def unit_card(im,x,y,text,active,fs,w,gl=False):
    f=font(FIG,fs);fb=font(FIGB,fs);d=ImageDraw.Draw(im);lh=int(fs*1.45)
    if gl and ':' in text[:46]:
        term,defn=text.split(':',1);term=term.strip();defn=defn.strip()
        lines=[(term,fb,YEL if active else (200,214,240))]+[(l,f,WHITE if active else (160,176,210)) for l in wrap(d,defn,f,w-110)]
    else:
        lines=[(l,f,WHITE if active else (160,176,210)) for l in wrap(d,text,f,w-110)]
    h=len(lines)*lh+40
    d.rounded_rectangle((x,y,x+w,y+h),24,fill=(24,46,98) if active else (19,38,82),outline=YEL if active else (52,78,134),width=7 if active else 2)
    if active: d.ellipse((x+24,y+22,x+42,y+40),fill=YEL)
    ty=y+14
    for l,ff,c in lines: d.text((x+66,ty),l,font=ff,fill=c);ty+=lh
    return y+h
def cards_state(t,label,title,units,k,fs,w,gl,maxvis,newalpha=1.0,page=None,tsize=70):
    im=blue_frame(t,label=None,footer=True,page=page);d=ImageDraw.Draw(im)
    d.text((64,150),label.upper(),font=font(FIGB,28),fill=YEL)
    f,ls=title_font_lines(d,title,tsize,1760);y=196
    for l in ls: d.text((60,y),l,font=f,fill=WHITE);y+=tsize+14
    y+=12
    vis=[]
    if k>=0:
        f_=font(FIG,fs);lh_=int(fs*1.45);avail=1010-y;acc=0;vis=[]
        for i in range(k,max(-1,k-maxvis),-1):
            u=units[i]
            if gl and ':' in u[:46]:
                term,defn=u.split(':',1);nl=1+len(wrap(d,defn.strip(),f_,w-110))
            else: nl=len(wrap(d,u,f_,w-110))
            h=nl*lh_+40+18
            if acc+h>avail and vis: break
            acc+=h;vis.insert(0,i)
    base=im
    if k>=0 and newalpha<1.0:
        a=im.copy();yy=y
        for i in vis[:-1]: yy=unit_card(a,70,yy,units[i],False,fs,w,gl)+18
        b=im.copy();yy=y
        for i in vis: yy=unit_card(b,70,yy,units[i],i==k,fs,w,gl)+18
        return Image.blend(a,b,newalpha)
    for i in vis: y=unit_card(im,70,y,units[i],i==k,fs,w,gl)+18
    return im
def cards_piece(name,label,title,units,voice,jingle=None,lead=1.0,tail=0.8,trans_end=False,maxvis=5,fs=40,gl=False,w=1780,span=None,tsize=70,align_units=None):
    if align_units:
        al,vdur,ratio=align(voice,align_units);al=al[len(align_units)-len(units):]
    else: al,vdur,ratio=align(voice,units)
    disp=[digits(u) for u in units];title=digits(title)
    if span: al=[(a,b) for a,b in al]
    total=lead+vdur+tail
    ev=[];t=0.0
    # state timeline
    states=[]
    states.append((0.0,lead+al[0][0],-1,1.0))
    for i,(a,b) in enumerate(al):
        s=lead+a;e=lead+(al[i+1][0] if i+1<len(al) else vdur+tail)
        states.append((s,s+0.12,i,0.5)); 
        # animate bg each 1 s
        tt=s+0.12
        while tt<e-0.01:
            nx=min(e,tt+1.0);states.append((tt,nx,i,1.0));tt=nx
    # fill initial
    fr=[];
    for (s,e,k,al_) in states:
        im=cards_state(s,label,title,disp,k,fs,w,gl,maxvis,al_,tsize=tsize)
        fr.append((im,e-s))
    # initial lead animation per second
    audio=[(TRANS,0.0,-8,'fx')]
    if jingle: audio.append((jingle,0.6,-4,'fx'))
    audio.append((vpath(voice),lead if not jingle else max(lead,2.0),vgain(vpath(voice)),'voice'))
    if jingle:  # shift timeline so voice begins after jingle intro
        pass
    if trans_end: audio.append((TRANS,total-1.9,-8,'fx'))
    pc=piece(name,fr,total,audio);pc['cues']=[(lead+a,lead+b,disp[i]) for i,(a,b) in enumerate(al)];return pc,ratio
