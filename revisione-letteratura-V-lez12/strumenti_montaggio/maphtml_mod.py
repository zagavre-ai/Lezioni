import sys;sys.path.insert(0,'.')
from tpl import *
import data
def maphtml(on,n,plain=False):
    on=set(on);boxes='';
    ox,oy=80,330
    for (i,t,x,y,w,h,l) in data.MAP:
        dim='' if (plain or i in on or i=='root') else 'opacity:.5;'
        if i=='aut':
            boxes+=f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;text-align:center;font:400 22px Mono;letter-spacing:.12em;color:#2060AF;{dim}">{e(t)}</div>';continue
        bg={0:'#0b1633;color:#fff',1:'#e4edf9;color:#0e1a38',2:'#fff;color:#0e1a38'}[l]
        bd='#2060AF' if l else '#0b1633'
        yl='background:#ffe600!important;color:#0e1a38!important;' if (i in on and i!='root' and not plain) else ''
        boxes+=f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;border:3px solid {bd};border-radius:16px;background:{bg};{yl}{dim}display:flex;align-items:center;justify-content:center;text-align:center;font:800 26px/1.25 Bric;padding:10px;white-space:pre-line;box-shadow:0 8px 22px rgba(30,60,110,.14)">{e(t)}</div>'
    pos={i:(x,y,w,h) for i,t,x,y,w,h,l in data.MAP}
    arr=''
    def pt(a,b):
        ax,ay,aw,ah=pos[a];bx,by,bw,bh=pos[b]
        return (ax+aw*0.35 if bx<ax else ax+aw*0.65,ay+ah+4,bx+bw*0.5,by-6) if by>ay+ah/2 else None
    for a,b in data.MAPARR:
        ax,ay,aw,ah=pos[a];bx,by,bw,bh=pos[b]
        if a=='b2': x1,y1,x2,y2=ax+aw*0.3,ay+ah+4,bx+bw-30,by-6
        elif b=='b1': x1,y1,x2,y2=ax+aw*0.25,ay+ah+4,bx+bw*0.55,by-6
        else: x1,y1,x2,y2=ax+aw*0.75,ay+ah+4,bx+bw*0.5,by-6
        arr+=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#0b1633" stroke-width="7" marker-end="url(#h)"/>'
    svg=f'<svg style="position:absolute;left:0;top:0" width="1760" height="800"><defs><marker id="h" markerWidth="6" markerHeight="6" refX="4" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#0b1633"/></marker></defs>{arr}</svg>'
    body=f'<div class=wrap style="width:1760px"><div class=topic>MAPPA CONCETTUALE DEL PROFESSORE</div><div style="position:absolute;left:0;top:66px;width:1760px;height:800px;transform:scale(.88);transform-origin:0 0">{svg}{boxes}</div></div>'
    return page(body,n,False)
