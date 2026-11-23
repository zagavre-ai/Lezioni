import sys, subprocess, json, re, os
sys.path.insert(0, '/tmp/claude-0/w/build')
from scenes2 import *
import mapdefs, layout, pickle
from maps import Node, map_scene

P = json.load(open('/tmp/claude-0/w/build/pillole.json'))
TOP = [t['short'] for t in spec.T]
TOPFULL = ["Il nuovo volto di Parigi e la nascita delle Avanguardie", "Matisse e i Fauves", "L'evoluzione di Matisse", "Picasso, Braque e la rivoluzione del Cubismo",
           "Le fasi del Cubismo", "Il Cubismo dei Salons, l'Orfismo e la scultura", "Rousseau, Chagall e Modigliani"]

def explode(name, parts):
    assert norm_join(parts) == norm_join([TXT[name]]), name
    return parts

def S_frags(i):
    t = TXT['S%d' % i]; s = sentences(t)
    if i == 4:
        a = s[0]; k = a.index(' e il periodo rosa'); s = [a[:k].strip(), a[k:].strip()] + s[1:]
        imgs = ['vita', 'acrobata', 'demoiselles', 'demoiselles', None]
    elif i == 5:
        a = s[1]; k = a.index(', con una tavolozza'); s = [s[0], a[:k + 1].strip(), a[k + 1:].strip()] + s[2:]
        imgs = [None, 'vollard', 'violino_tavolozza', None, 'fruttiera']
    elif i == 6:
        a = s[3]; k = a.index('; Picasso'); s = s[:3] + [a[:k + 1].strip(), a[k + 1:].strip()] + s[4:]
        imgs = [None, None, None, None, 'chitarra', None]
    elif i == 7:
        a = s[2]; k = a.index(' alle tradizioni'); b = s[3]; k2 = b.index(' ritratti e nudi')
        s = s[:2] + [a[:k].strip(), a[k:].strip(), b[:k2].strip(), b[k2:].strip()]
        imgs = [None, None, 'chagall_io', 'chagall_parigi', 'nudo', 'jeanne']
    else:
        imgs = {1: [None] * 4, 2: [None, None, None, 'felicita'], 3: [None, 'danza', None, None]}[i]
    return list(zip(explode('S%d' % i, s), imgs))

def simple_dark(sid, label, title, dur, jname, jgain=0.6, jat=0.0, sub=None):
    N = int(dur * FPS); e = Enc(OUT + 'seg/%s.mp4' % sid); track = np.zeros(N * 1600 + SR, np.float32)
    j = vid.jingle(jname)[:int(min(dur - 0.2, len(vid.jingle(jname)) / SR) * SR)]
    place(track, j, jat, jgain, 0.01, 0.6)
    for i in range(N):
        t = i / FPS; im = dark_bg_cached(t, 0.5); a = fade_alpha(t, 0.1, 0.5)
        layer = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
        spaced(ld, (140, 380), label.upper(), F('xbold', 30), (255, 205, 60), 8)
        ld.text((140, 440 + int(20 * (1 - a))), title, font=F('title', 150), fill=(255, 255, 255))
        if sub: ld.text((140, 620), sub, font=F('bold', 48), fill=(92, 214, 255))
        bw = int(300 * ease((t - 0.4) / 0.8)); ld.rounded_rectangle((140, 600, 140 + bw, 608), 4, fill=(92, 214, 255))
        overlay_alpha(im, layer, a); e.put(im)
    return finish(sid, e.close(), track, dict(kind='titolo'))

def from_mp4(sid, path, dur=None):
    v = OUT + 'seg/%s.mp4' % sid
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', path, '-vf', 'scale=1920:1080:flags=lanczos,fps=30,format=yuv420p', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19', '-an', v], check=True)
    n = int(subprocess.run(['ffprobe', '-v', 'error', '-count_packets', '-select_streams', 'v:0', '-show_entries', 'stream=nb_read_packets', '-of', 'csv=p=0', v], capture_output=True, text=True).stdout.strip())
    to48(path, OUT + 'seg/%s_raw.wav' % sid); a = load_wav(OUT + 'seg/%s_raw.wav' % sid)
    return finish(sid, n, a, dict(kind='sigla'))

