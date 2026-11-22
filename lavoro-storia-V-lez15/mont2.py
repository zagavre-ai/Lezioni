# -*- coding: utf-8 -*-
# Montaggio finale della Lezione 15 (correzioni 22/11): una sola Parte, audio mixato a -16 LUFS, codifica finale a gruppi.
import sys, os, json, subprocess, re, math, wave
import numpy as np
sys.path.insert(0, '/tmp/claude-0/l15')
from dati import *
from plan2 import AN_OF, tracts, plan
from assemble import Timeline, build_video, mix_audio, nframes, SR, XF, readwav
from extra import vdur, vname, norm_encode, VOX48
W = '/tmp/claude-0/l15'
KIT = '/home/user/Lezioni/kit'
SND = KIT + '/suoni'
OUT = W + '/out'; os.makedirs(OUT, exist_ok=True); os.makedirs(W + '/aud', exist_ok=True)
def vf(name): return f'{VOX48}/{vname(name)}.wav'
def sh(c): subprocess.run(c, check=True)
def info(n): return json.load(open(f'{W}/info/{n}.json'))

def prep_fixed():
    """sigla, sigla finale: ricodifica standard e audio a 48 kHz stereo"""
    for nm, src in [('sigla', 'Sigla_Storia_15s.mp4'), ('finale', 'Sigla_finale_5s_con_avviso_diritti.mp4')]:
        out = f'{W}/pieces/{nm}.mp4'
        if not os.path.exists(out): norm_encode(f'{KIT}/sigle/{src}', out)
        a = f'{W}/aud/{nm}.wav'
        if not os.path.exists(a): sh(['ffmpeg', '-y', '-v', 'error', '-i', f'{KIT}/sigle/{src}', '-vn', '-ac', '2', '-ar', '48000', '-c:a', 'pcm_s16le', a])

def norm_sch(name, out, limit=None):
    if not os.path.exists(out): norm_encode(f'{W}/sch/{name}.mp4', out, limit)
    return out

def prof_audio_events(name):
    """eventi 'prof': per ogni sotto-intervallo (inizio sorgente, fotogrammi) cosi' l'audio e il video escono insieme al fotogramma"""
    j = json.load(open(f'{W}/pieces/{name}.mp4.json')); subs = j['subs']; N = j['N']; ev = []; used = 0
    for si, (x, y) in enumerate(subs):
        nf = int(round((y - x) * 30)) if si < len(subs) - 1 else N - used
        ev.append((x, nf)); used += nf
    return ev

def build_timeline():
    prep_fixed(); segs, topics, intro, pageidx, dmin, isimg = plan(); TT = {T['n']: T for T in topics}
    T = Timeline(); S = lambda x: SND + '/' + x; P = W + '/pieces'
    T.add('sigla', f'{P}/sigla.mp4', [(0, 'wav', W + '/aud/sigla.wav')], 'sigla')
    i = info('cover'); T.add('cover', f'{P}/cover.mp4', [tuple(a) for a in i['audio']], 'cover')
    T.add('intro', f'{P}/intro.mp4', [(0, 'prof', prof_audio_events('intro'))], 'prof')
    i = info('agenda'); T.add('agenda', f'{P}/agenda.mp4', [tuple(a) for a in i['audio']], 'agenda')
    for pos, n in enumerate(GLOBAL_ORDER, 1):
        T.add(f'titolo{pos}', norm_sch(f'T{pos}', f'{P}/title{pos}.mp4'), [(0, 'wav', S('titolo.wav'))], f'titolo{pos}')
        ntr = len(tracts(segs, TT[n])[0]); ans = AN_OF[n]
        for k in range(ntr):
            T.add(f'prof{pos}_{k + 1}', f'{P}/T{n}_{k}.mp4', [(0, 'prof', prof_audio_events(f'T{n}_{k}'))], 'prof')
            if k < len(ans):
                i = info(f'an{n}_{k + 1}'); T.add(f'an{pos}_{k + 1}', f'{P}/an{n}_{k + 1}.mp4', [tuple(a) for a in i['audio']], f'an{pos}_{k + 1}')
        d = vdur(f'PI{n}'); cap_end = json.load(open(f'{W}/sch/R{pos}.json'))['caps'][-1][1] if os.path.exists(f'{W}/sch/R{pos}.json') else d + 1.2
        T.add(f'pillola{pos}', norm_sch(f'R{pos}', f'{P}/rep{pos}.mp4'), [(0, 'wav', S('repaso.wav')), (0.9, 'wav', vf(f'PI{n}'))], f'pillola{pos}')
        i = info(f'S{pos}'); T.add(f'schema{pos}', f'{P}/S{pos}.mp4', [tuple(a) for a in i['audio']], f'schema{pos}')
        T.add(f'quiz{pos}', norm_sch(f'Q{pos}', f'{P}/quiz{pos}.mp4', 4.6), [(0.5, 'wav', S('quiz.wav'))], f'quiz{pos}')
    i = info('GL'); T.add('glossario', f'{P}/GL.mp4', [tuple(a) for a in i['audio']], 'glossario')
    T.add('riepilogo', norm_sch('F', f'{P}/fin.mp4', vdur('FIN') + 2.5), [(0.8, 'wav', vf('FIN'))], 'riepilogo')
    T.add('verifica', norm_sch('V', f'{P}/ver.mp4', 4.6), [(0.5, 'wav', S('quiz.wav'))], 'verifica')
    T.add('finale', f'{P}/finale.mp4', [(0, 'wav', W + '/aud/finale.wav')], 'finale')
    T.add('compiti', norm_sch('C', f'{P}/comp.mp4'), [(0, 'wav', S('titolo.wav'))], 'compiti')
    for k in (1, 2):
        i = info(f'CPS{k}'); T.add(f'compito{k}', f'{P}/CPS{k}.mp4', [tuple(a) for a in i['audio']], f'compito{k}')
    for i in range(1, len(T.pieces)): T.pieces[i]['audio'].append((0, 'wav', S('trans.wav')))
    return T

