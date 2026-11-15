#!/usr/bin/env python3
"""Render degli approfondimenti animati (AN) di una lezione.
uso: render.py spec_dir_con_spec.py vox_dir out_dir [AN01 AN02 ...]
Se vox_dir/ANxx.wav esiste usa la voce Kore vera, altrimenti segnaposto muto di durata stimata (2,45 parole/s)."""
import sys, os, re, json, html, subprocess, shutil, tempfile, importlib.util
REPO = '/home/user/Lezioni'
sys.path.insert(0, REPO + '/kit/tools')
FONT = REPO + '/kit/tools/mappa_font'
C = dict(notte='#0B1530', blu='#2060AF', giallo='#FFE600', grigio='#EEF0F4', linea='#C9D0DC')
LEAD, TAIL, F, WPS = 0.5, 0.9, 0.5, 2.45

def css():
    o = []
    for fam, f, w in [('Bricolage Grotesque', 'BricolageGrotesque-ExtraBold.ttf', 800), ('Figtree', 'Figtree-Regular.ttf', 400),
                      ('Figtree', 'Figtree-SemiBold.ttf', 600), ('Figtree', 'Figtree-Bold.ttf', 700)]:
        import base64; o.append(f"@font-face{{font-family:'{fam}';src:url(data:font/ttf;base64,{base64.b64encode(open(FONT+'/'+f,'rb').read()).decode()});font-weight:{w}}}")
    return '\n'.join(o)

BASE = css() + f'''
*{{box-sizing:border-box}}html,body{{margin:0;width:1920px;height:1080px;overflow:hidden;background:{C["notte"]};
font-family:Figtree,Arial,sans-serif;color:#fff}}
.lab{{position:absolute;left:100px;top:70px;font-family:'Courier New',monospace;font-weight:700;font-size:30px;letter-spacing:.18em;color:{C["giallo"]}}}
.ttl{{position:absolute;left:100px;top:120px;right:100px;font-family:'Bricolage Grotesque';font-weight:800;font-size:70px;line-height:1.05}}
.ttlbig{{position:absolute;left:160px;right:160px;top:400px;font-family:'Bricolage Grotesque';font-weight:800;font-size:104px;line-height:1.05;text-align:center}}
.sub{{position:absolute;left:0;right:0;top:300px;text-align:center;font-family:'Courier New',monospace;font-weight:700;font-size:34px;letter-spacing:.2em;color:{C["giallo"]}}}
.bar{{position:absolute;left:100px;top:236px;width:160px;height:8px;background:{C["giallo"]}}}
.row{{position:absolute;left:100px;right:100px;top:330px;display:flex;gap:40px;align-items:stretch}}
.card{{flex:1;background:{C["grigio"]};color:{C["notte"]};border-radius:22px;padding:34px 36px 38px;border:6px solid {C["blu"]};
min-height:540px;display:flex;flex-direction:column}}
.card.new{{border-color:{C["giallo"]};box-shadow:0 0 0 6px rgba(255,230,0,.25)}}
.card .tag{{font-weight:700;font-size:30px;letter-spacing:.06em;text-transform:uppercase;color:{C["blu"]};margin-bottom:18px}}
.card .h{{font-family:'Bricolage Grotesque';font-weight:800;font-size:60px;line-height:1.05;margin-bottom:22px}}
.card .t{{font-size:40px;line-height:1.25;color:#1c2748}}
.tl{{position:absolute;left:100px;right:100px;top:300px;height:10px;background:{C["blu"]};border-radius:5px}}
.tl.card-year .tag{{font-family:'Bricolage Grotesque';font-size:72px;color:{C["blu"]};text-transform:none}}
.stack{{position:absolute;left:100px;right:100px;top:310px;display:flex;flex-direction:column;gap:30px}}
.r{{display:flex;align-items:center;gap:36px;background:{C["grigio"]};color:{C["notte"]};border-radius:20px;padding:26px 36px;
border:6px solid {C["blu"]};min-height:190px}}
.r.new{{border-color:{C["giallo"]};box-shadow:0 0 0 6px rgba(255,230,0,.25)}}
.r .tag{{flex:0 0 330px;font-weight:700;font-size:34px;letter-spacing:.04em;text-transform:uppercase;color:{C["blu"]}}}
.r .a,.r .b{{flex:1;font-size:40px;line-height:1.2;font-weight:600}}
.r .b{{border-left:4px solid {C["linea"]};padding-left:34px}}
.r .a em{{font-style:normal;background:{C["giallo"]};padding:2px 10px;border-radius:8px}}
.foot{{position:absolute;left:100px;bottom:50px;font-size:30px;color:{C["linea"]};letter-spacing:.06em}}
'''

