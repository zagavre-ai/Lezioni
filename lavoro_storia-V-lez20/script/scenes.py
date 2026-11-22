import re, math, html, os, sys
sys.path.insert(0, '/tmp/w/b')
from lib import *
from content import *

PASTEL = dict(pesca='#FFD9C2', celeste='#CFE8FB', paglierino='#FFF3B8', menta='#CDEFDD', lilla='#E4D9F7')
BORDO = dict(pesca='#E8743B', celeste='#3A8FD6', paglierino='#D9B400', menta='#2FA36B', lilla='#8A63C9')
LEGENDA = [('pesca', 'concetto centrale'), ('celeste', 'date e sequenze'), ('paglierino', 'parole chiave'), ('menta', 'esempi e opere'), ('lilla', 'conseguenze')]
UNI = "<br>"

def plain(h): return re.sub(r'<[^>]+>', '', h)

def est_h(card_html, per_line=60, lh=60, pad=44, gap=22):
    return math.ceil(len(plain(card_html)) / per_line) * lh + pad + gap

def pages(cards, budget=690):
    """spezza le card in pagine (finestre) da max 3 card che stanno nell'altezza"""
    P = []; cur = []; h = 0
    for i, c in enumerate(cards):
        eh = est_h(c)
        if cur and (h + eh > budget or len(cur) >= 3):
            P.append(cur); cur = []; h = 0
        cur.append(i); h += eh
    if cur: P.append(cur)
    # evita card sola in ultima pagina se si puo' prendere dalla precedente
    if len(P) > 1 and len(P[-1]) == 1 and len(P[-2]) > 2:
        P[-1].insert(0, P[-2].pop())
    return P

def title_lines(t, px=58):
    return 1 if len(t) * px * 0.50 < 1290 else 2

def slide_state(arg, page_cards, active, pnum, focus=False):
    A = ARGS[arg - 1]
    tpx = 58; nl = title_lines(A['titolo'], tpx)
    eyebrow = f"ARGOMENTO {arg} · {A['nome']}".upper()
    top = 200 + nl * 70 + 26
    h = chrome(eyebrow, A['titolo'], pnum, kw=A['kw'], title_px=tpx)
    if focus:
        c = A['cards'][active]
        lead = re.sub(r'<[^>]+>', '', c.split('</b>')[0]).strip().rstrip(':')
        h = chrome(eyebrow, lead, pnum, kw=A['kw'], title_px=tpx); nl = 1; top = 200 + 70 + 26
        h += f"<div style='position:absolute;left:0;top:{top+10}px;width:1920px'><div class='card on' style='position:relative;font-size:48px;line-height:1.5;opacity:1;padding:34px 40px'><i></i>{c}</div></div>"
    else:
        cs = [A['cards'][i] for i in page_cards]
        act = page_cards.index(active) if active in page_cards else None
        h += f"<div style='position:absolute;left:0;top:{top}px;width:1920px'>"
        for k, c in enumerate(cs):
            h += f"<div class='card{' on' if k == act else ''}' style='position:relative;margin-bottom:22px{';opacity:1' if active is None else ''}'><i></i>{c}</div>"
        h += '</div>'
    return pagina(h)

def image_state(arg, imgpath, caption, pnum, iw, ih, cams=True, hint=None, title=None):
    A = ARGS[arg - 1]
    h = chrome(f"ARGOMENTO {arg} · {A['nome']}".upper(), title or caption, pnum, kw=None, title_px=54)
    # area immagine: x 80..1370, y 290..960
    aw, ah = 1290, 670
    sc = min(aw / iw, ah / ih); w = int(iw * sc); hh = int(ih * sc)
    x = 80 + (aw - w) // 2; y = 290 + (ah - hh) // 2
    h += f"<img src='file://{imgpath}' style='position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{hh}px;border-radius:14px;box-shadow:0 12px 30px rgba(60,70,90,.25)'>"
    return pagina(h)

