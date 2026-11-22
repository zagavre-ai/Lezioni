# Mappe del prof ridisegnate (modello BES approvato): un riquadro alla volta con la sua freccia mentre la voce Kore lo legge.
import sys,json,subprocess,math
sys.path.insert(0,'/home/claude/w19/lib')
from ui import *
COL={'c':('#FFDCC6','#C2410C'),'d':('#DCEEFB','#1D4ED8'),'k':('#FFF3BF','#A16207'),'e':('#DDF3E4','#15803D'),'s':('#EBE3F7','#6D28D9')}
LEG=[('c','concetto centrale'),('d','date e sequenze'),('k','parole chiave'),('e','esempi e opere'),('s','conseguenze')]
def html(m):
    s=f'<div class=abs style="left:60px;top:30px;font:700 22px Figtree;letter-spacing:.14em;color:#2060AF">MAPPA DELL\'ARGOMENTO</div>'
    s+='<div class=abs style="right:60px;top:26px;display:flex;gap:16px;font:600 19px Figtree">'+''.join(f'<span style="display:flex;align-items:center;gap:6px"><i style="display:inline-block;width:24px;height:17px;border-radius:4px;border:3px solid {COL[k][1]};background:{COL[k][0]}"></i>{t}</span>' for k,t in LEG)+'</div>'
    s+='<div class=abs style="left:60px;right:60px;top:70px;height:2px;background:#CBD5E1"></div>'
    s+=f'<div class=abs id=q style="left:60px;right:60px;top:84px;font:800 46px/1.15 \'Bricolage Grotesque\';color:#2060AF">{m["domanda"]}</div>'
    svg='<svg class=abs width=1920 height=1080 style="left:0;top:0"><defs><marker id=ah markerUnits=userSpaceOnUse markerWidth=40 markerHeight=40 refX=20 refY=20 orient=auto><path d="M0,4 L36,20 L0,36 z" fill="#0B1530"/></marker></defs>'
    lab=''
    for i,(a,b,l) in enumerate(m['edges']):
        A=m['nodes'][a];B=m['nodes'][b]
        x1=A['x']+A['w']/2;y1=A['y']+A['h'];x2=B['x']+B['w']/2;y2=B['y']
        dx,dy=x2-x1,y2-y1;L=math.hypot(dx,dy);ux,uy=dx/L,dy/L
        x1+=ux*6;y1+=uy*6;x2-=ux*22;y2-=uy*22   # la punta non entra nel riquadro
        svg+=f'<line id=E{i} x1={x1:.0f} y1={y1:.0f} x2={x2:.0f} y2={y2:.0f} stroke="#0B1530" stroke-width=7 marker-end="url(#ah)" opacity=0 />'
        lab+=f'<div id=L{i} class=abs style="left:{(x1+x2)/2-110:.0f}px;top:{(y1+y2)/2-20:.0f}px;width:220px;text-align:center;font:600 30px/1.1 Figtree;color:#0B1530;opacity:0"><span style="background:#fff;padding:2px 12px;border-radius:8px">{l}</span></div>'
    svg+='</svg>'
    bx=''
    for k,n in m['nodes'].items():
        f,bd=COL[n['c']];fs=n.get('fs',38 if n['c']!='c' else 46)
        fam="font:800 %dpx 'Bricolage Grotesque'"%fs if n['c']=='c' else "font:600 %dpx Figtree"%fs
        bx+=f'<div id={k} class=abs style="left:{n["x"]}px;top:{n["y"]}px;width:{n["w"]}px;height:{n["h"]}px;box-sizing:border-box;display:flex;align-items:center;justify-content:center;text-align:center;padding:8px 20px;border-radius:16px;background:{f};border:{5 if n["c"]=="c" else 4}px solid {bd};{fam};line-height:1.3;opacity:0;color:#0B1530">{n["t"]}</div>'
    return s+svg+lab+bx
def ease(x):
    x=max(0,min(1,x));return 1-(1-x)**3
def frames(m,steps,tot,fps=30):
    """steps: [(node, edge_index|None, t_inizio, t_fine_evidenza)] ; ritorna funzione JS per t"""
    return steps
JS="""
function R(t,steps){
 const ease=x=>{x=Math.max(0,Math.min(1,x));return 1-Math.pow(1-x,3)};
 let cur=null;
 for(const [n,e,t0,t1] of steps){
  const el=document.getElementById(n),p=ease((t-(t0-0.1))/0.45);
  el.style.opacity=p;el.style.transform='translateY('+(16*(1-p))+'px)';
  if(e!==null){const ae=document.getElementById('E'+e),al=document.getElementById('L'+e),q=ease((t-(t0-0.55))/0.45);ae.setAttribute('opacity',q);al.style.opacity=q}
  el.style.boxShadow='none';
  if(t>=t0-0.1&&t<t1)cur=el;
 }
 if(cur)cur.style.boxShadow='0 0 0 9px #FFE600, 0 10px 24px rgba(11,21,48,.18)';
}"""
def render_map(m,steps,tot,out_mp4,still=None,fps=30):
    with B() as b:
        b.pg.set_content('<!doctype html><html><head><meta charset=utf-8><style>'+BASE+'</style></head><body>'+html(m)+'</body></html>')
        b.pg.wait_for_timeout(200);b.pg.add_script_tag(content=JS)
        ff=subprocess.Popen(['ffmpeg','-v','error','-y','-f','image2pipe','-framerate',str(fps),'-i','-','-c:v','libx264','-preset','veryfast','-crf','17','-pix_fmt','yuv420p',out_mp4],stdin=subprocess.PIPE)
        for i in range(int(tot*fps)):
            b.pg.evaluate(f'R({i/fps},{json.dumps(steps)})');ff.stdin.write(b.pg.screenshot(type='jpeg',quality=95))
        if still:
            b.pg.evaluate(f'R({tot},{json.dumps(steps)})');b.pg.screenshot(path=still)
        ff.stdin.close();ff.wait()
