# Motore di montaggio Telesio · Caputi (modello Gonna). Slide a stati (PNG) + tondo + montaggio con tagli di pausa.
import json, os, subprocess, html, re
from playwright.sync_api import sync_playwright
MATERIA = 'Chimica applicata e nobilitazione dei materiali per i prodotti della moda'
CORSO = 'Tecnico Sistema Moda · III-IV anno'
DOC = 'Prof.ssa Piera Caputi'
CSS = '''
@font-face{font-family:Fig;src:url(file:///root/.fonts/Figtree-Regular.ttf)}
@font-face{font-family:FigS;src:url(file:///root/.fonts/Figtree-SemiBold.ttf)}
@font-face{font-family:FigB;src:url(file:///root/.fonts/Figtree-Bold.ttf)}
@font-face{font-family:Bri;src:url(file:///root/.fonts/BricolageGrotesque-ExtraBold.ttf)}
*{box-sizing:border-box}
html,body{margin:0;width:1920px;height:1080px;overflow:hidden;background:#fff;color:#0B1530;font-family:Fig}
.k{position:absolute;left:60px;top:34px;font:700 22px FigB;letter-spacing:.14em;color:#2060AF;text-transform:uppercase}
.rule{position:absolute;left:60px;right:60px;top:76px;height:2px;background:#CBD5E1}
.ti{position:absolute;left:60px;top:100px;width:1300px;font:800 60px/1.08 Bri;color:#2060AF}
.cards{position:absolute;left:60px;top:230px;width:1300px;display:flex;flex-direction:column;gap:22px}
.card{padding:20px 30px;border-radius:16px;background:#F4F6FA;border:3px solid #CBD5E1;font:400 34px/1.42 Fig;color:#0B1530;box-shadow:0 6px 18px rgba(30,41,59,.10);position:relative}
.card b{font-family:FigB;font-weight:700}
.card.dim{opacity:.55}
.card.on{border-color:#2060AF;background:#fff;box-shadow:0 0 0 7px #FFE600,0 6px 18px rgba(30,41,59,.12)}
.card.on:before{content:"";position:absolute;left:-40px;top:50%;width:18px;height:18px;margin-top:-9px;border-radius:50%;background:#FFE600;border:3px solid #0B1530}
.col{position:absolute;left:1440px;width:420px}
.fascia{position:absolute;left:1440px;top:300px;width:420px;background:#FFE600;border-radius:6px;padding:12px 16px;text-align:center;box-shadow:0 5px 14px rgba(30,41,59,.15)}
.fascia .n{font:700 30px FigB;color:#0B1530}.fascia .m{font:600 19px/1.25 FigS;color:#0B1530;margin-top:4px}
.kw{position:absolute;left:1440px;top:520px;width:420px}
.kw h4{margin:0 0 12px;font:700 20px FigB;letter-spacing:.12em;color:#2060AF;text-transform:uppercase}
.kw span{display:block;margin:0 0 10px;padding:8px 14px;border-radius:10px;background:#FFF3B0;border:2px solid #E0B800;font:700 28px FigB}
.foot{position:absolute;left:60px;bottom:22px;right:60px;font:600 19px FigS;color:#2060AF;letter-spacing:.04em}
.foot i{float:right;font-style:normal}
'''
def foot(pag): return f'<div class="foot">{MATERIA} · {CORSO} · {DOC}<i>Pagina {pag}</i></div>'
def slide(k, titolo, cards, on=None, mostra=None, kw=(), pag=1, extra=''):
    """cards: lista di stringhe (HTML con <b>). on: indice della card in corso. mostra: quante card visibili (default tutte fino a on)."""
    assert len(cards) <= 3
    n = (on + 1) if mostra is None and on is not None else (mostra if mostra is not None else len(cards))
    cs = ''.join(f'<div class="card{" on" if i == on else " dim" if i != on else ""}">{c}</div>' for i, c in enumerate(cards[:n]))
    kws = ''.join(f'<span>{html.escape(w)}</span>' for w in kw[:5])
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="k">{k}</div><div class="rule"></div><div class="ti">{titolo}</div><div class="cards">{cs}</div>
<div class="fascia"><div class="n">{DOC}</div><div class="m">{MATERIA}<br>{CORSO}</div></div>
<div class="kw">{"<h4>Parole chiave</h4>"+kws if kws else ""}</div>{extra}{foot(pag)}</body></html>'''
class Rend:
    def __enter__(self):
        self.p = sync_playwright().start(); self.b = self.p.chromium.launch(executable_path='/opt/pw-browsers/chromium'); self.pg = self.b.new_page(viewport={'width': 1920, 'height': 1080}); return self
    def __exit__(self, *a): self.b.close(); self.p.stop()
    def png(self, htm, out, omit_bg=False):
        f = out + '.html'; open(f, 'w').write(htm); self.pg.goto('file://' + os.path.abspath(f)); self.pg.wait_for_timeout(120)
        self.pg.screenshot(path=out, omit_background=omit_bg); os.remove(f)
def sh(c, **k): return subprocess.run(c, check=True, **k)
def durata(p): return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout)
# --- piano di taglio delle pause (solo tra frasi, > 1,2 s -> 0,6 s) ---
def piano_tagli(segs, t0, t1, soglia=1.2, resta=0.6):
    """ritorna lista di intervalli (a,b) da tenere; taglia nel mezzo delle pause lunghe a fine frase."""
    cuts = []
    for a, b in zip(segs, segs[1:]):
        g = b['inizio'] - a['fine']; tx = a['testo'].rstrip()
        if g > soglia and tx[-1:] in '.?!' and not tx.endswith('...') and t0 < a['fine'] and b['inizio'] < t1:
            tolti = g - resta; mid = a['fine'] + g / 2
            cuts.append((round(mid - tolti / 2, 3), round(mid + tolti / 2, 3)))
    keep = []; cur = t0
    for c0, c1 in cuts: keep.append((cur, c0)); cur = c1
    keep.append((cur, t1)); return keep, cuts
def nuovo_t(t, keep, t0):
    """tempo originale -> tempo nel clip montato"""
    acc = 0.0
    for a, b in keep:
        if t <= a: return acc
        if t < b: return acc + (t - a)
        acc += b - a
    return acc

TONDO = dict(x=778, y=405, w=64)  # posizione misurata sul fotogramma 852x480 (centro 810,437; r ~31)
def prof_clip(src, keep, stati, out, k, gain_db=0.0, tondo=TONDO, pos=(1586, 140), dim=128, ruotofx=''):
    """stati: [(t_orig, png)] in ordine. keep: intervalli tenuti. crea mp4 1920x1080 30fps con slide a stati + tondo + audio pulito."""
    d = os.path.dirname(os.path.abspath(out)); lst = out + '.lst'; tot = sum(b - a for a, b in keep)
    t0 = keep[0][0]; ts = [nuovo_t(t, keep, t0) for t, _ in stati] + [tot]
    with open(lst, 'w') as f:
        for i, (_, p) in enumerate(stati):
            f.write(f"file '{os.path.abspath(p)}'\nduration {max(ts[i+1]-ts[i], 0.034):.3f}\n")
        f.write(f"file '{os.path.abspath(stati[-1][1])}'\n")
    fv = ''; fa = ''
    for i, (a, b) in enumerate(keep):
        fv += f'[1:v]trim={a}:{b},setpts=PTS-STARTPTS[v{i}];'
        fa += f'[1:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.02,afade=t=out:st={max(0,b-a-0.02):.3f}:d=0.02[a{i}];'
    n = len(keep)
    fv += ''.join(f'[v{i}]' for i in range(n)) + f'concat=n={n}:v=1:a=0[vv];'
    fa += ''.join(f'[a{i}]' for i in range(n)) + f'concat=n={n}:v=0:a=1,highpass=f=80,afftdn=nr=8:nf=-40,volume={gain_db}dB,alimiter=limit=0.84:level=disabled[aa];'
    fc = (fv + fa + f"[vv]crop={tondo['w']}:{tondo['w']}:{tondo['x']}:{tondo['y']},scale={dim}:{dim}:flags=lanczos,eq=contrast=1.05:saturation=1.08,format=rgba[tv];"
          f"[2:v]format=gray[m];[tv][m]alphamerge[tc];[0:v]fps=30,format=yuv420p[bg];[bg][tc]overlay={pos[0]}:{pos[1]}:format=auto,format=yuv420p[o]")
    sh(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lst,'-i',src,'-loop','1','-i',MASK,'-filter_complex',fc,'-map','[o]','-map','[aa]',
        '-t',f'{tot:.3f}','-c:v','libx264','-preset','veryfast','-crf','18','-r','30','-c:a','aac','-b:a','192k','-ar','48000',out])
    os.remove(lst); return tot
MASK = '/home/user/work/build/mask128.png'
