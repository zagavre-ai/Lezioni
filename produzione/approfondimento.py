#!/usr/bin/env python3
"""Approfondimento animato Telesio (segmento AN): JSON -> mp4 1920x1080 con voce.
Uso: python3 approfondimento.py an.json --out cartella [--voce voce.wav]
Se manca --voce la durata e' STIMATA (parole / 2,5 al secondo) e l'audio e' silenzio (segnaposto).
Le comparse dei riquadri sono distribuite in proporzione alle parole del testo di ogni schermata.
an.json: {id, tipo: linea|scheda|testo|confronto|parole, materia, titolo,
  schermate:[{voce:"testo detto", titolo?:"", cards:[{k:"1855", t:"titolo", d:"dettaglio breve"}],
              versi?:[righe], nota?:"..."}]}   (max 3 card per schermata)"""
import json, os, sys, html, subprocess, tempfile, shutil, argparse
sys.path.insert(0, os.path.join(os.environ.get('KIT', '/home/user/Lezioni/kit/tools')))
import mappa as M
C = M.C
VPS = 2.24  # parole al secondo, misurato sulle voci Kore gia consegnate

def parole(t): return max(1, len(t.split()))

def html_stato(an, sc, k, W=1920, H=1080):
    e = html.escape; tipo = an['tipo']; cards = sc.get('cards', []); versi = sc.get('versi')
    def op(i): return 1 if i < k else 0
    body = ''
    if tipo == 'testo' and versi:
        ev = sc.get('evid', list(range(len(versi))))  # indice verso evidenziato al passo k
        cur = ev[k - 1] if 0 < k <= len(ev) else -1
        righe = ''.join(f'<div class="v{" on" if i == cur else ""}">{e(v)}</div>' for i, v in enumerate(versi))
        nota = ''
        if 0 < k <= len(ev) and sc.get('note'):
            nota = f'<div class="nota">{e(sc["note"][k - 1])}</div>'
        body = f'<div class="versi">{righe}</div>{nota}'
    elif tipo == 'linea':
        n = len(cards); step = 1560 / max(n, 1)
        pts = ''.join(f'<div class="pt" style="left:{180 + step * (i + .5) - 14}px;opacity:{op(i)}"></div>'
                      f'<div class="lc" style="left:{180 + step * i + 15}px;width:{step - 30}px;opacity:{op(i)}">'
                      f'<div class="yr">{e(c.get("k", ""))}</div><div class="ct">{e(c["t"])}</div><div class="cd">{e(c.get("d", ""))}</div></div>'
                      for i, c in enumerate(cards))
        body = f'<div class="axis"></div>{pts}'
    else:
        n = len(cards); gap = 36; w = (1760 - gap * (n - 1)) / max(n, 1)
        cs = ''.join(f'<div class="cc" style="left:{80 + (w + gap) * i}px;width:{w}px;opacity:{op(i)}">'
                     + (f'<div class="kk">{e(c["k"])}</div>' if c.get('k') else '')
                     + f'<div class="ct">{e(c["t"])}</div><div class="cd">{e(c.get("d", ""))}</div></div>'
                     for i, c in enumerate(cards))
        body = cs
    tit = e(sc.get('titolo', ''))
    lab = {'linea': 'LINEA DEL TEMPO', 'scheda': 'SCHEDA', 'testo': 'ANALISI DEL TESTO', 'confronto': 'CONFRONTO',
           'parole': 'PAROLE CHIAVE'}[tipo]
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{M.font_css()}
*{{box-sizing:border-box}}html,body{{margin:0;width:{W}px;height:{H}px;background:{C["notte"]};overflow:hidden;
font-family:Figtree,Arial,sans-serif;color:#fff}}
.lab{{position:absolute;left:80px;top:50px;font-family:'DM Mono',monospace;font-size:30px;letter-spacing:.14em;color:{C["giallo"]}}}
.mat{{position:absolute;right:80px;top:50px;font-size:30px;letter-spacing:.12em;color:{C["linea"]}}}
.ti{{position:absolute;left:80px;top:100px;right:80px;font-family:'Bricolage Grotesque',Arial;font-weight:800;font-size:64px;line-height:1.05}}
.st{{position:absolute;left:80px;top:190px;right:80px;font-size:34px;color:{C["linea"]}}}
.cc{{position:absolute;top:330px;min-height:430px;background:{C["grigio"]};color:{C["notte"]};border-radius:22px;padding:34px;transition:none}}
.kk{{display:inline-block;background:{C["giallo"]};font-weight:700;font-size:34px;padding:4px 16px;border-radius:8px;margin-bottom:16px}}
.ct{{font-family:'Bricolage Grotesque',Arial;font-weight:800;font-size:44px;line-height:1.08;margin-bottom:14px}}
.cd{{font-size:34px;line-height:1.25}}
.axis{{position:absolute;left:180px;width:1560px;top:560px;height:8px;background:{C["blu"]}}}
.pt{{position:absolute;top:546px;width:36px;height:36px;border-radius:50%;background:{C["giallo"]};border:6px solid {C["notte"]}}}
.lc{{position:absolute;top:620px;background:{C["grigio"]};color:{C["notte"]};border-radius:18px;padding:22px}}
.lc .yr{{font-family:'Bricolage Grotesque',Arial;font-weight:800;font-size:52px;color:{C["blu"]}}}
.lc .ct{{font-size:36px}}.lc .cd{{font-size:30px}}
.versi{{position:absolute;left:80px;top:300px;width:1000px;font-family:Georgia,serif;font-size:44px;line-height:1.35}}
.v{{opacity:.45;padding:2px 14px;border-radius:8px}}.v.on{{opacity:1;background:{C["blu"]}}}
.nota{{position:absolute;left:1150px;top:300px;width:690px;background:{C["grigio"]};color:{C["notte"]};border-radius:22px;padding:34px;font-size:38px;line-height:1.25}}
</style></head><body><div class="lab">{lab}</div><div class="mat">{e(an.get("materia", "").upper())}</div>
<div class="ti">{e(an["titolo"])}</div><div class="st">{tit}</div>{body}</body></html>'''

def dur(p):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p],
                                capture_output=True, text=True).stdout)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('json'); ap.add_argument('--out', required=True); ap.add_argument('--voce')
    a = ap.parse_args(); an = json.load(open(a.json)); os.makedirs(a.out, exist_ok=True)
    tot_par = sum(parole(s['voce']) for s in an['schermate'])
    tot = dur(a.voce) if a.voce else tot_par / VPS + 1.5
    tmp = tempfile.mkdtemp(); stati = []  # (png, t_inizio)
    from playwright.sync_api import sync_playwright
    t = 0.0
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path='/opt/pw-browsers/chromium'); pg = b.new_page(viewport={'width': 1920, 'height': 1080})
        for si, sc in enumerate(an['schermate']):
            d = tot * parole(sc['voce']) / tot_par
            n = len(sc.get('evid', sc.get('cards', []))) if an['tipo'] != 'testo' else len(sc.get('evid', sc.get('versi', [])))
            for k in range(n + 1):
                png = f'{tmp}/{si}_{k}.png'
                pg.set_content(html_stato(an, sc, k)); pg.wait_for_timeout(120); pg.screenshot(path=png)
                stati.append((png, t + d * (0.04 if k == 0 else 0.04 + 0.92 * k / (n + 1) - 0.0)))
            # k=0 parte a t; le card compaiono equidistanti
            stati[-(n + 1)] = (stati[-(n + 1)][0], t)
            t += d
        b.close()
    starts = [s[1] for s in stati]
    seg = [starts[i + 1] - starts[i] for i in range(len(stati) - 1)] + [tot - starts[-1]]
    F = 0.4; inp = []; filt = []; last = '[0:v]'; off = 0.0
    for i, (png, _) in enumerate(stati):
        inp += ['-loop', '1', '-t', f'{max(seg[i], .5) + F:.3f}', '-i', png]
    for i in range(1, len(stati)):
        off += seg[i - 1]
        filt.append(f'{last}[{i}:v]xfade=transition=fade:duration={F}:offset={off - F / 2 if off > F else off:.3f}[v{i}]'); last = f'[v{i}]'
    filt.append(f'{last}format=yuv420p,fps=30[vo]')
    cmd = ['ffmpeg', '-y', '-v', 'error'] + inp
    if a.voce: cmd += ['-i', a.voce]
    else: cmd += ['-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo']
    cmd += ['-filter_complex', ';'.join(filt), '-map', '[vo]', '-map', f'{len(stati)}:a', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000',
            '-t', f'{tot:.3f}', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19', '-r', '30', os.path.join(a.out, an['id'] + '.mp4')]
    subprocess.run(cmd, check=True); shutil.rmtree(tmp)
    json.dump({'id': an['id'], 'durata_s': round(tot, 2), 'stima': not a.voce, 'parole': tot_par}, open(os.path.join(a.out, an['id'] + '.json'), 'w'))
    print(an['id'], round(tot, 1), 's', 'STIMA' if not a.voce else 'misurata')

if __name__ == '__main__': main()
