# Montaggio Letteratura V (chat D2).  uso: python3 monta.py NN fase [fase...]
# fasi: audio unita slide carte voci docente lista
import sys,os,json,re,subprocess,shutil,html
sys.path.insert(0,'/home/claude/w/bin');sys.path.insert(0,'/home/claude/v5');sys.path.insert(0,'/home/claude/lezioni/tools')
from conf import CONF;from allinea import allinea
NN=sys.argv[1];C=CONF[NN];N=C['N'];D=f'/home/claude/w/l{NN}/';os.makedirs(D+'m',exist_ok=True)
SRC=D+f'Letteratura_Lez{N}.mp4';AUD=D+'aud16.wav';FPS=30
MAT='LETTERATURA ITALIANA';DOC='Prof. Giorgio Mazzotti'
def run(c):subprocess.run(c,check=True)
def dur(f):return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)
TR=json.load(open(D+'trascr.json'));END=round(TR['durata'],2)
ARG=C['arg'];NA=len(ARG)
# ---------------------------------------------------------------- audio pulito del docente, -16 LUFS
def f_audio():
    if os.path.exists(AUD):return
    run(['ffmpeg','-y','-v','error','-i',SRC,'-vn','-af','highpass=f=80,arnndn=m=/home/claude/kitx/home/claude/kit/02_Video/sh.rnnn:mix=0.85,loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000','-ac','2','-ar','48000',AUD])
# ---------------------------------------------------------------- unità: card per argomento con i tempi
def f_unita():
    import taglio
    S={s['n']:s for s in json.load(open(D+'slides.json'))}
    U=[]
    for k,A in enumerate(ARG):
        a=taglio.snap(A['a']-0.15,AUD) if k else A['a'];b=ARG[k+1]['a'] if k+1<NA else END
        cards=[]
        for n in A['sl']:
            tit=S[n]['tx'][1][0]
            for t,bo in S[n]['tx'][2:]:
                if t=='Pagina':continue
                lab=bo.strip() if bo and t.startswith(bo.strip()[:5]) else ''
                txt=t[len(lab):].strip() if lab else t
                cards.append(dict(slide=n,tit=tit,lab=lab,txt=txt,full=t))
        r=allinea([c['full'] for c in cards],TR,a,b)
        # ancore affidabili, monotone, dentro l'argomento
        an={};last=a;ST=A.get('st',{})
        def win(i):
            n=cards[i]['slide'];ks=sorted(ST);lo=ST.get(n,a);hi=min([ST[k] for k in ks if k>n]+[b]);return lo,hi
        for i,x in enumerate(r):
            if ST and (i==0 or cards[i-1]['slide']!=cards[i]['slide']) and cards[i]['slide'] in ST:
                an[i]=max(ST[cards[i]['slide']],last+0.5) if i else max(ST[cards[i]['slide']],a);last=an[i];continue
            lo,hi=win(i) if ST else (a,b)
            if x and x[0] is not None and x[1]>=0.4 and last+3<x[0]<b-5 and lo<=x[0]<hi:an[i]=x[0];last=x[0]
        t0=a+min(8.0,(b-a)*0.05);pts=[(-1,t0)]+sorted(an.items())+[(len(cards),b-4)]
        L=[len(c['full']) for c in cards];cum=[0]
        for l in L:cum.append(cum[-1]+l)
        for i,c in enumerate(cards):
            if i in an:c['t']=round(an[i],2);c['src']='voce';continue
            p=max(x for x in pts if x[0]<i);q=min(x for x in pts if x[0]>i)
            p0=max(p[0],0);ci=cum[i]-cum[p0];cs=cum[q[0]]-cum[p0]
            c['t']=round(p[1]+(q[1]-p[1])*(ci/cs if cs else 0),2);c['src']='stima'
        if cards and cards[0]['src']=='stima':cards[0]['t']=round(t0,2)
        # pagine: stessa slide, al massimo 3 card
        pages=[];cur=[]
        for c in cards:
            if cur and (len(cur)==3 or cur[-1]['slide']!=c['slide']):pages.append(cur);cur=[]
            cur.append(c)
        if cur:pages.append(cur)
        U.append(dict(k=k+1,t=A['t'],a=round(a,2),b=round(b,2),img=A['img'],pages=pages))
    json.dump(U,open(D+'unita.json','w'),ensure_ascii=False,indent=1)
    for u in U:
        print('ARG',u['k'],u['t'],u['a'],u['b'])
        for p in u['pages']:
            for c in p:print('   %7.1f %-5s %s'%(c['t'],c['src'],c['full'][:70]))
