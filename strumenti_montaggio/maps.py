from lib import *
from slides import CSS as SCSS
from kore import *
from edl import fr
COL={'pesca':('#FFDCC6','#C2410C','concetto centrale'),'cel':('#DCEEFB','#1D4ED8','date e sequenze'),'pag':('#FFF3BF','#A16207','parole chiave'),
     'men':('#DDF3E4','#15803D','esempi e opere'),'lil':('#EBE3F7','#6D28D9','conseguenze')}
MCSS='''
#k{position:absolute;left:80px;top:30px;font:700 22px Fig;letter-spacing:.14em;color:#2060AF}
#q{position:absolute;left:80px;top:90px;font:800 44px/1.1 Bri;color:#0B1530;width:1760px}
#leg{position:absolute;right:60px;top:28px;display:flex;gap:16px;font:600 19px Fig;color:#0B1530}
#leg span{display:flex;align-items:center;gap:7px}#leg i{display:inline-block;width:24px;height:17px;border-radius:4px;border:3px solid}
#line{position:absolute;left:60px;right:60px;top:76px;height:2px;background:#CBD5E1}
#note{position:absolute;left:60px;top:1024px;font:600 26px Fig;color:#0B1530}
#f{position:absolute;right:60px;top:1030px;font:700 20px Fig;color:#2060AF;letter-spacing:.12em}
.b{position:absolute;display:flex;align-items:center;justify-content:center;text-align:center;padding:10px 24px;border-radius:16px;font:600 36px/1.4 Fig;color:#0B1530;opacity:0;overflow:hidden}
.b.big{font:800 50px/1.2 Bri;border-radius:18px}
.hl{box-shadow:0 0 0 9px #FFE600,0 10px 24px rgba(11,21,48,.18)}
'''
def box_style(c): bg,bd,_=COL[c];return f'background:{bg};border:5px solid {bd};'
def map_html(kick,boxes,arrows,note='',q=''):
    """boxes: {id:(col,x,y,w,h,testo,big)}"""
    h=[f'<!doctype html><meta charset=utf-8><style>{BASE}{MCSS}</style><body>']
    h.append(f'<div id=k>{esc(kick)}</div><div id=q>{esc(q)}</div><div id=leg>'+''.join(f'<span><i style="background:{bg};border-color:{bd}"></i>{lab}</span>' for bg,bd,lab in COL.values())+'</div><div id=line></div>')
    h.append(f'<div id=note>{esc(note)}</div><div id=f>STORIA V</div>')
    h.append('<svg width=1920 height=1080 style="position:absolute;left:0;top:0"><defs><marker id=ah markerUnits=userSpaceOnUse markerWidth=40 markerHeight=40 refX=20 refY=20 orient=auto><path d="M0,4 L36,20 L0,36 z" fill="#0B1530"/></marker></defs>')
    def edge(b,tx,ty):
        c,x,y,w,hh=b[:5];cx=x+w/2;cy=y+hh/2;dx=tx-cx;dy=ty-cy
        s=min((w/2+10)/abs(dx) if dx else 1e9,(hh/2+10)/abs(dy) if dy else 1e9);return cx+dx*s,cy+dy*s
    for i,(a,b) in enumerate(arrows):
        A=boxes[a];Bq=boxes[b]
        ax,ay=A[1]+A[3]/2,A[2]+A[4]/2;bx,by=Bq[1]+Bq[3]/2,Bq[2]+Bq[4]/2
        x1,y1=edge(A,bx,by);x2,y2=edge(Bq,ax,ay)
        h.append(f'<line id="AR{a}_{b}" x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="#0B1530" stroke-width="10" marker-end="url(#ah)" opacity="0"/>')
    h.append('</svg>')
    for k,(c,x,y,w,hh,t,big) in boxes.items():
        h.append(f'<div class="b{" big" if big else ""}" id="{k}" style="left:{x}px;top:{y}px;width:{w}px;height:{hh}px;{box_style(c)}">{esc(t)}</div>')
    h.append('''<script>function ease(x){x=Math.max(0,Math.min(1,x));return 1-Math.pow(1-x,3)}
window.STEPS=[];function setSteps(s){window.STEPS=s}
function render(t){var sig='';var cur=null;
 document.querySelectorAll('line').forEach(function(l){l.setAttribute('opacity',0)});
 STEPS.forEach(function(st){var b=document.getElementById(st[0]);
  (st[1]||[]).forEach(function(a){var l=document.getElementById('AR'+a);if(l){var p=ease((t-(st[2]-0.7))/0.5);l.setAttribute('opacity',Math.max(+l.getAttribute('opacity'),p).toFixed(2))}});
  var p=ease((t-st[2]+0.15)/0.45);b.style.opacity=p.toFixed(2);b.style.transform='translateY('+(18*(1-p)).toFixed(0)+'px)';
  b.classList.remove('hl');if(t>=st[2]-0.15&&t<st[2]+st[3]+0.35)cur=b;});
 if(cur)cur.classList.add('hl');
 document.querySelectorAll('.b').forEach(function(e){sig+=e.style.opacity+(e.classList.contains('hl')?'h':'')});
 document.querySelectorAll('line').forEach(function(l){sig+=l.getAttribute('opacity')});
 return sig;}</script></body>''')
    return ''.join(h)
