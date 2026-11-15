import sys, re, json, subprocess
NN = sys.argv[1]; N = int(NN); D = f'/home/claude/w/l{NN}/'
pdf = '/tmp/claude-0/-home-user-Lezioni/aa838b16-be86-588f-84fd-78776ad6250d/scratchpad/rel/compiti/LETTERATURA ITALIANA V /LEZIONE %d.pdf' % N
txt = subprocess.run(['pdftotext', '-layout', pdf, '-'], capture_output=True, text=True).stdout
qs = [re.sub(r'\s+', ' ', x).strip() for x in re.split(r'\n\s*\d\)\s', '\n' + txt.split('LEZIONE %d' % N, 1)[1])[1:]]
sys.path.insert(0, '/home/claude/w/bin'); from conf import CONF
json.dump({'titolo': 'Compiti · ' + CONF[NN]['titolo'], 'stato': f'compiti del prof. Mazzotti (file «LEZIONE {N}.pdf», release mazzotti-letteratura-V)',
           'esercizi': [{'n': i + 1, 'tipo': 'aperta', 'testo': q} for i, q in enumerate(qs)]}, open(D + 'out/compiti.json', 'w'), ensure_ascii=False, indent=1)
print('compiti', len(qs))
