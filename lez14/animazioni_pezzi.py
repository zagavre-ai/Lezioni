# -*- coding: utf-8 -*-
# Definizione dei pezzi (eseguito da animazioni.py: usa X, card, scena, num, icona, ... definiti li').
# Ogni funzione riceve il Pezzo P, ritorna (kicker, [scene_html]) o (kicker, [scene], [(a,b) scene scure]).
# I tempi vengono dalle parole della voce: a = P.v(i)  ->  a('parola', nth, dopo, pre).
K1 = 'Il dopoguerra e la nuova geopolitica'
K2 = 'Bretton Woods e il bipolarismo'
K3 = 'La dottrina Truman, il piano Marshall e Berlino'
K4 = "L'Europa del blocco occidentale"
K5 = 'Gli Stati Uniti negli anni Cinquanta'
K6 = 'Il blocco orientale e la destalinizzazione'
K7 = 'La guerra fredda in Asia'
def anello(t0, x, y, col, s=380):
    return X(f'<div style="width:{s}px;height:{s}px;border:12px solid {col};border-radius:50%"></div>', t0, 'abs', f'left:{x}px;top:{y}px', a='ring', d=2.4)
def limiti(P, i, *tt):
    """confini di scena: inizio voce, i tempi dati, fine voce (+0.5 di coda)"""
    v = P.v(i); return [P.off[i] - P.LEAD if i == 0 else v.inizio - 0.2] + list(tt) + [v.fine + (0.55 if i == len(P.voci) - 1 else 0.5)]

@pezzo('AN1_1', ['AN1'])
def AN1_1(P):
    a = P.v(0)
    b = limiti(P, 0, a("Nell'agosto", pre=0.35), a('vincitori', pre=0.3), a('San', pre=0.4), a('millenovecentoquarantotto', pre=0.5))
    s = []
    s.append(scena(b[0], b[1], 'Cinquanta milioni di morti', riga([
        colonna([num(0, 50, a('cinquanta', pre=1.0), d=1.8), X('milioni di morti', a('cinquanta', pre=0.2), 'lab', a='up')]),
        colonna([persone(30, a('cinquanta', pre=0.3), a('civili', pre=0.2), cols=10, s=64),
                 card('Soprattutto civili', '', 'pesca', a('civili', pre=0.15), w=620, hl=[(a('civili', pre=0.15), b[1])])], 'gap:30px')], 'gap:110px')))
    s.append(scena(b[1], b[2], "Agosto 1945: comincia l'era nucleare", colonna([
            X('Agosto 1945', a("Nell'agosto", pre=0.1), 'pillbox', a='left'),
            card('', 'Le bombe atomiche statunitensi sul Giappone', 'cel', a('bombe', pre=0.1), w=1080),
            card('', "Si apre l'era nucleare", 'lil', a("l'era", pre=0.1), w=1080),
            card('', "Per ora solo gli Stati Uniti hanno l'atomica", 'pag', a('ora', pre=0.4), w=1080, hl=[(a('ora', pre=0.4), b[2])])], 'align-items:flex-start'),
        extra=anello(b[1] + 0.2, 120, 420, '#E8825A') + anello(b[1] + 1.4, 120, 420, '#FFE600') + icona('atomo', b[1] + 0.3, TEL, 230, style='position:absolute;left:195px;top:495px', fl=5),
        bstyle='left:620px;width:1220px;align-items:flex-start'))
    s.append(scena(b[2], b[3], 'Un ordine fondato sulla giustizia', riga([
        icona('bilancia', b[2] + 0.2, TEL, 210, fl=4),
        colonna([riga([card('Norimberga', 'Tribunale internazionale', 'cel', a('Norimberga', pre=0.15), w=520, hl=[(a('Norimberga', pre=0.15), a('Tokyo', pre=0.15))]),
                       card('Tokyo', 'Tribunale internazionale', 'cel', a('Tokyo', pre=0.15), w=520, hl=[(a('Tokyo', pre=0.15), a('processano', pre=0.1))])]),
                 card('', 'Processano i responsabili della guerra', 'pesca', a('processano', pre=0.15), w=1080)])], 'gap:60px')))
    s.append(scena(b[3], b[4], '1945: nasce l\'ONU', riga([
        colonna([X('1945', a('San', pre=0.3), 'num', a='pop'), X('San Francisco', a('San', pre=0.1), 'lab', a='up')]),
        colonna([icona('globo', a('Organizzazione', pre=0.2), TEL, 150, fl=4),
                 sig('ONU', a('Organizzazione', pre=0.1)),
                 card('', 'Mantenere la pace e la sicurezza nel mondo', 'men', a('mantenere', pre=0.1), w=900)])], 'gap:110px')))
    s.append(scena(b[4], b[5], '1948: i diritti umani', riga([
        colonna([X('1948', b[4] + 0.4, 'num', a='pop')]),
        colonna([card('Dichiarazione universale dei diritti umani', '', 'lil', a('Dichiarazione', pre=0.15), w=1000),
                 card('', 'Nessun individuo può essere considerato superiore agli altri', 'pag', a('nessun', pre=0.1), w=1000, hl=[(a('nessun', pre=0.1), b[5])])])], 'gap:100px')))
    return K1, s

# ------------------------------------------------------------------ helper in piu'
def nodo(testo, col, t0, w=None, hl=None, fl=3, sub='', **k):
    f, b = PAL[col]
    st = f'background:{f};border-color:{b};' + (f'width:{w}px;' if w else '')
    return X(e(testo) + (f'<div class="sub" style="font-weight:500;font-size:34px;margin-top:8px">{sub}</div>' if sub else ''), t0, 'pnode', st, hl=hl, fl=fl, **k)
def pila(w, h, items): return f'<div style="position:relative;width:{w}px;height:{h}px">' + ''.join(items) + '</div>'
def tit_a(t0, testo, **k): return X(testo, t0, 'pillbox', a='left', **k)
def MAPPA(nome, ritaglio, canc, w, h):
    return mappa_img(nome, ritaglio, canc)
def linea_svg(punti, vb, t0, d=1.2, col='#E0354B', wd=18, dash='', hl=None):
    p = 'M' + ' L'.join(f'{x} {y}' for x, y in punti)
    return X(f'<svg viewBox="0 0 {vb[0]} {vb[1]}" style="position:absolute;left:0;top:0;width:100%;height:100%"><path d="{p}" fill="none" stroke="{col}" stroke-width="{wd}" stroke-linecap="round" stroke-linejoin="round" {dash}/></svg>',
             t0, 'abs', 'left:0;top:0;width:100%;height:100%', a='draw', d=d)
def mk(x, y, w, h, t0, t1=None, rect=False, lab='', lx=0, ly=0):
    s = X('', t0, 'mk' + (' r' if rect else ''), f'left:{x}%;top:{y}%;width:{w}%;height:{h}%', a='pop', d=0.45, t1=t1)
    if lab: s += X(e(lab), t0 + 0.1, 'mkl', f'left:{x + lx}%;top:{y + ly}%', a='pop', d=0.4, t1=t1)
    return s
def voto(t_si, t_no, x, label_si='SÌ', label_no='NO'):
    si = X(label_si, t_si, 'vt', 'background:#CDEFD9;border-color:#3FA66B', t1=t_no if t_no else None, fl=3)
    no = X(label_no, t_no, 'vt', 'background:#FFD9C2;border-color:#E8825A', fl=0) if t_no else ''
    return f'<div style="position:relative;width:150px;height:150px">{si}{no}</div>'
CSS += """
.vt{position:absolute;left:0;top:0;width:150px;height:150px;border:6px solid;border-radius:50%;display:flex;align-items:center;justify-content:center;font:800 54px Bri}
"""

