#!/usr/bin/env python3
"""Mappa concettuale Telesio: video animato (1920x1080) e pagina per la dispensa (A4 orizzontale).

Uso:
  python3 kit/tools/mappa.py mappa.json --out cartella [--durata 60] [--voce voce.wav] [--tempi 3,12,25,...]
                                         [--stretta] [--solo-pdf] [--solo-video]

mappa.json:
{
  "materia": "Letteratura italiana",
  "docente": "Prof. Giorgio Mazzotti",
  "titolo": "Giovanni Pascoli",            <- al centro (max ~4 parole)
  "rami": [                                <- da 2 a 6 rami, nell'ordine in cui la voce li dice
    {"concetto": "Il nido", "parola": "famiglia", "esempio": "X Agosto", "sotto": ["lutto del padre"]},
    ...
  ]
}
Regole: al massimo 6 rami; concetto <= 4 parole; parola chiave 1-2 parole; esempio <= 6 parole; "sotto" facoltativo, max 2 voci brevi.

Uscite in --out:
  mappa.mp4      animazione: compare il centro, poi un ramo alla volta (dissolvenza 0,6 s), poi resta tutta la mappa.
                 Con --voce l'audio viene montato e la durata segue la voce. Con --tempi (secondi) ogni ramo compare
                 nell'istante in cui la voce lo nomina (un numero per ramo).
  mappa.png      la mappa completa 1920x1080 (per controllo e miniature).
  mappa_dispensa.pdf  pagina A4 orizzontale, testo vero, leggibile in bianco e nero.
--stretta: lascia libera la colonna destra (x >= 1490) per il riquadro del docente.
"""
import json, os, sys, math, argparse, subprocess, tempfile, shutil, html

QUI = os.path.dirname(os.path.abspath(__file__))
FONT = os.path.join(QUI, 'mappa_font')
C = dict(notte='#0B1530', blu='#2060AF', giallo='#FFE600', grigio='#EEF0F4', linea='#C9D0DC')


def font_css():
    out = []
    for fam, f, w in [('Bricolage Grotesque', 'BricolageGrotesque-ExtraBold.ttf', 800),
                      ('Figtree', 'Figtree-Regular.ttf', 400), ('Figtree', 'Figtree-SemiBold.ttf', 600),
                      ('Figtree', 'Figtree-Bold.ttf', 700)]:
        p = os.path.join(FONT, f)
        if os.path.exists(p):
            import base64; out.append(f"@font-face{{font-family:'{fam}';src:url(data:font/ttf;base64,{base64.b64encode(open(p,'rb').read()).decode()});font-weight:{w}}}")
    return '\n'.join(out)


def posizioni(n, W, H, cx, cy):
    """Centri dei rami su un'ellisse intorno al centro, a partire dall'alto, in senso orario."""
    rx, ry = W * 0.36, H * 0.33
    start = -90 if n % 2 else -90 - 180 / n
    return [(cx + rx * math.cos(math.radians(start + 360 * i / n)),
             cy + ry * math.sin(math.radians(start + 360 * i / n))) for i in range(n)]


