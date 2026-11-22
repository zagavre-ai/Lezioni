#!/usr/bin/env python3
"""Mappe concettuali del prof (Storia V, lez.14): pezzi MAP1, MAP2, MAP3.
Modello grafico: scambio-mazzotti/correzioni_22-11/modello_mappa_BES (HTML + render a stati).

uso:  python3 lez14/mappe.py            -> usa le voci vere MB1..MB3 se ci sono, altrimenti silenzio provvisorio
      python3 lez14/mappe.py 1 3        -> solo le mappe indicate
      python3 lez14/mappe.py --prova    -> PROVA di sincronia con le vecchie voci MA1..MA3 (mai nel pezzo finale):
                                           scrive in /tmp/w/wk/mappe/prova/, non tocca /tmp/w/pezzi
Rilanciando quando arriva la voce vera: trascrive la voce (cache accanto al wav), allinea le parole ai riquadri,
rifà frame, audio e pezzo. Esce: /tmp/w/pezzi/MAPn.mkv/.json, MAPn_finale.png, MAPn.svg.
"""
import json, os, re, subprocess, sys, difflib, math, unicodedata, html as H

W = '/tmp/w'; VOX = W + '/vox/scambio/storia-V-lez14/vox'; WK = W + '/wk/mappe'; PZ = W + '/pezzi'
HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(HERE)
V0 = 0.3          # la voce parte a +0,3 s
TAIL = 0.35       # il riquadro resta giallo 0,35 s dopo la fine della voce
HOLD = 4.0        # mappa intera ferma 4 s (senza giallo) alla fine

# ---------- colori BES: (sfondo, bordo) ----------
COL = {'pes': ('#FFDCC6', '#C2410C'),   # concetto centrale
       'cel': ('#DCEEFB', '#1D4ED8'),   # date e sequenze
       'pag': ('#FFF3BF', '#A16207'),   # parole chiave
       'men': ('#DDF3E4', '#15803D'),   # esempi e opere
       'lil': ('#EBE3F7', '#6D28D9')}   # conseguenze
LEGENDA = [('pes', 'concetto centrale'), ('cel', 'date e sequenze'), ('pag', 'parole chiave'), ('men', 'esempi e opere'), ('lil', 'conseguenze')]

