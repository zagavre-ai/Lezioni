# Report dal 1/9/2026 a oggi: un Excel per alunno + quadro generale.
# Dati (privati, mai nel repository): stud_iuc.json (alunni e iscrizioni), report.json (report attività della piattaforma), quaderno.json (compiti).
import json, re, os, sys, datetime as dt, unicodedata
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

P = '/root/report_privato/'
INIZIO = dt.datetime(2026, 9, 1)  # decisione di Sara 11/11: solo il 2026, da settembre
OGGI = dt.datetime.now()
OGGI_TXT = OGGI.strftime('%d/%m/%Y')
ESCLUSI = {'50', '312'}  # account di prova e direzione
MESI = {m: i for i, m in enumerate(['gennaio', 'febbraio', 'marzo', 'aprile', 'maggio', 'giugno', 'luglio', 'agosto', 'settembre', 'ottobre', 'novembre', 'dicembre'], 1)}

S = json.load(open(P + 'stud_iuc.json'))
STUD, IUC = S['STUD'], S['IUC']
REP = json.load(open(P + 'report.json'))
Q = json.load(open(P + 'quaderno.json'))
RV = json.load(open(P + 'registri_voci.json'))  # registri PDF dei prof (inseriti nel registro online l'11/11)

def norm(s):
    s = unicodedata.normalize('NFD', s or '').encode('ascii', 'ignore').decode().upper()
    return re.sub(r'[^A-Z ]', ' ', s).split()

def data_log(s):  # "Mar, 06 Ottobre 2026, ore 17:15:41"
    m = re.search(r'(\d{1,2}) (\w+) (\d{4}), ore (\d{2}):(\d{2})', s or '')
    if not m or m.group(2).lower() not in MESI: return None
    return dt.datetime(int(m.group(3)), MESI[m.group(2).lower()], int(m.group(1)), int(m.group(4)), int(m.group(5)))

def data_tab(s, anni):  # "Mar, 06 Ottobre, ore 17:15:41" + anni noti dal registro della lezione
    m = re.search(r'(\d{1,2}) (\w+), ore (\d{2}):(\d{2})', s or '')
    if not m or m.group(2).lower() not in MESI: return None
    g, me = int(m.group(1)), MESI[m.group(2).lower()]
    y = anni.get((g, me))
    if y is None:  # senza registro: l'anno più recente che non supera oggi
        y = OGGI.year if dt.datetime(OGGI.year, me, g) <= OGGI else OGGI.year - 1
    return dt.datetime(y, me, g, int(m.group(3)), int(m.group(4)))

FAM = [(r'STORIA DELL.ARTE|ARTE E IMMAGINE|ARTE E TERRITORIO', 'Storia dell\'arte'), (r'ITALIAN|LETTERATURA', 'Italiano'), (r'INGLES', 'Inglese'),
       (r'FRANCES', 'Francese'), (r'SPAGNOL', 'Spagnolo'), (r'TEDESC', 'Tedesco'), (r'LATIN', 'Latino'), (r'^STORIA|STORIA ', 'Storia'),
       (r'DIRITTO', 'Diritto ed economia'), (r'SCIENZE UMANE|PSICOLOG', 'Scienze umane'), (r'MATEMATICA', 'Matematica'), (r'GEOGRAF', 'Geografia'),
       (r'FILOSOF', 'Filosofia'), (r'FISICA', 'Fisica'), (r'CHIMIC', 'Chimica'), (r'INFORMATIC', 'Informatica'), (r'ECONOMIA AZIENDALE', 'Economia aziendale'),
       (r'SCIENZE', 'Scienze')]
LINGUE = [(r'INGLES', 'Inglese'), (r'FRANCES', 'Francese'), (r'SPAGNOL', 'Spagnolo'), (r'TEDESC', 'Tedesco'), (r'LATIN', 'Latino'), (r'MOTORI', 'Scienze motorie')]
def materia(nome):
    n = (nome or '').upper()
    for r, f in LINGUE:  # le lingue prima: «LINGUA E LETTERATURA INGLESE» è Inglese
        if re.search(r, n): return f
    best = None
    for i, (r, f) in enumerate(FAM):  # altrimenti la materia nominata per prima («LEZIONI LIVE - MATEMATICA - …»)
        m = re.search(r, n)
        if m and (best is None or (m.start(), i) < best[0]): best = ((m.start(), i), f)
    return best[1] if best else (nome or '').strip().title()[:40]

