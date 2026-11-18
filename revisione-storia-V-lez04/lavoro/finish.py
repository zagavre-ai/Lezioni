# -*- coding: utf-8 -*-
# Orchestrazione finale: per una Parte costruisce tutti i pezzi, monta, mixa, sottotitola, scrive i file di consegna.
# uso: python3 finish.py <parte> <fase>      fasi: voci | schede | pezzi | monta
import sys, os, json, subprocess, re, glob, time
sys.path.insert(0, '/tmp/claude-0/w')
from dati import *
import slides as SL
from extra import *
from assemble import *
import corr
from plan_prof import plan
P = int(sys.argv[1]); FASE = sys.argv[2]
order = PARTI[P]; off = POFF[P]
os.makedirs(VOX48, exist_ok=True); os.makedirs(W + '/out', exist_ok=True)
NAMES = (sorted({f'PI{n}' for n in order}) + [f'SC{n}_{k}' for n in order for k in range(1, 6)] + [f'BEN{P}', f'FIN{P}', 'GL0']
         + [f'GL{i}' for i in range(1, 11) if (i <= 5) == (P == 1)] + [f'MAP{k}' for k, m in enumerate(MAPPE, 1) if m['dopo'] in order])

def fase_voci():
    for nm in NAMES:
        src = f'{VOX}/{nm}.wav'
        if not os.path.exists(src): print('MANCA', nm); continue
        wav48(src, f'{VOX48}/{nm}.wav', loud=-16)
    print('voci pronte')

def fase_schede():
    """pillole e riepilogo erano state disegnate con durate stimate (14,7 caratteri/s): le ridisegno solo se la voce vera le smentisce"""
    T = voice_texts(); rer = []
    for pos, n in enumerate(order, 1):
        name = f'P{P}R{pos}'; job = json.load(open(f'{W}/jobs/{name}.json')); d = vdur(f'PI{n}'); caps = split_caps(T[f'PI{n}'], d)
        need = caps[-1][1] + 1.2; err = abs(caps[0][1] - job['caps'][0][1])
        print(name, 'voce %.2f s | servono %.2f s, disegnata %.1f s | scarto didascalia %.2f s' % (d, need, job['dur'], err))
        if need > job['dur'] or err > 1.0:
            a = ARG[n - 1]; topic = a['nome']; tfs = 84 if len(topic) <= 30 else max(52, int(84 * 30 / len(topic)))
            json.dump({"type": "repaso", "kicker": "Pillola di storia", "big": "RIPASSO", "topic": topic, "tfs": tfs, "caps": caps, "dur": round(need + 0.5, 1)}, open(f'{W}/jobs/{name}.json', 'w'), ensure_ascii=False)
            for x in (f'{W}/sch/{name}.mp4', f'{W}/pieces/P{P}_rep{pos}.mp4'):
                if os.path.exists(x): os.remove(x)
            rer.append(name)
    d = vdur(f'FIN{P}'); name = f'P{P}F'; job = json.load(open(f'{W}/jobs/{name}.json'))
    print(name, 'voce %.2f s | servono %.2f s, disegnata %.1f s' % (d, d + 1.7, job['dur']))
    if d + 1.7 > job['dur']:
        job['dur'] = round(d + 2.2, 1); json.dump(job, open(f'{W}/jobs/{name}.json', 'w'), ensure_ascii=False)
        for x in (f'{W}/sch/{name}.mp4', f'{W}/pieces/P{P}_fin.mp4'):
            if os.path.exists(x): os.remove(x)
        rer.append(name)
    if rer: subprocess.run(['bash', '-c', 'cd /tmp/claude-0/w; echo ' + ' '.join(rer) + ' | tr " " "\\n" | xargs -P 4 -n 1 ./runjob.sh'], check=True)
    print('ridisegnate:', rer)

def norm_sch(name, out, limit=None):
    if not os.path.exists(out): norm_encode(f'{W}/sch/{name}.mp4', out, limit)
    return out

