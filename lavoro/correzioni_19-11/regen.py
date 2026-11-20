# -*- coding: utf-8 -*-
# Rigenera timeline_ParteN.json, scheda_pubblicazione_ParteN.json e testo_youtube_ParteN.txt SUL VIDEO FINALE:
# gli istanti dei titoli e dei quiz sono MISURATI sul video (correlazione con il suono dei kit); gli altri vengono dalla timeline e sono controllati su questi.
# uso: python3 regen.py PARTE
import sys, os, json, subprocess, zipfile, numpy as np
sys.path.insert(0, '/tmp/claude-0/l17')
from dati import PARTI, POFF, ARG
P = int(sys.argv[1]); order = PARTI[P]; off = POFF[P]
WK = '/home/user/w/l17/work'; OUT = f'{WK}/out{P}'; B = '/home/user/w/b17'
V = f'{OUT}/Storia_Lez17_Parte{P}_1080p.mp4'
tl = json.load(open(f'{B}/timeline_Parte{P}.json')); ST = dict(tl)
z = zipfile.ZipFile('/home/user/w/b04/Telesio_kit_produzione_v1.zip')
def ref(name):
    n = [x for x in z.namelist() if x.endswith('snd/' + name)][0]; open('/tmp/_r.wav', 'wb').write(z.read(n)); return rd('/tmp/_r.wav')[:16000]
SR = 8000
def rd(f, ss=None, d=None):
    c = ['ffmpeg', '-v', 'error'] + (['-ss', str(ss), '-t', str(d)] if ss is not None else []) + ['-i', f, '-ac', '1', '-ar', str(SR), '-f', 's16le', '-']
    return np.frombuffer(subprocess.run(c, capture_output=True).stdout, np.int16).astype(float)
def find(rf, t0, delta):
    s = max(0, t0 - 1.5); x = rd(V, s, 5); c = np.correlate(x, rf, 'valid'); return s + int(np.argmax(c)) / SR - delta
rq = ref('quiz.wav'); rt = ref('titolo.wav')
dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', V], capture_output=True, text=True).stdout)
meas = {}; rep = []
for pos in range(1, len(order) + 1):
    g = pos + off
    mq = find(rq, ST[f'quiz{g}'] + 0.5, 0.5); mt = find(rt, ST[f'titolo{g}'], 0.0)
    rep.append((f'quiz{g}', ST[f'quiz{g}'], mq)); rep.append((f'titolo{g}', ST[f'titolo{g}'], mt)); meas[f'quiz{g}'] = mq; meas[f'titolo{g}'] = mt
for nm, a, b in rep: print(f'{nm}: timeline {a:.3f} misurato {b:.3f} scarto {b - a:+.3f}')
bad = [r for r in rep if abs(r[2] - r[1]) > 0.1]
assert not bad, bad
T2 = [[nm, round(meas.get(nm, st), 3)] for nm, st in tl]
json.dump(T2, open(f'{OUT}/timeline_Parte{P}.json', 'w'))
S = {nm: st for nm, st in T2}
old = json.load(open(f'{B}/scheda_pubblicazione_Parte{P}.json'))
args = [{"n": a['n'], "titolo": a['titolo'], "inizio_s": round(S[f"titolo{a['n']}"], 3), "quiz_s": round(S[f"quiz{a['n']}"], 3)} for a in old['argomenti']]
d = dict(old); d['durata_s'] = round(dur, 2); d['argomenti'] = args
if P == 3:
    d['t_verifica'] = round(S['finale'], 2); d['t_compiti'] = round(S['finale'], 2)
json.dump(d, open(f'{OUT}/scheda_pubblicazione_Parte{P}.json', 'w'), ensure_ascii=False, indent=1)
mmss = lambda t: '%d:%02d' % (t // 60, t % 60)
L = ["TITOLO:", d['titolo'], "", "DESCRIZIONE:", d['titolo'], "Docente: Prof. Giorgio Mazzotti", "Centro Studi Telesio", "", "Argomenti:", "0:00 Introduzione"]
for a in args: L.append(f"{mmss(a['inizio_s'])} {a['n']}. {a['titolo']}")
L.append(f"{mmss(S['glossario'])} Glossario e ripasso finale")
L += ["", "Al termine di ogni argomento il video si ferma per il quiz di verifica (5 domande).", "Sottotitoli in italiano disponibili.", "© Centro Studi Telesio. Riproduzione vietata."]
open(f'{OUT}/testo_youtube_Parte{P}.txt', 'w').write('\n'.join(L) + '\n')
print('rigenerati timeline, scheda, testo YouTube; durata', round(dur, 2))
