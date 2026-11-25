import json,sys,os,subprocess,html as H
sys.path.insert(0,'/tmp/w14/build')
import gen
gen.PROFON=False;gen.DARK=False
E=H.escape
ENC=['-c:v','libx264','-preset','veryfast','-crf','19','-pix_fmt','yuv420p','-r','30','-an','-x264-params','keyint=60:scenecut=0','-threads','2']
COL={'c':('#FFDCC6','#C2410C'),'cel':('#DCEEFB','#1D4ED8'),'pag':('#FFF3BF','#A16207'),'men':('#DDF3E4','#15803D'),'lil':('#EBE3F7','#6D28D9')}
LEG='<div style="position:absolute;right:60px;top:24px;display:flex;gap:16px;font:600 20px Fig;color:#0B1530">'+''.join(f'<span style="display:flex;align-items:center;gap:6px"><i style="display:inline-block;width:24px;height:18px;background:{COL[k][0]};border:3px solid {COL[k][1]};border-radius:4px"></i>{t}</span>' for k,t in (('c','concetto centrale'),('cel','date e sequenze'),('pag','parole chiave'),('men','esempi e opere'),('lil','conseguenze')))+'</div>'
def box(x,y,w,h,t,k,fs=34,active=False,big=False):
    f,b=COL[k];ring='box-shadow:0 0 0 7px #FFE600;' if active else ''
    return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;box-sizing:border-box;display:flex;align-items:center;justify-content:center;text-align:center;padding:8px 18px;border-radius:16px;background:{f};border:5px solid {b};color:#0B1530;font:{"800 52px Bric" if big else f"600 {fs}px/1.3 Fig"};{ring}">{t}</div>'
def line(x1,y1,x2,y2): return f'<path d="M{x1},{y1} C{(x1+x2)/2},{y1} {(x1+x2)/2},{y2} {x2},{y2}" stroke="#0B1530" stroke-width="4" fill="none" opacity=".7"/>'
def screen(items,k,pag):
    """items: lista (tempo,[html box],linea) ; mostra i primi k, ultimo con anello giallo"""
    svg='';bx=''
    for i,(t,args,ln) in enumerate(items):
        if i<k:
            if ln: svg+=ln
            bx+=box(*args,active=(i==k-1))
    body=f'<div style="position:absolute;left:80px;top:128px" class="lab">MAPPA CONCETTUALE · LUIGI PIRANDELLO</div>{LEG}<svg style="position:absolute;left:0;top:0" width="1920" height="1080">{svg}</svg>{bx}'
    return gen.page(body,pag,prof=False)
