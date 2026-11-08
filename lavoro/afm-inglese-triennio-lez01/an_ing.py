# Glossario (GL1) e ripasso finale (RF1) animati, a tempo di voce
import sys,json,os,glob,shutil,subprocess
from playwright.sync_api import sync_playwright
D='/home/claude/lezioni/afm-inglese-triennio-lez01/'
TV=json.load(open(D+'voci/testi_voci.json'))
M={};[M.update(json.load(open(f))) for f in glob.glob(D+'voci/wav/meta_*.json')]
def it(i,e):return f'<span style="color:#5A6B85;font-size:.85em">{i}</span><br>{e}'
GL=[['Interdependence',it('interdipendenza','economies that depend on each other')],
['Free trade',it('libero scambio','promoted by the WTO')],
['Economies of scale',it('economie di scala','lower cost per item for large quantities')],
['LDCs',it('Paesi meno sviluppati','Least Developed Countries')],
['Smart factory',it('fabbrica intelligente','more efficient, productive, less wasteful')],
['Digital twin',it('gemello digitale','virtual copy of a process or production line')],
['Shortage',it('carenza','not enough workers or raw materials')],
['Recruitment',it('selezione del personale','how a company finds and hires people')]]
RF=[['Globalisation',['Interdependence of world economies','Transport · communication · labour · free trade','Good or bad? Supporters and opponents']],
['Technological advancement',['Industry 4.0: the Fourth Industrial Revolution','Automation · AI · smart factories','IoT · digital twin · edge and cloud computing']],
['Diversity and inclusion',['Cultures and identities side by side','Equal opportunities for everyone','Gen Z and new recruitment policies']],
['World instability',['Pandemic · Brexit · war in Ukraine','Shortages, delays and inflation','Remote work and virtual meetings']],
['Environmental concerns',['97% of organisations affected','Risk · regulations · public pressure','Resources, demand, working conditions']]]
def spec(k):
    m=M[k];P=[p+0.8 for p in m['phrases']];dur=round(m['dur']+0.8+2.5,2)
    sp={'id':k,'title':{'GL1':'Key words · Parole chiave','RF1':'Global Factors'}[k],'ey':{'GL1':'Glossary · Glossario','RF1':'Final review · Ripasso finale'}[k],'P':P,'caps':[c.replace('Industry four point zero','Industry 4.0').replace('ninety-seven per cent','97%').replace('twenty nineteen','2019') for c in TV[k]],'dur':dur}
    if k=='GL1':sp['gl']=GL
    if k=='RF1':sp['rf']=RF
    return sp
def render(sp,out,fps=30):
    N=int(sp['dur']*fps);d=out+'_f';shutil.rmtree(d,ignore_errors=True);os.makedirs(d)
    with sync_playwright() as p:
        b=p.chromium.launch(args=["--allow-file-access-from-files"]);pg=b.new_page(viewport={'width':1920,'height':1080})
        errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
        pg.goto('file://'+D+'an/anim_ing.html');pg.evaluate("document.fonts.ready");pg.wait_for_timeout(300);pg.evaluate("a=>init(a)",sp)
        shots=os.environ.get('SHOT')
        if shots:
            for t in shots.split(','):pg.evaluate("t=>draw(t)",float(t));pg.screenshot(path=f'{out}_{t}.png')
            print(errs);return
        for n in range(N):
            pg.evaluate("t=>draw(t)",n/fps);pg.screenshot(path=f'{d}/{n:05d}.png')
        b.close()
    subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(fps),'-i',d+'/%05d.png','-c:v','libx264','-preset','veryfast','-crf','16','-pix_fmt','yuv420p',out+'.mp4'],check=True)
    shutil.rmtree(d)
if __name__=='__main__':
    for k in sys.argv[1:]:
        if os.path.exists(D+f'an/{k}.mp4') and not os.environ.get('SHOT'):continue
        render(spec(k),D+'an/'+k);print(k,flush=True)
