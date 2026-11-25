from kinds import *
from cards import pick,slide_pick
from lib import _dd
ORIG='/tmp/w/orig/video.mp4'
TAF='highpass=f=70,afftdn=nr=4:nf=-50,volume=5.5dB,alimiter=limit=0.89:level=0'
def teacher_audio(aud,a,d,tot):
    sh(['ffmpeg','-v','error','-y','-ss',f'{a:.3f}','-t',f'{d+0.3:.4f}','-i',ORIG,'-vn','-af',
        TAF+",atrim=start=0.030,asetpts=PTS-STARTPTS,afade=t=in:d=0.04,afade=t=out:st=%.3f:d=0.04,aformat=sample_rates=48000:channel_layouts=stereo,apad=whole_dur=%.4f,atrim=0:%.4f"%(d-0.04,tot/FPS,tot/FPS),'-ar','48000','-ac','2',aud])
def slice_frames(frames,t0,t1):
    out=[];t=0.0
    for im,d in frames:
        s0,s1=t,t+d;t=s1
        lo=max(s0,t0);hi=min(s1,t1)
        if hi>lo+1e-6: out.append((im,hi-lo))
    return out
def p_teacher(name,a,b,frames_rel,CH=5400):
    d=b-a;tot=nfr(d)
    chunks=[(s,min(tot,s+CH)) for s in range(0,tot,CH)]
    outs=[]
    for ci,(f0,f1) in enumerate(chunks):
        t0=f0/FPS;t1=f1/FPS;L=t1-t0
        sl=slice_frames(frames_rel,t0,t1)
        dd,tt=video_from_frames(f'{name}_c{ci}',sl,L)
        fds=[]
        if ci==0: fds.append("fade=t=in:st=0:d=0.4")
        if ci==len(chunks)-1: fds.append(f"fade=t=out:st={tt/FPS-0.4:.3f}:d=0.4")
        fade=','.join(fds) if fds else 'null'
        fc=("[0:v]format=yuv420p[bg];[1:v]crop=182:137:859:344,scale=412:309:flags=lanczos,fps=30,eq=contrast=1.04:saturation=1.06,format=yuv420p[cam];"
            f"[bg][cam]overlay=1428:148:shortest=1,fps=30,{fade}[o]")
        out=f'{PC}/{name}_c{ci}.v.mp4'
        sh(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',f'{dd}/list.txt','-ss',f'{a+t0:.3f}','-t',f'{L+0.5:.3f}','-i',ORIG,
            '-filter_complex',fc,'-map','[o]','-frames:v',str(tt),'-c:v','libx264','-preset','veryfast','-crf','19','-pix_fmt','yuv420p','-r','30','-an',out])
        shutil.rmtree(dd,ignore_errors=True);outs.append(out)
    out=f'{PC}/{name}.v.mp4'
    lst=f'{PC}/{name}.clist.txt';open(lst,'w').write(''.join(f"file '{o}'\n" for o in outs))
    sh(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lst,'-c','copy',out])
    for o in outs: os.remove(o)
    aud=f'{PC}/{name}.wav'
    teacher_audio(aud,a,d,tot)
    return dict(name=name,v=out,a=aud,dur=tot/FPS,src=(a,b))
def group_pages(pk,title=''):
    if title: TOPY[0]=card_top(title)
    pages=[];cur=[]
    for t,x in pk:
        if len(cur)<3 and fits([c[1] for c in cur]+[x]): cur.append((t,x))
        else: pages.append(cur);cur=[(t,x)]
    if cur: pages.append(cur)
    return pages
SI='/tmp/w/simg/'
WIN={1:[(770,1282,'i-002.png',(8,30,772,580),"Gli imperi coloniali all'inizio del XX secolo")],
     2:[(1801,1858,'i-007.png',None,"Dove si trova: il Sudafrica")],
     3:[(2316,2362,'i-010.png',None,"Dove si trova: Fashoda")],
     6:[(3238,3322,'i-016.png',None,"La guerra tra Russia e Giappone (1904-1905)"),(3326,3400,'i-018.png',None,"La Domenica di sangue (1905)")],
     8:[(3900,4040,'i-022.png',None,"L'espansione degli Stati Uniti (1895-1914)")]}