# ---------- dati delle mappe (testo del prof) ----------
# box: id, colore, cx, top, w, h, righe   |  arrow: id, punti, etichetta, (lx,ly) | nota: testo righe sotto/accanto al riquadro
# step: (riquadro, [frecce], frase iniziale letta dalla voce)
MAPPE = {
 1: dict(titolo='Qual è il nuovo clima internazionale dopo la guerra?', voce='MB1', prova='MA1', dy=0, rootfont=46,
   boxes=[('B1','pes',960,170,640,90,['DOPO LA GUERRA']),
          ('B2','cel',360,450,560,140,['l’Organizzazione delle','Nazioni Unite (1945)']),
          ('B3','pag',960,450,560,140,['il declino delle potenze','europee']),
          ('B4','pag',1560,450,560,140,['l’affermazione di due','superpotenze']),
          ('B5','pag',360,760,560,130,['evitare nuove guerre']),
          ('B6','lil',1560,760,560,130,['la guerra fredda'])],
   arrows=[('A1',[(960,260),(960,345),(360,345),(360,446)],'nasce',(360,398)),
           ('A2',[(960,260),(960,446)],'si assiste a',(960,400)),
           ('A3',[(960,345),(1560,345),(1560,446)],None,None),
           ('A4',[(360,590),(360,756)],'con il compito di',(360,673)),
           ('A5',[(1560,590),(1560,756)],'tra le quali si crea',(1560,673))],
   note=[],
   steps=[('B1',[],'Qual è'),('B2',['A1'],'nasce l’Organizzazione'),('B5',['A4'],'con il compito'),
          ('B3',['A2'],'Si assiste'),('B4',['A3'],'e all’affermazione'),('B6',['A5'],'tra le quali')]),
 2: dict(titolo='Qual è la situazione dell’Europa nel quadro della guerra fredda?', voce='MB2', prova='MA2', dy=0, rootfont=46,
   boxes=[('B1','pes',960,165,480,80,['L’EUROPA']),
          ('B2','pag',500,380,560,120,['degli Stati Uniti','(occidente)']),
          ('B3','pag',1500,380,560,120,['dell’Unione Sovietica','(oriente)']),
          ('B4','men',330,590,500,120,['aiuti economici','(piano Marshall)']),
          ('B5','men',880,590,500,120,['un’alleanza militare','(NATO)']),
          ('B6','pag',1500,590,560,120,['il modello socialista']),
          ('B7','cel',330,790,500,150,['un processo di','integrazione economica','(CEE, 1957)']),
          ('B8','cel',1500,790,560,120,['i tentativi di autonomia','(Ungheria, 1956)'])],
   arrows=[('A1',[(960,245),(960,315),(500,315),(500,376)],'è sotto l’influenza',(960,280)),
           ('A2',[(960,315),(1500,315),(1500,376)],None,None),
           ('A3',[(500,500),(500,555),(330,555),(330,586)],'che offrono',(500,528)),
           ('A4',[(500,555),(880,555),(880,586)],None,None),
           ('A5',[(330,710),(330,786)],'che avviano',(330,748)),
           ('A6',[(1500,500),(1500,586)],'che impone',(1500,543)),
           ('A7',[(1500,710),(1500,786)],'e reprime',(1500,748))],
   note=[('N7','B7',80,948,500,['CEE = Comunità Economica Europea']),
         ('N5','B5',600,725,560,['NATO = North Atlantic','Treaty Organization, cioè','Organizzazione del Trattato','dell’Atlantico del Nord'])],
   steps=[('B1',[],'Qual è'),('B2',['A1'],'sotto l’influenza degli'),('B4',['A3'],'che offrono'),
          ('B7',['A5'],'che avviano'),('B5',['A4'],'e un’alleanza'),('B3',['A2'],'L’Europa è sotto l’influenza dell’Unione'),
          ('B6',['A6'],'che impone'),('B8',['A7'],'e reprime')]),
 3: dict(titolo='Come si estende la guerra fredda in Asia?', voce='MB3', prova='MA3', dy=0, rootfont=46,   # nessuna domanda del prof: cambiare qui il titolo
   boxes=[('B1','pes',960,150,480,90,['IN ASIA']),
          ('B2','pag',330,420,520,100,['Corea']),
          ('B3','pag',960,420,520,100,['Giappone']),
          ('B4','pag',1590,420,520,100,['Cina']),
          ('B5','cel',330,620,520,130,['la guerra tra Nord e Sud','(1950-1953)']),
          ('B6','lil',960,620,520,130,['una brillante ripresa','economica']),
          ('B7','men',1590,620,520,130,['Repubblica popolare','cinese']),
          ('B8','lil',960,850,520,130,['il principale alleato','degli USA in Asia']),
          ('B9','lil',1590,850,520,150,['sperimenta una forma','di socialismo autonoma','dall’Unione Sovietica'])],
   arrows=[('A1',[(960,240),(960,290),(330,290),(330,416)],'in',(330,353)),
           ('A2',[(960,240),(960,416)],'il',(960,353)),
           ('A3',[(960,290),(1590,290),(1590,416)],'in',(1590,353)),
           ('A4',[(330,520),(330,616)],'si combatte',(330,568)),
           ('A5',[(960,520),(960,616)],'realizza',(960,568)),
           ('A6',[(1590,520),(1590,616)],'nasce la',(1590,568)),
           ('A7',[(960,750),(960,846)],'e diventa',(960,798)),
           ('A8',[(1590,750),(1590,846)],'che',(1590,798))],
   note=[('N8','B8',700,990,520,['USA = Stati Uniti d’America'])],
   steps=[('B1',[],'In Asia'),('B2',['A1'],'In Corea'),('B5',['A4'],'si combatte'),('B3',['A2'],'Il Giappone'),
          ('B6',['A5'],'realizza una brillante'),('B8',['A7'],'e diventa'),('B4',['A3'],'In Cina'),
          ('B7',['A6'],'nasce la Repubblica'),('B9',['A8'],'che sperimenta')]),
}

