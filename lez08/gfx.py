# generatore HTML delle slide (modello Spagnolo: fondo bianco, #0B1530, #2060AF, giallo #FFE600)
import html as H, json, re
NOME='Giorgio Mazzotti'; RUOLO="PROF. DI STORIA DELL'ARTE"; MATERIA="STORIA DELL'ARTE V"
LOGO=open('/tmp/w/b/logo.svg').read().replace('<svg ','<svg style="height:54px;width:auto" ',1)
CSS='''
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1920px;height:1080px;background:#fff;overflow:hidden;font-family:'Figtree',sans-serif;color:#0B1530}
.logo{position:absolute;left:80px;top:50px}
.rule{position:absolute;left:80px;right:80px;top:124px;height:1px;background:#E3E8F0}
.rule2{position:absolute;left:80px;right:80px;top:981px;height:1px;background:#E3E8F0}
.label{position:absolute;left:80px;top:142px;font-weight:700;font-size:25px;letter-spacing:.14em;color:#2060AF;text-transform:uppercase;white-space:nowrap}
.title{position:absolute;left:80px;top:182px;width:1290px;font-family:'Bricolage Grotesque';font-weight:800;font-size:60px;line-height:1.05;color:#0B1530}
.bar{position:absolute;left:80px;width:86px;height:6px;border-radius:3px;background:#2060AF}
.foot{position:absolute;left:80px;top:996px;font-weight:700;font-size:23px;letter-spacing:.14em;color:#2060AF}
.pag{position:absolute;right:80px;top:996px;font-weight:700;font-size:23px;letter-spacing:.1em;color:#2060AF}
#cards{position:absolute;left:80px;width:1290px}
.card{position:relative;background:#F5F8FC;border-radius:18px;padding:20px 30px 20px 54px;margin-bottom:18px;font-size:40px;line-height:1.22;box-shadow:0 8px 26px rgba(70,80,100,.13);border:6px solid transparent;color:#0B1530}
.card b{font-weight:800}
.card.dim{opacity:.5;box-shadow:0 4px 14px rgba(70,80,100,.08)}
.card.on{background:#fff;border-color:#FFE600;box-shadow:0 10px 30px rgba(70,80,100,.2)}
.card .dot{position:absolute;left:16px;top:30px;width:20px;height:20px;border-radius:50%;background:#D9DEE8}
.card.on .dot{background:#FFE600;box-shadow:0 0 0 3px #0B1530}
.cam{position:absolute;left:1428px;top:148px;width:412px;height:309px;border-radius:14px;background:#cfd6e2;box-shadow:0 12px 34px rgba(70,80,100,.28)}
.strip{position:absolute;left:1428px;top:470px;width:412px;padding:14px 22px 14px;background:#FFE600;transform:rotate(-1.6deg);box-shadow:0 10px 24px rgba(70,80,100,.25);border-radius:4px}
.strip .n{font-family:'Bricolage Grotesque';font-weight:800;font-size:36px;line-height:1.1}
.strip .r{font-weight:800;font-size:19px;letter-spacing:.06em;margin-top:4px}
.keys{position:absolute;left:1428px;top:610px;width:412px}
.keys h4{font-weight:700;font-size:22px;letter-spacing:.14em;color:#2060AF;margin-bottom:12px}
.keys span{display:block;background:#EAF1FB;border-left:8px solid #2060AF;border-radius:8px;padding:8px 16px;margin-bottom:10px;font-weight:700;font-size:29px;line-height:1.15}
.cap{position:absolute;left:80px;width:1290px;font-size:28px;font-weight:600;color:#0B1530;line-height:1.25}
.cap i{font-style:normal;font-weight:800}
'''
def esc(s): return H.escape(s,quote=False)
def card_html(t, state):
    m=re.match(r'^([^:]{2,60}):\s*(.*)$',t,re.S)
    body=f'<b>{esc(m.group(1))}:</b> {esc(m.group(2))}' if m else esc(t)
    return f'<div class="card {state}"><span class="dot"></span>{body}</div>'
def base(label,title,page,keys=None,cam=True,title_lines=1):
    ky=''
    if keys: ky='<div class="keys"><h4>PAROLE CHIAVE</h4>'+''.join(f'<span>{esc(k)}</span>' for k in keys[:5])+'</div>'
    cam_html=f'<div class="cam"></div><div class="strip"><div class="n">{NOME}</div><div class="r">{RUOLO}</div></div>' if cam else ''
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="logo">{LOGO}</div><div class="rule"></div><div class="label">{esc(label)}</div>
<div class="title" style="font-size:{60 if title_lines==1 else 52}px">{esc(title)}</div>
{cam_html}{ky}<div class="rule2"></div><div class="foot">{MATERIA}</div>{"" if page is None else f'<div class="pag">Pagina {page}</div>'}
@@BODY@@</body></html>'''
def cards_slide(label,title,cards,active,page,keys=None,mode='overview',title_lines=1):
    top=270 if title_lines==1 else 316
    bar=f'<div class="bar" style="top:{top-12}px"></div>'
    if mode=='focus' and active is not None:
        t=cards[active]
        m=re.match(r'^([^:]{2,60}):\s*(.*)$',t,re.S)
        body=f'<div class="card on" style="font-size:54px;line-height:1.2;padding:34px 40px 34px 64px;margin-top:20px"><span class="dot" style="top:48px;width:26px;height:26px"></span>'+(f'<b>{esc(m.group(1))}:</b> {esc(m.group(2))}' if m else esc(t))+'</div>'
        ch=f'<div id="cards" style="top:{top+10}px">{body}</div>'
    else:
        ch=f'<div id="cards" style="top:{top+10}px">'+''.join(card_html(c,'on' if i==active else ('dim' if active is not None else '')) for i,c in enumerate(cards))+'</div>'
    return base(label,title,page,keys,True,title_lines).replace('@@BODY@@',bar+ch)
def art_slide(label,title,caption,page,keys=None):
    # l'opera viene composta a parte (zoom lento); qui solo cornice e didascalia
    cap=f'<div class="cap" style="top:915px">{caption}</div>'
    return base(label,title,page,keys,True).replace('@@BODY@@',cap)
ART_BOX=(80,176,1290,724)  # x,y,w,h area dell'opera
