# -*- coding: utf-8 -*-
# Animazioni «voce Kore»: approfondimenti e spiegoni. Pagina bianca nel modello slide (senza riquadro del docente),
# frasi chiave che entrano a tempo con la voce, immagine del prof con lento movimento.
# uso: python3 kore.py spec.json out.mp4      (spec: vedi make_spec)
import sys, os, json, subprocess, base64, html
from playwright.sync_api import sync_playwright
sys.path.insert(0, '/tmp/claude-0/w')
import slides as SL
W = '/tmp/claude-0/w'
CHROME = '/opt/pw-browsers/chromium-1243/chrome-linux64/chrome'

PAGE = """<html><head><meta charset=utf-8><style>%(css)s
.kick{position:absolute;left:80px;top:146px;background:#FFE600;border-radius:30px;padding:8px 26px;font-weight:800;font-size:24px;letter-spacing:.2em;color:#0B1530}
.k-t{position:absolute;left:80px;top:206px;font-family:'BG';font-weight:800;font-size:56px;letter-spacing:-.02em;line-height:1.05;width:1700px;color:#0B1530}
.chips{position:absolute;left:80px;top:300px;width:%(cw)spx}.chip{position:relative;margin-bottom:18px;border:3px solid #E3E7EF;border-radius:22px;padding:14px 26px;background:#fff;font-size:38px;line-height:1.35;font-weight:700;opacity:0;box-shadow:0 10px 30px rgba(30,40,70,.10)}
.chip .n{display:inline-block;width:46px;height:46px;border-radius:50%%;background:#E3E7EF;text-align:center;line-height:46px;font-weight:800;font-size:26px;margin-right:16px}
.chip.on{border-color:#FFE600;background:#FFFBD6;box-shadow:0 8px 24px rgba(255,214,0,.35)}
.chip.on .n{background:#FFE600}
.imgf{position:absolute;left:%(ix)spx;top:300px;width:%(iw)spx;height:640px;border-radius:22px;border:3px solid #E3E7EF;box-shadow:0 14px 40px rgba(30,40,70,.12);overflow:hidden;background:#fff}
.imgf img{position:absolute;left:0;top:0;width:100%%;height:100%%;object-fit:contain;transform-origin:50%% 50%%}
.bar2{position:absolute;left:80px;bottom:112px;height:8px;border-radius:4px;background:#E3E7EF;width:1760px}
.bar2 i{display:block;height:100%%;background:#2060AF;border-radius:4px;width:0}
</style></head><body>
<img id=logo src='data:image/svg+xml;base64,%(logo)s'><div class=hl></div><div class=fl></div>
<div class=kick>%(kicker)s</div><div class=k-t>%(title)s</div>
%(chips)s%(img)s
<div class=bar2><i id=pb></i></div>
<div class=foot style='left:80px'>Storia V</div><div class=foot style='right:80px' id=pg></div>
<script>
const CH=%(chj)s, DUR=%(dur)s;
function render(t){
  CH.forEach((c,i)=>{const e=document.getElementById('c'+i);
    const a=Math.min(1,Math.max(0,(t-c[0])/0.45)); e.style.opacity=a; e.style.transform='translateY('+((1-a)*26)+'px)';
    const on=(t>=c[0]&&t<c[1]); e.classList.toggle('on',on);});
  const im=document.getElementById('im'); if(im){const k=1+0.035*t/DUR; im.style.transform='scale('+k+')';}
  document.getElementById('pb').style.width=(100*Math.min(1,t/DUR))+'%%';
}
</script></body></html>"""

def make_html(spec):
    chips = spec['chips']; n = len(chips)
    hasimg = bool(spec.get('img'))
    cw = 860 if hasimg else 1700
    ys = []; y = 300; gap = 18
    hs = [(max(1, -(-len(c['text']) // (30 if hasimg else 58))) * 51 + 34) for c in chips]
    # se non entrano, riduci lo spazio
    tot = sum(hs) + gap * (n - 1)
    for h in hs: ys.append(y); y += h + gap
    ch = "<div class=chips>" + ''.join(f"<div class=chip id=c{i}><span class=n>{i + 1}</span>{html.escape(c['text'])}</div>" for i, c in enumerate(chips)) + "</div>"
    img = ''
    if hasimg:
        img = f"<div class=imgf><img id=im src='file://{spec['img']}'></div>"
    chj = json.dumps([[c['t0'], (chips[i + 1]['t0'] if i + 1 < n else spec['dur'] + 1)] for i, c in enumerate(chips)])
    return PAGE % dict(css=SL.CSS, cw=cw, ix=1000, iw=840, logo=SL.LOGO, kicker=html.escape(spec['kicker']), title=html.escape(spec['title']),
                       chips=ch, img=img, chj=chj, dur=spec['dur']), tot

def render_video(spec, out, fps=30):
    h, tot = make_html(spec)
    if tot > 700: print('ATTENZIONE: chips alti', tot, spec['title'])
    f = out + '.html'; open(f, 'w').write(h)
    N = int(round(spec['dur'] * fps))
    ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'image2pipe', '-framerate', str(fps), '-c:v', 'mjpeg', '-i', '-', '-frames:v', str(N),
                           '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-r', str(fps), '-g', '60', '-threads', '2', out], stdin=subprocess.PIPE)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME, args=['--allow-file-access-from-files', '--no-sandbox'])
        pg = b.new_page(viewport={'width': 1920, 'height': 1080})
        pg.goto('file://' + f); pg.wait_for_timeout(400)
        pg.evaluate("document.getElementById('pg').textContent='Pagina %s'" % spec.get('page', 1))
        for i in range(N):
            pg.evaluate(f"render({i / fps:.4f})")
            ff.stdin.write(pg.screenshot(type='jpeg', quality=94))
        b.close()
    ff.stdin.close(); ff.wait()

if __name__ == '__main__':
    render_video(json.load(open(sys.argv[1])), sys.argv[2])
