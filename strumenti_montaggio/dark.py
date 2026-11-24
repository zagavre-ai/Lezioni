from scenes import *
from kore import *
from edl import fr
from numeri import digits, gloss
import subprocess, random
FPSX=30
def act_js(act):
    return ('var ACT=%s;ACT.forEach(function(a){var e=document.querySelector("#"+a[0]+" .line, #"+a[0]+" .opt, #"+a[0]);'
            'var on=(t>=a[1]&&t<a[2]);var tgt=document.querySelector("#"+a[0]+" .line")||document.querySelector("#"+a[0]+" .opt");'
            'if(tgt){tgt.classList.toggle("on",on);tgt.classList.toggle("dim",!on&&t>=a[2]);} sig+=(on?"1":"0");});')%json.dumps(act)
BGV=f'{W}/bg_dark.mp4'
def make_bg(rend):
    if os.path.exists(BGV): return
    rend.load(dark_page([]));v=BGV+'.t.mp4'
    cmd=['ffmpeg','-v','error','-y','-f','image2pipe','-framerate','30','-i','-','-c:v','libx264','-preset','veryfast','-crf','12','-pix_fmt','yuv420p','-r','30',v]
    ff=subprocess.Popen(cmd,stdin=subprocess.PIPE)
    for i in range(360):
        rend.pg.evaluate(f'render({i/30})');ff.stdin.write(rend.pg.screenshot(type='jpeg',quality=95))
    ff.stdin.close();ff.wait();os.replace(v,BGV)
def run_scene(rend,html_,tot,audio_specs,out,hold_end=0.0):
    """testi con trasparenza sopra lo sfondo animato (loop di 12 s); audio mixato; mkv x264 crf 14 + pcm"""
    make_bg(rend)
    tot=fr(tot)
    v=out+'.v.mp4'
    rend.load(html_.replace('<body class="dark" >','<body class="dark" style="background:transparent">'))
    rend.pg.evaluate("var g=document.querySelectorAll('.bgl');g.forEach(function(e){e.remove()});document.body.style.background='transparent';document.documentElement.style.background='transparent';window.NOBG=true")
    cmd=['ffmpeg','-v','error','-y','-stream_loop','-1','-i',BGV,'-f','image2pipe','-framerate','30','-c:v','png','-i','-','-filter_complex','[0:v][1:v]overlay=0:0:shortest=1,format=yuv420p[v]',
         '-map','[v]','-c:v','libx264','-preset','veryfast','-crf','14','-r','30','-t',f'{tot:.3f}',v]
    ff=subprocess.Popen(cmd,stdin=subprocess.PIPE);n=int(round(tot*30));last=None;buf=None
    for i in range(n):
        sig=rend.pg.evaluate(f'render({i/30})')
        sig=sig[:-3] if False else sig
        if sig!=last or buf is None: buf=rend.pg.screenshot(type='png',omit_background=True);last=sig
        ff.stdin.write(buf)
    ff.stdin.close();ff.wait()
    a=out+'.a.wav';mix(audio_specs,tot,a);mux(v,a,out,tot);os.remove(v);os.remove(a)
    return tot
def still(rend,html_,t,png):
    """fotogramma finale (per dispensa) di una scena"""
    rend.load(html_);rend.pg.evaluate(f'render({t})');rend.shot(png)
# ---------- scheda titolo argomento ----------
def titolo_scene(rend,n,tit,out,png=None):
    items=[dict(id='k',html=f'<div class=k2>Argomento {n}</div>',x=160,y=330,t_in=0.5),
           dict(id='t',html=f'<div class=big style="width:1600px">{esc(tit)}</div>',x=160,y=400,t_in=0.9),
           dict(id='b',html='<div style="width:260px;height:10px;background:#FFE600;border-radius:5px"></div>',x=160,y=720,t_in=1.4)]
    h=dark_page(items)
    if png: still(rend,h,5.0,png)
    return run_scene(rend,h,3.7,[(JING['titolo'],0.2,0)],out)
