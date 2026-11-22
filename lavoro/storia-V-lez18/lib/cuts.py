import json,sys
sys.path.insert(0,'/home/user/work18/lib')
from asm import W
sys.path.insert(0,'/home/user/Lezioni/kit/tools')
from taglio import snap,level
SEG=json.load(open(W+'/lavoro-storia-V-lez18/trasc18.json'))
WAV=W+'/a/prof_raw.wav'
WORDS=[(w[0],w[1]) for s in SEG for w in s['parole']]
def prev_end(T):
    e=max((s['fine'] for s in SEG if s['fine']<=T+0.05),default=0);return e
def cut(T,lead=True):
    """punto di taglio nella pausa prima della frase che comincia a T"""
    pe=prev_end(T);before=max(0.15,min(1.0,T-pe+0.1))
    c=snap(T,WAV,before,0.0)
    return round(round(c*30)/30,4)
def info(c):
    prev=[w for w in WORDS if w[0]<c];nxt=[w for w in WORDS if w[0]>=c]
    return (prev[-1][0] if prev else None,nxt[0][0] if nxt else None,level(c,WAV))
def last_words(c,k=8):
    ws=[w[1].strip() for w in WORDS if w[0]<c][-k*2:]
    return ''.join(' '+x if x.startswith(' ') else x for x in ws).strip()[-70:]
