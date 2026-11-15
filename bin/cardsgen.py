# schede Quiz / Verifica / Compiti con bande blu sopra e sotto -> D/cards/*.png e mp4 statici
import sys, json, os, subprocess, importlib.util
sys.path.insert(0, '/home/claude/w/bin')
S = '/tmp/claude-0/-home-user-Lezioni/aa838b16-be86-588f-84fd-78776ad6250d/scratchpad/lez4'
spec = importlib.util.spec_from_file_location('carte4', S + '/carte.py'); cm = importlib.util.module_from_spec(spec); spec.loader.exec_module(cm)
from conf import CONF
import openpyxl
NN = sys.argv[1]; C = CONF[NN]; D = f'/home/claude/w/l{NN}/'; os.makedirs(D + 'cards', exist_ok=True)
nq = len([r for r in openpyxl.load_workbook(f'/home/claude/w/comune/Excel prova finale LETTERATURA ITALIANA V/DOMANDE LEZIONE {C["N"]}.xlsx').active.iter_rows(min_row=2,values_only=True) if r and r[0]])
nc = int(sys.argv[2]) if len(sys.argv) > 2 else 4
num = {4: 'Quattro', 3: 'Tre', 5: 'Cinque', 2: 'Due', 6: 'Sei'}.get(nc, str(nc))
P = {}
for i, A in enumerate(C['arg'], 1):
    P[f'Q{i}'] = cm.card('QUIZ', A['t'], "Rispondi alle domande sull'argomento appena visto.", "5 domande · per continuare almeno l'80%")
P['VER'] = cm.card('VERIFICA FINALE', C['titolo'], f'{nq} domande su tutta la lezione.', f"{nq} domande · per continuare almeno l'80%")
P['CI1'] = cm.card('COMPITI', 'I compiti della lezione', 'Rispondi e premi «Consegna».')
P['COMP'] = cm.card('COMPITI', C['titolo'], f'{num} domande aperte sulla lezione.', 'Rispondi e premi «Consegna»')
from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    b = pw.chromium.launch(); pg = b.new_page(viewport={'width': 1920, 'height': 1080})
    for k, h in P.items():
        pg.set_content(h); pg.wait_for_timeout(150); pg.screenshot(path=f'{D}cards/{k}.png')
    b.close()
for k in P:
    d = 4.0 if k.startswith('Q') or k == 'CI1' else 5.0
    o = f'{D}cards/{k}.mp4'
    if not os.path.exists(o):
        subprocess.run(['ffmpeg', '-y', '-v', 'error', '-loop', '1', '-framerate', '30', '-i', f'{D}cards/{k}.png', '-t', str(d), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-r', '30', o], check=True)
print('schede', len(P), 'domande test', nq, 'compiti', nc)
