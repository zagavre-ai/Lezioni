# Prepara la cartella di consegna e la pubblica sul ramo revisione-storia-arte-V-lez06
import sys, os, json, subprocess, shutil, hashlib, glob
sys.path.insert(0, '/tmp/w/build')
V = sys.argv[1]                       # video finale
NOME = 'Storia_arte_V_Lez6_Parte1_1080p.mp4'
TAG = 'storia-arte-V-lez06'; BR = 'revisione-' + TAG
D = f'/tmp/w/build/consegna/{TAG}'; shutil.rmtree(D, ignore_errors=True); os.makedirs(D)
sh = lambda c: subprocess.run(c, check=True, capture_output=True, text=True)
C = '/tmp/w/build/consegna'
# video a pezzi da 90 MB + sha256
vp = f'{D}/{NOME}'; shutil.copy(V, vp)
h = hashlib.sha256(open(vp, 'rb').read()).hexdigest(); open(vp + '.sha256', 'w').write(f'{h}  {NOME}\n')
sh(['split', '-b', '90M', '-d', '-a', '2', vp, vp + '.parte_']); os.remove(vp)
TL = V.replace('.mp4', '_timeline.json'); shutil.copy(TL, f'{D}/timeline_Parte1.json')
Q = f'{C}/quiz_argomenti.json'; shutil.copy(Q, f'{D}/quiz_argomenti.json')
for f in ('verifica_finale.json', 'compiti.json'): shutil.copy(f'{C}/{f}', f'{D}/{f}')
vtt = V.replace('.mp4', '.vtt')
if os.path.exists(vtt): shutil.copy(vtt, f'{D}/Storia_arte_V_Lez6_Parte1.vtt')
for f in glob.glob(f'{C}/*.pdf'): shutil.copy(f, D)
for f in glob.glob('/tmp/w/build/cr/*'): shutil.copy(f, D)
# scheda di pubblicazione
sh(['python3', '/home/user/Lezioni/kit/tools/scheda_da_timeline.py', V, f'{D}/timeline_Parte1.json', Q, "Storia dell'arte V · Lezione 6 · Simbolismo e Art Nouveau", f'{D}/scheda_pubblicazione_Parte1.json', "Storia dell'Arte V"])
S = json.load(open(f'{D}/scheda_pubblicazione_Parte1.json')); T = {n: t for n, t, l in json.load(open(TL))}
S['t_verifica'] = T['VER']; S['t_compiti'] = T['CI']; S['verifica'] = json.load(open(f'{C}/verifica_finale.json'))
json.dump(S, open(f'{D}/scheda_pubblicazione_Parte1.json', 'w'), ensure_ascii=False, indent=1)
for f in ('RAPPORTO_REVISIONE.md',):
    if os.path.exists(f'{C}/{f}'): shutil.copy(f'{C}/{f}', D)
print(os.listdir(D))