def leggi_report(rows):
    info = {r[0]: (r[1] if len(r) > 1 else '') for r in rows[:8] if r}
    lez, i = [], 9
    while i < len(rows) and len(rows[i]) >= 9 and re.match(r'^\d+$', str(rows[i][0])):
        lez.append(rows[i]); i += 1
    log = {}; cur = None
    for r in rows[i:]:
        if r and str(r[0]).startswith('Lezione ID:'):
            m = re.match(r'Lezione ID: (\d+)', r[0]); cur = m.group(1) if m else None; log[cur] = []
        elif cur and len(r) >= 3 and r[0] != 'Attività':
            log[cur].append((r[0], r[1], r[2]))
    out = []
    for l in lez:
        lid = str(l[0]); ev = log.get(lid, [])
        anni = {}
        for _, _, d in ev:
            x = data_log(d)
            if x: anni[(x.day, x.month)] = x.year
        pv, ul, comp = data_tab(l[6], anni), data_tab(l[7], anni), data_tab(l[8], anni)
        sessioni = sum(1 for a, _, _ in ev if a.startswith('Inizio visualizzazione'))
        out.append(dict(id=lid, tit=l[1], fr=l[2], test=l[3], tent=l[4], pun=l[5], pv=pv, ul=ul, comp=comp, ses=sessioni))
    return dict(corso=info.get('Corso', ''), cid=info.get('ID Corso', ''), durata=info.get('Durata del corso', ''), lez=out)

# ---------- compiti del quaderno per alunno ----------
def stato_compito(c):
    ev = c.get('ev') or []
    cons = [e for e in ev if e['t'] == 'consegna']; corr = [e for e in ev if e['t'] in ('correzione', 'da_rifare')]
    ver = [e for e in ev if e['t'] in ('verifica', 'segnalazione')]
    if c.get('st') and not ev: s = 'Storico (non assegnato agli alunni)'
    elif corr and (not cons or corr[-1]['il'] >= cons[-1]['il']):
        s = 'Da rifare' if corr[-1]['t'] == 'da_rifare' else ('Verificato' if ver and ver[-1]['t'] == 'verifica' else 'Corretto')
    elif cons: s = 'Consegnato, da correggere'
    else: s = 'Da consegnare'
    voto = next((e['v'] for e in reversed(corr) if e['t'] == 'correzione' and e.get('v')), None)
    return s, (cons[-1]['il'][:10] if cons else ''), (corr[-1]['il'][:10] if corr else ''), voto

QA = {}
for c in Q:
    if c['a'].upper().startswith('ALUNNO DI PROVA'): continue
    QA.setdefault(frozenset(norm(c['a'])), []).append(c)
def registro_di(nome):
    k = set(norm(nome)); out = []
    for v in RV:
        kk = set(norm(v['stud']))
        if kk <= k or k <= kk: out.append(v)
    return out
def compiti_di(nome):
    k = set(norm(nome))
    for kk, l in QA.items():
        if kk <= k or k <= kk: return l
    return []

# ---------- stile ----------
A = 'Arial'; NAVY = '0B1530'
H = Font(name=A, bold=True, color='FFFFFF', size=10); HF = PatternFill('solid', fgColor=NAVY)
N = Font(name=A, size=10); B = Font(name=A, size=10, bold=True); T = Font(name=A, size=14, bold=True, color=NAVY); SB = Font(name=A, size=10, italic=True, color='5B6478')
thin = Side(style='thin', color='C9D0DC'); BR = Border(left=thin, right=thin, top=thin, bottom=thin)
COL = {'Completata': 'D9F2E3', 'A metà': 'FFF4C2', 'Corretto': 'D9F2E3', 'Verificato': 'D9F2E3', 'Da rifare': 'FBE0DE', 'Consegnato, da correggere': 'FFF4C2', 'Storico (non assegnato agli alunni)': 'EEF0F4'}
def foglio(wb, nome, titolo, sotto, head, widths):
    ws = wb.create_sheet(nome); ws['A1'] = titolo; ws['A1'].font = T; ws['A2'] = sotto; ws['A2'].font = SB
    for i, h in enumerate(head, 1):
        c = ws.cell(4, i, h); c.font = H; c.fill = HF; c.alignment = Alignment(wrap_text=True, vertical='center'); c.border = BR
    for i, w in enumerate(widths, 1): ws.column_dimensions[get_column_letter(i)].width = w
    ws.row_dimensions[4].height = 32; ws.freeze_panes = 'A5'; return ws