# ---------- HTML / SVG ----------
CSS = """
@font-face{font-family:Fig;font-weight:500;src:url(file:///root/.fonts/Figtree-Medium.ttf)}
@font-face{font-family:Fig;font-weight:600;src:url(file:///root/.fonts/Figtree-SemiBold.ttf)}
@font-face{font-family:FigB;src:url(file:///root/.fonts/Figtree-Bold.ttf)}
@font-face{font-family:Bri;src:url(file:///root/.fonts/BricolageGrotesque-ExtraBold.ttf)}
html,body{margin:0;width:1920px;height:1080px;background:#fff;overflow:hidden}
#k{position:absolute;left:60px;top:34px;font:700 22px FigB;letter-spacing:.14em;color:#2060AF}
#line{position:absolute;left:60px;right:60px;top:78px;height:2px;background:#CBD5E1}
#leg{position:absolute;right:60px;top:24px;display:flex;gap:14px;font:600 18px Fig;color:#0B1530}
#leg span{display:flex;align-items:center;gap:6px}
#leg i{display:inline-block;width:22px;height:16px;border-radius:4px;border:3px solid}
#tit{position:absolute;left:60px;top:92px;font:800 44px Bri;color:#2060AF;white-space:nowrap;opacity:0}
.b{position:absolute;box-sizing:border-box;display:flex;align-items:center;justify-content:center;text-align:center;
   padding:6px 18px;border-radius:16px;font:600 36px/1.25 Fig;color:#0B1530;opacity:0;box-shadow:0 8px 20px rgba(11,21,48,.12)}
.b.root{font:800 46px/1.2 Bri;border-radius:20px;letter-spacing:.04em}
.n{position:absolute;box-sizing:border-box;padding:8px 14px;border:3px dashed #2060AF;border-radius:12px;background:#fff;font:600 34px/1.25 Fig;color:#0B1530;opacity:0}
.l{position:absolute;transform:translate(-50%,-50%);background:#fff;padding:0 12px;font:500 34px/1.2 Fig;color:#0B1530;white-space:nowrap;opacity:0}
.hl{box-shadow:0 0 0 9px #FFE600, 0 10px 24px rgba(11,21,48,.18)!important}
svg{position:absolute;left:0;top:0}
"""

def esc(s): return H.escape(s, quote=False)

