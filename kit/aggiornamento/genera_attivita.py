# Attività per alunno e giorno, da mostrare nel calendario del registro dei compiti.
import json, re, datetime as dt, sys
src = open('crea_report.py').read().split('# ---------- stile ----------')[0]
ns = {}; exec(src, ns)
REP, S, materia, data_log, data_tab, Q, norm = ns['REP'], ns['S'], ns['materia'], ns['data_log'], ns['data_tab'], ns['Q'], ns['norm']
RP = json.load(open('registri_piattaforma.json'))
INI = dt.datetime(2026, 9, 1)
src2 = open('registri_piatt.py').read().split('rows.sort')[0].replace('INI=dt.datetime(2026,10,1)', 'INI=dt.datetime(2026,9,1)').replace('FIN=dt.datetime(2026,11,12,23,59)', 'FIN=dt.datetime.now()')
n2 = {}; exec(src2, n2)
OUT = {}
def add(nome, d, it):
    if not d or d < INI: return
    OUT.setdefault(nome, {}).setdefault(d.date().isoformat(), []).append(it)
uid_of = {str(iuc): u for u, l in S['IUC'].items() for _, iuc in l}
for iuc, rows in REP.items():
    u = uid_of.get(iuc)
    if not u or u in ('50', '312'): continue
    nome = S['STUD'][u]['nome']
    info = {r[0]: (r[1] if len(r) > 1 else '') for r in rows[:8] if r}
    corso = info.get('Corso', '').strip()
    if re.search(r'DIRETTA|LIVE', corso, re.I): continue
    fam = materia(corso)
    lez, i = [], 9
    while i < len(rows) and len(rows[i]) >= 9 and re.match(r'^\d+$', str(rows[i][0])): lez.append(rows[i]); i += 1
    log = {}; cur = None
    for r in rows[i:]:
        if r and str(r[0]).startswith('Lezione ID:'):
            m = re.match(r'Lezione ID: (\d+)', r[0]); cur = m.group(1) if m else None; log[cur] = []
        elif cur and len(r) >= 3 and r[0] != 'Attività': log[cur].append(r)
    for l in lez:
        ev = log.get(str(l[0]), [])
        giorni = sorted({x.date() for x in (data_log(e[2]) for e in ev) if x})
        anni = {(x.day, x.month): x.year for x in (data_log(e[2]) for e in ev) if x}
        comp = data_tab(l[8], anni); pv = data_tab(l[6], anni)
        if pv and pv.date() not in giorni: giorni.append(pv.date())
        if comp and comp.date() not in giorni: giorni.append(comp.date())
        pun = l[5] if l[3] == 'SI' and l[5] not in ('-', '') else ''
        for g in sorted(set(giorni)):
            gd = dt.datetime.combine(g, dt.time(12))
            if comp and comp.date() == g: s = 'C'
            elif comp and comp.date() > g: s = 'A'
            else: s = 'I'
            add(nome, gd, {'k': 'v', 'f': fam, 'c': corso, 't': l[1], 's': s, 'p': pun if s == 'C' else '', 'cd': comp.date().isoformat() if comp else ''})
# lezioni in diretta (registro della piattaforma)
for r in n2['rows']:
    for u in r['al']:
        add(S['STUD'][u]['nome'], r['d'], {'k': 'l', 'f': materia(r['mat']), 't': r['tit'], 'doc': r['doc'], 'arg': r['arg'], 'fb': r['fb'], 'voto': r['voto'], 'ass': r['assente']})
# compiti del quaderno
nomi = {frozenset(norm(v['nome'])): v['nome'] for k, v in S['STUD'].items()}
def chi(a):
    k = set(norm(a))
    for kk, n in nomi.items():
        if kk <= k or k <= kk: return n
for c in Q:
    n = chi(c['a'])
    if not n or c.get('st'): continue
    f = materia(c['m']); base = {'k': 'q', 'f': f, 't': c['t'], 'l': c['l'], 'doc': c.get('doc') or ''}
    a = dt.datetime.fromisoformat(c['ass'][:19])
    add(n, a, {**base, 'e': 'assegnato', 'sc': c.get('sc') or ''})
    for e in c.get('ev') or []:
        d = dt.datetime.fromisoformat(e['il'][:19])
        if e['t'] == 'consegna': add(n, d, {**base, 'e': 'consegnato'})
        elif e['t'] == 'correzione': add(n, d, {**base, 'e': 'corretto', 'v': e.get('v') or ''})
        elif e['t'] == 'da_rifare': add(n, d, {**base, 'e': 'da rifare'})
from zoneinfo import ZoneInfo
json.dump({'letto': dt.datetime.now(ZoneInfo('Europe/Rome')).strftime('%d/%m/%Y %H:%M'), 'alunni': OUT}, open('attivita_registro.json', 'w'), ensure_ascii=False)
tot = sum(len(v) for a in OUT.values() for v in a.values())
print(len(OUT), 'alunni', tot, 'attività')