def riga(ws, r, vals, wrap=(), fill=None):
    for i, v in enumerate(vals, 1):
        c = ws.cell(r, i, v); c.font = N; c.border = BR; c.alignment = Alignment(vertical='top', wrap_text=(i in wrap))
        if isinstance(v, dt.datetime): c.number_format = 'DD/MM/YYYY HH:MM'
        if fill and fill.get(i): c.fill = PatternFill('solid', fgColor=fill[i])
f = lambda x: x.strftime('%d/%m/%Y') if x else ''
nel = lambda x: bool(x and INIZIO <= x <= OGGI)
def pct(s):
    m = re.match(r'(\d+)%', str(s or '')); return int(m.group(1)) if m else None

# registro elettronico della piattaforma (Lezioni → Visualizza registro), letto il 12/11
_src = open(P + 'registri_piatt.py').read().split('rows.sort')[0].replace('INI=dt.datetime(2026,10,1)', 'INI=dt.datetime(2026,9,1)').replace('FIN=dt.datetime(2026,11,12,23,59)', 'FIN=dt.datetime.now()')
_ns = {}; exec(_src, _ns)
RP = {}
for _r in sorted(_ns['rows'], key=lambda x: x['d']):
    for _u in _r['al']: RP.setdefault(_u, []).append(_r)
