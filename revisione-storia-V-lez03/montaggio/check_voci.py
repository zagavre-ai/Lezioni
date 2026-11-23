import sys, json, re, subprocess, os, difflib
import numpy as np
sys.path.insert(0, '/home/user/w3/build')
import data as D
T = {x['nome']: x['testo'] for x in json.load(open('/home/user/w3/voci/scambio/storia-V-lez03/testi_voci.json'))}
NEW = [n for n in T if n.startswith(('BEN_R2', 'SPG_0', 'DIC_', 'MP1_', 'MP2_', 'MP3_', 'CMP_1'))]
def norm(s): return re.findall(r"[a-z0-9àèéìòù]+", D.digits(s).lower().replace("'", " "))
rows = []
for n in NEW:
    p = f'/home/user/w3/vox_new/{n}.wav'
    if not os.path.exists(p): rows.append((n, 'MANCA')); continue
    x = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-ac', '1', '-ar', '48000', '-f', 'f32le', '-'], capture_output=True).stdout, np.float32)
    subprocess.run(['python3', '/home/user/w3/build/asr_batch.py', '/home/user/w3/asr_new', p], capture_output=True)
    j = json.load(open(f'/home/user/w3/asr_new/{n}.json')); a = norm(T[n]); b = norm(j['testo'])
    r = difflib.SequenceMatcher(None, a, b).ratio()
    miss = [w for w in a if w not in b][:6]
    e0 = float(np.abs(x[:2400]).max()); e1 = float(np.abs(x[-2400:]).max())
    rows.append((n, f'{len(x)/48000:.1f}s', f'conf {r:.2f}', f'bordi ini {e0:.3f} fine {e1:.3f}', 'ok' if r > .9 and e1 < .03 and e0 < .03 else 'DA CONTROLLARE', miss))
for r in rows: print(*r)
