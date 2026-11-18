# -*- coding: utf-8 -*-
# Scrive RAPPORTO_REVISIONE.md con i valori misurati (out/controlli_P*.txt, out/tl_P*.json, ecc.).   uso: python3 rapporto.py
import sys, os, json, re
sys.path.insert(0, '/tmp/claude-0/w')
from dati import *
W = '/tmp/claude-0/w'; OUT = W + '/out'
def rd(f):
    return open(f).read() if os.path.exists(f) else ''
L = []
def A(*x): L.append(' '.join(str(i) for i in x))

A('# RAPPORTO DI REVISIONE · Storia V · Lezione 4 · La Prima guerra mondiale (prof. Giorgio Mazzotti)')
A('Chat «revisione v3» (18/11/2026). Etichette: **misurato** = misura fatta sul file finale; **stima** = calcolo non verificato sul file; **non verificato** = non controllato.\n')
A(rd(OUT + '/rapporto_stato.md')); A('')
A('## 0. Punto di partenza')
A('- Per questa lezione **non esisteva nessuna consegna precedente** (nessun ramo `consegna-storia-V-lez04`) **e nessuna voce** (nessun ramo `voci-storia-V-lez04`). Ho quindi costruito la lezione **da zero** nel modello Spagnolo, partendo dal video originale del prof (release `mazzotti-storia-V`, `LEZIONE.4.LA.PRIMA.GUERRA.MONDIALE.mp4`, 1092×614, 104 min 07 s), dalle slide del prof (`LEZIONE 4.pdf`, 24 pagine), dalle sue mappe (`MAPPE LEZIONE 4.pdf`, 6 mappe), dal test (`DOMANDE LEZIONE 4.xlsx`) e dai compiti (`LEZIONE 4.pdf`).')
A('- La lezione dura 104 minuti di parlato: **esce in 3 Parti** (decisione di Sara), divise alla fine di un argomento: Parte 1 = presentazione + argomenti 1–3 · Parte 2 = argomenti 4, 5, 7(guerra totale) · Parte 3 = argomenti 6, 8, 9, 11, 10 (numeri = slide del prof). ')
A('- **Ordine degli argomenti = ordine del parlato.** Il prof parla della «guerra totale» (3619–4093 s) *prima* delle «grandi battaglie» (4094–4849 s) e del «bilancio umano» (5831–5924 s) *prima* dei «trattati di pace» (5925–6246 s), cioè in ordine diverso dalle slide. Il video segue ciò che dice. Gli 11 argomenti sono scelti sui titoli delle slide del prof.\n')
A('## 1. Misure sul video nuovo')
for P in (1, 2, 3):
    A(f'### Parte {P}')
    c = rd(f'{OUT}/controlli_P{P}.txt')
    A(c.split('| pezzo |')[0].strip() if c else '(controlli non eseguiti)')
    A('')
A('## 2. Confronto con Spagnolo Lez. 1 (punti 1–11 del modello + schede blu)')
A(rd(OUT + '/confronto.md') or '(vedi sotto)')
A('## 3. Tabella dei pezzi (sezione C della scheda tecnica): presente · minuto · durata misurata')
for P in (1, 2, 3):
    c = rd(f'{OUT}/controlli_P{P}.txt')
    if '| pezzo |' in c: A(f'### Parte {P}'); A('| pezzo |' + c.split('| pezzo |', 1)[1].split('\nfoglio')[0].strip()); A('')
A(rd(OUT + '/rapporto_corpo.md'))
open(OUT + '/RAPPORTO_REVISIONE.md', 'w').write('\n'.join(L) + '\n')
print('rapporto scritto', len('\n'.join(L)), 'caratteri')
