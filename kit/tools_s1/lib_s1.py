# Libreria di montaggio S1 · Storia V · Centro Studi Telesio
# Schede HTML -> PNG (Chromium), clip con ffmpeg (video H.264 + audio PCM, durate esatte in fotogrammi).
import os, sys, json, re, subprocess, base64, html, math, hashlib, shutil
from PIL import Image
import numpy as np

QUI = os.path.dirname(os.path.abspath(__file__))
FONT = '/home/user/Lezioni/kit/tools/mappa_font'
FPS = 30
CHROME = '/opt/pw-browsers/chromium-1243/chrome-linux64/chrome'
E = html.escape
SND = '/home/claude/v5/snd'


def fr(sec):
    return int(round(sec * FPS))


def b64(p):
    return base64.b64encode(open(p, 'rb').read()).decode()


LOGO_W = 'data:image/png;base64,' + b64(QUI + '/assets/logo_white.png')
LOGO_I = 'data:image/png;base64,' + b64(QUI + '/assets/logo_ink.png')


def fonts():
    o = []
    for fam, f, w in [('BG', 'BricolageGrotesque-ExtraBold.ttf', 800), ('FG', 'Figtree-Regular.ttf', 400),
                      ('FG', 'Figtree-SemiBold.ttf', 600), ('FG', 'Figtree-Bold.ttf', 700)]:
        o.append("@font-face{font-family:'%s';font-weight:%d;src:url(data:font/ttf;base64,%s)}" % (fam, w, b64('%s/%s' % (FONT, f))))
    return '\n'.join(o)


CSS = fonts() + """
:root{--notte:#0B1530;--blu:#2060AF;--giallo:#FFE600;--grigio:#EEF0F4;--linea:#C9D0DC}
*{box-sizing:border-box;margin:0;padding:0}
body{width:1920px;height:1080px;overflow:hidden;font-family:'FG';color:var(--notte);position:relative}
.abs{position:absolute}
.dark{background:#070C1F;color:#F3F5FA}
.dark .bg{position:absolute;inset:0;background:radial-gradient(1400px 900px at 30% 20%,#13224A 0%,#0A1330 55%,#060A1B 100%)}
.orb{position:absolute;border-radius:50%;filter:blur(90px)}
.o1{width:900px;height:900px;background:#2060AF;opacity:.45;left:200px;top:-100px}
.o2{width:700px;height:700px;background:#1FB5D6;opacity:.16;left:1200px;top:100px}
.o3{width:620px;height:620px;background:#D9954A;opacity:.2;left:1000px;top:600px}
.grid{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px);background-size:120px 120px}
.vig{position:absolute;inset:0;background:radial-gradient(ellipse at center,transparent 55%,rgba(0,0,0,.55) 100%)}
.light{background:#F5F8FC}
.bg2{font-family:'BG';font-weight:800;letter-spacing:-.02em;line-height:1.02}
.kick{font-weight:700;letter-spacing:.3em;text-transform:uppercase}
.band{position:absolute;left:0;right:0;height:96px;background:#2060AF;z-index:5}
.glass{background:rgba(255,255,255,.07);border:1.5px solid rgba(255,255,255,.18);border-radius:26px;box-shadow:0 24px 60px rgba(0,0,0,.35)}
.ghost{font-family:'BG';font-weight:800;color:transparent;-webkit-text-stroke:3px rgba(255,255,255,.12);line-height:.8;white-space:nowrap}
.card{background:#fff;border:3px solid #E3E8F1;border-radius:22px;box-shadow:0 10px 30px rgba(20,40,90,.08)}
.hd{position:absolute;left:80px;top:48px;height:58px}
.hl{position:absolute;left:80px;right:80px;top:124px;height:1px;background:#D9DFEA}
.ft{position:absolute;left:80px;right:80px;bottom:44px;border-top:1px solid #D9DFEA;padding-top:18px;font-weight:700;letter-spacing:.22em;font-size:20px;color:#2060AF;text-transform:uppercase}
.doc{position:absolute;left:1490px;top:150px;width:380px;height:218px;border:6px solid #2060AF;border-radius:18px;background:#2060AF;box-shadow:0 14px 30px rgba(20,40,90,.25)}
.tag{position:absolute;left:1490px;top:392px;width:380px;transform:rotate(-2.2deg);background:#FFE600;border-radius:8px;padding:16px 22px;box-shadow:0 8px 20px rgba(0,0,0,.18)}
.tag b{font-family:'BG';font-weight:800;font-size:26px;display:block}
.tag i{font-style:normal;font-size:19px;display:block;margin-top:2px}
.tag u{text-decoration:none;font-weight:700;letter-spacing:.14em;font-size:17px;display:block;margin-top:4px}
"""


