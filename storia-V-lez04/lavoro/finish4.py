# -*- coding: utf-8 -*-
# Orchestrazione 22/11 (Storia V lez. 4): pezzi non-prof + montaggio di una Parte.
# uso: python3 finish4.py voci | pezzi P | monta P
import sys, os, json, subprocess, re, glob, shutil
sys.path.insert(0, '/tmp/claude-0/w')
os.environ['PLAYWRIGHT_BROWSERS_PATH'] = '/opt/pw-browsers'
from dati import *
import slides as SL
import kore
from extra import *
import extra
from assemble import *
FASE = sys.argv[1]; P = int(sys.argv[2]) if len(sys.argv) > 2 else 0
MAPDIR = '/home/user/Lezioni/storia-V-lez04/mappe'
VP = W + '/vox_prov'; VA = W + '/vox_all'          # provvisorie / reali-o-provvisorie
for d in (VP, VA, W + '/vox48'): os.makedirs(d, exist_ok=True)
# --- testi di tutte le voci (vecchie + nuove) ---------------------------------------------------------------------------
sys.path.insert(0, '/tmp/w/voci')
import nuovi
ALLT = {v['nome']: v['testo'] for v in json.load(open(W + '/voci/testi_voci.json'))}
for v in nuovi.V: ALLT[v['nome']] = v['testo']
extra.VOX = VA                                         # vdur legge da qui
PROV = set()
def sync_voci():
    """copia le voci reali (se ci sono) in vox_all, altrimenti crea la provvisoria (silenzio di durata stimata 14,7 car/s)."""
    for nm, tx in ALLT.items():
        real = f'{W}/vox/{nm}.wav'; dst = f'{VA}/{nm}.wav'
        if os.path.exists(real):
            shutil.copy(real, dst)
        else:
            d = round(len(tx) / 14.7 + 0.6, 2); p = f'{VP}/{nm}.wav'
            if not os.path.exists(p):
                subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'lavfi', '-i', f'anullsrc=r=48000:cl=mono', '-t', str(d), '-c:a', 'pcm_s16le', p], check=True)
            shutil.copy(p, dst); PROV.add(nm)
        wav48(dst, f'{W}/vox48/{nm}.wav', loud=-16) if os.path.exists(real) else shutil.copy(dst, f'{W}/vox48/{nm}.wav')
    json.dump(sorted(PROV), open(W + '/voci_provvisorie.json', 'w'))
    print('voci provvisorie:', len(PROV))
if FASE == 'voci': sync_voci(); sys.exit()
VOX48 = W + '/vox48'
extra.voice_texts = lambda: ALLT

# --- dati dei pezzi nuovi -----------------------------------------------------------------------------------------------
APIMG = {1: ('map', 1), 2: ('img', 4), 3: ('img', 6), 4: ('img', 8), 5: ('img', 11), 6: ('img', 13), 7: ('img', 16), 8: ('img', 18), 9: ('map', 5), 10: ('img', 21), 11: ('img', 23)}
APTIT = {1: "La rivalità navale anglo-tedesca", 2: "La polveriera d'Europa", 3: "Il meccanismo delle alleanze", 4: "Il dramma della trincea", 5: "Il Patto di Londra",
         6: "Le battaglie di logoramento", 7: "Il fronte interno", 8: "Caporetto e la svolta", 9: "La fine dei grandi imperi", 10: "La pace di Versailles", 11: "Il bilancio umano della guerra"}
