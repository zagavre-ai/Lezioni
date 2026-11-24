from lib import *
from slides import CSS as SLIDE_CSS
DARK='''
body.dark{background:#0B1530;color:#fff}
.bgl{position:absolute;inset:0;overflow:hidden}
.glow{position:absolute;border-radius:50%;filter:blur(90px)}
.it{position:absolute;opacity:0}
.k2{font:700 30px Fig;letter-spacing:.18em;color:#FFE600;text-transform:uppercase}
.big{font:800 96px/1.05 Bri;color:#fff;letter-spacing:-.01em}
.mid{font:800 70px/1.1 Bri;color:#fff}
.line{position:relative;border:3px solid rgba(255,255,255,.28);border-radius:22px;padding:22px 40px 22px 70px;margin-bottom:22px;font:600 42px/1.4 Fig;color:#fff;background:rgba(255,255,255,.05)}
.line .dot{position:absolute;left:28px;top:36px;width:22px;height:22px;border-radius:50%;background:rgba(255,255,255,.35)}
.line.on{border:6px solid #FFE600;padding:19px 37px 19px 67px;background:rgba(255,230,0,.10);box-shadow:0 0 0 6px rgba(255,230,0,.22)}
.line.on .dot{background:#FFE600}
.line.dim{opacity:.62}
.opt{position:relative;border:3px solid rgba(255,255,255,.35);border-radius:20px;padding:20px 40px 20px 100px;margin-bottom:20px;font:600 40px/1.35 Fig;color:#fff;background:rgba(255,255,255,.06)}
.opt .L{position:absolute;left:30px;top:16px;width:52px;height:52px;border-radius:50%;background:#fff;color:#0B1530;font:800 32px/52px Fig;text-align:center}
.opt.ok{border:6px solid #FFE600;background:rgba(255,230,0,.16);box-shadow:0 0 0 6px rgba(255,230,0,.25)}
.opt.ko{opacity:.45}
.mark{position:absolute;right:30px;top:18px;font:800 44px Fig;color:#FFE600}
.bar{position:absolute;left:0;top:0;height:10px;background:#FFE600}
'''
BGJS='''
function bg(t){var g=document.querySelectorAll('.glow');
 g.forEach(function(e,i){var a=t*6.2831853/12+i*2.1;e.style.transform='translate('+(Math.sin(a)*130)+'px,'+(Math.cos(2*a)*80)+'px)';});}
function ease(x){x=Math.max(0,Math.min(1,x));return 1-Math.pow(1-x,3)}
'''
def dark_page(items,extra_js='',dark=True,css_extra='',transparent=False):
    """items: [{'id','html','x','y','w','t_in','t_out'(opz),'fade'(opz)}] ; window.ACT = [(id, t_on, t_off)] per classi on"""
    h=[f'<!doctype html><meta charset=utf-8><style>{BASE}{SLIDE_CSS}{DARK}{css_extra}</style><body class="{"dark" if dark else ""}" {'style="background:transparent"' if transparent else ''}>']
    if dark and not transparent:
        h.append('<div class=bgl><div class=glow style="left:-200px;top:-150px;width:900px;height:900px;background:rgba(32,96,175,.55)"></div>'
                 '<div class=glow style="right:-250px;bottom:-250px;width:1000px;height:1000px;background:rgba(32,96,175,.38)"></div>'
                 '<div class=glow style="left:900px;top:300px;width:420px;height:420px;background:rgba(255,230,0,.10)"></div></div>')
    for it in items:
        st=f'left:{it.get("x",0)}px;top:{it.get("y",0)}px;' + (f'width:{it["w"]}px;' if it.get('w') else '')
        h.append(f'<div class="it" id="{it["id"]}" style="{st}">{it["html"]}</div>')
    sched=[[it['id'],it.get('t_in',0),it.get('t_out',1e9),it.get('fade',0.45),it.get('rise',22)] for it in items]
    h.append('<script>'+BGJS+f'var S={json.dumps(sched)};'+'''
function render(t){bg(t);var sig='';
 S.forEach(function(s){var e=document.getElementById(s[0]);var p=ease((t-s[1])/s[3]);var q=1-ease((t-s[2])/0.35);var o=Math.min(p,q);
  e.style.opacity=o.toFixed(2);e.style.transform='translateY('+(s[4]*(1-p)).toFixed(0)+'px)';sig+=o.toFixed(2)});
 '''+extra_js+'''
 return sig+(window.NOBG?'':Math.floor(t*15));}
</script></body>''')
    return ''.join(h)
