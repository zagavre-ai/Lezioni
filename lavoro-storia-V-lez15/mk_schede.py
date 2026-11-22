# Schede blu animate (titoli, pillole, quiz, riepilogo, verifica, compiti) con lo strumento delle schede di Spagnolo.
import sys, os, json, subprocess
sys.path.insert(0, '/tmp/claude-0/l15')
from dati import *
from extra import split_caps, vdur
import schede_fast as SF
W = '/tmp/claude-0/l15'
os.makedirs(W + '/sch', exist_ok=True)
T = {v['nome']: v['testo'] for v in json.load(open(W + '/voci_testi_nuovi.json'))}
def tfsz(t): return 84 if len(t) <= 30 else max(52, int(84 * 30 / len(t)))
specs = {}
for pos, n in enumerate(GLOBAL_ORDER, 1):
    a = ARG[n - 1]; L = RIGHE[n]; m = max(len(x) for x in L); fs = min(128, int(128 * 20 / m))
    specs[f'T{pos}'] = {"type": "title", "num": f"{pos:02d}", "total": len(GLOBAL_ORDER), "lines": L, "ex": a['chip'], "fs": fs, "lineY": 720, "dur": 4}
    specs[f'Q{pos}'] = {"type": "quiz", "act": f"Quiz {pos}", "topic": a['nome'], "tfs": tfsz(a['nome']), "pts": "5 domande · per continuare almeno l'80%", "dur": 5}
    d = vdur(f'PI{n}'); caps = split_caps(T[f'PI{n}'], d)
    specs[f'R{pos}'] = {"type": "repaso", "kicker": "Pillola di storia", "big": "RIPASSO", "topic": a['nome'], "tfs": tfsz(a['nome']), "caps": caps, "dur": round(caps[-1][1] + 1.2, 1)}
d = vdur('FIN')
specs['F'] = {"type": "final", "kicker": "Storia V", "l1": "RIEPILOGO", "l2": "FINALE", "items": [[ARG[n - 1]['nome'], ""] for n in GLOBAL_ORDER], "sub": "Ripassiamo insieme ciò che abbiamo imparato.", "dur": round(d + 1.7 + 0.8, 1)}
specs['V'] = {"type": "quiz", "act": "Verifica", "topic": "Verifica finale", "tfs": 84, "pts": "10 domande · per continuare almeno l'80%", "dur": 5}
specs['C'] = {"type": "repaso", "kicker": "Dopo la lezione", "big": "COMPITI", "topic": "Per esercitarti a casa", "tfs": 84, "caps": [], "dur": 3.5}
if __name__ == '__main__':
    todo = sys.argv[1:] or list(specs)
    for k in todo:
        out = f'{W}/sch/{k}'
        if os.path.exists(out + '.mp4'): continue
        SF.render(specs[k], out, 1.0)
        import shutil; shutil.rmtree(out, ignore_errors=True); print('scheda', k, flush=True)
