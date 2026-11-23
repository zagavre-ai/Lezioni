# mappa del prof (una sola per la lezione), ridisegnata nel modello BES: stesse parole, stesse frecce
import sys, os, json, subprocess
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import anim
HERE=os.path.dirname(os.path.abspath(__file__))
from anim import *
TITOLO_MAPPA="Che cos'è l'Espressionismo?"
# id: (classe, x,y,w,h, testo)   classi: l1 pesca, cel celeste, pag paglierino, men menta, lil lilla ; 'lbl' ovale
BOX={
 'C':('l1',760,100,400,96,"ESPRESSIONISMO"),
 'cose':('pag',535,140,150,70,"cos'è"),
 'def':('cel',20,95,480,180,"un movimento artistico europeo nato in Germania nel 1905"),
 'prec':('pag',380,340,230,70,"precursori"),
 'vg':('men',20,300,310,58,"Vincent Van Gogh"),'mu':('men',20,368,310,58,"Edvard Munch"),'ga':('men',20,436,310,58,"Paul Gauguin"),
 'stile':('pag',1250,115,140,70,"stile"),
 's1':('pag',1420,95,480,100,"deformazioni di volti, figure violente"),
 's2':('pag',1420,205,480,100,"colori forti e contrastati; marcata linea di contorno"),
 'art':('pag',1160,350,290,110,"gli artisti rappresentano"),
 'a1':('lil',1500,335,400,70,"il proprio stato d'animo"),'a2':('lil',1500,420,400,70,"il dramma esistenziale"),
 'mov':('pag',855,300,210,70,"movimenti"),
 'db':('pag',20,510,360,100,"Die Brücke (Il Ponte)"),'dbd':('cel',20,622,360,80,"1905, a Dresda"),
 'dbn':('men',20,714,360,150,"Kirchner, Schmidt-Rottluff, Heckel"),'dbp':('lil',20,876,360,160,"un ponte simbolico tra l'artista e il mondo, l'arte verso nuovi mondi espressivi"),
 'man':('pag',410,510,610,530,"<b>manifesto</b><br>1. rifiuto dell'arte elegante<br>2. rappresentazione libera di idee, stati d'animo<br>3. immagini aggressive<br>4. figure deformate<br>5. rifiuto della prospettiva e del chiaroscuro<br>6. colori forti<br>7. linee spigolose"),
 'cav':('pag',1050,510,420,100,"Il Cavaliere Azzurro (1911)"),
 'cavd':('lil',1050,622,420,200,"ricercano una espressione spirituale attraverso il colore e la forma"),
 'cavn':('men',1050,834,420,200,"Kandinskij<br>Marc<br>Klee<br>Macke"),
 'no':('pag',1500,510,400,100,"Nuova Oggettività (1920)"),
 'nod':('lil',1500,622,400,180,"rappresentano la miseria sociale e morale"),
 'non':('men',1500,814,400,140,"Grosz<br>Otto Dix"),
}
EDGES={'e_cose':('C','cose'),'e_def':('cose','def'),'e_prec':('C','prec'),'e_vg':('prec','vg'),'e_mu':('prec','mu'),'e_ga':('prec','ga'),
 'e_stile':('C','stile'),'e_s1':('stile','s1'),'e_s2':('stile','s2'),'e_art':('C','art'),'e_a1':('art','a1'),'e_a2':('art','a2'),'e_mov':('C','mov'),
 'e_db':('mov','db'),'e_dbd':('db','dbd'),'e_dbn':('db','dbn'),'e_dbp':('db','dbp'),'e_man':('db','man'),'e_cav':('mov','cav'),'e_cavd':('cav','cavd'),'e_cavn':('cav','cavn'),
 'e_no':('mov','no'),'e_nod':('no','nod'),'e_non':('no','non')}
