import json,sys,os,subprocess,wave,numpy as np
sys.path.insert(0,'/tmp/w14/build');sys.path.insert(0,'/tmp/w14')
import gen
gen.PROFON=False;gen.DARK=True
E=gen.E
ENC=['-c:v','libx264','-preset','veryfast','-crf','19','-pix_fmt','yuv420p','-r','30','-an','-x264-params','keyint=60:scenecut=0','-threads','2']
def rd(f):
    w=wave.open(f);a=np.frombuffer(w.readframes(w.getnframes()),np.int16).reshape(-1,2);w.close();return a
def wr(f,a):
    w=wave.open(f,'wb');w.setnchannels(2);w.setsampwidth(2);w.setframerate(48000);w.writeframes(a.astype(np.int16).tobytes());w.close()
comp=json.load(open('/tmp/w14/out/compiti.json'))['esercizi']
T=json.load(open('/tmp/w14/tr/COMPITI.json'))
def start_of(tag):
    for s in T:
        if s['testo'].lower().startswith(tag): return s['inizio']
st=[start_of(f'compito {i}') or start_of(f'compito {["uno","due","tre","quattro"][i-1]}') for i in (1,2,3,4)]
st=[1.5,20.0,34.5,49.1]  # tempi misurati dalla trascrizione della voce
fin=68.3
OFF=0.6;VD=74.56;n_comp=round((OFF+VD+0.8)*30)
def page_html(k):
    if k==0: eyebrow='COMPITI';title='Compiti';body_cards=''
    body=f'<div style="position:absolute;left:80px;top:146px;width:1760px"><div class="lab">COMPITI</div><div class="tit" style="margin-top:34px">{"Compito "+str(k) if 1<=k<=4 else "Compiti"}</div><div class="bar"></div><div style="margin-top:44px">'
    if 1<=k<=4:
        t=comp[k-1]['testo']
        body+=f'<div class="card nc on" style="font-size:40px;line-height:1.5;padding-top:24px;padding-bottom:24px"><div class="n">{k}</div><div>{E(t)}</div></div>'
    elif k==5:
        body+='<div class="card nc on" style="font-size:40px;line-height:1.5;padding-top:24px;padding-bottom:24px"><div class="n">✓</div><div>Svolgi i compiti qui sotto e premi Consegna: arrivano al docente nel tuo quaderno dei compiti.</div></div>'
    body+='</div></div>'
    return gen.page(body,32,prof=False)
for k in range(6): gen.scrivi(f'compiti_{k}',page_html(k))
subprocess.run(['node','/tmp/w14/build/render.js','/tmp/w14/build/html','/tmp/w14/build/png'],check=True)
bounds=[0]+[round((OFF+x)*30) for x in st]+[round((OFF+fin)*30),n_comp]
parts=[]
for k in range(6):
    f=bounds[k+1]-bounds[k]
    po=f'/tmp/w14/vc/c{k}.mp4';subprocess.run(['ffmpeg','-v','error','-y','-loop','1','-framerate','30','-t',f'{f/30:.4f}','-i',f'/tmp/w14/build/png/compiti_{k}.png','-frames:v',str(f),*ENC,po],check=True);parts.append(po)
open('/tmp/w14/vc/lc.txt','w').write(''.join(f"file '{p}'\n" for p in parts))
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','/tmp/w14/vc/lc.txt','-c','copy','/tmp/w14/new2/COMP.mp4'],check=True)
V=rd('/tmp/w14/COMPITI_48k.wav');a=np.zeros((n_comp*1600,2),np.int16);o=int(OFF*48000);a[o:o+len(V)]=V[:len(a)-o]
wr('/tmp/w14/vc/COMP.wav',a)
# VER: fotogramma vecchio esteso; audio vecchio (jingle) + voce a +3,0 s
n_ver=round((3.0+9.08+0.8)*30)
subprocess.run(['ffmpeg','-v','error','-y','-loop','1','-framerate','30','-t',f'{n_ver/30:.4f}','-i','/tmp/w14/old_ver.png','-frames:v',str(n_ver),*ENC,'/tmp/w14/new2/VER.mp4'],check=True)
w=wave.open('/tmp/w14/asm2/old.wav');A=np.frombuffer(w.readframes(w.getnframes()),np.int16).reshape(-1,2);w.close()
f0=round(2891.262*30);f1=round((2891.262+5.0)*30)
a=np.zeros((n_ver*1600,2),np.int16);old=A[f0*1600:f1*1600];a[:len(old)]=old
V=rd('/tmp/w14/VER14_48k.wav');o=int(3.0*48000);a[o:o+len(V)]=np.clip(a[o:o+len(V)].astype(int)+V,-32768,32767)[:len(V)]
wr('/tmp/w14/vc/VER.wav',a)
json.dump({'VER':{'frames':n_ver,'wav':'/tmp/w14/vc/VER.wav'},'COMP':{'frames':n_comp,'wav':'/tmp/w14/vc/COMP.wav'}},open('/tmp/w14/vc/meta.json','w'))
print('ok',n_ver,n_comp)