APCH = {1: [(1, "Il Regno Unito: storico predominio sui mari"), (2, "Germania: potenziamento della flotta, piano Tirpitz"), (3, "Una minaccia diretta per il Regno Unito"), (4, "Nazionalismi e rivalità economiche: relazioni instabili")],
        2: [(1, "1908: la rivoluzione dei Giovani Turchi indebolisce l'Impero ottomano"), (2, "L'Austria-Ungheria annette la Bosnia-Erzegovina"), (3, "1912-1913: guerre balcaniche, regione instabile"), (4, "Polveriera d'Europa: Austria contro Russia")],
        3: [(1, "28 giugno 1914: Gavrilo Princip uccide Francesco Ferdinando a Sarajevo"), (2, "Ultimatum durissimo dell'Austria-Ungheria alla Serbia"), (3, "28 luglio: scatta la guerra"), (4, "Alleanze: Germania contro Russia e Francia; Belgio e Regno Unito")],
        4: [(1, "800 chilometri di trincee"), (2, "Mitragliatrici, artiglieria, filo spinato, armi chimiche"), (3, "Fango, malattie, parassiti e freddo"), (4, "Gravissimi traumi psicologici")],
        5: [(1, "Agosto 1914: il governo Salandra dichiara la neutralità"), (3, "Neutralisti: maggioranza in Parlamento"), (4, "Interventisti: dominano le piazze, vogliono Trento e Trieste"), (5, "Aprile 1915: Patto di Londra, accordo segreto con l'Intesa")],
        6: [(1, "Cadorna: undici offensive frontali sull'Isonzo"), (2, "1916: Strafexpedition in Trentino"), (3, "Verdun: circa 800.000 vittime"), (4, "Somme: attacco anglo-francese, bilancio devastante")],
        7: [(1, "Fronte interno: tutta la popolazione civile"), (2, "Produzione controllata, razionamento dei beni"), (3, "Privazioni, denutrizione, mercato nero"), (4, "Milioni di donne in fabbrica: emancipazione femminile")],
        8: [(1, "Ottobre 1917: offensiva austro-tedesca a Caporetto"), (2, "Ritirata in totale confusione, migliaia di prigionieri"), (3, "Resistenza sul Piave e sul monte Grappa"), (4, "Armando Diaz sostituisce Cadorna: rancio e licenze")],
        9: [(1, "1918: ultima offensiva tedesca a ovest"), (2, "Amiens: carri armati e mezzo milione di soldati statunitensi"), (3, "24 ottobre: vittoria italiana a Vittorio Veneto"), (4, "Armistizi di Villa Giusti e di Compiègne"), (5, "Crollano quattro imperi")],
        10: [(1, "Wilson: trasparenza diplomatica, libertà dei commerci, nazionalità"), (2, "Società delle Nazioni: debole fin da subito"), (3, "1919, Versailles: condizioni umilianti per la Germania")],
        11: [(1, "Circa 17 milioni di morti"), (2, "1918-1919: la spagnola, oltre 40 milioni di vittime"), (3, "Oltre 40 milioni di feriti: i mutilati"), (4, "Reduci: niente lavoro né pensioni dignitose")]}

def img_of(n):
    k, i = APIMG[n]
    f = f'{W}/img/p{i:02d}.png' if k == 'img' else f'{MAPDIR}/mappa{i}_finale.png'
    return f if os.path.exists(f) else None

def sent_times(name, nsent, lead=0.5):
    """inizio (s, dal principio del pezzo) di ogni frase della voce: pause della voce reale, altrimenti proporzionale ai caratteri"""
    tx = ALLT[name]; ss = re.split(r'(?<=[\.\!\?])\s+', tx.strip()); d = vdur(name); L = [len(s) for s in ss]; tot = sum(L)
    t = 0.0; prop = []
    for l in L: prop.append(t); t += d * l / tot
    if name in PROV or len(ss) < 2: return [lead + x for x in prop], len(ss)
    r = subprocess.run(['ffmpeg', '-v', 'info', '-i', f'{VA}/{name}.wav', '-af', 'silencedetect=n=-38dB:d=0.16', '-f', 'null', '-'], capture_output=True, text=True).stderr
    se = [float(x) for x in re.findall(r'silence_end: ([\d\.]+)', r)]
    out = [0.0]
    for x in prop[1:]:
        c = [s for s in se if abs(s - x) < 2.5 and s > out[-1] + 0.5]
        out.append(min(c, key=lambda s: abs(s - x)) if c else x)
    return [lead + x for x in out], len(ss)

def kore_piece(out, name, kicker, title, chips, imgf, page, tail=1.5, lead=0.5):
    """chips: [(indice_frase, testo)]"""
    if os.path.exists(out): return vdur(name) + lead + tail
    st, ns = sent_times(name, 0, lead)
    ch = [dict(text=t, t0=round(st[min(i, len(st) - 1)] - 0.2, 2)) for i, t in chips]
    dur = round(vdur(name) + lead + tail, 3)
    spec = dict(kicker=kicker, title=title, img=imgf, dur=dur, page=page, chips=ch)
    kore.render_video(spec, out + '.tmp.mp4'); n = norm_encode(out + '.tmp.mp4', out); os.remove(out + '.tmp.mp4')
    return n / 30.0

