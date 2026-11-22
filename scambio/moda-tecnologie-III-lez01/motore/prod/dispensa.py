# Dispensa A4 orizzontale = stesse slide del video + strato di testo invisibile. Copertina: solo materia e titolo. PDF separato con le mappe.
import sys,os,json,re,subprocess
sys.path.insert(0,'/home/user/lav/tools');sys.path.insert(0,'/home/user/lav/prod')
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,landscape
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors
from frasi import frasi
L='/home/user/lav/lez01/';SC=L+'scene/'
MAT='Tecnologie dei materiali e dei processi produttivi e organizzativi della moda'
PW,PH=landscape(A4)
def pulito(t):
    for a,b in (('✓',''),('→','->'),('≥','>='),('²','2'),('³','3'),('·','-'),('«','"'),('»','"'),('…','...'),('–','-'),('’',"'"),('−','-'),('×','x')):t=t.replace(a,b)
    return t.encode('latin-1','replace').decode('latin-1')
def img_pagina(c,png,testo,n,ytop=30):
    c.setFillColor(colors.white);c.rect(0,0,PW,PH,fill=1,stroke=0)
    w=PW-40;h=w*1080/1920;y=PH-h-ytop
    c.drawImage(ImageReader(png),20,y,w,h)
    to=c.beginText(24,y+h-14);to.setTextRenderMode(3);to.setFont('Helvetica',9)
    for ln in pulito(testo).split('\n'):
        for chunk in re.findall(r'.{1,150}(?:\s+|$)',ln):
            if chunk.strip():to.textLine(chunk.strip())
    c.drawText(to)
    c.setFillColor(colors.HexColor('#2060AF'));c.setFont('Helvetica-Bold',8)
    c.drawString(20,14,pulito(f'{MAT.upper()} - Pagina {n}'))
def cover_png(out,mappe=False):
    from playwright.sync_api import sync_playwright
    img=L+'img/IMG_COPERTINA_lana_seta.png'
    with sync_playwright() as p:
        br=p.chromium.launch(executable_path='/opt/pw-browsers/chromium');pg=br.new_page(viewport={'width':1920,'height':1080})
        pg.goto('file:///home/user/lav/prod/copertina.html');pg.evaluate('document.fonts.ready.then(()=>true)');pg.wait_for_timeout(300)
        pg.evaluate('d=>setData(d)',dict(kicker=MAT.upper(),titolo='Preparazione',sub='Tecnico Sistema Moda · III anno'+(' · MAPPE' if mappe else ''),voci=[],img=img,foot=''))
        pg.evaluate('()=>{setSteps([]);render(20)}');pg.screenshot(path=out);br.close()
def pagine_parte(parte,timeline,mappe_only=False):
    MAPPA=dict(json.load(open(L+f'scene_Parte{parte}.json')));fr=frasi(L+'Lezione.1.-.Preparazione.pt.1.1.pdf');P=[]
    for nome,t0,d in timeline:
        if nome in('SIGLA','SIGLA_FINALE'):continue
        is_map=bool(re.match(r'M\d+$',nome) or nome=='FM')
        if mappe_only and not is_map:continue
        m=re.match(r'D(\d+)$',nome)
        if m and int(m.group(1))>0:
            k=int(m.group(1));info=json.load(open(L+f'bg/A{k:02d}/info.json'))
            for g in info['G']:
                first=info['items'][g[0]]['T'];nxt=info['items'][g[-1]+1]['T'] if g[-1]+1<len(info['items']) else info['frames']/30
                t=max(first+0.5,nxt-0.6);png=f'/tmp/disp_{k}_{g[0]}.png'
                subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{t:.2f}','-i',L+f'bg/A{k:02d}/prof.mp4','-frames:v','1',png],check=True)
                tx='LA PROFESSORESSA SPIEGA\n'+'\n'.join(re.sub(r'\s+',' ',fr[info['items'][i]['j']][1]) for i in g)
                P.append((png,tx))
        else:
            sc=MAPPA.get(nome,nome);png=SC+sc+'.page.png';tf=SC+sc+'.page.txt'
            if os.path.exists(png):P.append((png,open(tf).read() if os.path.exists(tf) else ''))
    return P
def costruisci(parte,timeline,out,mappe=False):
    P=pagine_parte(parte,timeline,mappe_only=mappe)
    c=canvas.Canvas(out,pagesize=landscape(A4));c.setTitle(('Mappe - ' if mappe else 'Dispensa - ')+'Preparazione - '+MAT)
    cp=f'/tmp/cover_{int(mappe)}.png';cover_png(cp,mappe)
    img_pagina(c,cp,f'{MAT}\nPreparazione\nTecnico Sistema Moda - III anno'+('\nMAPPE' if mappe else ''),0);c.showPage()
    for n,(png,tx) in enumerate(P,1):
        img_pagina(c,png,tx,n);c.showPage()
    c.save();return len(P)
