# -*- coding: utf-8 -*-
# Mappe del prof (Storia V lez17) ridisegnate nel modello BES. Stesse parole, stessa struttura.
import json, os, sys, subprocess
CHROME='/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell'
COL={'c':('#FFDCC6','#C2410C'),'d':('#DCEEFB','#1D4ED8'),'k':('#FFF3BF','#A16207'),'e':('#DDF3E4','#15803D'),'s':('#EBE3F7','#6D28D9')}
# box: id, text, color, x,y,w,h, size
def B(i,t,c,x,y,w,h,s=36): return dict(id=i,t=t,c=c,x=x,y=y,w=w,h=h,s=s)
# arrow: id, points, label, (lx,ly)
def A(i,pts,lab=None,lp=None): return dict(id=i,pts=pts,lab=lab,lp=lp)
MAPS={
1:dict(q="Quali sono le cause e le conseguenze della crisi degli anni Settanta?",
 boxes=[B('b1',"LA GUERRA DEL KIPPUR (1973)",'c',560,190,800,100,46),
        B('b2',"Egitto e Siria",'k',130,430,540,120),B('b3',"Israele",'k',130,660,540,120),
        B('b4',"l'aumento del prezzo del petrolio",'s',900,430,640,130),
        B('b5',"calo della produzione",'s',1100,620,700,100),B('b6',"disoccupazione",'s',1100,750,700,100),B('b7',"inflazione",'s',1100,880,700,100)],
 arrows=[A('a1',[(760,290),(760,345),(400,345),(400,428)],"viene combattuta da",(580,345)),A('a2',[(400,550),(400,658)],"contro",(400,604)),
         A('a3',[(1220,290),(1220,428)],"causa",(1220,360)),
         A('a4',[(1000,560),(1000,670),(1098,670)],"che causa",(1000,600)),A('a5',[(1000,670),(1000,800),(1098,800)]),A('a6',[(1000,800),(1000,930),(1098,930)])],
 steps=[('b1',None,"Ecco la mappa. La guerra del Kippur, millenovecentosettantatré,"),('b2','a1',"viene combattuta da Egitto e Siria"),('b3','a2',"contro Israele."),
        ('b4','a3',"La guerra del Kippur causa l'aumento del prezzo del petrolio,"),('b5','a4',"che causa il calo della produzione,"),('b6','a5',"la disoccupazione"),('b7','a6',"e l'inflazione.")],
 voce="Quali sono le cause e le conseguenze della crisi degli anni Settanta? Ecco la mappa. La guerra del Kippur, millenovecentosettantatré, viene combattuta da Egitto e Siria contro Israele. La guerra del Kippur causa l'aumento del prezzo del petrolio, che causa il calo della produzione, la disoccupazione e l'inflazione.",
 nota=""),
2:dict(q="Quale risposta offre alla crisi il neoliberismo?",
 boxes=[B('b1',"IL NEOLIBERISMO",'c',710,190,500,100,46),
        B('b2',"l'intervento dello Stato in economia",'k',60,450,540,140),B('b3',"«meno Stato, più mercato»",'k',60,700,540,140),
        B('b4',"l'affidamento dei servizi ai privati",'k',690,450,540,140),B('b5',"la riduzione delle tasse",'k',690,700,540,140),
        B('b6',"Reagan negli USA (1981-1988)",'e',1430,450,430,170),B('b7',"Thatcher nel Regno Unito (1979-1990)",'e',1430,690,430,170)],
 arrows=[A('a1',[(960,290),(960,340),(330,340),(330,448)],"critica",(330,395)),A('a2',[(330,590),(330,698)],"e sostiene",(330,644)),
         A('a3',[(960,290),(960,340),(960,448)],"pratica",(960,395)),A('a4',[(960,590),(960,698)],"e promette",(960,644)),
         A('a5',[(960,290),(960,340),(1330,340),(1330,535),(1428,535)],"viene messo in atto da",(1330,400)),A('a6',[(1330,535),(1330,775),(1428,775)])],
 steps=[('b1',None,"Ecco la mappa. Il neoliberismo"),('b2','a1',"critica l'intervento dello Stato in economia"),('b3','a2',"e sostiene: meno Stato, più mercato."),
        ('b4','a3',"Pratica l'affidamento dei servizi ai privati"),('b5','a4',"e promette la riduzione delle tasse."),('b6','a5',"Viene messo in atto da Reagan negli Stati Uniti, dal millenovecentottantuno al millenovecentottantotto,"),('b7','a6',"e da Thatcher nel Regno Unito, dal millenovecentosettantanove al millenovecentonovanta.")],
 voce="Quale risposta offre alla crisi il neoliberismo? Ecco la mappa. Il neoliberismo critica l'intervento dello Stato in economia e sostiene: meno Stato, più mercato. Pratica l'affidamento dei servizi ai privati e promette la riduzione delle tasse. Viene messo in atto da Reagan negli Stati Uniti, dal millenovecentottantuno al millenovecentottantotto, e da Thatcher nel Regno Unito, dal millenovecentosettantanove al millenovecentonovanta.",
 nota="USA = Stati Uniti d'America"),
3:dict(q="Come si arriva alla fine dell'Unione Sovietica?",
 boxes=[B('b1',"MICHAIL GORBAČËV (1985)",'c',540,180,840,90,44),
        B('b2',"riforme",'s',60,400,540,130),B('b3',"trasparenza",'k',190,590,410,100),B('b4',"ristrutturazione",'k',190,720,410,100),
        B('b5',"l'autonomia dei paesi dell'Est europeo",'k',690,400,540,130),B('b6',"il socialismo cade (1989)",'d',690,620,540,120),B('b7',"il muro di Berlino (9 novembre 1989)",'d',690,820,540,140),
        B('b8',"un tentativo di colpo di Stato (1991)",'d',1320,400,540,130),B('b9',"la separazione di molti Stati dell'Unione",'k',1320,620,540,120),B('b10',"dissoluzione dell'Unione Sovietica (dicembre 1991)",'d',1320,820,540,140)],
 arrows=[A('a1',[(960,270),(960,310),(330,310),(330,398)],"introduce",(330,355)),A('a2',[(960,270),(960,398)],"riconosce",(960,355)),A('a3',[(960,270),(960,310),(1590,310),(1590,398)],"subisce",(1590,355)),
         A('a4',[(110,530),(110,640),(188,640)],"basate su",(110,562)),A('a5',[(110,640),(110,770),(188,770)]),
         A('a6',[(960,530),(960,618)],"dove",(960,560)),A('a7',[(960,740),(960,818)],"e viene aperto",(960,768)),
         A('a8',[(1590,530),(1590,618)],"e",(1590,560)),A('a9',[(1590,740),(1590,818)],"fino alla",(1590,768))],
 steps=[('b1',None,"Ecco la mappa. Michail Gorbačëv, millenovecentottantacinque,"),('b2','a1',"introduce riforme"),('b3','a4',"basate su trasparenza"),('b4','a5',"e ristrutturazione."),
        ('b5','a2',"Riconosce l'autonomia dei paesi dell'Est europeo,"),('b6','a6',"dove il socialismo cade nel millenovecentottantanove"),('b7','a7',"e viene aperto il muro di Berlino, il nove novembre millenovecentottantanove."),
        ('b8','a3',"Subisce un tentativo di colpo di Stato, nel millenovecentonovantuno,"),('b9','a8',"e la separazione di molti Stati dell'Unione,"),('b10','a9',"fino alla dissoluzione dell'Unione Sovietica, a dicembre del millenovecentonovantuno.")],
 voce="Come si arriva alla fine dell'Unione Sovietica? Ecco la mappa. Michail Gorbačëv, millenovecentottantacinque, introduce riforme basate su trasparenza e ristrutturazione. Riconosce l'autonomia dei paesi dell'Est europeo, dove il socialismo cade nel millenovecentottantanove e viene aperto il muro di Berlino, il nove novembre millenovecentottantanove. Subisce un tentativo di colpo di Stato, nel millenovecentonovantuno, e la separazione di molti Stati dell'Unione, fino alla dissoluzione dell'Unione Sovietica, a dicembre del millenovecentonovantuno.",
 nota="")
}
def html(k,materia="STORIA V"):
    M=MAPS[k];h=["<!doctype html><html><head><meta charset=utf-8><style>"]
    h.append("""@font-face{font-family:Fig;src:url(file:///root/.fonts/Figtree-SemiBold.ttf)}@font-face{font-family:FigB;src:url(file:///root/.fonts/Figtree-Bold.ttf)}@font-face{font-family:Bri;src:url(file:///root/.fonts/BricolageGrotesque-ExtraBold.ttf)}
html,body{margin:0;width:1920px;height:1080px;background:#fff;overflow:hidden}
#k{position:absolute;left:60px;top:30px;font:700 24px FigB;letter-spacing:.14em;color:#2060AF}
#q{position:absolute;left:60px;top:84px;font:800 44px Bri;color:#2060AF;width:1800px;line-height:1.1}
#f{position:absolute;left:60px;bottom:22px;font:700 22px FigB;color:#2060AF;letter-spacing:.06em}
#n{position:absolute;right:60px;bottom:22px;font:600 26px Fig;color:#0B1530}
#leg{position:absolute;right:60px;top:26px;display:flex;gap:16px;font:600 20px Fig;color:#0B1530}
#leg span{display:flex;align-items:center;gap:7px}#leg i{display:inline-block;width:24px;height:18px;border-radius:4px;border:3px solid}
.b{position:absolute;box-sizing:border-box;display:flex;align-items:center;justify-content:center;text-align:center;padding:8px 18px;border-radius:16px;font-family:Fig;line-height:1.3;color:#0B1530;opacity:0;font-weight:600}
.lab{position:absolute;transform:translate(-50%,-50%);background:#fff;padding:2px 12px;font:600 30px Fig;color:#0B1530;opacity:0;white-space:nowrap}
.hl{box-shadow:0 0 0 9px #FFE600,0 10px 24px rgba(11,21,48,.18)}
svg{position:absolute;left:0;top:0}svg path{fill:none;stroke:#0B1530;stroke-width:6;stroke-linejoin:round}
""")
    for c,(bg,bd) in COL.items(): h.append(f".{c}{{background:{bg};border:5px solid {bd}}}")
    h.append("</style></head><body><div id=k>MAPPA CONCETTUALE · "+materia+"</div>")
    h.append("<div id=leg>"+"".join(f"<span><i style='background:{COL[c][0]};border-color:{COL[c][1]}'></i>{n}</span>" for c,n in [('c','concetto centrale'),('d','date e sequenze'),('k','parole chiave'),('e','esempi e opere'),('s','conseguenze')])+"</div>")
    h.append(f"<div id=q>{M['q']}</div>")
    h.append("<svg width=1920 height=1080><defs><marker id=ah markerUnits=userSpaceOnUse markerWidth=34 markerHeight=34 refX=30 refY=17 orient=auto><path d='M3,3 L31,17 L3,31 z' style='fill:#0B1530;stroke:none'/></marker></defs>")
    for a in M['arrows']:
        d="M"+" L".join(f"{x},{y}" for x,y in a['pts'])
        h.append(f"<path id={a['id']} d='{d}' marker-end='url(#ah)' style='opacity:0'/>")
    h.append("</svg>")
    for a in M['arrows']:
        if a['lab']: h.append(f"<div class=lab id=L_{a['id']} style='left:{a['lp'][0]}px;top:{a['lp'][1]}px'>{a['lab']}</div>")
    for b in M['boxes']:
        f="Bri" if b['s']>=46 else "Fig"
        h.append(f"<div class='b {b['c']}' id={b['id']} style='left:{b['x']}px;top:{b['y']}px;width:{b['w']}px;height:{b['h']}px;font-size:{b['s']}px;font-family:{f};{'font-weight:800;letter-spacing:.04em' if b['s']>=46 else ''}'>{b['t']}</div>")
    h.append(f"<div id=f>{materia}</div><div id=n>{M['nota']}</div>")
    h.append("""<script>
function ease(x){x=Math.max(0,Math.min(1,x));return 1-Math.pow(1-x,3)}
window.ST=[];function setSteps(s){window.ST=s}
function state(k){
 document.querySelectorAll('path[id^=a]').forEach(e=>e.style.opacity=0);
 document.querySelectorAll('.lab').forEach(e=>e.style.opacity=0);
 document.querySelectorAll('.b').forEach(e=>{e.style.opacity=0;e.style.transform='none';e.classList.remove('hl')});
 ST.forEach(([b,a,st,du],i)=>{ if(i<=k){document.getElementById(b).style.opacity=1; if(a){document.getElementById(a).style.opacity=1;const l=document.getElementById('L_'+a);if(l)l.style.opacity=1}
   if(i==k&&k<ST.length)document.getElementById(b).classList.add('hl')}});
 if(k>=ST.length){document.querySelectorAll('path[id^=a]').forEach(e=>e.style.opacity=1);document.querySelectorAll('.lab').forEach(e=>e.style.opacity=1);document.querySelectorAll('.b').forEach(e=>{e.style.opacity=1;e.classList.remove('hl')})}
}
function render(t,all){
 document.querySelectorAll('path[id^=a]').forEach(e=>e.style.opacity=all?1:0);
 document.querySelectorAll('.lab').forEach(e=>e.style.opacity=all?1:0);
 document.querySelectorAll('.b').forEach(e=>{e.style.opacity=all?1:0;e.style.transform='none';e.classList.remove('hl')});
 if(all)return;let cur=null;
 for(const [b,a,st,du] of ST){const e=document.getElementById(b);
  if(a){const p=ease((t-(st-0.55))/0.45);document.getElementById(a).style.opacity=p;const l=document.getElementById('L_'+a);if(l)l.style.opacity=p}
  const p=ease((t-st+0.15)/0.45);e.style.opacity=p;e.style.transform='translateY('+(18*(1-p))+'px)';
  if(t>=st-0.15&&t<st+du+0.25)cur=e}
 if(cur)cur.classList.add('hl')}
</script></body></html>""")
    return "".join(h)
def timing(k,dur,lead=0.8):
    """tempi dei passi: proporzionali ai caratteri dei segmenti; la voce comincia a 'lead'. (q = domanda iniziale letta prima del primo passo)"""
    M=MAPS[k]; voce=M['voce']; q=M['q']; tot=len(voce); t=lambda ch: lead+dur*ch/tot
    pos=len(q)+1; out=[]
    for b,a,seg in M['steps']:
        out.append([b,a,round(t(pos),3),round(dur*len(seg)/tot,3)]); pos+=len(seg)+1
    return out
if __name__=='__main__':
    from playwright.sync_api import sync_playwright
    os.makedirs('/home/work/build/mappe',exist_ok=True)
    with sync_playwright() as p:
        br=p.chromium.launch(executable_path=CHROME,args=['--allow-file-access-from-files','--no-sandbox']); pg=br.new_page(viewport={'width':1920,'height':1080})
        for k in MAPS:
            f=f'/home/work/build/mappe/m{k}.html';open(f,'w').write(html(k));pg.goto('file://'+f);pg.wait_for_timeout(400)
            pg.evaluate("render(0,true)");pg.screenshot(path=f'/home/work/build/mappe/m{k}_finale.png')
        br.close()