def pg(inner):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{BASE}</style></head><body>{inner}</body></html>'

E = html.escape

def head(a):
    return f'<div class="lab">{E(a.get("label","APPROFONDIMENTO"))}</div><div class="ttl">{E(a["titolo"])}</div><div class="bar"></div>'

def cards_html(items, n_vis, timeline):
    o = []
    for i, c in enumerate(items):
        if i >= n_vis: break
        new = ' new' if i == n_vis - 1 else ''
        o.append(f'<div class="card{new}{" card-year" if timeline else ""}"><div class="tag">{E(c["tag"])}</div>'
                 f'<div class="h">{E(c["h"])}</div><div class="t">{E(c["t"])}</div></div>')
    # segnaposto invisibili per tenere le colonne stabili
    for i in range(n_vis, len(items)):
        o.append('<div class="card" style="visibility:hidden"></div>')
    tl = '<div class="tl"></div>' if timeline else ''
    return head({}) if False else tl + f'<div class="row" style="top:{360 if not timeline else 330}px">{"".join(o)}</div>'

def righe_html(items, n_vis):
    o = []
    for i, c in enumerate(items[:n_vis]):
        new = ' new' if i == n_vis - 1 else ''
        a = E(c['a'])
        if c.get('ev'): a = f'<em>{a}</em>'
        b = f'<div class="b">{E(c["b"])}</div>' if c.get('b') else ''
        o.append(f'<div class="r{new}"><div class="tag">{E(c["tag"])}</div><div class="a">{a}</div>{b}</div>')
    return f'<div class="stack">{"".join(o)}</div>'

def stati(a):
    """Elenco degli stati (HTML) : 0 = titolo, poi uno per elemento."""
    st = [pg(f'<div class="lab" style="left:0;right:0;top:270px;text-align:center">{E(a.get("label","APPROFONDIMENTO"))}</div>'
             f'<div class="ttlbig">{E(a["titolo"])}</div>')]
    for si, scr in enumerate(a['screens']):
        righe = scr[0].get('kind') == 'righe'
        for k in range(1, len(scr) + 1):
            body = righe_html(scr, k) if righe else cards_html(scr, k, a['kind'] == 'timeline')
            st.append(pg(head(a) + body))
    return st

def dur(p):
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p], capture_output=True, text=True)
    return float(r.stdout.strip())

def prepara_voce(a, vox, work):
    """Restituisce (wav_padded, dur_voce, vera?, tempi_marcatori(s) già con LEAD)"""
    testo = a['testo']
    marks = [m.start() for m in re.finditer(r'\[\[\d+\]\]', testo)]
    pulito, pos, off = '', [], 0
    for m in re.finditer(r'\[\[\d+\]\]', testo):
        pulito += testo[off:m.start()]; pos.append(len(pulito)); off = m.end()
    pulito += testo[off:]
    pulito = re.sub(r'\s+', ' ', pulito)
    nw = len(pulito.split())
    src = os.path.join(vox, a['id'] + '.wav')
    vera = os.path.exists(src)
    wav = os.path.join(work, a['id'] + '_pad.wav')
    if vera:
        d = dur(src)
        subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', src, '-af',
                        f'loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000,adelay={int(LEAD*1000)}:all=1,apad=pad_dur={TAIL}',
                        '-ac', '1', '-ar', '48000', wav], check=True)
    else:
        d = nw / WPS
        subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'lavfi', '-i', f'anullsrc=r=48000:cl=mono', '-t', f'{LEAD+d+TAIL:.3f}', wav], check=True)
    # posizione dei marcatori: proporzionale ai caratteri (poi, con voce vera, agganciata alla pausa più vicina)
    L = len(pulito)
    # un marcatore sta a inizio frase: usa il rapporto di parole
    t = []
    for p in pos:
        frac = len(pulito[:p].split()) / max(1, nw)
        tt = LEAD + frac * d
        if vera:
            try:
                import taglio
                tt = taglio.snap(tt, wav, before=1.2, after=1.2)
            except Exception as e:
                pass
        t.append(round(tt, 2))
    return wav, d, vera, t, pulito