def geom(m):
    """applica dy e restituisce box con left/top"""
    dy = m['dy']; B = {}
    for (i, c, cx, top, w, h, rg) in m['boxes']: B[i] = dict(id=i, col=c, left=cx - w // 2, top=top + dy, w=w, h=h, lines=rg, cx=cx)
    A = {}
    for (i, pts, lab, lp) in m['arrows']: A[i] = dict(id=i, pts=[(x, y + dy) for x, y in pts], lab=lab, lp=(lp[0], lp[1] + dy) if lp else None)
    N = {}
    for (i, bx, left, top, w, rg) in m['note']: N[i] = dict(id=i, box=bx, left=left, top=top + dy, w=w, lines=rg)
    return B, A, N

def arrow_path(pts):
    return 'M' + ' L'.join(f'{x},{y}' for x, y in pts)

def build_html(n, m, steps):
    B, A, N = geom(m)
    o = [f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>',
         '<div id="k">MAPPA</div>',
         '<div id="leg">' + ''.join(f'<span><i style="background:{COL[c][0]};border-color:{COL[c][1]}"></i>{t}</span>' for c, t in LEGENDA) + '</div><div id="line"></div>']
    if m['titolo']: o.append(f'<div id="tit">{esc(m["titolo"])}</div>')
    o.append('<svg width="1920" height="1080"><defs><marker id="ah" markerUnits="userSpaceOnUse" markerWidth="30" markerHeight="30" refX="25" refY="15" orient="auto"><path d="M1,3 L26,15 L1,27 z" fill="#0B1530"/></marker></defs>')
    for a in A.values(): o.append(f'<path id="{a["id"]}" d="{arrow_path(a["pts"])}" fill="none" stroke="#0B1530" stroke-width="6" stroke-linejoin="round" marker-end="url(#ah)" opacity="0"/>')
    o.append('</svg>')
    for a in A.values():
        if a['lab']: o.append(f'<div class="l" id="L{a["id"]}" style="left:{a["lp"][0]}px;top:{a["lp"][1]}px">{esc(a["lab"])}</div>')
    for b in B.values():
        bg, bd = COL[b['col']]; cl = 'b root' if b['col'] == 'pes' else 'b'
        o.append(f'<div class="{cl}" id="{b["id"]}" style="left:{b["left"]}px;top:{b["top"]}px;width:{b["w"]}px;height:{b["h"]}px;background:{bg};border:{5 if b["col"]=="pes" else 4}px solid {bd}">{"<br>".join(esc(x) for x in b["lines"])}</div>')
    for q in N.values():
        o.append(f'<div class="n" id="{q["id"]}" style="left:{q["left"]}px;top:{q["top"]}px;width:{q["w"]}px">{"<br>".join(esc(x) for x in q["lines"])}</div>')
    o.append(f'''<script>
window.STEPS={json.dumps(steps)};   // [box, [frecce], nota|null, inizio, fine]
function ease(x){{x=Math.max(0,Math.min(1,x));return 1-Math.pow(1-x,3)}}
function state(t){{ // opacita' e giallo, deterministico
  const s={{}};let hl=null;
  for(const [b,ar,nt,st,en] of STEPS){{
    ar.forEach(a=>{{const p=ease((t-(st-0.2))/0.4);s[a]=p;s['L'+a]=p;}});
    const p=ease((t-(st-0.05))/0.4);s[b]=p; if(nt)s[nt]=p; s['T']=Math.max(s['T']||0,b==STEPS[0][0]?p:0);
    if(t>=st && t<en) hl=b;
  }}
  return [s,hl];
}}
function render(t){{
  const [s,hl]=state(t);
  for(const k in s){{const e=document.getElementById(k);if(!e)continue;e.style.opacity=s[k];
    if(e.classList.contains('b')||e.classList.contains('n'))e.style.transform='translateY('+(16*(1-s[k]))+'px)';}}
  const T=document.getElementById('tit');if(T)T.style.opacity=s['T']||0;
  document.querySelectorAll('.b').forEach(e=>e.classList.toggle('hl',e.id===hl));
}}
function sig(t){{const [s,hl]=state(t);return JSON.stringify([Object.keys(s).map(k=>Math.round(s[k]*500)),hl])}}
</script></body></html>''')
    return '\n'.join(o)

def build_svg(n, m):
    B, A, N = geom(m)
    o = ['<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080" font-family="Figtree, sans-serif">',
         '<rect width="1920" height="1080" fill="#FFFFFF"/>',
         '<defs><marker id="ah" markerUnits="userSpaceOnUse" markerWidth="30" markerHeight="30" refX="25" refY="15" orient="auto"><path d="M1,3 L26,15 L1,27 z" fill="#0B1530"/></marker></defs>',
         '<text x="60" y="52" font-size="22" font-weight="700" letter-spacing="3" fill="#2060AF">MAPPA</text>',
         '<rect x="60" y="78" width="1800" height="2" fill="#CBD5E1"/>']
    x = 1860
    for c, t in reversed(LEGENDA):   # legenda in alto a destra
        w = len(t) * 10 + 8; x -= w; o.append(f'<text x="{x}" y="46" font-size="18" font-weight="600" fill="#0B1530">{t}</text>')
        x -= 30; o.append(f'<rect x="{x}" y="32" width="22" height="16" rx="4" fill="{COL[c][0]}" stroke="{COL[c][1]}" stroke-width="3"/>'); x -= 14
    if m['titolo']: o.append(f'<text x="60" y="138" font-size="44" font-weight="800" fill="#2060AF" font-family="Bricolage Grotesque, Figtree, sans-serif">{esc(m["titolo"])}</text>')
    for a in A.values(): o.append(f'<path d="{arrow_path(a["pts"])}" fill="none" stroke="#0B1530" stroke-width="6" stroke-linejoin="round" marker-end="url(#ah)"/>')
    for a in A.values():
        if a['lab']:
            w = len(a['lab']) * 17 + 24; lx, ly = a['lp']
            o.append(f'<rect x="{lx-w/2}" y="{ly-22}" width="{w}" height="44" fill="#FFFFFF"/><text x="{lx}" y="{ly+12}" text-anchor="middle" font-size="34" font-weight="500" fill="#0B1530">{esc(a["lab"])}</text>')
    for b in B.values():
        bg, bd = COL[b['col']]; sw = 5 if b['col'] == 'pes' else 4
        o.append(f'<rect x="{b["left"]}" y="{b["top"]}" width="{b["w"]}" height="{b["h"]}" rx="16" fill="{bg}" stroke="{bd}" stroke-width="{sw}"/>')
        k = len(b['lines']); fs = 46 if b['col'] == 'pes' else 36; lh = fs * 1.25
        y0 = b['top'] + b['h'] / 2 - (k - 1) * lh / 2 + fs * 0.35
        ff = ' font-family="Bricolage Grotesque, Figtree, sans-serif"' if b['col'] == 'pes' else ''
        fw = 800 if b['col'] == 'pes' else 600
        for i, ln in enumerate(b['lines']):
            o.append(f'<text x="{b["cx"]}" y="{y0+i*lh:.1f}" text-anchor="middle" font-size="{fs}" font-weight="{fw}"{ff} fill="#0B1530">{esc(ln)}</text>')
    for q in N.values():
        h = len(q['lines']) * 42.5 + 16
        o.append(f'<rect x="{q["left"]}" y="{q["top"]}" width="{q["w"]}" height="{h}" rx="12" fill="#FFFFFF" stroke="#2060AF" stroke-width="3" stroke-dasharray="9 6"/>')
        for i, ln in enumerate(q['lines']):
            o.append(f'<text x="{q["left"]+14}" y="{q["top"]+8+34+i*42.5-4:.1f}" font-size="34" font-weight="600" fill="#0B1530">{esc(ln)}</text>')
    o.append('</svg>')
    return '\n'.join(o)

# ---------- voce, trascrizione, allineamento ----------
def norm(s):
    s = unicodedata.normalize('NFD', s.lower().replace('’', ' ').replace("'", ' ')).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9 ]', ' ', s).split()