# schermata A: vita
C=(60,470,360,150,'LUIGI PIRANDELLO','c',34,False,True)
def cen(): return (60,470,360,150,'LUIGI PIRANDELLO','c',34)
A=[(0.0,(60,470,360,150,'LUIGI PIRANDELLO','c'),None),(5.0,(470,300,160,64,'La vita','pag'),line(420,545,470,332))]
vita=[(7.7,'<b>1867</b> - nasce ad Agrigento, da famiglia benestante'),(12.6,'1886 - studia a Palermo, poi Roma, infine nel 1889 a Bonn (Germania): Laurea in Lettere'),(22.0,'1892 - torna in Italia'),(25.0,'1894 - si sposa e va a vivere a Roma dove insegna Letteratura'),(30.4,'1903 - la zolfatara di famiglia è distrutta: precarie condizioni economiche'),(35.5,'la moglie comincia ad avere disturbi mentali'),(39.3,'anni Venti: comincia il successo delle opere teatrali'),(43.0,'1934: premio Nobel per la letteratura'),(47.2,'<b>1936</b> - Muore a Roma')]
pos=[(700,120,560,150),(700,285,560,170),(700,470,560,100),(700,585,560,150),(700,750,560,150),(1290,120,560,130),(1290,265,560,150),(1290,430,560,110),(1290,555,560,100)]
SA=[(0.0,(60,470,360,150,'LUIGI PIRANDELLO','c',34),None)]
SA.append((5.0,(470,300,160,64,'La vita','pag',34),line(420,545,470,332)))
for (t,tx),(x,y,w,h) in zip(vita,pos): SA.append((t,(x,y,w,h,tx,'cel',32),line(630,332,x,y+h/2)))
SB=[(0.0,(60,470,360,150,'LUIGI PIRANDELLO','c',34),None)]
SB.append((50.7,(470,190,300,80,'introduce in letteratura','pag',32),line(420,545,470,230)))
SB.append((51.9,(840,190,520,150,"- l'ironia,<br>- l'umorismo<br>- crisi delle certezze",'pag',34),line(770,230,840,265)))
SB.append((57.5,(470,640,230,70,'tematiche','pag',34),line(420,545,470,675)))
SB.append((59.6,(760,420,420,180,"la condizione di sofferenza e assurdità dell'esistenza umana",'lil',32),line(700,675,760,510)))
SB.append((63.3,(1230,390,600,92,"difficoltà a distinguere la realtà dall'apparenza",'men',30),line(1180,510,1230,436)))
SB.append((66.4,(1230,495,600,92,"l'individuo vive con addosso una maschera",'men',30),line(1180,510,1230,541)))
SB.append((68.0,(1230,600,300,70,'rapporti inautentici','men',30),line(1180,510,1230,635)))
SB.append((69.5,(1550,600,280,70,'casualità','men',30),line(1180,510,1550,635)))
SB.append((72.4,(760,640,420,110,'vicende curiose e paradossali','lil',32),line(700,675,760,695)))
SB.append((74.7,(760,780,520,130,"i suoi personaggi soffrono la solitudine e l'incomunicabilità",'lil',32),line(700,675,760,845)))
SC=[(0.0,(60,470,360,150,'LUIGI PIRANDELLO','c',34),None)]
SC.append((80.0,(470,470,170,64,'opere','pag',34),line(420,545,470,502)))
SC.append((81.8,(700,130,460,64,'novelle','pag',32),line(640,502,700,162)))
SC.append((82.6,(700,205,460,110,'Novelle per un anno <b>(dal 1894)</b>','men',32),line(1160,162,1160,260)))
SC.append((85.9,(700,360,460,64,'romanzi','pag',32),line(640,502,700,392)))
SC.append((86.8,(700,435,460,72,"L'esclusa <b>1901</b>",'men',32),None))
SC.append((89.5,(700,520,460,72,'Il fu Mattia Pascal <b>1904</b>','men',32),None))
SC.append((92.0,(700,605,460,110,'Uno nessuno e centomila <b>1926</b>','men',32),None))
SC.append((95.4,(1230,130,600,64,'testi teatrali','pag',32),line(640,502,1230,162)))
th=[(96.8,'Così è se (se vi pare) <b>1917</b>'),(99.5,'Il berretto a sonagli <b>1917</b>'),(103.0,'Il gioco delle parti <b>1918</b>'),(106.2,"Sei personaggi in cerca d'autore <b>1921</b>"),(110.0,'Enrico IV <b>1921</b>'),(112.4,'Questa sera si recita a soggetto <b>1929</b>')]
for i,(t,tx) in enumerate(th): SC.append((t,(1230,210+i*108,600,96,tx,'men',32),None))
SC.append((116.5,(700,780,460,64,'saggi','pag',32),line(640,502,700,812)))
SC.append((117.2,(700,860,460,72,"L'umorismo <b>1908</b>",'men',32),None))
SCREENS=[(SA,0.0,50.2,32),(SB,50.2,79.8,33),(SC,79.8,121.0,34)]
OFF=0.4;LEN=120.44;EXTRA=4.0
nf=round((OFF+LEN+1.0+EXTRA)*30)
parts=[];states=[]
def add(nm,t0,t1): states.append((nm,t0,t1))
for si,(S,a,b,pag) in enumerate(SCREENS):
    for k in range(1,len(S)+1):
        gen.scrivi(f'map25_{si}_{k}',screen(S,k,pag))
        t0=a if k==1 else S[k-1][0]; t1=S[k][0] if k<len(S) else b
        if k==1 and len(S)>1: t1=S[1][0]
        add(f'map25_{si}_{k}',t0,t1)
subprocess.run(['node','/tmp/w14/build/render.js','/tmp/w14/build/html','/tmp/w14/build/png'],check=True)
# schermata finale intera 4 s: vecchia mappa intera
fin_start=OFF+LEN+1.0
segs=[]
for i,(nm,t0,t1) in enumerate(states):
    f0=round((OFF+t0)*30);f1=round((OFF+t1)*30)
    if i==0: f0=0
    if i==len(states)-1: f1=round(fin_start*30)
    k=f1-f0
    if k>0: segs.append((nm,k))
# riempio eventuali buchi: ultimo stato fino a fin_start
tot=sum(k for _,k in segs);segs.append(('FIN',nf-tot))
for i,(nm,k) in enumerate(segs):
    src=f'/tmp/w14/build/png/{nm}.png' if nm!='FIN' else '/tmp/w14/build/png/mappa_prof.png'
    po=f'/tmp/w14/vc/m{i}.mp4';subprocess.run(['ffmpeg','-v','error','-y','-loop','1','-framerate','30','-t',f'{k/30:.4f}','-i',src,'-frames:v',str(k),*ENC,po],check=True);parts.append(po)
open('/tmp/w14/vc/lm.txt','w').write(''.join(f"file '{p}'\n" for p in parts))
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','/tmp/w14/vc/lm.txt','-c','copy','/tmp/w14/vc/R1.mp4'],check=True)
meta=json.load(open('/tmp/w14/vc/meta.json'));meta['R1']={'frames':nf};json.dump(meta,open('/tmp/w14/vc/meta.json','w'))
print('ok',nf,len(segs))
