# Genera lo sfondo (card sincronizzate) di un pezzo della prof. Rende solo gli stati distinti e li concatena.
import sys,json,re,os,subprocess,html as H
sys.path.insert(0,'/home/user/lav/tools')
from frasi import *
from piani import *
from playwright.sync_api import sync_playwright
L='/home/user/lav/lez01/'
FPS=30
def ease(x):x=max(0.0,min(1.0,x));return 1-(1-x)**3
NOTE=[(r'\bUE\b','UE = Unione Europea'),(r'\ba\.C\.','a.C. = avanti Cristo'),(r'\bd\.C\.','d.C. = dopo Cristo'),
      (r'°C','°C = gradi centigradi'),(r'\bmicron\b','micron = millesimo di millimetro'),(r'kg/mm²','kg/mm² = chilogrammi per millimetro quadrato')]
def nota(t):
    n=[b for a,b in NOTE if re.search(a,t)]
    if 'IWTO' in t and 'International' not in t:n.append('IWTO = Organizzazione Internazionale del Tessile Laniero')
    return ' · '.join(n[:3])
def pulisci(t):
    t=t.strip()
    if t.endswith(';'):t=t[:-1]+'.'
    return t[0].upper()+t[1:]
def card_html(t,pg=None):
    return H.escape(pulisci(correggi(t,pg))).replace('&#x27;',"'")
def raffina(fr,t0,W,j,win=9):
    """affina l'inizio della frase j sulle parole riconosciute vicino alla stima"""
    e=t0[j];toks=[norm(x) for x in fr[j][1].split()];cont=[x for x in toks if len(x)>=4][:4]
    if len(cont)<2:return e
    S=set(cont);best=(0,1e9,e)
    for i,(t,w,n) in enumerate(W):
        if abs(t-e)>win:continue
        seg=[x[2] for x in W[i:i+14]]
        sc=len(S&set(seg))
        if n in S and sc>=2:
            d=abs(t-e)
            if sc>best[0] or (sc==best[0] and d<best[1]):best=(sc,d,t)
    return best[2] if best[0]>=2 else e
CORREZ=[(r'Bombix','Bombyx'),(r'\bsgassatura\b','sgrassatura'),(r'\bai altoforni\b','agli altoforni'),
        (r'\bafrica\b','Africa'),(r'\basia\b','Asia'),(r'\bpatagonia\b','Patagonia'),(r'\bturchia\b','Turchia'),(r'\bankara\b','Ankara'),
        (r'\bstati uniti\b','Stati Uniti'),(r'\bhimalaya\b','Himalaya'),(r'\bkashmir\b','Kashmir'),(r'\bsudafrica\b','Sudafrica')]
REGISTRO=[]
def correggi(t,pg=None):
    o=t
    for a,b in CORREZ:t=re.sub(a,b,t)
    if t!=o:REGISTRO.append(dict(pagina=pg,prima=o,dopo=t))
    return t
def sentenze_w(k,a,b,fr,R,W,M,cmin=0.2):
    out=[];last=a-1
    for r in R:
        if not r or r['t0'] is None or r['cop']<cmin or not (a-1<=r['t0']<b):continue
        t=min(max(r['t0'],a),b);t=max(t,last+1.2)
        if t>=b-1.0:break
        j=r['k'];out.append(dict(j=j,t_orig=t,T=M(t),html=card_html(fr[j][1],fr[j][0]),note=nota(fr[j][1]),pg=fr[j][0],cop=r['cop']));last=t
    return out
def sentenze(k,a,b,fr,t0,W,M):
    js=[j for j in range(len(fr)) if a-1.0<=t0[j]<b]
    T=[];prev=-9
    for j in js:
        t=raffina(fr,t0,W,j);t=min(max(t,a),b)
        T.append(t)
    # monotono, distanza minima 1.0 s
    out=[];last=a-1
    for j,t in zip(js,T):
        t=max(t,last+1.0)
        if t>=b-1.0:break
        out.append(dict(j=j,t_orig=t,T=M(t),html=card_html(fr[j][1]),note=nota(fr[j][1]),pg=fr[j][0]));last=t
    return out
