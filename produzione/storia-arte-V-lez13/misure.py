import sys,os,json,re
sys.path.insert(0,'/tmp/claude-0/w/prod')
import build_lez as B
from eng import *
from subs import fix
IT=B.ITEMS;S=json.load(open(W+'/fin/starts.json'))['start']
mm=lambda t:'%d:%04.1f'%divmod(round(t*10)/10,60)
def ratio(x,sr=SR):
    X=np.abs(np.fft.rfft(x*np.hanning(len(x))))**2;f=np.fft.rfftfreq(len(x),1/sr)
    return 10*np.log10(X[f>4000].sum()/X[f>100].sum())
# 1) tabella tagli
rows=[]
for i,it in enumerate(IT):
    if it.kind!='prof':continue
    iv,good=keep(it.src_a,it.src_b)
    first=fix(good[0][0]['testo']);last=fix(good[-1][0]['testo'])
    w=last.split()[-8:];fin=bool(re.search(r'[.?!…]\s*$',last)) 
    t_end=S[i]/FPS+it.nf/FPS-0.4
    rows.append((it.name,mm(S[i]/FPS+0.4),mm(t_end),' '.join(first.split()[:6]),' '.join(w),'sì' if fin else 'NO (controllare)'))
json.dump(rows,open(W+'/fin/tabella_tagli.json','w'),ensure_ascii=False,indent=0)
for r in rows:print(' | '.join(r))
# 2) timbre
src=audio_load(SRC)  # tutta la sorgente (stereo)
def mono(x):return x.mean(1)
res=[]
final=audio_load(W+'/fin/audio.wav') if os.path.exists(W+'/fin/audio.wav') else None
o=[];f=[]
for i,it in enumerate(IT):
    if it.kind!='prof' or final is None:continue
    seg=[]
    for (a,n) in it.fr:seg.append(src[int(a*SR):int((a+n/FPS)*SR)])
    so=mono(np.concatenate(seg))
    s0=int((S[i]/FPS+0.4)*SR);sf=mono(final[s0:s0+len(so)])
    # solo pezzi lunghi >20 s e parlato (energia)
    if len(so)>20*SR:
        o.append(ratio(so[:20*SR]));f.append(ratio(sf[:20*SR]))
print('timbre (>4kHz rispetto a >100Hz) originale: media %.1f dB  finale: media %.1f dB  differenza %.1f dB'%(np.mean(o),np.mean(f),np.mean(f)-np.mean(o)))
json.dump({'orig':o,'fin':f},open(W+'/fin/timbre.json','w'))
