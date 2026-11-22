# Mappe del prof (3) ridisegnate nel modello BES: stati cumulativi, un riquadro alla volta con la sua freccia.
import json, sys
sys.path.insert(0,'/home/user/Lezioni/lavoro')
from tlib import BASE_CSS, esc, LOGO
COL={'pesca':('#FFDCC6','#C2410C'),'celeste':('#DCEEFB','#1D4ED8'),'paglierino':('#FFF3BF','#A16207'),'menta':('#DDF3E4','#15803D'),'lilla':('#EBE3F7','#6D28D9')}
CSS='''
.b{position:absolute;display:flex;align-items:center;justify-content:center;text-align:center;padding:8px 18px;border-radius:16px;font:500 34px/1.25 Fig}
.c{font:800 44px Bri;letter-spacing:.02em;border-radius:20px}
.al{position:absolute;font:600 30px/1 Fig;color:#0B1530;background:#fff;padding:2px 10px;white-space:nowrap}
.hl{box-shadow:0 0 0 9px #FFE600,0 10px 24px rgba(11,21,48,.2)!important;height:auto}
.leg{position:absolute;right:60px;top:24px;display:flex;gap:18px;font:600 20px Fig;color:#0B1530}
.leg span{display:flex;align-items:center;gap:7px}.leg i{display:inline-block;width:24px;height:17px;border-radius:4px;border:3px solid}
.mt{position:absolute;left:60px;top:62px;font:800 44px/1.1 Bri;color:#2060AF;width:1800px}
.mk{position:absolute;left:60px;top:26px;font:700 22px Fig;letter-spacing:.14em;color:#2060AF}
.ft{top:1030px!important;left:60px}.pg{top:1030px!important}
'''
LEG=''.join(f'<span><i style="background:{COL[k][0]};border-color:{COL[k][1]}"></i>{t}</span>' for k,t in [('pesca','concetto centrale'),('celeste','date e sequenze'),('paglierino','parole chiave'),('menta','esempi e opere'),('lilla','conseguenze')])
MAPPE={
 'M1':dict(titolo='Quali sono il programma e la struttura del Partito nazista?',
  boxes=[('B1',660,170,600,92,'pesca','IL PARTITO NAZISTA',1),
   ('B2',60,360,460,92,'paglierino','ideologia',0),('B3',730,360,460,92,'paglierino','squadre armate',0),('B4',1400,360,460,92,'paglierino','Hitler',0),
   ('B5',130,520,470,92,'paglierino','l\'idea di «popolo»',0),('B6',130,640,470,92,'paglierino','il nazionalismo',0),('B7',130,760,470,92,'paglierino','l\'antisemitismo',0),('B8',130,880,470,92,'paglierino','l\'antibolscevismo',0),
   ('B9',790,520,560,120,'menta','le squadre d\'assalto (SA)',0),('B10',790,690,560,120,'menta','le squadre di protezione (SS)',0),
   ('B11',1470,520,400,92,'paglierino','oratore trascinante',0),('B12',1470,640,400,92,'paglierino','leader indiscusso',0)],
  frecce=[('A1',[(960,262),(960,300),(290,300),(290,358)],'sostiene una',(480,300)),('A2',[(960,262),(960,358)],'si dota di',(960,310)),('A3',[(960,262),(960,300),(1630,300),(1630,358)],'trova in',(1440,300)),
   ('A4',[(96,452),(96,566),(128,566)],None,None),('A5',[(96,566),(96,686),(128,686)],None,None),('A6',[(96,686),(96,806),(128,806)],None,None),('A7',[(96,806),(96,926),(128,926)],None,None),
   ('A8',[(760,452),(760,580),(788,580)],None,None),('A9',[(760,580),(760,750),(788,750)],None,None),
   ('A10',[(1440,452),(1440,566),(1468,566)],None,None),('A11',[(1440,566),(1440,686),(1468,686)],None,None)],
  etichette=[('basata su',122,478),('che sono',792,478),('un',1472,478)],
  ordine=[('B1',[]),('B2',['A1']),('B5',['A4']),('B6',['A5']),('B7',['A6']),('B8',['A7']),('B3',['A2']),('B9',['A8']),('B10',['A9']),('B4',['A3']),('B11',['A10']),('B12',['A11'])]),
 'M2':dict(titolo='Come giunge al potere Hitler?',
  boxes=[('B1',560,170,800,100,'pesca','LA CRISI DEL 1929',1),('B2',460,370,1000,100,'lilla','il successo elettorale dei nazisti',0),
   ('B3',460,570,1000,100,'celeste','Hitler cancelliere (30 gennaio 1933)',0),('B4',180,810,640,130,'lilla','decreta l\'emergenza',0),('B5',1100,810,640,130,'lilla','chiede e ottiene i pieni poteri',0)],
  frecce=[('A1',[(960,270),(960,368)],'favorisce',(960,320)),('A2',[(960,470),(960,568)],'che porta a',(960,520)),('A3',[(960,670),(960,720),(500,720),(500,808)],'che',(960,720)),('A4',[(960,720),(1420,720),(1420,808)],None,None)],
  etichette=[],
  ordine=[('B1',[]),('B2',['A1']),('B3',['A2']),('B4',['A3']),('B5',['A4'])]),
 'M3':dict(titolo='',
  boxes=[('B1',660,170,600,92,'pesca','IL REGIME NAZISTA',1),
   ('B2',60,360,540,92,'paglierino','strumenti di repressione',0),('B3',690,360,540,92,'paglierino','consenso',0),('B4',1320,360,540,92,'paglierino','economia',0),
   ('B5',130,520,470,100,'menta','la Gestapo',0),('B6',130,650,470,110,'menta','il Tribunale del popolo',0),('B7',130,790,470,130,'menta','i campi di concentramento',0),
   ('B8',760,520,470,130,'menta','la «Forza attraverso la gioia»',0),('B9',760,680,470,100,'menta','la Gioventù hitleriana',0),('B10',760,810,470,130,'menta','gli spettacoli di massa, raduni',0),
   ('B11',1390,520,470,130,'lilla','massiccio intervento dello Stato',0),('B12',1390,740,470,100,'lilla','potenziare l\'esercito',0)],
  frecce=[('A1',[(960,262),(960,300),(330,300),(330,358)],'si dota di',(560,300)),('A2',[(960,262),(960,358)],'cerca il',(960,310)),('A3',[(960,262),(960,300),(1590,300),(1590,358)],'in',(1300,300)),
   ('A4',[(96,452),(96,570),(128,570)],None,None),('A5',[(96,570),(96,705),(128,705)],None,None),('A6',[(96,705),(96,855),(128,855)],None,None),
   ('A7',[(726,452),(726,585),(758,585)],None,None),('A8',[(726,585),(726,730),(758,730)],None,None),('A9',[(726,730),(726,875),(758,875)],None,None),
   ('A10',[(1626,452),(1626,518)],'pratica un',(1626,486)),('A11',[(1626,650),(1626,738)],'con lo scopo di',(1626,694))],
  etichette=[('come',122,478),('attraverso',752,478)],
  ordine=[('B1',[]),('B3',['A2']),('B8',['A7']),('B9',['A8']),('B10',['A9']),('B2',['A1']),('B5',['A4']),('B6',['A5']),('B7',['A6']),('B4',['A3']),('B11',['A10']),('B12',['A11'])]),
}
# M3: l'ordine di lettura segue la voce (repressione prima, poi consenso, poi economia) come nella mappa del prof, da sinistra a destra
MAPPE['M3']['ordine']=[('B1',[]),('B2',['A1']),('B5',['A4']),('B6',['A5']),('B7',['A6']),('B3',['A2']),('B8',['A7']),('B9',['A8']),('B10',['A9']),('B4',['A3']),('B11',['A10']),('B12',['A11'])]
def stato_html(nome,passo,finale=False,pagina='1'):
    M=MAPPE[nome];vis=M['ordine'][:passo+1] if passo is not None else M['ordine']
    vb={b for b,_ in vis};va={a for _,al in vis for a in al}
    cur=None if finale or passo is None else vis[-1][0]
    svg='<svg style="position:absolute;left:0;top:0" width="1920" height="1080"><defs><marker id="ah" markerUnits="userSpaceOnUse" markerWidth="30" markerHeight="30" refX="15" refY="15" orient="auto"><path d="M2,4 L28,15 L2,26 z" fill="#0B1530"/></marker></defs>'
    for a,pts,lab,pos in M['frecce']:
        if a in va:
            d=' '.join(f'{x},{y}' for x,y in pts)
            svg+=f'<polyline points="{d}" fill="none" stroke="#0B1530" stroke-width="5" stroke-linejoin="round" marker-end="url(#ah)"/>'
    svg+='</svg>';h=svg
    for a,pts,lab,pos in M['frecce']:
        if a in va and lab: h+=f'<div class="al" style="left:{pos[0]}px;top:{pos[1]}px;transform:translate(-50%,-50%)">{esc(lab)}</div>'
    # etichette dei rami (basata su…) compaiono con la loro prima freccia
    first={'M1':{'basata su':'A4','che sono':'A8','un':'A10'},'M3':{'come':'A4','attraverso':'A7'}}.get(nome,{})
    for t,x,y in M['etichette']:
        if first.get(t) in va: h+=f'<div class="al" style="left:{x}px;top:{y}px;font-size:30px;background:none;transform:translateY(-50%)">{esc(t)}</div>'
    for b,x,y,w,hh,col,t,c in M['boxes']:
        if b in vb:
            f,bo=COL[col];cl='b c' if c else 'b'
            h+=f'<div class="{cl}{" hl" if b==cur else ""}" style="left:{x}px;top:{y}px;width:{w}px;min-height:{hh}px;background:{f};border:{5 if c else 4}px solid {bo}">{esc(t)}</div>'
    body=f'<div class="mk">MAPPA DEL PROFESSORE</div><div class="leg">{LEG}</div><div class="mt">{esc(M["titolo"])}</div>' if False else f'<div class="mk">MAPPA</div><div class="leg">{LEG}</div><div class="mt" style="top:60px">{esc(M["titolo"])}</div>'
    body+=h+'<div class="fl" style="top:1020px"></div><div class="ft">STORIA</div>'
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{BASE_CSS}{CSS}</style></head><body>{body}</body></html>'
if __name__=='__main__':
    L=[]
    for n,M in MAPPE.items():
        for i in range(len(M['ordine'])):
            p=f'/tmp/w/map_{n}_{i}.html';open(p,'w').write(stato_html(n,i));L.append({'html':p,'png':f'/tmp/w/map_{n}_{i}.png'})
        p=f'/tmp/w/map_{n}_fin.html';open(p,'w').write(stato_html(n,None,True));L.append({'html':p,'png':f'/tmp/w/map_{n}_fin.png'})
    json.dump(L,open('/tmp/w/lmap.json','w'))
