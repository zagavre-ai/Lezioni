# Modello grafico Spagnolo Lez.1 adattato a Letteratura italiana V (misure a 1920x1080)
import html as H, os
MAT='LETTERATURA ITALIANA V'; PROF='Prof. Giorgio Mazzotti'
FONT=os.path.abspath('fonts')
CSS=f"""
@font-face{{font-family:Bric;font-weight:800;src:url('file://{FONT}/BricolageGrotesque-ExtraBold.ttf')}}
@font-face{{font-family:Fig;font-weight:400;src:url('file://{FONT}/Figtree-Regular.ttf')}}
@font-face{{font-family:Fig;font-weight:600;src:url('file://{FONT}/Figtree-SemiBold.ttf')}}
@font-face{{font-family:Fig;font-weight:700;src:url('file://{FONT}/Figtree-Bold.ttf')}}
@font-face{{font-family:Mono;font-weight:400;src:url('file://{FONT}/Figtree-Bold.ttf')}}
*{{box-sizing:border-box}}
body{{margin:0;width:1920px;height:1080px;background:#fff;position:relative;overflow:hidden;font-family:Fig,sans-serif;color:#0e1a38}}
.logo{{position:absolute;left:80px;top:50px;height:54px}}
.hl{{position:absolute;left:80px;right:80px;top:124px;border-top:1px solid #e3e8f1}}
.fl{{position:absolute;left:80px;right:80px;top:981px;border-top:1px solid #e3e8f1}}
.foot{{position:absolute;left:80px;right:80px;top:996px;display:flex;justify-content:space-between;font:400 20px Mono;letter-spacing:.12em;color:#2060AF;}}
.wrap{{position:absolute;left:80px;top:146px}}
.topic{{font:400 24px Mono;letter-spacing:.16em;color:#2060AF;text-transform:uppercase;min-height:30px}}
.title{{font:800 66px/1.06 Bric;color:#0e1a38;margin-top:62px;letter-spacing:-.5px}}
.bar{{height:6px;width:85px;background:#2060AF;border-radius:3px;margin-top:18px}}
.card{{background:transparent;border:0;box-shadow:none;padding:0;margin-top:30px}}
.chip{{display:inline-block;font:400 15px Mono;letter-spacing:.16em;color:#2060AF;background:#e4edf9;border-radius:7px;padding:5px 12px;margin:6px 0 4px 12px}}
.it{{display:flex;gap:18px;align-items:flex-start;padding:14px 22px;border-radius:16px;font-size:30px;line-height:1.32;font-weight:400;background:#fff;border:1.5px solid #dde5f0;box-shadow:0 6px 20px rgba(40,60,100,.08);margin:0 0 14px 0}}
.it .dot{{flex:none;width:34px;height:34px;border-radius:50%;background:#e4edf9;color:#2060AF;margin-top:2px;font:700 19px/34px Fig;text-align:center}}
.it b{{font-weight:700}}
.it.on{{background:#fff;border:2.5px solid #f2c200;box-shadow:0 8px 24px rgba(40,60,100,.12)}}
.it.on .dot{{background:#ffe600;color:#0e1a38}}
.it.on b{{background:#ffe600}}
.k{{background:#ffe600;padding:0 5px;border-radius:4px;font-weight:700}}
.pbox{{position:absolute;left:1428px;top:148px;width:410px;height:308px;border-radius:18px;background:#e9edf3;box-shadow:0 16px 40px rgba(40,50,80,.22)}}
.tag{{position:absolute;left:1428px;top:472px;width:416px;height:104px;background:#ffe600;border-radius:10px;transform:rotate(-3deg);box-shadow:0 10px 24px rgba(40,50,80,.20);padding:18px 24px;color:#0e1a38}}
.tag .n{{font:800 36px/1.1 Bric}} .tag .r{{font:700 20px/1.2 Fig;letter-spacing:.04em;margin-top:8px;text-transform:uppercase}}
"""
def page(body,n,prof=True,extra='',css=''):
    tg='<div class="tag"><div class="n">Giorgio Mazzotti</div><div class="r">Prof. di Letteratura Italiana</div></div>'
    p=('' if (not prof or prof=='none') else (tg if prof=='tagonly' else '<div class="pbox"></div>'+tg))
    return f"""<!doctype html><meta charset=utf-8><style>{CSS}{css}</style><body>
<img class=logo src="file://{os.path.abspath('logo_blu.svg')}"><div class=hl></div>{body}{p}
<div class=fl></div><div class=foot><span>{MAT} · {PROF}</span><span>Pagina {n}</span></div>{extra}"""
def e(s): return H.escape(s)
def content(topic,title,items,active,n,prof=True,chip=None,size=None,port=None,lead=True):
    w=(1305 if prof else 1760)
    li=''
    for i,(ld,txt) in enumerate(items):
        if lead: inner=f'<b>{e(ld)}</b>'+((": "+e(txt)) if txt else '')
        else: inner=e(ld)
        li+=f'<div class="it{" on" if i==active else ""}"><div class=dot>{i+1}</div><div>{inner}</div></div>'
    img=f'<img class=port src="file://{os.path.abspath(port)}">' if port else ''
    ch=f'<span class=chip>{e(chip)}</span>' if chip else ''
    css=f".wrap{{width:{w}px}}.port{{width:250px;height:330px;object-fit:cover;border-radius:14px;margin:14px 6px 14px 14px;box-shadow:0 8px 22px rgba(30,60,110,.22);align-self:flex-start}}.cw{{display:flex}}.cl{{flex:1}}"+(f".it{{font-size:{size}px}}" if size else '')+(".it{font-size:26px;padding:11px 20px;line-height:1.28}.dot{margin-top:11px}" if (prof and len(items)>=5) else '')
    body=f'<div class=wrap><div class=topic>{e(topic)}</div><div class=title>{e(title)}</div><div class=bar></div><div class=card>{ch}<div class=cw>{img}<div class=cl>{li}</div></div></div></div>'
    return page(body,n,prof,css=css)