# ordine di lettura: (voce, marcatore, [box], [frecce])
STEPS=[(1,'al',['C'],[]),(1,'movimento',['cose','def'],['e_cose','e_def']),(1,'precursori',['prec'],['e_prec']),(1,'vincent',['vg'],['e_vg']),(1,'edvard',['mu'],['e_mu']),(1,'paul',['ga'],['e_ga']),
 (2,'stile',['stile'],['e_stile']),(2,'deformazioni',['s1'],['e_s1']),(2,'colori',['s2'],['e_s2']),(2,'artisti',['art'],['e_art']),(2,'proprio',['a1'],['e_a1']),(2,'dramma',['a2'],['e_a2']),
 (3,'movimenti',['mov'],['e_mov']),(3,'primo',['db'],['e_db']),(3,'millenovecentocinque',['dbd'],['e_dbd']),(3,'ponte',['dbp'],['e_dbp']),(3,'kirchner',['dbn'],['e_dbn']),(3,'manifesto',['man'],['e_man']),
 (4,'secondo',['cav'],['e_cav']),(4,'ricercano',['cavd'],['e_cavd']),(4,'kandinskij',['cavn'],['e_cavn']),(4,'terzo',['no'],['e_no']),(4,'rappresentano',['nod'],['e_nod']),(4,'grosz',['non'],['e_non'])]