# ------------------------------------------------------------------ ARGOMENTO 1 (seconda parte)
@pezzo('AN1_2', ['AN2', 'AN3'])
def AN1_2(P):
    a = P.v(0); c = P.v(1)
    b = limiti(P, 0, a('primo', pre=0.3), a('Sono', nth=3, pre=0.3))
    s = []
    s.append(scena(b[0], b[1], 'Norimberga e Tokyo: tre concetti nuovi', riga([
        num(0, 3, a('compaiono', pre=0.2), d=1.4, style='font-size:260px'),
        colonna([icona('bilancia', a('Norimberga', pre=0.3), TEL, 200, fl=4),
                 card('', 'Per la prima volta nei processi di Norimberga e di Tokyo', 'cel', a('processi', pre=0.1), w=1000)])], 'gap:120px')))
    xs = [('Il primo', 'primo'), ('Il secondo', 'secondo'), ('Il terzo', 'terzo')]
    cs = [('Crimini di guerra', '', 'pesca', 'primo', 'secondo'), ("Crimini contro l'umanità", 'come lo sterminio dei civili', 'lil', 'secondo', 'terzo'),
          ('Crimini contro la pace', 'è colpevole chi scatena una guerra', 'pag', 'terzo', 'Sono')]
    cards = []
    for i, (t_, c_, col, w0, w1) in enumerate(cs):
        t0 = a(w0, pre=0.3); t1 = a(w1, pre=0.3) if w1 != 'Sono' else b[2]
        cards.append(colonna([X(str(i + 1), t0, 'big', a='pop'), card(t_, c_, col, t0 + 0.15, w=540, hl=[(t0 + 0.15, t1)])], 'gap:14px'))
    s.append(scena(b[1], b[2], 'Tre concetti giuridici nuovi', riga(cards, 'align-items:flex-start;gap:40px')))
    s.append(scena(b[2], b[3], 'Processi criticati, ma con prove inconfutabili', riga([
        card('Giudici delle nazioni vincitrici', 'Per questo qualcuno li ha criticati', 'pesca', a('giudici', pre=0.2), w=700),
        X('ma', a('ma', pre=0.0), 'big', a='pop'),
        card('Durano mesi', 'Portano alla luce prove inconfutabili', 'men', a('durano', pre=0.2), w=700)], 'gap:40px')))
    d = limiti(P, 1, c('Gli', pre=0.5), c('Ognuno', pre=0.4))
    s.append(scena(d[0], d[1], "Il Consiglio di Sicurezza dell'ONU", riga([
        num(0, 5, c('cinque', pre=0.9), d=1.2, style='font-size:260px'),
        colonna([X('membri permanenti', c('cinque', pre=0.4), 'lab', a='up'), sig('ONU', c('Consiglio', pre=0.0)),
                 card('', 'Le nazioni che si sono opposte al fascismo senza ambiguità', 'cel', c('nazioni', pre=0.1), w=1000)], 'align-items:flex-start')], 'gap:110px')))
    pa = [('Stati Uniti', 'Stati'), ('Unione Sovietica', 'Unione'), ('Regno Unito', 'Regno'), ('Francia', 'Francia'), ('Cina', 'Cina')]
    row = []
    for i, (n, w) in enumerate(pa):
        t0 = c(w, pre=0.25) if w != 'Stati' else c('Gli', pre=0.3)
        sub = 'allora guidata dai nazionalisti' if n == 'Cina' else ''
        row.append(colonna([icona('stella', t0, TEL, 90, fl=3), nodo(n, 'cel', t0 + 0.1, w=320, sub=sub, hl=[(t0 + 0.1, t0 + 1.6)])], 'gap:14px;align-items:center'))
    s.append(scena(d[1], d[2], 'Cinque membri permanenti', riga(row, 'gap:26px;align-items:flex-start')))
    t_no = c('uno', nth=0, dopo='basta', pre=0.2)
    s.append(scena(d[2], d[3], 'Il diritto di veto', colonna([
        riga([voto(c('Ognuno', pre=0.1), None, 0), voto(c('Ognuno', pre=0.1) + 0.15, None, 0), voto(c('Ognuno', pre=0.1) + 0.3, None, 0), voto(c('Ognuno', pre=0.1) + 0.45, None, 0), voto(c('Ognuno', pre=0.1) + 0.6, t_no, 0, 'SÌ', 'NO')], 'gap:40px'),
        card('Basta il no di uno solo dei cinque', 'e una risoluzione non passa', 'pesca', c('basta', pre=0.3), w=1100),
        card('', 'La concordia tra le nazioni non è davvero paritaria', 'pag', c('Per', nth=0, dopo='risoluzione', pre=0.2), w=1100)])))
    return K1, s

# ------------------------------------------------------------------ ARGOMENTO 2
@pezzo('AN2_1', ['AN4'])
def AN2_1(P):
    a = P.v(0)
    b = limiti(P, 0, a('Il', nth=0, dopo='riferimento', pre=0.0) if False else a('dollaro', pre=0.6), a('Nasce', pre=0.3), a("L'idea", pre=0.3))
    s = []
    s.append(scena(b[0], b[1], 'Bretton Woods: un nuovo sistema monetario', riga([
        num(1944, 1944, a('Bretton', pre=1.6), sep=False, style='font-size:250px'),
        card('', 'Gli accordi di Bretton Woods ridisegnano il sistema monetario mondiale', 'cel', a('accordi', pre=0.2), w=860),
        ], 'gap:90px')))
    s.append(scena(b[1], b[2], 'Il dollaro diventa la valuta di riferimento', riga([
        nodo('Sterlina britannica', 'bia', a('sterlina', pre=0.3), w=560, sub='prima era lei la valuta internazionale'),
        freccia(a('sterlina', pre=0.1), 0.8, w=200),
        nodo('Dollaro americano', 'pag', a('dollaro', pre=0.1), w=560, sub='valuta internazionale di riferimento', hl=[(a('dollaro', pre=0.1), b[2])])], 'gap:40px') if False else
        riga([nodo('Dollaro americano', 'pag', a('dollaro', pre=0.1), w=620, sub='diventa la valuta internazionale di riferimento', hl=[(a('dollaro', pre=0.1), a('prima', pre=0.1))]),
              X('prima:', a('prima', pre=0.1), 'lab', a='up'),
              nodo('Sterlina britannica', 'bia', a('sterlina', pre=0.2), w=620, sub='era la valuta di riferimento')], 'gap:40px')))
    s.append(scena(b[2], b[3], 'Fondo Monetario Internazionale e Banca Mondiale', colonna([
        sig('FMI', a('Fondo', pre=0.1)),
        riga([card('Fondo Monetario Internazionale', 'Una nazione in crisi non deve più indebitarsi con altre nazioni', 'cel', a('Fondo', pre=0.1), w=820),
              card('Banca Mondiale', 'Concede prestiti agevolati', 'men', a('Banca', pre=0.2), w=820)], 'align-items:stretch;gap:50px')])))
    s.append(scena(b[3], b[4], "L'idea: evitare un'altra crisi come quella del 1929", riga([
        card('Crisi del 1929', '', 'lil', a('millenovecentoventinove', pre=0.5), w=480),
        freccia(a('dittature', pre=0.5), 0.8, w=190),
        card('Dittature', 'come quella di Hitler', 'pesca', a('dittature', pre=0.3), w=520),
        ], 'gap:30px') ))
    return K2, s

@pezzo('AN2_2', ['AN5', 'AN6'])
def AN2_2(P):
    a = P.v(0); c = P.v(1)
    b = limiti(P, 0, a('Negli', pre=0.3), a('Ognuno', pre=0.3))
    s = []
    def gg(t0, t1, nome, col, sub):
        return None
    s.append(scena(b[0], b[1], 'Un mondo bipolare: due superpotenze', riga([
        colonna([nodo('Stati Uniti', 'cel', a('superpotenze', pre=1.2), w=520, fl=4)]),
        colonna([X('lontane per', a('lontane', pre=0.1), 'sub', a='up'), chip('geografia', a('geografia', pre=0.15)), chip('ideologia', a('ideologia', pre=0.15)), chip('sistemi produttivi', a('sistemi', pre=0.15))], 'gap:14px'),
        colonna([nodo('Unione Sovietica', 'pesca', a('superpotenze', pre=0.9), w=520, fl=4)])], 'gap:60px')))
    rows = [('Politica', 'Democrazia parlamentare', 'Regime totalitario a partito unico', a('Negli', pre=0.2)),
            ('Ideologia', 'Capitalismo', 'Comunismo', a('Da', nth=0, dopo='partito', pre=0.2)),
            ('Economia', 'Proprietà privata', 'Pianificazione dello Stato', a('americani', pre=0.5))]
    hdr = riga([X('', b[1], 'sub', 'width:300px'), X('Stati Uniti', b[1] + 0.2, 'lab', 'width:600px;text-align:center'), X('Unione Sovietica', b[1] + 0.3, 'lab', 'width:600px;text-align:center')], 'gap:30px')
    tr = ''.join(riga([X(r0, t0, 'lab', 'width:300px;font-size:44px'), card('', r1, 'cel', t0, w=600, fl=2), card('', r2, 'pesca', t0 + 0.2, w=600, fl=2)], 'gap:30px') for r0, r1, r2, t0 in rows)
    s.append(scena(b[1], b[2], 'Due modelli opposti', colonna([hdr.replace('b[1]', ''), tr], 'gap:22px')))
    s.append(scena(b[2], b[3], "L'Europa divisa tra i due eserciti", riga([
        X('<div style="display:flex;width:1500px;height:340px;border-radius:30px;overflow:hidden;box-shadow:0 10px 26px rgba(60,70,90,.2);border:5px solid #C9D3E3">'
          '<div style="flex:1;background:#CFE8FB;padding:36px"><div class="big">Occidente</div><div class="sub" style="margin-top:12px">agli americani</div></div>'
          '<div style="flex:1;background:#FFD9C2;padding:36px"><div class="big" style="color:#B5472A">Oriente</div><div class="sub" style="margin-top:12px">all\'Armata Rossa</div></div></div>',
          a('Ognuno', pre=0.1), a='wipe', d=1.0)])))
    # AN6: carta 1946 con la cortina di ferro
    src, size = mappa_img('im-004', (8, 48, 602, 516), [(514, 44, 592, 150)])
    d = limiti(P, 1, c('Una', nth=0, dopo='immagine', pre=0.3), c('occidente', pre=0.3))
    s.append(scena(d[0], d[1], 'Churchill, 1946', riga([
        num(1946, 1946, c('millenovecentoquarantasei', pre=1.5), sep=False, style='font-size:250px'),
        colonna([card('', 'Winston Churchill, ormai ex primo ministro britannico', 'cel', c('Winston', pre=0.2), w=860),
                 card('', "Usa un'immagine destinata a restare", 'pag', c('usa', pre=0.2), w=860)], 'align-items:flex-start')], 'gap:80px')))
    tC = c('cortina', pre=0.3)
    cam = [(tC - 0.5, .5, .5, 1.0), (tC + 0.6, .48, .5, 1.9), (c('Stettino', pre=0.2), .48, .38, 2.4), (c('Trieste', pre=0.6), .5, .64, 2.4), (c('occidente', pre=0.3), .5, .52, 1.25), (d[3] - 0.5, .5, .5, 1.0)]
    cortina = [(850, 535), (832, 600), (815, 652), (880, 700), (990, 768), (992, 815), (890, 850), (903, 905)]
    marks = linea_svg(cortina, (1782, 1404), tC + 0.2, d=c('Trieste', pre=0.2) - tC - 0.2, wd=22, dash='stroke-dasharray="1"') if False else linea_svg(cortina, (1782, 1404), tC + 0.2, d=max(2.0, c('Trieste', pre=0.2) - tC), wd=20) \
        + mk(47.7 - 3, 38.1 - 3.5, 6, 7, c('Stettino', pre=0.2), lab='Stettino', lx=-3, ly=-9) + mk(50.8 - 3, 64.5 - 3.5, 6, 7, c('Trieste', pre=0.2), lab='Trieste', lx=4, ly=-3)
    mp = mappa(src, size, 825, 650, cam, d[1] + 0.1, marks)
    s.append(scena(d[1], d[3], 'La cortina di ferro', riga([
        mp, colonna([
            card('Stettino', 'sul Mar Baltico', 'cel', c('Stettino', pre=0.3), w=840),
            card('Trieste', "sull'Adriatico", 'cel', c('Trieste', pre=0.3), w=840),
            card('', 'A occidente gli americani, a oriente i sovietici', 'pag', c('occidente', pre=0.3), w=840),
            card('', 'Una divisione concreta, politica e militare', 'pesca', c('divisione', nth=0, dopo='ideologica', pre=0.3), w=840)], 'align-items:flex-start;gap:22px')], 'gap:50px;justify-content:flex-start')))
    return K2, s

