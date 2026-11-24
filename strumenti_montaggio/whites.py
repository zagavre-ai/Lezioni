from dark import *
from numeri import gloss
from slides import slide_html, CSS as SCSS
from screens import img_uri,img_size,CAP
# ---------- approfondimento (scheda chiara senza riquadro del prof; frasi accese con la voce) ----------
APCSS='''
.ap-tag{position:absolute;left:1428px;top:148px;width:412px;border-radius:16px;background:#0B1530;color:#fff;padding:26px 28px;box-shadow:0 14px 34px rgba(60,72,98,.28)}
.ap-tag .a{font:700 22px Fig;letter-spacing:.16em;color:#FFE600}.ap-tag .b{font:800 44px/1.1 Bri;margin-top:10px}
.apimg{position:absolute;left:1428px;top:420px;width:412px;border-radius:16px;overflow:hidden;box-shadow:0 14px 34px rgba(60,72,98,.28)}
.apimg img{width:100%;display:block}
'''
def ap_scene(rend,nome,kick,tit,out,page,foto=None,png=None,tag='APPROFONDIMENTO'):
    """white page, frasi del testo voce accese man mano. foto: chiave immagine del prof (facoltativa)"""
    p,d,txt,isreal=voce(nome)
    f,tm=tempi_frasi(nome,txt,d)
    lead=0.9;cards=[gloss(digits(x)) for x in f]
    # finestre da 2 card
    wins=[];cur=[]
    for i in range(len(cards)):
        cur.append(i)
        if len(cur)==2: wins.append(cur);cur=[]
    if cur:
        if len(cur)==1 and wins: wins[-1].append(cur[0])
        else: wins.append(cur)
    # nessuna finestra oltre 3 card; altezza massima verificata via DOM sotto
    tot=lead+d+1.6
    states=[]
    for i,(a,b) in enumerate(tm):
        wi=[k for k,w in enumerate(wins) if i in w][0]
        states.append((lead+a-0.05,lead+b,wi,i))
    html=lambda wi,on: slide_html(kick,tit,[cards[i] for i in wins[wi]],None if on is None else wins[wi].index(on),None,page,prof=False)
    # costruisco una pagina sola con tutte le finestre e uso JS per mostrare/attivare
    parts=[]
    for wi,w in enumerate(wins):
        parts.append(f'<div class="win" id="w{wi}" style="display:none"><div class=cards style="left:80px;width:1300px;top:310px">'+''.join(f'<div class="card" id="c{i}"><span class=dot></span>{rich(cards[i])}</div>' for i in w)+'</div></div>')
    base=slide_html(kick,tit,None,None,None,page,prof=False)
    extra=f'<style>{APCSS}</style><div class=ap-tag><div class=a>{esc(tag)}</div><div class=b>{esc(kick.split("·")[0].strip())}</div></div>'
    if foto:
        extra+=f'<div class=apimg><img src="{img_uri(foto)}"></div>'
    js=('<script>var ST=%s;function ease(x){x=Math.max(0,Math.min(1,x));return 1-Math.pow(1-x,3)}'
        'window.NOBG=true;function render(t){var sig="";var cw=-1,ci=-1;ST.forEach(function(s){if(t>=s[0]){cw=s[2];ci=s[3]}});'
        'document.querySelectorAll(".win").forEach(function(w,k){w.style.display=(k==cw||(cw<0&&k==0))?"block":"none";});'
        'document.querySelectorAll(".card").forEach(function(c){var on=(c.id=="c"+ci);c.classList.toggle("on",on);});'
        'var cs=document.querySelectorAll(".cards");var tt=document.getElementById("tit");cs.forEach(function(e){e.style.top=(tt.offsetTop+tt.offsetHeight+30)+"px"});'
        'return cw+"_"+ci;}</script>')%json.dumps(states)
    page_html=base.replace('</body>',''.join(parts)+extra+js+'</body>')
    # frame finale per dispensa: tutte le frasi viste: mostro la prima finestra senza accesa
    rend.load(page_html)
    if png: rend.pg.evaluate('render(0)');rend.shot(png)
    v=out+'.v.mp4';cmd=['ffmpeg','-v','error','-y','-f','image2pipe','-framerate','30','-i','-','-c:v','libx264','-preset','veryfast','-crf','14','-pix_fmt','yuv420p','-r','30',v]
    ff=subprocess.Popen(cmd,stdin=subprocess.PIPE);n=int(round(fr(tot)*30));last=None;buf=None
    for i in range(n):
        sig=rend.pg.evaluate(f'render({i/30})')
        if sig!=last or buf is None: buf=rend.pg.screenshot(type='jpeg',quality=94);last=sig
        ff.stdin.write(buf)
    ff.stdin.close();ff.wait()
    a=out+'.a.wav';mix([(p,lead,0)],fr(tot),a);mux(v,a,out,fr(tot));os.remove(v);os.remove(a)
    return fr(tot)
