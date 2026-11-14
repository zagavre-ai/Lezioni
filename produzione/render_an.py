#!/usr/bin/env python3
"""Renderizza tutti gli AN di una lezione. Uso: render_an.py lezNN --vox cartella_wav --out cartella [--solo P1_AN1,...]
Senza wav usa silenzio della durata stimata (STIMA, segnato nel .json)."""
import sys, os, json, subprocess, importlib, argparse, shutil
QUI = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, QUI); sys.path.insert(0, '/home/user/Lezioni/kit/tools')
from playwright.sync_api import BrowserType
_l = BrowserType.launch
BrowserType.launch = lambda self, **k: _l(self, **{'executable_path': '/opt/pw-browsers/chromium', **k})
from playwright.sync_api import Page
import tempfile
_sc = Page.set_content
def _sc2(self, html, **k):
    f = tempfile.NamedTemporaryFile('w', suffix='.html', delete=False, encoding='utf-8'); f.write(html); f.close()
    self.goto('file://' + f.name); os.unlink(f.name)
Page.set_content = _sc2
import mappa as M, approfondimento as A
ap = argparse.ArgumentParser(); ap.add_argument('lez'); ap.add_argument('--vox'); ap.add_argument('--out', required=True); ap.add_argument('--solo')
o = ap.parse_args(); sys.path.insert(0, os.path.join(QUI, o.lez))
sp = importlib.import_module('spec_extra') if os.path.exists(os.path.join(QUI, o.lez, 'spec_extra.py')) else importlib.import_module('spec')
os.makedirs(o.out, exist_ok=True)
if not o.solo:   # un processo per ogni AN, con timeout e un nuovo tentativo (il browser ogni tanto si blocca)
    for a in sp.ANS:
        nome = f"P{a['parte']}_{a['id']}"
        if os.path.exists(f'{o.out}/{nome}.mp4') and os.path.exists(f'{o.out}/{nome}.json') and (o.vox is None or not json.load(open(f'{o.out}/{nome}.json'))['stima'] or not os.path.exists(os.path.join(o.vox, nome + '.wav'))): continue
        for t in range(3):
            try:
                subprocess.run([sys.executable, __file__, o.lez, '--out', o.out, '--solo', nome] + (['--vox', o.vox] if o.vox else []), timeout=240, check=True); break
            except Exception as e: print('riprovo', nome, e, flush=True)
    sys.exit()
def sil(sec, p): subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=mono', '-t', f'{sec:.2f}', p], check=True)
for a in sp.ANS:
    nome = f"P{a['parte']}_{a['id']}"
    if o.solo and nome not in o.solo.split(','): continue
    txt = sp.voce_testo(a); par = len(txt.split()); w = os.path.join(o.vox or '/nonesiste', nome + '.wav')
    tmp = os.path.join(o.out, nome + '_voce.wav'); stima = not os.path.exists(w)
    if stima: sil(par / A.VPS + 1.5, tmp)
    else: subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', w, '-af', 'loudnorm=I=-16:TP=-1.5:LRA=11', '-ar', '48000', '-ac', '1', tmp], check=True)
    tot = A.dur(tmp); d = os.path.join(o.out, nome)
    if a['tipo'] == 'mappa':
        os.makedirs(d, exist_ok=True); json.dump(a['mappa'], open(f'{d}/mappa.json', 'w'), ensure_ascii=False)
        cum = 0; t = []
        for i, vv in enumerate(a['voci']):
            if i > 0: t.append(max(0.8, tot * cum / par))
            cum += len(vv.split())
        sys.argv = ['mappa.py', f'{d}/mappa.json', '--out', d, '--voce', tmp, '--tempi', ','.join(f'{x:.2f}' for x in t)]
        M.main(); shutil.move(f'{d}/mappa.mp4', f'{o.out}/{nome}.mp4')
        json.dump({'id': nome, 'durata_s': round(tot, 2), 'stima': stima, 'parole': par}, open(f'{o.out}/{nome}.json', 'w'))
        print(nome, round(tot, 1), 'STIMA' if stima else 'misurata')
    else:
        j = dict(a); j['id'] = nome; json.dump(j, open(f'{o.out}/{nome}_an.json', 'w'), ensure_ascii=False)
        sys.argv = ['x', f'{o.out}/{nome}_an.json', '--out', o.out, '--voce', tmp]; A.main()
        os.remove(f'{o.out}/{nome}_an.json')
    j = json.load(open(f'{o.out}/{nome}.json')) if os.path.exists(f'{o.out}/{nome}.json') else {}
    j.update({'id': nome, 'stima': stima, 'durata_s': round(tot, 2), 'parole': par}); json.dump(j, open(f'{o.out}/{nome}.json', 'w'))
    os.remove(tmp)