# ---------- altri tipi di slide ----------
def cover(items,active,n,prof=False,title="Narrativa e saggistica del primo Novecento",sub="Prof. Giorgio Mazzotti"):
    li=''.join(f'<div class="it{" on" if i==active else ""}"><div class=dot>{i+1}</div><div>{e(t)}</div></div>' for i,t in enumerate(items))
    css=".wrap{width:%dpx}.ttl{font:800 86px/1.04 Bric;margin-top:46px;letter-spacing:-.8px}.card{margin-top:44px}.it{font-size:32px;padding:11px 22px}.dot{margin-top:16px}"%(1305 if prof else 1700)
    body=f'<div class=wrap><div class=topic>{MAT} · VIDEOLEZIONE</div><div class="title ttl">{e(title)}</div><div class=bar></div><div class=card><span class=chip>ARGOMENTI</span>{li}</div></div>'
    return page(body,1,prof,css=css)
def _grid(cards,cols,shown,active,big=False):
    out=''
    for i,c in enumerate(cards):
        tag,head,body=c
        vis=i<shown
        cl='gc'+(' act' if i==active else '')
        st='' if vis else 'visibility:hidden'
        out+=f'<div class="{cl}" style="{st}"><div class=nm>{i+1}</div>'+(f'<div class=tg>{e(tag)}</div>' if tag else '')+f'<div class=gh>{e(head)}</div>'+(f'<div class=gb>{e(body)}</div>' if body else '')+'</div>'
    return f'<div class=grid style="grid-template-columns:repeat({cols},1fr)">{out}</div>'
GCSS="""
.grid{display:grid;gap:26px;margin-top:40px;width:1760px}
.gc{position:relative;background:#fff;border:1.5px solid #dde5f0;border-radius:20px;box-shadow:0 8px 26px rgba(40,60,100,.09);padding:26px 30px}
.gc.act{border:2.5px solid #f2c200;box-shadow:0 10px 30px rgba(40,60,100,.13)}
.nm{position:absolute;top:16px;right:18px;width:32px;height:32px;border-radius:50%;background:#e4edf9;color:#2060AF;font:700 18px/32px Fig;text-align:center}
.gc.act .nm{background:#ffe600;color:#0e1a38}
.tg{font:400 18px Mono;letter-spacing:.14em;color:#2060AF;text-transform:uppercase;margin-bottom:10px}
.gh{font:800 40px/1.1 Bric;color:#0e1a38}
.gh2{font:800 40px/1.1 Bric}
.gb{font:400 30px/1.3 Fig;margin-top:12px;color:#1c2a4a}

"""
def cards(topic,title,chip,cs,shown,active,n,cols=None):
    k=len(cs);cols=cols or (k if k<=3 else (2 if k==4 else 3))
    body=f'<div class=wrap style="width:1760px"><div class=topic>{e(topic)}</div><div class=title>{e(title)}</div><div class=bar></div>{_grid(cs,cols,shown,active)}</div>'
    if chip: body=body.replace('<div class=topic>',f'<div class=topic><span class=chipx>{e(chip)}</span> · ',1)
    comp=".gc{padding:16px 26px}.gh{font-size:34px}.gb{font-size:25px;margin-top:6px}.grid{gap:16px;margin-top:26px}" if (k/cols)>2.1 else ""
    return page(body,n,False,css=GCSS+".chipx{color:#2060AF}"+comp)
def sentence(topic,title,text,hi,n):
    ws=text.split(' ');out=[]
    for i,w in enumerate(ws):
        c=hi.get(i)
        out.append(f'<span class="{"k" if c=="now" else ("kd" if c else "")}">{e(w)}</span>')
    css=".sent{font:600 64px/1.32 Fig;margin-top:70px;width:1620px;color:#0e1a38}.kd{background:#cfe0f7;border-radius:6px;padding:0 6px}.k{padding:0 6px}"
    body=f'<div class=wrap style="width:1760px"><div class=topic>{e(topic)}</div><div class=title>{e(title)}</div><div class=bar></div><div class=sent>{" ".join(out)}</div></div>'
    return page(body,n,False,css=css)
def simple(chip,title,sub,n,foot=True):
    body=f'<div class=wrap style="width:1700px;top:300px"><span class=chip style="margin:0">{e(chip)}</span><div class=title style="font-size:96px;margin-top:34px">{e(title)}</div><div class=bar></div><div style="font:400 40px/1.35 Fig;margin-top:40px;color:#1c2a4a">{sub}</div></div>'
    return page(body,n,False)