def build_pieces():
    order = PARTI[P]; off = POFF[P]; info = {}
    pg = {'n': 90}
    def nextpg(): pg['n'] += 1; return pg['n']
    # approfondimenti
    for n in order:
        out = f'{W}/pieces/P{P}_AP{n}.mp4'
        d = kore_piece(out, f'AP{n}', 'APPROFONDIMENTO', APTIT[n], APCH[n], img_of(n), nextpg())
        info[f'AP{n}'] = dict(audio=[(0.5, 'wav', f'{VOX48}/AP{n}.wav')], dur=d)
    # spiegone della Parte precedente
    if P > 1:
        prev = PARTI[P - 1]
        out = f'{W}/pieces/P{P}_SP0.mp4'
        kore_piece(out, f'SP{P}_0', 'RIPASSO', 'Ripasso della parte precedente', [(0, 'Che cosa abbiamo visto nella parte precedente')], None, nextpg(), tail=1.0)
        info['SP0'] = dict(audio=[(0.5, 'wav', f'{VOX48}/SP{P}_0.wav')])
        for i, m in enumerate(prev, 1):
            out = f'{W}/pieces/P{P}_SP{i}.mp4'
            a = ARG[m - 1]; ks = [k for k, _ in a['schema']]; ns = len(re.split(r'(?<=[\.\!\?])\s+', ALLT[f'SP{P}_{i}'].strip()))
            chips = [(min(j + 1, ns - 1), ks[j]) for j in range(5)]
            imgf = img_of(m) if APIMG[m][0] == 'img' else img_of(m)
            kore_piece(out, f'SP{P}_{i}', 'RIPASSO', a['nome'], chips, imgf, nextpg())
            info[f'SP{i}'] = dict(audio=[(0.5, 'wav', f'{VOX48}/SP{P}_{i}.wav')])
    # schemi, glossario (come prima)
    pages = {('schema', n): nextpg() for n in order}; pages[('gloss',)] = nextpg()
    for pos, n in enumerate(order, 1):
        st, N, audio, tot = schema_piece(P, n, pos, pages[('schema', n)])
        out = f'{W}/pieces/P{P}_S{pos}.mp4'
        if not os.path.exists(out): static_piece(st, out)
        info[f'S{pos}'] = dict(n=N, audio=audio)
    gi = GLP[P]; terms = [GLOSS[i] for i in gi]
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
    # copertina (senza riquadro del docente, senza nome)
    SL.render([(f'cover_np_P{P}', SL.html_cover(1, False, order, P if P > 1 else None))], W + '/slpng')
    d = vdur(f'B4_{P}'); N = fr(d + 1.2); out = f'{W}/pieces/P{P}_cover.mp4'
    if not os.path.exists(out): static_piece([(f'{W}/slpng/cover_np_P{P}.png', N)], out)
    info['cover'] = dict(n=N, audio=[(0.5, 'wav', f'{VOX48}/B4_{P}.wav')])
    # verifica e compiti (ultima Parte)
    if P == 3:
        txt = json.load(open('/tmp/w/rev/revisione-storia-V-lez04/compiti.json'))['esercizi']
        d0 = vdur('CP_0'); items = [(f'P3_cp_{k}', SL.frame('', 'Compiti', 130 + k, '<div class=cards style="top:300px">' + ''.join(
            f"<div class='card {'on' if i == k else ''}' style='font-size:34px;line-height:1.4'><div class=num>{i + 1}</div><div>{SL.esc(e['testo'])}</div></div>" for i, e in enumerate(txt)) + '</div>', prof=False, pill='COMPITI', titlesize=56)) for k in range(-1, 4)]
        SL.render(items, W + '/slpng')
        t = 0.6; audio = [(t, 'wav', f'{VOX48}/CP_0.wav')]; t += d0 + 1.0; starts = []
        for k in range(4):
            nm = f'CP_{k + 1}'; audio.append((t, 'wav', f'{VOX48}/{nm}.wav')); starts.append(t); t += vdur(nm) + 1.5
        N = fr(t + 2.0); st = [(f'{W}/slpng/P3_cp_-1.png', fr(starts[0] - 0.1))]
        for k in range(4):
            end = fr(starts[k + 1] - 0.1) if k < 3 else N
            st.append((f'{W}/slpng/P3_cp_{k}.png', end - sum(f for _, f in st)))
        out = f'{W}/pieces/P3_CP.mp4'
        if not os.path.exists(out): static_piece(st, out)
        info['CP'] = dict(n=N, audio=audio)
    json.dump(info, open(f'{W}/pieces/info4_P{P}.json', 'w'), default=str)
    print('pezzi pronti', P)