# ------------------------------------------------------------------ ARGOMENTO 3
@pezzo('AN3_1', ['AN7', 'AN8'])
def AN3_1(P):
    a = P.v(0); c = P.v(1)
    b = limiti(P, 0, a('Lo', nth=0, dopo='contenimento', pre=0.3), a('Mosca', pre=0.4))
    s = []
    s.append(scena(b[0], b[1], 'La dottrina Truman', riga([
        icona('scudo', a('dottrina', pre=0.2), TEL, 230, fl=5),
        colonna([card('', "Gli Stati Uniti si impegnano a bloccare l'espansione del comunismo ovunque nel mondo", 'cel', a('Stati', pre=0.2), w=1100),
                 X('Strategia del contenimento', a('strategia', pre=0.2), 'pillbox', a='left')], 'align-items:flex-start;gap:30px')], 'gap:80px')))
    s.append(scena(b[1], b[2], 'Il piano Marshall, 1947', riga([
        nodo('Stati Uniti', 'cel', a('Marshall', pre=0.2), w=420),
        colonna([X('aiuti', a('aiuti', pre=0.5), 'big', a='pop'), freccia(a('aiuti', pre=0.4), 0.9, w=420)], 'gap:0px'),
        nodo('Europa', 'men', a('ricostruire', pre=0.5), w=420)], 'gap:40px')
        + colonna([num(1947, 1947, a('millenovecentoquarantasette', pre=0.8), sep=False, style='font-size:110px', cls='big'), card('', 'Un colossale programma di aiuti per ricostruire l\'Europa', 'pag', a('colossale', pre=0.2), w=1200)], 'gap:14px;margin-top:30px')))
    s.append(scena(b[2], b[3], 'La risposta di Mosca', riga([
        card('Mosca', 'Vede nel piano un modo per comprare il consenso europeo', 'pesca', a('Mosca', pre=0.2), w=520),
        freccia(a('obbliga', pre=0.4), 0.7, w=110),
        card('Obbliga i paesi satelliti', 'a rifiutare i dollari americani', 'lil', a('obbliga', pre=0.2), w=520),
        freccia(a('Poi', pre=0.4), 0.7, w=110),
        card('Crea il Cominform', 'per coordinare i partiti comunisti europei, anche quelli occidentali', 'pag', a('Poi', pre=0.2), w=560)], 'gap:10px;align-items:stretch')
        + colonna([sig('Cominform', a('Cominform', pre=0.1))], 'margin-top:20px')))
    d = limiti(P, 1, c('Arrivano', nth=1, pre=0.3), c('E', nth=0, dopo='case', pre=0.3), c('La', nth=0, dopo='epoca', pre=0.3))
    s.append(scena(d[0], d[1], 'Gli aiuti materiali del piano Marshall', riga([
        icona('spiga', c('cibo', pre=0.2), '#3FA66B', 170, fl=4),
        colonna([card('Cibo e beni di prima necessità', '', 'men', c('cibo', pre=0.2), w=1100),
                 card('', 'Arrivano in un\'Europa con i campi devastati dalla guerra', 'bia', c('campi', pre=0.4), w=1100)], 'align-items:flex-start')], 'gap:60px')))
    s.append(scena(d[1], d[2], 'Benzina e carbone per ripartire', colonna([
        card('Benzina e carbone', 'per far ripartire:', 'pesca', c('benzina', pre=0.2), w=1100),
        riga([colonna([icona('fabbrica', c('fabbriche', pre=0.2), TEL, 130, fl=4), nodo('le fabbriche', 'cel', c('fabbriche', pre=0.2), w=360)], 'gap:10px'),
              colonna([icona('sbarra', c('trasporti', pre=0.2), TEL, 130, fl=4), nodo('i trasporti', 'cel', c('trasporti', pre=0.2), w=360)], 'gap:10px'),
              colonna([icona('sole', c('illuminare', pre=0.2), '#E0B800', 130, fl=4), nodo('le case illuminate', 'pag', c('illuminare', pre=0.2), w=420)], 'gap:10px')], 'gap:60px')])))
    s.append(scena(d[2], d[3], 'Quanti soldi arrivano', riga([
        colonna([num(0, 13, c('tredici', pre=0.9), d=1.6, cls='num'), X('miliardi di dollari', c('tredici', pre=0.3), 'lab', a='up'), X('circa', c('circa', pre=0.3), 'sub', a='fade')]),
        freccia(c('Italia', pre=0.8), 0.8, w=220),
        colonna([num(0, 1, c('Italia', pre=0.9), d=1.0, cls='num', style='color:#3FA66B'), X('miliardo all\'Italia', c('Italia', pre=0.3), 'lab', a='up'), X('una cifra enorme per l\'epoca', c('cifra', pre=0.3), 'sub', a='fade')])], 'gap:70px')))
    s.append(scena(d[3], d[4], 'La ricostruzione', colonna([
        riga([num(1948, 1948, c('millenovecentoquarantotto', pre=0.8), sep=False, cls='big', style='font-size:150px'), freccia(c('millenovecentocinquantadue', pre=0.8), 1.0, w=380),
              num(1952, 1952, c('millenovecentocinquantadue', pre=0.8), sep=False, cls='big', style='font-size:150px')], 'gap:40px'),
        card('', 'Gli americani vigilano su come vengono spesi i soldi', 'pag', c('vigilano', pre=0.3), w=1250)])))
    return K3, s


def cd(titolo, corpo, col, w=None, style=''):
    f, b = PAL[col]
    return (f'<div class="cd" style="background:{f};border-color:{b};' + (f'width:{w}px;' if w else '') + style + '">' + (f'<h3>{titolo}</h3>' if titolo else '') + (f'<p>{corpo}</p>' if corpo else '') + '</div>')
def slot(t0, t1, inner, w=860, top=0, a='up', hl=None, fl=0):
    return X(inner, t0, 'abs', f'left:0;top:{top}px;width:{w}px', a=a, d=0.55, t1=t1, hl=hl, fl=fl)

@pezzo('AN3_2', ['AN9'])
def AN3_2(P):
    a = P.v(0); b = limiti(P, 0)
    src, size = mappa_img('im-008', (200, 10, 790, 490), [(200, 86, 500, 114, (255, 255, 255))])
    tz = [a('americana', pre=0.3), a('sovietica', pre=0.3), a('britannica', pre=0.3), a('francese', pre=0.3)]
    tB = a('Ma', nth=0, dopo='francese', pre=0.3); t48 = a('millenovecentoquarantotto', pre=0.6); tP = a('Gli', nth=0, dopo='Ovest', pre=0.2)
    tS = a('Stalin', nth=1, pre=0.2); t49 = a('millenovecentoquarantanove', pre=0.6); tD = a('La', nth=0, dopo='est', pre=0.2)
    cam = [(0, .5, .5, 1.0), (a('Germania', pre=0.2), .22, .62, 1.45), (tB - 0.3, .22, .62, 1.45), (tB + 0.3, .75, .22, 2.3), (t48 + 1.0, .75, .22, 2.3), (tP, .3, .62, 1.5),
           (t49 - 0.2, .3, .62, 1.5), (t49 + 0.8, .27, .6, 1.9), (tD, .45, .5, 1.1), (b[1] - 0.6, .5, .5, 1.0)]
    mp = mappa(src, size, 799, 650, cam, 0.3, mk(33.5, 47, 8, 9.5, tB + 0.2, t1=tP, lab='Berlino', lx=-2, ly=-9))
    chips4 = ''.join(f'<div class="chip" style="position:absolute;left:{(i % 2) * 430}px;top:{210 + (i // 2) * 84}px;width:420px;font-size:36px;font-weight:700">{n}</div>' for i, n in enumerate(['zona americana', 'zona sovietica', 'zona britannica', 'zona francese']))
    chips4 = ''.join(X(n, t, 'chip', f'position:absolute;left:{(i % 2) * 430}px;top:{215 + (i // 2) * 84}px;width:420px;font-size:36px;font-weight:700', a='left', t1=tB - 0.1)
                     for i, (n, t) in enumerate(zip(['zona americana', 'zona sovietica', 'zona britannica', 'zona francese'], tz)))
    voli = ''.join(X(f'<svg width="100" height="100" viewBox="0 0 100 100" fill="#2060AF" transform="rotate(90)">{ICONE["aereo"]}</svg>', tP + 0.8 + 0.7 * i, 'abs', 'left:0;top:330px', a='flow', d=3.0, dx=740, t1=tS - 0.1) for i in range(5))
    st = pila(860, 650, [
        slot(0.4, tB - 0.1, cd('Germania e Berlino', 'divise in quattro zone di occupazione', 'cel', 860)),
        chips4,
        slot(tB, t48 - 0.1, cd('Ma Berlino', 'si trova dentro la zona sovietica', 'pesca', 860)),
        slot(t48, tP - 0.1, cd('1948', 'Stalin chiude gli accessi via terra a Berlino Ovest', 'lil', 860)),
        slot(tP, tS - 0.1, cd('Il ponte aereo', 'Gli occidentali riforniscono la città solo con gli aerei', 'men', 860)),
        voli, num(0, 427, a('quattrocentoventisette', pre=1.0), d=1.6, cls='big', style='position:absolute;left:0;top:470px;font-size:130px', suf=' giorni', t1=tS - 0.1),
        slot(tS, t49 - 0.1, cd('Stalin deve togliere il blocco', '', 'pag', 860)),
        slot(t49, tD - 0.1, cd('1949: nascono due Stati', '', 'cel', 860)),
        sig('RFT', a('Repubblica', pre=0.1), style='position:absolute;left:0;top:190px;width:860px', t1=tD - 0.1),
        sig('RDT', a('Repubblica', nth=1, pre=0.1), style='position:absolute;left:0;top:300px;width:860px', t1=tD - 0.1),
        slot(tD, b[1], cd('La divisione durerà', "circa quarant'anni", 'lil', 860), hl=[(tD, b[1])]),
        num(0, 40, tD + 0.3, d=1.5, cls='big', style='position:absolute;left:0;top:300px;font-size:200px', suf=' anni', t1=b[1]),
    ])
    return K3, [scena(b[0], b[1], 'Germania e Berlino divise', riga([mp, st], 'gap:50px;justify-content:flex-start;align-items:flex-start'), bstyle='justify-content:flex-start')]

