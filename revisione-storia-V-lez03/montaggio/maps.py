# Mappe del prof ridisegnate (modello BES approvato): un riquadro alla volta con la voce Kore, 34-50 px
from lib import *
import tpl
from tpl import esc
COL = {'l1': ('#FFDCC6', '#C2410C'), 'cel': ('#DCEEFB', '#1D4ED8'), 'pag': ('#FFF3BF', '#A16207'), 'men': ('#DDF3E4', '#15803D'), 'lil': ('#EBE3F7', '#6D28D9')}
MAPS = {
 1: dict(title="Quale svolta imprime Giolitti alla vita politica italiana?", tsize=46,
   voices=['MP1_1', 'MP1_2', 'MP1_3', 'MP1_4', 'MP1_5', 'MP1_6', 'MP1_7'],
   nodes=[('N1', 'LA “CRISI DI FINE SECOLO”', 'l1', 960, 215, 780, 92), ('N2', 'la vittoria dei liberali progressisti', 'pag', 960, 373, 880, 92),
          ('N3', 'Giolitti', 'pag', 960, 531, 420, 92), ('N4', "ministro dell'Interno (1901)", 'cel', 490, 701, 780, 92),
          ('N5', 'la neutralità nei conflitti sociali', 'pag', 490, 859, 800, 92), ('N6', 'presidente del Consiglio (1903-1914)', 'cel', 1430, 701, 820, 92),
          ('N7', 'riforme a favore dei ceti popolari', 'lil', 1430, 859, 820, 92)],
   edges=[('N1', 'N2', 'si risolve con'), ('N2', 'N3', 'che con'), ('N3', 'N4', 'da'), ('N3', 'N6', 'da'), ('N4', 'N5', 'sceglie'), ('N6', 'N7', 'introduce')]),
 2: dict(title="Quali sono le caratteristiche dello sviluppo economico italiano nei primi anni del Novecento?", tsize=44,
   voices=['MP2_1', 'MP2_2', 'MP2_3', 'MP2_4', 'MP2_5', 'MP2_6'],
   nodes=[('N1', 'LO SVILUPPO INDUSTRIALE', 'l1', 960, 270, 860, 100), ('N2', 'siderurgico, meccanico ed elettrico', 'pag', 330, 500, 540, 150),
          ('N3', "l'intervento dello Stato", 'pag', 960, 500, 540, 150), ('N4', '“triangolo industriale”', 'pag', 1590, 500, 540, 150),
          ('N5', 'i servizi telefonici e ferroviari', 'men', 960, 750, 540, 150), ('N6', 'la “questione meridionale”', 'lil', 1590, 750, 540, 150)],
   edges=[('N1', 'N2', 'riguarda i settori'), ('N1', 'N3', 'è favorito da'), ('N1', 'N4', 'si concentra nel'), ('N3', 'N5', 'che gestisce'), ('N4', 'N6', 'e aggrava')]),
 3: dict(title="Come Giolitti affronta le pressioni dei nazionalisti e l'avanzata dei socialisti?", tsize=44,
   voices=['MP3_1', 'MP3_2', 'MP3_3', 'MP3_4', 'MP3_5', 'MP3_6', 'MP3_7'],
   nodes=[('N1', 'GIOLITTI', 'l1', 960, 235, 520, 96), ('N2', 'pressioni di industriali e nazionalisti', 'pag', 490, 420, 800, 130),
          ('N3', 'la guerra di Libia (1911-1912)', 'cel', 490, 620, 800, 130), ('N4', 'scarsi risultati economici', 'lil', 490, 820, 800, 110),
          ('N5', 'la prevedibile avanzata dei socialisti', 'pag', 1430, 420, 800, 130), ('N6', 'un patto con i cattolici (1913)', 'cel', 1430, 620, 800, 130),
          ('N7', 'una maggioranza instabile', 'lil', 1430, 820, 800, 110)],
   edges=[('N1', 'N2', 'cede alle'), ('N2', 'N3', 'e decide'), ('N3', 'N4', 'che dà'), ('N1', 'N5', 'affronta'), ('N5', 'N6', 'con'), ('N6', 'N7', 'ma ottiene')]),
}
MCSS = tpl.BASE + '''
.b{position:absolute;display:flex;align-items:center;justify-content:center;text-align:center;border-radius:16px;padding:6px 20px;font:500 40px/1.25 Fig;color:#0B1530}
.b.l1{font:800 44px/1.2 Bri;letter-spacing:.04em}
.hl{box-shadow:0 0 0 10px #FFE600,0 12px 26px rgba(11,21,48,.22)}
.lab{position:absolute;text-transform:none;letter-spacing:0;transform:translate(-50%,-50%);background:#fff;padding:0 14px;font:600 32px/1 Fig;color:#0B1530}
#leg{position:absolute;right:80px;top:48px;display:flex;gap:22px;font:600 22px Fig;color:#0B1530}
#leg span{display:flex;align-items:center;gap:8px}#leg i{display:inline-block;width:26px;height:18px;border-radius:5px;border:3px solid}
.mt{position:absolute;left:80px;top:140px;width:1760px;font-weight:800;font-family:Bri;color:#2060AF;line-height:1.1}
svg{position:absolute;left:0;top:0}
'''
def map_html(M, upto, hl, part_label='MAPPA DEL PROFESSORE'):
    nodes = {n[0]: n for n in M['nodes']}
    order = [n[0] for n in M['nodes']]
    vis = set(order[:upto])
    leg = ''.join(f'<span><i style="background:{COL[k][0]};border-color:{COL[k][1]}"></i>{t}</span>' for k, t in
                  (('l1', 'concetto centrale'), ('cel', 'date e sequenze'), ('pag', 'parole chiave'), ('men', 'esempi e opere'), ('lil', 'conseguenze')))
    svg = '<svg width="1920" height="1080"><defs><marker id="ah" markerUnits="userSpaceOnUse" markerWidth="34" markerHeight="34" refX="30" refY="17" orient="auto"><path d="M0,3 L32,17 L0,31 z" fill="#0B1530"/></marker></defs>'
    labs = ''
    for a, b, lab in M['edges']:
        if b not in vis: continue
        na, nb = nodes[a], nodes[b]
        x1, y1 = na[3], na[4] + na[6]; x2, y2 = nb[3], nb[4]
        nch = sum(1 for e in M['edges'] if e[0] == a)
        ym = y2 - 44 if nch > 1 else (y1 + y2) / 2
        d = f'M{x1},{y1} V{ym} H{x2} V{y2}' if x1 != x2 else f'M{x1},{y1} V{y2}'
        svg += f'<path d="{d}" fill="none" stroke="#0B1530" stroke-width="5" marker-end="url(#ah)"/>'
        if nch > 1: labs += f'<div class="lab" style="left:{x2}px;top:{y2 - 24}px;font-size:30px;padding:0 8px">{esc(lab)}</div>'
        else: labs += f'<div class="lab" style="left:{x1}px;top:{(y1 + y2) / 2}px">{esc(lab)}</div>'
    svg += '</svg>'
    bx = ''
    for nid in order:
        if nid not in vis: continue
        _, txt, cl, cx, y, w, h = nodes[nid]; bg, bd = COL[cl]
        bx += f'<div class="b {cl}{" hl" if nid == hl else ""}" style="left:{cx - w / 2}px;top:{y}px;width:{w}px;height:{h}px;background:{bg};border:5px solid {bd}">{esc(txt)}</div>'
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{MCSS}</style></head><body><div class="logo">{tpl.LOGO_B}</div><div class="rule"></div>' \
           f'<div id="leg">{leg}</div><div class="mt" style="font-size:{M["tsize"]}px">{esc(M["title"])}</div>{svg}{labs}{bx}' \
           f'<div class="foot"></div><div class="fl">{tpl.MATERIA}</div><div class="fr" style="letter-spacing:.14em">{part_label}</div></body></html>'
