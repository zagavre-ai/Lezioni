# Mappe del docente ridisegnate (modello BES): ramo per ramo con la voce
import sys, math, json
sys.path.insert(0, '/tmp/claude-0/w/build')
from scenes import *

COL = {'c': ((255, 220, 200), (200, 70, 30)), 'd': ((220, 235, 251), (32, 96, 208)), 'k': ((255, 241, 194), (168, 101, 10)),
       'e': ((221, 242, 226), (30, 138, 74)), 'q': ((234, 226, 247), (106, 51, 200))}
LEG = [('c', 'concetto centrale'), ('d', 'date e sequenze'), ('k', 'parole chiave'), ('e', 'esempi e opere'), ('q', 'conseguenze')]
INK = NAVY

class Node:
    def __init__(s, id, text, kind, cx, cy, w, size=34, shape='box', bold=False):
        s.id, s.text, s.kind, s.cx, s.cy, s.w, s.size, s.shape, s.bold = id, text, kind, cx, cy, w, size, shape, bold
        im = Image.new('RGBA', (10, 10)); d = ImageDraw.Draw(im); f = F('bold' if bold else 'med', size)
        if kind == 'lab': s.lines = wrap(d, text, f, w); pad = 4
        else: s.lines = wrap(d, text, f, w - 36); pad = 10
        lw = max(d.textlength(l, font=f) for l in s.lines)
        if kind == 'lab': s.w = int(lw) + 16
        elif shape == 'ellipse': s.w = max(int(lw) + 70, 120)
        else: s.w = min(w, int(lw) + 40)
        s.lh = int(size * 1.16); s.h = len(s.lines) * s.lh + 2 * pad + (14 if shape == 'ellipse' else 0)
    @property
    def box(s): return (s.cx - s.w / 2, s.cy - s.h / 2, s.cx + s.w / 2, s.cy + s.h / 2)

def edge_pt(n, tx, ty):
    """punto sul bordo del nodo n lungo la direzione verso (tx,ty)"""
    dx, dy = tx - n.cx, ty - n.cy
    if dx == 0 and dy == 0: return n.cx, n.cy
    hw, hh = n.w / 2 + 6, n.h / 2 + 6
    k = min(hw / abs(dx) if dx else 1e9, hh / abs(dy) if dy else 1e9)
    return n.cx + dx * k, n.cy + dy * k