def dark_html(eyebrow, title, lines=(), active=None, sub=None, tpx=84, lpx=44, top=None, cam=False, items_style=''):
    h = f"<div class='eyebrow' style='left:120px;top:110px'>{html.escape(eyebrow)}</div>"
    h += f"<div class='title' style='left:120px;top:170px;width:1680px;font-size:{tpx}px;color:#fff'>{title}</div>"
    if sub: h += f"<div style='position:absolute;left:120px;top:{170 + 110 * (2 if len(title) > 40 else 1)}px;font-size:36px;color:#C9D6F2;width:1500px'>{sub}</div>"
    if lines:
        t = top or (420 if len(title) < 40 else 470)
        h += f"<div style='position:absolute;left:120px;top:{t}px;width:1680px'>"
        for k, l in enumerate(lines):
            on = (k == active)
            vis = 1 if (active is None or k <= active) else 0
            h += (f"<div style='position:relative;margin-bottom:20px;padding:20px 34px;border-radius:16px;font-size:{lpx}px;line-height:1.4;"
                  f"background:rgba(255,255,255,{.16 if on else .07});border:3px solid {'#FFE600' if on else 'rgba(255,255,255,.18)'};"
                  f"color:#fff;opacity:{vis if on or k < (active if active is not None else 99) else 0};{items_style}'>"
                  f"{'<i style=position:absolute;left:-14px;top:-14px;width:30px;height:30px;border-radius:50%;background:#FFE600;border:3px_solid_#0B1530></i>' if on else ''}{l}</div>")
        h += '</div>'
    return pagina(h, dark=True)

def cover_html(args_on=8, cam=False, title_top=True):
    h = "<img class='logo' src='file://%s/assets/logo.png'><div class='hr'></div><div class='hr2'></div>" % B
    h += "<div class='foot' style='left:80px'>STORIA · VIDEOLEZIONE</div>"
    h += f"<div class='eyebrow'>STORIA · VIDEOLEZIONE</div>"
    h += f"<div class='title' style='top:190px;width:1290px;font-size:92px;color:#2060AF;line-height:1.06'>GLI ANNI NOVANTA:<br>IL MONDO POST-BIPOLARE</div>"
    h += "<div class='bar' style='top:420px'></div>"
    h += "<div style='position:absolute;left:80px;top:470px;width:1290px;background:#F6F8FC;border:2px solid #E3E8F0;border-radius:18px;padding:26px 36px;box-shadow:0 10px 26px rgba(60,70,90,.10)'>"
    h += "<div style='font-weight:800;font-size:24px;letter-spacing:.16em;color:#2060AF;margin-bottom:12px'>ARGOMENTI</div><div style='columns:2;column-gap:40px;font-size:31px;line-height:1.45;font-weight:600'>"
    for i in range(8):
        on = i < args_on
        h += f"<div style='break-inside:avoid;opacity:{1 if on else 0}'>{i + 1}. {html.escape(ARGS[i]['nome'])}</div>"
    h += "</div></div>"
    if cam: h += "<div class='cams'></div><div class='band'><b>Giorgio Mazzotti</b><span>PROF. DI STORIA</span></div>"
    return pagina(h)

def argomenti_slide(active=None, cam=True):
    h = chrome("DI COSA PARLIAMO", "Gli argomenti di oggi", 2, cam=cam, title_px=64)
    h += "<div style='position:absolute;left:80px;top:320px;width:1290px'>"
    for i, a in enumerate(ARGS):
        on = i == active
        h += (f"<div style='position:relative;margin-bottom:14px;padding:12px 30px;border-radius:14px;font-size:38px;font-weight:600;background:#fff;"
              f"border:3px solid {'#FFE600' if on else '#E3E8F0'};opacity:{1 if (active is None or on) else .6};box-shadow:0 8px 20px rgba(60,70,90,.10)'>"
              f"<span style='color:#2060AF;font-weight:800'>{i + 1}</span> &nbsp;{html.escape(a['nome'])}</div>")
    h += "</div>"
    return pagina(h)

def titolo_arg(arg, eyebrow='ARGOMENTO'):
    A = ARGS[arg - 1]
    return dark_html(f"{eyebrow} {arg}", A['nome'], tpx=100)

def quiz_scheda(arg=None, titolo=None):
    t = titolo or (f"Quiz · {ARGS[arg - 1]['nome']}")
    return dark_html("QUIZ", t, lines=["5 domande", "Per continuare serve almeno l'80% di risposte giuste"], tpx=84, lpx=44, top=470)

def logo_dark():
    return ''

