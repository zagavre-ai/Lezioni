# -*- coding: utf-8 -*-
# Sottotitoli, timeline, scheda di pubblicazione e testo YouTube dal montaggio finale (tempi = quelli del video finale).
import sys, os, json, re
sys.path.insert(0, '/tmp/claude-0/l15')
from dati import *
from plan2 import AN_OF, tracts, plan, load
import corr
from sl2 import DISP
from extra import vdur, vname
from quiz import Q
import mk_static as MS
W = '/tmp/claude-0/l15'; OUT = W + '/out'
TL = json.load(open(f'{OUT}/tl.json'))          # [(nome, start_s, frames)]
START = {n: s for n, s, _ in TL}; FR = {n: f for n, _, f in TL}
total = TL[-1][1] + TL[-1][2] / 30.0
T = {v['nome']: v['testo'] for v in json.load(open(W + '/voci_testi_nuovi.json'))}
segs_all = load()
def ts(t):
    h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return '%02d:%02d:%06.3f' % (h, m, s)

def prof_cues():
    cues = []
    names = [('intro', 'intro')] + [(f'prof{pos}_{k + 1}', f'T{n}_{k}') for pos, n in enumerate(GLOBAL_ORDER, 1) for k in range(10) if os.path.exists(f'{W}/pieces/T{n}_{k}.mp4.json')]
    for tl_name, f in names:
        j = json.load(open(f'{W}/pieces/{f}.mp4.json')); subs = j['subs']; N = j['N']; base = START[tl_name]; acc = 0.0; used = 0
        for si, (a, b) in enumerate(subs):
            nf = int(round((b - a) * 30)) if si < len(subs) - 1 else N - used
            ss = [s for s in segs_all if s['inizio'] >= a - 0.05 and s['fine'] <= b + 0.05]
            for (c0, c1, tx) in corr.cues(ss): cues.append((base + acc + (c0 - a), base + acc + (c1 - a), tx))
            acc += nf / 30.0; used += nf
    return cues

def chunks(txt, maxc=84):
    parts = re.split(r'(?<=[\.\!\?:])\s+', txt); out = []; cur = ''
    for p in parts:
        if len(cur) + len(p) + 1 > maxc and cur: out.append(cur); cur = p
        else: cur = (cur + ' ' + p).strip()
    if cur: out.append(cur)
    return out

def voice_cues(piece, off, name, cues):
    d = vdur(name); txt = DISP(T[name]); ch = chunks(txt); tot = sum(len(c) for c in ch); t = START[piece] + off
    for c in ch:
        dd = d * len(c) / tot; cues.append((t, t + dd - 0.05, c)); t += dd

def kore_cues():
    cues = []
    i = json.load(open(f'{W}/info/cover.json')); voice_cues('cover', i['audio'][0][0], 'BEN_R2', cues)
    i = json.load(open(f'{W}/info/agenda.json')); voice_cues('agenda', i['audio'][0][0], 'DP', cues)
    for pos, n in enumerate(GLOBAL_ORDER, 1):
        for k, an in enumerate(AN_OF[n], 1):
            nm = f'an{pos}_{k}'; i = json.load(open(f'{W}/info/an{n}_{k}.json')); name = f'AN{an}'
            ss = MS.sents(T[name]); st = MS.starts(name, ss); d = vdur(name)
            for j, s in enumerate(ss):
                a = START[nm] + i['audio'][0][0] + st[j]; b = START[nm] + i['audio'][0][0] + (st[j + 1] if j + 1 < len(ss) else d)
                cues.append((a, b - 0.05, DISP(s)))
        voice_cues(f'pillola{pos}', 0.9, f'PI{n}', cues)
        i = json.load(open(f'{W}/info/S{pos}.json'))
        for k, (off, kind, path) in enumerate(i['audio'], 1):
            nm = f'SC{n}_{k}'; d = vdur(nm); cues.append((START[f'schema{pos}'] + off, START[f'schema{pos}'] + off + d, DISP(T[nm])))
    i = json.load(open(f'{W}/info/GL.json'))
    for (off, kind, path), nm in zip(i['audio'], ['GL0'] + [f'GL{x + 1}' for x in range(len(GLOSS))]):
        d = vdur(nm); cues.append((START['glossario'] + off, START['glossario'] + off + d, DISP(T[nm])))
    voice_cues('riepilogo', 0.8, 'FIN', cues)
    for k in range(1, 5): voice_cues(f'compito{k}', 0.5, f'CPT{k}', cues)
    return cues

