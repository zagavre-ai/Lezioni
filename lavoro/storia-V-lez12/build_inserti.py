import sys, os, time
sys.path.insert(0, '/home/user/Lezioni/lavoro/storia-V-lez12')
import inserti as I, montaggio as M, voce, contenuti as C
OUT = M.OUT
def fatto(n): return os.path.exists(f'{OUT}/{n}/v.mp4') and os.path.exists(f'{OUT}/{n}/ok')
def run(n, f, *a):
    if fatto(n) and '--forza' not in sys.argv: return
    t = time.time(); f(*a); open(f'{OUT}/{n}/ok', 'w').write('ok'); print(n, round(time.time() - t), flush=True)
KIT = M.KIT
run('sigla', I.pezzo_da_file, 'sigla', f'{KIT}/sigle/Sigla_Storia_15s.mp4')
run('sigla_fin', I.pezzo_da_file, 'sigla_fin', f'{KIT}/sigle/Sigla_finale_5s_con_avviso_diritti.mp4')
run('cover_ben', I.cover_benvenuto); run('cover_ben2', I.cover_benvenuto2); run('spiegone', I.spiegone); run('argomenti', I.argomenti_scheda)
IMG = {3: 'asia', 4: 'spagna', 6: 'europa'}
for k in range(1, 7):
    run(f'tit{k}', I.titolo, k)
    run(f'app{k}', I.approfondimento, k, IMG.get(k))
    if k in (2, 4, 6): run(f'mappa{k}', I.mappa, k)
    run(f'pil{k}', I.pillola, k); run(f'quiz{k}', I.quiz, k)
run('glossario', I.glossario); run('ripasso', I.ripasso_finale); run('mappe_fin', I.mappe_finale)
run('verifica', I.verifica); run('compiti_intro', I.compiti_intro); run('compiti', I.compiti)
