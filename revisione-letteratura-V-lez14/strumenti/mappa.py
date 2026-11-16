import sys;sys.path.insert(0,'/tmp/w14/build')
import gen,html
E=html.escape
boxes=[];lines=[];
def box(x,y,w,h,t,cls='b',fs=22):
    boxes.append(f'<div class="{cls}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;font-size:{fs}px"><span>{t}</span></div>');return (x,y,w,h)
def line(a,b,side_a='r',side_b='l',col='#2060AF'):
    def pt(r,s):
        x,y,w,h=r;return {'l':(x,y+h/2),'r':(x+w,y+h/2),'t':(x+w/2,y),'b':(x+w/2,y+h)}[s]
    (x1,y1),(x2,y2)=pt(a,side_a),pt(b,side_b)
    if side_a in 'lr': mx=(x1+x2)/2;d=f'M{x1},{y1} C{mx},{y1} {mx},{y2} {x2},{y2}'
    else: my=(y1+y2)/2;d=f'M{x1},{y1} C{x1},{my} {x2},{my} {x2},{y2}'
    lines.append(f'<path d="{d}" stroke="{col}" stroke-width="3" fill="none" opacity=".75"/>')
C=box(745,205,430,92,'LUIGI PIRANDELLO','c',36)
# vita
V=box(470,430,110,48,'vita','n',24)
vita=['<b>1867</b> - nasce ad Agrigento, da famiglia benestante','1886 - studia a Palermo, poi Roma infine nel 1889 a Bonn (Germania): Laurea in Lettere','1892 - torna in Italia','1894 - si sposa e va a vivere a Roma dove insegna Letteratura','1903 - la zolfatara di famiglia è distrutta: precarie condizioni economiche','la moglie comincia ad avere disturbi mentali','anni Venti: comincia il successo delle opere teatrali','1934: premio Nobel per la letteratura','<b>1936</b> - Muore a Roma']
hs=[56,72,40,56,56,56,56,40,40];y=180;
line(C,V,'l','t')
for t,h in zip(vita,hs):
    r=box(80,y,360,h,t,'b',19);line(V,r,'l','r');y+=h+14
# introduce
I=box(1160,160,250,64,'introduce in letteratura','n',20)
R=box(1500,150,340,80,"- l'ironia,<br>- l'umorismo<br>- crisi delle certezze",'g',21)
line(C,I,'r','l','#3C9A5F');line(I,R,'r','l','#3C9A5F')
# tematiche
T=box(1160,440,170,48,'tematiche','n',24);line(C,T,'r','l')
a=box(1365,300,260,110,"la condizione di sofferenza e assurdità dell'esistenza umana",'o',21)
b=box(1365,470,260,64,'vicende curiose e paradossali','o',21)
c=box(1365,555,260,96,"i suoi personaggi soffrono la solitudine e l'incomunicabilità",'o',21)
for x in (a,b,c): pass
line(T,a,'r','l');line(T,b,'r','l');line(T,c,'r','l')
for i,t in enumerate(["difficoltà a distinguere la realtà dall'apparenza","l'individuo vive con addosso una maschera",'rapporti inautentici','casualità']):
    r=box(1655,240+[0,76,152,214][i],185,[66,66,48,48][i],t,'b',17);line(a,r,'r','l')
# opere
O=box(880,690,120,46,'opere','n',24);line(C,O,'b','t')
groups=[('novelle',[("Novelle per un anno<br><small>(dal 1894)</small>",)],40),('romanzi',[("L'esclusa<br><small>1901</small>",),("Il fu Mattia Pascal<br><small>1904</small>",),("Uno nessuno e centomila<br><small>1926</small>",)],470),
 ('testi teatrali',[("Così è (se vi pare)<br><small>1917</small>",),("Il berretto a sonagli<br><small>1917</small>",),("Il gioco delle parti<br><small>1918</small>",),("Sei personaggi in cerca di autore<br><small>1921</small>",),("Enrico IV<br><small>1921</small>",),("Questa sera si recita a soggetto<br><small>1929</small>",)],0),('saggi',[("L'umorismo<br><small>1908</small>",)],0)]
x=470;pos={}
# righe figli
cw=150;gap=10;y1=830
xs=[]
cur=520
G=[]
for gname,items,_ in groups: G.append((gname,items))
tot=sum(len(i) for _,i in G);W=1760;cw=int((W-(tot-1)*gap-3*30)/tot);cur=80
for gname,items in G:
    n=len(items);gw=n*cw+(n-1)*gap
    g=box(cur+gw/2-90,770,180,40,gname,'n',21);line(O,g,'b','t')
    for t in items:
        r=box(cur,825,cw,125,t[0],'t',18);line(g,r,'b','t');cur+=cw+gap
    cur+=30-gap+gap
body=f'<svg style="position:absolute;left:0;top:0" width="1920" height="1080">{"".join(lines)}</svg>'+''.join(boxes)
body=f'<div style="position:absolute;left:80px;top:128px;right:80px" class="lab">MAPPA CONCETTUALE · LUIGI PIRANDELLO</div>'+'<div style="position:absolute;inset:0;top:0">'+body+'</div>'
css=""".b,.g,.o,.t,.n,.c{position:absolute;display:flex;align-items:center;justify-content:center;text-align:center;line-height:1.18;padding:6px 10px;border-radius:12px;color:#0B1530;font-weight:600}
.b{background:#fff;border:2px solid #C9D3E3}.t{background:#E8F4FB;border:2px solid #2060AF}.g{background:#EAF6EC;border:2px solid #3C9A5F}.o{background:#FFF3D6;border:2px solid #E2A93B}
.n{background:#fff;border:3px solid #2060AF;border-radius:30px;color:#2060AF;font-weight:700}.c{background:#0B1530;color:#fff;font:800 36px Bric;border-radius:46px}
small{font-size:.8em;font-weight:700;color:#2060AF}"""
h=gen.page(body,pag=1,prof=False,extra=css).replace('Pagina 1','Mappa della lezione')
open('/tmp/w14/pdfhtml/mappa.html','w',encoding='utf-8').write(h)
