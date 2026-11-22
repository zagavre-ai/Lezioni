# Modello approvato (Gadda, Letteratura V lez20): un riquadro alla volta mentre la voce M1..M8 lo legge.
# order = (riquadro, freccia che lo raggiunge, voce). Le voci stanno in voci/vox/Mn.wav. Lancia dalla cartella della mappa.
import json,subprocess,sys
from playwright.sync_api import sync_playwright
dur={f'M{i}':float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'voci/vox/M{i}.wav'],capture_output=True,text=True).stdout) for i in range(1,9)}
order=[('B1',None,'M1'),('B2',None,'M2'),('B3','A1','M3'),('B5','A3','M4'),('B4','A2','M5'),('B6',None,'M6'),('B7',None,'M7'),('B8',None,'M8')]
t=1.2;steps=[]
for b,a,m in order:
    if a: t+=0.6
    steps.append([b,a,round(t,3),dur[m],m]); t+=dur[m]+0.7
TOT=t+4.0
json.dump({'steps':steps,'tot':TOT},open('steps.json','w'))
mode=sys.argv[1] if len(sys.argv)>1 else 'video'
with sync_playwright() as p:
    br=p.chromium.launch(); pg=br.new_page(viewport={'width':1920,'height':1080})
    import os; pg.goto('file://'+os.path.abspath('mappa.html')); pg.wait_for_timeout(500)
    pg.evaluate(f"setSteps({json.dumps([s[:4] for s in steps])})")
    if mode=='finale':
        pg.evaluate(f"render({TOT})"); pg.screenshot(path='finale.png'); pg.evaluate(f"render({steps[3][2]+1})"); pg.screenshot(path='meta.png')
    else:
        ff=subprocess.Popen(['ffmpeg','-v','error','-y','-f','image2pipe','-framerate','30','-i','-','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','video_muto.mp4'],stdin=subprocess.PIPE)
        n=int(TOT*30)
        for i in range(n):
            pg.evaluate(f"render({i/30})"); ff.stdin.write(pg.screenshot(type='png'))
        ff.stdin.close(); ff.wait()
    br.close()
print('totale',round(TOT,1),'s')