def build_map(rend,spec,out_mp4,out_png,pg_note=None):
    """spec: dict(kick, boxes, arrows, steps=[(voce,[box ids],[arrow ids])], note)
       ritorna durata, e scrive mp4 (video+audio, mkv)"""
    steps=[];t=0.6;specs=[]
    for voc,bxs,arrs in spec['steps']:
        p,d,txt,isreal=voce(voc)
        if arrs: t+=0.6
        for k,bid in enumerate(bxs):
            steps.append([bid,[f'{a}_{b}' for a,b in arrs] if k==0 else [],round(t,3),d])
        specs.append((p,t,0));t+=d+0.7
    tot=fr(t+4.0-0.7)
    chime=f'{W}/voc/chime.wav'
    if not os.path.exists(chime): sh(['ffmpeg','-v','error','-y','-f','lavfi','-i',"aevalsrc='0.28*(sin(2*PI*880*t)+0.6*sin(2*PI*1320*t))*exp(-0.6*t)':d=4.2:s=48000",'-ar','48000','-ac','2',chime])
    specs.append((chime,t-0.7+0.15,-8))
    html_=map_html(spec['kick'],spec['boxes'],spec['arrows'],spec.get('note',''),spec.get('q',''))
    rend.load(html_)
    rend.pg.evaluate(f'setSteps({json.dumps(steps)})')
    if out_png:
        rend.pg.evaluate(f'render({tot})');rend.shot(out_png)
    if out_mp4:
        import subprocess
        v=out_mp4+'.v.mp4'
        cmd=['ffmpeg','-v','error','-y','-f','image2pipe','-framerate','30','-i','-','-c:v','libx264','-preset','veryfast','-crf','14','-pix_fmt','yuv420p','-r','30',v]
        ff=subprocess.Popen(cmd,stdin=subprocess.PIPE);n=int(round(tot*30));last=None;buf=None
        for i in range(n):
            sig=rend.pg.evaluate(f'render({i/30})')
            if sig!=last or buf is None: buf=rend.pg.screenshot(type='jpeg',quality=94);last=sig
            ff.stdin.write(buf)
        ff.stdin.close();ff.wait()
        a=out_mp4+'.a.wav';mix(specs,tot,a)
        mux(v,a,out_mp4,tot);os.remove(v);os.remove(a)
    return tot,steps
