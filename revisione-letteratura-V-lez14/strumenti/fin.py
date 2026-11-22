import sys,json,subprocess,re;sys.path.insert(0,'/tmp/w14/build');sys.path.insert(0,'/tmp/w14')
import gen,buildd
gen.PROFON=False
for P in (1,2): gen.scrivi(f'newcover_np{P}',gen.cover(f'Luigi Pirandello · Parte {P}',buildd.ARGS[P],pag=1,prof=False))
m=open('/tmp/w14/pdfhtml/mappa.html',encoding='utf-8').read().replace('&nbsp;·&nbsp; Prof. Giorgio Mazzotti','')
open('/tmp/w14/build/html/mappa_prof.html','w',encoding='utf-8').write(m)
subprocess.run(['node','/tmp/w14/build/render.js','/tmp/w14/build/html','/tmp/w14/build/png'],check=True)
ENC=['-c:v','libx264','-preset','veryfast','-crf','19','-pix_fmt','yuv420p','-r','30','-an','-x264-params','keyint=60:scenecut=0','-threads','1']
for P in (1,2):
    for n,a,d in json.load(open(f'/tmp/w14/tl{P}.json')):
        if n=='INTRO1':
            k=round((a+d)*30)-round(a*30)
            subprocess.run(['ffmpeg','-v','error','-y','-loop','1','-framerate','30','-t',f'{k/30:.3f}','-i',f'/tmp/w14/build/png/newcover_np{P}.png','-frames:v',str(k),*ENC,f'/tmp/w14/new{P}/INTRO1_np.mp4'],check=True)