QUADRO = []; MANCANTI = []; SENZA = []
os.makedirs(P + 'finale', exist_ok=True)
for uid, st in STUD.items():
    if uid in ESCLUSI: continue
    nome, ind = st['nome'], st.get('ind', '')
    corsi = []
    for cid, iuc in IUC.get(uid, []):
        rows = REP.get(str(iuc))
        if rows is None: MANCANTI.append((nome, cid, iuc)); continue
        r = leggi_report(rows); r['iuc'] = iuc; r['mat'] = materia(r['corso']); corsi.append(r)
    comp = compiti_di(nome); reg = registro_di(nome); rp = RP.get(uid, [])
    attivi = any(nel(x) for c in corsi for l in c['lez'] for x in (l['pv'], l['ul'], l['comp']))
    if not attivi and not comp and not reg and not rp:
        ultima = max([x for c in corsi for l in c['lez'] for x in (l['ul'], l['comp']) if x] or [None])
        SENZA.append((nome, ind, len(corsi), f(ultima))); continue
    wb = Workbook(); wb.remove(wb.active)
    sotto = f'{nome} · {ind} · periodo dal 01/09/2026 al {OGGI_TXT} · dati della piattaforma e del quaderno dei compiti letti il {OGGI_TXT}'
    # 1. Riepilogo
    ws = foglio(wb, 'Riepilogo', f'Report dal 1° settembre al {OGGI.day} novembre 2026', sotto,
                ['Materia', 'Corso (nome sulla piattaforma)', 'Lezioni aperte nel periodo', 'Completate nel periodo', 'A metà', 'Test superati (media)', 'Ultima attività',
                 'Compiti assegnati', 'Consegnati', 'Corretti', 'Voti', 'Domande delle live (storico)'], [18, 46, 11, 11, 9, 14, 13, 10, 10, 9, 14, 13])
    r = 5; tot = dict(ap=0, co=0, me=0, te=0, pts=[])
    usate = set()
    for c in sorted(corsi, key=lambda x: (x['mat'], x['corso'])):
        L = c['lez']; ap = [l for l in L if nel(l['pv']) or nel(l['ul']) or nel(l['comp'])]
        co = [l for l in L if nel(l['comp'])]; me = [l for l in ap if not l['comp']]
        te = [l for l in co if l['test'] == 'SI' and pct(l['pun']) is not None]; pts = [pct(l['pun']) for l in te]
        ult = max([x for l in L for x in (l['ul'], l['comp']) if x] or [None])
        cm = [x for x in comp if materia(x['m']) == c['mat']] if c['mat'] not in usate else []
        usate.add(c['mat'])
        ass = [x for x in cm if not x.get('st')]; stor = [x for x in cm if x.get('st')]
        S2 = [stato_compito(x) for x in ass]
        voti = [s[3] for s in S2 if s[3]]
        riga(ws, r, [c['mat'], c['corso'], len(ap), len(co), len(me), f"{len(te)} ({round(sum(pts)/len(pts))}%)" if pts else '—', f(ult),
                     len(ass), sum(1 for s in S2 if s[1]), sum(1 for s in S2 if s[0] in ('Corretto', 'Verificato')), ', '.join(voti) or ('senza voto' if S2 else ''), len(stor)], wrap=(2,))
        tot['ap'] += len(ap); tot['co'] += len(co); tot['me'] += len(me); tot['te'] += len(te); tot['pts'] += pts; r += 1
    for m in sorted({materia(x['m']) for x in comp} - usate):  # compiti di materie senza corso registrato
        cm = [x for x in comp if materia(x['m']) == m]; ass = [x for x in cm if not x.get('st')]; S2 = [stato_compito(x) for x in ass]
        riga(ws, r, [m, '(nessun corso con questo nome: compiti delle lezioni in diretta)', '', '', '', '', '', len(ass), sum(1 for s in S2 if s[1]),
                     sum(1 for s in S2 if s[0] in ('Corretto', 'Verificato')), ', '.join(s[3] for s in S2 if s[3]), len(cm) - len(ass)], wrap=(2,)); r += 1
    riga(ws, r, ['TOTALE', '', f'=SUM(C5:C{r-1})', f'=SUM(D5:D{r-1})', f'=SUM(E5:E{r-1})', '', '', f'=SUM(H5:H{r-1})', f'=SUM(I5:I{r-1})', f'=SUM(J5:J{r-1})', '', f'=SUM(L5:L{r-1})'])
    for i in range(1, 13): ws.cell(r, i).font = B
    r += 2
    for t in ['Come si legge',
              '• Lezioni aperte nel periodo: lezioni con almeno una visualizzazione dal 1/9 a oggi.',
              '• Completate: la piattaforma ha registrato la «Data completamento» nel periodo (test superato, se previsto).',
              '• A metà: aperte nel periodo ma non completate.',
              '• Compiti: dal quaderno dei compiti. «Domande delle live (storico)» = domande assegnate nelle lezioni in diretta del prof. Mazzotti, registrate per memoria: non ancora assegnate come compito.',
              '• Le date della tabella lezioni sono complete di anno grazie al registro attività della piattaforma.']:
        ws.cell(r, 1, t).font = B if t == 'Come si legge' else N; r += 1
    # 2. Dettaglio lezioni
    ws = foglio(wb, 'Dettaglio lezioni', 'Lezioni seguite dal 1° settembre a oggi', sotto,
                ['Materia', 'Corso', 'ID', 'Lezione (nome sulla piattaforma)', 'Stato', 'Prima visualizzazione', 'Ultimo accesso', 'Completata il', 'Visualizzazioni', 'Test', 'Tentativi', 'Punteggio'],
                [16, 34, 7, 52, 11, 17, 17, 17, 9, 6, 9, 9])
    r = 5
    for c in sorted(corsi, key=lambda x: (x['mat'], x['corso'])):
        for l in c['lez']:
            if not (nel(l['pv']) or nel(l['ul']) or nel(l['comp'])): continue
            s = 'Completata' if nel(l['comp']) else 'A metà'
            riga(ws, r, [c['mat'], c['corso'], int(l['id']), l['tit'], s, l['pv'], l['ul'], l['comp'], l['ses'], l['test'], int(l['tent']) if str(l['tent']).isdigit() else l['tent'], l['pun']],
                 wrap=(2, 4), fill={5: COL.get(s)}); r += 1
    if r == 5:
        ultima = max([x for c in corsi for l in c['lez'] for x in (l['ul'], l['comp']) if x] or [None])
        ws.cell(5, 1, 'Nessuna lezione seguita sulla piattaforma dal 1° settembre a oggi.' + (f' Ultima attività: {f(ultima)}.' if ultima else '')).font = N
    # 3. Compiti
    ws = foglio(wb, 'Compiti', 'Compiti dal quaderno dei compiti', sotto,
                ['Materia', 'Lezione', 'Compito', 'Docente', 'Assegnato il', 'Scadenza', 'Stato', 'Consegnato il', 'Corretto il', 'Voto'], [16, 46, 40, 18, 12, 11, 22, 12, 12, 8])
    r = 5
    for x in sorted(comp, key=lambda x: (x['m'], x['ass'])):
        s, dc, dr, v = stato_compito(x)
        riga(ws, r, [x['m'], x['l'], x['t'], x['doc'], x['ass'][:10], x['sc'] or '', s, dc, dr, v or ''], wrap=(2, 3), fill={7: COL.get(s)}); r += 1
    if r == 5: ws.cell(5, 1, 'Nessun compito registrato nel quaderno per questo alunno.').font = N
    # 3b. Registro dei compiti (dai registri PDF dei prof)
    ws = foglio(wb, 'Registro', 'Registro dei compiti dei docenti (lezioni in diretta)', sotto + ' · fonte: registri PDF inviati dai docenti, inseriti nel registro online',
                ['Giorno', 'Materia', 'Docente', 'Contenuto del registro'], [12, 22, 20, 110])
    r = 5
    for v in sorted(reg, key=lambda x: (x['giorno'], x['mat'])):
        riga(ws, r, [v['giorno'], v['mat'].title(), v['doc'].title(), v['testo']], wrap=(4,)); r += 1
    if r == 5: ws.cell(5, 1, 'Nessun registro dei compiti ricevuto dai docenti per questo alunno.').font = N
    # 3c. Registro elettronico della piattaforma
    ws = foglio(wb, 'Registro piattaforma', 'Registro elettronico della piattaforma (lezioni in diretta)', sotto + ' · fonte: Lezioni → «Visualizza registro», compilato dal docente a fine lezione',
                ['Data e ora', 'Docente', 'Materia', 'Argomento trattato', 'Giudizio sull\'alunno', 'Voto', 'Compiti / indicazioni'], [15, 16, 14, 55, 55, 9, 40])
    r = 5
    for x in rp:
        riga(ws, r, [x['d'], x['doc'], x['mat'], x['arg'], x['fb'], x['voto'], x['comp']], wrap=(4, 5, 7), fill=({i: 'FBE0DE' for i in range(1, 8)} if x['assente'] else None)); r += 1
    if r == 5: ws.cell(5, 1, 'Nessun registro della piattaforma per questo alunno nel periodo.').font = N
    # 4. Report genitori
    ws = wb.create_sheet('Report genitori'); ws.column_dimensions['A'].width = 110
    ws['A1'] = f'Report per la famiglia · {nome}'; ws['A1'].font = T
    ws['A2'] = f'Periodo dal 1° settembre al {OGGI.day} novembre 2026'; ws['A2'].font = SB
    rr = 4; righe = []; ferme = []
    for c in sorted(corsi, key=lambda x: (x['mat'], x['corso'])):
        L = c['lez']; co = [l for l in L if nel(l['comp'])]; me = [l for l in L if (nel(l['pv']) or nel(l['ul'])) and not l['comp']]
        pts = [pct(l['pun']) for l in co if l['test'] == 'SI' and pct(l['pun']) is not None]
        if not co and not me: ferme.append(c['mat']); continue
        t = f'• {c["mat"]} ({c["corso"]}): {len(co)} lezioni completate'
        if pts: t += f', test superati con una media del {round(sum(pts)/len(pts))}%'
        if me: t += f'; {len(me)} lezioni iniziate e da completare'
        righe.append(t + '.')
    if ferme: righe.append('• Nessuna lezione seguita nel periodo in: ' + ', '.join(sorted(set(ferme))) + '.')
    ass = [x for x in comp if not x.get('st')]
    if ass:
        S2 = [stato_compito(x) for x in ass]
        righe.append(f'• Compiti: {len(ass)} assegnati, {sum(1 for s in S2 if s[1])} consegnati, {sum(1 for s in S2 if s[0] in ("Corretto","Verificato"))} corretti dal docente.')
    if reg:
        mm = sorted({v['mat'].title() for v in reg})
        righe.append(f'• Registro dei compiti dei docenti: {len(reg)} giornate di lezione in diretta con compiti assegnati ({", ".join(mm)}).')
    if rp:
        vv = [f"{x['d']:%d/%m} {x['mat']}: {x['voto']}" for x in rp if x['voto']]
        righe.append(f'• Lezioni in diretta con registro del docente: {len(rp)}' + (f'; voti: {"; ".join(vv)}.' if vv else '; nessun voto registrato.'))
    stor = [x for x in comp if x.get('st')]
    if stor: righe.append(f'• Lezioni in diretta del prof. Mazzotti: registrate le domande di {len(stor)} lezioni.')
    if not righe: righe = ['• Nessuna attività registrata sulla piattaforma nel periodo.']
    for t in righe: ws.cell(rr, 1, t).font = N; ws.cell(rr, 1).alignment = Alignment(wrap_text=True); rr += 1
    fn = re.sub(r'[^A-Za-z0-9]+', '_', nome.title()).strip('_')
    wb.save(P + f'finale/Report_{fn}_1set-{OGGI.strftime("%d%b").lower()}.xlsx')
    # quadro
    allL = [l for c in corsi for l in c['lez']]
    co = [l for l in allL if nel(l['comp'])]; me = [l for l in allL if (nel(l['pv']) or nel(l['ul'])) and not l['comp']]
    pts = [pct(l['pun']) for l in co if l['test'] == 'SI' and pct(l['pun']) is not None]
    ult = max([x for l in allL for x in (l['ul'], l['comp']) if x] or [None])
    S2 = [stato_compito(x) for x in ass]
    QUADRO.append([nome, ind, len(corsi), len(co), len(me), round(sum(pts)/len(pts)) if pts else '', f(ult), len(ass), sum(1 for s in S2 if s[1]),
                   sum(1 for s in S2 if s[0] in ('Corretto', 'Verificato')), len(stor), len(reg), len(rp), '; '.join(f"{x['d']:%d/%m} {x['voto']}" for x in rp if x['voto'])])