def load_map(name, M):
    p = '/tmp/claude-0/w/build/lay_%s.pkl' % name
    if os.path.exists(p):
        d = pickle.load(open(p, 'rb'))
        for i, (cx, cy, w) in d.items():
            n = M.nodes[i]
            if n.kind == 'lab': n.cx, n.cy = cx, cy
            else: M.nodes[i] = Node(i, n.text, n.kind, cx, cy, w, n.size, n.shape, n.bold)
    return M

def build(which):
    segs = {}
    if which == 'cover':
        segs['COVER'] = cover_scene('COVER', 'Le Avanguardie', TOPFULL)
    if which == 'siglie':
        segs['SIGLA'] = from_mp4('SIGLA', '/home/user/Lezioni/kit/sigle/Sigla_Storia_arte_15s.mp4')
        segs['SIGLAF'] = from_mp4('SIGLAF', '/home/user/Lezioni/kit/sigle/Sigla_finale_5s_con_avviso_diritti.mp4')
    if which.startswith('T'):
        i = int(which[1:]); segs[which] = title_scene(which, i, spec.ptitle(spec.T[i - 1]['pdf']))
    if which.startswith('S'):
        i = int(which[1:]); segs[which] = appro_scene(which, 'S%d' % i, S_frags(i), TOP[i - 1])
    if which.startswith('P') and which[1:].isdigit():
        i = int(which[1:]); rows = [digits(x) for x in P['P%d' % i]]
        segs[which] = rows_scene(which, 'Pillola di ripasso', 'RIPASSO', TOP[i - 1], rows, 'P%d' % i, P['P%d' % i], lead=1.0, jingle_name='repaso', jingle_at=0.0, jingle_gain=0.8, size=38)
    if which.startswith('Q'):
        i = int(which[1:]); segs[which] = quiz_scene(which, 'Pausa del video · Quiz', 'Quiz %d' % i, TOP[i - 1], "5 domande · serve almeno l'80% per continuare")
    if which == 'GL':
        fr = sentences(TXT['GL'], 20); fr = [x for x in re.split(r'(?<=[.])\s+', TXT['GL'])]
        explode('GL', fr); rows = [digits(x) for x in fr[1:]]
        segs['GL'] = rows_scene('GL', 'Parole chiave', 'GLOSSARIO', 'Le parole della lezione', rows, 'GL', fr, lead=0.8, size=32, x0=860, jingle_name='repaso', jingle_gain=0.5)
    if which == 'RF':
        fr = [x for x in re.split(r'(?<=[.])\s+', TXT['RF'])]; explode('RF', fr); rows = [digits(x) for x in fr[1:]]
        segs['RF'] = rows_scene('RF', 'Ripasso finale', 'RIEPILOGO', 'Argomento per argomento', rows, 'RF', fr, lead=0.8, size=34, x0=860, jingle_name='repaso', jingle_gain=0.5)
    if which == 'VE':
        segs['VE'] = quiz_scene('VE', 'Verifica di sbarramento', 'Verifica finale', 'Le Avanguardie', "10 domande · serve almeno l'80% per continuare")
    if which == 'CI':
        segs['CI'] = simple_dark('CI', 'Adesso tocca a te', 'Compiti', 3.5, 'finale', 0.8)
    if which == 'COMP':
        c = [x['testo'] for x in json.load(open('/tmp/claude-0/w/out/data/compiti.json'))['esercizi']]
        segs['COMP'] = compiti_scene('COMP', c, 'Svolgi i compiti qui sotto e premi Consegna: arrivano al docente nel tuo quaderno dei compiti.')
    if which in ('MAP_FAUVES', 'MAP_CUBISMO', 'MAP_FINALE'):
        defs = {'MAP_FAUVES': (mapdefs.fauves, mapdefs.FR_FAU), 'MAP_CUBISMO': (mapdefs.cubismo, mapdefs.FR_CUB), 'MAP_FINALE': (mapdefs.finale, mapdefs.FR_FIN)}[which]
        M = defs[0]()
        if which == 'MAP_CUBISMO': mapdefs.layout_cubismo(M)
        elif which == 'MAP_FINALE': mapdefs.layout_finale(M)
        else: load_map(which, M)
        sid = {'MAP_FAUVES': 'M2', 'MAP_CUBISMO': 'M5', 'MAP_FINALE': 'MF'}[which]
        segs[sid] = map_scene(sid, M, which, defs[1])
    return segs

if __name__ == '__main__':
    for w in sys.argv[1:]:
        r = build(w); print(w, {k: (v['frames'], v.get('real')) for k, v in r.items()}, flush=True)
