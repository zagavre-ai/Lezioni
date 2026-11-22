import sys, json, io; sys.path.insert(0, '/home/user/w3/build')
from pieces import *
import maps
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from PIL import Image
PW, PH = landscape(A4)
def add_page(c, arr, texts):
    im = Image.fromarray(arr); buf = io.BytesIO(); im.save(buf, 'PNG'); buf.seek(0)
    from reportlab.lib.utils import ImageReader
    h = PW * arr.shape[0] / arr.shape[1]; y = (PH - h) / 2
    c.drawImage(ImageReader(buf), 0, y, PW, h)
    t = c.beginText(20, PH - 30); t.setTextRenderMode(3); t.setFont('Helvetica', 10)   # strato di testo invisibile
    for line in texts:
        t.textLine(line.encode('latin-1', 'replace').decode('latin-1'))
    c.drawText(t); c.showPage()
def cover_plain(label_extra=None):
    h = tpl.frame('STORIA V · VIDEOLEZIONE' if not label_extra else f'STORIA V · {label_extra}', "L'Italia<br>di Giolitti", '', None, cam=False)
    h = h.replace('</style>', '.tit{font-size:112px !important;line-height:1.02 !important;top:190px !important}</style>', 1)
    return shot(h)
which = sys.argv[1]
if which in ('1', '2'):
    pages = json.load(open(f'/home/user/w3/pages_Parte{which}.json'))
    c = canvas.Canvas(sys.argv[2], pagesize=(PW, PH)); c.setTitle("Storia V · L'Italia di Giolitti · Dispensa Parte " + which); c.setAuthor('Centro Studi Telesio')
    add_page(c, cover_plain(), ["STORIA V", "L'Italia di Giolitti"])
    for pg in pages:
        A = D.ARG[pg['arg']]
        if pg['kind'] == 'slide':
            sub = [pg['cards'][i] for i in pg['idx']]; l2 = None if pg['lit'] is None else pg['idx'].index(pg['lit'])
            arr = shot(slide_html(pg['label'], esc(pg['title']), sub, l2, pg['page'], pg['kw'], cam=False))
            tx = [pg['label'], pg['title']] + [(x[0] if isinstance(x, (tuple, list)) else x) for x in sub] + [('Parole chiave: ' + ', '.join(pg['kw']))]
            tx += [x[1] for x in sub if isinstance(x, (tuple, list)) and x[1]]
        else:
            p_, ttl, cap = D.IMG[pg['img']]
            arr = shot(image_slide_html(pg['label'], esc(ttl), p_, cap, pg['page'], pg['kw'], cam=False))
            tx = [pg['label'], ttl, re.sub('<[^>]+>', ' ', cap)]
        add_page(c, arr, tx)
    c.save(); print('dispensa', len(pages) + 1, 'pagine')
else:   # PDF delle mappe: copertina + MAPPE
    c = canvas.Canvas(sys.argv[2], pagesize=(PW, PH)); c.setTitle("Storia V · L'Italia di Giolitti · Mappe"); c.setAuthor('Centro Studi Telesio')
    h = tpl.frame('STORIA V · VIDEOLEZIONE', "L'Italia<br>di Giolitti", '<div style="position:absolute;left:80px;top:560px;font:800 96px Bri;letter-spacing:.12em;color:#0B1530">MAPPE</div>', None, cam=False)
    h = h.replace('</style>', '.tit{font-size:112px !important;line-height:1.02 !important;top:190px !important}</style>', 1)
    add_page(c, shot(h), ['MAPPE', 'STORIA V', "L'Italia di Giolitti"])
    for k, M in maps.MAPS.items():
        tx = [M['title']] + [n[1] for n in M['nodes']] + [e[2] for e in M['edges']]
        add_page(c, shot(maps.map_html(M, len(M['nodes']), None)), tx)
    c.save(); print('mappe pdf')