# ---------- copertina animata (nessun riquadro del docente) ----------
def copertina_scene(rend,part,argomenti,out,png=None,voce_nome='BEN1'):
    p,d,txt,_=voce(voce_nome)
    items=[dict(id='k',html=f'<div class=k2>Storia V · Videolezione</div>',x=160,y=150,t_in=0.5),
           dict(id='t',html='<div class=big style="width:1500px;font-size:110px">Il mondo<br>dal 2001 ad oggi</div>',x=160,y=210,t_in=1.0),
           dict(id='b',html='<div style="width:260px;height:10px;background:#FFE600;border-radius:5px"></div>',x=160,y=520,t_in=1.6)]
    # gli argomenti compaiono man mano mentre la voce li nomina (tempi proporzionali al testo)
    n=len(argomenti);base=1.5+d*0.38;span=d*0.55
    for i,a_ in enumerate(argomenti):
        t=base+span*i/n
        items.append(dict(id=f'g{i}',html=f'<div class=line style="font-size:44px;width:1380px;padding:14px 30px 14px 66px"><span class=dot style="top:26px"></span>{esc(a_)}</div>',x=160,y=590+i*92,t_in=t,fade=0.5))
    tot=1.0+d+1.0
    h=dark_page(items)
    if png: still(rend,h,tot,png)
    return run_scene(rend,h,tot,[(p,1.0,0)],out)
# ---------- slide "intro del prof" (stile Spagnolo: titolo, box argomenti, riquadro) ----------
def intro_slide_html(argomenti,page,kicker='STORIA V · VIDEOLEZIONE'):
    css='''
    .ct{position:absolute;left:80px;top:196px;width:1300px;font:800 84px/1.05 Bri;color:#0B1530;letter-spacing:-.01em}
    .ct:after{content:"";display:block;width:84px;height:7px;background:#2060AF;border-radius:4px;margin-top:22px}
    .box{position:absolute;left:80px;top:480px;width:1180px;background:#F5F8FC;border:3px solid #DCE3EE;border-radius:22px;padding:26px 36px;box-shadow:0 10px 28px rgba(60,72,98,.13)}
    .box h5{margin:0 0 14px;font:800 24px Fig;letter-spacing:.16em;color:#2060AF}
    .box li{font:600 36px/1.45 Fig;margin-left:6px;color:#0B1530}
    '''
    base=slide_html(kicker,'x',None,None,None,page,prof=True).replace('<div class=tit id=tit style="font-size:56px">x</div>','')
    ul=''.join(f'<li>{esc(a_)}</li>' for a_ in argomenti)
    return base.replace('</body>',f'<style>{css}</style><div class=ct>Il mondo<br>dal 2001 ad oggi</div><div class=box><h5>ARGOMENTI</h5><ul style="margin:0;padding-left:30px">{ul}</ul></div></body>')