def img_state(label,title,page,kw,imgfile,box):
    im=white_frame(label,title,page,True,kw)
    src=Image.open(SI+imgfile).convert('RGB')
    if imgfile=='i-002.png':
        c=src.getpixel((672,150));ImageDraw.Draw(src).rectangle((684,0,797,102),fill=c)
    if box: src=src.crop(box)
    y0=card_top(title);availh=1000-y0;availw=1290
    sc=min(availw/src.width,availh/src.height,1.6)
    sz=(int(src.width*sc),int(src.height*sc))
    big=src.resize(sz,Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.2,percent=70,threshold=2))
    x=60+(availw-sz[0])//2;y=y0+(availh-sz[1])//2
    shadow_rect(im,(x,y,x+sz[0],y+sz[1]),r=6,blur=12,off=(0,6),alpha=50)
    im.paste(big,(x,y))
    return im
def chunks_win(t0,t1,seg=75,pause=15):
    out=[];cur=t0
    while cur<t1:
        end=min(t1,cur+seg)
        if t1-end<25: end=t1
        out.append((cur,end));cur=end+pause
    return out
def splice(fr,a,wins,label,page_of,kw):
    segs=[];t=a
    for im,d in fr: segs.append([t,t+d,im]);t+=d
    for (t0,t1,imgf,box,ttl) in wins:
        cut=chunks_win(t0,t1)
        for (c0,c1) in cut:
            pg=page_of(c0);imw=img_state(label,ttl,pg,kw,imgf,box)
            new=[]
            for s0,s1,im in segs:
                if s1<=c0 or s0>=c1: new.append([s0,s1,im]);continue
                if s0<c0: new.append([s0,c0,im])
                if s1>c1: new.append([c1,s1,im])
            new.append([c0,c1,imw]);segs=sorted(new,key=lambda x:x[0])
    return [(im,e-s) for s,e,im in segs]
def teacher_states(a,b,label,title,picks,kw,page0,n=None):
    TOPY[0]=card_top(title)
    """pages of up to 3 cards. returns frames_rel, list of (page_no,cards,times) and next page number"""
    pk=[(t,digits(x)) for t,x in picks]
    pages=[];cur=[]
    for t,x in pk:
        if len(cur)<3 and fits([c[1] for c in cur]+[x]): cur.append((t,x))
        else: pages.append(cur);cur=[(t,x)]
    if cur: pages.append(cur)
    fr=[];pg=page0;info=[]
    # first state before first card
    pg_i=0
    if not pages: 
        fr.append((white_frame(label,title,pg,True,kw),b-a));return fr,[],pg+1
    t_prev=a
    for pi,page in enumerate(pages):
        cards=[c[1] for c in page]
        start=page[0][0]
        if pi==0 and start>a+0.2:
            fr.append((slide_state(label,title,pg,cards,-1,kw),start-a));t_prev=start
        for ci,(t,x) in enumerate(page):
            nxt=page[ci+1][0] if ci+1<len(page) else (pages[pi+1][0][0] if pi+1<len(pages) else b)
            fr.append((slide_state(label,title,pg,cards,ci,kw),nxt-t))
        info.append((pg,cards,[c[0] for c in page]))
        pg+=1
    # fix first: if first start<=a ensure durations sum
    tot=sum(d for _,d in fr)
    if abs(tot-(b-a))>0.01: fr[-1]=(fr[-1][0],fr[-1][1]+(b-a)-tot)
    if n in WIN:
        def page_of(t):
            for (p_,cards,times) in info:
                pass
            k=0
            for (p_,cards,times) in info:
                if times[0]<=t: k=p_
            return k or page0
        fr=splice(fr,a,WIN[n],label,page_of,kw)
    return fr,info,pg
# ---------------- maps
BES={'center':((255,224,200),(232,120,70)),'key':((255,243,190),(214,170,20)),'plain':((208,240,222),(60,160,110)),
     'cons':((228,220,248),(130,100,200)),'date':((204,230,250),(60,130,200))}
