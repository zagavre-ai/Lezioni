# -*- coding: utf-8 -*-
# Dispensa A4 orizzontale: le slide del video (stessa grafica, stesso ordine, stessa numerazione) a tutta larghezza + strato di testo invisibile.
import sys, os, json, re
sys.path.insert(0, '/tmp/claude-0/l15')
from dati import *
import sl2
from plan2 import AN_OF, IMG_TOPIC
import mk_static as MS
from playwright.sync_api import sync_playwright
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
W = '/tmp/claude-0/l15'
pdfmetrics.registerFont(TTFont('FG', '/home/user/Lezioni/kit/caratteri/Figtree-Medium.ttf'))
IMGFILES = {6: ['up_p06_x29.png'], 8: ['up_p08_x34.png', 'up_p08_x35.png'], 11: ['up_p11_x42.png'], 13: ['up_p13_x47.png'], 15: ['up_p15_x52.png']}
PAGES = MS.PAGES
def build_pages():
    cp = sl2.cards_from_pdf(); out = [(0, 'cover', sl2.cover_dispensa())]
    for key, pg in sorted(PAGES.items(), key=lambda kv: kv[1]):
        if key == ('cover',): continue
        if key == ('agenda',): h = sl2.agenda(-1, pg)
        elif key[0] == 'txt': h = sl2.txt_slide(key[1], key[2], -1, cp, pg, prof=False)
        elif key[0] == 'img': h = sl2.img_slide(IMG_TOPIC[key[1]], [f'{W}/img/{f}' for f in IMGFILES[key[1]]], pg, prof=False)
        elif key[0] == 'an':
            an = key[1]; n = next(n for n in GLOBAL_ORDER if an in AN_OF[n]); ss = MS.sents(MS.TXT[f'AN{an}'])
            lab = f"{GLOBAL_ORDER.index(n) + 1:02d} · {ARG[n - 1]['nome']} · APPROFONDIMENTO"; h = sl2.an_slide(lab, ss[0].rstrip('.'), ss[1:], -1, len(ss) - 1, pg)
        elif key[0] == 'schema': h = sl2.schema(key[1], 99, pg)
        elif key[0] == 'gloss': h = sl2.gloss(-1, pg)
        elif key[0] == 'cmp': k0 = 2 * key[1] - 1; h = sl2.compiti2(k0, [c['testo'] for c in json.load(open(W + '/compiti.json'))['compiti']][k0 - 1:k0 + 1], -1, pg)
        else: continue
        out.append((pg, str(key), h))
    return out
def main(outpdf):
    pages = build_pages(); os.makedirs(W + '/dsp', exist_ok=True); texts = []; pngs = []
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=sl2.CHROME, args=['--allow-file-access-from-files', '--no-sandbox'])
        pg = b.new_page(viewport={'width': 1920, 'height': 1080}, device_scale_factor=1.5)
        for i, (n, name, h) in enumerate(pages):
            f = f'{W}/dsp/p{i:03d}.html'; open(f, 'w').write(h); pg.goto('file://' + f); pg.wait_for_timeout(250)
            png = f'{W}/dsp/p{i:03d}.png'; pg.screenshot(path=png); pngs.append(png)
            texts.append(pg.evaluate("document.body.innerText"))
        b.close()
    PW, PH = landscape(A4); c = canvas.Canvas(outpdf, pagesize=(PW, PH)); c.setTitle('Storia V · ' + LEZ_TITOLO); c.setAuthor('Centro Studi Telesio')
    for png, tx in zip(pngs, texts):
        h = PW * 1080 / 1920; y0 = (PH - h) / 2
        c.drawImage(png, 0, y0, width=PW, height=h)
        t = c.beginText(20, PH - 24); t.setFont('FG', 6); t.setTextRenderMode(3)
        for line in [x for x in tx.split('\n') if x.strip()]: t.textLine(line)
        c.drawText(t); c.showPage()
    c.save(); print(outpdf, len(pngs), 'pagine')
if __name__ == '__main__': main(sys.argv[1])
