# Dispensa A4 orizzontale (identica alle slide del video, con strato di testo invisibile) e PDF delle mappe
import sys,json,os,subprocess;sys.path.insert(0,'/home/user/Lezioni/lavoro_lez03')
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image
import dati,lib,scene_doc as SD,mappe as MP
import montaggio as M
from parti import *
pdfmetrics.registerFont(TTFont('Fig','/home/user/Lezioni/kit/caratteri/Figtree-Regular.ttf'))
PW,PH=landscape(A4)
def cam_still(t):
    f=f'/tmp/w/b/cam_{int(t)}.png'
    if not os.path.exists(f):
        M.sh(['ffmpeg','-v','error','-y','-ss',f'{t:.2f}','-i',SD.SRC,'-vf',M.CAMV,'-frames:v','1',f])
    return Image.open(f).convert('RGB')
def pagina(img,testi,c):
    p='/tmp/w/b/dp.jpg';img.save(p,quality=93)
    c.drawImage(p,0,(PH-PW*9/16)/2,PW,PW*9/16)
    t=c.beginText(20,PH-30);t.setTextRenderMode(3);t.setFont('Fig',8)
    for x in testi:t.textLine(x)
    c.drawText(t);c.showPage()
def build():
    kI=json.load(open('/tmp/w/b/kI.json'))['kI'];sc=piano_scene(kI)
    for s in sc:build_scene(s,render=False)      # fissa i numeri di pagina
    for k in [('m','FR',1),('m','FR',2),('m','IT',1),('m','IT',2)]:SD.page_of(k)
    c=canvas.Canvas('/tmp/w/final/Dispensa_Storia_arte_V_Lez3.pdf',pagesize=landscape(A4));c.setTitle('Storia dell\'arte V · Il Realismo · Dispensa')
    pagina(cover(False),[ "STORIA DELL'ARTE V","Il Realismo"]+ARGS,c)
    # pagina 2: argomenti
    pagina(args_slide(None),['Di cosa parliamo']+ARGS,c)
    first={}
    for s in sc:
        first.setdefault(s['nome'],s)
    inv={v:k for k,v in SD.PAGES.items()}
    scn={}
    for s in sc:
        if s['tipo']=='txt':scn.setdefault(('t',s['id']),s)
    for pg in sorted(inv):
        key=inv[pg]
        if key[0]=='t':
            p,wi=key[1],key[2];cards=dati.cards(p);wc=[cards[i] for i in SD.WIN[p][wi]]
            img=lib.slide_cards(pg,dati.TIT[p],wc,None,dati.KW[p])
            s=[x for x in sc if x['tipo']=='txt' and x['id']==p][0];a,b=piece_range(s['k0'],s['k1'])
            testi=[dati.TIT[p]]+[''.join(r[0]+' ' for r in cc) for cc in wc]+['Parole chiave']+dati.KW[p]
        elif key[0]=='i':
            im=key[1];s=[x for x in sc if x['tipo']=='img' and x['id']==im][0];a,b=piece_range(s['k0'],s['k1'])
            img=lib.slide_image(pg,SD.TITOLI_IMG[im],im,dati.DID[im],dati.KW[SD.IMGKW[im]])
            testi=[SD.TITOLI_IMG[im],dati.DID[im],'Parole chiave']+dati.KW[SD.IMGKW[im]]
        else:
            nm,scr=key[1],key[2]
            sp={('FR',1):(MP.FR_A,MP.FR_ORDER),('FR',2):(MP.FR_B,MP.FR_B_ORDER),('IT',1):(MP.IT_A,MP.IT_ORDER),('IT',2):(MP.IT_B,MP.IT_B_ORDER)}[(nm,scr)]
            img=MP.render_map(sp[0],set(sum([o[0] for o in sp[1]],[])),set(),f'Pagina {pg}')
            testi=['Mappa del professore']+[b['t'] for b in sp[0]['boxes'].values() if b['k']!='img']
            pagina(img,testi,c);continue
        cam=cam_still((a+b)/2);img.paste(cam,(1428,148))
        pagina(img,testi,c)
    c.save();print('dispensa pagine',c.getPageNumber()-1)
    # PDF mappe
    c=canvas.Canvas('/tmp/w/final/Mappe_Storia_arte_V_Lez3.pdf',pagesize=landscape(A4));c.setTitle('Storia dell\'arte V · Il Realismo · Mappe')
    cv=cover(False);d=ImageDraw.Draw(cv);d.rounded_rectangle((80,470,520,560),16,fill=GIALLO);d.text((110,486),'MAPPE',font=F('t',60),fill=NOTTE)
    pagina(cv,['MAPPE',"STORIA DELL'ARTE V",'Il Realismo'],c)
    for (nm,scr),(sp,od) in {('FR',1):(MP.FR_A,MP.FR_ORDER),('FR',2):(MP.FR_B,MP.FR_B_ORDER),('IT',1):(MP.IT_A,MP.IT_ORDER),('IT',2):(MP.IT_B,MP.IT_B_ORDER)}.items():
        pg=SD.PAGES[('m',nm,scr)]
        pagina(MP.render_map(sp,set(sum([o[0] for o in od],[])),set(),f'Pagina {pg}'),['Mappa del professore']+[b['t'] for b in sp['boxes'].values() if b['k']!='img'],c)
    c.save()
if __name__=='__main__':build()
