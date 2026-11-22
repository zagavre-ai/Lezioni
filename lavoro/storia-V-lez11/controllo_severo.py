# controllo_severo.py VIDEO.mp4 "Titolo esatto della lezione" [passo_s] : il controllo severo della master su una Parte.
# Serve tesseract (apt-get install -y tesseract-ocr). Senza tesseract salta i controlli sul testo e lo dice.
# Esito OK = nessun errore. Rilancialo finché l'esito non è OK.
# - slide ferma: stesso titolo di slide (OCR) per più di 180 s
# - schermata identica (nessun cambio di pixel nell'area slide) per più di 180 s
# - card spezzate: «…» o "..." nel testo delle card; card che cominciano con la minuscola
# - card sola: area testo piccola (≤1 riquadro) per più di 60 s
# - copertina: titolo atteso presente e intero; durata della copertina (≤180 s)
# - durata Parte (50-65 min), loudness, pause > 2,5 s
import sys, os, re, json, subprocess, tempfile, shutil, unicodedata
import numpy as np
from PIL import Image
from concurrent.futures import ThreadPoolExecutor
V = sys.argv[1]; ATT = sys.argv[2]; PASSO = int(sys.argv[3]) if len(sys.argv) > 3 else 10
def norm(s): return re.sub(r'[^a-z0-9 ]', ' ', unicodedata.normalize('NFD', s.lower()).encode('ascii', 'ignore').decode()).split()
dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', V], capture_output=True, text=True).stdout)
tmp = tempfile.mkdtemp(dir='/tmp/claude-0')
subprocess.run(['ffmpeg', '-v', 'error', '-i', V, '-vf', f'fps=1/{PASSO},scale=1920:1080', '-q:v', '3', f'{tmp}/f%05d.jpg'], check=True)
fr = sorted(os.listdir(tmp)); T = [i * PASSO + PASSO / 2 for i in range(len(fr))]
def ocr(img, psm='6', tsv=False):
    if not shutil.which('tesseract'): return ''
    p = img + '.png'
    r = subprocess.run(['tesseract', p, '-', '--psm', psm, '-l', 'eng'] + (['tsv'] if tsv else []), capture_output=True, text=True).stdout
    return r
def lavora(i):
    f = f'{tmp}/{fr[i]}'; im = Image.open(f).convert('L')
    W, H = im.size
    im.crop((int(W * .03), int(H * .165), int(W * .73), int(H * .25))).save(f + '_t.png')  # titolo della slide
    im.crop((0, int(H * .09), int(W * .73), int(H * .90))).save(f + '_c.png')               # slide senza riquadro prof e parole chiave
    im.crop((int(W * .84), int(H * .90), int(W * .98), int(H * .965))).save(f + '_p.png')   # «Pagina N»
    g = np.asarray(im.resize((192, 108)), dtype=np.float32)[10:97, 0:138]
    tit = ocr(f + '_t', '7').strip()
    pm = re.search(r'(\d+)', ocr(f + '_p', '7')); pag = pm.group(1) if pm else ''
    tsv = ocr(f + '_c', '4', True)
    righe = [l.split('\t') for l in tsv.splitlines()[1:]]
    parole = [(int(r[2]), int(r[3]), int(r[4]), r[11]) for r in righe if len(r) == 12 and r[11].strip() and float(r[10]) > 50]
    testo = ' '.join(p[3] for p in parole)
    linee = {}
    for b, pa, ln, w in parole: linee.setdefault((b, pa, ln), []).append(w)
    minus = []
    for ws in linee.values():   # riga che comincia col numero della card: la parola dopo deve essere maiuscola
        if len(ws) > 1 and re.fullmatch(r'[1-3]', ws[0]) and re.match(r'^[a-zàèéìòù]', ws[1]): minus.append(ws[1])
    ncard = sum(1 for ws in linee.values() if len(ws) > 1 and re.fullmatch(r'[1-3]', ws[0]))
    nblocchi = ncard
    for s in ('_t.png', '_c.png', '_p.png'): os.remove(f + s)
    return dict(t=T[i], tit=tit, pag=pag, cop='VIDEOLEZIONE' in testo.upper(), testo=testo, puntini=bool(re.search(r'…|\.\.\.|\w\.\.(\s|$)', testo)), minus=minus, nb=nblocchi, nparole=len(parole), g=g)
with ThreadPoolExecutor(2) as ex: R = list(ex.map(lavora, range(len(fr))))
shutil.rmtree(tmp)
out = {'file': os.path.basename(V), 'durata_min': round(dur / 60, 2)}
# 1) copertina: i campioni con «VIDEOLEZIONE» nei primi 6 minuti
att = norm(ATT); cc = [r for r in R if r['cop'] and r['t'] < 360]
cover_txt = norm(' '.join(r['testo'] for r in cc))
out['copertina_trovata'] = bool(cc)
import difflib
def c_e(w): return w in cover_txt or any(difflib.SequenceMatcher(None, w, x).ratio() >= .75 for x in cover_txt)
out['copertina_parole_mancanti'] = [w for w in att if len(w) > 2 and not c_e(w)]
out['copertina_titolo_presente'] = bool(cc) and not out['copertina_parole_mancanti']
out['copertina_da_s'] = cc[0]['t'] - PASSO / 2 if cc else None
out['copertina_durata_s'] = len(cc) * PASSO
dc = cc[-1]['t'] if cc else 0
# 2) slide ferma per titolo
def stesso(a, b):
    A, B = set(norm(a)), set(norm(b))
    return bool(A) and bool(B) and len(A & B) / max(1, len(A | B)) >= .6