# ---------- pillola di ripasso ----------
def pillola_scene(rend,n,tit,vox_intro,vox_lines,out,png=None):
    pi,dpi,_,_=voce(vox_intro)
    t=3.4+0.3;specs=[(JING['repaso'],0.1,0),(pi,t,0)];items=[];act=[]
    items.append(dict(id='k',html='<div class=k2>Ripasso · '+esc(tit)+'</div>',x=120,y=60,t_in=0.3,w=1700))
    t+=dpi+0.5
    y=150
    texts=[]
    for k,vn in enumerate(vox_lines):
        p,d,txt,_=voce(vn)
        shown=gloss(digits(txt))
        items.append(dict(id=f'L{k}',html=f'<div class=line style="font-size:40px;padding:14px 36px 14px 66px"><span class=dot style="top:26px"></span>{esc(shown)}</div>',x=120,y=0,w=1680,t_in=t-0.15))
        act.append((f'L{k}',t-0.15,t+d+0.2));specs.append((p,t,0));texts.append((shown,t,d));t+=d+0.6
    tot=t+1.1
    # posizioni verticali: dopo il rendering misuro le altezze
    js=('var yy=150;for(var i=0;i<%d;i++){var e=document.getElementById("L"+i);e.style.top=yy+"px";yy+=e.offsetHeight+16;}'%len(vox_lines))
    h=dark_page(items,extra_js=act_js(act)).replace('function render(t){',f'function render(t){{{js}',1)
    if png: still(rend,h,tot,png)
    return run_scene(rend,h,tot,specs,out)
# ---------- quiz ----------
LET='ABCD'
SIGLE={'USA':"USA = Stati Uniti d'America",'ISIS':'ISIS = Stato Islamico','BRICS':'BRICS = Brasile, Russia, India, Cina, Sudafrica','NATO':"NATO = alleanza militare occidentale",
       'UE':'UE = Unione Europea','COVID':'COVID-19 = malattia da coronavirus','MES':'MES = Meccanismo europeo di stabilità','PNRR':'PNRR = Piano nazionale di ripresa e resilienza','ONU':'ONU = Nazioni Unite','EU':'EU = Unione Europea'}
def nota_sigle(t):
    import re as _re
    f=[v for k,v in SIGLE.items() if _re.search(r'\b'+k+r'(-19)?\b',t)]
    return 'Sigle: '+'; '.join(f) if f else ''
def quiz_items(qs,seed):
    rnd=random.Random(seed);res=[]
    for q in qs:
        opts=[q['a']]+list(q['w']);rnd.shuffle(opts)
        res.append(dict(p=q['p'],o=opts,c=opts.index(q['a']),e=q['e'],n=q.get('n') or nota_sigle(q['p']+' '+q['a']+' '+' '.join(q['w'])+' '+q['e'])))
    return res