LEG=[('center','Concetto centrale'),('date','Date e sequenze'),('key','Parole chiave'),('plain','Esempi e opere'),('cons','Conseguenze')]
COLX=[330,940,1550]
C4=[250,730,1190,1670]
MAPS={
 'MAPD1':dict(title="Qual è la situazione di Regno Unito e Francia all'inizio del secolo?",
   nodes=[('c',"LE POTENZE LIBERALI",'center',960,None,760,300),
     ('ru',"Regno Unito",'key',560,None,420,470),('fr',"Francia",'key',1400,None,420,470),
     ('rs',"riforme sociali",'plain',560,None,420,640),('rep',"repubblicani e reazionari",'plain',1400,None,500,640),
     ('irl',"la questione irlandese",'plain',330,None,440,830),('gue',"la guerra contro i coloni olandesi in Africa",'cons',830,None,500,830),
     ('dre',"caso Dreyfus",'cons',1400,None,420,830)],
   edges=[('c','ru',"sono"),('c','fr',""),('ru','rs',"caratterizzato da"),('rs','irl',"e impegnato da"),('rs','gue',""),('fr','rep',"dove si scontrano"),('rep','dre',"in particolare nel")],
   order=['c','ru','rs','irl','gue','fr','rep','dre']),
 'MAPD2':dict(title="Qual è la situazione degli imperi europei?",
   nodes=[('c',"GLI IMPERI EUROPEI",'center',960,None,760,300),
     ('g',"Germania",'key',COLX[0],None,500,470),('a',"Austria-Ungheria",'key',COLX[1],None,500,470),('r',"Russia",'key',COLX[2],None,500,470),
     ('g1',"Guglielmo II",'plain',COLX[0],None,500,640),('a1',"una felice stagione culturale",'plain',COLX[1],None,500,640),('r1',"guerra contro il Giappone",'cons',COLX[2],None,500,640),
     ('g2',"una politica estera aggressiva",'cons',COLX[0],None,500,830),('a2',"le spinte autonomistiche delle minoranze",'cons',COLX[1],None,500,830),('r2',"una rivoluzione (1905)",'date',COLX[2],None,500,830)],
   edges=[('c','g',"sono"),('c','a',""),('c','r',""),('g','g1',"dove sale al trono"),('g1','g2',"che adotta"),('a','a1',"che vive"),('a1','a2',"ma è minacciata da"),('r','r1',"che è sconfitta nella"),('r1','r2',"e dove scoppia")],
   order=['c','g','g1','g2','a','a1','a2','r','r1','r2']),
 'MAPD3':dict(title="Che cosa accade nel mondo extraeuropeo?",
   nodes=[('c',"NEL MONDO EXTRAEUROPEO",'center',960,None,860,300),
     ('j',"Giappone",'key',C4[0],None,440,470),('ci',"Cina",'key',C4[1],None,440,470),('u',"USA",'key',C4[2],None,440,470),('m',"Messico",'key',C4[3],None,440,470),
     ('j1',"la modernizzazione del Paese",'plain',C4[0],None,440,640),('ci1',"la Repubblica",'plain',C4[1],None,440,640),('u1',"riforme progressiste",'plain',C4[2],None,440,640),('m1',"una rivoluzione",'plain',C4[3],None,440,640),
     ('j2',"una potenza mondiale",'cons',C4[0],None,440,830),('ci2',"una dittatura",'cons',C4[1],None,440,830),('u2',"il controllo su America Latina e Pacifico",'cons',C4[2],None,440,830),('m2',"una guerra civile",'cons',C4[3],None,440,830)],
   edges=[('c','j',"in"),('c','ci',""),('c','u',""),('c','m',""),('j','j1',"prosegue"),('j1','j2',"che diventa"),('ci','ci1',"nasce"),('ci1','ci2',"che lascia il posto a"),('u','u1',"si registrano"),('u1','u2',"e cresce"),('m','m1',"scoppia"),('m1','m2',"cui segue")],
   order=['c','j','j1','j2','ci','ci1','ci2','u','u1','u2','m','m1','m2']),
}
NF=font(FIGSB,36);NFB=font(FIGB,36);LF=font(FIG,34)
def map_layout(m):
    d=_dd;L={}
    for nid,text,kind,cx,_,w,top in m['nodes']:
        f=NFB if kind in('key','center') else NF
        if kind=='center': f=font(FIGB,38)
        ls=wrap(d,text,f,w-44);h=len(ls)*46+30
        L[nid]=dict(text=text,kind=kind,x0=cx-w//2,x1=cx+w//2,y0=top,y1=top+h,lines=ls,f=f,cx=cx)
    return L
def draw_map(m,L,shown,active,page=None):
    im=Image.new('RGB',(W,H),WHITE);d=ImageDraw.Draw(im)
    im.paste(LOGO_B,(56,34),LOGO_B)
    ft=font(BRI,46);y=130
    for l in wrap(d,m['title'],ft,1330): d.text((60,y),l,font=ft,fill=BLUE);y+=58
    # legend
    lx,ly=1440,36
    for kd,lab in LEG:
        fill,bor=BES[kd];d.rounded_rectangle((lx,ly+4,lx+44,ly+38),8,fill=fill,outline=bor,width=4);d.text((lx+60,ly),lab,font=LF,fill=NAVY);ly+=46
    d.text((56,1030),MAT,font=font(FIGB,20),fill=BLUE)
    # edges first
    for p,c,lab in m['edges']:
        if c not in shown: continue
        P,C=L[p],L[c];px=P['cx'];cx=C['cx'];y0=P['y1'];y1=C['y0'];ym=(y0+y1)//2 if abs(px-cx)>5 else y1
        ym=y1-44 if abs(px-cx)>5 else y1
        if abs(px-cx)>5 and ym<y0+10: ym=y0+10
        col=NAVY
        d.line((px,y0,px,ym),fill=col,width=4)
        if abs(px-cx)>5: d.line((px,ym,cx,ym),fill=col,width=4)
        d.line((cx,ym,cx,y1-2),fill=col,width=4)
        d.polygon([(cx-11,y1-18),(cx+11,y1-18),(cx,y1)],fill=col)
        if lab:
            if abs(px-cx)>5 and lab=='vede':
                lx_=px+16;ly_=(y0+ym)//2-18
            elif abs(px-cx)>5:
                lx_=cx+16;ly_=(ym+y1)//2-18
            else:
                lx_=cx+16;ly_=(y0+y1)//2-18
            d.text((lx_,ly_),lab,font=LF,fill=NAVY)
    for nid in m['order']:
        if nid not in shown: continue
        n=L[nid];fill,bor=BES[n['kind']]
        if nid==active: fill=YEL
        shadow_rect(im,(n['x0'],n['y0'],n['x1'],n['y1']),r=20,blur=8,off=(0,5),alpha=40)
        d.rounded_rectangle((n['x0'],n['y0'],n['x1'],n['y1']),20,fill=fill,outline=bor,width=6)
        ty=n['y0']+14
        for l in n['lines']:
            f=n['f']
            if n['kind']=='center': d.text(((n['x0']+n['x1'])/2,ty),l,font=f,fill=NAVY,anchor='ma')
            else: d.text(((n['x0']+n['x1'])/2,ty),l,font=f,fill=NAVY,anchor='ma')
            ty+=46
    return im
def p_map(name,mid,voice,hold=4.0,lead=1.0):
    m=MAPS[mid];L=map_layout(m)
    vt=TXT[voice]
    phrases=[m['title']]+[L[n]['text'] for n in m['order']]
    # center text is uppercase in the map, spoken as sentence case
    al,vdur,ratio=align(voice,[p.lower() if i==1 else p for i,p in enumerate(phrases)])
    fr=[];shown=[];total=lead+vdur+hold
    fr.append((draw_map(m,L,[],None),lead+al[1][0]))
    for i,nid in enumerate(m['order']):
        s=lead+al[i+1][0];e=lead+(al[i+2][0] if i+2<len(al) else vdur)
        shown.append(nid)
        fr.append((draw_map(m,L,list(shown),nid),max(0.05,e-s)))
    fr.append((draw_map(m,L,list(shown),None),hold))
    tot=sum(d for _,d in fr)
    audio=[(TRANS,0.0,-8,'fx'),(vpath(voice),lead,vgain(vpath(voice)),'voice'),(TRANS,lead+vdur+0.6,-8,'fx')]
    pc=piece(name,fr,total,audio);pc['cues']=[(lead+al[0][0],lead+al[0][1],m['title'])]+[(lead+al[i+1][0],lead+al[i+1][1],L[n]['text'].capitalize() if n=='c' else L[n]['text']) for i,n in enumerate(m['order'])]
    return pc,ratio,draw_map(m,L,list(m['order']),None)
def p_media(name,src,kind='sigla'):
    out=f'{PC}/{name}.v.mp4';aud=f'{PC}/{name}.wav'
    dur=float(sh(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',src]).stdout)
    tot=nfr(dur)
    sh(['ffmpeg','-v','error','-y','-i',src,'-vf',f'fps=30,format=yuv420p','-frames:v',str(tot),'-c:v','libx264','-preset','veryfast','-crf','19','-pix_fmt','yuv420p','-r','30','-an',out])
    sh(['ffmpeg','-v','error','-y','-i',src,'-vn','-af',f'aformat=sample_rates=48000:channel_layouts=stereo,apad=whole_dur={tot/FPS:.4f},atrim=0:{tot/FPS:.4f}','-ar','48000','-ac','2',aud])
    return dict(name=name,v=out,a=aud,dur=tot/FPS)
