# Copertine con titolo su una riga (lez 17): stessa posizione del titolo, card ARGOMENTI sotto senza sovrapposizione. Il pezzo cover tiene i primi 3 s con l'avviso diritti (strisce prese dalla consegna).
import sys, os, json, subprocess
sys.path.insert(0, '/tmp/claude-0/l17'); os.environ['PLAYWRIGHT_BROWSERS_PATH'] = '/opt/pw-browsers'
import slides as SL
from dati import PARTI
from PIL import Image
WK = '/home/user/w/l17/work'; os.makedirs(f'{WK}/clips', exist_ok=True)
for P in (1, 2, 3):
    tl = json.load(open(f'/home/user/w/b17/timeline_Parte{P}.json')); st = dict(tl); names = [n for n, _ in tl]
    i = names.index('cover'); N = round((tl[i + 1][1] - tl[i][1]) * 30) + 12
    SL.render([(f'cover_np_P{P}', SL.html_cover(1, False, PARTI[P], P if P > 1 else None))], f'{WK}/slpng')
    plain = f'{WK}/slpng/cover_np_P{P}.png'
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', f'{st["cover"] + 0.9:.2f}', '-i', f'/home/user/w/l17/old/Parte{P}.mp4', '-frames:v', '1', f'{WK}/slpng/oldn{P}.png'], check=True)
    new = Image.open(plain).convert('RGB'); old = Image.open(f'{WK}/slpng/oldn{P}.png').convert('RGB')
    new.paste(old.crop((150, 850, 1770, 975)), (150, 850)); new.save(f'{WK}/slpng/cover_notice_P{P}.png')
    for nm, png, fr in (('a', f'{WK}/slpng/cover_notice_P{P}.png', 90), ('b', plain, N - 90)):
        subprocess.run(['ffmpeg', '-y', '-v', 'error', '-loop', '1', '-framerate', '30', '-i', png, '-frames:v', str(fr), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '14', '-pix_fmt', 'yuv420p', '-g', '30', '-r', '30', '-an', f'{WK}/clips/c{P}{nm}.mp4'], check=True)
    open(f'{WK}/clips/c{P}.txt', 'w').write(f"file '{WK}/clips/c{P}a.mp4'\nfile '{WK}/clips/c{P}b.mp4'\n")
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', f'{WK}/clips/c{P}.txt', '-c', 'copy', f'{WK}/clips/cover{P}.mp4'], check=True)
    print('cover', P, N)