# ------------------------------------------------------------------ ARGOMENTO 4
@pezzo('AN4_1', ['AN10', 'AN11'])
def AN4_1(P):
    a = P.v(0); c = P.v(1)
    b = limiti(P, 0, a('Si', nth=0, dopo='sociale', pre=0.3), a('E', nth=0, dopo='gratuita', pre=0.3))
    s = []
    s.append(scena(b[0], b[1], 'Lo Stato sociale in Europa occidentale', riga([
        nodo('New Deal americano', 'cel', a('New', pre=0.3), w=560, sub='politiche di riferimento'),
        freccia(a('Stato', pre=0.3), 0.8, w=200),
        nodo('Stato sociale', 'pag', a('Stato', pre=0.2), w=560, sub='in inglese: Welfare State', hl=[(a('Welfare', pre=0.2), b[1])])], 'gap:30px')))
    s.append(scena(b[1], b[2], 'Che cosa garantisce lo Stato sociale', riga([
        colonna([icona('dollaro', a('salari', pre=0.2), '#3FA66B', 130, fl=4), card('Salari minimi', 'anche i più poveri possono accedere ai beni e ai consumi', 'men', a('salari', pre=0.2), w=780)], 'gap:14px'),
        colonna([icona('scudo', a('assistenza', pre=0.2), TEL, 130, fl=4), card('Assistenza sanitaria', 'il più possibile gratuita', 'cel', a('assistenza', pre=0.2), w=780)], 'gap:14px')], 'gap:60px;align-items:flex-start')))
    s.append(scena(b[2], b[3], 'Lo Stato interviene nell\'economia', colonna([
        card('Opere pubbliche e infrastrutture', 'Lo Stato interviene nell\'economia', 'pesca', a('Stato', nth=0, dopo='gratuita', pre=0.2), w=1300),
        riga([nodo('Regno Unito', 'cel', a('Regno', pre=0.2), w=520, sub='laburisti di Attlee'), nodo('Francia', 'cel', a('Quarta', pre=0.4), w=420, sub='Quarta Repubblica'),
              nodo('Italia', 'bia', a('Italia', pre=0.2), w=420, sub='lo Stato sociale arriverà più tardi')], 'gap:30px;align-items:stretch')])))
    d = limiti(P, 1, c('Nel', nth=0, dopo='intervenire', pre=0.4), c('millenovecentocinquantasette', pre=0.6))
    s.append(scena(d[0], d[1], 'Aprile 1949: nasce la NATO', riga([
        icona('scudo', c('NATO', pre=0.2), TEL, 220, fl=5),
        colonna([sig('NATO', c('NATO', pre=0.1)), card('Un\'alleanza difensiva', 'Se uno Stato membro viene attaccato, gli altri devono intervenire', 'cel', c('alleanza', pre=0.2), w=1100)], 'align-items:flex-start;gap:26px')], 'gap:70px')))
    paesi = ['Francia', 'Germania Ovest', 'Italia', 'Belgio', 'Olanda', 'Lussemburgo']
    pw = ['Francia', 'Germania', 'Italia', 'Belgio', 'Olanda', 'Lussemburgo']
    s.append(scena(d[1], d[2], '1951: nasce la CECA, l\'Europa dei sei', colonna([
        sig('CECA', c('CECA', pre=0.1)),
        riga([chip(p_, c(w, pre=0.2), style='font-size:38px;font-weight:800;padding:14px 26px') for p_, w in zip(paesi, pw)], 'gap:16px;flex-wrap:wrap'),
        card('', 'Abbassa i dazi su materie prime come il carbone', 'men', c('abbassa', pre=0.2), w=1200)])))
    s.append(scena(d[2], d[3], '1957: i Trattati di Roma', riga([
        colonna([card('Comunità Economica Europea', '', 'cel', c('Comunità', pre=0.2), w=700), sig('CEE', c('Comunità', pre=0.1))], 'gap:14px;align-items:flex-start'),
        colonna([card('Euratom', '', 'lil', c('Euratom', pre=0.2), w=500), sig('Euratom', c('Euratom', pre=0.1))], 'gap:14px;align-items:flex-start'),
        ], 'gap:40px;align-items:flex-start') + colonna([icona('stella', c('scintilla', pre=0.3), '#E0B800', 100, fl=4), card('', 'La scintilla della futura Unione Europea', 'pag', c('scintilla', pre=0.2), w=1000)], 'gap:10px;margin-top:20px')))
    return K4, s

@pezzo('AN4_2', ['AN12', 'AN24'])
def AN4_2(P):
    a = P.v(0); c = P.v(1)
    b = limiti(P, 0, a('Il', nth=0, dopo='oggi', pre=0.3), a('All', dopo='aiutano', pre=0.3))
    s = []
    s.append(scena(b[0], b[1], 'La NATO è un\'alleanza difensiva', riga([
        icona('scudo', a('NATO', pre=0.2), TEL, 200, fl=5),
        colonna([sig('NATO', a('NATO', pre=0.1)), card('Difensiva, non offensiva', '', 'cel', a('difensiva', pre=0.2), w=900),
                 card('Esiste ancora oggi', '', 'men', a('esiste', pre=0.2), w=900)], 'align-items:flex-start;gap:26px')], 'gap:70px')))
    tp = a('principio', pre=0.2); ta = a('aiutano', pre=1.0)
    nodi = [(300, 450, 'Stato membro'), (300, 620, 'Stato membro'), (300, 790, 'Stato membro')]
    ex = ''.join(X(e(t_), tp + 0.15 * i, 'pnode', f'position:absolute;left:{x - 150}px;top:{y - 70}px;width:300px;background:#CFE8FB;border-color:#4A9AD8;font-size:36px', fl=3) for i, (x, y, t_) in enumerate(nodi))
    ex += X('Stato attaccato', tp + 0.3, 'pnode', 'position:absolute;left:1250px;top:520px;width:380px;background:#FFD9C2;border-color:#E8825A;font-size:40px', fl=3)
    ex += X('<svg width="90" height="90" viewBox="0 0 100 100" stroke="#B5472A" fill="none">' + ICONE['croce'] + '</svg>', a('attaccato', pre=0.2), 'abs', 'left:1580px;top:470px', a='pop')
    ex += ''.join(freccia_abs(460, y, 1240, 590 + (y - 620) * 0.2, ta + 0.2 * i, d=0.9) for i, (x, y, t_) in enumerate(nodi))
    s.append(scena(b[1], b[2], 'Difesa reciproca', X('Gli altri lo aiutano', ta, 'pillbox', 'position:absolute;left:760px;top:880px', a='pop') + ex, raw=True))
    s.append(scena(b[2], b[3], 'Gli Stati Uniti e l\'alleanza', colonna([
        riga([card('', 'All\'inizio alcuni paesi europei temevano ancora la Germania', 'bia', a('All', dopo='aiutano', pre=0.1), w=780),
              freccia(a('Stati', nth=0, dopo='Germania', pre=0.3), 0.7, w=120),
              card('', 'Con gli Stati Uniti l\'alleanza diventa soprattutto antisovietica', 'pesca', a('Stati', nth=0, dopo='Germania', pre=0.1), w=780)], 'gap:20px;align-items:stretch'),
        riga([nodo('Entra l\'Italia', 'cel', a('Entra', pre=0.2), w=560, sub='accolta con qualche diffidenza'),
              nodo('Entra la Turchia', 'cel', a('turchia', pre=0.4), w=560, sub='storica rivale della Russia')], 'gap:40px;align-items:stretch')])))
    d = limiti(P, 1, c('Con', nth=0, dopo='CECA', pre=0.3), c('Col', pre=0.3), c('E', nth=0, dopo='capitali', pre=0.3))
    s.append(scena(d[0], d[1], 'All\'inizio: un accordo per commerciare liberamente', riga([
        icona('chiave', c('accordo', pre=0.2), TEL, 160, fl=4),
        card('', 'L\'integrazione europea è solo un accordo per commerciare liberamente', 'cel', c('accordo', pre=0.2), w=1200)], 'gap:50px')))
    s.append(scena(d[1], d[2], 'CECA, 1951: sei paesi e il carbone', colonna([
        sig('CECA', c('CECA', pre=0.1)),
        riga([nodo('Belgio', 'men', c('Belgio', pre=0.2), w=420, sub='ha il carbone in abbondanza'),
              X(''.join(f'<svg width="60" height="60" viewBox="0 0 100 100" fill="#0B1530"><rect x="14" y="14" width="72" height="72" rx="14"/></svg>' for _ in range(1)), c('Belgio', pre=0.2) + 0.5 + 0.0, 'abs', 'position:relative;left:0;top:0', a='flow', d=2.0, dx=420, t1=d[2]) if False else freccia(c('Belgio', pre=0.0), 0.9, w=260),
              nodo('Italia', 'pesca', c('Italia', pre=0.2), w=420, sub='il carbone non ce l\'ha')], 'gap:30px;align-items:stretch'),
        card('', 'Sei paesi abbassano i dazi su materie prime come il carbone', 'cel', c('abbassano', pre=0.2), w=1300)])))
    s.append(scena(d[2], d[3], 'CEE, 1957: un mercato comune', colonna([
        sig('CEE', c('CEE', pre=0.1)),
        card('Nasce un mercato comune', 'Col tempo arriva la libera circolazione di:', 'pag', c('mercato', pre=0.2), w=1300),
        riga([chip(t_, c(w, pre=0.2), style='font-size:44px;font-weight:800;padding:14px 30px') for t_, w in [('merci', 'merci'), ('servizi', 'servizi'), ('persone', 'persone'), ('capitali', 'capitali')]], 'gap:24px')])))
    s.append(scena(d[3], d[4], 'Più avanti, e l\'Euratom', riga([
        colonna([X('Più avanti verranno', c('avanti', pre=0.2), 'lab', a='up'), chip('l\'abolizione dei controlli alle frontiere', c('abolizione', pre=0.2), style='font-size:38px'), chip('la moneta unica', c('moneta', pre=0.2), style='font-size:38px')], 'align-items:flex-start;gap:18px'),
        colonna([sig('Euratom', c('Euratom', pre=0.1)), card('Non decolla', 'anche per l\'opposizione della Francia di de Gaulle', 'lil', c('decolla', pre=0.2), w=760)], 'gap:14px;align-items:flex-start')], 'gap:70px;align-items:flex-start')))
    return K4, s

