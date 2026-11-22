# prof_arg.py: costruisce il pezzo "la prof spiega" di un argomento: card sincronizzate, animazioni sopra la voce, tondo della prof.
import json, os, re, sys, html, subprocess
sys.path.insert(0, os.path.dirname(__file__))
import clip, bozza_card
from playwright.sync_api import sync_playwright
from render import render_scena
from monta import salva
import numpy as np
BOLD = []
def hcard(t):
    s = html.escape(t)
    for b in BOLD:
        s = re.sub(r'(?<![\w>])(' + re.escape(html.escape(b)) + r')(?![\w<])', r'<b>\1</b>', s, count=1, flags=re.I)
    return s
def misura(cards_html):
    with sync_playwright() as p:
        br = p.chromium.launch(executable_path='/opt/pw-browsers/chromium', args=['--no-sandbox']); pg = br.new_page(viewport={'width':1920,'height':1080})
        pg.goto('file://' + os.path.abspath(os.path.join(os.path.dirname(__file__),'prof.html'))); pg.wait_for_timeout(400)
        H = pg.evaluate("""hs=>{const c=document.getElementById('cards');c.innerHTML='';return hs.map(h=>{const e=document.createElement('div');e.className='card';e.innerHTML=h;c.appendChild(e);const r=e.getBoundingClientRect().height;return r})}""", cards_html)
        br.close()
    return H
def pack(cards, H, maxh=790, gap=20, maxn=3):
    slides = []; cur = []; h = 0
    for c, hh in zip(cards, H):
        add = hh + (gap if cur else 0)
        if cur and (len(cur) >= maxn or h + add > maxh):
            slides.append(cur); cur = []; h = 0; add = hh
        cur.append(c); h += add
    if cur: slides.append(cur)
    return slides
def costruisci(arg, subs, anims, trasc, clean_wav, src_mp4, outdir, ruolo=None, tag='a'):
    """arg: dict(t0,t1). subs: [(t_from, titolo, [parole chiave])]. anims: [(a,b,kind,params)] in tempi originali.
       ritorna dict(durata, keep, cards, slides)"""
    os.makedirs(outdir, exist_ok=True)
    x = clip.leggi_wav(clean_wav)
    keep, cut = clip.intervalli(trasc, x, arg['t0'], arg['t1'])
    M, D = clip.mappa_tempi(keep); nfr = int(round(D*30)); D = nfr/30
    fr = bozza_card.frasi(trasc, arg['t0'], arg['t1'])
    cards = [dict(t0=round(clip.orig2nuovo(M, f['t0']), 3), h=hcard(f['testo']), testo=f['testo'], o0=f['t0'], o1=f['t1']) for f in fr]
    for i, c in enumerate(cards): c['t1'] = cards[i+1]['t0'] if i+1 < len(cards) else D
    H = misura([c['h'] for c in cards]); 
    for c, h in zip(cards, H): c['alt'] = h
    sl = pack(cards, H)
    slides = []
    for i, g in enumerate(sl):
        t0 = max(0.0, g[0]['t0'] - 0.35)
        if slides: t0 = max(t0, slides[-1]['t1'])
        t1 = sl[i+1][0]['t0'] - 0.35 if i+1 < len(sl) else D
        # titolo e parole chiave dal sotto-argomento a cui appartiene la prima card
        sub = [s for s in subs if s[0] <= g[0]['o0'] + 0.01][-1] if subs else (0, '', [])
        slides.append(dict(t0=round(t0,3), t1=round(t1,3), title=sub[1], chiave=sub[2][:5], cards=[dict(t0=c['t0'], t1=c['t1'], h=c['h']) for c in g]))
    an = []
    for a, b, k, p in anims:
        p = dict(p); t0n = clip.orig2nuovo(M, a)
        if 'so' in p: p['steps'] = [round(clip.orig2nuovo(M, t) - t0n, 3) for t in p.pop('so')]
        an.append(dict(t0=round(t0n,3), t1=round(clip.orig2nuovo(M, b),3), kind=k, **p))
    dati = dict(kicker='LA PROFESSORESSA SPIEGA', slides=slides, anims=an)
    json.dump(dati, open(f'{outdir}/{tag}_dati.json','w'), ensure_ascii=False)
    json.dump(dict(keep=keep, cut=cut, D=D, M=M), open(f'{outdir}/{tag}_tempi.json','w'))
    return dict(D=D, nfr=nfr, keep=keep, dati=dati, cards=cards, M=M)
def rendi(res, src_mp4, clean_wav, outdir, tag='a'):
    D = res['D']; keep = res['keep']
    x = clip.leggi_wav(clean_wav)
    clip.audio_taglio(x, keep, f'{outdir}/{tag}_prof.wav')
    clip.video_tondo(src_mp4, keep, f'{outdir}/{tag}_tondo.mp4')
    n, nshot = render_scena(os.path.join(os.path.dirname(__file__),'prof.html'), res['dati'], D, f'{outdir}/{tag}_scena.mp4')
    return n, nshot

def composita(outdir, tag='a'):
    here = os.path.dirname(__file__)
    subprocess.run(['ffmpeg','-v','error','-y','-i',f'{outdir}/{tag}_scena.mp4','-i',f'{outdir}/{tag}_tondo.mp4','-loop','1','-i',os.path.join(here,'maschera.png'),
      '-filter_complex','[1:v][2:v]alphamerge[c];[0:v][c]overlay=1488:158:shortest=1,format=yuv420p[o]','-map','[o]','-r','30','-c:v','libx264','-preset','veryfast','-crf','19',f'{outdir}/{tag}.mp4'],check=True)