# ---------------------------------------------------------------- grafica comune
FONTS="""@font-face{font-family:Brico;src:url(file:///root/.fonts/BricolageGrotesque-ExtraBold.ttf)}"""
CSS_BASE="""*{box-sizing:border-box;margin:0;padding:0}body{width:1920px;height:1080px;overflow:hidden;font-family:'Figtree',sans-serif}
.brico{font-family:'Bricolage Grotesque';font-weight:800}.mono{font-family:'DM Mono',monospace}"""
def shot(pages,outdir):
    """pages: lista di (nome, html) -> png 1920x1080"""
    from playwright.sync_api import sync_playwright
    os.makedirs(outdir,exist_ok=True)
    with sync_playwright() as p:
        b=p.chromium.launch();pg=b.new_page(viewport={'width':1920,'height':1080})
        for n,h in pages:
            f=f'{outdir}/{n}.png'
            if os.path.exists(f):continue
            pg.set_content('<!doctype html><meta charset=utf-8><style>'+CSS_BASE+'</style>'+h);pg.evaluate('document.fonts.ready');pg.wait_for_timeout(60)
            pg.screenshot(path=f)
        b.close()
E=html.escape
import base64
def URI(f):return 'data:image/%s;base64,'%('png' if f.endswith('png') else 'jpeg')+base64.b64encode(open(f,'rb').read()).decode()
def slide_html(u,page,act,pnum,cover=False):
    img=u['img'] if u else None
    if cover:
        body=f"""<div style="position:absolute;left:90px;top:300px;width:1340px">
<div class=mono style="font-size:30px;letter-spacing:6px;color:#2060AF">{MAT}</div>
<div class=brico style="font-size:86px;line-height:1.05;color:#0B1530;margin-top:26px">{E(C['titolo'])}</div>
<div style="height:10px;width:420px;background:#FFE600;margin-top:34px;border-radius:5px"></div>
<div style="font-size:36px;color:#0B1530;margin-top:40px;font-weight:600">{DOC}</div></div>"""
    else:
        cx=80+(380 if img else 0);cw=1440-cx
        cards=''
        for i,c in enumerate(page):
            on=i==act;done=i<act
            st=('border:4px solid #2060AF;box-shadow:0 0 0 10px rgba(255,230,0,.60);opacity:1' if on else 'border:4px solid #C9D0DC;opacity:%s'%('.55' if done else '.40'))
            lab=f'<span style="font-weight:800;color:#2060AF">{E(c["lab"])}</span> ' if c['lab'] else ''
            cards+=f"""<div style="display:flex;gap:24px;align-items:flex-start;background:#fff;border-radius:22px;padding:26px 32px;{st}">
<div style="flex:none;width:52px;height:52px;border-radius:50%;background:{'#2060AF' if on else '#C9D0DC'};color:#fff;font-weight:800;font-size:28px;display:flex;align-items:center;justify-content:center">{i+1}</div>
<div style="font-size:{34 if len(c['full'])<150 else 31}px;line-height:1.32;color:#0B1530">{lab}{E(c['txt'])}</div></div>"""
        pic=f'<img src="{URI(D+"img/"+img)}" style="position:absolute;left:80px;top:230px;width:340px;border-radius:14px;box-shadow:0 10px 30px rgba(11,21,48,.25)">' if img else ''
        body=f"""<div class=mono style="position:absolute;left:80px;top:54px;font-size:24px;letter-spacing:5px;color:#2060AF">ARGOMENTO {u['k']} · {E(u['t'].upper())}</div>
<div class=brico style="position:absolute;left:80px;top:96px;width:1380px;font-size:{54 if len(page[0]['tit'])<46 else 46}px;line-height:1.08;color:#0B1530">{E(page[0]['tit'])}</div>
<div style="position:absolute;left:80px;top:{178 if len(page[0]['tit'])<46 else 170}px;width:300px;height:8px;background:#FFE600;border-radius:4px"></div>
{pic}<div style="position:absolute;left:{cx}px;top:230px;width:{cw}px;display:flex;flex-direction:column;gap:26px">{cards}</div>"""
    right=f"""<div style="position:absolute;left:1490px;top:0;width:430px;height:1080px;background:#0B1530"></div>
<div style="position:absolute;left:1505px;top:140px;width:400px;height:224px;border-radius:16px;border:3px solid #2060AF;background:#000"></div>
<div style="position:absolute;left:1510px;top:390px;width:390px;color:#fff;font-size:30px;font-weight:700">{DOC}</div>
<div class=mono style="position:absolute;left:1510px;top:436px;width:390px;color:#C9D0DC;font-size:22px;letter-spacing:3px">{MAT}</div>
<img src="{URI("/home/claude/v5/logo_white.png")}" style="position:absolute;left:1560px;top:940px;width:290px">"""
    foot=f'<div class=mono style="position:absolute;left:80px;top:1020px;font-size:22px;color:#6b7590;letter-spacing:2px">{MAT} · {DOC} · Pagina {pnum}</div>'
    return f'<div style="position:absolute;inset:0;background:#EEF0F4"></div>{body}{right}{foot}'
