from pieces import *
from voice import prepare,starts,real
from numconv import num_words
import re,html as _h
TEXTS={}
def load_texts():
    for p in (W+'/vox/scambio/storia-V-lez16/testi_voci.json',):
        for d in json.load(open(p)):TEXTS[d['nome']]=d['testo']
    # testi nuovi non ancora presenti nel file letto
    import nuove_voci
    for d in nuove_voci.N:TEXTS[d['nome']]=d['testo']
load_texts()
REDONE={'BENV1','AP1','MD1','MD2','MD3'}
def vname(base):
    """voci rifatte: se esiste la versione _R2 si usa quella; senza nome del prof: _R2 anche provvisoria; le altre l'originale"""
    if real(base+'_R2'):return base+'_R2'
    return base+'_R2' if base in REDONE else base
def sentences(t):
    t=t.replace('F. K','F.§K')
    return [s.strip().replace('§',' ') for s in re.split(r'(?<=[.?!])\s+',t) if s.strip()]
def screen(t):return num_words(t)
# ------------ composizione di un pezzo ------------
def compose(nome,states,audios,D,prev_png,blue=False,sfx=None):
    """states: [(t_sec,png)] ; audios: [(t_sec,wav)] ; D secondi. blue: sfondo animato + stati trasparenti"""
    out=f'{OUT}/{nome}.mkv';nF=fr(D);Dq=nF/FPS
    st=[(fr(t),p) for t,p in states];st[0]=(0,st[0][1])
    sa,sf,sm=still_inputs(st,nF,'rgba' if blue else 'yuv420p')
    inp=list(sa);fc=[sf];k=sm
    if blue:
        bg=B+'/png/blu_bg.png'
        inp+=['-loop','1','-framerate','30','-t',f'{Dq:.3f}','-i',bg];fc.append(f"[{k}:v]crop=1920:1080:x='(iw-1920)/2+(iw-1920)/2*sin(t/2.7)':y='(ih-1080)/2+(ih-1080)/2*sin(t/3.3+1)',fps=30[bgv];[bg]fade=t=in:st=0.1:d=0.45:alpha=1[fg];[bgv][fg]overlay=0:0:eof_action=pass,format=yuv420p[vbase]");k+=1
    else:fc.append("[bg]format=yuv420p[vbase]")
    labs=[]
    sounds=[(0.0,SND+'trans.wav')]+(sfx or [])+audios
    for i,(t,w) in enumerate(sounds):
        inp+=['-i',w];ms=int(t*1000);fc.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=stereo,adelay={ms}|{ms}[s{i}]");labs.append(f'[s{i}]');k+=1
    fc.append(''.join(labs)+f"amix=inputs={len(labs)}:normalize=0:duration=longest,apad,atrim=0:{Dq:.4f}[am]")
    vmap='[vbase]'
    if prev_png:
        inp+=['-loop','1','-t','0.4','-i',prev_png];fc.append(trans_filter(str(k),'vout'));vmap='[vout]'
    cmd=['ffmpeg','-v','error','-y']+inp+['-filter_complex',';'.join(fc),'-map',vmap,'-map','[am]','-t',f'{Dq:.4f}']+V_ENC+A_ENC+[out]
    sh(cmd);return out,Dq
def ensure_blu_bg():
    p=B+'/png/blu_bg.png'
    if not os.path.exists(p):
        open(B+'/html/blu_bg.html','w').write(blu_bg().replace('1920px','2400px').replace('1080px','1400px').replace('inset:0','left:0;top:0;width:2400px;height:1400px'))
        json.dump([dict(html=B+'/html/blu_bg.html',out=p,w=2400,h=1400)],open(B+'/jobs_bg.json','w'))
        subprocess.run(['node',B+'/render.js',B+'/jobs_bg.json'],cwd=B)
LEAD=0.9;TAIL=1.3
def vdur(name,text):
    return prepare(name,text)[1]