CSSM='''@font-face{font-family:Fig;src:url(file:///root/.fonts/Figtree-SemiBold.ttf)}@font-face{font-family:FigB;src:url(file:///root/.fonts/Figtree-Bold.ttf)}@font-face{font-family:Bri;src:url(file:///root/.fonts/BricolageGrotesque-ExtraBold.ttf)}
html,body{margin:0;width:1920px;height:1080px;background:#fff;overflow:hidden}
#k{position:absolute;left:20px;top:8px;font:800 40px Bri;color:#0B1530}
#f{position:absolute;left:20px;bottom:6px;font:700 22px FigB;color:#2060AF;letter-spacing:.14em}
.b{position:absolute;box-sizing:border-box;display:flex;align-items:center;justify-content:center;text-align:center;padding:8px 14px;border-radius:14px;font:600 36px/1.2 Fig;color:#0B1530;opacity:0}
.b.left{text-align:left;justify-content:flex-start}
.l1{background:#FFDCC6;border:5px solid #C2410C;font:800 50px Bri}.cel{background:#DCEEFB;border:4px solid #1D4ED8}.lil{background:#EBE3F7;border:4px solid #6D28D9}
.pag{background:#FFF3BF;border:4px solid #A16207}.men{background:#DDF3E4;border:4px solid #15803D}
.b b{font-weight:800}
#leg{position:absolute;right:20px;top:14px;display:flex;gap:12px;font:600 18px Fig;color:#0B1530}#leg span{display:flex;align-items:center;gap:6px}#leg i{display:inline-block;width:22px;height:16px;border-radius:4px;border:3px solid}
.hl{box-shadow:0 0 0 8px #FFE600,0 10px 24px rgba(11,21,48,.18)}
svg{position:absolute;left:0;top:0}
'''
def html():
    bx=''.join(f'<div class="b {c}{" left" if "<br>" in t and i=="man" else ""}" id="B_{i}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">{t}</div>' for i,(c,x,y,w,h,t) in BOX.items())
    ed=''.join(f'<line id="{k}" stroke="#0B1530" stroke-width="7" marker-end="url(#ah)" opacity="0"/>' for k in EDGES)
    js='''const BOX=%s,EDG=%s;
function anchor(a,b){const A=BOX[a],B=BOX[b];const ax=A[1]+A[3]/2,ay=A[2]+A[4]/2,bx=B[1]+B[3]/2,by=B[2]+B[4]/2;
 function clip(r,cx,cy,tx,ty){const dx=tx-cx,dy=ty-cy;const sx=dx?(r[3]/2+2)/Math.abs(dx):1e9,sy=dy?(r[4]/2+2)/Math.abs(dy):1e9;const s=Math.min(sx,sy);return [cx+dx*s,cy+dy*s]}
 return [clip(A,ax,ay,bx,by),clip(B,bx,by,ax,ay)]}
for(const k in EDG){const [a,b]=EDG[k];const [p,q]=anchor(a,b);const e=document.getElementById(k);e.setAttribute('x1',p[0]);e.setAttribute('y1',p[1]);e.setAttribute('x2',q[0]);e.setAttribute('y2',q[1])}
function ease(x){x=Math.max(0,Math.min(1,x));return 1-Math.pow(1-x,3)}
window.render=function(S,t){ // S=[[ [box],[edges],start,dur ]]
 document.querySelectorAll('.b').forEach(e=>{e.style.opacity=0;e.classList.remove('hl')});document.querySelectorAll('line').forEach(e=>e.setAttribute('opacity',0));
 let cur=[];
 for(const [bs,es,st,du] of S){es.forEach(k=>document.getElementById(k).setAttribute('opacity',ease((t-(st-0.5))/0.4)));
  bs.forEach(b=>{const e=document.getElementById('B_'+b);const p=ease((t-st+0.15)/0.4);e.style.opacity=p;e.style.transform='translateY('+(14*(1-p))+'px)'});
  if(t>=st-0.15&&t<st+du) cur=bs}
 cur.forEach(b=>document.getElementById('B_'+b).classList.add('hl'))}
''' % (json.dumps({k:[0]+list(v[1:5]) for k,v in BOX.items()}),json.dumps(EDGES))
    leg='<div id="leg"><span><i style="background:#FFDCC6;border-color:#C2410C"></i>concetto centrale</span><span><i style="background:#DCEEFB;border-color:#1D4ED8"></i>date e sequenze</span><span><i style="background:#FFF3BF;border-color:#A16207"></i>parole chiave</span><span><i style="background:#DDF3E4;border-color:#15803D"></i>esempi e opere</span><span><i style="background:#EBE3F7;border-color:#6D28D9"></i>conseguenze</span></div>'
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSSM}</style></head><body><div id="k">{TITOLO_MAPPA}</div>{leg}<div id="f">STORIA DELL\'ARTE V</div><svg width="1920" height="1080"><defs><marker id="ah" markerUnits="userSpaceOnUse" markerWidth="34" markerHeight="34" refX="30" refY="17" orient="auto"><path d="M0,3 L32,17 L0,31 z" fill="#0B1530"/></marker></defs>{ed}</svg>{bx}<script>{js}</script></body></html>'
def build_video():
    wav,tot,offs=concat_voci('M_MAPPA',['M_MAPPA_1','M_MAPPA_2','M_MAPPA_3','M_MAPPA_4'],0.6)
    CONC['M_MAPPA']=(wav,tot,None); V0=0.8
    S=[]; groups={}
    for v,m,bs,es in STEPS: groups.setdefault(v,[]).append((m,bs,es))
    for v in (1,2,3,4):
        T=tempi_marcatori(f'M_MAPPA_{v}',[g[0] for g in groups[v]])
        for (m,bs,es),t in zip(groups[v],T): S.append([bs,es,V0+offs[v-1]+t,0])
    for i in range(len(S)): S[i][3]=(S[i+1][2]-S[i][2]) if i+1<len(S) else 2.5
    total=V0+tot+4.0
    open(f'{B}/mappa8.html','w').write(html())
    out=f'{B}/p_mappa.mkv'; mix_audio([(wav,V0,1.0)],total,f'{B}/a_mappa.wav'); json.dump(S,open(f'{B}/mappa8_steps.json','w'))
    json.dump({'parts':[(os.path.basename(wav),V0)],'total':total},open(f'{B}/meta_mappa.json','w'))
    r=subprocess.run(['node',f'{HERE}/mapframes.js',f'{B}/mappa8.html',f'{B}/mappa8_steps.json',str(total),f'{B}/a_mappa.wav',out,f'{B}/mappa8_finale.png'])
    if r.returncode: raise SystemExit('mappa fallita')
    return out
if __name__=='__main__': print(build_video())
