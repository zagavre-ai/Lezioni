# Sottotitoli .vtt sul video finale: docente = trascrizione automatica con correzione dei nomi; Kore = testo esatto
import sys, os, re, json
sys.path.insert(0, '/tmp/claude-0/w/build')
import asr
from scenes import TXT, digits, voice, sentences, norm_join
OUT = '/tmp/claude-0/w/out/'

FIX = [(r'\bla nouveau\b', "l'Art Nouveau"), (r'\b(?:Fov|Fove|Foves|FOV|Fovs|Vov|Fauve)\b\.?', 'Fauves'), (r'\b(?:Mathis|Matis|Mattis|Matiss|Matiz|Mathisse)\b', 'Matisse'),
       (r'\b(?:Brac|Brach|Bracq|Bach|Wack|Bracque|Brack|Brague)\b', 'Braque'), (r'\bCézanne|Cezanne|Cèzanne|Cesanne\b', 'Cézanne'),
       (r'\b(?:Shagal|Chagal|Sciagall|Chagall)\b', 'Chagall'), (r'\bModigliani|Migliani|Modiliani\b', 'Modigliani'), (r'\b(?:Delone|Deloné|Delonay|Delaunay)\b', 'Delaunay'),
       (r'\bTuve Eiffel|Tour Eiffel|Torre Eiffel\b', 'Tour Eiffel'), (r'\b(?:Vlaming|Devlaming|Vlaminc)\b', 'Vlaminck'), (r'\bDérène|Derene|Derrain|Derain\b', 'Derain'),
       (r'\b(?:Vos se lei|Vo se lei|Voss e lei|Vos e lei|Vose lei|Vauxcelles)\b', 'Vauxcelles'), (r'\bpapi de coup[eé]|papier d[eé] coup[eé]\b', 'papiers découpés'),
       (r'\bpapi col[eè]|papier col[eè]\b', 'papiers collés'), (r'\bSalon d.Autunne|Salon d.Hauton|salon des Hautomne\b', "Salon d'Automne"), (r'\bShuskin|Scukin|Shukin|Schuchin\b', 'Shchukin'),
       (r'\bMax Jacob et\b', 'Max Jacob e'), (r'\bApolliner|Apollinaire\b', 'Apollinaire'), (r'\bArcepco|Archipenco|Arcipenko\b', 'Archipenko'), (r'\bBrancusi\b', 'Brâncuși'),
       (r'\bGleises|Gleizes\b', 'Gleizes'), (r'\bMetzinger\b', 'Metzinger'), (r'\bLéger|Leger\b', 'Léger'), (r'\bDoganiere\b', 'Doganiere'), (r'\bKees van Duggen\b', 'Kees van Dongen'),
       (r'\bRaul Dufi\b', 'Raoul Dufy'), (r'\bChambodelet|Chambodele\b', 'Baudelaire'), (r'\bSaint Cope\b', 'Saint-Tropez'), (r'\bSignac|Cignac\b', 'Signac')]

def fixtxt(t):
    for a, b in FIX: t = re.sub(a, b, t)
    return t

def cues_from_words(words, t0, maxc=42, maxd=6.0):
    """words: [(t, parola)] relativi al segmento -> cue [(inizio, fine, testo)] in tempo assoluto"""
    cues = []; cur = []
    def flush(end):
        nonlocal cur
        if not cur: return
        txt = ' '.join(w for _, w in cur); lines = []; line = ''
        for w in txt.split():
            if len(line) + len(w) + 1 > maxc and line: lines.append(line); line = w
            else: line = (line + ' ' + w).strip()
        lines.append(line)
        cues.append((t0 + cur[0][0], t0 + min(end, cur[0][0] + maxd), '\n'.join(lines[:2]) if len(lines) <= 2 else '\n'.join(lines[:2]) + '\n' + ' '.join(lines[2:]))); cur = []
    for k, (t, w) in enumerate(words):
        if cur:
            gap = t - cur[-1][0]; chars = sum(len(x) + 1 for _, x in cur) + len(w)
            if gap > 0.9 or chars > 78 or (t - cur[0][0]) > maxd - 0.5 or re.search(r'[.?!]$', cur[-1][1]) and chars > 30:
                flush(min(t, cur[-1][0] + 0.9)) if False else flush(cur[-1][0] + 0.6)
        cur.append((t, w))
    flush(cur[-1][0] + 0.7 if cur else 0)
    return cues

def vtt_time(t):
    h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return '%02d:%02d:%06.3f' % (h, m, s)

def kore_words(name, lead, text=None):
    v = voice(name); fr = [x for x in re.split(r'(?<=[.!?])\s+', TXT[name].strip()) if x]
    times, wt = asr.align(v['words'], fr, span=v['span'], want_words=True)
    out = []
    for f, ts in zip(fr, wt):
        for w, t in zip(digits(f).split(), ts): out.append((lead + t, w))
    return out

def build(timeline, lead_of, out_vtt):
    """timeline: [[sid, inizio, durata]] ; lead_of(sid) -> (nome voce, ritardo voce nel segmento) per i segmenti Kore"""
    cues = []
    for sid, st, du in timeline:
        if sid.startswith('D'):
            n = sid[1:]; w = asr.words(OUT + 'teacher/T%s.wav' % n)
            words = [(float(t), fixtxt(x)) for t, x in w]
            cues += cues_from_words(words, st)
        else:
            r = lead_of(sid)
            if r: cues += cues_from_words(kore_words(*r), st)
    cues.sort()
    with open(out_vtt, 'w') as f:
        f.write('WEBVTT\n\n')
        for k, (a, b, t) in enumerate(cues):
            if k + 1 < len(cues): b = min(b, cues[k + 1][0] - 0.02)
            f.write('%s --> %s\n%s\n\n' % (vtt_time(a), vtt_time(max(b, a + 0.4)), t))
    return len(cues)
