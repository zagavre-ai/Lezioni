from kinds import *
from cards import pick
from lib import _dd
ORIG='/tmp/w/orig/video.mp4'
TAF='highpass=f=70,afftdn=nr=4:nf=-50,volume=5.9dB,alimiter=limit=0.89:level=0'
def teacher_audio(aud,a,d,tot):
    sh(['ffmpeg','-v','error','-y','-ss',f'{a:.3f}','-t',f'{d+0.3:.4f}','-i',ORIG,'-vn','-af',
        TAF+",atrim=start=0.030,asetpts=PTS-STARTPTS,afade=t=in:d=0.04,afade=t=out:st=%.3f:d=0.04,aformat=sample_rates=48000:channel_layouts=stereo,apad=whole_dur=%.4f,atrim=0:%.4f"%(d-0.04,tot/FPS,tot/FPS),'-ar','48000','-ac','2',aud])
def p_teacher(name,a,b,frames_rel):
    """frames_rel: list of (PIL image, dur) covering b-a seconds (bg without webcam)"""
    d=b-a
    dd,tot=video_from_frames(name,frames_rel,d)
    out=f'{PC}/{name}.v.mp4'
    fade=f"fade=t=in:st=0:d=0.4,fade=t=out:st={tot/FPS-0.4:.3f}:d=0.4"
    fc=("[0:v]fps=30,format=yuv420p[bg];[1:v]crop=180:135:853:345,scale=412:309:flags=lanczos,fps=30,eq=contrast=1.04:saturation=1.06,format=yuv420p[cam];"
        f"[bg][cam]overlay=1428:148:shortest=1,{fade}[o]")
    sh(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',f'{dd}/list.txt','-ss',f'{a:.3f}','-t',f'{d+0.5:.3f}','-i',ORIG,
        '-filter_complex',fc,'-map','[o]','-frames:v',str(tot),'-c:v','libx264','-preset','veryfast','-crf','19','-pix_fmt','yuv420p','-r','30','-an',out])
    aud=f'{PC}/{name}.wav'
    teacher_audio(aud,a,d,tot)
    shutil.rmtree(dd,ignore_errors=True)
    return dict(name=name,v=out,a=aud,dur=tot/FPS,src=(a,b))
def group_pages(pk):
    pages=[];cur=[]
    for t,x in pk:
        if len(cur)<3 and fits([c[1] for c in cur]+[x]): cur.append((t,x))
        else: pages.append(cur);cur=[(t,x)]
    if cur: pages.append(cur)
    return pages
def teacher_states(a,b,label,title,picks,kw,page0):
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
    return fr,info,pg
# ---------------- maps
BES={'center':((255,224,200),(232,120,70)),'key':((255,243,190),(214,170,20)),'plain':((208,240,222),(60,160,110)),
     'cons':((228,220,248),(130,100,200)),'date':((204,230,250),(60,130,200))}
LEG=[('center','Concetto centrale'),('date','Date e sequenze'),('key','Parole chiave'),('plain','Esempi e opere'),('cons','Conseguenze')]
COLX=[340,960,1580]
MAPS={
 'MAPPA1':dict(title='Quali sono i caratteri della società di massa?',
   nodes=[('c',"LA SOCIETÀ AGLI INIZI DEL NOVECENTO",'center',960,None,1000,318),
          ('a',"fiducia nel progresso",'plain',480,None,540,530),
          ('b',"Belle époque",'key',480,None,540,725),
          ('m',"le masse",'key',1440,None,540,530),
          ('v',"nelle città",'cons',1170,None,440,725),
          ('s',"soggetti attivi della vita sociale",'cons',1670,None,440,725)],
   edges=[('c','a',"è caratterizzata da"),('a','b',"e viene ricordata come"),('c','m',"vede"),('m','v',"vivere"),('m','s',"diventare")],
   order=['c','a','b','m','v','s']),
 'MAPPA2':dict(title="Quali trasformazioni avvengono nell'economia all'inizio del secolo?",
   nodes=[('c',"L'ECONOMIA AGLI INIZI DEL NOVECENTO",'center',960,None,1000,318),
     ('c1',"la nascita dei consumi",'key',COLX[0],None,540,525),('c2',"l'accesso a beni durevoli",'plain',COLX[0],None,540,700),('c3',"l'aumento del tempo libero",'cons',COLX[0],None,540,875),
     ('i1',"lo sviluppo dell'industria",'plain',COLX[1],None,540,525),('i2',"la produzione di massa",'key',COLX[1],None,540,700),('i3',"la concentrazione delle industrie",'cons',COLX[1],None,540,875),
     ('a1',"una crisi agricola",'plain',COLX[2],None,540,525),('a2',"lo spopolamento delle campagne",'plain',COLX[2],None,540,700),('a3',"l'emigrazione transoceanica",'key',COLX[2],None,540,875)],
   edges=[('c','c1',"vede"),('c','i1',""),('c','a1',""),('c1','c2',"con"),('c2','c3',"e"),('i1','i2',"con"),('i2','i3',"e"),('a1','a2',"con"),('a2','a3',"e")],
   order=['c','c1','c2','c3','i1','i2','i3','a1','a2','a3']),
 'MAPPA3':dict(title="Quali trasformazioni avvengono nella politica all'inizio del secolo?",
   nodes=[('c',"LA POLITICA AGLI INIZI DEL NOVECENTO",'center',960,None,1000,318),
     ('v1',"l'ampliamento del diritto di voto",'plain',COLX[0],None,540,525),('v2',"la nascita dei partiti di massa",'key',COLX[0],None,540,700),('v3',"i partiti socialisti",'cons',COLX[0],None,540,875),
     ('h1',"un nuovo orientamento della Chiesa",'plain',COLX[1],None,540,525),('h2',"la collaborazione fra imprenditori e operai",'key',COLX[1],None,540,700),
     ('f1',"la nascita delle prime organizzazioni femministe",'key',COLX[2],None,540,525),('f2',"i diritti economici, civili e politici delle donne",'cons',COLX[2],None,540,700)],
   edges=[('c','v1',"vede"),('c','h1',""),('c','f1',""),('v1','v2',"con"),('v2','v3',"in particolare"),('h1','h2',"che propone"),('f1','f2',"che si battono per")],
   order=['c','v1','v2','v3','h1','h2','f1','f2']),
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
