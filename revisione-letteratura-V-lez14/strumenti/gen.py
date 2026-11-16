# generatore slide nel modello Spagnolo (1920x1080). Funzioni -> html
import html as H,re,os,base64
B=os.path.dirname(os.path.abspath(__file__))
LOGO='file://'+B+'/logo_blu.svg'; LOGOW='file://'+B+'/logo_bianco.svg'
MAT='LETTERATURA ITALIANA V'; PROF='Prof. Giorgio Mazzotti'
CSS="""
@font-face{font-family:Bric;font-weight:800;src:url(file://%s/fonts/BricolageGrotesque-ExtraBold.ttf)}
@font-face{font-family:Fig;font-weight:400;src:url(file://%s/fonts/Figtree-Regular.ttf)}
@font-face{font-family:Fig;font-weight:600;src:url(file://%s/fonts/Figtree-SemiBold.ttf)}
@font-face{font-family:Fig;font-weight:700;src:url(file://%s/fonts/Figtree-Bold.ttf)}
*{box-sizing:border-box;margin:0;padding:0}
body{width:1920px;height:1080px;background:#fff;position:relative;overflow:hidden;font-family:Fig,sans-serif;color:#0B1530}
.logo{position:absolute;left:80px;top:52px;width:165px}
.hl{position:absolute;left:80px;right:80px;height:1px;background:#E6E9EF}
.lab{font:700 23px Fig;letter-spacing:3px;color:#2060AF;text-transform:uppercase}
.tit{font:800 64px/1.08 Bric;letter-spacing:-1px;color:#0B1530}
.bar{width:85px;height:6px;border-radius:3px;background:#2060AF;margin-top:26px}
.foot{position:absolute;top:998px;font:700 21px Fig;letter-spacing:2.5px;color:#2060AF}
.card{background:#fff;border:1px solid #E3E8F0;border-radius:22px;box-shadow:0 14px 40px rgba(11,21,48,.08);padding:26px 38px;font:500 31px/1.38 Fig;color:#0B1530}
.card b{font-weight:700;color:#2060AF}
.mk{background:linear-gradient(transparent 38%%,#FFE600 38%%,#FFE600 92%%,transparent 92%%);padding:0 3px;margin:0 -3px}
.box{position:absolute;left:1428px;top:148px;width:412px;height:309px;border-radius:18px;background:#E9EDF3;box-shadow:0 18px 44px rgba(11,21,48,.22)}
.band{position:absolute;left:1430px;top:470px;width:413px;height:104px;background:#FFE600;border-radius:8px;transform:rotate(-3deg);box-shadow:0 10px 26px rgba(11,21,48,.18);padding:14px 22px}
.band .n{font:800 36px/1.1 Bric;color:#0B1530;letter-spacing:-.3px}
.band .r{font:700 21px/1.2 Fig;color:#0B1530;text-transform:uppercase;margin-top:6px;letter-spacing:.5px}
"""%((B,)*4)
def page(body,pag=None,prof=True,foot=True,logo=True,extra=''):
    s='<!doctype html><html><head><meta charset="utf-8"><style>'+CSS+extra+'</style></head><body>'
    if logo: s+=f'<img class="logo" src="{LOGO}"><div class="hl" style="top:124px"></div>'
    s+=body
    if prof: s+='<div class="box"></div><div class="band"><div class="n">Giorgio Mazzotti</div><div class="r">Prof. di Letteratura italiana</div></div>'
    if foot:
        s+='<div class="hl" style="top:981px"></div>'
        s+=f'<div class="foot" style="left:80px">{MAT} &nbsp;·&nbsp; {PROF}</div>'
        if pag: s+=f'<div class="foot" style="right:80px">Pagina {pag}</div>'
    return s+'</body></html>'
E=H.escape
def rich(t,active=False):
    """«**lead:** resto» -> lead in blu; se active il lead evidenziato in giallo"""
    m=re.match(r'^(.{3,90}?:)\s(.*)$',t,re.S)
    if m:
        lead=E(m.group(1));cls=' class="mk"' if active else ''
        return f'<b><span{cls}>{lead}</span></b> {E(m.group(2))}'
    return E(t)
def cards(label,title,items,active=None,pag=1,prof=True,fs=None):
    w=1305 if prof else 1760
    body=f'<div style="position:absolute;left:80px;top:146px;width:{w}px"><div class="lab">{E(label)}</div>'
    body+=f'<div class="tit" style="margin-top:34px;font-size:{58 if len(title)>48 else 64}px">{E(title)}</div><div class="bar"></div>'
    body+=f'<div style="margin-top:44px;display:flex;flex-direction:column;gap:22px">'
    for i,t in enumerate(items):
        st=f' style="font-size:{fs}px"' if fs else ''
        body+=f'<div class="card"{st}>{rich(t,active==i)}</div>'
    body+='</div></div>'
    return page(body,pag,prof)
def cover(title,args,pag=1,prof=True):
    body=f'<div style="position:absolute;left:80px;top:146px;width:1300px"><div class="lab">{MAT} · VIDEOLEZIONE</div>'
    body+=f'<div class="tit" style="margin-top:46px;font-size:92px;line-height:1.02">{E(title)}</div><div class="bar" style="margin-top:34px"></div>'
    body+='<div class="card" style="margin-top:56px;padding:30px 42px;font-size:30px"><div class="lab" style="font-size:17px;letter-spacing:2.5px;margin-bottom:18px;background:#E8EFF9;display:inline-block;padding:5px 14px;border-radius:7px">ARGOMENTI</div>'
    h=(len(args)+1)//2
    body+='<div style="display:flex;gap:46px">'
    for col in (args[:h],args[h:]):
        body+='<ul style="list-style:none;flex:1">'+''.join(f'<li style="margin:9px 0;padding-left:30px;position:relative;line-height:1.28"><span style="position:absolute;left:4px;top:13px;width:10px;height:10px;border-radius:5px;background:#2060AF"></span>{E(a)}</li>' for a in col)+'</ul>'
    body+='</div></div></div>'
    return page(body,pag,prof)
def sezione(num,nome,pag=None):
    body=f'<div style="position:absolute;left:80px;top:330px;width:1700px"><div class="lab" style="font-size:30px">ARGOMENTO {num:02d}</div><div class="tit" style="font-size:96px;margin-top:40px;line-height:1.04">{E(nome)}</div><div class="bar" style="width:140px;height:9px;margin-top:40px"></div></div>'
    return page(body,pag,prof=False)
def scrivi(nome,html,d='html'):
    open(f'{B}/{d}/{nome}.html','w',encoding='utf-8').write(html)