def render(a, vox, out, work):
    wav, d, vera, t, pulito = prepara_voce(a, vox, work)
    tot = dur(wav)
    o = os.path.join(out, a['id'] + '.mp4')
    if a['kind'] == 'mappa':
        jm = os.path.join(work, a['id'] + '_mappa.json')
        json.dump(dict(materia='Letteratura italiana', docente='Prof. Giorgio Mazzotti', titolo=a['titolo'], rami=a['rami']), open(jm, 'w'), ensure_ascii=False)
        md = os.path.join(work, a['id'] + '_m'); os.makedirs(md, exist_ok=True)
        subprocess.run([sys.executable, '/tmp/claude-0/-home-user-Lezioni/aa838b16-be86-588f-84fd-78776ad6250d/scratchpad/lez4/tools/mappa.py', jm, '--out', md, '--voce', wav, '--tempi', ','.join(str(x) for x in t)], check=True)
        shutil.copy(md + '/mappa.mp4', o)
        shutil.copy(md + '/mappa_dispensa.pdf', os.path.join(out, a['id'] + '_dispensa.pdf'))
        if a.get('finale'): shutil.copy(md + '/mappa_dispensa.pdf', os.path.join(out, 'mappa_finale_dispensa.pdf'))
    else:
        from playwright.sync_api import sync_playwright
        S = stati(a)
        assert len(S) == len(t) + 1, (a['id'], len(S), len(t))
        with sync_playwright() as pw:
            b = pw.chromium.launch(); p = b.new_page(viewport={'width': 1920, 'height': 1080})
            for k, h in enumerate(S):
                p.set_content(h); p.wait_for_timeout(120); p.screenshot(path=f'{work}/{a["id"]}_s{k}.png')
            b.close()
        cue = [0.0] + t + [tot]
        seg = [cue[i + 1] - cue[i] for i in range(len(S))]
        inp, filt, last, off = [], [], '[0:v]', 0.0
        for k in range(len(S)):
            inp += ['-loop', '1', '-t', f'{seg[k] + (F if k < len(S) - 1 else 0):.3f}', '-i', f'{work}/{a["id"]}_s{k}.png']
        for k in range(1, len(S)):
            off += seg[k - 1]
            filt.append(f'{last}[{k}:v]xfade=transition=fade:duration={F}:offset={off - F/2:.3f}[v{k}]'); last = f'[v{k}]'
        filt.append(f'{last}format=yuv420p,fps=30[vo]')
        n = len(S)
        subprocess.run(['ffmpeg', '-y', '-v', 'error'] + inp + ['-i', wav, '-filter_complex', ';'.join(filt), '-map', '[vo]', '-map', f'{n}:a',
                       '-t', f'{tot:.3f}', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19', '-r', '30', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', o], check=True)
    # sottotitoli: frasi proporzionali alla durata
    fr = [x.strip() for x in re.split(r'(?<=[.!?:])\s+', pulito) if x.strip()]
    lens = [len(x) for x in fr]; tl = sum(lens); tt = LEAD; cues = []
    for x, l in zip(fr, lens):
        dd = d * l / tl; cues.append([round(tt, 2), round(tt + dd, 2), x]); tt += dd
    json.dump(dict(id=a['id'], dopo=a['dopo'], titolo=a['titolo'], durata=dur(o), voce_vera=vera, voce_s=d, cue=cues, tempi=t),
              open(os.path.join(out, a['id'] + '.json'), 'w'), ensure_ascii=False, indent=1)
    return dur(o), vera

if __name__ == '__main__':
    spec, vox, out = sys.argv[1:4]
    sel = sys.argv[4:]
    sp = importlib.util.spec_from_file_location('spec', spec); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    os.makedirs(out, exist_ok=True); work = tempfile.mkdtemp(prefix='an_')
    for a in m.AN:
        if sel and a['id'] not in sel: continue
        d, v = render(a, vox, out, work)
        print(a['id'], a['titolo'], f'{d:.1f}s', 'VOCE' if v else 'segnaposto', flush=True)
    shutil.rmtree(work)
