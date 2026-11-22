import sys,os,json,hashlib,subprocess
sys.path.insert(0,'/home/user/work/build')
from L import *
from playwright.sync_api import sync_playwright
CSSM="""
@font-face{font-family:Fig;font-weight:600;src:url(file:///root/.fonts/Figtree-SemiBold.ttf)}
@font-face{font-family:Fig;font-weight:700;src:url(file:///root/.fonts/Figtree-Bold.ttf)}
@font-face{font-family:Bri;font-weight:800;src:url(file:///root/.fonts/BricolageGrotesque-ExtraBold.ttf)}
html,body{margin:0;width:1920px;height:1080px;background:#fff;overflow:hidden}
#k{position:absolute;left:60px;top:34px;font:700 22px Fig;letter-spacing:.14em;color:#2060AF}
#f{position:absolute;left:60px;bottom:22px;font:700 20px Fig;color:#2060AF;letter-spacing:.12em}
#pgn{position:absolute;right:60px;bottom:22px;font:700 20px Fig;color:#2060AF;letter-spacing:.12em}
#line{position:absolute;left:60px;right:60px;top:78px;height:2px;background:#CBD5E1}
#q{position:absolute;left:60px;top:92px;font:800 46px Bri;color:#2060AF;letter-spacing:-.01em}
#note{position:absolute;left:60px;bottom:62px;font:600 30px Fig;color:#0B1530}
.b{position:absolute;box-sizing:border-box;display:flex;align-items:center;justify-content:center;text-align:center;padding:8px 20px;border-radius:14px;font:600 40px/1.25 Fig;color:#0B1530}
.pes{background:#FFDCC6;border:5px solid #C2410C;font:800 46px Bri;border-radius:18px;letter-spacing:.02em}
.cel{background:#DCEEFB;border:4px solid #1D4ED8}
.lil{background:#EBE3F7;border:4px solid #6D28D9}
.pag{background:#FFF3BF;border:4px solid #A16207}
.men{background:#DDF3E4;border:4px solid #15803D}
#leg{position:absolute;right:60px;top:26px;display:flex;gap:14px;font:600 18px Fig;color:#0B1530}
#leg span{display:flex;align-items:center;gap:6px}
#leg i{display:inline-block;width:22px;height:16px;border-radius:4px;border:3px solid}
.hl{box-shadow:0 0 0 9px #FFE600,0 10px 24px rgba(11,21,48,.18)}
.lb{position:absolute;font:600 34px Fig;color:#0B1530;white-space:nowrap}
svg{position:absolute;left:0;top:0}
"""
LEG='<div id="leg"><span><i style="background:#FFDCC6;border-color:#C2410C"></i>concetto centrale</span><span><i style="background:#DCEEFB;border-color:#1D4ED8"></i>date e sequenze</span><span><i style="background:#FFF3BF;border-color:#A16207"></i>parole chiave</span><span><i style="background:#DDF3E4;border-color:#15803D"></i>esempi e opere</span><span><i style="background:#EBE3F7;border-color:#6D28D9"></i>conseguenze</span></div>'
LX,RX,CW=90,1050,780
def col(x,w=CW): return x,w
# box: id:(x,y,w,h,cls,text)
MAPS={}
MAPS['M1']=dict(voce='MP1',q="Come giunge al potere assoluto Stalin?",note="",
 boxes={'C':(560,176,800,92,'pes',"ALLA MORTE DI LENIN (1924)"),
  'L1':(LX,330,CW,90,'pag',"Trockij"),'L2':(LX,480,CW,90,'pag',"leader dell'Armata rossa"),'L3':(LX,630,CW,90,'pag',"rivoluzione permanente"),'L4':(LX,780,CW,90,'lil',"sconfitto ed esiliato"),
  'R1':(RX,330,CW,90,'pag',"Stalin"),'R2':(RX,480,CW,90,'pag',"segretario del Partito"),'R3':(RX,630,CW,90,'pag',"rivoluzione in un solo paese"),'R4':(RX,780,CW,90,'lil',"il potere assoluto")},
 arrows={'AL':((LX+CW//2,268),(LX+CW//2,330),"si scontrano",None),'AR':((RX+CW//2,268),(RX+CW//2,330),None,None),
  'A2':((LX+CW//2,420),(LX+CW//2,480),"che è",None),'A3':((LX+CW//2,570),(LX+CW//2,630),"e sostiene la",None),'A4':((LX+CW//2,720),(LX+CW//2,780),"ma viene",None),
  'B2':((RX+CW//2,420),(RX+CW//2,480),"che è",None),'B3':((RX+CW//2,570),(RX+CW//2,630),"sostiene la",None),'B4':((RX+CW//2,720),(RX+CW//2,780),"e raggiunge",None)},
 order=[('C',None,"Alla morte di Lenin"),('L1','AL',"Trockij è il leader"),('L2','A2',"il leader dell'Armata"),('L3','A3',"la rivoluzione permanente"),('L4','A4',"sconfitto ed esiliato"),
  ('R1','AR',"Stalin è il segretario"),('R2','B2',"il segretario del Partito"),('R3','B3',"la rivoluzione in un solo paese"),('R4','B4',"il potere assoluto")])
MAPS['M23']=dict(voce='MP23',q="Come avviene l'industrializzazione dell'URSS?",note="URSS: Unione delle Repubbliche Socialiste Sovietiche",
 boxes={'C':(440,176,1040,92,'pes',"LA SVOLTA ECONOMICA DI STALIN"),
  'L1':(LX,330,CW,110,'pag',"la collettivizzazione dell'agricoltura"),'L2':(LX,520,CW,90,'lil',"la resistenza dei contadini"),'L3':(LX,690,CW,90,'lil',"gravissime carestie"),
  'R1':(RX,330,CW,110,'pag',"piani quinquennali per l'industria"),'R2':(RX,520,CW,90,'pag',"lo sfruttamento dei lavoratori"),'R3':(RX,690,CW,110,'lil',"il decollo dell'industria pesante")},
 arrows={'AL':((LX+CW//2,268),(LX+CW//2,330),"si basa su",None),'AR':((RX+CW//2,268),(RX+CW//2,330),None,None),
  'A2':((LX+CW//2,440),(LX+CW//2,520),"che provoca",None),'A3':((LX+CW//2,610),(LX+CW//2,690),"e",None),
  'B2':((RX+CW//2,440),(RX+CW//2,520),"che si basano su",None),'B3':((RX+CW//2,610),(RX+CW//2,690),"ma consentono",None)},
 order=[('C',None,"La svolta economica"),('L1','AL',"La collettivizzazione dell'agricoltura"),('L2','A2',"la resistenza dei contadini"),('L3','A3',"gravissime carestie"),
  ('R1','AR',"i piani quinquennali"),('R2','B2',"sfruttamento dei lavoratori"),('R3','B3',"il decollo dell'industria")])
MAPS['M4']=dict(voce='MP4',q="Su che cosa si basa il totalitarismo di Stalin?",note="Gulag: campi di lavoro forzato",
 boxes={'C':(560,176,800,92,'pes',"IL TOTALITARISMO DI STALIN"),
  'V':(LX,330,CW,120,'pag',"un uso spietato della violenza"),'K':(RX,330,CW,120,'pag',"l'organizzazione del consenso"),
  'V1':(LX,530,375,120,'pag',"i rivali politici"),'V2':(LX+405,530,375,120,'pag',"i cittadini comuni"),
  'V3':(LX,730,375,100,'men',"le «purghe»"),'V4':(LX+405,730,375,100,'men',"Gulag"),
  'K1':(RX+70,530,CW-70,110,'pag',"il controllo delle attività associative"),'K2':(RX+70,660,CW-70,110,'pag',"il controllo della scuola e della gioventù"),'K3':(RX+70,790,CW-70,110,'pag',"il controllo della cultura e delle arti")},
 arrows={'AV':((LX+CW//2,268),(LX+CW//2,330),"si basa su",None),'AK':((RX+CW//2,268),(RX+CW//2,330),None,None),
  'A1':((LX+190,450),(LX+190,530),"contro",None),'A2':((LX+595,450),(LX+595,530),None,None),
  'A3':((LX+190,650),(LX+190,730),"con",None),'A4':((LX+595,650),(LX+595,730),"deportati nei",None),
  'B1':((RX+30,450),(RX+30,585),"basata su",(RX+30,585,RX+70,585)),'B2':((RX+30,585),(RX+30,715),None,(RX+30,715,RX+70,715)),'B3':((RX+30,715),(RX+30,845),None,(RX+30,845,RX+70,845))},
 order=[('C',None,"il totalitarismo di Stalin"),('V','AV',"un uso spietato della violenza"),('K','AK',"l'organizzazione del consenso"),('V1','A1',"i rivali politici"),('V3','A3',"le purghe"),
  ('V2','A2',"i cittadini comuni"),('V4','A4',"deportati nei Gulag"),('K1','B1',"delle attività associative"),('K2','B2',"della scuola e della gioventù"),('K3','B3',"della cultura e delle arti")])
def html_map(M):
    h=f'<div id=k>MAPPA</div>{LEG}<div id=line></div><div id=q>{M["q"]}</div><div id=f>STORIA V</div>'
    h+='<svg width="1920" height="1080"><defs><marker id="ah" markerUnits="userSpaceOnUse" markerWidth="34" markerHeight="34" refX="17" refY="17" orient="auto"><path d="M0,3 L30,17 L0,31 z" fill="#0B1530"/></marker></defs>'
    for a,((x1,y1),(x2,y2),lab,ex) in M['arrows'].items():
        h+=f'<g id="{a}" opacity=0><line x1="{x1}" y1="{y1}" x2="{x2-0}" y2="{y2}" stroke="#0B1530" stroke-width="7" {'' if ex else 'marker-end="url(#ah)"'}/>'
        if ex: h+=f'<line x1="{ex[0]}" y1="{ex[1]}" x2="{ex[2]-12}" y2="{ex[3]}" stroke="#0B1530" stroke-width="7" marker-end="url(#ah)"/>'
        h+='</g>'
    h+='</svg>'
    for a,((x1,y1),(x2,y2),lab,ex) in M['arrows'].items():
        if lab: h+=f'<div class=lb id="L{a}" style="left:{x1+22}px;top:{(y1+y2)//2-22}px;opacity:0">{lab}</div>'
    for b,(x,y,w,hh,c,t) in M['boxes'].items():
        h+=f'<div class="b {c}" id="{b}" style="left:{x}px;top:{y}px;width:{w}px;height:{hh}px;opacity:0">{t}</div>'
    if M.get('note'): h+=f'<div id=note>{M["note"]}</div>'
    return h
def times(M,lead=0.3):
    """tempi di comparsa delle caselle dalla voce (ASR se c'è, altrimenti proporzionale al testo)"""
    n=M['voce'];txt=TXT[n].lower();p=vpath(n);d=dur(p)
    w=asr_words(n)
    cum=None
    if w:
        L=[len(x[1].strip()) for x in w];cum=[0]
        for l in L: cum.append(cum[-1]+l)
    def tf(frac):
        if w:
            T=cum[-1];target=frac*T
            for i in range(len(w)):
                if cum[i+1]>=target: return w[i][0]
            return w[-1][0]
        return 0.15+frac*(d-0.3)
    pos=0;res=[]
    for b,a,anc in M['order']:
        i=txt.find(anc.lower(),pos)
        if i<0: i=txt.find(anc.lower().split()[0],pos)
        if i<0: i=pos
        # l'ultima occorrenza per 'il potere assoluto' (anche nel titolo)
        if anc in ("il potere assoluto",): i=txt.rfind(anc.lower())
        res.append((b,a,max(0.0,tf(i/len(txt))-0.05)));pos=i+1
    return res,d
def build(name,M,out_dir,fps=30,final_hold=4.0):
    res,d=times(M)
    T0=1.0  # la voce parte a T0
    steps=[(b,a,T0+t) for b,a,t in res]
    end_voice=T0+d
    tot=end_voice+0.8+final_hold
    return steps,end_voice,tot
def state_at(M,steps,end_voice,t):
    st={};cur=None
    for i,(b,a,ts) in enumerate(steps):
        p=min(1,max(0,(t-(ts-0.15))/0.45))
        st[b]=round(1-(1-p)**3,1)
        if a: 
            pa=min(1,max(0,(t-(ts-0.6))/0.45));st[a]=round(1-(1-pa)**3,1);st['L'+a]=st[a]
        nxt=steps[i+1][2] if i+1<len(steps) else end_voice+0.3
        if ts-0.15<=t<nxt-0.15: cur=b
    st['_hl']=cur if t<end_voice+0.3 else None
    return st
JSAPPLY="""(s)=>{for(const k in s){if(k=='_hl')continue;const e=document.getElementById(k);if(!e)continue;e.style.opacity=s[k];if(e.classList.contains('b'))e.style.transform=`translateY(${(1-s[k])*16}px)`}
document.querySelectorAll('.b').forEach(e=>e.classList.toggle('hl',e.id==s._hl))}"""
def render_map(name,M,steps,end_voice,tot,out_mp4,still=None,fps=30):
    N=int(round(tot*fps));prev=None;prevfn=None
    os.makedirs(f'{B}/mp/{name}',exist_ok=True)
    with sync_playwright() as p:
        b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',args=['--no-sandbox','--allow-file-access-from-files'])
        pg=b.new_page(viewport={'width':1920,'height':1080})
        open('/tmp/_m.html','w').write(f'<!doctype html><meta charset=utf-8><style>{CSSM}</style><body>{html_map(M)}</body>')
        pg.goto('file:///tmp/_m.html');pg.evaluate('document.fonts.ready');pg.wait_for_timeout(200)
        ff=subprocess.Popen(['ffmpeg','-y','-v','error','-f','image2pipe','-framerate',str(fps),'-i','-','-c:v','libx264','-preset','veryfast','-crf','16','-pix_fmt','yuv420p',out_mp4],stdin=subprocess.PIPE)
        for i in range(N):
            st=state_at(M,steps,end_voice,i/fps);key=json.dumps(st,sort_keys=True)
            if key!=prev:
                pg.evaluate(JSAPPLY,st);png=pg.screenshot(type='png');prev=key;prevpng=png
            ff.stdin.write(prevpng)
        ff.stdin.close();ff.wait()
        if still:
            full={k:1 for k in list(M['boxes'])+list(M['arrows'])+['L'+a for a in M['arrows']]};full['_hl']=None
            pg.evaluate(JSAPPLY,full);pg.screenshot(path=still)
        b.close()
if __name__=='__main__':
    for nm,M in MAPS.items():
        if os.path.exists(f'{B}/mp/{nm}.ok'): continue
        steps,ev,tot=build(nm,M,None)
        json.dump(dict(steps=steps,end_voice=ev,tot=tot),open(f'{B}/mp/{nm}.json','w'))
        render_map(nm,M,steps,ev,tot,f'{B}/mp/{nm}.mp4',still=f'{B}/mp/{nm}.png')
        open(f'{B}/mp/{nm}.ok','w').write('1');print(nm,tot,flush=True)