def dur(f):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f], capture_output=True, text=True).stdout)

def trascrivi(wav):
    out = f'{WK}/' + os.path.basename(wav)[:-4] + '_asr'
    cache = out + '.json'
    if not os.path.exists(cache) or os.path.getmtime(cache) < os.path.getmtime(wav):
        subprocess.run([sys.executable, REPO + '/kit/tools/trascrivi.py', wav, out], check=True)
    return json.load(open(cache))

def parole_asr(seg):
    cur = None; out = []
    for x in seg:
        for t, w in x['parole']:
            if w.startswith(' ') or cur is None:
                if cur: out.append(cur)
                cur = [float(t), w.strip()]
            else: cur[1] += w
    if cur: out.append(cur)
    res = []
    for t, w in out:
        for q in norm(w): res.append((t, q))
    return res

def tempi_parole(testo, wav):
    """ritorna (tokens_testo, tempi[i] in s dall'inizio della voce, info)"""
    T = norm(testo)
    if wav and os.path.exists(wav):
        P = parole_asr(trascrivi(wav)); st = lambda w: w[:4]
        sm = difflib.SequenceMatcher(None, [st(w) for w in T], [st(w) for t, w in P], autojunk=False)
        tm = [None] * len(T); ok = 0
        for a, b, k in sm.get_matching_blocks():
            for i in range(k): tm[a + i] = P[b + i][0]; ok += 1
        D = dur(wav); dur_stim = D
        info = dict(reale=True, durata=D, parole_testo=len(T), parole_riconosciute=len(P), allineate=ok,
                    numeri_asr=[w for t, w in P if any(c.isdigit() for c in w)], non_allineate=[T[i] for i in range(len(T)) if tm[i] is None], asr=' '.join(w for t, w in P))
    else:
        D = len(T) / 2.5; tot = sum(len(w) + 1 for w in T); c = 0; tm = []
        for w in T: tm.append(D * c / tot); c += len(w) + 1
        info = dict(reale=False, durata=D, parole_testo=len(T))
    # interpola i vuoti
    known = [i for i, t in enumerate(tm) if t is not None]
    if not known: tm = [D * i / len(T) for i in range(len(T))]
    else:
        for i in range(len(T)):
            if tm[i] is None:
                p = max([k for k in known if k < i], default=None); q = min([k for k in known if k > i], default=None)
                if p is None: tm[i] = max(0.0, tm[q] - 0.25 * (q - i))
                elif q is None: tm[i] = tm[p] + 0.25 * (i - p)
                else: tm[i] = tm[p] + (tm[q] - tm[p]) * (i - p) / (q - p)
    return T, tm, info

