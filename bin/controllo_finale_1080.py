# Controllo finale UNICO (uguale per tutte le chat), sul file da caricare su YouTube.
# uso: python3 tools/controllo_finale.py VIDEO.mp4 TIMELINE.json SOTTOTITOLI.vtt [--tag TAG --parte N --titolo "..." --voci kore --invia]
# timeline = [[nome, inizio_s, durata_s], ...]  (D* = pezzi del docente, Q* = schede Quiz)
# Misura: durata, fotogrammi, peso, scatto dei Quiz, fermi immagine nei pezzi del docente, volume del parlato,
# sottotitoli (sovrapposti, oltre la fine, attacco sulla voce), e fa un foglio di miniature (un fotogramma per pezzo).
# Scrive VIDEO.controllo.txt e, con --tag, aggiorna lo stato per la master (tools/stato.py).
import sys,os,json,re,subprocess,argparse,numpy as np
a=argparse.ArgumentParser();a.add_argument('video');a.add_argument('timeline');a.add_argument('vtt')
for k in ['tag','parte','titolo','voci','scheda']:a.add_argument('--'+k)
a.add_argument('--invia',action='store_true');a.add_argument('--joff',type=float,default=0.5);o=a.parse_args()
V=o.video;TL=json.load(open(o.timeline));R=[];OK={}
def sh(c):return subprocess.run(c,capture_output=True,text=True)
def say(*x):s=' '.join(str(i) for i in x);print(s,flush=True);R.append(s)
# 1. durata, fotogrammi, peso
j=json.loads(sh(['ffprobe','-v','error','-count_packets','-select_streams','v:0','-show_entries','stream=nb_read_packets,width,height:format=duration,size','-of','json',V]).stdout)
dur=float(j['format']['duration']);fr=int(j['streams'][0]['nb_read_packets']);mb=int(j['format']['size'])/1e6;w,h=j['streams'][0]['width'],j['streams'][0]['height']
OK['fotogrammi']=abs(fr-dur*30)<=3;OK['peso']=mb<=419.4;OK['risoluzione']=(w,h)==(1920,1080)
say('durata %d:%04.1f (%.1f s) | fotogrammi %d (attesi %d) %s | peso %.1f MB (%.1f MiB) %s | %dx%d %s'%(dur//60,dur%60,dur,fr,round(dur*30),'OK' if OK['fotogrammi'] else 'NO',mb,mb/1.048576,'OK' if OK['peso'] else 'NO',w,h,'OK' if OK['risoluzione'] else 'NO'))
# 2. scatto dei Quiz (correlazione con il jingle)
SR=8000
def rd(f,ss=None,d=None):
    c=['ffmpeg','-v','error']+(['-ss',str(ss),'-t',str(d)] if ss is not None else [])+['-i',f,'-ac','1','-ar',str(SR),'-f','s16le','-']
    return np.frombuffer(subprocess.run(c,capture_output=True).stdout,np.int16).astype(float)
JW=[p for p in ['/home/claude/v5/snd/quiz.wav','/home/claude/lezioni/kit/snd/quiz.wav'] if os.path.exists(p)]
qs=[(n,t) for n,t,l in TL if re.fullmatch(r'Q\d+',n)];bad=[]
if JW and qs:
    ref=rd(JW[0])[:SR*2]
    for n,t in qs:
        x=rd(V,t-1.5,5);k=int(np.argmax(np.correlate(x,ref,'valid')));sc=t-1.5+k/SR-(t+o.joff)
        if abs(sc)>0.05:bad.append((n,round(sc,3)))
    OK['quiz']=not bad;say('quiz',len(qs),'scatto 0,0 s:','OK' if not bad else 'DA CORREGGERE %s'%bad)
else:OK['quiz']=False;say('quiz: jingle di riferimento o schede Q non trovati')
# 3. fermi immagine nei pezzi del docente (freezedetect, >= 1,0 s)
fz=sh(['ffmpeg','-v','info','-i',V,'-vf','freezedetect=n=0.00005:d=1.0','-map','0:v','-f','null','-']).stderr
st=[float(x) for x in re.findall(r'freeze_start: ([\d.]+)',fz)];en=[float(x) for x in re.findall(r'freeze_end: ([\d.]+)',fz)]+[dur]
D=[(n,t,t+l) for n,t,l in TL if n.startswith('D') and l>1.0]
fd=[(round(s,1),round(e,1),n) for s,e in zip(st,en) for n,a0,b0 in D if s<b0-0.3 and e>a0+0.3]
OK['fermi']=not fd;say('fermi immagine nei pezzi del docente:','nessuno OK' if not fd else '%d DA GUARDARE %s'%(len(fd),fd[:8]))
# 4. volume del parlato del docente (ebur128 sui pezzi D)
lu=[]
for n,a0,b0 in D[:12]:
    m=re.findall(r'I:\s+(-?[\d.]+) LUFS',sh(['ffmpeg','-v','info','-ss',str(a0),'-t',str(min(b0-a0,120)),'-i',V,'-af','ebur128','-f','null','-']).stderr)
    if m:lu.append(float(m[-1]))
lv=round(float(np.median(lu)),1) if lu else None;OK['volume']=lv is not None and -17.5<=lv<=-14.5
say('volume del parlato (mediana dei pezzi del docente):',lv,'LUFS','OK' if OK['volume'] else 'FUORI (atteso circa -16)')
# 5. sottotitoli
def ts(s):h_,m_,x=s.split(':');return int(h_)*3600+int(m_)*60+float(x)
cues=[(ts(a_),ts(b_)) for a_,b_ in re.findall(r'(\d+:\d\d:[\d.]+) --> (\d+:\d\d:[\d.]+)',open(o.vtt).read())]
sov=sum(1 for i in range(1,len(cues)) if cues[i][0]<cues[i-1][1]-0.01);oltre=sum(1 for c in cues if c[1]>dur+0.1)
x16=rd(V);e=np.convolve(x16**2,np.ones(400)/400,'same');thr=np.percentile(e,60)
er=[]
for c0,c1 in cues[::max(1,len(cues)//40)]:
    i0=int(max(0,c0-0.8)*SR);seg=e[i0:int((c0+0.8)*SR)]
    if len(seg) and seg[:int(0.5*SR)].mean()<thr*0.5:  # solo blocchi che iniziano dopo una pausa
        on=np.argmax(seg>thr);er.append(abs(i0/SR+on/SR-c0))
p03=round(100*sum(1 for x in er if x<=0.3)/len(er)) if er else None
OK['sottotitoli']=len(cues)>0 and sov==0 and oltre==0 and (p03 is None or p03>=80)
say('sottotitoli: %d blocchi, sovrapposti %d, oltre la fine %d, attacco sulla voce entro 0,3 s: %s'%(len(cues),sov,oltre,'%d%% di %d verificabili'%(p03,len(er)) if er else 'non verificabile'),'OK' if OK['sottotitoli'] else 'DA GUARDARE')
# 6. foglio di miniature: un fotogramma a metà di ogni pezzo (da guardare a occhio: slide giusta, niente schermo nero)
cs=V+'.miniature.jpg';pts=[t+l/2 for n,t,l in TL if l>2][:48];fr_=[]
for i,t in enumerate(pts):
    f=f'/tmp/cf_{i:02d}.jpg';sh(['ffmpeg','-v','error','-y','-ss',str(t),'-i',V,'-frames:v','1','-vf','scale=320:-2',f]);fr_.append(f)
if fr_:sh(['ffmpeg','-v','error','-y','-framerate','1','-i','/tmp/cf_%02d.jpg','-vf','tile=6x%d'%((len(fr_)+5)//6),'-frames:v','1',cs]);[os.remove(f) for f in fr_]
say('foglio di miniature:',cs)
tutto=all(OK.values());say('ESITO:','TUTTO OK' if tutto else 'DA SISTEMARE: '+', '.join(k for k,v in OK.items() if not v))
open(V+'.controllo.txt','w').write('\n'.join(R)+'\n')
if o.tag and o.parte:
    c=[sys.executable,'/home/claude/lezioni/tools/stato.py',o.tag,'--parte',str(o.parte),'--video',V,'--vtt',o.vtt,
       '--quiz_ok','si' if OK['quiz'] else 'no','--fermi_ok','si' if OK['fermi'] else 'no','--sub_ok','si' if OK['sottotitoli'] else 'no',
       '--stato','PRONTA' if tutto else 'IN_MONTAGGIO','--nota','controllo_finale: '+R[-1]]
    if o.titolo:c+=['--titolo',o.titolo]
    if o.voci:c+=['--voci',o.voci]
    if o.scheda:c+=['--scheda',o.scheda]
    c+=['--timeline',o.timeline]
    if o.invia:c+=['--invia']
    print(sh(c).stdout[-300:])
