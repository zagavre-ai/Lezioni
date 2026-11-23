# Dati della lezione · Storia V · Lezione 3 «L'Italia di Giolitti» (tempi = secondi del video originale del prof)
import json, re, sys
sys.path.insert(0, '/home/user/w3/build')
from sync import cards as pdf_cards, S
TITOLO = "L'Italia di Giolitti"
PDF_PAGE = {1: 2, 2: 4, 3: 5, 4: 7, 5: 9, 6: 10, 7: 11, 8: 12, 9: 13, 10: 15, 11: 17}
# refusi del PDF del prof corretti nelle nostre slide (elencati nel rapporto)
FIX = [("Sciopero del 1904", "sciopero del 1904"), ("femministe", "femministi")]
SIGLE = {  # sigla spiegata sullo schermo ogni volta che compare
    (3, 0): "PSI = Partito Socialista Italiano",
    (8, 3): "Fiat = Fabbrica Italiana Automobili Torino",
    (11, 0): "PSI = Partito Socialista Italiano",
}
ARG = {
 1: dict(titolo="La crisi di fine secolo e la svolta liberale", a=31, b=202, kw=["Adua", "Crispi", "Bava Beccaris", "Gaetano Bresci", "Zanardelli"]),
 2: dict(titolo="La nuova linea politica di Giolitti", a=203, b=252, kw=["neutralità dello Stato", "sindacati", "Camere del lavoro", "riforme"]),
 3: dict(titolo="I rapporti con i socialisti e lo sciopero del 1904", a=253, b=297, kw=["Turati", "riformisti", "massimalisti", "sciopero generale"]),
 4: dict(titolo="Il rapporto con i cattolici e il trasformismo", a=298, b=329, kw=["Non expedit", "Pio X", "deputati cattolici", "trasformismo"]),
 5: dict(titolo="Le riforme sociali e scolastiche", a=330, b=401, kw=["riposo settimanale", "Istituto Nazionale Assicurazioni", "legge Orlando", "legge Daneo-Credaro"]),
 6: dict(titolo="Il suffragio universale maschile e il Patto Gentiloni", a=402, b=481, kw=["suffragio universale maschile", "indennità parlamentare", "Patto Gentiloni", "divorzio"]),
 7: dict(titolo="Le riforme mancate: le donne in lotta", a=482, b=499, kw=["Anna Kuliscioff", "Lucciola", "delitto d'onore", "ospedali psichiatrici"]),
 8: dict(titolo="Il decollo industriale italiano", a=500, b=564, kw=["protezionismo", "banca mista", "Ansaldo", "Fiat, automobili di Torino", "Montecatini"]),
 9: dict(titolo="Il divario Nord-Sud e l'emigrazione", a=565, b=615, kw=["triangolo industriale", "Mezzogiorno", "Salvemini", "9 milioni di emigrati"]),
 10: dict(titolo="La politica coloniale e la guerra in Libia", a=616, b=669, kw=["Libia", "Pascoli", "Tripolitania e Cirenaica", "trattato di Losanna", "Dodecaneso"]),
 11: dict(titolo="La caduta di Giolitti e la «settimana rossa»", a=670, b=726, kw=["Mussolini", "Salandra", "Patto Gentiloni", "settimana rossa", "Ancona"]),
}
# eventi per argomento: ('card', t, indice)  ('img', t0, t1, chiave)  ('mid', t_bersaglio, 'ANk')  = inserto dopo una frase intera
EV = {
 1: [('card', 245.3, 0), ('card', 505.0, 1), ('card', 586.7, 2), ('card', 802.1, 3), ('card', 878.0, 4), ('card', 981.3, 5),
     ('mid', 380, 'AN1'), ('mid', 708, 'AN2'), ('img', 1141.6, 1146.8, 'regicidio')],
 2: [('img', 1147.7, 1158.7, 'giolitti'), ('card', 1148.9, 0), ('card', 1262.7, 1), ('card', 1295.2, 2), ('card', 1343.8, 3), ('mid', 1294, 'AN3')],
 3: [('card', 1372.7, 0), ('card', 1454.4, 1), ('card', 1482.9, 2), ('card', 1511.4, 3), ('mid', 1446.8, 'AN5'), ('img', 1605.2, 1610.0, 'turati')],
 4: [('card', 1610.7, 0), ('card', 1705.7, 1), ('card', 1730.6, 2), ('mid', 1677.9, 'AN7'), ('img', 1763.3, 1785.9, 'murri')],
 5: [('card', 1814.1, 0), ('card', 1824.2, 1), ('card', 1855.8, 2), ('card', 1985.2, 3), ('card', 2087.5, 4), ('mid', 1925.9, 'AN9')],
 6: [('card', 2155.0, 0), ('card', 2385.1, 1), ('card', 2497.1, 2), ('card', 2517.4, 3), ('mid', 2312.4, 'AN11')],
 7: [('card', 2646.0, 0), ('card', 2652.0, 1), ('card', 2669.9, 2), ('card', 2700.7, 3), ('mid', 2668.0, 'AN13')],
 8: [('card', 2815.0, 0), ('card', 2846.3, 1), ('card', 2871.8, 2), ('card', 2884.6, 3), ('card', 3107.5, 4), ('mid', 2960, 'AN16'), ('mid', 3081, 'AN15')],
 9: [('card', 3161.9, 0), ('card', 3189.6, 1), ('card', 3252.3, 2), ('card', 3336.6, 4), ('img', 3343.1, 3375.8, 'emigrazione'), ('card', 3376.1, 3), ('card', 3440.3, 4), ('mid', 3252, 'AN17')],
 10: [('card', 3487.2, 0), ('card', 3678.8, 2), ('card', 3697.3, 1), ('card', 3721.8, 3), ('card', 3729.8, 4), ('mid', 3593.4, 'AN19'), ('mid', 3696.2, 'AN20'), ('img', 3789.8, 3801.9, 'libia')],
 11: [('card', 3837.3, 0), ('card', 3959.5, 1), ('card', 3963.1, 2), ('card', 4003.2, 3), ('mid', 3906.2, 'AN21')],
}
END_AP = {1: None, 2: 'AN4', 3: 'AN6', 4: 'AN8', 5: 'AN10', 6: 'AN12', 7: 'AN14', 8: None, 9: 'AN18', 10: None, 11: 'AN22'}
# mappe del prof: dopo quale argomento
MAPPE = {2: 1, 9: 2, 11: 3}
IMG = {
 'regicidio': ('/home/user/w3/img/regicidio_hd.png', 'Il regicidio di Monza', "Il regicidio di Monza: nel 1900 l'anarchico Gaetano Bresci uccide re Umberto I."),
 'giolitti': ('/home/user/w3/img/giolitti_hd.png', 'Giovanni Giolitti', "<b>Giovanni Giolitti</b><br>Un ritratto fotografico di Giolitti nel 1905."),
 'turati': ('/home/user/w3/img/turati_hd.png', 'Filippo Turati', "<b>Il leader dei socialisti moderati</b><br>Un ritratto fotografico di Filippo Turati."),
 'murri': ('/home/user/w3/img/murri_hd.png', 'Romolo Murri', "<b>Romolo Murri</b><br>Il democratico-cristiano Romolo Murri in una fotografia degli anni Dieci."),
 'emigrazione': ('/home/user/w3/img/emigrazione_hd.png', 'I flussi migratori italiani', "<b>Infografica</b><br>I flussi migratori italiani nel primo Novecento."),
 'libia': ('/home/user/w3/img/libia_hd.png', 'La guerra di Libia (1911-1912)', "<b>Leggere la carta</b><br>La guerra di Libia (1911-1912)."),
}

