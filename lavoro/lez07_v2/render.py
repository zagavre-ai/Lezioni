# Schede e slide 1920x1080 con HTML + Chromium
import json,os,re,html,sys
from playwright.sync_api import sync_playwright
sys.path.insert(0,'/home/claude/w7b')
FD='/home/claude/main/kit/tools/mappa_font'
CSS=f"""
@font-face{{font-family:Bricolage;src:url(file://{FD}/BricolageGrotesque-ExtraBold.ttf);font-weight:800}}
@font-face{{font-family:Figtree;src:url(file://{FD}/Figtree-Regular.ttf);font-weight:400}}
@font-face{{font-family:Figtree;src:url(file://{FD}/Figtree-SemiBold.ttf);font-weight:600}}
@font-face{{font-family:Figtree;src:url(file://{FD}/Figtree-Bold.ttf);font-weight:700}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1920px;height:1080px;background:#FFFFFF;font-family:Figtree,sans-serif;color:#0B1530;position:relative;overflow:hidden}}
.logo{{position:absolute;left:80px;top:48px;height:54px}}
.kick{{position:absolute;left:80px;top:134px;font-size:20px;font-weight:700;letter-spacing:.12em;color:#2060AF;text-transform:uppercase}}
.hl{{position:absolute;left:80px;top:196px;width:1250px;font:800 62px Bricolage;line-height:1.05}}
.bar{{position:absolute;left:80px;top:270px;width:84px;height:5px;background:#2060AF;border-radius:3px}}
.items{{position:absolute;left:80px;top:312px;width:1290px}}
.it{{background:#fff;border-radius:16px;padding:20px 28px 20px 84px;margin-bottom:16px;font-size:31px;line-height:1.32;color:#8A93A6;position:relative;border:3px solid #E6EBF3;box-shadow:0 4px 16px rgba(11,21,48,.06)}}
.it b{{font-weight:700}}
.it .n{{position:absolute;left:26px;top:20px;width:36px;height:36px;border-radius:18px;background:#E4ECF8;color:#2060AF;font-size:20px;font-weight:700;text-align:center;line-height:36px}}
.it.on{{color:#0B1530;border-color:#FFE600;box-shadow:0 6px 22px rgba(255,230,0,.35)}}
.it.on .n{{background:#2060AF;color:#fff}}
.it.on b{{color:#0B1530}}
.foot{{position:absolute;left:80px;right:80px;bottom:44px;border-top:1px solid #DDE4EF;padding-top:22px;font-size:19px;font-weight:700;letter-spacing:.14em;color:#2060AF;display:flex;justify-content:space-between}}
.box{{position:absolute;left:1428px;top:146px;width:410px;height:308px;border-radius:18px;background:#E9EEF6;box-shadow:0 12px 36px rgba(0,0,0,.20)}}
.tag{{position:absolute;left:1430px;top:466px;width:412px;background:#FFE600;transform:rotate(-2.5deg);padding:18px 22px 16px;border-radius:6px;line-height:1.1;box-shadow:0 8px 20px rgba(0,0,0,.16);color:#0B1530}}
.tag .a{{font:800 30px Bricolage}} .tag .b{{font-size:19px;font-weight:700;margin-top:8px;letter-spacing:.04em;text-transform:uppercase}}
.kw{{position:absolute;left:1428px;top:620px;width:412px;border-top:3px solid #2060AF;padding-top:12px}}
.kw h4{{font-size:15px;font-weight:700;letter-spacing:.14em;color:#2060AF;margin-bottom:10px}}
.kw div{{padding:5px 0;border-bottom:1px solid #DDE4EF}}
.kw .e{{font-size:27px;font-weight:700}} .kw .i{{font-size:19px;color:#5B6B86;margin-top:2px}}
"""
def md(s): return re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',html.escape(s,quote=False))
LOGO='file:///home/claude/w7b/as/Telesio_logo_blu.svg'
TAG='<div class="tag"><div class="a">Maria Vittoria Fontanesi</div><div class="b">Prof.ssa di Inglese</div></div>'
def foot(p): return f'<div class="foot"><span>INGLESE &nbsp;·&nbsp; Prof.ssa Maria Vittoria Fontanesi</span><span>Pagina {p}</span></div>' if p else ''
def slide_html(kick,title,items,cur,kws,page=None,prof=True):
    its=''
    for i,t in enumerate(items):
        its+=f'<div class="it{" on" if i==cur else ""}"><span class="n">{i+1}</span>{md(t)}</div>'
    k=''.join(f'<div><div class="e">{html.escape(e)}</div><div class="i">it. {html.escape(i)}</div></div>' for e,i in kws)
    extra='.it{font-size:28px;padding:15px 24px 15px 80px;margin-bottom:12px}.it .n{top:15px}' if len(items)>=5 else ''
    return f'''<html><head><style>{CSS}{extra}</style></head><body><img class="logo" src="{LOGO}">
<div class="kick">{html.escape(kick)}</div><div class="hl">{html.escape(title)}</div><div class="bar"></div>
<div class="items">{its}</div>{'<div class="box"></div>'+TAG if prof else ''}
<div class="kw"><h4>KEY WORDS · PAROLE CHIAVE</h4>{k}</div>
{foot(page)}</body></html>'''
BAND='<div style="position:absolute;left:0;right:0;height:96px;background:#2060AF;top:0"></div><div style="position:absolute;left:0;right:0;height:96px;background:#2060AF;bottom:0"></div>'
def card_html(big,small,bands=True,dark=False,extra=''):
    bg='#0B1530' if dark else '#FFFFFF';fg='#fff' if dark else '#0B1530'
    return f'''<html><head><style>{CSS}body{{background:{bg};color:{fg}}}
.c{{position:absolute;left:160px;right:160px;top:50%;transform:translateY(-50%);text-align:center}}
.c .b{{font:800 92px Bricolage;line-height:1.06}} .c .s{{font-size:44px;font-weight:600;margin-top:34px;color:{'#FFE600' if dark else '#2060AF'}}} .c .x{{font-size:30px;margin-top:22px;opacity:.8}}</style></head><body>{BAND if bands else ''}
<img src="{LOGO}" style="position:absolute;left:50%;top:{150 if bands else 110}px;height:70px;transform:translateX(-50%)">
<div class="c"><div class="b">{html.escape(big)}</div><div class="s">{html.escape(small)}</div>{extra}</div></body></html>'''
def cover_html(title,topics,page=1):
    lis=''.join(f'<li>{html.escape(t)}</li>' for t in topics)
    return f'''<html><head><style>{CSS}.cv{{position:absolute;left:80px;top:300px;width:1290px;background:#F7F9FC;border:2px solid #E6EBF3;border-radius:16px;padding:26px 36px;box-shadow:0 6px 20px rgba(11,21,48,.06)}}
.cv h5{{display:inline-block;font-size:16px;font-weight:700;letter-spacing:.14em;color:#2060AF;background:#E4ECF8;border-radius:8px;padding:5px 12px;margin-bottom:16px}}
.cv ul{{columns:2;column-gap:60px;padding-left:28px;font-size:32px;line-height:1.55}} .cv li::marker{{color:#2060AF}}
.hl{{top:150px;font-size:92px}} .bar{{top:262px}}</style></head><body><img class="logo" src="{LOGO}">
<div class="kick" style="top:116px">Inglese · Videolezione</div><div class="hl">{html.escape(title)}</div><div class="bar"></div>
<div class="cv"><h5>ARGOMENTI</h5><ul>{lis}</ul></div>{foot(page)}</body></html>'''
def topic_html(n,title,page):
    return f'''<html><head><style>{CSS}.hl{{top:420px;font-size:104px;width:1700px}} .bar{{top:548px;width:120px;height:8px}}</style></head><body><img class="logo" src="{LOGO}">
<div class="kick" style="top:370px">{n:02d} · Topic {n}</div><div class="hl">{html.escape(title)}</div><div class="bar"></div>{foot(page)}</body></html>'''
def shot(pg,h,out):
    open('/home/claude/w7b/sl/_t.html','w').write(h);pg.goto('file:///home/claude/w7b/sl/_t.html');pg.wait_for_timeout(150);pg.screenshot(path=out)
if __name__=='__main__':
    from content import ARG
    with sync_playwright() as p:
        b=p.chromium.launch();pg=b.new_page(viewport={'width':1920,'height':1080})
        a=ARG[0]
        shot(pg,slide_html('01 · '+a['titolo'],a['slides'][1]['t'],a['slides'][1]['items'],1,a['slides'][1]['kw']),'sl/test.png')
        shot(pg,card_html('Quiz · Business structures','5 questions · at least 80% to continue'),'sl/testq.png')
