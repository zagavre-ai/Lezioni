# -*- coding: utf-8 -*-
# Dispensa A4 orizzontale di una Parte: stesse slide del video (senza riquadro del docente), testo invisibile selezionabile. uso: python3 dispensa.py P
import sys, os, json, re, subprocess, html
sys.path.insert(0, '/tmp/claude-0/w'); os.environ['PLAYWRIGHT_BROWSERS_PATH'] = '/opt/pw-browsers'
from dati import *
import slides as SL, build3 as B, fitz
from plan_prof import plan
W = '/tmp/claude-0/w'; P = int(sys.argv[1]); order = PARTI[P]; off = POFF[P]
sys.path.insert(0,'/tmp/w/voci'); import nuovi
ALLT = {v['nome']: v['testo'] for v in json.load(open(W + '/voci/testi_voci.json'))}; ALLT.update({v['nome']: v['testo'] for v in nuovi.V})
segs, topics, intro, pageidx, dmin, isimg, cp = plan(); B.CPG = cp
D = f'{W}/disp{P}'; os.makedirs(D, exist_ok=True)
pages = []   # (nome, html|png, testo)
def add_html(nm, h, tx): pages.append((nm, ('html', h), tx))
def add_png(nm, f, tx): pages.append((nm, ('png', f), tx))
def frame_of(mp4, t, out):
    d = float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',mp4])); t = min(t, d * 0.8)
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', str(t), '-i', mp4, '-frames:v', '1', out], check=True); return out
def strip(h): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<style.*?</style>|<[^>]+>', ' ', h, flags=re.S))).strip()
pn = 0
add_html('cover', re.sub(r"<div class=card2.*?</ul></div>", '', SL.html_cover(1, False, order, P if P > 1 else None), flags=re.S), 'STORIA V · VIDEOLEZIONE La Prima guerra mondiale')
for pos, n in enumerate(order, 1):
    g = pos + off
    add_png(f'tit{n}', frame_of(f'{W}/sch/P{P}T{pos}.mp4', 2.2, f'{D}/tit{n}.png'), f"Argomento {g} {ARG[n-1]['nome']}")
    seen = set(); j = json.load(open(f'{W}/pieces/P{P}_T{n}.mp4.json'))
    for sk, act, f in j['seq']:
        key = (tuple(sk[:3]) if sk[0] != 'cards' else tuple(sk))
        if key in seen: continue
        seen.add(key); pn += 1
        if sk[0] == 'cards':
            st = eval(sk[2]); cards = ''
            for i in st:
                h, b = SL.head_body(cp[n][i]); cards += f"<div class=card><div class=num>{i+1}</div><div><b>{SL.esc(h)}:</b> {SL.esc(b)}</div></div>"
            h = SL.frame(f"{SL.P2(n):02d} · {ARG[n-1]['nome']}", SL.esc(ARG[n-1]['titolo']), pn, f"<div class=cards>{cards}</div>", prof=False, titlesize=50)
        elif sk[0] == 'img': h = SL.html_img(int(sk[2]), f"{W}/img/p{int(sk[1]):02d}.png", pn, prof=False)
        elif sk[0] == 'imgc': continue
        else: continue
        add_html(f's{n}_{pn}', h, strip(h))
    ap = f'{W}/pieces/P{P}_AP{n}.mp4'; add_png(f'ap{n}', frame_of(ap, 30, f'{D}/ap{n}.png'), 'Approfondimento ' + ALLT[f'AP{n}'])
    k = next((k for k, m in enumerate(MAPPE, 1) if m['dopo'] == n), None)
    if k: add_png(f'map{k}', f'/home/user/Lezioni/storia-V-lez04/mappe/mappa{k}_finale.png', 'Mappa ' + ' '.join(re.findall(r'"text": "([^"]+)"', open('/home/user/Lezioni/storia-V-lez04/mappe/mappe.json').read()[:0] or '')) + MAPPE[k - 1]['titolo'] + ' ' + MAPPE[k - 1]['voce'])
    add_png(f'pil{n}', frame_of(f'{W}/sch/P{P}R{pos}.mp4', 12, f'{D}/pil{n}.png'), 'Ripasso ' + ARG[n - 1]['nome'] + ' ' + ALLT[f'PI{n}'])
    h = SL.html_schema(n, 5, 90 + pos); add_html(f'sch{n}', h, strip(h))
h = SL.html_gloss(-1, 99, [GLOSS[i] for i in GLP[P]]); add_html('gl', h, strip(h))
add_png('fin', frame_of(f'{W}/sch/P{P}F.mp4', 6, f'{D}/fin.png'), 'Riepilogo finale ' + ' '.join(ARG[n - 1]['nome'] for n in order))
# render
from playwright.sync_api import sync_playwright
doc = fitz.open()
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=SL.CHROME, args=['--allow-file-access-from-files', '--no-sandbox']); pg = b.new_page(viewport={'width': 1920, 'height': 1080})
    for nm, (k, v), tx in pages:
        if k == 'html':
            f = f'{D}/{nm}.html'; open(f, 'w').write(v); pg.goto('file://' + f); pg.wait_for_timeout(200); png = f'{D}/{nm}.png'; pg.screenshot(path=png)
        else: png = v
        from PIL import Image as _I
        jp = png.rsplit('.', 1)[0] + '_q.jpg'; _I.open(png).convert('RGB').save(jp, quality=88); png = jp
        page = doc.new_page(width=842, height=595)
        page.insert_image(fitz.Rect(0, (595 - 842 * 9 / 16) / 2, 842, (595 + 842 * 9 / 16) / 2), filename=png)
        page.insert_textbox(fitz.Rect(20, 20, 820, 575), re.sub(r'\s+', ' ', tx), fontsize=6, render_mode=3)
    b.close()
out = f'{W}/out/Storia_Lez4_Parte{P}_dispensa.pdf'; doc.save(out); print(out, len(doc), 'pagine')