def pagina(d, visibili, W, H, stampa=False, stretta=False):
    """HTML della mappa con i primi `visibili` rami (0 = solo centro)."""
    e = html.escape
    area_w = 1410 if stretta else W
    top = 150 if not stampa else 120
    cx, cy = area_w / 2 + (40 if stretta else 0), top + (H - top) / 2
    n = len(d['rami'])
    pos = posizioni(n, area_w - 80, H - top, cx, cy)
    cw, ch = (330, 190) if not stampa else (300, 170)
    bg = '#ffffff' if stampa else C['grigio']
    lines, cards = [], []
    for i, (r, (x, y)) in enumerate(zip(d['rami'], pos)):
        op = 1 if i < visibili else 0
        lines.append(f'<line x1="{cx}" y1="{cy}" x2="{x}" y2="{y}" stroke="{C["notte"] if stampa else C["blu"]}" '
                     f'stroke-width="{3 if stampa else 5}" opacity="{op}"/>')
        sotto = ''.join(f'<div class="s">• {e(s)}</div>' for s in r.get('sotto', [])[:2])
        es = f'<div class="es"><span>es.</span> {e(r["esempio"])}</div>' if r.get('esempio') else ''
        pk = f'<div class="pk">{e(r["parola"])}</div>' if r.get('parola') else ''
        cards.append(f'<div class="card" style="left:{x - cw / 2}px;top:{y - ch / 2}px;width:{cw}px;min-height:{ch}px;opacity:{op}">'
                     f'<div class="n">{i + 1}</div><div class="c">{e(r["concetto"])}</div>{pk}{es}{sotto}</div>')
    head = '' if stampa else (f'<div class="hd"><div class="lab">MAPPA CONCETTUALE</div>'
                              f'<div class="mat">{e(d.get("materia", "").upper())}</div></div>')
    foot = (f'<div class="ft">{e(d.get("materia", "").upper())} · {e(d.get("docente", ""))} · Mappa della lezione</div>'
            if stampa else '')
    tit = (f'<div class="tt">Mappa della lezione: {e(d["titolo"])}</div>' if stampa else '')
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
{font_css()}
*{{box-sizing:border-box}}html,body{{margin:0;width:{W}px;height:{H}px;background:{bg};overflow:hidden;
font-family:Figtree,Arial,sans-serif;color:{C["notte"]}}}
svg{{position:absolute;left:0;top:0}}
.hd{{position:absolute;left:80px;top:46px;right:{510 if stretta else 80}px;display:flex;justify-content:space-between;align-items:baseline;
border-bottom:3px solid {C["linea"]};padding-bottom:14px}}
.lab{{font-family:'Bricolage Grotesque',Arial;font-weight:800;font-size:40px;letter-spacing:.04em;color:{C["notte"]}}}
.mat{{font-size:26px;font-weight:600;letter-spacing:.12em;color:{C["blu"]}}}
.tt{{position:absolute;left:40px;top:28px;font-family:'Bricolage Grotesque',Arial;font-weight:800;font-size:34px}}
.ft{{position:absolute;left:40px;right:40px;bottom:18px;border-top:1px solid #999;padding-top:6px;font-size:14px;color:#333}}
.ctr{{position:absolute;left:{cx - 190}px;top:{cy - 70}px;width:380px;min-height:140px;display:flex;align-items:center;
justify-content:center;text-align:center;padding:18px 24px;border-radius:18px;
background:{'#fff' if stampa else C["notte"]};color:{C["notte"] if stampa else '#fff'};
border:{('4px solid ' + C["notte"]) if stampa else 'none'};
font-family:'Bricolage Grotesque',Arial;font-weight:800;font-size:{40 if stampa else 46}px;line-height:1.08}}
.card{{position:absolute;background:#fff;border:{'2px solid #222' if stampa else '3px solid ' + C["blu"]};border-radius:14px;
padding:16px 18px 14px 18px;box-shadow:{'none' if stampa else '0 6px 0 rgba(11,21,48,.08)'}}}
.n{{position:absolute;left:-16px;top:-16px;width:40px;height:40px;border-radius:50%;background:{C["notte"]};color:#fff;
font-weight:700;font-size:22px;display:flex;align-items:center;justify-content:center}}
.c{{font-family:'Bricolage Grotesque',Arial;font-weight:800;font-size:{30 if stampa else 34}px;line-height:1.08;margin-bottom:8px}}
.pk{{display:inline-block;font-weight:700;font-size:{22 if stampa else 26}px;padding:2px 10px;border-radius:6px;
background:{'#fff' if stampa else C["giallo"]};border:{'2px dashed #222' if stampa else 'none'};margin-bottom:6px}}
.es{{font-size:{21 if stampa else 25}px;line-height:1.2}}.es span{{font-weight:700;color:{'#222' if stampa else C["blu"]}}}
.s{{font-size:{19 if stampa else 22}px;line-height:1.2;color:#333;margin-top:3px}}
</style></head><body>{head}{tit}
<svg width="{W}" height="{H}">{''.join(lines)}</svg>
<div class="ctr">{e(d["titolo"])}</div>{''.join(cards)}{foot}</body></html>'''


def durata_audio(p):
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p],
                       capture_output=True, text=True)
    return float(r.stdout.strip())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('json'); ap.add_argument('--out', required=True)
    ap.add_argument('--durata', type=float, default=0); ap.add_argument('--voce')
    ap.add_argument('--tempi'); ap.add_argument('--stretta', action='store_true')
    ap.add_argument('--solo-pdf', action='store_true'); ap.add_argument('--solo-video', action='store_true')
    a = ap.parse_args()
    d = json.load(open(a.json))
    n = len(d['rami'])
    if not 2 <= n <= 6: sys.exit('servono da 2 a 6 rami')
    os.makedirs(a.out, exist_ok=True)
    from playwright.sync_api import sync_playwright
    tmp = tempfile.mkdtemp()
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        if not a.solo_pdf:
            pg = b.new_page(viewport={'width': 1920, 'height': 1080})
            for k in range(n + 1):
                pg.set_content(pagina(d, k, 1920, 1080, stretta=a.stretta)); pg.wait_for_timeout(150)
                pg.screenshot(path=f'{tmp}/s{k}.png')
            shutil.copy(f'{tmp}/s{n}.png', os.path.join(a.out, 'mappa.png'))
        if not a.solo_video:
            pg = b.new_page(viewport={'width': 1123, 'height': 794})
            pg.set_content(pagina(d, n, 1123, 794, stampa=True)); pg.wait_for_timeout(200)
            pg.pdf(path=os.path.join(a.out, 'mappa_dispensa.pdf'), width='297mm', height='210mm',
                   print_background=True, margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'})
        b.close()
    if a.solo_pdf:
        print('OK', a.out); return
    tot = durata_audio(a.voce) if a.voce else (a.durata or 8 + 6 * n)
    if a.tempi:
        t = [float(x) for x in a.tempi.split(',')]
        if len(t) != n: sys.exit('--tempi: serve un numero per ramo')
    else:
        t0 = min(3.0, tot * 0.08); passo = (tot * 0.85 - t0) / n
        t = [t0 + passo * i for i in range(n)]
    t = [max(0.8, min(x, tot - 1.5)) for x in t]
    # segmenti: s0 fino a t[0], poi s1 ... sn; dissolvenza 0,6 s
    seg = [t[0]] + [t[i + 1] - t[i] for i in range(n - 1)] + [tot - t[-1]]
    F = 0.6
    inp, filt, last = [], [], '[0:v]'
    for k in range(n + 1):
        inp += ['-loop', '1', '-t', f'{seg[k] + (F if k < n else 0):.3f}', '-i', f'{tmp}/s{k}.png']
    off = 0.0
    for k in range(1, n + 1):
        off += seg[k - 1]
        filt.append(f'{last}[{k}:v]xfade=transition=fade:duration={F}:offset={off:.3f}[v{k}]'); last = f'[v{k}]'
    filt.append(f'{last}format=yuv420p,fps=30[vo]')
    cmd = ['ffmpeg', '-y', '-v', 'error'] + inp
    if a.voce: cmd += ['-i', a.voce]
    cmd += ['-filter_complex', ';'.join(filt), '-map', '[vo]']
    if a.voce: cmd += ['-map', f'{n + 1}:a', '-c:a', 'aac', '-b:a', '192k']
    cmd += ['-t', f'{tot:.3f}', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19', '-r', '30',
            os.path.join(a.out, 'mappa.mp4')]
    subprocess.run(cmd, check=True)
    shutil.rmtree(tmp)
    print(f'OK {a.out} · durata {tot:.1f} s · rami a {", ".join(f"{x:.1f}" for x in t)} s')


if __name__ == '__main__':
    main()
