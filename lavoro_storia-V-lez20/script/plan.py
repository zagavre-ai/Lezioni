import sys, json, os, wave, numpy as np
sys.path.insert(0, '/tmp/w/b')
from vpieces import *
import states as ST

META = json.load(open('/tmp/w/b/ch/meta.json')) if os.path.exists('/tmp/w/b/ch/meta.json') else {}
SIGLA = KIT + '/sigle/Sigla_Storia_15s.mp4'
SIGF = KIT + '/sigle/Sigla_finale_5s_con_avviso_diritti.mp4'
PROV = {}  # voci provvisorie: nome -> testo

def silence(name, words):
    """voce provvisoria: silenzio della durata stimata (parole / 2,5 al secondo)"""
    out = f'/tmp/w/b/aud/prov_{name}.wav'; os.makedirs('/tmp/w/b/aud', exist_ok=True)
    if os.path.exists(f'/tmp/w/vox/{name}.wav'):
        from audio import prep_voice
        PROV.pop(name, None); return prep_voice(name)
    d = max(2.0, words / 2.5)
    with wave.open(out, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(48000); w.writeframes(np.zeros((int(d * 48000), 2), np.int16).tobytes())
    PROV[name] = dict(durata_stimata=round(d, 1)); return out

TXT_NEW = {
 'SP0': "Prima di continuare, facciamo un ripasso di tutto quello che abbiamo visto nella parte precedente, argomento per argomento.",
 'FINP1': "La prima parte finisce qui. Nella parte successiva trovi gli ultimi argomenti, il glossario, la verifica finale e i compiti.",
 'PS2_4': "Dopo la Guerra del Golfo Bush Senior non depone Saddam Hussein: per molti conservatori americani è stato troppo leggero, e non viene rieletto.",
 'PS3_4': "In Kosovo la NATO interviene anche senza il permesso dell'ONU; alla fine Milosevic viene arrestato e portato davanti alla Corte penale internazionale.",
}
COMPITI = json.load(open('/tmp/w/old/compiti.json'))['esercizi']

def sigla_piece(name, clip, part, overlay=None, first=None):
    f = first or (B + '/png/' + os.path.basename(clip).replace('.mp4', '_first.png'))
    from audio import dur
    return Piece(name, [(0, f)], fixed_total=round(dur(clip) * 30) / 30, video_clip=clip, trans=False, part=part, overlay=overlay)

def cover_kore(part=1):
    # voce di benvenuto provvisoria: INTRO1 (contiene il nome del prof: da sostituire con INTRO1_N)
    voice = 'INTRO1'
    if os.path.exists('/tmp/w/vox/INTRO1_N.wav'): voice = 'INTRO1_N'
    else: PROV['INTRO1_N'] = dict(provvisoria_con='INTRO1 (dice il nome del prof)')
    wav = prep_voice(voice); D = dur(wav) + 0.6
    S, ts = sentence_times(voice, TV[voice])
    lead = 0.8; states = [(0, want(cover_html(0), 'cov0'))]
    # le voci degli argomenti compaiono lungo la seconda frase
    t1 = lead + (ts[1] if len(ts) > 1 else 5); t2 = lead + (ts[2] if len(ts) > 2 else 20)
    for i in range(1, 9):
        t = t1 + (t2 - t1) * (i - 1) / 8.0 * 0.95
        states.append((t, want(cover_html(i), f'cov{i}')))
    pc = Piece('COVER', states, audio=wav, D=D, part=part, fade_in='black')
    fin = TXT_NEW.get('INTRO1_N') or TV[voice].replace(' del professor Giorgio Mazzotti', '')
    S2, t2s = sentence_times(voice, fin); pc.subtitle = subs_from([digits(x) for x in S2], t2s, lead, D - 0.6)
    return pc

def prof_piece(name, reg, part, cam=True):
    m = META[name]
    c = CHUNKS[name]
    if c.get('kind') == 'cover':
        sts = [(0, want(cover_html(8, cam=True), 'cov_cam'))]; d = m['dur']
    elif c.get('kind') == 'argomenti':
        sts = [(0, want(argomenti_slide(None), 'argom_cam'))]; d = m['dur']
    else:
        sts, d = ST.prof_states(name, m, reg)
    return Piece(name, sts, audio=f'/tmp/w/b/ch/{name}.wav', D=d, cam=f'/tmp/w/b/ch/{name}_cam.mp4', part=part)

def ap_piece(k, part):
    return reveal_piece(f'AP{k}', 'APPROFONDIMENTO', '', f'AP{k}', part=part)

def build_part1():
    reg = ST.Reg(3); P = []
    P.append(sigla_piece('SIGLA1', SIGLA, 1))
    P.append(cover_kore())
    P.append(prof_piece('D0', reg, 1)); P.append(prof_piece('D1', reg, 1))
    for k in (1, 2, 3, 4):
        P.append(tpiece(k, 1))
        if k == 1:
            P.append(prof_piece('A1a', reg, 1))
            P.append(reveal_piece('AN1a', 'APPROFONDIMENTO', 'La fine dell\'Unione Sovietica', 'AN1a', part=1))
            P.append(prof_piece('A1b', reg, 1))
        elif k == 3:
            P.append(prof_piece('A3a', reg, 1))
            P.append(ap_piece(3, 1))
            P.append(prof_piece('A3b', reg, 1))
            P.append(reveal_img_piece('AN3a', 'APPROFONDIMENTO', "La carta dell'ex Iugoslavia", 'AN3a', 'iugoslavia', part=1))
        else:
            P.append(prof_piece(f'A{k}', reg, 1))
        if k != 3: P.append(ap_piece(k, 1))
        # mappa
        mp = {3: 1, 4: 2}.get(k)
        if mp: p, _ = map_prof_piece(mp, 1); p.name = f'MAP{k}'; P.append(p)
        extra = {}
        if k == 2:
            extra = {'PS2_4': silence('PS2_4', len(TXT_NEW['PS2_4'].split())), 'PS2_4_t': TXT_NEW['PS2_4']}; PROV['PS2_4']['testo'] = TXT_NEW['PS2_4']
        if k == 3:
            extra = {'PS3_4': silence('PS3_4', len(TXT_NEW['PS3_4'].split())), 'PS3_4_t': TXT_NEW['PS3_4']}; PROV['PS3_4']['testo'] = TXT_NEW['PS3_4']
        P.append(pill_piece(k, 1, extra))
        P.append(qpiece(k, 1))
    # fine Parte 1
    w = silence('FINP1', len(TXT_NEW['FINP1'].split())); PROV['FINP1']['testo'] = TXT_NEW['FINP1']
    png = want(dark_html('FINE DELLA PRIMA PARTE', 'Ci vediamo nella seconda parte', lines=['Gli ultimi argomenti', 'Il glossario e la verifica finale', 'I compiti'], tpx=78, top=470), 'finp1')
    P.append(Piece('FINP1', [(0, png)], audio=w, D=dur(w) + 0.5, part=1))
    P.append(sigla_piece('SIGF1', SIGF, 1, overlay=B + '/assets/avviso.png'))
    return P, reg

def build_part2():
    reg = ST.Reg(2); P = []
    P.append(sigla_piece('SIGLA2', SIGLA, 2))
    # spiegone della Parte 1
    w = silence('SP0', len(TXT_NEW['SP0'].split())); PROV['SP0']['testo'] = TXT_NEW['SP0']
    png = want(dark_html('RIPASSO DELLA PARTE PRECEDENTE', 'Prima di continuare: che cosa abbiamo visto', lines=[a['nome'] for a in ARGS[:5]], tpx=70, lpx=40, top=420), 'sp0')
    P.append(Piece('SP0', [(0, png)], audio=w, D=dur(w) + 0.5, part=2, fade_in='black'))
    imgs = {1: ('cecenia', None), 2: ('kuwait', None), 3: ('iugoslavia', B + '/png/mapp1_fin.png'),
            4: ('ue', B + '/png/mapp2_fin.png'), 5: ('ritratti', B + '/png/mapp3_fin.png')}
    for a in range(1, 6):
        i, m = imgs[a]
        P.append(spiegone_piece(a, 2, m, i))
    for k in (5, 6, 7, 8):
        P.append(tpiece(k, 2)); P.append(prof_piece(f'A{k}', reg, 2)); P.append(ap_piece(k, 2))
        mp = {5: 3, 8: 4}.get(k)
        if mp: p, _ = map_prof_piece(mp, 2); p.name = f'MAP{k}'; P.append(p)
        P.append(pill_piece(k, 2)); P.append(qpiece(k, 2))
    # glossario, ripasso finale, mappa finale
    P.append(reveal_piece('GLOSS', 'GLOSSARIO', 'Le parole da ricordare', 'RGL1', part=2, skip_first=True))
    for a in range(1, 9): P.append(reveal_piece(f'RF{a}', f'RIPASSO FINALE · ARGOMENTO {a}', ARGS[a - 1]['nome'], f'R{a}', part=2, skip_first=False, tpx=66))
    P.append(reveal_piece('RFIN', 'RIPASSO FINALE', 'La lezione in breve', 'RF1', part=2, skip_first=False))
    P.append(reveal_piece('FIN', 'PER OGGI È TUTTO', 'Ora tocca a te', 'FIN1', part=2, skip_first=False))
    # verifica di sbarramento
    ver = json.load(open('/tmp/w/old/verifica_finale.json'))
    png = want(dark_html('VERIFICA FINALE', 'Verifica di sbarramento', lines=[f"{len(ver['domande'])} domande", "Per superarla serve almeno l'80% di risposte giuste"], tpx=84, lpx=44, top=470), 'verifica')
    P.append(Piece('VERIFICA', [(0, png)], lead=0, tail=0.5, trans=False, mixes=[(KIT + '/suoni/quiz.wav', 0.5, 0.0)], fixed_total=6.0, part=2))
    P.append(sigla_piece('SIGF2', SIGF, 2, overlay=B + '/assets/avviso.png'))
    # compiti
    png = want(dark_html('COMPITI', 'Compiti', tpx=110), 'compiti_intro')
    P.append(Piece('COMPITI', [(0, png)], lead=0, tail=0.5, trans=False, mixes=[(KIT + '/suoni/titolo.wav', 0.3, 0.0)], fixed_total=3.5, part=2, fade_in='black'))
    for e in COMPITI:
        t = e['testo'].replace('Elcin', 'Eltsin').replace('No- Global', 'No-Global')
        w = silence(f"COMP{e['n']}", len(t.split())); PROV[f"COMP{e['n']}"]['testo'] = t
        png = want(dark_html('COMPITI', f"Esercizio {e['n']}", lines=[t], active=0, tpx=72, lpx=44, top=330), f"comp{e['n']}")
        P.append(Piece(f"COMP{e['n']}", [(0, png)], audio=w, D=dur(w) + 0.5, part=2))
    return P, reg
