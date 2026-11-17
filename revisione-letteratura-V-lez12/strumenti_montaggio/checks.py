import subprocess,numpy as np,json,re,sys
sys.path.insert(0,'/home/user/w/b')
import plan
V='/home/user/w/out/Letteratura_Lez12_Parte1_1080p.mp4';O='/home/user/w/Letteratura_Lez12.mp4'
J=json.load(open('/home/user/w/b/states.json'));S=J['START'];N=J['NEWF'];FPS=30
SR=16000
def rd(f,ss=None,d=None):
    c=['ffmpeg','-v','error']+(['-ss',f'{ss:.3f}','-t',f'{d:.3f}'] if ss is not None else [])+['-i',f,'-vn','-ac','1','-ar',str(SR),'-f','s16le','-']
    return np.frombuffer(subprocess.run(c,capture_output=True).stdout,np.int16).astype(float)
print('== SCARTO AUDIO/VIDEO del prof (correlazione audio finale vs originale)')
for k,(o0,o1) in plan.DSEG.items():
    t0=S[k]/FPS;res=[]
    for f in (0.15,0.5,0.85):
        o=o0+(o1-o0)*f;t=t0+(o-o0)
        a=rd(V,t,4);b=rd(O,o-1,6)
        # gli audio non sono uguali (pulito vs originale): uso l'inviluppo
        ea=np.abs(a[::40]);eb=np.abs(b[::40]);c=np.correlate(eb-eb.mean(),ea-ea.mean(),'valid');i=int(np.argmax(c))
        res.append(i*40/SR-1.0)
    print(k,'scarti (s):',[round(x,3) for x in res])
print('== FERMI IMMAGINE nel riquadro del prof')
for k in plan.DSEG:
    a=S[k]/FPS+0.7;d=(plan.DSEG[k][1]-plan.DSEG[k][0])-1.5
    r=subprocess.run(['ffmpeg','-nostats','-ss',f'{a:.2f}','-t',f'{d:.2f}','-i',V,'-vf','crop=410:308:1428:148,freezedetect=n=0.0008:d=1','-an','-f','null','-'],capture_output=True,text=True).stderr
    print(k,'fermi >=1 s:',len(re.findall('freeze_start',r)))
print('== MISURE GENERALI')
j=json.loads(subprocess.run(['ffprobe','-v','error','-count_packets','-select_streams','v:0','-show_entries','stream=nb_read_packets,width,height:format=duration,size','-of','json',V],capture_output=True,text=True).stdout)
dur=float(j['format']['duration']);fr=int(j['streams'][0]['nb_read_packets'])
print('durata %.3f s (%d:%04.1f) fotogrammi %d (durata*30=%d) peso %.1f MB %dx%d'%(dur,dur//60,dur%60,fr,round(dur*30),int(j['format']['size'])/1e6,j['streams'][0]['width'],j['streams'][0]['height']))
e=subprocess.run(['ffmpeg','-nostats','-i',V,'-af','ebur128=peak=true','-vn','-f','null','-'],capture_output=True,text=True).stderr
i=e.rfind('Summary');print(e[i:].replace('\n',' | ')[:400])
print('== SILENZI >=2,8 s')
e=subprocess.run(['ffmpeg','-nostats','-i',V,'-af','silencedetect=n=-45dB:d=2.8','-vn','-f','null','-'],capture_output=True,text=True).stderr
for a,d in re.findall(r'silence_start: ([\d.]+).*?silence_duration: ([\d.]+)',e,flags=re.S): 
    t=float(a);blk=[n for n in S if S[n]/FPS<=t<(S[n]+N[n])/FPS]
    print('  %.1f s per %.1f s  (blocco %s)'%(t,float(d),blk[0] if blk else '?'))
