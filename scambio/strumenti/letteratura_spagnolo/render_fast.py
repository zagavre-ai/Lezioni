# render_fast.py: come dark.render ma JPEG e fps scelto (poi portato a 30 fps), durata esatta in fotogrammi
import sys,os,shutil,subprocess,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),".."))
import schede_spagnolo as d
from playwright.sync_api import sync_playwright
def render_many(items):
    # items: [(spec, out_mp4, fps)]
    with sync_playwright() as p:
        b=p.chromium.launch(args=["--allow-file-access-from-files"]);pg=b.new_page(viewport={'width':1920,'height':1080},device_scale_factor=1)
        for spec,out,fps in items:
            tmp=out+'_f'; shutil.rmtree(tmp,ignore_errors=True); os.makedirs(tmp)
            html='<!doctype html><meta charset=utf-8><style>%s</style><body>%s'%(d.CSS,d.BODY); open(tmp+'/p.html','w').write(html)
            pg.goto('file://'+os.path.abspath(tmp+'/p.html')); pg.evaluate("document.fonts.ready"); pg.add_script_tag(content=d.JS); pg.evaluate("(s)=>init(s)",spec)
            N=int(round(spec['dur']*fps))
            for n in range(N):
                pg.evaluate("([t,f])=>draw(t,f)",[n/fps,n]); pg.screenshot(path='%s/%05d.jpg'%(tmp,n+1),type='jpeg',quality=93)
            nf30=int(round(spec['dur']*30))
            subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(fps),'-i',tmp+'/%05d.jpg','-vf','fps=30,format=yuv420p','-frames:v',str(nf30),'-c:v','libx264','-preset','veryfast','-crf','16',out],check=True)
            shutil.rmtree(tmp); print('reso',out,N,'fotogrammi',flush=True)
        b.close()
if __name__=='__main__':
    render_many([(json.loads(a),o,int(f)) for a,o,f in json.load(open(sys.argv[1]))])