def run_jobs():
    """pillole e riepilogo (schede blu) per la Parte"""
    extra.make_jobs(P)
    names = [f'P{P}R{pos}' for pos in range(1, len(PARTI[P]) + 1)] + [f'P{P}F']
    if P == 3: json.dump({"type": "quiz", "act": "Verifica finale", "tfs": 70, "topic": "La Prima guerra mondiale", "pts": "per continuare almeno l'80%", "dur": 4.9}, open(f'{W}/jobs/P3V.json', 'w'), ensure_ascii=False); names.append('P3V')
    if P == 3: json.dump({"type": "title", "num": "00", "total": 1, "lines": ["Compiti"], "ex": "Quattro domande aperte", "fs": 150, "lineY": 560, "dur": 3.5}, open(f'{W}/jobs/P3C.json', 'w'), ensure_ascii=False); names.append('P3C')
    subprocess.run(['bash', '-c', 'cd /tmp/claude-0/w; echo ' + ' '.join(names) + ' | tr " " "\\n" | xargs -P 2 -n 1 ./runjob.sh'], check=True)

def sig(out, src, wavout):
    if not os.path.exists(out): norm_encode(src, out)
    if not os.path.exists(wavout): wav48(src, wavout)
    return out

def monta():
    order = PARTI[P]; off = POFF[P]; info = json.load(open(f'{W}/pieces/info4_P{P}.json'))
    T = Timeline(); S = lambda x: SND + '/' + x
    KIT = '/home/user/Lezioni/kit'
    T.add('sigla', sig(W + '/pieces/sigla.mp4', KIT + '/sigle/Sigla_Storia_15s.mp4', W + '/aud/sigla.wav'), [(0, 'wav', W + '/aud/sigla.wav')], 'sigla')
    if P > 1:
        T.add('spiegone0', f'{W}/pieces/P{P}_SP0.mp4', [tuple(a) for a in info['SP0']['audio']], 'spiegone')
        for i in range(1, len(PARTI[P - 1]) + 1):
            T.add(f'spiegone{i}', f'{W}/pieces/P{P}_SP{i}.mp4', [tuple(a) for a in info[f'SP{i}']['audio']], 'spiegone')
    T.add('cover', f'{W}/pieces/P{P}_cover.mp4', [tuple(a) for a in info['cover']['audio']], 'cover')
    if P == 1:
        j = json.load(open(f'{W}/pieces/P1_intro.mp4.json'))
        T.add('intro', f'{W}/pieces/P1_intro.mp4', [(0, 'prof', [tuple(s) for s in j['subs']])], 'prof')
    for pos, n in enumerate(order, 1):
        g = pos + off
        T.add(f'titolo{g}', norm_sch(f'P{P}T{pos}', f'{W}/pieces/P{P}_title{pos}.mp4'), [(0, 'wav', S('titolo.wav'))], f'titolo{g}')
        j = json.load(open(f'{W}/pieces/P{P}_T{n}.mp4.json'))
        T.add(f'prof{g}', f'{W}/pieces/P{P}_T{n}.mp4', [(0, 'prof', [tuple(s) for s in j['subs']])], 'prof')
        T.add(f'appro{g}', f'{W}/pieces/P{P}_AP{n}.mp4', [tuple(a) for a in info[f'AP{n}']['audio']], f'appro{g}')
        k = next((k for k, m in enumerate(MAPPE, 1) if m['dopo'] == n), None)
        if k and os.path.exists(f'{MAPDIR}/mappa{k}.mp4'):
            T.add(f'mappa{n}', f'{MAPDIR}/mappa{k}.mp4', [(0.5, 'wav', f'{VOX48}/MAP{k}.wav')], f'mappa{n}')
        d = vdur(f'PI{n}')
        T.add(f'pillola{g}', norm_sch(f'P{P}R{pos}', f'{W}/pieces/P{P}_rep{pos}.mp4', split_caps(ALLT[f'PI{n}'], d)[-1][1] + 1.2), [(0, 'wav', S('repaso.wav')), (0.9, 'wav', f'{VOX48}/PI{n}.wav')], f'pillola{g}')
        T.add(f'schema{g}', f'{W}/pieces/P{P}_S{pos}.mp4', [tuple(a) for a in info[f'S{pos}']['audio']], f'schema{g}')
        T.add(f'quiz{g}', norm_sch(f'P{P}Q{pos}', f'{W}/pieces/P{P}_quiz{pos}.mp4'), [(0.5, 'wav', S('quiz.wav'))], f'quiz{g}')
    T.add('glossario', f'{W}/pieces/P{P}_GL.mp4', [tuple(a) for a in info['GL']['audio']], 'glossario')
    T.add('riepilogo', norm_sch(f'P{P}F', f'{W}/pieces/P{P}_fin.mp4', vdur(f'F3_{P}') + 1.7), [(0.8, 'wav', f'{VOX48}/F3_{P}.wav')], 'riepilogo')
    if P == 3:
        T.add('verifica', norm_sch('P3V', f'{W}/pieces/P3_ver.mp4'), [(0.5, 'wav', S('quiz.wav')), (0.9, 'wav', f'{VOX48}/VER_0.wav')], 'verifica')
    T.add('finale', sig(W + '/pieces/finale.mp4', KIT + '/sigle/Sigla_finale_5s_con_avviso_diritti.mp4', W + '/aud/finale.wav'), [(0, 'wav', W + '/aud/finale.wav')], 'finale')
    if P == 3:
        T.add('compiti_intro', norm_sch('P3C', f'{W}/pieces/P3_cpi.mp4'), [(0, 'wav', S('titolo.wav'))], 'compiti')
        T.add('compiti', f'{W}/pieces/P3_CP.mp4', [tuple(a) for a in info['CP']['audio']], 'compiti')
    for i in range(1, len(T.pieces)): T.pieces[i]['audio'].append((0, 'wav', S('trans.wav')))
    json.dump([{k: v for k, v in p.items() if k != 'audio'} for p in T.pieces], open(f'{W}/out/timeline_P{P}.json', 'w'), indent=1)
    print('durata', round(T.total_frames() / 30, 1), 's', len(T.pieces), 'pezzi', flush=True)
    video = f'{W}/out/Storia_Lez4_Parte{P}_video.mp4'
    build_video(T, video, f'{W}/out/tmp{P}')
    prof = np.frombuffer(open(W + '/aud/prof.wav', 'rb').read()[44:], dtype=np.int16).astype(np.float32) / 32768
    mix = mix_audio(T, None, prof)
    import wave
    def write(arr, path):
        pcm = (np.clip(arr, -0.89, 0.89) * 32767).astype(np.int16)
        w = wave.open(path, 'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes()); w.close()
    write(mix, f'{W}/out/audio{P}_pre.wav')
    r = subprocess.run(['ffmpeg', '-nostats', '-i', f'{W}/out/audio{P}_pre.wav', '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True).stderr
    I = float(re.findall(r'\n\s+I:\s+(-?[\d\.]+) LUFS', r)[-1]); gain = 10 ** ((-16.0 - I) / 20.0); print('LUFS prima %.2f, guadagno %.2f dB' % (I, 20 * math.log10(gain)))
    write(mix * gain, f'{W}/out/audio{P}.wav')
    json.dump({'timeline': [(p['name'], round(p['start'] / 30, 3), p['n']) for p in T.pieces]}, open(f'{W}/out/tl_P{P}.json', 'w'))
    sh(['ffmpeg', '-y', '-v', 'error', '-i', video, '-i', f'{W}/out/audio{P}.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000',
        '-movflags', '+faststart', f'{W}/out/Storia_Lez4_Parte{P}_1080p.mp4'])
    print('montato', P)

def norm_sch(name, out, limit=None):
    if not os.path.exists(out): norm_encode(f'{W}/sch/{name}.mp4', out, limit)
    return out

if FASE == 'pezzi': sync_voci(); build_pieces()
elif FASE == 'jobs': sync_voci(); run_jobs()
elif FASE == 'monta': sync_voci(); monta()
