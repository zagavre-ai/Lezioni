# -*- coding: utf-8 -*-
# PDF A4 orizzontale: slide identiche al video (senza riquadro e fascia) e mappe del prof con la nostra grafica.
import sys, os, json, re
sys.path.insert(0, '/tmp/claude-0/l15')
from dati import *
import slides as SL
from playwright.sync_api import sync_playwright
import fitz
W = '/tmp/claude-0/l15'

def to_pdf(htmls, out):
    docs = []
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=SL.CHROME, args=['--allow-file-access-from-files', '--no-sandbox'])
        pg = b.new_page(viewport={'width': 1920, 'height': 1080})
        for i, h in enumerate(htmls):
            h = h.replace('</style>', '@page{size:A4 landscape;margin:0}html,body{margin:0}body{top:145px !important}</style>', 1)
            f = f'{W}/slpng/_pdf{i}.html'; open(f, 'w').write(h)
            pg.goto('file://' + f); pg.wait_for_timeout(200)
            pg.pdf(path=f'{W}/slpng/_pdf{i}.pdf', width='297mm', height='210mm', scale=0.58, print_background=True, margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'}, page_ranges='1')
            docs.append(f'{W}/slpng/_pdf{i}.pdf')
        b.close()
    m = fitz.open()
    for d in docs: m.insert_pdf(fitz.open(d))
    m.save(out); print(out, len(m), 'pagine')

def slide_pdf(P, out):
    from build_prof import IMGFILE
    from plan_prof import IMGPAGES
    order = PARTI[P]; pass
    cp = SL.cards_from_pdf(); pages = {eval(k): v for k, v in json.load(open(f'{W}/pieces/pages_P{P}.json')).items()}
    htmls = []; seen = set()
    # ordine per numero di pagina
    for key, pg in sorted(pages.items(), key=lambda kv: kv[1]):
        if key == ('cover',): htmls.append(SL.html_cover(pg, False, order, P if P > 1 else None))
        elif key[0] == 'txt': htmls.append(SL.html_txt(key[1], -1, cp, pg, prof=False))
        elif key[0] == 'img':
            # argomento in cui compare (dai json dei pezzi)
            n = None
            for T in order:
                f = f'{W}/pieces/P{P}_T{T}.mp4.json'
                if os.path.exists(f):
                    for k, _ in json.load(open(f))['runs']:
                        if k[0] == 'img' and int(k[1]) == key[1]: n = T
            htmls.append(SL.html_img(n or order[0], IMGFILE[key[1]], pg, prof=False))
        elif key[0] == 'schema': htmls.append(SL.html_schema(key[1], NC, pg))
        elif key[0] == 'gloss': htmls.append(SL.html_gloss(-1, pg))
    to_pdf(htmls, out)

def mappe_pdf(P, out):
    from dati import mappa_di
    pass
    hs = []
    for i, n in enumerate(PARTI[P]):
        kind, idx = mappa_di(n)
        hs.append(SL.html_map(idx, 1.0, i + 1) if kind == 'prof' else SL.html_newmap(n, NC, i + 1))
    to_pdf(hs, out)