# ------------------------------------------------------------------ ARGOMENTO 5
@pezzo('AN5_1', ['AN13', 'AN14'])
def AN5_1(P):
    a = P.v(0); c = P.v(1)
    b = limiti(P, 0, a('Il', nth=0, dopo='comunismo', pre=0.3), a('Alcuni', pre=0.3))
    s = []
    s.append(scena(b[0], b[1], 'Negli Stati Uniti torna la paura del rosso', riga([
        X('Red Scare', a('Red', pre=0.2), 'big', 'font-size:150px;color:#B5472A', a='pop'),
        card('', 'La paura del rosso, cioè del comunismo', 'pesca', a('paura', pre=0.2), w=820)], 'gap:70px')))
    s.append(scena(b[1], b[2], 'Il maccartismo', riga([
        colonna([nodo('Senatore McCarthy', 'cel', a('senatore', pre=0.3), w=640), X('Maccartismo', a('maccartismo', pre=0.3), 'pillbox', a='left')], 'gap:30px'),
        colonna([card('', 'Un clima da caccia alle streghe', 'lil', a('clima', pre=0.2), w=900),
                 card('', 'Si cercano comunisti infiltrati ovunque: dal Congresso al programma atomico', 'pag', a('cercano', pre=0.2), w=900)], 'align-items:flex-start')], 'gap:50px')))
    s.append(scena(b[2], b[3], 'I segreti atomici e i Rosenberg', riga([
        colonna([card('', 'Alcuni segreti atomici erano stati davvero passati all\'Unione Sovietica', 'cel', a('Alcuni', pre=0.2), w=700)]),
        freccia(a('coniugi', pre=0.4), 0.7, w=130),
        colonna([num(1953, 1953, a('millenovecentocinquantatre', pre=0.8), sep=False, cls='big', style='font-size:120px'),
                 card('I coniugi Rosenberg', 'condannati a morte con l\'accusa di spionaggio nucleare', 'lil', a('coniugi', pre=0.2), w=720)], 'gap:12px')], 'gap:20px;align-items:flex-start')))
    d = limiti(P, 1, c('Il', nth=0, dopo='cambia', pre=0.3), c('Dopo', pre=0.3))
    s.append(scena(d[0], d[1], 'Eisenhower: la strategia americana cambia', riga([
        nodo('Eisenhower', 'cel', c('Eisenhower', pre=0.3), w=520, sub='repubblicano, generale della seconda guerra mondiale'),
        freccia(c('strategia', pre=0.3), 0.8, w=200),
        nodo('Nuova strategia americana', 'pag', c('strategia', pre=0.2), w=600)], 'gap:30px')))
    s.append(scena(d[1], d[2], 'Dal contenimento al rollback', riga([
        colonna([icona('muro', c('contenimento', pre=0.2), TEL, 130, fl=3), card('Contenimento', 'voleva fermare il comunismo ai confini', 'cel', c('contenimento', pre=0.2), w=700)], 'gap:14px'),
        colonna([icona('sbarra', c('rollback', pre=0.2), '#B5472A', 130, fl=3), card('Rollback', 'vuole respingerlo: l\'obiettivo dichiarato è liberare i popoli sottomessi', 'pesca', c('rollback', pre=0.2), w=860)], 'gap:14px')], 'gap:50px;align-items:flex-start')))
    s.append(scena(d[2], d[3], 'Dopo Stalin: disgeli e corsa agli armamenti', riga([
        colonna([num(1953, 1953, c('millenovecentocinquantatre', pre=0.8), sep=False, cls='big', style='font-size:120px'), card('', 'Muore Stalin: la tensione cala un poco', 'cel', c('tensione', pre=0.3), w=640), card('', 'Si alternano brevi disgeli', 'bia', c('alternano', pre=0.2), w=640)], 'gap:16px'),
        colonna([X('<div style="display:flex;align-items:flex-end;gap:26px">' + ''.join(f'<span>{icona("atomo", c("corsa", pre=0.2) + 0.5 * i, "#B5472A", sz, a="pop")}</span>' for i, sz in enumerate([90, 140, 200])) + '</div>', c('corsa', pre=0.3), 'abs', 'position:relative', a='none'),
                 card('', 'Una corsa agli armamenti nucleari sempre più distruttiva', 'pesca', c('corsa', pre=0.2), w=780)], 'gap:16px')], 'gap:60px;align-items:flex-start')))
    return K5, s

