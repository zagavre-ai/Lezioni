# -*- coding: utf-8 -*-
import json, sys, re, os, glob, hashlib
sys.path.insert(0, '/home/user/Lezioni/lavoro/storia-V-lez12')
import vtt as V, contenuti as C
W = '/home/user/w12'
def mm(t):
    t = round(t, 1); return f"{int(t//60)}:{t%60:04.1f}"
def tab_fine():
    out = []
    for n in (1, 2):
        tl = json.load(open(f'{W}/asm{n}/timeline.json'))['pezzi']
        out.append(f'\n**Parte {n}**\n\n| Pezzo | Inizio (min) | Fine (min) | Ultime parole del prof | Frase finita |\n|---|---|---|---|---|')
        for nome, t0, d, fr in tl:
            if not nome.startswith('prof'): continue
            j = json.load(open(f'{W}/pezzi/{nome}.json')); tb = j['tb']
            seg = [s for s in V.ASR if s['fine'] <= tb + 0.05 and s['fine'] >= tb - 1.5]
            s = seg[-1] if seg else None
            parole = ' '.join(w for _, w in s['parole'])[-60:] if s else '?'
            ok = 'sì' if s and s['testo'].strip().endswith(('.', '?', '!')) else 'da verificare'
            out.append(f"| {nome} | {mm(t0)} | {mm(t0+d)} | …{parole} | {ok} |")
    return '\n'.join(out)
def tab_voci():
    rap = json.load(open(f'{W}/rapporto_voci.json')); out = ['| Voce | Durata (s) | Somiglianza con il testo | Bordo finale (max, <0,03) | Differenze principali (trascrizione automatica) |', '|---|---|---|---|---|']
    for nome, d, sim, bf, diff in rap:
        out.append(f"| {nome} | {d:.1f} | {sim} | {bf:.3f} | {'; '.join(a+' → '+b for a,b in diff[:3]) or '—'} |")
    return '\n'.join(out)
if __name__ == '__main__':
    print(tab_fine()); print(); print(tab_voci())