def trova(T, frase, da):
    F = norm(frase)
    for k in range(len(F)):          # se la frase non c'e' (solo nelle prove con testo riassunto) accorcia da sinistra
        G = F[k:]
        for i in range(da, len(T) - len(G) + 1):
            if T[i:i + len(G)] == G:
                if k: print('  ATTENZIONE: frase accorciata', frase)
                return i
    raise SystemExit(f'frase non trovata nel testo: {frase!r} (da {da})')

# ---------- audio ----------
def fai_audio(wav, D, tot, out):
    if wav and os.path.exists(wav):
        m = subprocess.run(['ffmpeg', '-hide_banner', '-i', wav, '-af', 'aresample=48000,loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json', '-f', 'null', '-'], capture_output=True, text=True).stderr
        j = json.loads(m[m.rindex('{'):])
        ln = f"loudnorm=I=-16:TP=-1.5:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}:measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true"
        af = f"aresample=48000,{ln},aresample=48000,pan=stereo|c0=c0|c1=c0,afade=t=in:d=0.03,afade=t=out:st={D-0.03:.3f}:d=0.03,adelay={int(V0*1000)}|{int(V0*1000)},apad=whole_dur={tot:.4f}"
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', wav, '-af', af, '-t', f'{tot:.4f}', '-ar', '48000', '-ac', '2', '-c:a', 'pcm_s16le', out], check=True)
    else:
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo', '-t', f'{tot:.4f}', '-c:a', 'pcm_s16le', out], check=True)

