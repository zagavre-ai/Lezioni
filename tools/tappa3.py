# Materiale della TAPPA 3 (controllo prima del montaggio finale): miniature delle slide e delle scene, tagli, sincronia.
# uso: python3 tappa3.py cartella_lezione nome_uscita   → <cartella>/tappa3/<nome>.zip
import sys,os,json,glob,subprocess,re,zipfile,numpy as np
sys.path.insert(0,'/home/claude/lezioni/tools');import taglio
from PIL import Image,ImageDraw,ImageFont
from playwright.sync_api import sync_playwright
D=os.path.abspath(sys.argv[1])+'/';NAME=sys.argv[2];O=D+'tappa3/';os.makedirs(O,exist_ok=True)
for f in glob.glob(O+'*'):os.remove(f)
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
def font(n):
    try:return ImageFont.truetype(FONT,n)
    except Exception:return ImageFont.load_default()
def sheet(items,out,cols=4,rows=2,w=480,h=270,title=''):
    pages=[];per=cols*rows
    for p in range(0,len(items),per):
        S=Image.new('RGB',(cols*(w+12)+12,rows*(h+40)+60),'#E9EDF3');d=ImageDraw.Draw(S)
        d.text((12,14),f'{title} · {p//per+1}/{(len(items)+per-1)//per}',fill='#0B1530',font=font(22))
        for i,(lab,img) in enumerate(items[p:p+per]):
            x=12+(i%cols)*(w+12);y=50+(i//cols)*(h+40)
            S.paste(Image.open(img).convert('RGB').resize((w,h)),(x,y));d.text((x,y+h+6),lab,fill='#0B1530',font=font(18))
        f=f'{out}_{p//per+1:02d}.png';S.save(f);pages.append(f)
    return pages
tmp=O+'_tmp/';os.makedirs(tmp,exist_ok=True)
# a) slide della docente (come appaiono nel video, prima frase accesa)
SL=json.load(open(D+'slides.json'));items=[]
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1920,'height':1080});pg.goto('file://'+D+'slides_spoken.html');pg.wait_for_timeout(1500)
    sh=pg.query_selector_all('.sheet')
    for i,s in enumerate(sh):
        f=tmp+f'sl{i:03d}.png';s.screenshot(path=f);items.append((f'slide {i+1} · arg {SL[i]["a"]+1 if i<len(SL) else "?"}',f))
    b.close()
A=sheet(items,O+'a_slide',title='Slide della docente')
# b) scene con voce: due fotogrammi (a metà e alla fine)
items=[]
for f in sorted(glob.glob(D+'po/S*.mp4'))+sorted(glob.glob(D+'an/AN*.mp4'))+sorted(glob.glob(D+'an/GL*.mp4'))+sorted(glob.glob(D+'an/RF*.mp4'))+sorted(glob.glob(D+'dk/*.mp4')):
    n=os.path.basename(f)[:-4];du=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)
    for lab,t in (('metà',du/2),('fine',max(0,du-2.5))):
        g=tmp+f'{n}_{lab}.png';subprocess.run(['ffmpeg','-v','error','-y','-ss','%.2f'%t,'-i',f,'-frames:v','1',g]);items.append((f'{n} · {lab}',g))
B_=sheet(items,O+'b_scene',title='Schemi, animazioni, glossario, ripasso, schede')
# c) tagli: confini dei pezzi della docente (inizio di ogni argomento) con livello e parole intorno
Aal=json.load(open(D+'align_s.json'))['align'];U=json.load(open(D+'units.json'))
W=[w for l in open(D+'pk.jsonl') for w in json.loads(l)['w']]
x=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',D+'audio/audio_B_full.wav','-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout,np.float32)
def lev(t):
    s=x[max(0,int((t-0.1)*16000)):int((t+0.1)*16000)];return round(20*np.log10(np.sqrt((s**2).mean())+1e-9),1)
def words(a,b):return ' '.join(w for t,w in W if a<=t<b)
st={}
for o in Aal:
    k=U[o['i']]['a'];st[k]=min(st.get(k,1e9),o['t'])
cuts=[]
for k in sorted(st):
    c=taglio.snap(st[k]-0.15,D+'audio/audio_B_full.wav');cuts.append((k+1,c,lev(c),words(c-4,c),words(c,c+4)))
# d) sincronia: per ogni cambio di slide la frase che si accende e le parole della docente
P=json.load(open(D+'sv_plan.json'));syn=[]
for i,t0 in enumerate(P['starts'][:len(SL)]):
    syn.append((i+1,SL[i]['a']+1,round(t0,1),U[SL[i]['ids'][0]]['txt'][:70],words(t0,t0+6)))
def mmss(t):return '%d:%04.1f'%(t//60,t%60)
R=['# Tappa 3 · '+NAME,'','## c) Tagli (inizio di ogni argomento)','','| Arg. | Taglio | Livello | Parole prima | Parole dopo |','|---|---|---|---|---|']
R+=[f'| {k} | {mmss(c)} | {l} dB | …{a[-70:]} | {b[:70]}… |' for k,c,l,a,b in cuts]
R+=['','Un livello sotto circa −40 dB = pausa. Sopra −35 dB va ascoltato.','','## d) Sincronia: cambio di slide → parole della docente nei 6 secondi dopo','','| Slide | Arg. | Tempo | Prima frase della slide | Parole della docente |','|---|---|---|---|---|']
R+=[f'| {s} | {a} | {mmss(t)} | {f} | {w[:90]} |' for s,a,t,f,w in syn]
pi=os.path.exists(D+'piene.json')
R+=['','## e) Controlli automatici','',f'- slide: {len(SL)}; slide troppo piene: vedi log della fase A ({"nessuna" if not pi else "piene.json"})',
'- numeri chiave rivisti a mano (numeri_chiave.json)','- non controllati: ascolto in cuffia dell\'audio, labiale (si fa a montaggio finito)']
open(O+'tappa3.md','w').write('\n'.join(R))
z=O+NAME+'.zip'
with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED) as Z:
    for f in A+B_+[O+'tappa3.md']:Z.write(f,os.path.basename(f))
import shutil;shutil.rmtree(tmp)
print(z,len(A),'fogli slide',len(B_),'fogli scene',len(cuts),'tagli',len(syn),'cambi di slide')