# ------------------------------------------------------------------ ARGOMENTO 6
@pezzo('AN6_1', ['AN15', 'AN17'])
def AN6_1(P):
    a = P.v(0); c = P.v(1)
    b = limiti(P, 0, a('Germania', pre=0.3), a('Unica', pre=0.3))
    s = []
    s.append(scena(b[0], b[1], 'Gli stati satelliti', riga([
        card('', "Dove è arrivata l'Armata Rossa, Stalin impone una rigida stalinizzazione", 'pesca', a('Armata', pre=0.3), w=1000),
        X('Stati satelliti', a('nascono', pre=0.2), 'pillbox', a='left')], 'gap:50px')))
    import math as M
    sat = [('Germania Est', 'Germania'), ('Polonia', 'Polonia'), ('Cecoslovacchia', 'Cecoslovacchia'), ('Ungheria', 'Ungheria'), ('Romania', 'Romania'), ('Bulgaria', 'Bulgaria'), ('Albania', 'Albania')]
    cx, cy, rx, ry = 960, 640, 650, 235; ex = ''
    ex += X('Mosca', a('Germania', pre=0.2), 'pnode', f'position:absolute;left:{cx - 190}px;top:{cy - 75}px;width:380px;background:#FFD9C2;border-color:#E8825A', fl=3)
    ex += X('regimi a partito unico', a('partito', pre=0.3), 'chip', f'position:absolute;left:{cx - 190}px;top:{cy + 62}px;width:380px;text-align:center;font-weight:700', a='up')
    for i, (n, w) in enumerate(sat):
        ang = -M.pi / 2 + 2 * M.pi * i / 7 - 0.45
        x = cx + rx * M.cos(ang); y = cy + ry * M.sin(ang) - 20; t0 = a(w, pre=0.25)
        ex += freccia_abs(int(cx + (x - cx) * 0.33), int(cy - 10 + (y - cy) * 0.30), int(cx + (x - cx) * 0.74), int(cy - 10 + (y - cy) * 0.70), t0, d=0.7, wd=7)
        ex += X(n, t0 + 0.1, 'chip', f'position:absolute;left:{x - 150:.0f}px;top:{y - 26:.0f}px;width:300px;text-align:center;font-size:36px;font-weight:800;background:#CFE8FB;border-left-color:#4A9AD8;border-radius:16px', fl=2)
    s.append(scena(b[1], b[2], 'Controllati da Mosca', ex, raw=True))
    s.append(scena(b[2], b[3], 'L\'eccezione: la Jugoslavia', riga([
        nodo('Mosca', 'pesca', a('Jugoslavia', pre=0.3), w=380),
        colonna([icona('croce', a('rompe', pre=0.3), '#B5472A', 110, fl=2), X('1948', a('millenovecentoquarantotto', pre=0.5), 'pillbox', a='pop')], 'gap:6px'),
        nodo('Jugoslavia', 'men', a('Jugoslavia', pre=0.2), w=460, sub='del maresciallo Tito: comunista, ma autonoma')], 'gap:40px')))
    d = limiti(P, 1, c('Al', nth=0, dopo='Krusciov', pre=0.3), c('Si', nth=0, dopo='personalità', pre=0.3), c('In', nth=0, dopo='represse', pre=0.3))
    s.append(scena(d[0], d[1], '1953: muore Stalin', riga([
        num(1953, 1953, c('millenovecentocinquantatre', pre=0.8), sep=False, cls='big', style='font-size:170px'),
        colonna([card('', 'Muore Stalin', 'bia', c('muore', pre=0.2), w=800), card('', 'Il nuovo leader è Nikita Krusciòv', 'cel', c('nuovo', pre=0.2), w=800)], 'align-items:flex-start')], 'gap:70px')))
    s.append(scena(d[1], d[2], 'Il rapporto segreto di Krusciòv', colonna([
        card('Ventesimo congresso del partito', 'un rapporto segreto che poi trapela', 'cel', c('ventesimo', pre=0.2), w=1300),
        card('Krusciòv denuncia', 'i crimini di Stalin e il culto della personalità', 'pesca', c('denuncia', pre=0.2), w=1300)])))
    s.append(scena(d[2], d[3], 'Speranze di libertà, ma repressione', riga([
        icona('sole', c('speranze', pre=0.2), '#E0B800', 150, fl=4),
        card('Speranze di libertà', '', 'pag', c('speranze', pre=0.2), w=520),
        freccia(c('Polonia', pre=0.4), 0.7, w=120),
        card('Polonia', 'rivolte popolari, che vengono represse', 'lil', c('Polonia', pre=0.2), w=640)], 'gap:24px')))
    car = ''.join(X('<svg width="130" height="130" viewBox="0 0 100 100" fill="#0B1530">' + ICONE['carro'] + '</svg>', c('carri', pre=0.3) + 0.9 * i, 'abs', 'position:relative;margin-left:0', a='pop', d=0.4) for i in range(3))
    s.append(scena(d[3], d[4], 'Ungheria, 1956', colonna([
        riga([num(1956, 1956, c('millenovecentocinquantasei', pre=0.8), sep=False, cls='big', style='font-size:130px'),
              card('Un nuovo governo', 'vuole uscire dal Patto di Varsavia: l\'alleanza militare dei paesi dell\'Est', 'cel', c('governo', pre=0.2), w=1100)], 'gap:40px'),
        riga([X(car, c('carri', pre=0.3), 'abs', 'position:relative;display:flex;gap:14px', a='none'), card('Mosca manda i carri armati', '', 'pesca', c('carri', pre=0.2), w=700),
              card('', 'Il partito unico e il controllo sovietico restano', 'lil', c('Il', nth=0, dopo='armati', pre=0.2), w=700)], 'gap:30px')])))
    return K6, s

@pezzo('AN6_2', ['AN16', 'AN21'])
def AN6_2(P):
    a = P.v(0); c = P.v(1)
    b = limiti(P, 0, a('Il', nth=0, dopo='consumo', pre=0.3), a('E', nth=0, dopo='Bucarest', pre=0.3))
    s = []
    s.append(scena(b[0], b[1], 'Il modello sovietico nei paesi satelliti', riga([
        colonna([icona('spiga', a('terre', pre=0.2), '#3FA66B', 120, fl=3), card('Terre collettivizzate', 'con la forza', 'men', a('terre', pre=0.2), w=520)], 'gap:12px'),
        colonna([icona('fabbrica', a('industrie', pre=0.2), TEL, 120, fl=3), card('Industrie nazionalizzate', '', 'cel', a('industrie', pre=0.2), w=520)], 'gap:12px'),
        colonna([icona('sbarra', a('piani', pre=0.2), '#B5472A', 120, fl=3), card('Piani sulla produzione pesante', 'a scapito dei beni di consumo', 'pesca', a('piani', pre=0.2), w=580)], 'gap:12px')], 'gap:30px;align-items:flex-start')))
    s.append(scena(b[1], b[2], 'Il Comecon lega le economie a Mosca', riga([
        colonna([nodo('Varsavia', 'cel', a('Varsavia', pre=0.2), w=360), nodo('Budapest', 'cel', a('Budapest', pre=0.2), w=360), nodo('Bucarest', 'cel', a('Bucarest', pre=0.2), w=360)], 'gap:20px'),
        freccia(a('lega', pre=0.0) if False else a('Bucarest', pre=0.1), 0.9, w=300),
        nodo('Mosca', 'pesca', a('Mosca', pre=0.3), w=380, sub='Comecon: ne lega le economie')], 'gap:30px')))
    s.append(scena(b[2], b[3], '1955: nasce il Patto di Varsavia', riga([
        colonna([icona('scudo', a('millenovecentocinquantacinque', pre=0.4), '#4A9AD8', 150), nodo('NATO', 'cel', a('NATO', pre=0.4), w=420, sub='nata nel 1949'), sig('NATO', a('NATO', pre=0.2))], 'gap:12px'),
        X('risposta', a('risposta', pre=0.2), 'lab', a='up'),
        colonna([icona('scudo', a('Patto', pre=0.2), '#E8825A', 150), nodo('Patto di Varsavia', 'pesca', a('Patto', pre=0.2), w=560, sub='1955, sul piano militare')], 'gap:12px')], 'gap:50px;align-items:flex-start')))
    # AN21: carta 1955
    src, size = mappa_img('im-012', (0, 38, 525, 642), [(34, 518, 108, 618)])
    d = limiti(P, 1)
    tW, tE, tJ, tF = c('ovest', pre=0.3), c('est', nth=0, dopo='ovest', pre=0.3), c('Al', nth=0, dopo='Bulgaria', pre=0.3), c('Questa', pre=0.3)
    cam = [(0, .5, .5, 1.0), (tW, .3, .55, 1.7), (c('Grecia', pre=0.3), .75, .65, 1.9), (tE - 0.3, .65, .5, 1.7), (tJ - 0.2, .65, .62, 2.1), (tF - 0.2, .5, .5, 1.0)]
    marks = (mk(63, 69.5, 18, 6, c('Grecia', pre=0.1), t1=tE, rect=True) + mk(49, 59, 9, 8, tE + 0.2, t1=tJ, rect=False) if False else '') \
        + mk(66, 66.5, 16, 7.5, c('Grecia', pre=0.1), t1=tE, rect=True, lab='Grecia', lx=0, ly=-9) + mk(84, 67.5, 14, 7, c('Turchia', pre=0.1), t1=tE, rect=True, lab='Turchia', lx=-6, ly=-9) \
        + mk(48, 40, 12, 7, tE + 0.5, t1=tJ, rect=True, lab='Germania Est', lx=0, ly=-9) + mk(70, 61, 14, 7, tE + 1.5, t1=tJ, rect=True, lab='Bulgaria', lx=0, ly=-9) \
        + mk(57, 59.5, 17, 9, tJ + 0.2, t1=tF, rect=True, lab='Jugoslavia', lx=0, ly=-9)
    mp = mappa(src, size, 565, 650, cam, d[0] + 0.1, marks)
    st = pila(1100, 650, [
        slot(d[0] + 0.4, tW, cd('La carta dell\'Europa nel 1955', 'Una divisione in due blocchi', 'cel', 1100), w=1100),
        slot(tW, tE, cd('A ovest: i paesi della NATO', 'Stati Uniti e Canada, i paesi dell\'Europa occidentale, la Grecia e la Turchia', 'cel', 1100), w=1100),
        sig('NATO', c('NATO', pre=0.1), style='position:absolute;left:0;top:330px;width:1100px;font-size:34px', t1=tE),
        slot(tE, tJ, cd('A est: il Patto di Varsavia', 'dalla Germania Est alla Bulgaria', 'pesca', 1100), w=1100),
        X('Patto di Varsavia: l\'alleanza militare dei paesi dell\'Est', tE + 0.5, 'chip', 'position:absolute;left:0;top:300px;width:1100px', t1=tJ),
        slot(tJ, tF, cd('Al centro dei Balcani: la Jugoslavia di Tito', 'comunista, ma fuori dal Patto', 'men', 1100), w=1100),
        slot(tF, d[1], cd('Una divisione quasi uguale', 'fino al crollo dell\'Unione Sovietica', 'pag', 1100), w=1100, hl=[(tF, d[1])]),
    ])
    s.append(scena(d[0], d[1], 'L\'Europa nel 1955', riga([mp, st], 'gap:50px;justify-content:flex-start;align-items:flex-start'), bstyle='justify-content:flex-start'))
    return K6, s

# ------------------------------------------------------------------ ARGOMENTO 7
def freccia_svg(p0, p1, vb, t0, d=1.0, col='#E0354B', wd=16, L=60):
    ang = math.atan2(p1[1] - p0[1], p1[0] - p0[0])
    h1 = (p1[0] - L * math.cos(ang - 0.45), p1[1] - L * math.sin(ang - 0.45)); h2 = (p1[0] - L * math.cos(ang + 0.45), p1[1] - L * math.sin(ang + 0.45))
    p = f'M{p0[0]} {p0[1]} L{p1[0]} {p1[1]} M{h1[0]:.0f} {h1[1]:.0f} L{p1[0]} {p1[1]} L{h2[0]:.0f} {h2[1]:.0f}'
    return X(f'<svg viewBox="0 0 {vb[0]} {vb[1]}" style="position:absolute;left:0;top:0;width:100%;height:100%"><path d="{p}" fill="none" stroke="{col}" stroke-width="{wd}" stroke-linecap="round" stroke-linejoin="round"/></svg>',
             t0, 'abs', 'left:0;top:0;width:100%;height:100%', a='draw', d=d)

