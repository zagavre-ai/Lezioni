import sys, os, json, html
sys.path.insert(0, '/home/user/Lezioni/lez12')
import scenes as S, engine as E, piano as PI
from scenes import rr, kore, kore_lines, cache, PNG, JG, ARGO, EYEB, MAT, loud
from voci import VOCI
O = PI.OPERE
# ---------------- approfondimenti ----------------
AN = {
 'AN1A': ('Approfondimento · 01', 'I folli anni Venti', [
    ("Europa: ricostruzione materiale", "Dopo la prima"), ("Stati Uniti: nulla da ricostruire", "Gli Stati Uniti, invece"),
    ("Folli anni Venti: divertimento, nuovi gusti e nuovi stili", "Sono i cosiddetti"), ("L'età del jazz", "È l'età del jazz"), ("Un'epoca di rottura", "Non è più il mondo")], None),
 'AN1B': ('Approfondimento · 01', 'Parigi, capitale della cultura', [
    ("Parigi: capitale mondiale della cultura, dell'arte e della vita notturna", "Parigi ha vinto"), ("Germania ridimensionata", "a fronte"),
    ("Stati Uniti più presenti in Europa", "Gli Stati Uniti sono"), ("Fitzgerald a Parigi", "Anche gli intellettuali"), ("Qui fioriscono Surrealismo e Dadaismo", "È in questo contesto")], None),
 'AN2A': ('Approfondimento · 02', 'Dada: una rivolta antiartistica', [
    ("Zurigo, 1916", "Il Dadaismo nasce"), ("Svizzera: rifugio contro la guerra", "La Svizzera non"), ("Cabaret Voltaire: Hugo Ball e Tristan Tzara", "Il luogo simbolo"),
    ("Movimento antiartistico", "Dada non è uno stile"), ("Unica regola: non avere regole", "La sua unica regola")], None),
 'AN2B': ('Approfondimento · 02', 'Ruota di bicicletta', [
    ("Ruota di bicicletta, 1913", "Nel millenovecentotredici"), ("Primo ready-made rettificato", "Il movimento nasce"),
    ("Funzione d'uso annullata", "Così annulla"), ("Un nuovo senso, visivo e concettuale", "È una combinazione")], [(0, (O + 'duchamp_ruota.png', 80, 320, 700, 600), 'Marcel Duchamp · Ruota di bicicletta')]),
 'AN3A': ('Approfondimento · 03', 'Automatismo psichico e Surrealtà', [
    ("Parigi, 1924: Manifesto di André Breton", "Nel millenovecentoventiquattro"), ("Psicoanalisi di Freud: sogno e inconscio", "ed è figlio"),
    ("Automatismo psichico", "Lo strumento principale"), ("Surrealtà: sogno e veglia", "Il risultato è"), ("Dal Dada all'inconscio", "Il Surrealismo prende")], None),
 'AN4A': ('Approfondimento · 04', 'Max Ernst e Joan Miró', [
    ("Max Ernst: L'angelo del focolare, 1937", "Max Ernst dipinge"), ("Figura mostruosa in uno spazio desolato", "una figura mostruosa"),
    ("Paura dei totalitarismi europei", "L'opera riflette"), ("Joan Miró: le Costellazioni", "Joan Miró, nei primi")],
    [(0, (O + 'angelo.png', 80, 320, 800, 600), "Max Ernst · L'angelo del focolare"), (3, (O + 'miro_a.png', 80, 320, 800, 600), 'Joan Miró · Costellazioni')]),
 'AN4B': ('Approfondimento · 04', 'René Magritte: parole e immagini', [
    ("Parole, immagini e realtà", "René Magritte usa"), ("La chiave dei sogni: le parole non corrispondono agli oggetti", "Ne La chiave dei sogni"),
    ("Il tradimento delle immagini: Ceci n'est pas une pipe", "Ne Il tradimento"), ("Le affinità elettive: un uovo in una gabbia", "Ne Le affinità"),
    ("La percezione è una rappresentazione soggettiva", "Per Magritte")],
    [(0, (O + 'chiave_sogni.png', 80, 320, 700, 600), 'René Magritte · La chiave dei sogni'), (2, (O + 'pipa.png', 80, 320, 800, 600), 'René Magritte · Il tradimento delle immagini'),
     (3, (O + 'afflitta.png', 80, 320, 700, 600), 'René Magritte · Le affinità elettive')]),
}
PILL = {
 1: ('Ripasso · 01', 'I folli anni Venti', [
   ("Dopo la prima guerra mondiale: i folli anni Venti, tra Zurigo, Parigi e New York", "Dopo la prima"), ("Spirito di rottura contro l'ideologia borghese e capitalista", "C'è uno spirito"),
   ("Parigi: capitale della cultura, dell'arte e della vita notturna (Montparnasse e Rive Gauche)", "Parigi è la capitale"), ("Contro il mercato dell'arte: niente gallerie tradizionali e collezionisti speculatori", "Gli artisti rifiutano"),
   ("Nuovi luoghi di ritrovo: caffè, club e locali anticonformisti", "I nuovi luoghi")]),
 2: ('Ripasso · 02', 'Il Dadaismo e Marcel Duchamp', [
   ("Dada nasce a Zurigo nel 1916, al Cabaret Voltaire", "Dada nasce"), ("Movimento antiartistico: l'unica regola è non avere regole", "È un movimento"),
   ("Dada: una parola senza senso, scoperta per caso sul dizionario", "Dada è una parola"), ("Jean Arp: la legge del caso; in Germania nasce il fotomontaggio", "Jean Arp"),
   ("Duchamp e i ready-made: il valore passa dall'abilità manuale al pensiero", "Con Marcel Duchamp"), ("Opere simbolo: Ruota di bicicletta, Scolabottiglie e Fontana", "Le opere simbolo")]),
 3: ('Ripasso · 03', 'Il Surrealismo e gli oggetti surrealisti', [
   ("Parigi, 1924: Manifesto di André Breton", "Il Surrealismo nasce"), ("Si ispira alla psicoanalisi di Freud: sogno, irrazionalità, inconscio", "Si ispira"),
   ("Automatismo psichico: il pensiero puro, senza il controllo della ragione", "L'automatismo"), ("Surrealtà: una realtà superiore, sogno e veglia insieme", "La surrealtà"),
   ("Oggetti surrealisti: desideri nascosti ed effetto perturbante", "Gli oggetti surrealisti"), ("Telefono aragosta di Dalí e Colazione in pelliccia di Meret Oppenheim", "come il Telefono")]),
 4: ('Ripasso · 04', 'Ernst, Miró, Dalí e Magritte', [
   ("Max Ernst: L'angelo del focolare e la paura dei totalitarismi", "Max Ernst dipinge"), ("Joan Miró: le Costellazioni, pittogrammi e segni semplici", "Joan Miró crea"),
   ("Salvador Dalí: il metodo paranoico-critico", "Salvador Dalí usa"), ("La persistenza della memoria: orologi molli e relatività del tempo", "e ne La persistenza"),
   ("René Magritte: il rapporto ambiguo tra parole, immagini e realtà", "René Magritte indaga"), ("Da Ceci n'est pas une pipe a La condizione umana", "da Ceci n'est")]),
}
# ---------------- mappa del docente (BES) ----------------
MAPCSS = """
.mb{position:absolute;display:flex;align-items:center;justify-content:center;text-align:center;padding:10px 22px;border-radius:16px;font:600 36px/1.4 Figtree;color:#0B1530;opacity:1}
.mb h5{margin:0 0 6px;font:800 36px 'Figtree'}
.mb ul{margin:0;padding:0;list-style:none;font:600 36px/1.45 Figtree}
.c1{background:#FFDCC6;border:5px solid #C2410C;font:800 52px 'Bricolage Grotesque'}
.cel{background:#DCEEFB;border:4px solid #1D4ED8}.lil{background:#EBE3F7;border:4px solid #6D28D9}
.pag{background:#FFF3BF;border:4px solid #A16207}.men{background:#DDF3E4;border:4px solid #15803D}
.hlm{box-shadow:0 0 0 9px #FFE600,0 10px 24px rgba(11,21,48,.18)}
#leg{position:absolute;right:60px;top:26px;display:flex;gap:16px;font:600 20px Figtree;color:#0B1530}
#leg span{display:flex;align-items:center;gap:7px}#leg i{display:inline-block;width:24px;height:17px;border-radius:4px;border:3px solid}
.mt{position:absolute;left:60px;top:90px;font:800 56px 'Bricolage Grotesque';color:#0B1530}
.mk{position:absolute;left:60px;top:26px;font:700 22px Figtree;letter-spacing:.14em;color:#2060AF}
svg{position:absolute;left:0;top:0}
"""
MB = {  # id: (x,y,w,h,classe,html)
 'B1': (610, 185, 700, 100, 'c1', 'Dadaismo (Zurigo 1916)'),
 'B2': (520, 340, 880, 170, 'pag', 'Movimento artistico di rottura contro la società borghese e capitalista'),
 'B3': (60, 340, 400, 170, 'pag', "L'unica regola è non avere regole"),
 'B4': (1460, 340, 400, 170, 'pag', "Dada è una parola senza senso, fa leva sull'irrazionalità"),
 'B5': (60, 600, 700, 400, 'men', '<div><h5>Principali esponenti:</h5><ul><li>Tristan Tzara</li><li>Jean Arp</li><li>Marcel Duchamp</li><li>Man Ray</li><li>Marcel Janco</li></ul></div>'),
 'B6': (1000, 600, 860, 400, 'pag', "<div><h5>Principali tecniche e concetti trattati:</h5><ul><li>Ready-made</li><li>Provocazione totale</li><li>Valore dell'idea</li><li>Oggetti con altro significato</li></ul></div>"),
}
ARR = {'A1': (960, 290, 960, 336), 'A2': (516, 425, 466, 425), 'A3': (1404, 425, 1454, 425), 'A4': (700, 514, 420, 596), 'A5': (1220, 514, 1400, 596), 'A6': (764, 800, 996, 800)}
ORDER = [('B1', None, 'M1'), ('B2', ['A1'], 'M2'), ('B3', ['A2'], 'M3'), ('B4', ['A3'], 'M4'), ('B5', ['A4'], 'M5'), ('B6', ['A5', 'A6'], 'M6')]
def render_map(k, o):
    shown = ORDER[:k + 1] if k >= 0 else []
    h = '<div class=mk>MAPPA DEL PROFESSORE · DADAISMO</div>'
    h += '<div id=leg>' + ''.join(f'<span><i style="background:{c};border-color:{b}"></i>{t}</span>' for c, b, t in [('#FFDCC6', '#C2410C', 'concetto centrale'), ('#DCEEFB', '#1D4ED8', 'date e sequenze'), ('#FFF3BF', '#A16207', 'parole chiave'), ('#DDF3E4', '#15803D', 'esempi e opere'), ('#EBE3F7', '#6D28D9', 'conseguenze')]) + '</div>'
    h += "<div class=mt>Che cos'è il Dadaismo?</div>"
    h += '<svg width=1920 height=1080><defs><marker id=ah markerUnits=userSpaceOnUse markerWidth=40 markerHeight=40 refX=20 refY=20 orient=auto><path d="M0,4 L36,20 L0,36 z" fill="#0B1530"/></marker></defs>'
    for b, arrows, m in shown:
        for a in (arrows or []):
            x1, y1, x2, y2 = ARR[a]; h += f'<line x1={x1} y1={y1} x2={x2} y2={y2} stroke="#0B1530" stroke-width=10 marker-end="url(#ah)"/>'
    h += '</svg>'
    for i, (b, arrows, m) in enumerate(shown):
        x, y, w, hh, cl, t = MB[b]
        h += f'<div class="mb {cl}{" hlm" if (i == k and k < 99) else ""}" style="left:{x}px;top:{y}px;width:{w}px;height:{hh}px">{t}</div>'
    rr().page(h, o, bg='#fff', css=MAPCSS)