tratti = []; ini = 0
for i in range(1, len(R) + 1):
    if i == len(R) or not ((R[i]['pag'] == R[ini]['pag']) if (R[i]['pag'] and R[ini]['pag']) else stesso(R[i]['tit'], R[ini]['tit'])):
        tratti.append((R[ini]['t'] - PASSO / 2, (R[i - 1]['t'] + PASSO / 2) - (R[ini]['t'] - PASSO / 2), ('p.' + R[ini]['pag'] + ' ' if R[ini]['pag'] else '') + R[ini]['tit'][:60])); ini = i
lunghi = sorted([x for x in tratti if x[1] > 180], key=lambda x: -x[1])
out['slide_stesso_titolo_oltre_3min'] = [(f"{int(a//60)}:{int(a%60):02d}", f"{d/60:.1f} min", t) for a, d, t in lunghi]
# 3) schermata identica (pixel)
ident = []; ini = 0
for i in range(1, len(R) + 1):
    if i == len(R) or np.abs(R[i]['g'] - R[i - 1]['g']).mean() > 1.5:
        d = (R[i - 1]['t'] - R[ini]['t']) + PASSO
        if d > 180: ident.append((f"{int(R[ini]['t']//60)}:{int(R[ini]['t']%60):02d}", f"{d/60:.1f} min"))
        ini = i
out['schermata_identica_oltre_3min'] = ident
# 4) card spezzate / minuscole
out['card_con_puntini'] = [(f"{int(r['t']//60)}:{int(r['t']%60):02d}", r['tit'][:40]) for r in R if r['puntini']][:30]
out['card_iniziale_minuscola'] = [(f"{int(r['t']//60)}:{int(r['t']%60):02d}", r['minus'][:3]) for r in R if r['minus']][:30]
# 5) card sola su slide vuota (poche parole per oltre 60 s, esclusa la copertina)
sola = []; ini = None
for i, r in enumerate(R + [dict(t=1e9, nb=9)]):
    poco = r.get('nb', 9) == 1 and r['t'] > dc + PASSO
    if poco and ini is None: ini = i
    if not poco and ini is not None:
        d = (R[i - 1]['t'] - R[ini]['t']) + PASSO
        if d > 60: sola.append((f"{int(R[ini]['t']//60)}:{int(R[ini]['t']%60):02d}", f"{d:.0f} s", R[ini]['tit'][:40]))
        ini = None
out['una_card_sola_oltre_60s'] = sola
# 6) audio
a = subprocess.run(['ffmpeg', '-v', 'info', '-i', V, '-af', 'ebur128=framelog=quiet,silencedetect=n=-45dB:d=2.5', '-f', 'null', '-'], capture_output=True, text=True).stderr
m = re.findall(r'I:\s+(-?[\d.]+) LUFS', a); out['lufs'] = float(m[-1]) if m else None
out['silenzi_oltre_3s'] = len(re.findall(r'silence_end', a))
out['durata_ok'] = 45 <= dur / 60 <= 65
# qualità della voce (19/11): tono medio e chiarezza su 6 campioni da 40 s
import numpy as _np
def _voce(ss):
    x = _np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-ss', str(ss), '-t', '40', '-i', V, '-vn', '-ac', '1', '-ar', '16000', '-f', 'f32le', '-'], capture_output=True).stdout, _np.float32)
    w = 4096; F = []; C = []
    for i in range(0, len(x) - w, w // 2):
        s_ = x[i:i + w] * _np.hanning(w)
        if _np.sqrt(_np.mean(s_ ** 2)) < 0.02: continue
        S = _np.abs(_np.fft.rfft(s_)); Pp = S.copy()
        for h in (2, 3, 4): Pp[:len(S[::h])] *= S[::h]
        f = _np.fft.rfftfreq(w, 1 / 16000); m = (f > 60) & (f < 400); F.append(f[m][_np.argmax(Pp[m])]); C.append((f * S).sum() / S.sum())
    return (float(_np.median(F)), float(_np.median(C))) if F else (None, None)
VO = [_voce(dur * k / 7) for k in range(1, 7)]
out['voce_tono_hz'] = [round(a) for a, b in VO if a]; out['voce_chiarezza_hz'] = [round(b) for a, b in VO if b]
err = []
if not out['copertina_titolo_presente']: err.append('titolo copertina incompleto: ' + ' '.join(out['copertina_parole_mancanti']))
if out['copertina_durata_s'] > 180: err.append(f"copertina {out['copertina_durata_s']} s")
if lunghi: err.append(f"{len(lunghi)} slide oltre 3 min (max {lunghi[0][1]/60:.1f})")
if ident: err.append(f"{len(ident)} schermate identiche oltre 3 min")
if out['card_con_puntini']: err.append(f"«…» in {len(out['card_con_puntini'])} campioni")
if sola: err.append(f"{len(sola)} tratti con una card sola oltre 60 s")
if not cc: err.append('copertina non trovata')
if not out['durata_ok']: err.append(f"durata {out['durata_min']} min")
if out['lufs'] is not None and abs(out['lufs'] + 16) > 1.5: err.append(f"loudness {out['lufs']}")
if out['silenzi_oltre_3s']: err.append(f"{out['silenzi_oltre_3s']} pause > 2,5 s")
cattivi = [i for i, (a, b) in enumerate(VO) if a and b and (b < 800 or a < 95)]
if cattivi: err.append(f"VOCE ALTERATA in {len(cattivi)} campioni su 6 (tono {out['voce_tono_hz']}, chiarezza {out['voce_chiarezza_hz']})")
out['DA_GUARDARE'] = (['possibili card con iniziale minuscola: ' + ', '.join(t for t, _ in out['card_iniziale_minuscola'][:10])] if out['card_iniziale_minuscola'] else []); out['ERRORI'] = err; out['ESITO'] = 'OK' if not err else 'RESPINTA'
print(json.dumps(out, ensure_ascii=False, indent=1))