@pezzo('AN7_1', ['AN18'])
def AN7_1(P):
    a = P.v(0); b = limiti(P, 0, a('Una', pre=0.3), a('Cos', pre=0.3))
    s = []
    s.append(scena(b[0], b[1], 'Il Giappone occupato', riga([
        nodo('Giappone', 'pesca', a('Giappone', pre=0.2), w=460),
        card('', 'Resta occupato dagli americani, sotto la guida del generale MacArthur', 'cel', a('occupato', pre=0.2), w=1100)], 'gap:50px')))
    s.append(scena(b[1], b[2], 'Una nuova costituzione e una crescita straordinaria', colonna([
        riga([card('Nuova costituzione democratica', 'conserva l\'imperatore, che però deve dichiarare di non essere divino', 'lil', a('costituzione', pre=0.2), w=1000),
              card('Democrazia parlamentare e capitalista', '', 'cel', a('democrazia', pre=0.2), w=700)], 'gap:30px;align-items:stretch'),
        riga([icona('sbarra', a('crescita', pre=0.2), '#3FA66B', 100, fl=3), card('Crescita economica straordinaria', 'fondata sulla tecnologia e sulle esportazioni', 'men', a('crescita', pre=0.2), w=1300)], 'gap:30px')])))
    s.append(scena(b[2], b[3], 'Il principale alleato in Asia', riga([
        nodo('Giappone', 'pesca', b[2] + 0.4, w=420),
        freccia(a('principale', pre=0.2), 0.8, w=240),
        nodo('Stati Uniti', 'cel', a('Stati', nth=0, dopo='Cos', pre=0.1), w=460, sub='il Giappone è il loro principale alleato in Asia')], 'gap:40px')))
    return K7, s

@pezzo('AN7_2', ['AN19', 'AN22'])
def AN7_2(P):
    a = P.v(0); c = P.v(1)
    b = limiti(P, 0, a('millenovecentocinquanta', pre=0.4), a('difeso', pre=0.6), a('millenovecentocinquantatre', pre=0.5))
    s = []
    s.append(scena(b[0], b[1], '1949: la Cina diventa comunista', riga([
        colonna([num(1949, 1949, a('millenovecentoquarantanove', pre=0.8), sep=False, cls='big', style='font-size:120px'), nodo('Cina', 'pesca', a('Cina', pre=0.2), w=420, sub='diventa comunista')], 'gap:12px'),
        freccia(a('Corea', pre=0.3), 0.8, w=220),
        nodo('Corea del Nord', 'cel', a('Corea', pre=0.2), w=520, sub='vuole fare lo stesso in tutta la penisola')], 'gap:30px')))
    s.append(scena(b[1], b[2], '1950: il Nord invade il Sud', riga([
        colonna([nodo('Unione Sovietica', 'pesca', a('Unione', pre=0.2), w=480), nodo('Cina di Mao', 'pesca', a('Cina', nth=1, pre=0.2), w=480)], 'gap:18px'),
        colonna([X('appoggiano', a('appoggiato', pre=0.2), 'sub', a='up'), freccia(a('appoggiato', pre=0.2), 0.7, w=170)], 'gap:0'),
        nodo('Corea del Nord', 'cel', a('invade', pre=1.8), w=440, sub='comunista'),
        freccia(a('invade', pre=0.3), 0.8, w=170),
        nodo('Corea del Sud', 'men', a('invade', pre=0.2), w=420)], 'gap:14px')))
    s.append(scena(b[2], b[3], 'Il Sud è difeso dall\'ONU', colonna([
        sig('ONU', a('ONU', pre=0.1)),
        card('Un contingente dell\'ONU', 'guidato dagli Stati Uniti difende il Sud', 'cel', a('contingente', pre=0.2), w=1300),
        card('La risoluzione passa', 'perché il delegato sovietico era assente', 'pag', a('risoluzione', pre=0.2), w=1300)])))
    s.append(scena(b[3], b[4], '1953: l\'armistizio e il trentottesimo parallelo', riga([
        num(0, 38, a('trentottesimo', pre=1.2), d=1.2, suf='°', cls='num', style='font-size:250px'),
        colonna([card('Un armistizio ripristina il confine', 'sul trentottesimo parallelo', 'cel', a('armistizio', pre=0.2), w=860),
                 card('', 'Non c\'è mai stata una vera pace: la Corea è divisa ancora oggi', 'lil', a('mai', pre=0.2), w=860)], 'align-items:flex-start')], 'gap:60px')))
    # AN22 carta della Corea
    src, size = mappa_img('im-016', (5, 40, 605, 445))
    d = limiti(P, 1)
    t50 = c('millenovecentocinquanta', pre=0.3); t3 = c('tre', pre=0.3); tF = c('Alla', pre=0.3); tN = c('nord', nth=0, dopo='parallelo', pre=0.3)
    cam = [(d[0], .5, .5, 1.0), (c('Cina', pre=0.4), .25, .25, 1.9), (t50 - 0.2, .25, .6, 1.7), (t3 - 0.2, .75, .55, 1.8), (tF - 0.2, .75, .6, 1.5), (tN, .75, .55, 1.8), (d[1] - 0.6, .5, .5, 1.0)]
    vb = (1800, 1215)
    marks = (mk(14, 8, 9, 9, c('Cina', pre=0.2), t1=t50, lab='Cina', lx=-1, ly=-9)
             + freccia_svg((330, 600), (520, 1090), vb, t50, d=1.4) + mk(63.2, 42, 8, 11, c('Pyongyang', pre=0.1), lab='Pyongyang', lx=-11, ly=-10)
             + mk(70.5, 60.5, 8, 11, c('Seul', pre=0.1), lab='Seul', lx=3, ly=-10)
             + linea_svg([(925, 725), (1800, 725)], vb, tF, d=1.2, col='#0B1530', wd=26) + linea_svg([(925, 725), (1800, 725)], vb, tF + 0.1, d=1.2, col='#FFE600', wd=14))
    mp = mappa(src, size, 960, 648, cam, d[0] + 0.1, marks)
    st = pila(760, 648, [
        slot(d[0] + 0.4, t50, cd('La carta della Corea', 'La Corea del Nord confina con la Cina', 'cel', 760), w=760),
        slot(t50, t3, cd('1950', 'Il Nord comunista avanza verso sud', 'pesca', 760), w=760),
        slot(t3, tF, cd('Per tre anni', 'il fronte si sposta avanti e indietro lungo la penisola, con milioni di vittime', 'lil', 760), w=760),
        slot(tF, tN, cd('Alla fine', 'il confine torna sul 38° parallelo', 'pag', 760), w=760),
        slot(tN, d[1], cd('A nord', 'la capitale è Pyongyang', 'cel', 760) + '<div style="height:24px"></div>' + cd('A sud', 'la capitale è Seul', 'men', 760), w=760),
    ])
    s.append(scena(d[0], d[1], 'La guerra di Corea sulla carta', riga([mp, st], 'gap:40px;justify-content:flex-start;align-items:flex-start'), bstyle='justify-content:flex-start'))
    return K7, s

@pezzo('AN7_3', ['AN20', 'AN23'])
def AN7_3(P):
    a = P.v(0); c = P.v(1)
    b = limiti(P, 0, a('Nel', nth=0, dopo='Taiwan', pre=0.3), a('Negli', pre=0.3))
    s = []
    s.append(scena(b[0], b[1], '1949: Mao vince la guerra civile', riga([
        colonna([num(1949, 1949, a('millenovecentoquarantanove', pre=0.8), sep=False, cls='big', style='font-size:120px'),
                 nodo('Mao Zedong', 'pesca', a('Mao', pre=0.3), w=520, sub='vince la guerra civile'), ], 'gap:12px'),
        freccia(a('proclama', pre=0.4), 0.8, w=170),
        nodo('Repubblica Popolare Cinese', 'pesca', a('proclama', pre=0.2), w=560),
        colonna([nodo('Chiang Kai-shek', 'cel', a('nazionalisti', pre=0.2), w=520, sub='i nazionalisti si rifugiano a Taiwan')])], 'gap:24px')))
    s.append(scena(b[1], b[2], '1958: il Grande balzo in avanti', riga([
        colonna([num(1958, 1958, a('millenovecentocinquantotto', pre=0.8), sep=False, cls='big', style='font-size:120px'), card('Grande balzo in avanti', 'per industrializzare il paese', 'pag', a('Grande', pre=0.2), w=620)], 'gap:12px'),
        freccia(a('fallisce', pre=0.4), 0.7, w=130),
        card('Il piano fallisce', '', 'lil', a('fallisce', pre=0.2), w=420),
        freccia(a('carestia', pre=0.4), 0.7, w=130),
        card('Carestia', 'milioni di morti', 'pesca', a('carestia', pre=0.2), w=420)], 'gap:8px;align-items:flex-start')))
    s.append(scena(b[2], b[3], 'La rottura e la Rivoluzione Culturale', riga([
        colonna([X('Anni Sessanta', a('anni', pre=0.2), 'pillbox', a='left'), card('', 'La Cina rompe con l\'Unione Sovietica', 'cel', a('rompe', pre=0.2), w=560)], 'gap:16px;align-items:flex-start'),
        colonna([num(1966, 1966, a('millenovecentosessantasei', pre=0.8), sep=False, cls='big', style='font-size:100px'), card('Rivoluzione Culturale', 'Le Guardie Rosse epurano i dirigenti ritenuti infedeli', 'lil', a('Rivoluzione', pre=0.2), w=700),
                 card('', 'Il paese cade nel caos e nella violenza', 'pesca', a('caos', pre=0.3), w=700)], 'gap:12px;align-items:flex-start')], 'gap:40px;align-items:flex-start')))
    d = limiti(P, 1, c('Per', nth=0, dopo='Taiwan', pre=0.3), c('Ancora', pre=0.3))
    s.append(scena(d[0], d[1], 'Il governo nazionalista a Taiwan', riga([
        nodo('Cina comunista', 'pesca', c('vittoria', pre=0.2), w=460, sub='vittoria di Mao'),
        colonna([X('si rifugia', c('rifugia', pre=0.2), 'sub', a='up'), freccia(c('rifugia', pre=0.1), 0.8, w=250)], 'gap:0'),
        nodo('Taiwan', 'cel', c('isola', pre=0.3), w=420, sub='isola: il governo nazionalista di Chiang Kai-shek')], 'gap:30px')))
    s.append(scena(d[1], d[2], 'Il seggio cinese all\'ONU', colonna([
        sig('ONU', c('ONU', pre=0.1)),
        riga([card('Per molti anni', 'il seggio cinese all\'ONU resta a Taiwan', 'cel', c('seggio', pre=0.2), w=780), card('La Cina comunista', 'resta isolata', 'pesca', c('isolata', pre=0.2), w=560)], 'gap:30px;align-items:stretch'),
        card('', 'La situazione cambia solo negli anni Settanta', 'pag', c('cambia', pre=0.2), w=1300)])))
    s.append(scena(d[2], d[3], 'Taiwan oggi', riga([
        nodo('Taiwan', 'cel', c('Taiwan', nth=1, pre=0.2), w=520, sub='vuole restare indipendente'),
        X('<svg width="140" height="80" viewBox="0 0 140 80"><path d="M30 40 L6 40 M20 24 L4 40 L20 56 M110 40 L134 40 M120 24 L136 40 L120 56" fill="none" stroke="#2060AF" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/></svg>', c('mentre', pre=0.2), 'arr', a='pop'),
        nodo('Repubblica Popolare Cinese', 'pesca', c('mentre', pre=0.2), w=620, sub='vuole riunirla a sé')], 'gap:30px')))
    return K7, s