def draw_node(im, n, lit=False, alpha=1.0, scale=1.0):
    if n.kind == 'lab':
        d = ImageDraw.Draw(im); f = F('semi', n.size); y = n.cy - len(n.lines) * n.lh / 2
        x0, y0, x1, y1 = n.box; d.rectangle((x0 - 6, y0 + 4, x1 + 6, y1 - 4), fill=(255, 255, 255))
        for l in n.lines:
            d.text((n.cx - d.textlength(l, font=f) / 2, y), l, font=f, fill=INK); y += n.lh
        return
    fill, line = COL[n.kind]
    if lit: fill = YEL
    layer = Image.new('RGBA', im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(layer)
    x0, y0, x1, y1 = n.box
    if scale != 1.0:
        cx, cy = n.cx, n.cy; x0, x1 = cx + (x0 - cx) * scale, cx + (x1 - cx) * scale; y0, y1 = cy + (y0 - cy) * scale, cy + (y1 - cy) * scale
    if n.shape == 'ellipse': d.ellipse((x0, y0, x1, y1), fill=fill, outline=line, width=5)
    else: d.rounded_rectangle((x0, y0, x1, y1), 18, fill=fill, outline=line, width=5)
    if scale == 1.0:
        f = F('bold' if n.bold else 'med', n.size); y = n.cy - len(n.lines) * n.lh / 2 - 2
        for l in n.lines:
            d.text((n.cx - d.textlength(l, font=f) / 2, y), l, font=f, fill=INK); y += n.lh
    overlay_alpha(im, layer, alpha)

def arrow(im, p0, p1, prog=1.0, head=True):
    d = ImageDraw.Draw(im, 'RGBA'); x0, y0 = p0; x1, y1 = p1
    L = math.hypot(x1 - x0, y1 - y0)
    if L < 1: return
    ux, uy = (x1 - x0) / L, (y1 - y0) / L
    ex, ey = x0 + (x1 - x0) * prog, y0 + (y1 - y0) * prog
    hs = 22 if head else 0
    d.line((x0, y0, ex - ux * (hs * .8 if prog >= .999 else 0), ey - uy * (hs * .8 if prog >= .999 else 0)), fill=INK, width=5)
    if head and prog >= .999:
        nx, ny = -uy, ux
        d.polygon([(ex, ey), (ex - ux * hs + nx * hs * .5, ey - uy * hs + ny * hs * .5), (ex - ux * hs - nx * hs * .5, ey - uy * hs - ny * hs * .5)], fill=INK)

def frame_base(title, maplabel=''):
    im = Image.new('RGBA', (W, H), (255, 255, 255, 255)); d = ImageDraw.Draw(im)
    d.text((60, 34), title, font=F('title', 54), fill=NAVY)
    # legenda in alto a destra
    x = 1860; f = F('semi', 22)
    for k, t in reversed(LEG):
        tw_ = d.textlength(t, font=f); x -= tw_; d.text((x, 98), t, font=f, fill=INK)
        x -= 40; fill, line = COL[k]; d.rounded_rectangle((x, 100, x + 30, 124), 6, fill=fill, outline=line, width=3); x -= 28
    d.line((60, 138, 1860, 138), fill=LINE, width=2)
    spaced(d, (60, 1046), MATERIA, F('bold', 20), BLUE, 3)
    return im

def poly_arrow(im, pts, prog=1.0, head=True):
    d = ImageDraw.Draw(im, 'RGBA')
    Ls = [math.hypot(pts[i+1][0]-pts[i][0], pts[i+1][1]-pts[i][1]) for i in range(len(pts)-1)]
    tot = sum(Ls); goal = tot * prog; acc = 0
    for i, L in enumerate(Ls):
        if goal <= acc: break
        f = min(1.0, (goal - acc) / L) if L else 1
        x0, y0 = pts[i]; x1, y1 = pts[i+1]
        last = (i == len(Ls) - 1)
        ex, ey = x0 + (x1 - x0) * f, y0 + (y1 - y0) * f
        if last and head and prog >= .999 and L:
            ux, uy = (x1 - x0) / L, (y1 - y0) / L; hs = 22
            d.line((x0, y0, ex - ux * hs * .8, ey - uy * hs * .8), fill=INK, width=5)
            nx, ny = -uy, ux
            d.polygon([(ex, ey), (ex - ux * hs + nx * hs * .5, ey - uy * hs + ny * hs * .5), (ex - ux * hs - nx * hs * .5, ey - uy * hs - ny * hs * .5)], fill=INK)
        else:
            d.line((x0, y0, ex, ey), fill=INK, width=5)
            if not last or f < 1: pass
        acc += L

class Map:
    def __init__(s, title, nodes, edges, steps):
        s.title = title; s.nodes = {n.id: n for n in nodes}; s.edges = edges; s.steps = steps
    def draw_edges(s, im, upto_nodes, prog=None):
        """edges: (a, b, arrowhead) ; mostra solo quelli il cui nodo b e' nell'insieme"""
        for e in s.edges:
            a, b, ah = e[:3]
            if b in upto_nodes:
                p = 1.0 if prog is None else prog.get(b, 1.0)
                na, nb = s.nodes[a], s.nodes[b]
                if len(e) > 3 and e[3] == 'elbow':
                    bx = e[4]; pts = [(na.box[2], na.cy), (bx, na.cy), (bx, nb.cy), (nb.box[0] - 6, nb.cy)]
                    poly_arrow(im, pts, p, ah)
                    continue
                p0 = edge_pt(na, nb.cx, nb.cy); p1 = edge_pt(nb, na.cx, na.cy)
                arrow(im, p0, p1, p, ah)
    def static(s, lit=None):
        im = frame_base(s.title); s.draw_edges(im, set(s.nodes))
        for n in s.nodes.values(): draw_node(im, n, lit=(lit == n.id))
        return im

def map_scene(sid, M, vname, frs, lead=0.8, hold=4.0):
    """frs: lista (frammento di testo voce, [id nodi]) ; il primo frammento e' la domanda del titolo (nodi [])"""
    v = voice(vname); fr = [f for f, _ in frs]; times = frags(vname, fr)
    N = int(math.ceil((lead + v['span'][1] + 0.4 + hold) * FPS)); e = Enc(OUT + 'seg/%s.mp4' % sid)
    track = np.zeros(N * 1600 + SR, np.float32); place(track, v['a'], lead, 1.0)
    t_node = {}; lit_win = {}
    for j, (_, ids) in enumerate(frs):
        t0 = lead + times[j][0]; t1 = lead + times[j][1]
        for k, nid in enumerate(ids):
            ts = t0 + k * min(0.9, (t1 - t0) / max(1, len(ids)))
            t_node[nid] = ts; lit_win[nid] = (ts, ts + min(max(1.0, (t1 - t0) / max(1, len(ids))), 3.0) if len(ids) > 1 else t1)
    t_end_speech = lead + v['span'][1]
    for i in range(N):
        t = i / FPS; im = frame_base(M.title)
        shown = {n for n, ts in t_node.items() if t >= ts - 0.15}
        prog = {n: ease((t - (ts - 0.15)) / 0.5) for n, ts in t_node.items()}
        M.draw_edges(im, shown, prog)
        for nid in shown:
            n = M.nodes[nid]; ts = t_node[nid]
            a = ease((t - (ts + 0.25)) / 0.3)
            if a <= 0: continue
            lit = lit_win[nid][0] <= t < lit_win[nid][1] if n.kind != 'lab' else False
            draw_node(im, n, lit=lit, alpha=a, scale=0.9 + 0.1 * a if a < 1 else 1.0) if n.kind != 'lab' else draw_node(im, n, alpha=a)
        e.put(im)
    return finish(sid, e.close(), track, dict(kind='mappa', real=v['real'], title=M.title, t_end_speech=t_end_speech))