def write_vtt(path):
    cues = sorted(prof_cues() + kore_cues())
    res = []
    for a, b, tx in cues:
        if res and a < res[-1][1]: res[-1] = (res[-1][0], a - 0.02, res[-1][2])
        res.append((a, b, tx))
    res = [c for c in res if c[1] > c[0] + 0.1]
    with open(path, 'w') as f:
        f.write('WEBVTT\n\n')
        for a, b, tx in res: f.write(f'{ts(a)} --> {ts(b)}\n{corr.wrap2(tx)}\n\n')
    print('vtt', len(res), 'cue'); return res

def export_timeline(path):
    rows = []
    for n, s, f in TL:
        m = re.match(r'titolo(\d+)$', n)
        if m: nm = f'T{m.group(1)}'
        elif re.match(r'quiz(\d+)$', n): nm = 'Q' + n[4:]
        elif n.startswith('prof'): nm = 'D' + n
        elif n == 'intro': nm = 'Dintro'
        elif n == 'cover': nm = 'cover1'
        elif n.startswith('pillola'): nm = 'r' + n[7:]
        elif n.startswith('schema'): nm = 'sch' + n[6:]
        elif n == 'glossario': nm = 'gloss1'
        elif n == 'riepilogo': nm = 'f1'
        elif n == 'verifica': nm = 'V1'
        elif n == 'compiti': nm = 'C1'
        elif n.startswith('compito'): nm = 'cpt' + n[7:]
        else: nm = n
        rows.append([nm, round(s, 3), round(f / 30.0, 3)])
    json.dump(rows, open(path, 'w')); return rows

def write_scheda(path, ytpath, dur_final):
    args = []; quiz = {}
    for pos, n in enumerate(GLOBAL_ORDER, 1):
        args.append({"n": pos, "titolo": ARG[n - 1]['nome'], "inizio_s": round(START[f'titolo{pos}'], 3), "quiz_s": round(START[f'quiz{pos}'], 3)})
        quiz[f'Q{pos}'] = {"title": f"Quiz {pos} · {ARG[n - 1]['nome']}", "items": [{"p": p, "a": a, "w": w, "e": e} for p, a, w, e in Q[n]]}
    d = {"materia": "Storia", "titolo": f"Storia V · {LEZ_TITOLO}", "durata_s": round(dur_final, 2), "argomenti": args, "quiz": quiz,
         "t_verifica": round(START['verifica'], 2), "t_compiti": round(START['compiti'], 2)}
    json.dump(d, open(path, 'w'), ensure_ascii=False, indent=1)
    mm = lambda t: '%d:%02d' % (t // 60, t % 60)
    L = ["TITOLO:", d['titolo'], "", "DESCRIZIONE:", f"Storia V · {LEZ_TITOLO}", "Docente: Prof. Giorgio Mazzotti", "Centro Studi Telesio", "", "Argomenti:", "0:00 Introduzione"]
    L.append(f"{mm(START['agenda'])} Di cosa parliamo")
    for a in args: L.append(f"{mm(a['inizio_s'])} {a['n']}. {a['titolo']}")
    L += [f"{mm(START['glossario'])} Glossario e ripasso finale", f"{mm(START['verifica'])} Verifica finale", f"{mm(START['compiti'])} Compiti", "",
          "Al termine di ogni argomento il video si ferma per il quiz di verifica (5 domande).", "Sottotitoli in italiano disponibili.", "© Centro Studi Telesio. Riproduzione vietata."]
    open(ytpath, 'w').write('\n'.join(L) + '\n')

if __name__ == '__main__':
    dur = float(sys.argv[1]) if len(sys.argv) > 1 else total
    write_vtt(f'{OUT}/Storia_Lez15_Parte1.vtt'); export_timeline(f'{OUT}/timeline_Parte1.json'); write_scheda(f'{OUT}/scheda_pubblicazione_Parte1.json', f'{OUT}/testo_youtube_Parte1.txt', dur)