def quiz_scene(rend,kick,title,qs,out,soglia_txt,png=None,think=9.0,reveal=5.0,jingle=True,seed=1):
    """scheda introduttiva + domande: ogni domanda resta 'think' s, poi si accende la risposta giusta con la spiegazione"""
    Q=quiz_items(qs,seed);n=len(Q)
    items=[];sched=[];t=0.0
    items.append(dict(id='k0',html=f'<div class=k2>{esc(kick)}</div>',x=160,y=330,t_in=0.3,t_out=4.2,w=1600))
    items.append(dict(id='t0',html=f'<div class=big>Quiz</div>',x=160,y=395,t_in=0.5,t_out=4.2))
    items.append(dict(id='s0',html=f'<div class=mid style="font-size:50px;width:1500px;line-height:1.25">{esc(soglia_txt)}</div><div style="font:700 38px Fig;color:#FFE600;margin-top:18px">Rispondi · premi Controlla · poi Continua</div>',x=160,y=560,t_in=1.4,t_out=4.2))
    specs=[(JING['quiz'],0.5,0)] if jingle else []
    t=4.2;js=[]
    for i,q in enumerate(Q):
        t0=t;t1=t+think;t2=t1+reveal
        items.append(dict(id=f'q{i}',html=(f'<div class=k2>{esc(kick)} · domanda {i+1} di {n}</div><div style="font:800 56px/1.2 Bri;color:#fff;margin:18px 0 26px;width:1640px">{esc(q["p"])}</div>'+
            ''.join(f'<div class=opt id="o{i}_{j}"><span class=L>{LET[j]}</span>{esc(o)}<span class=mark></span></div>' for j,o in enumerate(q['o']))+
            (f'<div style="margin-top:6px;font:600 30px/1.3 Fig;color:#BFD4F2;width:1640px">{esc(q["n"])}</div>' if q['n'] else '')+
            (f'<div id=e{i} style="opacity:0;margin-top:14px;font:600 36px/1.35 Fig;color:#FFE600;width:1640px">✓ {esc(q["e"])}</div>' if q['e'] else '')),x=140,y=70,t_in=t0+0.2,t_out=t2-0.1,w=1640,fade=0.35,rise=14))
        js.append((i,q['c'],t1,t2));t=t2
    tot=t+0.6
    tk=f'{W}/voc/tick_{int(think+reveal)}.wav'
    if not os.path.exists(tk):
        sh(['ffmpeg','-v','error','-y','-f','lavfi','-i',f"aevalsrc='0.35*sin(2*PI*1100*t)*exp(-60*mod(t,1))*(1-lt(t,0.1)*0)':d={think+reveal}:s=48000",'-ar','48000','-ac','2',tk])
    for (_,_,t1_,_) in js: specs.append((tk,t1_-think+0.1,-14))
    # barra del tempo + risposta giusta
    ex=('var QS=%s;QS.forEach(function(q){var on=(t>=q[2]&&t<q[3]);var ee=document.getElementById("e"+q[0]);if(ee)ee.style.opacity=(t>=q[2]+0.2&&t<q[3])?1:0;'
        'for(var j=0;j<4;j++){var o=document.getElementById("o"+q[0]+"_"+j);if(!o)continue;o.classList.toggle("ok",on&&j==q[1]);o.classList.toggle("ko",on&&j!=q[1]);o.querySelector(".mark").textContent=(on&&j==q[1])?"✓ giusta":"";}'
        'sig+=(on?"1":"0");});'
        'var BAR=%s;var bw=0;BAR.forEach(function(b){if(t>=b[0]&&t<b[1])bw=1920*(1-(t-b[0])/(b[1]-b[0]));});bw=Math.round(bw/24)*24;document.getElementById("bar").style.width=bw+"px";sig+=Math.floor(bw/4);')%(json.dumps(js),json.dumps([(a-think,a) for (_,_,a,_) in js]))
    h=dark_page(items,extra_js=ex).replace('<div class=bgl>','<div class=bar id=bar style="z-index:9;width:0"></div><div class=bgl>',1)
    if png: still(rend,h,0.9+4.0,png)
    return run_scene(rend,h,tot,specs,out)
# ---------- carte "una frase alla volta" generiche (glossario, ripasso, riepilogo) ----------
def lista_scene(rend,kick,voci_intro,righe,out,png=None,titolo=None,size=40,chiudi=1.0):
    """righe: [(testo_schermo, nome_voce)] -> ogni riga si accende con la sua voce; voci_intro: nome voce iniziale (o None)"""
    t=0.6;specs=[];items=[];act=[]
    items.append(dict(id='k',html='<div class=k2>'+esc(kick)+'</div>',x=120,y=60,t_in=0.3,w=1700))
    if voci_intro:
        p,d,_,_=voce(voci_intro);specs.append((p,t,0));t+=d+0.5
    for k,(shown,vn) in enumerate(righe):
        p,d,_,_=voce(vn)
        items.append(dict(id=f'L{k}',html=f'<div class=line style="font-size:{size}px;padding:14px 36px 14px 66px"><span class=dot style="top:26px"></span>{shown}</div>',x=120,y=0,w=1680,t_in=t-0.15))
        act.append((f'L{k}',t-0.15,t+d+0.2));specs.append((p,t,0));t+=d+0.55
    tot=t+chiudi
    js=('var yy=140;for(var i=0;i<%d;i++){var e=document.getElementById("L"+i);e.style.top=yy+"px";yy+=e.offsetHeight+14;}'%len(righe))
    h=dark_page(items,extra_js=act_js(act)).replace('function render(t){',f'function render(t){{{js}',1)
    if png: still(rend,h,tot,png)
    return run_scene(rend,h,tot,specs,out)