wb = Workbook(); wb.remove(wb.active)
ws = foglio(wb, 'Quadro generale', f'Quadro generale alunni · dal 1° settembre al {OGGI.day} novembre 2026', f'{len(QUADRO)} alunni · dati letti il {OGGI_TXT}',
            ['Alunno', 'Indirizzo', 'Corsi', 'Lezioni completate nel periodo', 'Lezioni a metà', 'Media test (%)', 'Ultima attività', 'Compiti assegnati', 'Consegnati', 'Corretti', 'Domande live (storico)', 'Giornate nel registro dei docenti (PDF)', 'Lezioni live con registro piattaforma', 'Voti dai registri'],
            [28, 46, 7, 13, 10, 10, 13, 10, 10, 9, 12, 13, 13, 30])
r = 5
for q in sorted(QUADRO, key=lambda x: x[0]):
    riga(ws, r, q, wrap=(2, 14), fill={4: 'FBE0DE' if q[3] == 0 else None}); r += 1
riga(ws, r, ['TOTALE', '', f'=SUM(C5:C{r-1})', f'=SUM(D5:D{r-1})', f'=SUM(E5:E{r-1})', '', '', f'=SUM(H5:H{r-1})', f'=SUM(I5:I{r-1})', f'=SUM(J5:J{r-1})', f'=SUM(K5:K{r-1})', f'=SUM(L5:L{r-1})', f'=SUM(M5:M{r-1})', ''])
for i in range(1, 15): ws.cell(r, i).font = B
if SENZA:
    ws2 = foglio(wb, 'Senza attività', 'Iscritti senza nessuna attività dal 1° settembre 2026', 'Probabili ex alunni: nessun report individuale',
                 ['Alunno', 'Indirizzo', 'Corsi', 'Ultima attività'], [28, 46, 7, 14])
    for i, x in enumerate(sorted(SENZA), 5): riga(ws2, i, list(x), wrap=(2,))
wb.save(P + f'finale/Quadro_generale_alunni_1set-{OGGI.strftime("%d%b").lower()}.xlsx')
print('alunni', len(QUADRO), 'report mancanti', len(MANCANTI), MANCANTI[:5])