# ---------- una mappa ----------
def fai(n, prova=False):
    m = MAPPE[n]; testi = {x['nome']: x['testo'] for x in json.load(open(W + '/voci_nuove.json'))}
    nome = m['prova'] if prova else m['voce']
    wav = f'{VOX}/{nome}.wav'
    testo = testi[m['voce']] if not prova else (json.load(open(W + '/old/testi_voci.json')) and
            {x['nome']: x['testo'] for x in json.load(open(W + '/old/testi_voci.json'))}[nome])
    if not prova and not os.path.exists(wav): wav = None
    if prova and not os.path.exists(wav): raise SystemExit('manca ' + wav)
    T, tm, info = tempi_parole(testo, wav)
    D = info['durata']; tot_voce_fine = V0 + D
    tot = math.ceil((tot_voce_fine + TAIL + HOLD) * 30) / 30
    # inizio di ogni passo
    idx = 0; ini = []
    for (b, ar, frase) in m['steps']:
        if not ini: ini.append(V0); idx = 0      # il primo riquadro (radice) legge la domanda dall'inizio
        else: idx = trova(T, frase, idx); ini.append(V0 + tm[idx])
        idx += 1
    # monotoni, almeno 0,6 s tra passi
    for k in range(1, len(ini)): ini[k] = max(ini[k], ini[k - 1] + 0.6)
    fine = ini[1:] + [tot_voce_fine + TAIL]
    notemap = {q[1]: q[0] for q in m['note']}
    steps = [[b, ar, notemap.get(b), round(ini[k], 3), round(fine[k], 3)] for k, (b, ar, fr) in enumerate(m['steps'])]
    # il box delle note e le frecce devono esistere tutte
    d = f'{WK}/prova' if prova else WK; os.makedirs(d, exist_ok=True)
    tag = f'MAP{n}'
    open(f'{d}/{tag}.html', 'w').write(build_html(n, m, steps))
    fin = f'{PZ}/{tag}_finale.png' if not prova else f'{d}/{tag}_finale.png'
    job = dict(html=f'{d}/{tag}.html', tot=tot, outdir=f'{d}/{tag}_frames', final=fin)
    subprocess.run(['rm', '-rf', job['outdir']]); json.dump(job, open(f'{d}/{tag}_job.json', 'w'))
    subprocess.run(['node', HERE + '/mappe_shot.js', f'{d}/{tag}_job.json'], check=True, env={**os.environ, 'NODE_PATH': '/opt/node-tools/node_modules'}, cwd=HERE)
    runs = json.load(open(job['outdir'] + '/frames.json'))
    with open(f'{d}/{tag}_concat.txt', 'w') as f:
        for p, c in runs: f.write(f"file '{p}'\nduration {c/30:.6f}\n")
        f.write(f"file '{runs[-1][0]}'\n")
    fai_audio(wav, D, tot, f'{d}/{tag}.wav')
    mkv = f'{d}/{tag}.mkv' if prova else f'{PZ}/{tag}.mkv'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', f'{d}/{tag}_concat.txt', '-i', f'{d}/{tag}.wav',
                    '-vf', 'fps=30,format=yuv420p', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '16', '-c:a', 'pcm_s16le', '-ar', '48000', '-ac', '2',
                    '-frames:v', str(round(tot * 30)), '-t', f'{tot:.4f}', mkv], check=True)
    if not prova:
        open(f'{PZ}/{tag}.svg', 'w').write(build_svg(n, m))
        info_s = dict(info); info_s.pop('asr', None)
        json.dump(dict(durata_s=round(round(tot * 30) / 30, 4), voci=[m['voce']],
                       note='voce %s (%s); mappa ramo per ramo; giallo finche la voce legge il riquadro; mappa intera ferma %.1f s' % (
                           m['voce'], 'VERA' if info['reale'] else 'PROVVISORIA (silenzio stimato): rilanciare mappe.py con la voce vera', HOLD),
                       passi=steps, allineamento=info_s), open(f'{PZ}/{tag}.json', 'w'), ensure_ascii=False, indent=1)
    else:
        open(f'{d}/{tag}.svg', 'w').write(build_svg(n, m))
    print(tag, 'durata', round(tot, 3), 'voce', 'reale' if info['reale'] else 'provvisoria', 'passi', [(s[0], s[3]) for s in steps])
    if info.get('non_allineate'): print('  parole del testo non ritrovate nella trascrizione:', info['non_allineate'])

if __name__ == '__main__':
    a = sys.argv[1:]; prova = '--prova' in a; a = [x for x in a if x != '--prova']
    os.makedirs(PZ, exist_ok=True); os.makedirs(WK, exist_ok=True)
    for n in ([int(x) for x in a] or [1, 2, 3]): fai(n, prova)