def card_list(arg):
    t, cs = pdf_cards(PDF_PAGE[arg])
    out = []
    for i, c in enumerate(cs):
        for a, b in FIX: c = c.replace(a, b)
        c = c.replace("L'indennità", "L'indennità")
        out.append((c, SIGLE.get((arg, i))))
    t2 = t
    for a, b in FIX: t2 = t2.replace(a, b)
    return ARG[arg]['titolo'], out

# gap utili per i tagli (prima frase intera)
def gap_after(j): return S[j + 1]['inizio'] - S[j]['fine']
def snap_cut(target, lo, hi, mingap=0.5):
    """indice j (a..b-1) tale che il taglio dopo S[j] cade in una pausa >= mingap, più vicino a target"""
    best = None
    for j in range(lo, hi):
        if gap_after(j) >= mingap:
            d = abs(S[j]['fine'] - target)
            if best is None or d < best[0]: best = (d, j)
    return best[1]

# AN: testo dai testi_voci (numeri in lettere) -> schermo in cifre
ONES = {'uno': 1, 'due': 2, 'tre': 3, 'quattro': 4, 'cinque': 5, 'sei': 6, 'sette': 7, 'otto': 8, 'nove': 9, 'dieci': 10, 'undici': 11, 'dodici': 12,
        'tredici': 13, 'quattordici': 14, 'quindici': 15, 'sedici': 16, 'diciassette': 17, 'diciotto': 18, 'diciannove': 19}