# ---------- mappe ----------
def map_html(titolo_q, nodes, edges, shown, active, center_label=None):
    """nodes: dict id -> (x,y,w,h,testo,colore,bold) ; edges: lista (da,a,label,id_visibile_con) ; shown: set di id visibili ; active: set id accesi in giallo"""
    h = "<div class='eyebrow' style='left:80px;top:60px;color:#2060AF'>MAPPA</div>"
    h += f"<div style='position:absolute;left:80px;top:100px;width:1250px;font-family:Bricolage Grotesque;font-weight:800;font-size:46px;line-height:1.1;color:#2060AF'>{titolo_q}</div>"
    # legenda in alto a destra
    h += "<div style='position:absolute;right:60px;top:50px;width:430px;background:#fff;border:2px solid #E3E8F0;border-radius:14px;padding:12px 18px;box-shadow:0 6px 18px rgba(60,70,90,.12)'>"
    for c, l in LEGENDA:
        h += f"<div style='display:flex;align-items:center;font-size:24px;font-weight:600;margin:3px 0'><span style='display:inline-block;width:34px;height:22px;border-radius:6px;background:{PASTEL[c]};border:3px solid {BORDO[c]};margin-right:12px'></span>{l}</div>"
    h += "</div>"
    svg = "<svg width='1920' height='1080' style='position:absolute;left:0;top:0'><defs><marker id='ar' markerWidth='12' markerHeight='12' refX='9' refY='6' orient='auto'><path d='M1,1 L10,6 L1,11' fill='none' stroke='#0B1530' stroke-width='2'/></marker></defs>"
    lab = ''
    for e in edges:
        a, b, label, vis = e
        if vis not in shown: continue
        xa, ya, wa, ha = nodes[a][:4]; xb, yb, wb, hb = nodes[b][:4]
        # collegamento dal centro-basso/alto
        if abs((yb) - (ya + ha)) > 20 and yb > ya + ha - 5:
            x1, y1 = xa + wa / 2, ya + ha; x2, y2 = xb + wb / 2, yb
        elif yb + hb < ya + 5:
            x1, y1 = xa + wa / 2, ya; x2, y2 = xb + wb / 2, yb + hb
        elif xb > xa:
            x1, y1 = xa + wa, ya + ha / 2; x2, y2 = xb, yb + hb / 2
        else:
            x1, y1 = xa, ya + ha / 2; x2, y2 = xb + wb, yb + hb / 2
        my = (y1 + y2) / 2
        if abs(x1 - x2) > 4 and abs(y2 - y1) > 20 and y2 > y1:
            svg += f"<path d='M{x1},{y1} L{x1},{my} L{x2},{my} L{x2},{y2 - 2}' fill='none' stroke='#0B1530' stroke-width='3' marker-end='url(#ar)'/>"
            lx, ly = (x1 + x2) / 2 if False else x2, my - 6
        else:
            svg += f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2 - (2 if y2 > y1 else -2) if abs(x1-x2)<=4 else y2}' stroke='#0B1530' stroke-width='3' marker-end='url(#ar)'/>"
            lx, ly = (x1 + x2) / 2, my
        if label:
            lab += f"<div style='position:absolute;left:{lx - 150 + (0 if abs(x1-x2)<=4 else 0)}px;top:{ly - 18 if abs(x1-x2)>4 else ly - 22}px;width:300px;text-align:center;font-size:34px;font-weight:500;color:#0B1530;background:#fff;{'' if abs(x1-x2)>4 else 'width:auto;left:%dpx;padding:0 10px' % (lx + 12)}'>{label}</div>"
    svg += '</svg>'
    nh = ''
    for nid, (x, y, w, hh, txt, col, bold) in nodes.items():
        if nid not in shown: continue
        on = nid in active
        nh += (f"<div style='position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{hh}px;display:flex;align-items:center;justify-content:center;text-align:center;"
               f"border-radius:20px;border:5px solid {'#FFE600' if on else BORDO[col]};background:{'#FFF3A0' if on else PASTEL[col]};"
               f"box-shadow:{'0 0 0 6px rgba(255,230,0,.55),' if on else ''}0 8px 18px rgba(60,70,90,.18);font-size:{40 if bold else 38}px;line-height:1.2;font-weight:{800 if bold else 600};padding:8px 18px;color:#0B1530'>{txt}</div>")
    return pagina(h + svg + lab + nh)

