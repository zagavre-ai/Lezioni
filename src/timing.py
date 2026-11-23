"""Tempi dalle voci. wav_words(nome) -> lista [(t,parola)] della voce (vera trascritta con trascrivi.py, oppure provvisoria stimata).
align(attese, words) -> per ogni gruppo di parole attese, (inizio, fine) in secondi nella voce.
Le voci vere stanno in /tmp/w/vox/NOME.wav (da scambio/<tag>/vox/ della master); le provvisorie in /tmp/w/vox_prov/NOME.wav (silenzio stimato a 2.6 parole/s)."""
import os,re,json,subprocess,difflib,wave
V_REAL='/tmp/w/vox'; V_PROV='/tmp/w/vox_prov'; CACHE='/tmp/w/vox_words'
os.makedirs(CACHE,exist_ok=True)
def norm(w): return re.sub(r"[^\wàèéìòùç]+","",w.lower())
def words_of(text): return [w for w in re.split(r"\s+",text.strip()) if norm(w)]
def voice_path(nome):
    for d in (V_REAL,V_PROV):
        p=f'{d}/{nome}.wav'
        if os.path.exists(p): return p
    raise FileNotFoundError(nome)
def is_real(nome): return os.path.exists(f'{V_REAL}/{nome}.wav')
def dur(nome):
    with wave.open(voice_path(nome)) as w: return w.getnframes()/w.getframerate()
def wav_words(nome,testo):
    """[(t,parola)] ; voce vera: trascritta (cache); provvisoria: stima proporzionale ai caratteri."""
    p=voice_path(nome)
    if not is_real(nome):
        W=words_of(testo); tot=sum(len(norm(w))+1 for w in W); d=dur(nome)-0.4; t=0.2; out=[]
        for w in W: out.append((t,w)); t+=d*(len(norm(w))+1)/tot
        return out
    c=f'{CACHE}/{nome}.json'
    if not os.path.exists(c):
        subprocess.run(['python3','/home/user/Lezioni/kit/tools/trascrivi.py',p,f'{CACHE}/{nome}'],check=True,env={**os.environ,'TELESIO_ASR':'/tmp/asr'})
    S=json.load(open(c)); out=[]
    for s in S:
        for t,w in s['parole']:
            if (w.startswith(' ') or not out) and norm(w): out.append([t,w.strip()])
            elif out: out[-1][1]+=w.strip()
    return [(t,w) for t,w in out if norm(w)]
def align(attese,words):
    """attese: lista di stringhe (blocchi di testo in ordine). Ritorna [(inizio,fine)] per blocco, con difflib sulle parole normalizzate."""
    exp=[];idx=[]
    for i,b in enumerate(attese):
        for w in words_of(b): exp.append(norm(w)); idx.append(i)
    got=[norm(w) for t,w in words]
    sm=difflib.SequenceMatcher(None,exp,got,autojunk=False)
    m={}                      # indice atteso -> indice trascritto
    for a,b,n in sm.get_matching_blocks():
        for k in range(n): m[a+k]=b+k
    # interpola le parole non abbinate
    keys=sorted(m); res=[None]*len(exp)
    for i in range(len(exp)):
        if i in m: res[i]=m[i]
        else:
            lo=[k for k in keys if k<i]; hi=[k for k in keys if k>i]
            if lo and hi: res[i]=m[lo[-1]]+(m[hi[0]]-m[lo[-1]])*(i-lo[-1])/(hi[0]-lo[-1])
            elif lo: res[i]=m[lo[-1]]+(i-lo[-1])
            elif hi: res[i]=max(0,m[hi[0]]-(hi[0]-i))
            else: res[i]=i
    out=[]; 
    for bi in range(len(attese)):
        ii=[i for i in range(len(exp)) if idx[i]==bi]
        a=res[ii[0]]; b=res[ii[-1]]
        ia=min(int(round(a)),len(words)-1); ib=min(int(round(b)),len(words)-1)
        t0=words[ia][0]; t1=(words[ib+1][0] if ib+1<len(words) else dur_total(words)) 
        out.append((t0,t1))
    return out
def dur_total(words): return words[-1][0]+0.6
