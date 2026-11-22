# Lezione 8 · L'Espressionismo · libreria comune
import json, re, os, subprocess, bisect
W='/tmp/w'; B='/tmp/w/b'; KIT='/home/user/Lezioni/kit'
ORIG=f'{W}/v/LEZIONE.8.L.ESPRESSIONISMO.mp4'
TRASC=json.load(open(f'{W}/t/trasc.json'))
def sh(c, **k): return subprocess.run(c, shell=isinstance(c,str), capture_output=True, text=True, **k)
# frasi con tempi (dai segni di punteggiatura della trascrizione)
def frasi():
    out=[]; cur=[]; 
    for s in TRASC:
        for t,w in s['parole']:
            if w.strip() in ('.','?','!'):
                if cur: out.append({'i':cur[0][0],'f':t,'testo':re.sub(r'\s+([,.?!])',r'\1',''.join(x[1] for x in cur)).strip()}); cur=[]
            else: cur.append((t,w))
        # fine segmento senza punto: la frase continua nel segmento dopo
    if cur: out.append({'i':cur[0][0],'f':TRASC[-1]['fine'],'testo':''.join(x[1] for x in cur).strip()})
    return out
FR=frasi(); FI=[f['i'] for f in FR]
def frase_a(t):  # indice della frase che comincia in o subito dopo t
    return min(bisect.bisect_left(FI,t),len(FR)-1)
def snap_inizio(t, tol=3.0):
    """inizio di frase piu' vicino a t (entro tol), altrimenti t"""
    j=frase_a(t); c=[FR[k]['i'] for k in (j-1,j) if 0<=k<len(FR)]
    b=min(c,key=lambda x:abs(x-t)); return b if abs(b-t)<=tol else t
def fine_frase_prima(t):
    """tempo di fine dell'ultima frase che finisce entro t"""
    j=bisect.bisect_right([f['f'] for f in FR],t)-1; return FR[j]['f'], FR[j]