# mappe del prof (parole identiche, nell'ordine del prof)
MAPPE_PROF = {
 1: dict(titolo="Che cosa accade in Iugoslavia dopo la fine dell'URSS (Unione Sovietica)?", arg=3,
   nodes={'c': (680, 250, 560, 100, 'IN IUGOSLAVIA', 'pesca', True), 'a': (590, 450, 740, 100, 'indipendenza di alcuni Stati', 'paglierino', True),
          'b': (680, 640, 560, 100, 'guerre civili', 'lilla', True),
          'l1': (60, 840, 540, 110, 'Croazia (1991)', 'menta', False), 'l2': (690, 840, 540, 110, 'Bosnia-Erzegovina (1992)', 'menta', False), 'l3': (1320, 840, 540, 110, 'Kosovo (1998)', 'menta', False)},
   edges=[('c', 'a', 'la', 'a'), ('a', 'b', 'causa', 'b'), ('b', 'l1', 'in', 'l1'), ('b', 'l2', 'in', 'l2'), ('b', 'l3', 'in', 'l3')],
   steps=[['c'], ['a', 'b'], ['l1', 'l2', 'l3']], voci=['MP1_0', 'MP1_1', 'MP1_2']),
 2: dict(titolo="Come si evolve la Comunità economica europea negli anni Novanta?", arg=4,
   nodes={'c': (680, 250, 560, 100, 'IN EUROPA', 'pesca', True), 'a': (590, 440, 740, 110, 'trattato di Maastricht (1992)', 'celeste', True),
          'l': (80, 680, 600, 100, "l'Unione europea", 'paglierino', True), 'l2': (80, 880, 600, 120, 'politico oltre che economico', 'menta', False),
          'r': (1240, 680, 600, 120, 'controlli sui bilanci degli Stati', 'paglierino', False), 'r2': (1240, 890, 600, 100, 'moneta unica europea', 'lilla', True)},
   edges=[('c', 'a', 'il', 'a'), ('a', 'l', 'crea', 'l'), ('l', 'l2', 'che ha carattere', 'l2'), ('a', 'r', 'introduce', 'r'), ('r', 'r2', 'per dare vita alla', 'r2')],
   steps=[['c', 'a'], ['l', 'l2'], ['r', 'r2']], voci=['MP2_0', 'MP2_1', 'MP2_2']),
 3: dict(titolo="Quali sono le vicende politiche italiane negli anni Novanta?", arg=5,
   nodes={'c': (680, 240, 560, 100, 'IN ITALIA', 'pesca', True), 'a': (590, 420, 740, 130, 'legge elettorale maggioritaria', 'paglierino', True),
          'b': (680, 610, 560, 100, 'bipolarismo', 'lilla', True),
          'l': (80, 790, 640, 130, 'la vittoria del centrodestra (1994)', 'celeste', False), 'l2': (80, 970, 640, 90, 'Silvio Berlusconi', 'menta', False),
          'r': (1200, 790, 640, 130, 'la vittoria del centrosinistra (1996)', 'celeste', False), 'r2': (1200, 970, 640, 90, 'Romano Prodi', 'menta', False)},
   edges=[('c', 'a', 'la', 'a'), ('a', 'b', 'introduce il', 'b'), ('b', 'l', 'con', 'l'), ('l', 'l2', 'guidato da', 'l2'), ('b', 'r', 'con', 'r'), ('r', 'r2', 'guidato da', 'r2')],
   steps=[['c', 'a'], ['b'], ['l', 'l2'], ['r', 'r2']], voci=['MP3_0', 'MP3_1', 'MP3_2', 'MP3_3']),
 4: dict(titolo="Che cos'è la globalizzazione e quali nuove potenze economiche si affermano?", arg=8,
   nodes={'c': (640, 240, 640, 100, 'LA GLOBALIZZAZIONE', 'pesca', True),
          'a': (60, 520, 560, 130, 'le aziende multinazionali', 'paglierino', False), 'a2': (60, 780, 560, 130, 'delocalizzano la produzione', 'lilla', False),
          'b': (680, 520, 560, 130, "l'integrazione dei mercati e della finanza", 'paglierino', True), 'b2': (680, 780, 560, 130, 'le tecnologie informatiche e telematiche', 'paglierino', True),
          'd': (1300, 520, 560, 130, "l'industrializzazione di nuovi paesi", 'lilla', False), 'd2': (1300, 780, 560, 130, 'la Cina', 'menta', False)},
   edges=[('c', 'a', 'ha per protagoniste', 'a'), ('a', 'a2', 'che', 'a2'), ('c', 'b', 'è accelerata da', 'b'), ('b', 'b2', 'favorita da', 'b2'), ('c', 'd', 'favorisce', 'd'), ('d', 'd2', 'come', 'd2')],
   steps=[['c'], ['a', 'a2'], ['b', 'b2'], ['d', 'd2']], voci=['MP4_0', 'MP4_1', 'MP4_2', 'MP4_3']),
}

