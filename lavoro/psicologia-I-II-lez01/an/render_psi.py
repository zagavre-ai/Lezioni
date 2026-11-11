# Rende le animazioni di approfondimento (ANx), glossario (GLc) e ripasso finale (RFc) con anim_psi.html
import sys,json,os,shutil,subprocess,re
from playwright.sync_api import sync_playwright
D='/home/claude/lezioni/psicologia-I-II-lez01/'
CPS=14.8
NUOVI=json.load(open(D+'testi_voci_NUOVI.json'))
TITLES={'AN1':'Una chiave per comprendere','AN2':'I contesti dell\'esistenza umana','AN3':'Relazioni quotidiane e ricerca di sé','AN4':'Una società multiculturale e tecnologica','AN5':'Oggetto di studio differente','AN6':'La ricerca delle cause','AN7':'La natura multi-causale','AN8':'I tre fattori del comportamento','AN9':'Le quattro discipline','AN10':'Il percorso del primo biennio','GLc':'Le parole chiave','RFc':'Ripasso finale'}
GLT=[('Scienze umane','Le discipline che studiano l\'essere umano, le sue azioni e la sua mente.'),('Scienze della natura','Le discipline che studiano la realtà materiale, come la chimica e la biologia.'),('Metodo scientifico','Casi da analizzare, dati da ricavare ed esperimenti per confermarli.'),('Natura multi-causale','Le azioni umane non dipendono mai da una sola causa.'),('Dimensione storica','Comportamenti, valori e tradizioni cambiano nel corso del tempo.'),('Psicologia','Studia il comportamento e i processi mentali dell\'individuo.'),('Sociologia','Analizza le strutture sociali, le istituzioni e i processi di interazione nei gruppi.'),('Antropologia','Studia i popoli e le diverse culture umane nel mondo.'),('Metodologia della ricerca','Strumenti scientifici e tecniche per svolgere le indagini sul campo.')]
RFT=[['Le scienze umane come strumento',['Una chiave per comprendere le esperienze vissute','Una società multiculturale e tecnologica'],1,2],
['Scienze umane e scienze della natura',['Oggetto di studio differente: l\'essere umano','Stesso metodo scientifico'],2,3],
['I fattori del comportamento',['Natura multi-causale','Biologici e di sviluppo · ambiente · dimensione storica'],3,4],
['Le discipline e il percorso',['Psicologia · sociologia · antropologia · metodologia','Primo biennio: si comincia dalla psicologia'],4,99]]
def meta(name):
    f=D+'voci/wav/meta_S1.json'
    if os.path.exists(f):
        M=json.load(open(f))
        if name in M: return M[name]
    return None
def texts(name):
    if name in NUOVI: return NUOVI[name]
    m=meta(name)
    if m: return m['text']
    raise SystemExit('testi mancanti per '+name)
def spec(name):
    m=meta(name)
    if name=='GLc':
        ph=['Le parole chiave della lezione.']+[g[0]+': '+g[1] for g in GLT]
        m=m or None
    elif name=='RFc':
        ph=m['text'] if m else ['Ricapitoliamo la lezione.']*6
    else: ph=NUOVI[name]
    if m and name in('GLc','RFc'):ph=m['text']
    if m: P=[p+0.8 for p in m['phrases']];dur=m['dur']+0.8+2.5
    else:
        P=[];t=0.8
        for p in ph:P.append(round(t,2));t+=len(p)/CPS+0.45
        dur=t+2.2
    sp={'id':name.rstrip('c') if name in('GLc','RFc') else name,'scene':{'GLc':'GL','RFc':'RF'}.get(name,name),'title':TITLES[name],'ey':{'GLc':'Glossario','RFc':'Ripasso finale'}.get(name,'Approfondimento'),'P':P,'caps':ph,'dur':round(dur,2)}
    if name=='GLc': sp['gl']=GLT;sp['nocap']=1;sp['id']='GL'
    if name=='RFc': sp['rf']=RFT;sp['id']='RF'
    return sp
def render(name,out=None,scale=1.0):
    sp=spec(name);out=out or D+'an/'+name
    d=out+'_f';shutil.rmtree(d,ignore_errors=True);os.makedirs(d)
    N=int(round(sp['dur']*30));frames=[];last=None;nshot=0
    with sync_playwright() as p:
        b=p.chromium.launch(args=["--allow-file-access-from-files"]);pg=b.new_page(viewport={'width':1920,'height':1080},device_scale_factor=scale)
        errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
        pg.goto('file://'+D+'an/anim_psi.html');pg.evaluate("document.fonts.ready");pg.wait_for_timeout(400)
        pg.evaluate("a=>init(a)",sp)
        for n in range(N):
            k=pg.evaluate("t=>draw(t)",n/30.0)
            if k!=last:
                f='%s/%05d.png'%(d,n);pg.screenshot(path=f);nshot+=1;frames.append([f,1]);last=k
            else: frames[-1][1]+=1
        b.close()
    if errs:print('ERRORI JS',errs[:3])
    L=''.join("file '%s'\nduration %.5f\n"%(f,c/30.0) for f,c in frames)+"file '%s'\n"%frames[-1][0]
    open(d+'/l.txt','w').write(L)
    subprocess.run(['ffmpeg','-y','-loglevel','error','-f','concat','-safe','0','-i',d+'/l.txt','-vf','fps=30,format=yuv420p','-c:v','libx264','-preset','veryfast','-threads','2','-crf','17',out+'.mp4'],check=True)
    shutil.rmtree(d);print(name,'dur',sp['dur'],'frames',N,'screenshot',nshot,flush=True)
def shots(name,fracs):
    sp=spec(name);out=D+'fr/'
    with sync_playwright() as p:
        b=p.chromium.launch(args=["--allow-file-access-from-files"]);pg=b.new_page(viewport={'width':1920,'height':1080})
        errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
        pg.goto('file://'+D+'an/anim_psi.html');pg.evaluate("document.fonts.ready");pg.wait_for_timeout(400);pg.evaluate("a=>init(a)",sp)
        for i,k in enumerate(fracs):
            t=sp['P'][k]+3.0 if k<len(sp['P']) else sp['dur']-1
            pg.evaluate("t=>draw(t)",t);pg.screenshot(path=out+'%s_%d.png'%(name,k))
        print(name,sp['dur'],errs)
if __name__=='__main__':
    if sys.argv[1]=='shot':shots(sys.argv[2],[int(x) for x in sys.argv[3:]])
    else:
        for n in sys.argv[1:]:
            if not os.path.exists(D+'an/%s.mp4'%n):render(n)
