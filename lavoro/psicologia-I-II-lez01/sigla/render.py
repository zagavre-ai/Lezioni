import os,shutil,subprocess
from playwright.sync_api import sync_playwright
D='/home/claude/lezioni/psicologia-I-II-lez01/sigla/';d=D+'f';shutil.rmtree(d,ignore_errors=True);os.makedirs(d)
with sync_playwright() as p:
    b=p.chromium.launch(args=["--allow-file-access-from-files"]);pg=b.new_page(viewport={'width':1920,'height':1080})
    pg.goto('file://'+D+'sigla.html');pg.evaluate("document.fonts.ready");pg.wait_for_timeout(400)
    for n in range(450):
        pg.evaluate("t=>draw(t)",n/30.0);pg.screenshot(path='%s/%05d.png'%(d,n+1))
    b.close()
# musica: 5 s in ripetizione per 15 s con dissolvenze
subprocess.run(['ffmpeg','-y','-loglevel','error','-stream_loop','2','-i','/home/claude/sigle_zip/sigle/musica_filosofia_psicologia.wav','-t','15','-af','afade=t=in:d=0.3,afade=t=out:st=14.2:d=0.8,loudnorm=I=-18:TP=-1.5,aresample=48000','-ac','2',D+'mus.wav'],check=True)
subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate','30','-i',d+'/%05d.png','-i',D+'mus.wav','-c:v','libx264','-preset','veryfast','-threads','2','-crf','16','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-shortest',D+'../Sigla_Psicologia_15s.mp4'],check=True)
shutil.rmtree(d);print('SIGLA_OK')