# ---------- mappe costruite con le parole del prof (argomenti senza mappa del prof, e mappa finale) ----------
def own_map_html(titolo_q, centro, rami, shown, active):
    """rami: lista (testo, colore). Layout: centro al mezzo; rami in due colonne"""
    n = len(rami)
    cx, cy, cw, ch = 690, 470, 540, 140
    nodes = {'c': (cx, cy, cw, ch, centro, 'pesca', True)}
    L = [0, 1, 2] if n >= 5 else [0, 1]
    left_rows = [230, 465, 710]; right_rows = [230, 465, 710]
    slots = []
    # ordine di lettura: sinistra alto, destra alto, sinistra mezzo, destra mezzo, sinistra basso, destra basso
    order = [('L', 0), ('R', 0), ('L', 1), ('R', 1), ('L', 2), ('R', 2)]
    if n == 4: order = [('L', 0), ('R', 0), ('L', 2), ('R', 2)]
    if n == 5: order = [('L', 0), ('R', 0), ('L', 1), ('R', 2), ('L', 2)]
    for k, (txt, col) in enumerate(rami):
        side, row = order[k]
        x = 60 if side == 'L' else 1300; y = (left_rows if side == 'L' else right_rows)[row]
        nodes[f'r{k}'] = (x, y, 560, 150, txt, col, False)
    svg = "<svg width='1920' height='1080' style='position:absolute;left:0;top:0'><defs><marker id='ar' markerWidth='12' markerHeight='12' refX='9' refY='6' orient='auto'><path d='M1,1 L10,6 L1,11' fill='none' stroke='#0B1530' stroke-width='2'/></marker></defs>"
    for k in range(n):
        if f'r{k}' not in shown: continue
        x, y, w, hh = nodes[f'r{k}'][:4]
        if x < cx:  # sinistra
            x1, y1 = cx, cy + ch / 2; x2, y2 = x + w, y + hh / 2
        else:
            x1, y1 = cx + cw, cy + ch / 2; x2, y2 = x, y + hh / 2
        if abs(y2 - y1) < 12:
            svg += f"<line x1='{x1}' y1='{y1}' x2='{x2 + (4 if x2 > x1 else -4)}' y2='{y2}' stroke='#0B1530' stroke-width='3' marker-end='url(#ar)'/>"
        else:
            # esce dall'alto/basso del centro verso il ramo
            xm = cx + cw / 2 + (-150 if x < cx else 150)
            if y2 < y1: y1 = cy
            else: y1 = cy + ch
            svg += f"<path d='M{xm},{y1} L{xm},{y2} L{x2 + (4 if x2 > xm else -4)},{y2}' fill='none' stroke='#0B1530' stroke-width='3' marker-end='url(#ar)'/>"
    svg += '</svg>'
    base = map_html(titolo_q, {'c': nodes['c']}, [], {'c'}, set())  # titolo+legenda+centro
    # riusa map_html per i nodi (senza archi) poi sovrappone svg
    allnodes = {k: v for k, v in nodes.items()}
    h = map_html(titolo_q, allnodes, [], shown | {'c'}, active)
    return h.replace('</body>', svg + '</body>')