def fase_pezzi():
    """schema, mappe, glossario, cover con voce"""
    SL.POS.clear(); SL.POS.update({n: i + 1 + off for i, n in enumerate(order)})
    pages = {eval(k): v for k, v in json.load(open(f'{W}/pieces/pages_P{P}.json')).items()}
    info = {}
    # schemi
    for pos, n in enumerate(order, 1):
        st, N, audio, tot = schema_piece(P, n, pos, pages[('schema', n)])
        out = f'{W}/pieces/P{P}_S{pos}.mp4'
        if not os.path.exists(out): static_piece(st, out)
        info[f'S{pos}'] = dict(n=N, audio=audio)
    # mappe
    for k, m in enumerate(MAPPE, 1):
        if m['dopo'] not in order: continue
        d = vdur(f'MAP{k}'); N = fr(d + 1.8)
        items = [(f'P{P}_map{k}_{j}', SL.html_map(k, f, 1)) for j, f in enumerate([0.14, 0.28, 0.42, 0.56, 0.7, 0.84, 1.0])]
        SL.render(items, W + '/slpng')
        t0 = 0.5; t1 = d * 0.9 + 0.5; st = []; prev = 0
        for j in range(7):
            end = fr(t0 + (t1 - t0) * (j + 1) / 7) if j < 6 else N
            if j == 0: end = fr(t0 + (t1 - t0) / 7)
            st.append((f'{W}/slpng/P{P}_map{k}_{j}.png', end - prev)); prev = end
        st[-1] = (st[-1][0], N - sum(f for _, f in st[:-1]))
        out = f'{W}/pieces/P{P}_M{k}.mp4'
        if not os.path.exists(out): static_piece(st, out)
        info[f'M{k}'] = dict(n=N, audio=[(0.5, 'wav', f'{VOX48}/MAP{k}.wav')])
    # glossario
    terms = GLOSS[:5] if P == 1 else GLOSS[5:]
    gi = [0, 1, 2, 3, 4] if P == 1 else [5, 6, 7, 8, 9]
    items = [(f'P{P}_gl_{j}', SL.html_gloss(j, pages[('gloss',)], terms)) for j in range(len(terms))] + [(f'P{P}_gl_e', SL.html_gloss(-1, pages[('gloss',)], terms))]
    SL.render(items, W + '/slpng')
    t = 0.6; audio = [(t, 'wav', f'{VOX48}/GL0.wav')]; t += vdur('GL0') + 1.0; starts = []
    for j, gidx in enumerate(gi):
        nm = f'GL{gidx + 1}'; audio.append((t, 'wav', f'{VOX48}/{nm}.wav')); starts.append(t); t += vdur(nm) + 1.2
    tot = t + 1.5; N = fr(tot)
    st = [(f'{W}/slpng/P{P}_gl_e.png', fr(starts[0] - 0.1))]
    for j in range(len(terms)):
        end = fr(starts[j + 1] - 0.1) if j + 1 < len(terms) else N
        st.append((f'{W}/slpng/P{P}_gl_{j}.png', end - sum(f for _, f in st)))
    out = f'{W}/pieces/P{P}_GL.mp4'
    if not os.path.exists(out): static_piece(st, out)
    info['GL'] = dict(n=N, audio=audio)
    # cover con voce
    d = vdur(f'BEN{P}'); N = fr(d + 1.2)
    out = f'{W}/pieces/P{P}_cover.mp4'
    st = [(f'{W}/slpng/cover_np_notice_P{P}.png', fr(3.0)), (f'{W}/slpng/cover_np_P{P}.png', N - fr(3.0))]
    if not os.path.exists(out): static_piece(st, out)
    info['cover'] = dict(n=N, audio=[(0.5, 'wav', f'{VOX48}/BEN{P}.wav')])
    json.dump(info, open(f'{W}/pieces/info_P{P}.json', 'w'), default=str)
    print('pezzi pronti')

