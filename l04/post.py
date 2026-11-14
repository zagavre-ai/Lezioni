#!/usr/bin/env python3
"""Dopo l'assemblaggio: timeline, vtt, scheda, dispensa, compiti. uso: post.py  (percorsi fissi in testa)"""
import json, re, os, subprocess, shutil, sys
S = '/tmp/claude-0/-home-user-Lezioni/aa838b16-be86-588f-84fd-78776ad6250d/scratchpad'
L = f'{S}/l04/consegna-letteratura-V-lez04'; O = f'{S}/lez4/outfinale'; AN = f'{S}/lez4/out'; W = f'{S}/lez4/wlavoro'
os.makedirs(O, exist_ok=True)
sys.path.insert(0, f'{S}/lez4'); import spec as SP
FPS = 30
TL = json.load(open(f'{L}/timeline.json')); newpos = json.load(open(f'{W}/newpos.json'))
final = f'{O}/Letteratura_Lez4_Parte1_1080p.mp4'
dur = float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',final],capture_output=True,text=True).stdout)
info = {n: (t, l) for n, t, l in TL}
cuts = []  # (t_old, [AN ids], frames totali)
ans = {n: (a, b) for n, tp, a, b, s, e in [(x[0], x[1], x[2], x[3], x[4], x[5]) for x in newpos] if tp == 'A'}
adur = {x[0]: (x[5] - x[4]) / FPS for x in newpos if x[1] == 'A'}
ins = {}
for a in SP.AN: ins.setdefault(a['dopo'], []).append(a['id'])
for k, ids in ins.items():
    t = info[k][0] + info[k][1]; cuts.append((round(t * FPS) / FPS, ids))
cuts.sort()
def shift(t):  # t_old -> spostamento
    return sum(sum(adur[i] for i in ids) for c, ids in cuts if c <= t + 0.02)
newTL = []
for n, t, l in TL:
    newTL.append([n, round(t + shift(t), 3), l])
for c, ids in cuts:
    s = c + sum(sum(adur[i] for i in i2) for c2, i2 in cuts if c2 < c - 0.02)
    for i in ids:
        newTL.append([i, round(s, 3), round(adur[i], 3)]); s += adur[i]
newTL.sort(key=lambda x: x[1])
json.dump(newTL, open(f'{O}/timeline.json', 'w'))
# VTT
def ts(x): h = int(x // 3600); m = int(x % 3600 // 60); return '%02d:%02d:%06.3f' % (h, m, x % 60)
def pt(s): h, m, r = s.split(':'); return int(h) * 3600 + int(m) * 60 + float(r)
blocks = [b.strip().split('\n') for b in open(f'{L}/Letteratura_Lez4_Parte1.vtt').read().split('\n\n')[1:] if b.strip()]
cues = []
cutt = [c for c, _ in cuts]
for b in blocks:
    a, e = [pt(x) for x in b[0].split(' --> ')]
    for c in cutt:
        if a < c < e: e = c
    cues.append([a + shift(a), e + shift(e - 1e-3) if False else e + shift(a), '\n'.join(b[1:])])
for c, ids in cuts:
    base = c + sum(sum(adur[i] for i in i2) for c2, i2 in cuts if c2 < c - 0.02)
    for i in ids:
        j = json.load(open(f'{AN}/{i}.json'))
        for a, e, tx in j['cue']:
            ws = tx.split()
            # spezza in blocchi da circa 80 caratteri, su 2 righe
            chunks, cur = [], ''
            for w in ws:
                if len(cur) + len(w) > 80: chunks.append(cur); cur = w
                else: cur = (cur + ' ' + w).strip()
            if cur: chunks.append(cur)
            tot = sum(len(x) for x in chunks); t0 = a
            for x in chunks:
                d = (e - a) * len(x) / tot
                half = x.split(); mid = len(half) // 2
                tx2 = ' '.join(half[:mid]) + '\n' + ' '.join(half[mid:]) if len(x) > 42 else x
                cues.append([base + t0, base + t0 + d - 0.02, tx2]); t0 += d
        base += adur[i]
cues.sort(key=lambda c: c[0])
with open(f'{O}/Letteratura_Lez4_Parte1.vtt', 'w') as f:
    f.write('WEBVTT\n\n')
    for a, e, tx in cues: f.write(f'{ts(a)} --> {ts(e)}\n{tx}\n\n')
# scheda
sch = json.load(open(f'{L}/scheda_pubblicazione.json')); nt = {n: t for n, t, l in newTL}
sch['durata_s'] = round(dur, 2)
for a in sch['argomenti']:
    a['inizio_s'] = nt[f'T{a["n"]}']; a['quiz_s'] = nt[f'Q{a["n"]}']
sch['t_verifica'] = nt['VERIFICA']; sch['t_compiti'] = nt['COMPITI']
sch['approfondimenti'] = [{'id': i, 'titolo': a['titolo'], 'inizio_s': nt[i]} for a in SP.AN for i in [a['id']]]
json.dump(sch, open(f'{O}/scheda_pubblicazione.json', 'w'), ensure_ascii=False, indent=1)
# capitoli YouTube
def t(s): s = int(s); return '%d:%02d' % (s // 60, s % 60)
# dispensa: mappe
from pypdf import PdfReader, PdfWriter
r = PdfReader(f'{L}/Dispensa_Letteratura_Lez4.pdf'); w = PdfWriter()
mp = lambda f: PdfReader(f).pages[0]
dopo = {1: 'mappa_finale_dispensa.pdf', 2: 'AN03_dispensa.pdf', 3: 'AN12_dispensa.pdf', 5: 'AN06_dispensa.pdf', 10: 'AN10_dispensa.pdf'}
for i, p in enumerate(r.pages, 1):
    w.add_page(p)
    if i in dopo: w.add_page(mp(f'{AN}/{dopo[i]}'))
w.write(f'{O}/Dispensa_Letteratura_Lez4.pdf')
# compiti del prof
txt = subprocess.run(['pdftotext', '-layout', f'{S}/rel/compiti/LETTERATURA ITALIANA V /LEZIONE 4.pdf', '-'], capture_output=True, text=True).stdout
qs = [re.sub(r'\s+', ' ', x).strip() for x in re.split(r'\n\s*\d\)\s', '\n' + txt.split('LEZIONE 4', 1)[1])[1:]]
json.dump({'titolo': 'Compiti · Naturalismo e Verismo', 'stato': 'compiti del prof. Mazzotti (file «LEZIONE 4.pdf», release mazzotti-letteratura-V)',
           'esercizi': [{'n': i + 1, 'tipo': 'aperta', 'testo': q} for i, q in enumerate(qs)]}, open(f'{O}/compiti.json', 'w'), ensure_ascii=False, indent=1)
for f in ['Quiz_Letteratura_Lez4.txt', 'Test_Letteratura_Lez4.xlsx', 'quiz_argomenti.json']: shutil.copy(f'{L}/{f}', O)
print('durata', dur, 'cues', len(cues), 'compiti', len(qs))