# ------------------------------------------------------------------ SPIEGONE (apertura Parte 2)
KR = 'Ripasso della prima parte'
@pezzo('RIP2', ['RIP2'])
def RIP2(P):
    a = P.v(0)
    tA = a('Dopo', pre=0.3); tB = a('accordi', pre=0.5); tC = a('dottrina', pre=0.6); tD = a('millenovecentoquarantanove', pre=0.6)
    b = [0, tA, tB, tC, tD, P.v(0).fine + 0.55]
    s = []
    # scheda blu animata di apertura
    dk = (X('Prima di ripartire:<br>ricordiamo la prima parte', 0.35, 'dk dtit', 'left:140px;top:330px;width:1640px', a='up', d=0.8)
          + X('Argomento per argomento', 1.8, 'dk dsub', 'left:140px;top:640px', a='up', d=0.7)
          + X('', 1.2, 'dk', 'left:140px;top:600px;width:220px;height:10px;border-radius:5px;background:#FFE600', a='wipe', d=0.9))
    s.append(scena(b[0], b[1], None, dk, raw=True))
    s[-1] = s[-1].replace('<section', '<section style="z-index:60"', 1)
    MP = lambda n: f'/tmp/w/pezzi/MAP{n}_finale.png'
    M1 = (1920, 1080)
    def zoom(t0, t1): return [(t0, .5, .5, 1.0), (t1, .5, .5, 1.03)]
    # argomento 1
    tONU = a('ONU', pre=0.1); t5 = a('cinque', pre=0.3); tDi = a('Dichiarazione', pre=0.2)
    left1 = colonna([sig('ONU', tONU), riga([num(0, 5, t5, d=0.9, cls='big', style='font-size:110px'), X('membri permanenti con diritto di veto', t5 + 0.1, 'sub', 'font-weight:700;width:440px', a='up')], 'gap:24px'),
                     card('Dichiarazione universale dei diritti umani', '', 'lil', tDi, w=620)], 'align-items:flex-start;gap:22px;width:640px')
    mp1 = mappa(MP(1), M1, 1000, 562, zoom(b[1], b[2]), b[1] + 0.8, '', style='')
    s.append(scena(b[1], b[2], 'Il dopoguerra e la nuova geopolitica', riga([left1, colonna([mp1])], 'gap:40px;justify-content:flex-start;align-items:flex-start'), bstyle='justify-content:flex-start'))
    # argomento 2
    tBW = a('accordi', pre=0.2); tBip = a('bipolare', pre=0.4); tCo = a('cortina', pre=0.3)
    left2 = colonna([card('Bretton Woods', 'il dollaro diventa la moneta di riferimento', 'pag', tBW, w=760),
                     card('Mondo bipolare', 'Stati Uniti democratici e capitalisti contro Unione Sovietica comunista e a partito unico', 'cel', tBip, w=760),
                     card('Una cortina di ferro', "divide l'Europa", 'pesca', tCo, w=760)], 'align-items:flex-start;gap:20px')
    src4, size4 = mappa_img('im-004', (8, 48, 602, 516), [(514, 44, 592, 150)])
    cortina = [(850, 535), (832, 600), (815, 652), (880, 700), (990, 768), (992, 815), (890, 850), (903, 905), (920, 930), (1075, 1135)]
    mp4 = mappa(src4, size4, 825, 650, [(tCo - 0.2, .5, .5, 1.0), (b[3] - 0.5, .5, .55, 1.15)], tCo - 0.1, linea_svg(cortina, (1782, 1404), tCo + 0.3, d=2.5, wd=22))
    sc2 = X(f'<div class="dollar" style="text-align:center"><svg width="300" height="300" viewBox="0 0 100 100" fill="#E0B800" stroke="#E0B800">{ICONE["dollaro"]}</svg></div>', tBW, 'abs', 'position:relative;left:0;top:0', a='pop', fl=5, t1=tCo - 0.3)
    s.append(scena(b[2], b[3], 'Bretton Woods e il bipolarismo', riga([left2, colonna([sc2]), mp4], 'gap:40px;justify-content:flex-start;align-items:flex-start;position:relative'), bstyle='justify-content:flex-start'))
    # argomento 3
    tT = a('dottrina', pre=0.2); tM = a('Marshall', pre=0.2); tU = a('URSS', pre=0.2); tCm = a('Cominform', pre=0.2); tBl = a('blocco', pre=0.2); tPa = a('ponte', pre=0.2)
    laneA = riga([nodo('Dottrina Truman', 'cel', tT, w=480), freccia(tM - 0.2, 0.6, w=120), nodo('Piano Marshall', 'cel', tM, w=480), freccia(a('contenere', pre=0.3), 0.6, w=120), nodo('Contenere il comunismo', 'pag', a('contenere', pre=0.1), w=620)], 'gap:10px;justify-content:flex-start')
    laneB = riga([nodo("L'URSS risponde", 'pesca', tU, w=480), freccia(tCm - 0.2, 0.6, w=120), nodo('Cominform', 'pesca', tCm, w=480), freccia(tBl - 0.2, 0.6, w=120), nodo('Blocco di Berlino', 'lil', tBl, w=520)], 'gap:10px;justify-content:flex-start')
    voli = ''.join(X(f'<svg width="90" height="90" viewBox="0 0 100 100" fill="#3FA66B" transform="rotate(90)">{ICONE["aereo"]}</svg>', tPa + 0.6 * i, 'abs', 'left:1300px;top:560px', a='flow', d=2.4, dx=450, t1=b[4]) for i in range(4))
    laneC = X('Il ponte aereo supera il blocco', tPa, 'pillbox', 'margin-left:1250px', a='left')
    chips = colonna([sig('URSS', tU, style='font-size:30px;width:880px'), sig('Cominform', tCm, style='font-size:30px;width:880px')], 'gap:10px;align-items:flex-start;width:900px')
    s.append(scena(b[3], b[4], 'La dottrina Truman, il piano Marshall e Berlino', colonna([laneA, laneB, riga([chips, laneC], 'gap:30px;justify-content:flex-start;width:100%')], 'gap:30px;align-items:flex-start;width:100%') , extra=voli, bstyle='justify-content:flex-start'))
    # germania 1949 + passaggio alla parte 2
    src8, size8 = mappa_img('im-008', (200, 10, 790, 490), [(200, 86, 500, 114, (255, 255, 255))])
    tF = a('Adesso', pre=0.3)
    mp8 = mappa(src8, size8, 615, 500, [(tD - 0.3, .5, .5, 1.0), (tD + 0.8, .3, .6, 1.9), (tF, .35, .55, 1.4), (b[5] - 0.3, .5, .5, 1.0)], tD + 0.1, '')
    left4 = colonna([card('1949', 'nascono due Germanie', 'cel', tD + 0.2, w=900, hl=[(tD + 0.2, tF)]),
                     sig('RFT', tD + 1.2, style='font-size:30px'), sig('RDT', tD + 2.0, style='font-size:30px'),
                     card('Adesso', 'vediamo come vivono le due Europe', 'pag', tF, w=900, hl=[(tF, b[5])])], 'align-items:flex-start;gap:20px')
    s.append(scena(b[4], b[5], 'Due Germanie, due Europe', riga([mp8, left4], 'gap:50px;justify-content:flex-start;align-items:flex-start'), bstyle='justify-content:flex-start'))
    return KR, s, [(-1, b[1] + 0.1)]