def fase_monta():
    info = json.load(open(f'{W}/pieces/info_P{P}.json'))
    T = Timeline(); S = lambda x: SND + '/' + x
    ev = []   # eventi per sottotitoli e scheda: (tipo, piece)
    T.add('sigla', W + '/pieces/sigla.mp4', [(0, 'wav', W + '/aud/sigla.wav')], 'sigla')
    T.add('cover', f'{W}/pieces/P{P}_cover.mp4', [tuple(a) for a in info['cover']['audio']], 'cover')
    if P == 1:
        j = json.load(open(f'{W}/pieces/P1_intro.mp4.json'))
        T.add('intro', f'{W}/pieces/P1_intro.mp4', [(0, 'prof', [tuple(s) for s in j['subs']])], 'prof')
    for pos, n in enumerate(order, 1):
        g = pos + off
        T.add(f'titolo{g}', norm_sch(f'P{P}T{pos}', f'{W}/pieces/P{P}_title{pos}.mp4'), [(0, 'wav', S('titolo.wav'))], f'titolo{g}')
        j = json.load(open(f'{W}/pieces/P{P}_T{n}.mp4.json'))
        T.add(f'prof{g}', f'{W}/pieces/P{P}_T{n}.mp4', [(0, 'prof', [tuple(s) for s in j['subs']])], 'prof')
        for k, m in enumerate(MAPPE, 1):
            if m['dopo'] == n and n in order:
                T.add(f'mappa{k}', f'{W}/pieces/P{P}_M{k}.mp4', [tuple(a) for a in info[f'M{k}']['audio']], f'mappa{k}')
        d = vdur(f'PI{n}')
        T.add(f'pillola{g}', norm_sch(f'P{P}R{pos}', f'{W}/pieces/P{P}_rep{pos}.mp4', split_caps(voice_texts()[f'PI{n}'], d)[-1][1] + 1.2), [(0, 'wav', S('repaso.wav')), (0.9, 'wav', f'{VOX48}/PI{n}.wav')], f'pillola{g}')
        T.add(f'schema{g}', f'{W}/pieces/P{P}_S{pos}.mp4', [tuple(a) for a in info[f'S{pos}']['audio']], f'schema{g}')
        T.add(f'quiz{g}', norm_sch(f'P{P}Q{pos}', f'{W}/pieces/P{P}_quiz{pos}.mp4'), [(0.5, 'wav', S('quiz.wav'))], f'quiz{g}')
    T.add('glossario', f'{W}/pieces/P{P}_GL.mp4', [tuple(a) for a in info['GL']['audio']], 'glossario')
    T.add('riepilogo', norm_sch(f'P{P}F', f'{W}/pieces/P{P}_fin.mp4', vdur(f'FIN{P}') + 1.7), [(0.8, 'wav', f'{VOX48}/FIN{P}.wav')], 'riepilogo')
    T.add('finale', W + '/pieces/finale.mp4', [(0, 'wav', W + '/aud/finale.wav')], 'finale')
    # trans.wav a ogni cambio
    for i in range(1, len(T.pieces)): T.pieces[i]['audio'].append((0, 'wav', S('trans.wav')))
    json.dump([{k: v for k, v in p.items() if k != 'audio'} for p in T.pieces], open(f'{W}/out/timeline_P{P}.json', 'w'), indent=1)
    print('durata', round(T.total_frames() / 30, 1), 's', len(T.pieces), 'pezzi')
    video = f'{W}/out/Storia_Lez4_Parte{P}_video.mp4'
    build_video(T, video, f'{W}/out/tmp{P}')
    # audio
    prof = np.frombuffer(open(W + '/aud/prof.wav', 'rb').read()[44:], dtype=np.int16).astype(np.float32) / 32768
    mix = mix_audio(T, None, prof)
    import wave
    mx = np.abs(mix).max(); print('picco mix', mx)
    import wave
    def write(arr, path):
        pcm = (np.clip(arr, -0.89, 0.89) * 32767).astype(np.int16)
        w = wave.open(path, 'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes()); w.close()
    write(mix, f'{W}/out/audio{P}_pre.wav')
    r = subprocess.run(['ffmpeg', '-nostats', '-i', f'{W}/out/audio{P}_pre.wav', '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True).stderr
    I = float(re.findall(r'\n\s+I:\s+(-?[\d\.]+) LUFS', r)[-1]); gain = 10 ** ((-16.0 - I) / 20.0); print('LUFS prima %.2f, guadagno %.2f dB' % (I, 20 * math.log10(gain)))
    mix = mix * gain; write(mix, f'{W}/out/audio{P}.wav')
    json.dump({'timeline': [(p['name'], round(p['start'] / 30, 3), p['n']) for p in T.pieces]}, open(f'{W}/out/tl_P{P}.json', 'w'))
    sh(['ffmpeg', '-y', '-v', 'error', '-i', video, '-i', f'{W}/out/audio{P}.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000',
        '-movflags', '+faststart', f'{W}/out/Storia_Lez4_Parte{P}_1080p.mp4'])
    print('montato')

{'voci': fase_voci, 'schede': fase_schede, 'pezzi': fase_pezzi, 'monta': fase_monta}[FASE]()
