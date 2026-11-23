#!/usr/bin/env python3
# 22/11 · CONTROLLO RAPIDO prima della consegna (obbligatorio, 3-5 minuti su una Parte di 55 min).
# Uso:  python3 kit/tools/controllo_rapido.py VIDEO.mp4 "Titolo esatto della lezione" [cartella_uscita]
# Produce, nella cartella d'uscita (default: accanto al video):
#   - foglio_fotogrammi_<nome>.jpg : 24 fotogrammi con il minuto (+ quelli delle pause mute). DA GUARDARE prima di consegnare.
#   - controllo_rapido_<nome>.json : misure ed elenco dei difetti con il minuto.
# Esito OK solo se l'elenco ERRORI è vuoto. Il foglio va consegnato sul ramo revisione insieme al video.
import json, os, re, subprocess, sys, tempfile, shutil
from PIL import Image, ImageDraw, ImageFont

V = sys.argv[1]; TIT = sys.argv[2] if len(sys.argv) > 2 else ''
OUT = sys.argv[3] if len(sys.argv) > 3 else os.path.dirname(os.path.abspath(V))
nome = os.path.splitext(os.path.basename(V))[0]
def sh(c): return subprocess.run(c, capture_output=True, text=True)
dur = float(sh(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', V]).stdout or 0)
mm = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
err, avv, out = [], [], {'video': os.path.basename(V), 'durata_min': round(dur / 60, 2)}

# 1) formato
pr = json.loads(sh(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height,r_frame_rate,nb_frames', '-of', 'json', V]).stdout)['streams'][0]
out['formato'] = f"{pr['width']}x{pr['height']} {pr['r_frame_rate']}"
if (pr['width'], pr['height']) != (1920, 1080): err.append(f"formato {pr['width']}x{pr['height']} (serve 1920x1080)")
if pr['r_frame_rate'] not in ('30/1', '30000/1000'): err.append(f"fotogrammi al secondo {pr['r_frame_rate']} (serve 30)")
mb = os.path.getsize(V) / 1048576; out['peso_MB'] = round(mb)
if mb > 400: err.append(f"peso {mb:.0f} MB (massimo 400)")

# 2) audio: volume e pause mute (oltre 2,5 s) con il minuto
a = sh(['ffmpeg', '-v', 'info', '-i', V, '-vn', '-af', 'ebur128=peak=true,silencedetect=n=-45dB:d=2.5', '-f', 'null', '-']).stderr
m = re.findall(r'I:\s+(-?[\d.]+) LUFS', a); out['LUFS'] = float(m[-1]) if m else None
pk = re.findall(r'Peak:\s+(-?[\d.]+) dBFS', a); out['picco_dBTP'] = float(pk[-1]) if pk else None
if out['LUFS'] is None or abs(out['LUFS'] + 16) > 1: err.append(f"volume {out['LUFS']} LUFS (serve -16 ±1)")
if out['picco_dBTP'] is not None and out['picco_dBTP'] > -1: err.append(f"picco {out['picco_dBTP']} dBTP (massimo -1)")
st = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', a)]; du = [float(x) for x in re.findall(r'silence_duration: ([\d.]+)', a)]
pause = [(s, d) for s, d in zip(st, du)]
out['pause_mute'] = [f"{mm(s)} ({d:.1f} s)" for s, d in pause]
if pause: err.append(f"{len(pause)} pause mute oltre 2,5 s: " + ', '.join(out['pause_mute'][:25]))

# 3) fotogrammi ogni 15 s: piè di pagina (nome del docente), fasce sopra/sotto le schede, schermate uguali
tmp = tempfile.mkdtemp()
sh(['ffmpeg', '-v', 'error', '-i', V, '-vf', 'fps=1/15,scale=960:540', f'{tmp}/f_%05d.png'])
fr = sorted(os.listdir(tmp)); T = [i * 15 for i in range(len(fr))]
nomi_doc = re.compile(r'(?i)\bprof\b|prof\.|mazzotti|caputi|docente')
piede, fasce, prec, fermo_da, fermi = [], [], None, 0, []
for i, f in enumerate(fr):
    im = Image.open(f'{tmp}/{f}').convert('RGB'); W, H = im.size
    # piè di pagina sinistro (ingrandito per l'OCR)
    im.crop((0, int(H * .90), int(W * .62), int(H * .97))).convert('L').resize((int(W * 1.24 * 2), int(H * .07 * 2))).save(f'{tmp}/p.png')
    t = sh(['tesseract', f'{tmp}/p.png', '-', '--psm', '7', '-l', 'eng']).stdout
    if nomi_doc.search(t): piede.append(T[i])
    # fasce colorate sopra e sotto (la scheda non riempie lo schermo)
    px = im.load(); top = [px[x, 3] for x in range(0, W, 40)]; bot = [px[x, H - 4] for x in range(0, W, 40)]; mid = [px[x, H // 2] for x in range(0, W, 40)]
    uni = lambda L: max(max(c) - min(c) for c in zip(*L)) < 12
    if uni(top) and uni(bot) and top[0] == bot[0] and sum(top[0]) < 600 and abs(sum(top[0]) - sum(mid[0])) > 60: fasce.append(T[i])
    # schermata identica
    g = im.crop((0, 0, int(W * .72), H)).convert('L').resize((96, 72)); b = list(g.getdata())  # senza la colonna del docente (la webcam si muove sempre)
    if prec is not None and sum(abs(x - y) for x, y in zip(b, prec)) / len(b) < 0.6: pass
    else:
        if T[i] - fermo_da > 180: fermi.append((fermo_da, T[i] - fermo_da))
        fermo_da = T[i]
    prec = b
if dur - fermo_da > 180: fermi.append((fermo_da, dur - fermo_da))
out['nome_docente_nel_pie_di_pagina'] = [mm(t) for t in piede][:20]
if len(piede) >= 2: err.append(f"nome del docente nel piè di pagina ({len(piede)} fotogrammi, es. {', '.join(mm(t) for t in piede[:4])})")
out['schede_con_fasce'] = [mm(t) for t in fasce][:20]
if fasce: err.append(f"schede che non riempiono lo schermo (fasce sopra e sotto) a {', '.join(mm(t) for t in fasce[:6])}")
out['schermate_ferme_oltre_3_min'] = [f"{mm(a)} per {d / 60:.1f} min" for a, d in fermi]
if fermi: err.append("schermata identica oltre 3 minuti: " + ', '.join(out['schermate_ferme_oltre_3_min']))

# 4) titolo esatto in copertina (primi 6 minuti)
if TIT:
    parole = [w for w in re.findall(r"\w+", TIT.lower()) if len(w) > 2]
    trovate = set()
    for i in range(min(len(fr), 24)):
        tt = sh(['tesseract', f'{tmp}/{fr[i]}', '-', '--psm', '3', '-l', 'eng']).stdout.lower()
        trovate |= {w for w in parole if w in tt}
    out['titolo_in_copertina'] = f"{len(trovate)}/{len(parole)} parole"
    if len(trovate) < max(1, int(len(parole) * .7)): avv.append(f"titolo «{TIT}» non letto bene in copertina: guardalo sul foglio")

# 5) foglio dei fotogrammi: 24 istanti regolari + le pause mute
ist = sorted(set([dur * (k + .5) / 24 for k in range(24)] + [s + min(d, 2) / 2 for s, d in pause[:12]]))
ce = [];
for t in ist:
    p = f'{tmp}/c_{len(ce):03d}.jpg'; sh(['ffmpeg', '-v', 'error', '-y', '-ss', f'{t:.2f}', '-i', V, '-frames:v', '1', '-vf', 'scale=480:270', p])
    if os.path.exists(p): ce.append((t, p))
cols = 4; rows = (len(ce) + cols - 1) // cols
sheet = Image.new('RGB', (cols * 480, rows * 300), 'white'); d = ImageDraw.Draw(sheet)
try: fnt = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 18)
except Exception: fnt = ImageFont.load_default()
muti = {round(s + min(dd, 2) / 2, 2) for s, dd in pause[:12]}
for k, (t, p) in enumerate(ce):
    x, y = (k % cols) * 480, (k // cols) * 300; sheet.paste(Image.open(p), (x, y + 30))
    lab = mm(t) + ('  PAUSA MUTA' if round(t, 2) in muti else ''); d.text((x + 8, y + 5), lab, fill=(179, 38, 30) if 'PAUSA' in lab else (11, 21, 48), font=fnt)
os.makedirs(OUT, exist_ok=True)
fog = f'{OUT}/foglio_fotogrammi_{nome}.jpg'; sheet.save(fog, quality=82)
shutil.rmtree(tmp)
out['foglio'] = os.path.basename(fog); out['ERRORI'] = err; out['DA_GUARDARE'] = avv + [
    'Apri il foglio dei fotogrammi e controlla con gli occhi: fondo bianco; schede di titolo/quiz/ripasso in BLU SCURO a tutto schermo; card a 40 px e intere; '
    'nessun nome del docente fuori dalla fascia gialla; riquadro del docente giusto (Mazzotti 4:3, Caputi tondo); copertina con il titolo esatto; mappe del prof con la legenda BES; '
    'in fondo sigla finale con l\'avviso dei diritti e intro «Compiti».']
out['ESITO'] = 'OK' if not err else 'DA CORREGGERE'
json.dump(out, open(f'{OUT}/controllo_rapido_{nome}.json', 'w'), ensure_ascii=False, indent=1)
print(json.dumps(out, ensure_ascii=False, indent=1))
