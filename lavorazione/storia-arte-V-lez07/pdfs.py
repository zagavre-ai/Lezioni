# Dispensa A4 orizzontale (identica alle slide del video + testo invisibile) e PDF delle mappe
import sys, os, io
sys.path.insert(0, '/tmp/claude-0/w/build')
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import teacher, spec, gfx
from gfx import *
pdfmetrics.registerFont(TTFont('Fig', FD + 'Figtree-Regular.ttf'))
PW, PH = landscape(A4)

def cover_img(extra=None, with_args=False):
    im = new_slide(); d = ImageDraw.Draw(im)
    spaced(d, (80, 170), "STORIA DELL'ARTE V · VIDEOLEZIONE" if not extra else "STORIA DELL'ARTE V · %s" % extra, F('xbold', 28), BLUE, 5)
    d.text((80, 230), 'Le Avanguardie', font=F('title', 150), fill=NAVY); d.rounded_rectangle((80, 430, 200, 438), 4, fill=BLUE)
    footer(im, 1); return im

def page_pdf(c, im, texts):
    buf = io.BytesIO(); im.convert('RGB').save(buf, 'JPEG', quality=93, subsampling=0); buf.seek(0)
    from reportlab.lib.utils import ImageReader
    h = PW * 1080 / 1920; y = (PH - h) / 2
    c.drawImage(ImageReader(buf), 0, y, PW, h)
    t = c.beginText(20, PH - 30); t.setTextRenderMode(3); t.setFont('Fig', 8)
    for line in texts: t.textLine(line)
    c.drawText(t); c.showPage()

def dispensa(path):
    teacher.ensure_pages(); c = canvas.Canvas(path, pagesize=(PW, PH)); c.setTitle('Storia dell\'arte V · Le Avanguardie'); c.setAuthor('Centro Studi Telesio')
    page_pdf(c, cover_img(), ["Storia dell'arte V", 'Le Avanguardie'])
    seen = set(); B = teacher.bounds()
    for j, t in enumerate(spec.T):
        iv = teacher.keep_frames(B[j][0], B[j][1]); m = teacher.mapper(iv)
        seq, screens, ycs = teacher.timeline_states(t, m, sum(b - a for a, b in iv))
        cs = spec.cards(t['pdf'])
        for f, st, lab in seq:
            key = (t['n'], 'title') if st[0] == 'title' else ((t['n'], 'img', st[1]) if st[0] == 'img' else (t['n'], 'cards', st[1]))
            if key in seen: continue
            seen.add(key); pg = teacher.PAGES[key]
            if st[0] == 'cards': st2 = ('cards', st[1], tuple(3 for _ in st[2]))
            else: st2 = st
            im = teacher.render_state(t, st2, screens, ycs, pg)
            # senza riquadro del docente: si ridisegna la colonna destra solo con le parole chiave
            im = strip_box(im, t, st2, screens, ycs, pg)
            tx = [spec.ptitle(t['pdf'])]
            if st[0] == 'cards': tx += [cs[i] for i in screens[st[1]]]
            elif st[0] == 'img': tx += [spec.CAP[st[1]]]
            tx += t['kw'] + [gfx.MATERIA, 'Pagina %d' % pg]
            page_pdf(c, im, tx)
    c.save()

def strip_box(im, t, st, screens, ycs, pg):
    # ricostruisce la slide senza ombra/fascia del docente
    import teacher as T
    orig = gfx.right_column
    gfx.right_column = lambda im_, kw=None, box=True: orig(im_, kw, box=False)
    T.right_column = gfx.right_column
    try: out = T.render_state(t, st, screens, ycs, pg)
    finally: gfx.right_column = orig; T.right_column = orig
    return out

def mappe(path, maps):
    c = canvas.Canvas(path, pagesize=(PW, PH)); c.setTitle("Storia dell'arte V · Le Avanguardie · Mappe")
    im = cover_img('MAPPE'); d = ImageDraw.Draw(im)
    d.text((80, 470), 'MAPPE', font=F('title', 110), fill=BLUE)
    page_pdf(c, im, ["Storia dell'arte V", 'Le Avanguardie', 'MAPPE'])
    for M in maps:
        im = M.static(); tx = [M.title] + [n.text for n in M.nodes.values()]
        page_pdf(c, im, tx)
    c.save()
