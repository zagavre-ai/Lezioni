import os, json, hashlib
from playwright.sync_api import sync_playwright
MATERIA="Tecnologie dei materiali e dei processi produttivi e organizzativi della moda"
PROF="Prof.ssa Piera Caputi"
CSS=open('/home/claude/prod/base.css').read()
EXTRA="""
.wrap{position:absolute;left:60px;top:250px;width:1300px;display:flex;flex-direction:column;gap:26px}
.card{position:relative;opacity:1;transform:none;transition:none}
.card.old{opacity:.5}
.ti{position:absolute;left:60px;top:104px;width:1300px;font:800 58px/1.08 Bri;color:#0B1530}
.nome{position:absolute;left:1455px;top:500px;width:370px;padding:10px 0;text-align:center;background:#FFE600;color:#0B1530;font:700 30px FigB;transform:rotate(-3deg);border-radius:4px}
.ruolo{position:absolute;left:1440px;top:566px;width:400px;text-align:center;font:600 19px/1.25 FigS;color:#2060AF}
.pk{position:absolute;left:1455px;top:720px;width:380px}
.pk h4{margin:0 0 10px;font:700 22px FigB;letter-spacing:.1em;color:#2060AF}
.pk span{display:block;margin:0 0 6px;padding:4px 14px;border-radius:10px;background:#FFF8B0;border:2px solid #E6C800;font:700 27px FigB;color:#0B1530}
.foot{font-size:19px}
"""
def pagina(label,title,cards,attivo,chips=()):
    c=''.join(f'<div class="card{" on" if i==attivo else (" old" if i<attivo else "")}">{h}</div>' for i,h in enumerate(cards[:attivo+1]))
    pk=''.join(f'<span>{x}</span>' for x in chips[:5])
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{EXTRA}</style></head><body>
<div class="k">{label}</div><div class="rule"></div><div class="ti">{title}</div>
<div class="wrap">{c}</div>
<div class="nome">{PROF}</div><div class="ruolo">{MATERIA}<br>Tecnico Sistema Moda · III anno</div>
{('<div class="pk"><h4>PAROLE CHIAVE</h4>'+pk+'</div>') if chips else ''}
<div class="foot">{MATERIA.upper()} · {PROF}</div></body></html>"""
class R:
    def __enter__(s):
        s.p=sync_playwright().start(); s.b=s.p.chromium.launch(executable_path='/opt/pw-browsers/chromium',args=['--no-sandbox']); s.pg=s.b.new_page(viewport={'width':1920,'height':1080}); return s
    def __exit__(s,*a): s.b.close(); s.p.stop()
    def png(s,html,out):
        f='/home/claude/prod/_tmp.html'; open(f,'w').write(html); s.pg.goto('file://'+f); s.pg.wait_for_timeout(150); s.pg.screenshot(path=out); return out