TENS = {'venti': 20, 'trenta': 30, 'quaranta': 40, 'cinquanta': 50, 'sessanta': 60, 'settanta': 70, 'ottanta': 80, 'novanta': 90}
TV = {'vent': 20, 'trent': 30, 'quarant': 40, 'cinquant': 50, 'sessant': 60, 'settant': 70, 'ottant': 80, 'novant': 90}
def parse_it(w):
    s = w.lower().replace("'", "").replace('’', '')
    if not s: return None
    tot = 0; rest = s
    m = re.match(r'^(?:(due|tre|quattro|cinque|sei|sette|otto|nove)mila|mille)', rest)
    if m:
        tot += (ONES[m.group(1)] if m.group(1) else 1) * 1000; rest = rest[m.end():]
    m = re.match(r'^(?:(due|tre|quattro|cinque|sei|sette|otto|nove))?cent(?:(?=ottan|otto)|o)', rest)
    if m:
        tot += (ONES[m.group(1)] if m.group(1) else 1) * 100; rest = rest[m.end():]
    if rest:
        m = re.match(r'^(vent|trent|quarant|cinquant|sessant|settant|ottant|novant)(i|a)?(uno|due|tre|quattro|cinque|sei|sette|otto|nove)?$', rest)
        if m:
            tot += TV[m.group(1)] + (ONES[m.group(3)] if m.group(3) else 0)
        elif rest in ONES: tot += ONES[rest]
        else: return None
    return tot if tot else None
def digits(text):
    def rep(m):
        v = parse_it(m.group(0))
        pre = m.string[:m.start()].rstrip()
        if v and v <= 10 and (not pre or pre[-1] in '.?!:'): return m.group(0)   # «Tre protagonisti…» a inizio frase resta in lettere
        return str(v) if v else m.group(0)
    text = re.sub(r"\b(vent|trent|quarant)'anni", lambda m: str({'vent': 20, 'trent': 30, 'quarant': 40}[m.group(1)]) + ' anni', text)
    t = re.sub(r"\b[a-zA-Zàèéìòù]{3,}\b", rep, text)
    for a, b in [("Umberto Primo", "Umberto I"), ("Vittorio Emanuele Terzo", "Vittorio Emanuele III"), ("Pio Decimo", "Pio X"), ("Pio Nono", "Pio IX"),
                 ("Leone Tredicesimo", "Leone XIII"), ("Giovanni Primo", "Giovanni I")]:
        t = t.replace(a, b)
    for a, b in [(r'\bPSI\b(?! \()', 'PSI, cioè Partito Socialista Italiano,'), (r'\bINA\b(?! \()', 'INA, cioè Istituto Nazionale Assicurazioni,'), (r'\bFiat\b(?! \()', 'Fiat, cioè Fabbrica Italiana Automobili Torino,')]:
        t = re.sub(a, b, t, count=1)
    return t
if __name__ == '__main__':
    for x in ["milleottocentottantasette", "millenovecentododici", "trent'anni", "ventuno", "nove milioni", "dodici", "ottanta", "millenovecento", "millenovecentotre", "ventotto", "novantasei", "Primo"]:
        print(x, digits(x))