def mix_prof(T, out_wav):
    """mix: voci, jingle e parlato del prof; il parlato del prof e' tagliato a fotogrammi interi"""
    prof = np.frombuffer(open(W + '/aud/prof.wav', 'rb').read()[44:], dtype=np.int16).astype(np.float32) / 32768
    total = int(round(T.total_frames() / 30.0 * SR)); mix = np.zeros((total, 2), dtype=np.float32)
    for p in T.pieces:
        t0 = int(round(p['start'] * SR / 30))
        for off, kind, arg in p['audio']:
            if kind == 'wav': a = readwav(arg)
            else:
                segs_ = []
                for x, nf in arg:
                    sg = prof[int(round(x * SR)): int(round(x * SR)) + nf * (SR // 30)].copy(); f = int(0.01 * SR)
                    sg[:f] *= np.linspace(0, 1, f); sg[-f:] *= np.linspace(1, 0, f); segs_.append(sg)
                a = np.repeat(np.concatenate(segs_)[:, None], 2, axis=1)
            s = t0 + int(round(off * SR)); e = min(total, s + len(a)); mix[s:e] += a[:e - s]
    return mix

def write(arr, path):
    pcm = (np.clip(arr, -1, 1) * 32767).astype(np.int16)
    w = wave.open(path, 'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes()); w.close()

def main():
    T = build_timeline()
    json.dump([{k: v for k, v in p.items() if k != 'audio'} for p in T.pieces], open(f'{OUT}/timeline_raw.json', 'w'), indent=1)
    print('durata', round(T.total_frames() / 30, 1), 's', len(T.pieces), 'pezzi', flush=True)
    video = f'{OUT}/video_nov.mp4'
    if not os.path.exists(video + '.ok'):
        build_video(T, video, f'{OUT}/tmp'); open(video + '.ok', 'w').write('1')
    mix = mix_prof(T, None)
    mx = np.abs(mix).max(); print('picco mix', mx)
    write(np.clip(mix, -0.95, 0.95), f'{OUT}/audio_pre.wav')
    r = subprocess.run(['ffmpeg', '-nostats', '-i', f'{OUT}/audio_pre.wav', '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True).stderr
    I = float(re.findall(r'\n\s+I:\s+(-?[\d\.]+) LUFS', r)[-1]); gain = 10 ** ((-16.0 - I) / 20.0); print('LUFS prima %.2f, guadagno %.2f dB' % (I, 20 * math.log10(gain)))
    write(np.clip(mix * gain, -1, 1), f'{OUT}/audio_g.wav')
    # limitatore leggero sui picchi (-1,2 dBTP)
    sh(['ffmpeg', '-y', '-v', 'error', '-i', f'{OUT}/audio_g.wav', '-af', 'alimiter=limit=0.87:attack=3:release=40:level=disabled', '-c:a', 'pcm_s16le', f'{OUT}/audio.wav'])
    json.dump([(p['name'], round(p['start'] / 30, 3), p['n']) for p in T.pieces], open(f'{OUT}/tl.json', 'w'))
    print('pronto per la codifica finale')

if __name__ == '__main__':
    main()
