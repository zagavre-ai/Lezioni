import re,json,sys,os,shutil,subprocess
from playwright.sync_api import sync_playwright
S=''
files=['']*20
AN=files[12:]
TIT=['La lana nel mondo','Il vello e la cernita','Provenienza e categorie super','La lana, il fuoco e il taglio','Lane speciali a confronto','La seta: storia e leggende']
REP=[('diciannove virgola settantacinque','19,75'),('undici virgola venticinque','11,25'),('super ottanta',"super 80's"),('super duecentocinquanta',"super 250's"),
('da tredici a sedici','13-16'),('da tredici a quindici','13-15'),('da quindici a diciannove','15-19'),('da diciassette a ventitré','17-23'),('da venti a venticinque micron','20-25 micron'),
('centoventi grammi','120 g'),('da quattrocento a mille grammi','400-1.000 g'),('milleseicento grammi','1.600 g'),('quattromila grammi','4.000 g'),
('terzo millennio avanti Cristo','III millennio a.C.'),('dodicesimo secolo','XII secolo'),('Novecento','1900'),('il novanta per cento','il 90%'),('una intera','un\'intera')]
def cap(s):
    for a,b in REP: s=s.replace(a,b)
    return s
def spec(k,voice_times=None):
    ph=[p.strip() for p in re.split(r'(?:Taglio\. ){2}Taglio\. ?',AN[k]) if p.strip()]
    if voice_times: P=voice_times[:len(ph)];dur=voice_times[-1]
    else:
        P=[];t=0.8
        for p in ph: P.append(round(t,2));t+=len(p.split())/2.4+0.7
        dur=t+2.5
    return {'id':'AN%d'%(k+1),'title':TIT[k],'P':P,'caps':[cap(p) for p in ph],'dur':round(dur,2)}
def render(sp,out,scale=1.0,fps=30):
    N=int(sp['dur']*fps);d=out+'_f';shutil.rmtree(d,ignore_errors=True);os.makedirs(d)
    with sync_playwright() as p:
        b=p.chromium.launch(args=["--allow-file-access-from-files"]);pg=b.new_page(viewport={'width':1920,'height':1080},device_scale_factor=scale)
        pg.goto('file:///home/claude/lezioni/psicologia-I-II-lez02/an/anim.html');pg.evaluate("document.fonts.ready");pg.wait_for_timeout(300)
        pg.evaluate("a=>init(a)",sp)
        for n in range(N):
            pg.evaluate("t=>draw(t)",n/fps);pg.screenshot(path=f'{d}/{n:05d}.png')
        b.close()
    subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(fps),'-i',d+'/%05d.png','-c:v','libx264','-preset','veryfast','-crf','17','-pix_fmt','yuv420p',out+'.mp4'],check=True)
    shutil.rmtree(d)
if __name__=='__main__':
    ks=[int(x) for x in sys.argv[1:]] or range(6)
    for k in ks:
        import os as _o
        mp='/home/claude/lezioni/psicologia-I-II-lez02/voci/wav/meta_R1.json'
        vt=None
        if _o.path.exists(mp):
            m=json.load(open(mp))['AN%d'%(k+1)];vt=[p+0.8 for p in m['phrases']]+[m['dur']+0.8+2.5]
        sp=spec(k,vt);json.dump(sp,open(f'AN{k+1}.json','w'),ensure_ascii=False)
        if os.environ.get('SHOT'):
            with sync_playwright() as p:
                b=p.chromium.launch(args=["--allow-file-access-from-files"]);pg=b.new_page(viewport={'width':1920,'height':1080})
                errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
                pg.goto('file:///home/claude/lezioni/psicologia-I-II-lez02/an/anim.html');pg.evaluate("document.fonts.ready");pg.wait_for_timeout(300);pg.evaluate("a=>init(a)",sp)
                pg.evaluate("t=>draw(t)",sp['dur']-1.0);pg.screenshot(path=f'AN{k+1}_end.png');print(k+1,sp['dur'],errs)
        else: render(sp,f'AN{k+1}');print('AN',k+1,sp['dur'],flush=True)
