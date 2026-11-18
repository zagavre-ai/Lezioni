# sottotitoli.py WORK N  — .vtt della Parte N: parlato della prof (dalla trascrizione con i tempi, ricollocata nel video finale) + voce Kore (testi noti, tempi dalle durate)
# blocchi da max 2 righe x 42 caratteri, 1-6 s. Termini corretti a mano dove la trascrizione automatica sbaglia.
import sys,os,json,re,subprocess
QUI=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,QUI);sys.path.insert(0,QUI+'/..')
import contenuti as C
W=os.path.abspath(sys.argv[1]);N=int(sys.argv[2])
TL=json.load(open(f'{W}/out/Diritto_4222_Parte{N}_1080p_timeline.json'))
TR=json.load(open(QUI+'/../../../diritto-4222/trascr.json'))
SRC={'C0':(0,9.6),'T1':(139,508),'T2':(543,1400),'T3':(1410,1469),'T4':(1474,1653),'T5':(1658,2001),'T6':(2011,2387),'T7':(2482,2604)}
FIX=[(r'\babbiamento\b','avviamento'),(r'\bAbbiamento\b','Avviamento'),(r'\bl\'abbiamento\b',"l'avviamento"),(r'ISO 3100\b','ISO 31000'),(r'\bUni ISO\b','UNI ISO'),(r'\bTeleton\b','Telethon'),(r'\bstellantis\b','Stellantis'),(r'\bFiat\b','Fiat'),(r'\bseguro\b','seguito'),(r'\bstakeholders\b','stakeholder'),(r'\bCSRD\b','CSRD')]
def fix(t):
    for a,b in FIX:t=re.sub(a,b,t)
    return t
def dur(f):return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)
def vd(k):return dur(f'{W}/vp/{k}.wav')
def chunk(text,a,b):
    """spezza testo in blocchi (<=84 caratteri su 2 righe di <=42), tempi proporzionali ai caratteri"""
    w=text.split();out=[];cur=''
    for x in w:
        if len((cur+' '+x).strip())>84:out.append(cur);cur=x
        else:cur=(cur+' '+x).strip()
    if cur:out.append(cur)
    tot=sum(len(c) for c in out) or 1;t=a;res=[]
    for c in out:
        d=(b-a)*len(c)/tot;res.append((t,t+d,c));t+=d
    return res
def due_righe(c):
    if len(c)<=42:return c
    w=c.split();best=None
    for i in range(1,len(w)):
        a,b=' '.join(w[:i]),' '.join(w[i:])
        s=max(len(a),len(b))
        if best is None or s<best[0]:best=(s,a,b)
    return best[1]+'\n'+best[2]
cues=[];seen=set()
def kore(t0,key,text=None,gap=0):
    d=vd(key);txt=text or json.load(open(QUI+'/../testi_voci.json'))[key][0]
    # sul video mostro il testo originale (con le sigle), non la versione per la voce
    return d
def orig(key):
    # testo da mostrare: ricostruito dai contenuti
    m=re.match(r'^(N\d[a-f])_s(\d+)_i(\d+)$',key)
    if m:return C.ANIM[m.group(1)]['slides'][int(m.group(2))-1]['items'][int(m.group(3))-1]['say']
    m=re.match(r'^S(\d)_(\d)$',key)
    if m:return C.SCHEMI_VOCE[int(m.group(1))][int(m.group(2))-1]
    m=re.match(r'^M(\d)_(\d)$',key)
    if m:return C.MAPPE[int(m.group(1))]['intro'] if m.group(2)=='0' else C.MAPPE[int(m.group(1))]['rami'][int(m.group(2))-1][3]
    m=re.match(r'^MF_(\d)$',key)
    if m:return C.MAPPA_FINALE['intro'] if m.group(1)=='0' else C.MAPPA_FINALE['rami'][int(m.group(1))-1][3]
    m=re.match(r'^R(\d)$',key)
    if m:return C.PILLOLA_ANNUNCIO[int(m.group(1))]
    m=re.match(r'^F_(\d)$',key)
    if m:return C.RIEPILOGO_VOCE[int(m.group(1))]
    m=re.match(r'^RP_(\d)$',key)
    if m:return C.RIPASSO_P1[int(m.group(1))]
    if key=='W01':return C.BENVENUTO
def add(t0,key):
    d=vd(key)
    for a,b,c in chunk(orig(key),t0,t0+d):cues.append((a,b,c))
    return d

def parole(a0,a1):
    W_=[]
    for sg in TR:
        cur=None
        for t,tok in sg['parole']:
            if tok.startswith(' ') or cur is None:
                if cur:W_.append(cur)
                cur=[t,tok.strip()]
            else:cur[1]+=tok
        if cur:W_.append(cur)
    return [(t,w) for t,w in W_ if a0-0.01<=t<a1 and w]
def blocchi(a0,a1,off):
    ws=parole(a0,a1);out=[];cur=[];
    for i,(t,w) in enumerate(ws):
        cur.append((t,w));txt=' '.join(x[1] for x in cur)
        nxt=ws[i+1][0] if i+1<len(ws) else a1
        fine=len(txt)>=60 or w[-1:] in '.?!' or (nxt-t>0.7 and len(txt)>25) or i==len(ws)-1
        if fine:
            out.append((cur[0][0]+off,min(nxt,cur[-1][0]+1.2)+off if nxt-t>1.0 else nxt+off,fix(txt)));cur=[]
    return out
seenT=set()
for nome,start,dd in TL:
    if nome=='cover':add(start+0.9,'W01')
    elif re.match(r'^T\d$',nome):
        if dd<10:continue   # titolo: nessuna voce
        a0,a1=SRC[nome];cues.extend(blocchi(a0,a1,start-a0))
    elif nome=='C0':
        cues.extend(blocchi(0,9.6,start))
    elif nome.startswith('N'):
        t=start+0.9
        for si,s in enumerate(C.ANIM[nome]['slides'],1):
            for ii in range(1,len(s['items'])+1):
                d=add(t,f'{nome}_s{si}_i{ii}');t+=d+0.4
            t+=0.8
    elif re.match(r'^S\d$',nome):
        t=start+1.0
        for i in range(1,7):d=add(t,f'{nome}_{i}');t+=d+2.5
    elif re.match(r'^R\d$',nome):add(start+0.9,nome)
    elif re.match(r'^(M\d|MF)$',nome):
        t=start+0.9
        for i in range(0,7):
            if i>6:break
            try:d=add(t,f'{nome}_{i}')
            except Exception:break
            t+=d+0.5
    elif nome=='FIN':
        t=start+0.9
        for i in range(len(C.RIEPILOGO_VOCE)):d=add(t,f'F_{i}');t+=d+0.35
    elif nome=='RP':
        t=start+0.9
        for i in range(len(C.RIPASSO_P1)):d=add(t,f'RP_{i}');t+=d+0.35
cues.sort()
def ts(x):h=int(x//3600);m=int(x%3600//60);s=x%60;return '%02d:%02d:%06.3f'%(h,m,s)
out=['WEBVTT','']
for a,b,c in cues:
    if b-a<0.8:b=a+0.8
    out+=[f'{ts(a)} --> {ts(b)}',due_righe(c),'']
open(f'{W}/out/Diritto_4222_Parte{N}.vtt','w').write('\n'.join(out))
print(N,len(cues),'blocchi')
