import json,sys,html,math
sys.path.insert(0,'/tmp/w/b')
exec(open('/tmp/w/map/mapgen.py').read().split("def layout")[0])
L=json.load(open('/tmp/w/map/layout.json'));BX=L['boxes'];SZ=L['sz']
B='/tmp/w/b'
CSS=f"""
@font-face{{font-family:Fig;src:url(file://{B}/fonts/Figtree-SemiBold.ttf);font-weight:600}}
@font-face{{font-family:FigB;src:url(file://{B}/fonts/Figtree-Bold.ttf)}}
@font-face{{font-family:Bri;src:url(file://{B}/fonts/BricolageGrotesque-ExtraBold.ttf)}}
html,body{{margin:0;width:1920px;height:1080px;background:#fff;overflow:hidden;position:relative}}
#k{{position:absolute;left:60px;top:34px;font:700 22px FigB;letter-spacing:.14em;color:#2060AF}}
#f{{position:absolute;left:60px;top:1044px;font:600 20px Fig;color:#2060AF;letter-spacing:.06em}}
#p{{position:absolute;right:60px;top:1044px;font:600 20px Fig;color:#2060AF;letter-spacing:.06em}}
#line{{position:absolute;left:60px;right:60px;top:78px;height:2px;background:#CBD5E1}}
.b{{position:absolute;box-sizing:border-box;display:flex;align-items:center;justify-content:center;text-align:center;padding:0 11px;white-space:nowrap;border-radius:14px;font-family:Fig;line-height:1.22;color:#0B1530}}
#leg{{position:absolute;right:60px;top:24px;display:flex;gap:14px;font:600 18px Fig;color:#0B1530}}
#leg span{{display:flex;align-items:center;gap:6px}}
#leg i{{display:inline-block;width:22px;height:16px;border-radius:4px;border:3px solid}}
svg{{position:absolute;left:0;top:0}}
"""
LEG='<div id="leg">'+''.join(f'<span><i style="background:{COL[k][0]};border-color:{COL[k][1]}"></i>{t}</span>' for k,t in (('l1','concetto centrale'),('cel','date e sequenze'),('pag','parole chiave'),('men','esempi e opere'),('lil','conseguenze')))+'</div>'
def rect(i): x,y,w,h=BX[i][:4];return x,y,w,h
def edge_point(src,dst):
    sx,sy,sw,sh=rect(src);dx,dy,dw,dh=rect(dst)
    cx,cy=sx+sw/2,sy+sh/2;tx,ty=dx+dw/2,dy+dh/2
    vx,vy=cx-tx,cy-ty
    t=1e9
    if vx: t=min(t,(dw/2)/abs(vx))
    if vy: t=min(t,(dh/2)/abs(vy))
    return tx+vx*t,ty+vy*t,cx,cy
def state(vis,hl,page=None,footer_prof=True):
    arrows=''
    for p,c in AR:
        if c in vis and p in vis:
            ex,ey,cx,cy=edge_point(p,c)
            ang=math.atan2(ey-cy,ex-cx)
            ux,uy=math.cos(ang),math.sin(ang);hx,hy=ex-ux*26,ey-uy*26
            px,py=-uy,ux
            tri=f'{ex},{ey} {hx+px*13},{hy+py*13} {hx-px*13},{hy-py*13}'
            arrows+=f'<line x1="{cx}" y1="{cy}" x2="{hx}" y2="{hy}" stroke="#0B1530" stroke-width="7"/><polygon points="{tri}" fill="#0B1530"/>'
    boxes=''
    for nid,t,c,col,g in N:
        if nid not in vis: continue
        x,y,w,h,lines,fs=BX[nid];bg,bd=COL[c]
        bw=5 if c=='l1' else 4
        extra='box-shadow:0 0 0 8px #FFE600,0 10px 24px rgba(11,21,48,.18);' if nid in hl else ''
        fam='font-family:Bri;font-weight:800;' if c=='l1' else ''
        boxes+=f'<div class="b" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{bg};border:{bw}px solid {bd};font-size:{fs}px;{fam}{extra}">{"<br>".join(html.escape(x) for x in lines)}</div>'
    ft='LETTERATURA ITALIANA V · Prof. Giorgio Mazzotti' if footer_prof else 'LETTERATURA ITALIANA V'
    pg=f'<div id="p">Pagina {page}</div>' if page else ''
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div id="k">MAPPA DEL PROFESSORE</div>{LEG}<div id="line"></div><svg width="1920" height="1080">{arrows}</svg>{boxes}<div id="f">{ft}</div>{pg}</body></html>'
GROUPS={}
for nid,t,c,col,g in N: GROUPS.setdefault(g,[]).append(nid)
if __name__=='__main__':
    allv=set(n[0] for n in N)
    open('/tmp/w/map/h/final.html','w').write(state(allv,set()))