def f_slide():
    U=json.load(open(D+'unita.json'));P=[('cover',slide_html(None,None,0,1,cover=True))];pn=1
    for u in U:
        for j,pg in enumerate(u['pages']):
            pn+=1
            for i in range(len(pg)):P.append((f"a{u['k']}p{j}c{i}",slide_html(u,pg,i,pn)))
    shot(P,D+'sl')
    print(len(P),'immagini')
# ---------------------------------------------------------------- pezzi del docente: slide a tempo + webcam + audio
def doc_piece(name,a,b,states):
    """states: [(t_assoluto, png)] in ordine"""
    o=D+f'm/{name}.mkv'
    if os.path.exists(o):return o
    d=b-a;lst=D+f'm/{name}.ffc';s=''
    T=[max(a,t) for t,_ in states]+[b]
    for i,(t,png) in enumerate(states):
        dd=T[i+1]-T[i]
        if dd<=0:continue
        nn=max(1,int(dd//1.0));
        for _ in range(nn):s+=f"file '{png}'\nduration {dd/nn:.4f}\n"
    s+=f"file '{states[-1][1]}'\n";open(lst,'w').write(s)
    x,y,w,h=C['cam']
    I=[i for i in json.load(open(D+'campos.json')) if i[1]-i[0]>=3];J=[]
    for i in I:
        if J and abs(J[-1][2]-i[2])<=4 and abs(J[-1][3]-i[3])<=4:J[-1][1]=i[1]
        else:J.append(list(i))
    J=[i for i in J if i[1]>a and i[0]<b];J[0][0]=a;J[-1][1]=b
    def ex(k):
        e=str(J[-1][k])
        for i in reversed(J[:-1]):e=f"if(lt(t,{i[1]-a:.2f}),{i[k]},{e})"
        return "'"+e+"'"
    x,y=ex(2),ex(3);w,h=242,132
    LT=1.3
    run(['nice','-n','5','ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',lst,'-ss','%.3f'%a,'-t','%.3f'%d,'-i',SRC,'-ss','%.3f'%a,'-t','%.3f'%d,'-i',AUD,'-filter_complex',
        f"[0:v]fps=30,format=yuv420p,trim=duration={d:.3f}[s];[1:v]fps=30,crop={w}:{h}:{x}:{y},normalize=blackpt=black:whitept=white:smoothing=30:independence=0.6:strength=0.5,scale=394:218:flags=lanczos,hqdn3d=2:2:3:3,unsharp=5:5:0.8,eq=contrast=1.05:saturation=1.1:gamma=1.04[c];[s][c]overlay=1508:143:shortest=1,tpad=start_mode=clone:start_duration={LT}:stop_mode=clone:stop_duration={LT},format=yuv420p[v];"
        f"[2:a]aformat=channel_layouts=stereo,aresample=48000,adelay={int(LT*1000)}|{int(LT*1000)},apad=pad_dur={LT}[aa]",
        '-map','[v]','-map','[aa]','-t','%.3f'%(d+2*LT),'-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-r','30','-g','60','-c:a','pcm_s16le','-ar','48000','-ac','2',o])
    return o
def f_docente():
    U=json.load(open(D+'unita.json'));out=[]
    out.append(doc_piece('D0',0.0,U[0]['a'],[(0.0,D+'sl/cover.png')]))
    for u in U:
        st=[]
        for j,pg in enumerate(u['pages']):
            for i,c in enumerate(pg):st.append((c['t'],D+f"sl/a{u['k']}p{j}c{i}.png"))
        st[0]=(u['a'],st[0][1])
        out.append(doc_piece(f"D{u['k']}",u['a'],u['b'],st));print('D',u['k'],flush=True)
if __name__=='__main__':
    for f in sys.argv[2:]:globals()['f_'+f]()
