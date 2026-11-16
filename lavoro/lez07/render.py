# Schede e slide 1920x1080 con HTML + Chromium
import json,os,re,html,sys
from playwright.sync_api import sync_playwright
sys.path.insert(0,'/home/claude/w7')
FD='/home/claude/main/kit/tools/mappa_font'
CSS=f"""
@font-face{{font-family:Bricolage;src:url(file://{FD}/BricolageGrotesque-ExtraBold.ttf);font-weight:800}}
@font-face{{font-family:Figtree;src:url(file://{FD}/Figtree-Regular.ttf);font-weight:400}}
@font-face{{font-family:Figtree;src:url(file://{FD}/Figtree-SemiBold.ttf);font-weight:600}}
@font-face{{font-family:Figtree;src:url(file://{FD}/Figtree-Bold.ttf);font-weight:700}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1920px;height:1080px;background:#F4F7FB;font-family:Figtree,sans-serif;color:#0B1530;position:relative;overflow:hidden}}
.logo{{position:absolute;left:80px;top:48px;height:54px}}
.kick{{position:absolute;left:80px;top:134px;font-size:20px;font-weight:700;letter-spacing:.12em;color:#2060AF;text-transform:uppercase}}
.hl{{position:absolute;left:80px;top:196px;width:1250px;font:800 62px Bricolage;line-height:1.05}}
.bar{{position:absolute;left:80px;top:270px;width:84px;height:5px;background:#2060AF;border-radius:3px}}
.items{{position:absolute;left:80px;top:312px;width:1290px}}
.it{{background:#fff;border-radius:16px;padding:20px 28px 20px 84px;margin-bottom:16px;font-size:31px;line-height:1.32;color:#8A93A6;position:relative;border:3px solid transparent;box-shadow:0 2px 10px rgba(32,96,175,.06)}}
.it b{{font-weight:700}}
.it .n{{position:absolute;left:26px;top:20px;width:36px;height:36px;border-radius:18px;background:#E4ECF8;color:#2060AF;font-size:20px;font-weight:700;text-align:center;line-height:36px}}
.it.on{{color:#0B1530;border-color:#FFE600;box-shadow:0 6px 22px rgba(255,230,0,.35)}}
.it.on .n{{background:#2060AF;color:#fff}}
.it.on b{{color:#0B1530}}
.foot{{position:absolute;left:80px;right:80px;bottom:36px;border-top:1px solid #DDE4EF;padding-top:14px;font-size:18px;font-weight:700;letter-spacing:.1em;color:#2060AF;text-transform:uppercase}}
.box{{position:absolute;left:1428px;top:148px;width:412px;height:312px;border-radius:22px;background:#E9EEF6;box-shadow:0 8px 28px rgba(11,21,48,.18)}}
.tag{{position:absolute;left:1440px;top:452px;width:400px;background:#FFE600;transform:rotate(-2.2deg);padding:14px 20px;font-weight:800;line-height:1.15;box-shadow:0 8px 20px rgba(0,0,0,.18)}}
.tag .a{{font-size:19px}} .tag .b{{font-size:14px;margin-top:3px}} .tag .c{{font-size:17px;margin-top:3px;text-transform:uppercase}}
.kw{{position:absolute;left:1428px;top:640px;width:412px;border-top:3px solid #2060AF;padding-top:12px}}
.kw h4{{font-size:15px;font-weight:700;letter-spacing:.14em;color:#2060AF;margin-bottom:10px}}
.kw div{{padding:8px 0;border-bottom:1px solid #DDE4EF}}
.kw .e{{font-size:27px;font-weight:700}} .kw .i{{font-size:19px;color:#5B6B86;margin-top:2px}}
"""
def md(s): return re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',html.escape(s,quote=False))
LOGO='file:///home/claude/w7/as/Telesio_logo_blu.svg'
def slide_html(kick,title,items,cur,kws):
    its=''
    for i,t in enumerate(items):
        its+=f'<div class="it{" on" if i==cur else ""}"><span class="n">{i+1}</span>{md(t)}</div>'
    k=''.join(f'<div><div class="e">{html.escape(e)}</div><div class="i">it. {html.escape(i)}</div></div>' for e,i in kws)
    extra='.it{font-size:28px;padding:15px 24px 15px 80px;margin-bottom:12px}.it .n{top:15px}' if len(items)>=5 else ''
    return f'''<html><head><style>{CSS}{extra}</style></head><body><img class="logo" src="{LOGO}">
<div class="kick">{html.escape(kick)}</div><div class="hl">{html.escape(title)}</div><div class="bar"></div>
<div class="items">{its}</div><div class="box"></div>
<div class="tag"><div class="a">Prof.ssa Maria Vittoria Fontanesi</div><div class="b">Inglese</div><div class="c">Triennio Amministrazione,<br>Finanza e Marketing</div></div>
<div class="kw"><h4>KEY WORDS · PAROLE CHIAVE</h4>{k}</div>
<div class="foot">Inglese &nbsp;·&nbsp; Prof.ssa Maria Vittoria Fontanesi</div></body></html>'''
BAND='<div style="position:absolute;left:0;right:0;height:96px;background:#2060AF;top:0"></div><div style="position:absolute;left:0;right:0;height:96px;background:#2060AF;bottom:0"></div>'
def card_html(big,small,bands=True,dark=False,extra=''):
    bg='#0B1530' if dark else '#F4F7FB';fg='#fff' if dark else '#0B1530'
    return f'''<html><head><style>{CSS}body{{background:{bg};color:{fg}}}
.c{{position:absolute;left:160px;right:160px;top:50%;transform:translateY(-50%);text-align:center}}
.c .b{{font:800 92px Bricolage;line-height:1.06}} .c .s{{font-size:44px;font-weight:600;margin-top:34px;color:{'#FFE600' if dark else '#2060AF'}}} .c .x{{font-size:30px;margin-top:22px;opacity:.8}}</style></head><body>{BAND if bands else ''}
<img src="{LOGO}" style="position:absolute;left:50%;top:{150 if bands else 110}px;height:70px;transform:translateX(-50%)">
<div class="c"><div class="b">{html.escape(big)}</div><div class="s">{html.escape(small)}</div>{extra}</div></body></html>'''
def shot(pg,h,out):
    open('/home/claude/w7/sl/_t.html','w').write(h);pg.goto('file:///home/claude/w7/sl/_t.html');pg.wait_for_timeout(150);pg.screenshot(path=out)
if __name__=='__main__':
    from content import ARG
    with sync_playwright() as p:
        b=p.chromium.launch();pg=b.new_page(viewport={'width':1920,'height':1080})
        a=ARG[0]
        shot(pg,slide_html('01 · '+a['titolo'],a['slides'][1]['t'],a['slides'][1]['items'],1,a['slides'][1]['kw']),'sl/test.png')
        shot(pg,card_html('Quiz · Business structures','5 questions · at least 80% to continue'),'sl/testq.png')
