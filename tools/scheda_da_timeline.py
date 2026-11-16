# Scheda di pubblicazione da timeline + quiz_argomenti; durata MISURATA sul file finale.
# uso: python3 scheda_da_timeline.py video.mp4 timeline.json quiz_argomenti.json "Titolo · Parte N" uscita.json ["Materia"]
import sys, json, subprocess
V, TL, QZ, TIT, OUT = sys.argv[1:6]
dur = float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',V],capture_output=True,text=True).stdout)
T = json.load(open(TL)); Q = json.load(open(QZ)); st = {n: t for n, t, l in T}
arg = []; quiz = {}
for n, t, l in T:
    if n.startswith('T') and n[1:].isdigit():
        k = int(n[1:]); q = 'Q%d' % k
        arg.append({'n': k, 'titolo': Q[q]['title'].split(' · ', 1)[1], 'inizio_s': round(t, 3), 'quiz_s': round(st[q], 3)})
        quiz[q] = Q[q]
json.dump({'materia': (sys.argv[6] if len(sys.argv) > 6 else ''), 'titolo': TIT, 'durata_s': round(dur, 2), 'argomenti': arg, 'quiz': quiz}, open(OUT, 'w'), ensure_ascii=False, indent=1)
print(OUT, round(dur, 2), [(a['n'], a['titolo'], a['inizio_s'], a['quiz_s']) for a in arg])
