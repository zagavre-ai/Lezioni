# Sottotitoli .vtt dal video FINALE, solo sui pezzi del docente (D*), Whisper «base», con i nomi corretti dalle slide.
# uso: python3 sub.py NN video.mp4 timeline.json uscita.vtt
import sys,json,subprocess,re,numpy as np
from faster_whisper import WhisperModel
NN,V,TL,OUT=sys.argv[1:5]
FIX={'07':[(r'\b[Hh]?[Uu]i?s?mans?\b|Wiesman|Wismance|Uismans|\busmo\b','Huysmans'),(r'[Dd]es?\s?[Ee]ss?[ae]nt\w*|Desessant\w*','Des Esseintes'),(r'[Dd]orian\s?[Gg]r[ae][iy]','Dorian Gray'),(r'Oscar\s?[WV]\w+','Oscar Wilde'),(r'\b[Ww]i?e?sman\w*','Huysmans'),(r'\b[Oo]?scar [Ww]ild\b','Oscar Wilde'),(r'\b[Gg]razie (del?l?)[\' ]?[Ee]dda\b','Grazia Deledda'),(r'\b[Dd]ell?\'?[Ee]dda\b|[Dd]el[ae]dda','Deledda'),(r'[Gg]razi[ae] [Dd]eledda','Grazia Deledda'),(r'[Cc]ontro corrente','Controcorrente'),(r'\b[Zz]ol[aà]\b','Zola'),(r'[Rr]askin','Ruskin'),(r'[Ee]lias [Pp]ort\w+','Elias Portolu'),(r'[Nn]uoro','Nuoro'),(r'800 esca','ottocentesca'),(r'[Ii]nglielterla|Ingliel?terra','Inghilterra')],
     '12':[(r'[Bb]erg?ks?on','Bergson'),(r'[Ff]r[eo]i?u?d\b','Freud'),(r'[Nn]i?e?t?z?c?h?ce\b|Nice\b','Nietzsche'),(r'[Ee]instein|Ainstain','Einstein'),(r'[Pp]rou?st\w?','Proust'),(r'[Kk]af?ca\b','Kafka'),(r'[Vv]irginia [WV]\w+','Virginia Woolf'),(r'\b[WV]olf\b|\bWoolfe?\b','Woolf'),(r'[Gg]reg[oó]r? [Ss]a[mn]s\w*','Gregor Samsa'),(r'[Dd]allo\w*','Dalloway'),(r'[Ss]hakesp\w+|[Ss]cespir','Shakespeare'),(r'[Bb]loomsbury\w*|[Bb]lum\s?sbury','Bloomsbury')],'18':[(r'\b[Mm]ontan[ae]\b','Montale'),(r'[Uu]n ?garetti','Ungaretti'),(r'[Pp]i ?landello','Pirandello'),(r'[Vv]ie[us]+[eò]\w*|[Vv]essor','Vieusseux'),(r'[Dd]rusill?a ?[Tt]an[sz]i','Drusilla Tanzi'),(r'[Ss]enia\b|[Gg]senia','Xenia'),(r'\b900\b','Novecento'),(r'[Ss]oppi di seppia|[Oo]ssi di sepia','Ossi di seppia')],
 '23':[(r'[Pp]rimo [Ll]e[vw]i\b','Primo Levi'),(r'[Aa]u?sc?h?wi[tc]+z?\w*','Auschwitz'),(r'[Gg]iustizia e [Ll]ibert[aà]','Giustizia e Libertà')]}[NN]
tl=json.load(open(TL));segs=[(t,t+l) for n,t,l in tl if n.startswith('D') and l>1.0]
a=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',V,'-vn','-ac','1','-ar','16000','-f','s16le','-'],capture_output=True).stdout,np.int16).astype(np.float32)/32768
m=WhisperModel('base',device='cpu',compute_type='int8',cpu_threads=2);W=[]
for s0,s1 in segs:
    x=a[int(s0*16000):int(s1*16000)]
    r,_=m.transcribe(x,language='it',word_timestamps=True,vad_filter=True)
    for s in r:
        for w in s.words:
            if s0+w.end<=s1:W.append([s0+w.start,s0+w.end,w.word])
# blocchi: max 84 caratteri (2x42), 1-6 s, spezzati su pause >0,5 s e punteggiatura
B=[];cur=[]
for w in W:
    if cur and (w[0]-cur[-1][1]>0.5 or len(''.join(x[2] for x in cur+[w]))>84 or w[1]-cur[0][0]>6):B.append(cur);cur=[]
    cur.append(w)
    if re.search(r'[.?!]$',w[2].strip()) and w[1]-cur[0][0]>=1:B.append(cur);cur=[]
if cur:B.append(cur)
def ts(t):return '%02d:%02d:%06.3f'%(t//3600,t%3600//60,t%60)
def wrap(s):
    if len(s)<=42:return s
    k=s.rfind(' ',0,len(s)//2+8);return s[:k]+'\n'+s[k+1:]
L=['WEBVTT','']
a8=a[::2];e=np.convolve(a8**2,np.ones(400)/400,'same');thr=np.percentile(e,60)
def onset(t):
    i0=int(max(0,t-0.8)*8000);seg=e[i0:int((t+0.8)*8000)]
    if not (seg>thr).any():return t
    o=i0/8000+np.argmax(seg>thr)/8000
    return o
prev=0
for b in B:
    tx=''.join(x[2] for x in b).strip();tx=re.sub(r"\s+'","'",tx);tx=re.sub(r'\s+',' ',tx)
    for p,r in FIX:tx=re.sub(p,r,tx)
    t0=max(onset(b[0][0]),prev+0.01);t1=max(b[-1][1],t0+1.0)
    L+=[f'{ts(t0)} --> {ts(t1)}',wrap(tx),''];prev=t1
open(OUT,'w').write('\n'.join(L));print('blocchi',len(B))
