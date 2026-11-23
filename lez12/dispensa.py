# Dispensa A4 orizzontale (slide identiche al video, senza riquadro/fascia) + PDF mappe, con strato di testo invisibile
import sys, os, re, html
sys.path.insert(0, '/home/user/Lezioni/lez12')
import scenes as S, run as RN, piano as PI
from piano import SL, IM
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.utils import ImageReader
D = '/home/user/Lezioni/lavoro/consegna/'; os.makedirs(D, exist_ok=True)
txt = lambda s: re.sub(r'<[^>]+>', '', html.unescape(s))
def cover_png(map_=False):
    o = f'{S.PNG}cop_{int(map_)}.png'
    def f(p):
        h = f'<img class=logo src="file://{S.pj(0)}"><div class=hl0></div>'
        h += f'<div class=eb style="top:150px">{"MAPPE · " if map_ else ""}STORIA DELL\'ARTE V</div>'
        h += f'<div class=ti style="top:230px;font-size:120px;width:1500px">{PI.TITOLO}</div><div class=bar style="top:520px"></div>'
        h += f'<div class=ft><b style="left:0">{S.MAT}</b></div>'
        S.rr().page(h, p)
    return S.cache(o, f)
def pagina(c, png, testo):
    W, H = landscape(A4); iw = W; ih = W * 1080 / 1920; y = (H - ih) / 2
    c.drawImage(ImageReader(png), 0, y, iw, ih)
    t = c.beginText(20, H - 30); t.setTextRenderMode(3); t.setFont('Helvetica', 10)
    for line in testo: t.textLine(line)
    c.drawText(t); c.showPage()
def dispensa():
    c = canvas.Canvas(D + 'StoriaArteV_Lez12_dispensa.pdf', pagesize=landscape(A4)); c.setTitle('Storia dell\'arte V · Dadaismo e Surrealismo · dispensa')
    pagina(c, cover_png(), ['Storia dell\'arte V', PI.TITOLO])
    for k, n in sorted(PAGES.items(), key=lambda x: x[1]):
        if k in SL:
            a, title, cards, kw = SL[k]; png = S.png_slide(k, None, None, False); tx = [PI.EYEB[a], txt(title)] + [txt(x) for x in cards] + ['Parole chiave: ' + ', '.join(kw)] + ['Pagina %d' % n]
        else:
            a, title, items = IM[k]; png = S.png_slide(k, None, None, False); tx = [PI.EYEB[a], txt(title)] + [txt(i[5]) for i in items if i[5]] + ['Pagina %d' % n]
        pagina(c, png, tx)
    c.save()
def mappe():
    c = canvas.Canvas(D + 'StoriaArteV_Lez12_mappe.pdf', pagesize=landscape(A4)); c.setTitle('Storia dell\'arte V · Dadaismo e Surrealismo · mappe')
    pagina(c, cover_png(True), ['Mappe', 'Storia dell\'arte V', PI.TITOLO])
    p = S.cache(f'{S.PNG}map_full.png', lambda o: RN.render_map(99, o))
    pagina(c, p, ["Che cos'è il Dadaismo?", 'Dadaismo (Zurigo 1916)', 'Movimento artistico di rottura contro la società borghese e capitalista', "L'unica regola è non avere regole",
                  "Dada è una parola senza senso, fa leva sull'irrazionalità", 'Principali esponenti: Tristan Tzara, Jean Arp, Marcel Duchamp, Man Ray, Marcel Janco',
                  "Principali tecniche e concetti trattati: Ready-made, Provocazione totale, Valore dell'idea, Oggetti con altro significato"])
    c.save()
PAGES = S.PAGES
if __name__ == '__main__':
    dispensa(); mappe(); print('ok')
