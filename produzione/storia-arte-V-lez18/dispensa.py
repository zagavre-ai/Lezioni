# Dispensa A4 orizzontale = stesse schede del video (senza riquadro, fascia, evidenziazione) + strato di testo invisibile; PDF mappe vettoriale
import sys, os, json
sys.path.insert(0, '/home/user/w18')
from lib import *
from dati import *
import piano
from pages import ORDINE, PG
import kore
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
R = '/home/user/w18/'; O = R + 'consegna/'; PD = R + 'b/pd/'; os.makedirs(PD, exist_ok=True)
pdfmetrics.registerFont(TTFont('Fig', FD + 'Figtree-Regular.ttf')); pdfmetrics.registerFont(TTFont('FigB', FD + 'Figtree-Bold.ttf'))
pdfmetrics.registerFont(TTFont('FigS', FD + 'Figtree-SemiBold.ttf')); pdfmetrics.registerFont(TTFont('Bri', FD + 'BricolageGrotesque-ExtraBold.ttf'))
PW, PH = landscape(A4)

def pagina_slide(sid):
    if sid == 'COV':
        im = copertina(TITOLO, [t for _, t in ARGOMENTI], prof=False, page=1)
        return im, [TITOLO] + [t for _, t in ARGOMENTI]
    if sid in piano.TXT:
        a, tit, keys = piano.TXT[sid]
        # tutte le card normali, niente riquadro
        im = base_slide(piano.LAB[a], PG[sid]); y = title_block(im, tit); draw_cards(im, [piano.C[k] for k in keys], -1, y)
        return im, [tit] + [l + ' ' + b for l, b in (piano.C[k] for k in keys)]
    a, f, cr, kws = piano.IMG[sid]
    src = Image.open(R + 'img/' + f).convert('RGB')
    if cr: src = src.crop((int(cr[0] * src.width), int(cr[1] * src.height), int(cr[2] * src.width), int(cr[3] * src.height)))
    im = slide_immagine(piano.LAB[a], PG[sid], src, kws=None)
    # senza riquadro del prof: la colonna destra mostra solo le parole chiave
    d = ImageDraw.Draw(im); d.rectangle((1380, 130, 1900, 600), fill=(255, 255, 255, 255)); keywords_panel(im, kws)
    # sposta le parole chiave in alto (niente riquadro)
    return im, kws

def ultimo_frame(mp4, t_fine=None):
    p = PD + os.path.basename(mp4) + '.png'
    import subprocess
    d = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', mp4], capture_output=True, text=True).stdout)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{d - 1.0 if t_fine is None else t_fine:.2f}', '-i', mp4, '-frames:v', '1', p], check=True)
    return Image.open(p).convert('RGB')

def testi_scena(nome):
    a = nome.split('_')[-1]
    if nome.startswith('ap_'):
        cfg = kore.AP_CFG.get(a)
        if a == 'A1': return ['Dall\'agricoltura all\'industria al terziario tecnologico', '1979 Lyotard teorizza la condizione postmoderna', '1989 Cade il muro di Berlino', '1991 Si scioglie l\'Unione Sovietica', '2001 Attacco alle Twin Towers']
        return [c[1] for c in cfg[1]]
    if nome.startswith('rip_'): return RIP[a]
    if nome == 'gloss': return [t + ': ' + d for t, d in GLOSS]
    if nome == 'rf': return [t + ': ' + d for t, d in RF]
    return []

