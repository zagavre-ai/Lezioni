#!/usr/bin/env python3
"""Prepara la cartella di consegna di una Parte (dopo la codifica finale).
uso: python3 consegna_s1.py spec.py lavoro_dir PARTE LEZ_NUM uscita_dir excel_test.xlsx compiti.pdf
Scrive: quiz .txt/.json, compiti.json, test .xlsx, scheda_pubblicazione, testo YouTube, LEGGIMI, video a pezzi da 90 MB + sha256."""
import sys, os, json, re, shutil, subprocess, hashlib, importlib.util
sp = importlib.util.spec_from_file_location('spec', sys.argv[1])
S = importlib.util.module_from_spec(sp)
sp.loader.exec_module(S)
W, PARTE, NUM, OUT, XLS, CPDF = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5], sys.argv[6], sys.argv[7]
os.makedirs(OUT, exist_ok=True)
TOOLS = '/home/user/Lezioni/kit/tools'
VID = '%s/Storia_Lez%d_Parte%d_1080p.mp4' % (W, NUM, PARTE)
PART = [p for p in S.PARTI if p['n'] == PARTE][0]
quiz = json.load(open(W + '/quiz.json'))
# quiz .txt completo (tutti gli argomenti, una volta sola) e .json
lines = ['QUIZ DI ARGOMENTO · Storia · %s' % S.TITOLO, 'STATO: da approvare dalla master (regola del 13/11)', '']
for k in sorted(quiz, key=lambda x: int(x[1:])):
    q = quiz[k]
    lines.append('== Argomento %s · %s ==' % (k[1:], q['title'].split(' · ', 1)[1]))
    for i, it in enumerate(q['items'], 1):
        opts = [it['a']] + it['w']
        lines.append('%d. %s' % (i, it['p']))
        for lab, o in zip('ABCD', opts):
            lines.append('   %s) %s%s' % (lab, o, '  <-- giusta' if o == it['a'] else ''))
        lines.append('   Spiegazione: %s' % it['e'])
    lines.append('')
open('%s/Quiz_Storia_Lez%d.txt' % (OUT, NUM), 'w').write('\n'.join(lines))
shutil.copy(W + '/quiz.json', '%s/quiz_argomenti.json' % OUT)
# compiti
t = subprocess.run(['pdftotext', '-layout', CPDF, '-'], capture_output=True, text=True).stdout
items = [re.sub(r'\s+', ' ', x).strip() for x in re.split(r'\n\s*(?=\d\)\s)', t) if re.match(r'\s*\d\)', x)]
items = [re.sub(r'^\d\)\s*', '', x) for x in items]
json.dump({'lezione': S.TITOLO, 'docente': 'Prof. Giorgio Mazzotti', 'domande_aperte': items}, open('%s/compiti.json' % OUT, 'w'), ensure_ascii=False, indent=1)
shutil.copy(XLS, '%s/Storia_Lez%d_test_finale_docente.xlsx' % (OUT, NUM))
shutil.copy(CPDF, '%s/Storia_Lez%d_compiti_docente.pdf' % (OUT, NUM))
for f in ['Storia_Lez%d_dispensa.pdf' % NUM]:
    if os.path.exists(W + '/' + f):
        shutil.copy(W + '/' + f, OUT + '/' + f)
# sottotitoli, timeline
for f in ['Storia_Lez%d_Parte%d.vtt' % (NUM, PARTE)]:
    shutil.copy(W + '/' + f, OUT + '/' + f)
shutil.copy('%s/timeline_Parte%d.json' % (W, PARTE), '%s/timeline_Parte%d.json' % (OUT, PARTE))
# scheda + testo YouTube
sch = '%s/scheda_pubblicazione_Parte%d.json' % (OUT, PARTE)
tit = '%s · Parte %d' % (S.TITOLO, PARTE)
subprocess.run([sys.executable, TOOLS + '/scheda_da_timeline.py', VID, '%s/timeline_Parte%d.json' % (W, PARTE), W + '/quiz.json', tit, sch, 'Storia'], check=True)
yt = subprocess.run([sys.executable, TOOLS + '/testo_youtube.py', sch, 'Storia', 'Prof. Giorgio Mazzotti', 'Lezione %d · %s' % (NUM, S.TITOLO), str(PARTE), '%s/timeline_Parte%d.json' % (W, PARTE)], capture_output=True, text=True)
open('%s/testo_youtube_Parte%d.txt' % (OUT, PARTE), 'w').write(yt.stdout)
# video a pezzi da 90 MB
base = os.path.basename(VID)
sha = hashlib.sha256()
with open(VID, 'rb') as f, open('%s/%s.sha256' % (OUT, base), 'w') as o:
    k = 0
    while True:
        b = f.read(90 * 1024 * 1024)
        if not b:
            break
        sha.update(b)
        open('%s/%s.parte_%02d' % (OUT, base, k), 'wb').write(b)
        k += 1
    full = hashlib.sha256()
    with open(VID, 'rb') as g:
        for blk in iter(lambda: g.read(1 << 20), b''):
            full.update(blk)
    o.write('%s  %s\n' % (full.hexdigest(), base))
open('%s/LEGGIMI_Parte%d.txt' % (OUT, PARTE), 'w').write(
    'Storia V · Lezione %d · %s · consegna Parte %d.\nVideo a pezzi da 90 MB: riunisci con  cat %s.parte_* > %s  e controlla con il file .sha256.\n'
    'Test finale: Excel del docente. Compiti: PDF del docente e compiti.json. Quiz: tutti gli argomenti in Quiz_Storia_Lez%d.txt.\n' % (NUM, S.TITOLO, PARTE, base, base, NUM))
print('consegna', OUT, os.listdir(OUT))