def page(body, cls='light', extra_css=''):
    return '<!doctype html><meta charset=utf-8><style>%s%s</style><body class="%s">%s</body>' % (CSS, extra_css, cls, body)


def dark_bg(inner, logo=True, bande_on=False):
    return ('<div class=bg></div><div class="orb o1"></div><div class="orb o2"></div><div class="orb o3"></div><div class=grid></div>'
            + ('<img class=abs src="%s" style="left:150px;top:78px;height:64px">' % LOGO_W if logo and not bande_on else '') + inner + '<div class=vig></div>')


# ----------------------------------------------------------------- renderer
class Renderer:
    def __init__(self):
        from playwright.sync_api import sync_playwright
        self.pw = sync_playwright().start()
        self.b = self.pw.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
        self.pg = self.b.new_page(viewport={'width': 1920, 'height': 1080})

    def shot(self, html_str, path):
        self.pg.set_content(html_str)
        self.pg.wait_for_timeout(60)
        self.pg.evaluate("document.fonts.ready")
        self.pg.screenshot(path=path)
        return path

    def fit(self, html_str, path, sel_container, max_bottom):
        """Come shot, ma sceglie corpo (38..30 px) e interlinea in modo che il contenitore stia sopra max_bottom."""
        self.pg.set_content(html_str)
        self.pg.evaluate("document.fonts.ready")
        self.pg.wait_for_timeout(60)
        b = 0
        for fs in (38, 36, 34, 32, 30):
            done = False
            for lh, pad, gap in [(1.36, 24, 20), (1.30, 20, 16), (1.26, 16, 12), (1.22, 12, 10)]:
                self.pg.evaluate("(a)=>{const r=document.documentElement.style;r.setProperty('--fs',a[0]+'px');r.setProperty('--lh',a[1]);r.setProperty('--pad',a[2]+'px');r.setProperty('--gap',a[3]+'px');}", [fs, lh, pad, gap])
                b = self.pg.evaluate("()=>{const e=document.querySelector('%s');return e?e.getBoundingClientRect().bottom:0}" % sel_container)
                if b <= max_bottom:
                    done = True
                    break
            if done:
                break
        self.pg.screenshot(path=path)
        return b

    def close(self):
        self.b.close()
        self.pw.stop()


# ----------------------------------------------------------------- ffmpeg
def sh(cmd, **k):
    r = subprocess.run(cmd, capture_output=True, text=True, **k)
    if r.returncode:
        raise RuntimeError('ffmpeg: ' + ' '.join(cmd[:6]) + '\n' + r.stderr[-1500:])
    return r


def dur(f):
    return float(sh(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f]).stdout)


def nframes(f):
    return int(sh(['ffprobe', '-v', 'error', '-count_packets', '-select_streams', 'v:0', '-show_entries', 'stream=nb_read_packets', '-of', 'csv=p=0', f]).stdout)


VENC = ['-c:v', 'libx264', '-preset', 'ultrafast', '-crf', '17', '-pix_fmt', 'yuv420p', '-r', '30', '-g', '30']
AENC = ['-c:a', 'pcm_s16le', '-ar', '48000', '-ac', '2']


def blend_seq(a, b, n, outdir, tag):
    """n fotogrammi di dissolvenza tra le immagini a e b; restituisce i percorsi."""
    A = np.asarray(Image.open(a).convert('RGB'), dtype=np.float32)
    B = np.asarray(Image.open(b).convert('RGB'), dtype=np.float32)
    ps = []
    for i in range(1, n + 1):
        t = i / (n + 1)
        p = '%s/%s_x%02d.png' % (outdir, tag, i)
        Image.fromarray((A * (1 - t) + B * t).astype(np.uint8)).save(p)
        ps.append(p)
    return ps