def scene_mappa():
    voices = ['M0'] + [m for _, _, m in ORDER]
    ws = {v: loud(E.vox(v)) for v in voices}; sp = {v: E.voice_span(ws[v]) for v in voices}
    t = 1.9; aud = [(JG['trans'][0], None, None, 0.0, -6)]; tm = {}
    S.META['MAPPA'] = {}
    for v in voices:
        vs, ve = sp[v]; aud.append((ws[v], vs, ve - vs, t, 0)); tm[v] = (t, ve - vs); S.META['MAPPA'][v] = dict(voice=v, v0=t, vs=vs, ve=ve); t += ve - vs + 0.9
    ST = [(cache(f'{PNG}map_t.png', lambda o: render_map(-1, o)), 0.0, 1.9 + tm['M0'][1] + 0.4, False)]
    # titolo della mappa (domanda) sul primo passo
    starts = [tm[m][0] - 0.4 for _, _, m in ORDER]
    for i in range(len(ORDER)):
        ST.append((cache(f'{PNG}map_{i}.png', lambda o, i=i: render_map(i, o)), starts[i], starts[i + 1] if i + 1 < len(ORDER) else t - 0.9 + 0.2, False))
    ST.append((cache(f'{PNG}map_full.png', lambda o: render_map(99, o)), t - 0.9 + 0.2, None, False))
    D = t - 0.9 + 0.2 + 4.0
    aud.append((JG['finale'][0], None, 4.0, t - 0.9 + 0.2, -9))
    return E.make('MAPPA', D, 'white', ST, audio=aud), E.snap(D)