def costruisci():
    pagine = []   # (immagine, [testi])
    scene = {n: t for n, t, d in json.load(open(R + 'timeline_scene.json'))}
    base = R + 'b/'
    def ap(a): return (ultimo_frame(base + f'ap_{a}.mp4', 1.5 + 0.0), testi_scena(f'ap_{a}'))
    visti = set()
    for pid, a_, b_, arg, st in piano.PEZZI:
        for _, sid, _ in st:
            if sid in visti: continue
            visti.add(sid); pagine.append(pagina_slide(sid))
        if arg.startswith('A') and arg != 'A0':
            d = float(__import__('subprocess').run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', base + f'ap_{arg}.mp4'], capture_output=True, text=True).stdout)
            pagine.append((ultimo_frame(base + f'ap_{arg}.mp4', d - 1.2), testi_scena(f'ap_{arg}')))
            if arg == 'A4': pagine.append((ultimo_frame(base + 'map2.mp4', float(__import__('subprocess').run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', base + 'map2.mp4'], capture_output=True, text=True).stdout) - 1.5), MAPTXT2('MAP2')))
            if arg == 'A7': pagine.append((ultimo_frame(base + 'map3.mp4', float(__import__('subprocess').run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', base + 'map3.mp4'], capture_output=True, text=True).stdout) - 1.5), MAPTXT2('MAP3')))
            if True:
                dd = float(__import__('subprocess').run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', base + f'rip_{arg}.mp4'], capture_output=True, text=True).stdout)
                pagine.append((ultimo_frame(base + f'rip_{arg}.mp4', dd - 1.0), testi_scena(f'rip_{arg}')))
    for n in ('gloss', 'rf'):
        dd = float(__import__('subprocess').run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', base + f'{n}.mp4'], capture_output=True, text=True).stdout)
        pagine.append((ultimo_frame(base + f'{n}.mp4', dd - 1.0), testi_scena(n)))
    dd = float(__import__('subprocess').run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', base + 'map1.mp4'], capture_output=True, text=True).stdout)
    pagine.append((ultimo_frame(base + 'map1.mp4', dd - 1.5), MAPTXT2('MAP1')))
    return pagine

def MAPTXT2(k): return [MAPPE[k]['domanda']] + [n[1] for n in MAPPE[k]['nodi']]

def copertina_dispensa(extra=None):
    im = Image.new('RGBA', (W, H), (255, 255, 255, 255)); d = ImageDraw.Draw(im)
    im.alpha_composite(logo('blu', 52), (80, 50)); d.line((80, 124, 1840, 124), fill=(226, 230, 238), width=2)
    y = 330
    if extra: text_sp(d, (80, 250), extra, F('bold', 30), BLU, 6); y = 340
    text_sp(d, (80, y - 80 if not extra else 300 - 0), '', F('bold', 25), BLU, 3) if False else None
    text_sp(d, (80, 148 if not extra else 148), "STORIA DELL'ARTE V", F('bold', 25), BLU, 3.2)
    f = F('bric', 96); yy = 330
    for ln in wrap(d, TITOLO, f, 1700): d.text((80, yy), ln, font=f, fill=NOTTE); yy += 112
    d.rounded_rectangle((80, yy + 10, 165, yy + 17), 3, fill=BLU)
    return im

def pdf_slide(out, pagine, copertina_im):
    c = canvas.Canvas(out, pagesize=(PW, PH)); c.setTitle("Storia dell'arte V · " + TITOLO); c.setAuthor('Centro Studi Telesio')
    def pagina(img, testi, n):
        p = PD + f'pg{n}.jpg'; img.convert('RGB').save(p, quality=92)
        h = PW * 1080 / 1920; y = (PH - h) / 2
        c.drawImage(p, 0, y, PW, h)
        t = c.beginText(20, PH - 24); t.setTextRenderMode(3); t.setFont('Fig', 8)
        for ln in testi: t.textLine(ln)
        c.drawText(t); c.showPage()
    pagina(copertina_im, [TITOLO, "Storia dell'arte V"], 0)
    for i, (im, tx) in enumerate(pagine, 1): pagina(im, tx, i)
    c.save()

def pdf_mappe(out):
    S = PW / 1920
    c = canvas.Canvas(out, pagesize=(PW, PH)); c.setTitle("Mappe · Storia dell'arte V · " + TITOLO); c.setAuthor('Centro Studi Telesio')
    # copertina
    cov = copertina_dispensa('MAPPE'); p = PD + 'covmap.jpg'; cov.convert('RGB').save(p, quality=92)
    h = PW * 1080 / 1920; c.drawImage(p, 0, (PH - h) / 2, PW, h)
    t = c.beginText(20, PH - 24); t.setTextRenderMode(3); t.setFont('Fig', 8); t.textLine('MAPPE'); t.textLine("Storia dell'arte V"); t.textLine(TITOLO); c.drawText(t); c.showPage()
    def rgb(x): return tuple(v / 255 for v in x)
    for pgn, key in enumerate(['MAP1', 'MAP2', 'MAP3'], 1):
        M = MAPPE[key]; D = kore.MAPDEF[key]; texts = [n[1] for n in M['nodi']]
        def X(x): return x * S
        def Y(y): return PH - (PH - 1080 * S) / 2 - y * S
        c.setStrokeColor(rgb(NOTTE)); c.setFillColor(rgb(NOTTE)); c.setFont('Bri', 44 * S)
        c.setFillColor(rgb(NOTTE)); c.setFont('Bri', 50 * S); c.drawString(X(80), Y(190), M['domanda'])
        # legenda
        x = 1840
        c.setFont('Fig', 20 * S)
        for k_, lab in reversed(kore.LEG):
            w_ = pdfmetrics.stringWidth(lab, 'Fig', 20 * S); x -= w_ / S; c.setFillColor(rgb(NOTTE)); c.drawString(X(x), Y(84), lab); x -= 34
            c.setFillColor(rgb(kore.COL[k_][0])); c.setStrokeColor(rgb(kore.COL[k_][1])); c.setLineWidth(3 * S); c.roundRect(X(x), Y(86), 24 * S, 20 * S, 4 * S, fill=1, stroke=1); x -= 22
        # frecce (vettoriali) e riquadri
        for (a, b) in D['arrows']:
            ca, wa, ha = D['box'][a][0], D['box'][a][1], D['box'][a][2]; cb, wb, hb = D['box'][b][0], D['box'][b][1], D['box'][b][2]
            p0 = kore.edge_pt(ca, wa + 30, ha + 30, cb); p1 = kore.edge_pt(cb, wb + 30, hb + 30, ca)
            c.setStrokeColor(rgb(NOTTE)); c.setLineWidth(10 * S); c.line(X(p0[0]), Y(p0[1]), X(p1[0]), Y(p1[1]))
            ang = math.atan2(p1[1] - p0[1], p1[0] - p0[0]); L = 40
            pts = [(p1[0], p1[1]), (p1[0] - L * math.cos(ang - .45), p1[1] - L * math.sin(ang - .45)), (p1[0] - L * math.cos(ang + .45), p1[1] - L * math.sin(ang + .45))]
            pth = c.beginPath(); pth.moveTo(X(pts[0][0]), Y(pts[0][1])); pth.lineTo(X(pts[1][0]), Y(pts[1][1])); pth.lineTo(X(pts[2][0]), Y(pts[2][1])); pth.close()
            c.setFillColor(rgb(NOTTE)); c.drawPath(pth, fill=1, stroke=0)
        for i, (cc, w_, h_, role, sz) in enumerate(D['box']):
            fill, bord = kore.COL[role]
            c.setFillColor(rgb(fill)); c.setStrokeColor(rgb(bord)); c.setLineWidth((6 if role == 'centro' else 5) * S)
            c.roundRect(X(cc[0] - w_ / 2), Y(cc[1] + h_ / 2), w_ * S, h_ * S, 16 * S, fill=1, stroke=1)
            fn = 'Bri' if role == 'centro' else 'FigS'
            lines = wrap(ImageDraw.Draw(Image.new('RGB', (10, 10))), texts[i], F('bric' if role == 'centro' else 'semi', sz), w_ - 50)
            lh = sz * 1.3; ty = cc[1] - lh * len(lines) / 2
            c.setFillColor(rgb(NOTTE)); c.setFont(fn, sz * S)
            for ln in lines:
                c.drawCentredString(X(cc[0]), Y(ty + sz * 0.95), ln); ty += lh
        # piè di pagina
        c.setFont('FigB', 9); c.setFillColor(rgb(BLU)); c.drawString(X(80), 20, "STORIA DELL'ARTE V"); c.drawRightString(PW - X(80), 20, f'Pagina {pgn}')
        c.showPage()
    c.save()

if __name__ == '__main__':
    pdf_mappe(O + 'StoriaArte_Lez18_mappe.pdf')
    if '--slide' in sys.argv:
        pg = costruisci(); pdf_slide(O + 'StoriaArte_Lez18_dispensa.pdf', pg, copertina_dispensa())
    print('ok')