def still(png, n, out):
    if not os.path.exists(out):
        sh(['ffmpeg', '-y', '-v', 'error', '-loop', '1', '-framerate', '30', '-i', png] + ['-c:v', 'libx264', '-preset', 'ultrafast', '-crf', '17', '-pix_fmt', 'yuv420p', '-r', '30', '-g', '30', '-frames:v', str(n), out])
    return out


def slide_video(states, out_v, xf=0, workdir='/tmp', tag='s'):
    """Video senza audio da stati-immagine (con dissolvenze di xf fotogrammi); ogni stato è un clip -loop 1."""
    seq = []
    for i, (p, n) in enumerate(states):
        if i > 0 and xf > 0 and n > xf + 2:
            for q in blend_seq(states[i - 1][0], p, xf, workdir, '%s%03d' % (tag, i)):
                seq.append((q, 1))
            n -= xf
        seq.append((p, n))
    parts = []
    for k, (p, n) in enumerate(seq):
        h = hashlib.md5(('%s|%d' % (p, n)).encode()).hexdigest()[:10]
        parts.append(still(p, n, '%s/st_%s.mp4' % (workdir, h)))
    lst = out_v + '.txt'
    with open(lst, 'w') as f:
        for q in parts:
            f.write("file '%s'\n" % os.path.abspath(q))
    sh(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', out_v])
    return sum(n for p, n in seq)


def audio_filter_inputs(items, total_s):
    """items = [(wav, ritardo_s, gain_db)] -> (input args, filter_complex, label); gli ingressi audio partono dall'indice 1"""
    args = []
    fc = []
    for i, (w, d, g) in enumerate(items):
        args += ['-i', w]
    labs = []
    for i, (w, d, g) in enumerate(items):
        fc.append('[%d:a]aresample=48000,aformat=channel_layouts=stereo,volume=%fdB,adelay=%d|%d[a%d]' % (i + 1, g, int(d * 1000), int(d * 1000), i))
        labs.append('[a%d]' % i)
    if not items:
        return args, None, None
    fc.append('%samix=inputs=%d:normalize=0,apad=whole_dur=%.4f,atrim=0:%.4f[aout]' % (''.join(labs), len(items), total_s, total_s))
    return args, ';'.join(fc), '[aout]'


def clip(states, out, audio_items=(), xf=0, workdir='/tmp', tag='c'):
    """Clip da stati-immagine con audio PCM della durata esatta del video."""
    nexp = sum(n for p, n in states)
    if os.path.exists(out + '.ok') and open(out + '.ok').read().strip() == str(nexp):
        return nexp
    ov = out + '.v.mp4'
    n = slide_video(states, ov, xf, workdir, tag)
    total = n / FPS
    aargs, fc, lab = audio_filter_inputs(list(audio_items), total)
    cmd = ['ffmpeg', '-y', '-v', 'error', '-i', ov] + aargs
    if fc:
        cmd += ['-filter_complex', fc, '-map', '0:v', '-map', lab]
    else:
        cmd += ['-f', 'lavfi', '-t', '%.4f' % total, '-i', 'anullsrc=r=48000:cl=stereo', '-map', '0:v', '-map', '1:a']
    cmd += ['-c:v', 'copy'] + AENC + ['-t', '%.4f' % total, out]
    sh(cmd)
    k = nframes(out)
    assert k == n, (out, k, n)
    os.remove(ov)
    open(out + '.ok', 'w').write(str(n))
    return n


def wav_dur(p):
    return dur(p)


def silence_wav(path, secs):
    if not os.path.exists(path):
        sh(['ffmpeg', '-y', '-v', 'error', '-f', 'lavfi', '-t', '%.3f' % secs, '-i', 'anullsrc=r=48000:cl=stereo', '-c:a', 'pcm_s16le', path])
    return path