# ---------------- glossario / ripasso / compiti ----------------
GL = [("Dada", "parola senza senso, scoperta per caso sul dizionario", "Dada:"), ("Ready-made", "«pronto all'uso»: oggetto comune sottratto al suo contesto ed esposto come opera d'arte", "Ready-made:"),
      ("Fotomontaggio", "ritagli di giornali e foto per svelare in modo ironico le contraddizioni della società", "Fotomontaggio:"),
      ("Automatismo psichico", "pensiero puro, libero dal controllo della ragione", "Automatismo psichico:"), ("Surrealtà", "realtà superiore: sogno e veglia insieme", "Surrealtà:"),
      ("Effetto perturbante", "shock e disagio creati da accostamenti insoliti", "Effetto perturbante:"),
      ("Frottage", "sfregamento (grafite su carta sopra una superficie ruvida)", "Frottage:"), ("Biomorfismo", "forme geometriche e organiche che fluttuano nello spazio", "Biomorfismo:"),
      ("Metodo paranoico-critico", "razionalizzazione guidata di immagini deliranti, illusioni ottiche e ossessioni", "Metodo paranoico-critico:")]
def render_gloss(k):
    def f(o):
        h, _ = rr().dk_base('Glossario', 'Le parole della lezione', 1)
        for i, (t, d, _m) in enumerate(GL[:k + 1]):
            x = 80 + (i % 3) * 600; y = 316 + (i // 3) * 216
            h += f'<div class="panel{" act" if i == k else ""}" style="left:{x}px;top:{y}px;width:570px;height:206px;padding:16px 24px"><h3 style="font-size:34px">{t}</h3><p style="font-size:28px;line-height:1.28">{d}</p></div>'
        rr().dark_page(h, o)
    return cache(f'{PNG}gl_{k}.png', f)
RF = [("I folli anni Venti", "Dopo la prima guerra mondiale nascono movimenti contro l'ideologia borghese e capitalista, lontani dal mercato dell'arte tradizionale.", "Primo argomento"),
      ("Il Dadaismo", "Zurigo 1916: l'unica regola è non avere regole. Jean Arp e la legge del caso; Marcel Duchamp e il ready-made.", "Secondo argomento"),
      ("Il Surrealismo", "Parigi 1924: Manifesto di André Breton. Psicoanalisi di Freud, automatismo psichico, surrealtà.", "Terzo argomento"),
      ("Le opere surrealiste", "Max Ernst, Joan Miró, Salvador Dalí e René Magritte: immagini oniriche e perturbanti tra parole, immagini e realtà.", "Quarto argomento")]
def render_rf(k):
    def f(o):
        h, _ = rr().dk_base('Ripasso finale', 'Argomento per argomento', 1)
        for i, (t, d, _m) in enumerate(RF[:k + 1]):
            x = 80 + (i % 2) * 900; y = 330 + (i // 2) * 330
            h += f'<div class="panel{" act" if i == k else ""}" style="left:{x}px;top:{y}px;width:860px;height:300px"><h3>{i+1} · {t}</h3><p style="font-size:32px">{d}</p></div>'
        rr().dark_page(h, o)
    return cache(f'{PNG}rf_{k}.png', f)
CMP = [x for x in __import__('re').split(r'(?=Compito (?:uno|due|tre|quattro)\.)', VOCI['COMPITI']) if x.strip()]
CT = ["Descrivi il contesto storico e culturale dei “folli anni Venti” e ricostruisci la nascita del Dadaismo a Zurigo nel 1916, spiegando il significato del nome, le idee espresse nel Manifesto di Tristan Tzara, l'uso del caso nei collage di Jean Arp e la svolta politica e satirica del fotomontaggio dadaista in Germania.",
      "Spiega in che modo Marcel Duchamp rivoluziona il concetto tradizionale di arte attraverso i Ready-Made, chiarendo il passaggio dall'abilità manuale all'operazione mentale e analizzando le sue opere simbolo come lo Scolabottiglie e la Fontana.",
      "Illustra i fondamenti teorici del Surrealismo nato a Parigi nel 1924 con il Manifesto di André Breton, soffermandoti sul legame con la psicoanalisi di Freud, sulla tecnica dell'automatismo psichico, sul concetto di Surrealtà e sull'effetto perturbante degli oggetti surrealisti di Salvador Dalí e Meret Oppenheim.",
      "Confronta i diversi linguaggi artistici del Surrealismo attraverso le figure di Max Ernst, Joan Miró, Salvador Dalí e René Magritte, analizzando tecniche come il frottage, il biomorfismo e il metodo paranoico-critico insieme alla riflessione sul rapporto ambiguo tra parole, immagini e realtà nelle opere di Magritte."]
def render_comp(k):
    def f(o):
        h, _ = rr().dk_base('Compiti', None, 1)
        if k < 4:
            h += f'<div class=sub style="top:170px;color:#9DC3FF;font-size:34px">Compito {k+1} di 4</div>'
            h += f'<div class="ck act" style="top:240px;font-size:40px;line-height:1.5;padding:34px 44px"><b style="font-size:44px">{k+1}</b> {CT[k]}</div>'
        else:
            h += '<div class=big style="top:330px;font-size:84px">Svolgi i compiti qui sotto e premi Consegna</div><div class=sub style="top:640px">Arrivano al docente nel tuo quaderno dei compiti.</div>'
        rr().dark_page(h, o)
    return cache(f'{PNG}cp_{k}.png', f)
def card_scene(name, eyebrow, title, sub, jingle, D, jat=0.0, gain=-3):
    png = cache(f'{PNG}{name}.png', lambda o: rr().dark_title(eyebrow, title, o, sub))
    return E.make(name, D, 'dark', [(png, 0, None, False)], audio=[(JG[jingle][0], None, None, jat, gain)]), E.snap(D)
def kfile(f, name):
    o = E.B + name + '.mov'
    if not os.path.exists(o):
        n = round(E.dur(f) * 30); E.run(['ffmpeg', '-y', '-v', 'error', '-i', f, '-vf', 'scale=1920:1080,fps=30,format=yuv420p', '-af', f'aresample=48000,aformat=channel_layouts=stereo,apad=whole_len={n*1600},atrim=end_sample={n*1600}', '-frames:v', str(n), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '14', '-c:a', 'pcm_s16le', o])
    return o, E.dur(o)
def build(name, nxt=None):
    """restituisce (file, durata)"""
    nextprof = nxt is not None and nxt.startswith('D')
    if name == 'SIG': return kfile('/home/user/Lezioni/kit/sigle/Sigla_Storia_15s.mp4', 'SIG')
    if name == 'SF': return kfile('/home/user/Lezioni/kit/sigle/Sigla_finale_5s_con_avviso_diritti.mp4', 'SF')
    if name == 'COVER':
        return kore('COVER', 'V0_BENVENUTO', None, lambda k: S.png_cover(False), start_j='trans', end_j='trans', hold=1.2, v0=1.9)
    if name.startswith('D'): return S.scene_prof(name)
    if name[0] == 'T': a = int(name[1]); return card_scene(name, f'Argomento {a}', ARGO[a], None, 'titolo', 3.3, 0.1)
    if name[0] == 'Q': a = int(name[1]); return card_scene(name, f'Quiz · {a}', ARGO[a], '5 domande · per continuare serve almeno l’80%', 'quiz', 4.0, 0.5, 0)
    if name == 'VF': return card_scene('VF', 'Verifica di sbarramento', 'Verifica finale', '10 domande · per continuare serve almeno l’80%', 'quiz', 4.0, 0.5, 0)
    if name == 'CI': return card_scene('CI', 'Alla fine della lezione', 'Compiti', None, 'finale', 3.5, 0.1, -4)
    if name.startswith('AN'):
        ey, ti, lines, imgs = AN[name]
        return kore_lines(name, name, ey, ti, [l for l, m in lines], [m for l, m in lines], 'trans', 'trans' if nextprof else None, imgs=imgs)
    if name.startswith('PILL'):
        a = int(name[-1]); ey, ti, lines = PILL[a]
        return kore_lines(name, name, ey, ti, [l for l, m in lines], [m for l, m in lines], 'repaso', None, fs=40)
    if name == 'MAPPA': return scene_mappa()
    if name == 'GLOSS': return kore('GLOSS', 'GLOSS', [m for _, _, m in GL], render_gloss, 'trans', None)
    if name == 'RF': return kore('RF', 'RF', [m for _, _, m in RF], render_rf, 'trans', None)
    if name == 'COMPITI':
        return kore('COMPITI', 'COMPITI', ['Compito uno', 'Compito due', 'Compito tre', 'Compito quattro', 'Svolgi i compiti'], render_comp, None, None, hold=2.0, v0=0.6)
    raise KeyError(name)
if __name__ == '__main__':
    import time
    tl = []; lst = []; t = 0.0
    names = sys.argv[1:] or PI.SEQ
    for i, n in enumerate(PI.SEQ):
        if n not in names: continue
        t0 = time.time(); f, d = build(n, PI.SEQ[i + 1] if i + 1 < len(PI.SEQ) else None)
        print(n, round(d, 2), round(time.time() - t0), 's', flush=True)
    if not sys.argv[1:]: json.dump(S.META, open(E.W + 'build/meta.json', 'w'))