def schedule(m,voci,dur,lead=1.0,gap=0.6,tail=4.0):
    """voci: lista di (nome_voce,[(nodo,arco|None),...]). dur: nome->secondi. Ritorna (steps, tot, tempi_voci)"""
    t=lead;steps=[];vt=[]
    for nome,items in voci:
        d=dur[nome];vt.append((nome,round(t,3),d))
        n=len(items)
        for j,(nodo,arco) in enumerate(items):
            t0=t+d*j/n+(0.15 if j==0 else 0)
            t1=t+d*(j+1)/n if j<n-1 else t+d+0.35
            steps.append([nodo,arco,round(t0,3),round(t1,3)])
        t+=d+gap
    return steps,round(t-gap+tail,3),vt
MAPPE={
1:{'domanda':'Quali fenomeni politici caratterizzano gli anni Settanta?',
 'nodes':{'C':dict(c='c',t='IL CLIMA POLITICO ITALIANO',x=560,y=200,w=800,h=100),
  'N68':dict(c='d',t='1968',x=170,y=400,w=420,h=96),'CG':dict(c='k',t='la contestazione giovanile',x=170,y=585,w=420,h=110),'MO':dict(c='s',t='la mobilitazione operaia',x=170,y=785,w=420,h=110),
  'N70':dict(c='d',t='anni Settanta',x=1010,y=400,w=420,h=96),'OT':dict(c='k',t="l'offensiva terrorista",x=970,y=575,w=500,h=100),
  'DX':dict(c='k',t='destra',x=770,y=755,w=300,h=90),'SX':dict(c='k',t='sinistra',x=1370,y=755,w=300,h=90),
  'AD':dict(c='e',t='attentati dinamitardi',x=700,y=915,w=440,h=96),'AS':dict(c='e',t='attentati e sequestri',x=1300,y=915,w=440,h=96)},
 'edges':[('C','N68','nel'),('N68','CG','vede'),('CG','MO','seguita da'),('C','N70','negli'),('N70','OT','vede'),('OT','DX','di'),('OT','SX','di'),('DX','AD','con'),('SX','AS','con')],
 'voci':[('MP1_0',[('C',None)]),('MP1_1',[('N68',0),('CG',1)]),('MP1_2',[('MO',2)]),('MP1_3',[('N70',3),('OT',4)]),('MP1_4',[('DX',5),('AD',7)]),('MP1_5',[('SX',6),('AS',8)])]},
2:{'domanda':'Come viene affrontata l\'emergenza degli «anni di piombo»?',
 'nodes':{'C':dict(c='c',t='LA SITUAZIONE POLITICA DEL PAESE',x=480,y=230,w=960,h=100),
  'BE':dict(c='k',t='Berlinguer',x=200,y=470,w=500,h=100),'CS':dict(c='e',t='un «compromesso storico»',x=160,y=700,w=580,h=110),
  'DC':dict(c='k',t='la Democrazia cristiana',x=1160,y=470,w=560,h=100),'GS':dict(c='e',t='un «governo di solidarietà nazionale»',x=1140,y=690,w=600,h=130),'BR':dict(c='s',t='le Brigate rosse rapiscono e uccidono Moro',x=1140,y=900,w=600,h=130)},
 'edges':[('C','BE','spinge'),('BE','CS','a proporre'),('C','DC','spinge'),('DC','GS','a proporre'),('GS','BR','ma')],
 'voci':[('MP2_0',[('C',None)]),('MP2_1',[('BE',0),('CS',1)]),('MP2_2',[('DC',2),('GS',3)]),('MP2_3',[('BR',4)])]},
3:{'domanda':'Come cambia il quadro politico negli anni Novanta?',
 'nodes':{'C':dict(c='c',t='NEGLI ANNI NOVANTA',x=610,y=210,w=700,h=100),
  'PC':dict(c='k',t='Partito comunista',x=80,y=470,w=520,h=100),'PD':dict(c='s',t='Partito democratico della sinistra',x=80,y=700,w=520,h=120),
  'DC':dict(c='k',t='Democrazia cristiana',x=700,y=470,w=520,h=100),'RU':dict(c='s',t='il ruolo di garante della posizione internazionale del paese',x=670,y=700,w=580,h=190,fs=36),
  'IN':dict(c='d',t='inchiesta giudiziaria (1992)',x=1320,y=470,w=520,h=100),'SC':dict(c='s',t='uno scandalo che travolge la DC, cioè Democrazia Cristiana, e i suoi alleati',x=1280,y=700,w=580,h=230,fs=35)},
 'edges':[('C','PC','il'),('PC','PD','diventa'),('C','DC','la'),('DC','RU','perde'),('C','IN','una'),('IN','SC','causa')],
 'voci':[('MP3_0',[('C',None)]),('MP3_1',[('PC',0),('PD',1)]),('MP3_2',[('DC',2),('RU',3)]),('MP3_3',[('IN',4),('SC',5)])]}}
