# schede Quiz / Verifica / Compiti con bande blu sopra e sotto (1920x1080), per Letteratura V lez 4
import json, base64, html, sys
S = '/tmp/claude-0/-home-user-Lezioni/aa838b16-be86-588f-84fd-78776ad6250d/scratchpad'
FONT = '/home/user/Lezioni/kit/tools/mappa_font'; E = html.escape
def b64(p): return base64.b64encode(open(p, 'rb').read()).decode()
CSS = ''.join(f"@font-face{{font-family:'{a}';src:url(data:font/ttf;base64,{b64(FONT+'/'+f)});font-weight:{w}}}" for a, f, w in
   [('Bricolage Grotesque','BricolageGrotesque-ExtraBold.ttf',800),('Figtree','Figtree-Regular.ttf',400),('Figtree','Figtree-SemiBold.ttf',600)])
LOGO = 'data:image/png;base64,' + b64('/home/claude/v5/logo_white.png')
BAND = 150
def card(kick, title, sub, pill=None):
    p = f'<div class="pill">{E(pill)}</div>' if pill else ''
    return f'''<!doctype html><meta charset=utf-8><style>{CSS}
*{{margin:0;box-sizing:border-box}}body{{width:1920px;height:1080px;background:#0B1530;position:relative;overflow:hidden;font-family:Figtree}}
.b{{position:absolute;left:0;right:0;height:{BAND}px;background:#2060AF}}
.w{{position:absolute;left:140px;right:140px;top:260px}}.k{{font-family:'Courier New',monospace;font-weight:700;font-size:34px;letter-spacing:.16em;color:#FFE600}}
.t{{margin-top:24px;font-family:'Bricolage Grotesque';font-weight:800;font-size:96px;line-height:1.05;color:#fff}}
.y{{margin-top:34px;width:220px;height:10px;background:#FFE600}}
.s{{margin-top:34px;font-size:44px;color:#fff}}
.pill{{display:inline-block;margin-top:30px;font-family:'Courier New',monospace;font-weight:700;font-size:34px;background:#FFE600;color:#0B1530;border-radius:40px;padding:10px 30px}}
img{{position:absolute;right:140px;top:780px;width:300px}}</style><body>
<div class=b style="top:0"></div><div class=b style="bottom:0"></div>
<div class=w><div class=k>{E(kick)}</div><div class=t>{E(title)}</div><div class=y></div><div class=s>{E(sub)}</div>{p}</div><img src="{LOGO}"></body>'''
def main(out):
    sch = json.load(open(f'{S}/l04/consegna-letteratura-V-lez04/scheda_pubblicazione.json'))
    tit = sch['titolo'].split(' · ')[0]; arg = {a['n']: a['titolo'] for a in sch['argomenti']}
    P = {}
    for n, t in arg.items():
        P[f'Q{n}'] = card('QUIZ', t, "Rispondi alle domande sull'argomento appena visto.", "5 domande · per continuare almeno l'80%")
    P['VERIFICA'] = card('VERIFICA FINALE', tit, 'Dieci domande su tutta la lezione.', "10 domande · per continuare almeno l'80%")
    P['COMPITI_INTRO'] = card('COMPITI', 'I compiti della lezione', 'Rispondi e premi «Consegna».')
    P['COMPITI'] = card('COMPITI', tit, 'Quattro domande aperte sulla lezione.', 'Rispondi e premi «Consegna»')
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page(viewport={'width': 1920, 'height': 1080})
        for k, h in P.items():
            pg.set_content(h); pg.wait_for_timeout(150); pg.screenshot(path=f'{out}/card_{k}.png')
        b.close()
if __name__ == '__main__': main(sys.argv[1])