MAPPE_OWN = {
 1: dict(arg=1, voce='MAP1', titolo="Che cosa accade con il crollo dell'URSS (Unione Sovietica)?", centro="IL CROLLO DELL'URSS",
         rami=[("la fine del bipolarismo e della Guerra fredda (1991)", 'celeste'), ("la «fine della storia»: Francis Fukuyama", 'paglierino'),
               ("la transizione russa: Boris Eltsin, inflazione, impoverimento, oligarchi", 'paglierino'), ("la Cecenia: spinte separatiste e guerra", 'lilla'),
               ("Putin (1999): restaura il controllo statale", 'celeste')],
         anchors=['Primo ramo', 'Secondo ramo', 'Terzo ramo', 'Quarto ramo', 'Quinto ramo']),
 2: dict(arg=2, voce='MAP2', titolo="Che ruolo hanno gli Stati Uniti dopo il crollo dell'URSS (Unione Sovietica)?", centro="L'EGEMONIA DEGLI STATI UNITI",
         rami=[("un mondo unipolare: unica superpotenza, «poliziotto del mondo»", 'paglierino'), ("la presidenza Bush Senior (1989-1993)", 'celeste'),
               ("la Guerra del Golfo: l'Iraq di Saddam Hussein invade il Kuwait", 'menta'), ("la presidenza Clinton (1993-2001): crescita economica e accordi commerciali", 'lilla')],
         anchors=['Primo ramo', 'Secondo ramo', 'Terzo ramo', 'Quarto ramo']),
 6: dict(arg=6, voce='MAP6', titolo="Che cosa accade dopo la Guerra fredda in Medio Oriente, Africa e America Latina?", centro="MEDIO ORIENTE, AFRICA E AMERICA LATINA",
         rami=[("Israele e Palestina: gli accordi di Oslo (1993)", 'celeste'), ("l'estremismo islamico: Talebani e Al-Qaeda di Osama bin Laden", 'paglierino'),
               ("l'Africa: guerre civili e genocidio in Ruanda (1994)", 'lilla'), ("il Sudafrica: fine dell'Apartheid, Nelson Mandela presidente (1994)", 'menta'),
               ("l'America Latina: ritorno alla democrazia, tra crisi e disuguaglianze", 'paglierino')],
         anchors=['Primo ramo', 'Secondo ramo', 'Terzo ramo', 'Quarto ramo', 'Quinto ramo']),
 7: dict(arg=7, voce='MAP7', titolo="Quali sono i nuovi protagonisti dell'Asia?", centro="I NUOVI PROTAGONISTI IN ASIA",
         rami=[("la Cina: capitalismo senza democrazia dopo Tienanmen (1989)", 'paglierino'), ("le Tigri asiatiche: Corea del Sud, Taiwan, Singapore, Hong Kong", 'menta'),
               ("la crisi finanziaria del 1997", 'lilla'), ("il Giappone in stallo: stagnazione economica", 'lilla'),
               ("l'India: riforme e centro mondiale del software", 'paglierino')],
         anchors=['Primo ramo', 'Secondo ramo', 'Terzo ramo', 'Quarto ramo', 'Quinto ramo']),
 0: dict(arg=0, voce='MAPF1', titolo="Il mondo dopo la fine della Guerra fredda", centro="GLI ANNI NOVANTA",
         rami=[("il crollo dell'URSS (Unione Sovietica) chiude la Guerra fredda (1991)", 'celeste'), ("gli Stati Uniti: unica superpotenza, Guerra del Golfo", 'paglierino'),
               ("l'Europa: guerre nella ex Iugoslavia e Unione Europea a Maastricht", 'menta'), ("l'Italia: la Seconda Repubblica dopo Mani pulite", 'paglierino'),
               ("Medio Oriente, Africa, Asia: nuovi conflitti e nuovi protagonisti", 'lilla'), ("la globalizzazione: Internet e mercati", 'lilla')],
         anchors=['Il crollo', 'Gli Stati Uniti', "L'Europa", "L'Italia", 'Nel resto', 'E tutto']),
}

def dark_img_html(eyebrow, title, sentence, imgpath, iw, ih, tpx=64, lpx=42):
    h = f"<div class='eyebrow' style='left:120px;top:90px'>{html.escape(eyebrow)}</div>"
    h += f"<div class='title' style='left:120px;top:140px;width:1680px;font-size:{tpx}px;color:#fff'>{title}</div>"
    if sentence:
        h += (f"<div style='position:absolute;left:120px;top:330px;width:900px;padding:26px 34px;border-radius:18px;font-size:{lpx}px;line-height:1.45;"
              f"background:rgba(255,255,255,.16);border:3px solid #FFE600;color:#fff'>{sentence}</div>")
    aw, ah = 700, 660
    sc = min(aw / iw, ah / ih); w = int(iw * sc); hh = int(ih * sc)
    h += f"<div style='position:absolute;left:1080px;top:330px;width:720px;height:680px;background:#fff;border-radius:18px;box-shadow:0 12px 30px rgba(0,0,0,.35);display:flex;align-items:center;justify-content:center'><img src='file://{imgpath}' style='width:{w}px;height:{hh}px'></div>"
    return pagina(h, dark=True)