# ---------------- le mappe ----------------
def B(c,x,y,w,h,t,big=False): return (c,x,y,w,h,t,big)
MAPS={
 'M1':dict(kick="MAPPA",q="Come cambiano gli USA dopo l'attentato dell'11 settembre 2001?",
   boxes={'B1':B('pesca',60,190,860,240,"Gli USA dopo l'attentato dell'11 settembre 2001",True),'B2':B('cel',1100,215,700,190,"Guerra in Iraq 2003"),
          'B3':B('cel',60,500,860,210,"Crisi economica 2007-2008 diventata poi mondiale"),'B4':B('cel',1100,490,700,250,"2008 · Barack Obama primo presidente afro-americano"),
          'B5':B('lil',60,790,900,210,"Le riforme sociali di Obama non bastano a risollevare l'economia USA: avanzano i conservatori"),
          'B6':B('lil',1100,790,760,220,"Donald Trump diventa presidente nel 2016 fino al 2020; poi ancora nel 2024. Protezionismo, lotta all'immigrazione, populismo")},
   arrows=[('B1','B2'),('B1','B3'),('B3','B4'),('B3','B5'),('B4','B5'),('B5','B6')],note="USA = Stati Uniti d'America",
   steps=[('MA1_0',['B1'],[]),('MA1_1',['B2'],[('B1','B2')]),('MA1_2',['B3'],[('B1','B3')]),('MB1_1',['B4'],[('B3','B4')]),('MB1_2',['B5'],[('B3','B5'),('B4','B5')]),('MB1_3',['B6'],[('B5','B6')])]),
 'M2':dict(kick="MAPPA",q="Quali sono i nuovi Stati emergenti a partire dal 2000?",
   boxes={'T':B('pesca',460,160,1000,160,"Nuovi Stati emergenti a partire dal 2000: i BRICS",True),
          'P1':B('men',420,360,420,95,"Brasile"),'P2':B('men',420,485,420,95,"Russia"),'P3':B('men',420,630,420,95,"India"),
          'P4':B('men',420,755,420,95,"Cina"),'P5':B('men',420,890,420,95,"Sudafrica"),
          'K2':B('pag',930,480,420,105,"Molto aggressiva"),'K3':B('cel',930,610,420,105,"Guerra in Ucraina 2022"),'K4':B('pag',930,750,520,105,"Superpotenza economica")},
   arrows=[('T','P1'),('P2','K2'),('K2','K3'),('P4','K4')],note="BRICS = Brasile, Russia, India, Cina, Sudafrica",
   steps=[('MA2_0',['T'],[]),('MA2_1',['P1'],[('T','P1')]),('MA2_2',['P2','K2'],[('P2','K2')]),('MA2_3',['K3'],[('K2','K3')]),('MA2_4',['P3'],[]),('MA2_5',['P4','K4'],[('P4','K4')]),('MA2_6',['P5'],[])]),
 'M3':dict(kick="MAPPA",q="Che cosa accade in Medio Oriente e Nord Africa?",
   boxes={'B1':B('pesca',620,160,680,170,"Medio Oriente e Nord Africa",True),'B2':B('pag',60,440,520,250,"Conflitto arabo-israeliano ancora in corso"),
          'B3':B('cel',700,450,520,170,"Primavere arabe 2011"),'B4':B('lil',600,690,720,300,"Cadono i regimi in: Tunisia, Egitto, Libia, Siria"),
          'B5':B('lil',1340,450,520,270,"Si costituisce l'ISIS fra Siria e Libia")},
   arrows=[('B1','B2'),('B1','B3'),('B1','B5'),('B3','B4')],note="ISIS = Stato Islamico",
   steps=[('MA3_0',['B1'],[]),('MA3_1',['B2'],[('B1','B2')]),('MA3_2',['B3'],[('B1','B3')]),('MA3_3',['B4'],[('B3','B4')]),('MA3_4',['B5'],[('B1','B5')])]),
 'M4A':dict(kick="MAPPA · 1 di 2",q="Come l'Europa e l'Italia affrontano la crisi del 2008?",
   boxes={'B1':B('pesca',520,170,880,190,"L'Europa e l'Italia nel periodo della crisi 2008",True),'B2':B('cel',620,430,680,150,"Crisi del debito sovrano"),
          'B3':B('lil',60,680,840,250,"Aumentano euroscetticismo e populismo · Brexit caso esemplare"),'B4':B('men',1000,660,860,300,"Paesi in difficoltà maggiore: Irlanda, Grecia, Spagna, Portogallo, Italia")},
   arrows=[('B1','B2'),('B2','B3'),('B2','B4')],note="Brexit = uscita del Regno Unito dall'Unione Europea",
   steps=[('MA4_0',['B1'],[]),('MA4_1',['B2'],[('B1','B2')]),('MA4_2',['B4'],[('B2','B4')]),('MA4_3',['B3'],[('B2','B3')])]),
 'M4B':dict(kick="MAPPA · 2 di 2",q="Come l'Europa e l'Italia affrontano la crisi del 2008?",
   boxes={'B4':B('men',60,180,880,230,"Paesi in difficoltà maggiore: Irlanda, Grecia, Spagna, Portogallo, Italia"),
          'B5':B('cel',640,470,1200,200,"Servono governi stabili; il IV governo Berlusconi cade nel 2011 e arriva il governo tecnico di Monti"),
          'B6':B('lil',60,730,780,250,"In Italia il Movimento 5 Stelle raccoglie il dissenso contro la politica e l'austerità"),
          'B7':B('cel',940,770,360,190,"Vittoria parziale 2018"),'B8':B('cel',1380,750,480,230,"Durante Covid Draghi guida governo tecnico")},
   arrows=[('B4','B5'),('B5','B6'),('B6','B7'),('B7','B8')],note="Covid = malattia da coronavirus, la pandemia del 2020",
   steps=[('MB4_0',['B4'],[]),('MB4_1',['B5'],[('B4','B5')]),('MB4_2',['B6'],[('B5','B6')]),('MB4_3',['B7'],[('B6','B7')]),('MB4_4',['B8'],[('B7','B8')])]),
}
