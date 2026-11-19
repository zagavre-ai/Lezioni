# -*- coding: utf-8 -*-
# PDF A4 delle slide (identiche al video, senza riquadro) e delle mappe (mappa.py) per una Parte. uso: python3 pdfs2.py PARTE
import sys, os, json, re
sys.path.insert(0, '/tmp/claude-0/w')
os.environ['PLAYWRIGHT_BROWSERS_PATH'] = '/opt/pw-browsers'
sys.argv_save = sys.argv; P = int(sys.argv[1]); sys.argv = ['build2.py', str(P)]
exec(open('/home/user/w/l04/work/build2.py').read().split("if __name__")[0])
from playwright.sync_api import sync_playwright
import fitz
WK = '/home/user/w/l04/work'; OUT = f'{WK}/out{P}'; order = PARTI[P]
cp = SL.cards_from_pdf()

def parse(k):
    out = []
    for t in k.split('|'):
        try: out.append(eval(t))
        except Exception: out.append(t)
    return tuple(out)

pagesf = f'{NEWP}/pages_P{P}_all.json'
pages = {parse(k): v for k, v in json.load(open(pagesf)).items()}
if P == 3:
    pass
htmls = []
for key, pg in sorted(pages.items(), key=lambda kv: kv[1]):
    if key[0] == 'cover': htmls.append(SL.html_cover(pg, False, order, P if P > 1 else None))
    elif key[0] == 'percorso': htmls.append(html_percorso(order, pg).replace("<div class=shadow></div>", ""))
    elif key[0] == 'cards':
        n, cset = key[1], key[2]; a = ARG[n - 1]; cards = ''
        for i in cset:
            h, b = SL.head_body(cp[n][i])
            cards += f"<div class='card'><div class=num>{i + 1}</div><div><b>{SL.esc(h)}:</b> {SL.esc(b)}</div></div>"
        htmls.append(SL.frame(f"{SL.P2(n):02d} · {a['nome']}", SL.esc(a['titolo']).replace("casus belli", "<i>casus belli</i>"), pg, f"<div class=cards>{cards}</div>", prof=False, titlesize=50, pdf=True))
    elif key[0] == 'img': htmls.append(SL.html_img(key[2], IMGFILE[key[1]], pg, prof=False))
    # 'imgc' (immagine + card) e' la stessa immagine gia' presente: non si ripete nel PDF

def to_pdf(htmls, out):
    docs = []
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=SL.CHROME, args=['--allow-file-access-from-files', '--no-sandbox'])
        pg = b.new_page(viewport={'width': 1920, 'height': 1080})
        for i, h in enumerate(htmls):
            h = h.replace('</style>', '@page{size:A4 landscape;margin:0}html,body{margin:0}body{top:145px !important}</style>', 1)
            f = f'{SLP}/_pdf{i}.html'; open(f, 'w').write(h)
            pg.goto('file://' + f); pg.wait_for_timeout(200)
            pg.pdf(path=f'{SLP}/_pdf{i}.pdf', width='297mm', height='210mm', scale=0.58, print_background=True, margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'}, page_ranges='1')
            docs.append(f'{SLP}/_pdf{i}.pdf')
        b.close()
    m = fitz.open()
    for d in docs: m.insert_pdf(fitz.open(d))
    m.save(out); print(out, len(m), 'pagine')

to_pdf(htmls, f'{OUT}/Storia_Lez4_Parte{P}_slide.pdf')
# mappe: una pagina A4 per argomento (mappa.py), nell'ordine del video
m = fitz.open()
for n in order:
    m.insert_pdf(fitz.open(f'{WK}/maps/{n}/mappa_dispensa.pdf'))
m.save(f'{OUT}/Storia_Lez4_Parte{P}_mappe.pdf'); print('mappe', len(m), 'pagine')
