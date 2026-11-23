# Assemblaggio: sequenza delle scene -> un solo file con una sola codifica finale
import sys, os, json, subprocess
sys.path.insert(0, '/home/user/w18')
import kore, prof
from kore import *
from pages import PG
R = '/home/user/w18/'; OUT = R + 'b/'
D = 'dark'; Wt = 'white'

def sequenza():
    """[(nome, tipo, costruttore)] in ordine"""
    S = []
    S.append(('sigla', D, None))
    S.append(('welcome', Wt, lambda: benvenuto()))
    S.append(('prof_D0', Wt, lambda: prof.pezzo('D0')))
    for i, (a, tit) in enumerate(ARGOMENTI, 1):
        S.append((f'tit_{a}', D, lambda i=i, a=a, tit=tit: titolo_scheda(i, a, tit)))
        S.append((f'prof_P{i}', Wt, lambda i=i: prof.pezzo(f'P{i}')))
        S.append((f'ap_{a}', Wt, lambda a=a, tit=tit: approfondimento(a, tit)))
        if a == 'A4': S.append(('map2', Wt, lambda: mappa_scheda('MAP2', 'map2', PG['MAP2'])))
        if a == 'A7': S.append(('map3', Wt, lambda: mappa_scheda('MAP3', 'map3', PG['MAP3'])))
        S.append((f'rip_{a}', D, lambda a=a, tit=tit: pillola(a, tit)))
        S.append((f'quiz_{a}', D, lambda a=a, tit=tit: quiz_scheda(a, tit)))
    S += [('gloss', D, lambda: glossario()), ('rf', D, lambda: ripasso_finale()), ('map1', Wt, lambda: mappa_scheda('MAP1', 'map1', PG['MAP1'])),
          ('verifica', D, lambda: verifica()), ('sigla_fin', D, None), ('compiti_intro', D, lambda: compiti_intro()), ('compiti', D, lambda: compiti())]
    return S

def colori(S):
    """colore della dissolvenza a ogni confine: scuro solo se entrambe le scene sono scure"""
    fade = {}
    for i, (n, t, _) in enumerate(S):
        fin = (D if (i == 0 or S[i - 1][1] == D) and t == D else Wt)
        fout = (D if (i == len(S) - 1 or S[i + 1][1] == D) and t == D else Wt)
        fade[n] = (fin, fout)
    # prima scena dopo la sigla (nera): dissolvenza dal nero
    fade['welcome'] = (D, Wt)
    return fade

def prepara_sigle():
    a = OUT + 'sigla_arte_n.mp4'
    if not os.path.exists(a):
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', OUT + 'sigla_arte.mp4', '-vf', 'fade=t=out:st=14.6:d=0.4:color=black,format=yuv420p', '-r', '30', '-c:v', 'libx264', '-preset', 'ultrafast', '-crf', '14',
                        '-c:a', 'aac', '-b:a', '256k', '-ar', '48000', '-ac', '2', a], check=True)
    b = OUT + 'sigla_fin_n.mp4'
    if not os.path.exists(b):
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', '/home/user/Lezioni/kit/sigle/Sigla_finale_5s_con_avviso_diritti.mp4', '-vf', 'format=yuv420p', '-r', '30', '-c:v', 'libx264', '-preset', 'ultrafast', '-crf', '14',
                        '-c:a', 'aac', '-b:a', '256k', '-ar', '48000', '-ac', '2', b], check=True)
    return a, b

def stereo(p):
    """audio stereo 48k per tutti"""
    o = p.replace('.mp4', '_s.mp4')
    if os.path.exists(o) and os.path.getmtime(o) >= os.path.getmtime(p): return o
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', p, '-c:v', 'copy', '-c:a', 'aac', '-b:a', '256k', '-ar', '48000', '-ac', '2', o], check=True)
    return o

def dur(p):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p], capture_output=True, text=True).stdout)

def monta(final='Storia_arte_Lez18_Parte1_1080p.mp4', crf=19, solo_elenco=False):
    S = sequenza(); kore.FADE.update(colori(S))
    sa, sf = prepara_sigle()
    files = []; tl = []; t = 0.0
    for n, ty, fn in S:
        p = sa if n == 'sigla' else sf if n == 'sigla_fin' else fn()
        if n.startswith('prof_'): p = stereo(p)
        files.append(p); d = dur(p); tl.append((n, round(t, 3), round(d, 3))); t += d
    json.dump(tl, open(R + 'timeline_scene.json', 'w'), indent=1)
    if solo_elenco: return tl
    lst = R + 'b/lista_finale.txt'
    open(lst, 'w').write(''.join(f"file '{f}'\n" for f in files))
    out = R + final
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-vf', 'format=yuv420p', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709',
                    '-c:v', 'libx264', '-preset', 'veryfast', '-crf', str(crf), '-r', '30', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-movflags', '+faststart', out], check=True)
    return tl

if __name__ == '__main__':
    tl = monta(solo_elenco='--elenco' in sys.argv)
    print(tl[-1], sum(x[2] for x in tl))
