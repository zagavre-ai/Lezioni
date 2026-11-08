# Blocchi di testo dalla dispensa d'Inglese (formato Fontanesi): paragrafi ed elenchi, con grassetti e pagina.
# Scrive blocks.json (come Tecnologie) e heads.json: titoli di argomento (h1) e di sezione (h2) con l'indice del primo blocco.
import json, re
P = json.load(open('pdf_lines.json'))
B = []; H = []; cur = None; last_top = None
def flush():
    global cur
    if cur and ''.join(t for _, t in cur['runs']).strip(): B.append(cur)
    cur = None
def add(runs, kind, pg):
    global cur
    if cur is None: cur = {'t': kind, 'runs': [], 'pg': pg}
    for b, t in runs:
        if cur['runs'] and cur['runs'][-1][0] == b: cur['runs'][-1][1] += t
        else: cur['runs'].append([b, t])
for pg, L in enumerate(P, 1):
    if pg == 1: continue                      # copertina
    last_top = None
    for l in L:
        s = ''.join(t for _, t in l['runs']).strip()
        if l['size'] < 10 or not s or s == '.': continue          # intestazione, piè di pagina
        if l['size'] >= 20:                                        # «1: Economic systems»
            flush(); last_top = None
            if not (H and H[-1][1] == 'h1' and H[-1][2] == s): H.append([len(B), 'h1', s])
            continue
        allb = all(b for b, t in l['runs'] if t.strip())
        if (allb and l['size'] >= 11.5 and len(s) < 70) or re.match(r'^\d\. (Introduzione|Analisi)', s):   # «1.1 FREE MARKET ECONOMY»
            flush(); H.append([len(B), 'h2', s]); last_top = None; continue
        bullet = s[:1] in '•●▪-' or re.match(r'^\d+(\.\d+)?\.?\s{1,4}\S', s)
        gap = (l['top'] - last_top) if last_top is not None else 99
        runs = [[b, t] for b, t in l['runs']]
        if bullet:
            flush(); runs[0][1] = re.sub(r'^\s*[•●▪-]\s*', '', runs[0][1]); add(runs, 'li', pg)
        elif cur is not None and gap < 23:
            if cur['runs'] and not cur['runs'][-1][1].endswith((' ', '-')): runs[0][1] = ' ' + runs[0][1].lstrip()
            add(runs, cur['t'], pg)
        else:
            flush(); add(runs, 'p', pg)
        last_top = l['top']
flush()
for b in B:
    for r in b['runs']: r[1] = re.sub(r'\s+', ' ', r[1])
    b['runs'][0][1] = b['runs'][0][1].lstrip(); b['runs'][-1][1] = b['runs'][-1][1].rstrip()
json.dump(B, open('blocks.json', 'w'), ensure_ascii=False); json.dump(H, open('heads.json', 'w'), ensure_ascii=False)
for i, b in enumerate(B):
    hs = [h for h in H if h[0] == i]
    for h in hs: print('   ' * (h[1] == 'h2') + '## ' + h[2])
    print('%3d %s p%d %s' % (i, b['t'], b['pg'], ''.join(t for _, t in b['runs'])[:110]))