def gruppi(items,h,maxh=815,gap=22,maxn=3):
    G=[];cur=[];tot=0
    for i,it in enumerate(items):
        hh=h[i]
        if cur and (len(cur)>=maxn or tot+gap+hh>maxh):G.append(cur);cur=[];tot=0
        tot+=(gap if cur else 0)+hh;cur.append(i)
    if cur:G.append(cur)
    return G
def build_bg(nome,items,D,title,keys,outdir,extra_cards=None):
    os.makedirs(outdir,exist_ok=True)
    N=int(round(D*FPS))
    with sync_playwright() as p:
        br=p.chromium.launch(executable_path='/opt/pw-browsers/chromium');pg=br.new_page(viewport={'width':1920,'height':1080})
        pg.goto('file:///home/user/lav/prod/prof.html');pg.evaluate('pronto()');pg.wait_for_timeout(300)
        cards=[dict(html=i['html'],note=i['note']) for i in items]
        res=pg.evaluate('([a,b,c])=>setup(a,b,c)',[title,cards,keys]);h=res['h'];top0=res['top'];print('titolo/chiavi: top card',top0,'fine chiavi',res['keysEnd'],flush=True)
        G=gruppi(items,h,maxh=1040-top0);gi={};tops={}
        for g,ids in enumerate(G):
            y=top0
            for i in ids:gi[i]=g;tops[i]=y;y+=h[i]+22
        cache={};frames=[];prevkey=None
        for f in range(N):
            t=f/FPS;vis=[];
            act=-1
            for i,it in enumerate(items):
                if it['T']<=t:act=i
            if act>=0:
                g=gi[act]
                for i in G[g]:
                    if i<=act:vis.append([i,round(ease((t-items[i]['T'])/0.3),2),1 if i==act else 0,tops[i]])
                if g>0 and t<items[G[g][0]]['T']+0.3:
                    a=round(1-ease((t-items[G[g][0]]['T']+0.05)/0.25),2)
                    if a>0:
                        for i in G[g-1]:vis.append([i,a,0,tops[i]])
            key=json.dumps(vis)
            if key not in cache:
                pg.evaluate('st=>draw(st)',{'vis':vis});fn=f'{outdir}/s{len(cache):05d}.png'
                pg.screenshot(path=fn);cache[key]=fn
            frames.append(cache[key])
        br.close()
    # elenco concat con durate per gruppi di frame identici
    lst=outdir+'/lista.txt';runs=[];
    for fn in frames:
        if runs and runs[-1][0]==fn:runs[-1][1]+=1
        else:runs.append([fn,1])
    with open(lst,'w') as o:
        for fn,n in runs:o.write(f"file '{fn}'\nduration {n/FPS:.6f}\n")
        o.write(f"file '{runs[-1][0]}'\n")
    out=outdir+'/bg.mp4'
    subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lst,'-vf',f'fps={FPS},format=yuv420p','-frames:v',str(N),'-c:v','libx264','-preset','veryfast','-crf','14',out],check=True)
    json.dump(dict(refusi=REGISTRO,G=G,items=[{k:v for k,v in i.items() if k!='html'} for i in items],unici=len(cache),frames=N),open(outdir+'/info.json','w'),ensure_ascii=False)
    return out,G,h
if __name__=='__main__':
    k=int(sys.argv[1])
    tr=json.load(open(L+'trasc.json'));W=parole_asr(tr)
    fr=frasi(L+'Lezione.1.-.Preparazione.pt.1.1.pdf')
    R=json.load(open(L+'frasi_w.json'))
    a,b=PEZZI[k];iv=intervalli(a,b,W);M=Mappa(iv)
    items=sentenze_w(k,a,b,fr,R,W,M)
    ns={};exec(open(L+f'cont/a{k:02d}.py').read(),ns);A=ns['A']
    print('A',k,'frasi',len(items),'durata',round(M.dur,1))
    out,G,h=build_bg(f'A{k:02d}',items,M.dur,A['titolo'],A['chiavi'],f'/home/user/lav/lez01/bg/A{k:02d}')
    print(out,len(G),'gruppi')
