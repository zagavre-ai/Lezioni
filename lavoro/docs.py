# -*- coding: utf-8 -*-
# Sottotitoli, scheda di pubblicazione, quiz, testo YouTube, timeline per una Parte.   uso: python3 docs.py <parte>
import sys, os, json, re
sys.path.insert(0, '/tmp/claude-0/l17')
from dati import *
from quiz import Q
import corr
from slides import DISP
from extra import vdur, voice_texts
W = '/tmp/claude-0/l17'
P = int(sys.argv[1]); order = PARTI[P]; off = POFF[P]
OUT = W + '/out'
TL = json.load(open(f'{OUT}/tl_P{P}.json'))['timeline']       # [(nome, start_s, frames)]
START = {n: s for n, s, _ in TL}; FR = {n: f for n, _, f in TL}
segs = json.load(open(TRASCR))
T = voice_texts()
dur = sum(FR[n] for n in FR)  # solo per controllo
total = TL[-1][1] + TL[-1][2] / 30.0

def ts(t):
    h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return '%02d:%02d:%06.3f' % (h, m, s)

def vtt_cues():
    cues = []
    # pezzi del prof
    for name, sub in [(p, None) for p in ['intro'] if P == 1] + [(f'prof{pos + off}', None) for pos in range(1, len(order) + 1)]:
        fn = f'{W}/pieces/P1_intro.mp4.json' if name == 'intro' else f"{W}/pieces/P{P}_T{order[int(name[4:]) - off - 1]}.mp4.json"
        subs = json.load(open(fn))['subs']; base = START[name]; acc = 0.0
        for a, b in subs:
            ss = [s for s in segs if s['inizio'] >= a - 0.05 and s['fine'] <= b + 0.05]
            for (c0, c1, tx) in corr.cues(ss):
                cues.append((base + acc + (c0 - a), base + acc + (c1 - a), tx))
            acc += b - a
    # voci
    def voice(name, piece, off_s, vname):
        d = vdur(vname); txt = DISP(T[vname])
        parts = re.split(r'(?<=[\.\!\?:])\s+', txt)
        chunks = []; cur = ''
        for p in parts:
            if len(cur) + len(p) + 1 > 84 and cur: chunks.append(cur); cur = p
            else: cur = (cur + ' ' + p).strip()
        if cur: chunks.append(cur)
        tot = sum(len(c) for c in chunks); t = START[piece] + off_s
        for c in chunks:
            dd = d * len(c) / tot; cues.append((t, t + dd - 0.05, c)); t += dd
    voice('cover', 'cover', 0.5, BEN[P])
    for pos, n in enumerate(order, 1):
        g = pos + off
        voice('pillola', f'pillola{g}', 0.9, f'PI{n}')
        t = 0.8
        for k in range(1, nc(n) + 1):
            nm = f'SC{n}_{k}'; d = vdur(nm)
            cues.append((START[f'schema{g}'] + t, START[f'schema{g}'] + t + d, DISP(T[nm]))); t += d + 1.8
    for n in order: voice('mappa', f'mappa{n}', 0.5, mapvoice(n))
    t = START['glossario'] + 0.6; cues.append((t, t + vdur('LG0'), T['LG0'])); t += vdur('LG0') + 1.0
    for gi in [i + 1 for i in GLP[P]]:
        d = vdur(f'LG{gi}'); cues.append((t, t + d, DISP(T[f'LG{gi}']))); t += d + 1.2
    voice('riepilogo', 'riepilogo', 0.8, FIN[P])
    cues.sort()
    res = []
    for i, (a, b, tx) in enumerate(cues):
        if res and a < res[-1][1]: res[-1] = (res[-1][0], a - 0.02, res[-1][2])
        res.append((a, b, tx))
    return [c for c in res if c[1] > c[0] + 0.1]

def write_vtt():
    cues = vtt_cues()
    with open(f'{OUT}/Storia_Lez17_Parte{P}.vtt', 'w') as f:
        f.write('WEBVTT\n\n')
        for a, b, tx in cues: f.write(f'{ts(a)} --> {ts(b)}\n{corr.wrap2(tx)}\n\n')
    print('vtt', len(cues), 'cue')

def quiz_items(n):
    return [{"p": p, "a": a, "w": w, "e": e} for p, a, w, e in Q[n]]

def write_scheda():
    args = []; quiz = {}
    for pos, n in enumerate(order, 1):
        g = pos + off
        args.append({"n": g, "titolo": ARG[n - 1]['nome'], "inizio_s": round(START[f'titolo{g}'], 3), "quiz_s": round(START[f'quiz{g}'], 3)})
        quiz[f'Q{g}'] = {"title": f"Quiz {g} · {ARG[n - 1]['nome']}", "items": quiz_items(n)}
    d = {"materia": "Storia", "titolo": f"Storia V · Lezione 17 · {LEZ_TITOLO}" + (f" · Parte {P}" if len(PARTI) > 1 else ""), "durata_s": round(total, 2), "argomenti": args, "quiz": quiz}
    if P == max(PARTI): d['t_verifica'] = round(START['finale'], 2); d['t_compiti'] = round(START['finale'], 2)
    json.dump(d, open(f'{OUT}/scheda_pubblicazione_Parte{P}.json', 'w'), ensure_ascii=False, indent=1)
    # youtube
    def mmss(t): return '%d:%02d' % (t // 60, t % 60)
    L = ["TITOLO:", d['titolo'], "", "DESCRIZIONE:", f"Storia V · Lezione 17 · {LEZ_TITOLO}" + (f" · Parte {P}" if len(PARTI) > 1 else ""), "Docente: Prof. Giorgio Mazzotti", "Centro Studi Telesio", "", "Argomenti:", "0:00 Introduzione"]
    for a in args: L.append(f"{mmss(a['inizio_s'])} {a['n']}. {a['titolo']}")
    L.append(f"{mmss(START['glossario'])} Glossario e ripasso finale")
    L += ["", "Al termine di ogni argomento il video si ferma per il quiz di verifica (5 domande).", "Sottotitoli in italiano disponibili.", "© Centro Studi Telesio. Riproduzione vietata."]
    open(f'{OUT}/testo_youtube_Parte{P}.txt', 'w').write('\n'.join(L) + '\n')
    json.dump([[n, round(s, 3)] for n, s, _ in TL], open(f'{OUT}/timeline_Parte{P}.json', 'w'))
    print('scheda ok; durata', round(total, 1))

write_vtt(); write_scheda()
