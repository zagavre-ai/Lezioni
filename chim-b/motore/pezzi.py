# -*- coding: utf-8 -*-
import os, sys, json, re, html, subprocess, random
sys.path.insert(0, os.path.dirname(__file__))
import monta, maps
HERE = os.path.dirname(os.path.abspath(__file__)); PZ = os.path.join(HERE, 'pezzi.html')
class Ctx:  # cartelle di lavoro
    def __init__(s, lav, vox, img, out): s.lav=lav; s.vox=vox; s.img=img; s.out=out; s.prova=set()
def stima(testo): return max(1.2, len(testo.split()) * 0.42 + 0.4)
def voce(ctx, nome, testo=None):
    """percorso wav normalizzato della voce; se manca (solo per le prove) genera un segnaposto silenzioso e lo segna."""
    dst = f'{ctx.lav}/voxn/{nome}.wav'; os.makedirs(os.path.dirname(dst), exist_ok=True)
    src = f'{ctx.vox}/{nome}.wav'
    if os.path.exists(src): return monta.norm_voce(src, dst)
    ctx.prova.add(nome); d = stima(testo or nome); ph = f'{ctx.lav}/segnaposto/{nome}.wav'; os.makedirs(os.path.dirname(ph), exist_ok=True)
    if not os.path.exists(ph): subprocess.run(['ffmpeg','-v','error','-y','-f','lavfi','-i',f'anullsrc=r=48000:cl=stereo','-t',f'{d:.2f}','-c:a','pcm_s16le',ph],check=True)
    return ph
def img(ctx, nome):
    p = f'{ctx.img}/{nome}.png'; return ('file://' + p) if os.path.exists(p) else ''
def esc(t): return html.escape(t)
def frasi_voce(testo):
    return [s.strip() for s in re.split(r'(?<=[\.\?\!])\s+', testo) if s.strip()]
def _durate(wavs): return [monta.dur_wav(w) for w in wavs]
def fai(ctx, nome, dati, wavs, lead=1.0, gap=0.6, coda=1.6, jingles=(), extra_t=None):
    d = _durate(wavs); st, t = monta.piano(d, lead, gap)
    dati = dict(dati); dati['steps'] = st
    durata = (t if extra_t is None else extra_t) + coda
    voci = [(s[0], w) for s, w in zip(st, wavs)]
    out = f'{ctx.out}/{nome}'
    monta.pezzo(out, PZ, dati, durata, voci, [(a,b,c) for a,b,c in jingles])
    return durata
# --- builders
def titolo(ctx, k, tit, imgname):
    w = voce(ctx, f'T{k}_TIT', tit)
    return fai(ctx, f'T{k}', dict(kind='titolo', titolo=tit, img=img(ctx, imgname)), [w], lead=1.0, coda=1.8, jingles=[(0.0,'titolo.wav',1.0)])
def approf(ctx, k, testo, imgname, tit_arg):
    fr = frasi_voce(testo); w = voce(ctx, f'P{k}_APP', testo); d = monta.dur_wav(w)
    # prima frase = domanda; le altre in card, con tempi proporzionali ai caratteri
    lead = 1.0; tot = sum(len(f) for f in fr); t = lead; segs = []
    for f in fr: dd = d * len(f) / tot; segs.append((t, t+dd)); t += dd
    cards = [dict(h=esc(f), t0=round(a,2), t1=round(b,2)) for f,(a,b) in zip(fr[1:], segs[1:])]
    dati = dict(kind='approf', domanda=fr[0], frasi=cards, img=img(ctx, imgname))
    return fai(ctx, f'P{k}', dati, [w], lead=lead, coda=2.0)
def pillola(ctx, k, righe, tit):
    ws = [voce(ctx, f'R{k}_{j}', r) for j, r in enumerate(righe, 1)]
    return fai(ctx, f'R{k}', dict(kind='pillola', titolo=tit, righe=[esc(r) for r in righe]), ws, lead=1.0, gap=0.8, coda=2.0, jingles=[(0.0,'repaso.wav',1.0)])
def quiz_scheda(ctx, k):
    out = f'{ctx.out}/QS{k}'; dur = 3.5
    monta.pezzo(out, PZ, dict(kind='qscheda', steps=[]), dur, [], [(0.5,'quiz.wav',1.0)])  # scatto del jingle a +0,5 s
    return dur
def quiz_dom(ctx, k, i, q, giusta, sbagliate, sp, kicker):
    rnd = random.Random(k*100+i); opz = sbagliate[:] ; pos = rnd.randrange(4); opz.insert(pos, giusta)
    wq = voce(ctx, f'Q{k}_{i}_Q', q); ws = voce(ctx, f'Q{k}_{i}_S', 'La risposta giusta: ' + giusta + '. ' + sp)
    dq = monta.dur_wav(wq); ds = monta.dur_wav(ws)
    # piano: voce domanda, opzioni, pausa per pensare 6 s, voce spiegazione
    lead = 0.8; tq = lead; ts = tq + dq + 0.5 + 4*0.35 + 6.0
    st = [[tq, dq], [ts, ds]]
    dati = dict(kind='dom', kicker=kicker, num=f'DOMANDA {i} DI 5', q=q, opz=[esc(o) for o in opz], giusta=pos, sp='<b style="font-family:FigB">Risposta giusta: </b>'+esc(giusta)+'.<br>'+esc(sp), steps=st)
    durata = ts + ds + 1.8
    out = f'{ctx.out}/Q{k}_{i}'
    monta.pezzo(out, PZ, dati, durata, [(tq, wq), (ts, ws)], [])
    return durata
def mappa(ctx, k, voci_nomi, voci_testi, nodi, tit, kicker, tenuta=4.0):
    ws = [voce(ctx, n, t) for n, t in zip(voci_nomi, voci_testi)]
    d = _durate(ws); st, t = monta.piano(d, 1.2, 0.9)
    dati = dict(kind='mappa', kicker=kicker, nodi=nodi, steps=st, tenuta=tenuta)
    durata = t + tenuta
    monta.pezzo(f'{ctx.out}/M{k}', PZ, dati, durata, [(s[0], w) for s, w in zip(st, ws)], [])
    return durata
