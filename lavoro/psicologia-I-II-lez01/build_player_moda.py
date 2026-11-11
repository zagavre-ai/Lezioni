# Lettore interattivo per Tecnologie Lez1 · Parte 1 / Parte 2 (soglia 80%)
import re,json,sys,os,shutil
sys.path.insert(0,'/home/claude/lezioni/psicologia-I-II-lez01')
import struttura as S
part=int(sys.argv[1]);D='/home/claude/lezioni/psicologia-I-II-lez01/'
OUT=D+f'consegna/Tecnologie_Lez1_Parte{part}/Lezione_interattiva/';os.makedirs(OUT,exist_ok=True)
QS=[1,2,3,4,5] if part==1 else [6,7,8,9];QOFF=QS[0]-1
VIDEO=f'Tecnologie_Lez1_Parte{part}_VIDEO.mp4'
tl=json.load(open(D+f'timeline_P{part}.json'));T={n:s for n,s,d in tl}
stops=[round(T['Q%d'%q]+1.8,2) for q in QS]
tops=[0.0]+[round(T['T%d'%q],2) for q in QS]
# ---- esercizi: solo i quiz di questa parte, rinumerati 1..n ----
E=json.load(open(D+'es/esercizi.json'));E=[dict(e,quiz=e['quiz']-QOFF) for e in E if e['quiz'] in QS]
src=open(D+'es/Esercizi_Moda_Lez1_anteprima.html').read()
m=re.search(r"__DATA__|(\{\"E\":.*?\"Q\":\{.*?\}\})",src)
data=json.dumps({'E':E,'Q':{q-QOFF:S.ARG[q-1][1] for q in QS}},ensure_ascii=False)
i0=src.index('{"E":');depth=0
for j in range(i0,len(src)):
    if src[j]=='{':depth+=1
    elif src[j]=='}':
        depth-=1
        if depth==0:break
src=src[:i0]+data+src[j+1:]
e=src
def rep(a,b,cnt=1):
    global e
    assert e.count(a)==cnt,(e.count(a),a[:70]);e=e.replace(a,b)
B=open('/home/claude/player/build_player.py').read()
for a,b in re.findall(r"^rep\((.+?),(.+)\)$",B,re.M): pass
# riusa le sostituzioni del lettore di Spagnolo (stessa base)
code=B[B.index('e=src'):B.index("open('esercizi.html','w')")]
code=code.replace('e=src\n','')
exec(code)
rep("h.appendChild(mk('h1',null,'Quiz '+cur+' · '+esc(Q[cur])));","h.appendChild(mk('h1',null,'Quiz '+(cur+%d)+' · '+esc(Q[cur])));"%QOFF)
open(OUT+'esercizi.html','w').write(e)
# ---- index.html ----
fonts=''.join(re.findall(r'@font-face\{[^}]*\}',src));logo=re.search(r'<header><img src="([^"]+)"',src).group(1)
P=open('/home/claude/player/player_tpl.html').read()
N=len(QS)
names={i+1:S.ARG[q-1][1] for i,q in enumerate(QS)}
titles=['Introduzione' if part==1 else 'Ripasso della Parte 1']+[S.ARG[q-1][1] for q in QS]
P=P.replace("NAMES={1:'Femminile',2:'Plurale',3:'Interrogativos',4:'Pronombres sujeto',5:'SER y TENER',6:'Verbos regulares',7:'Verbos reflexivos'}","NAMES="+json.dumps(names,ensure_ascii=False))
P=re.sub(r"var TITLES=\[[^\]]*\];","var TITLES="+json.dumps(titles,ensure_ascii=False)+";",P)
for a,b in [('i<7;i++)if(!DONE[i+1])return i;return 7','i<NQ;i++)if(!DONE[i+1])return i;return NQ'),('return i<7?STOPS[i]','return i<NQ?STOPS[i]'),('for(var j=0;j<7;j++)','for(var j=0;j<NQ;j++)'),
            ('for(var i=0;i<7;i++){var s=STOPS[i]','for(var i=0;i<NQ;i++){var s=STOPS[i]'),('for(var q=1;q<=7;q++)','for(var q=1;q<=NQ;q++)'),('for(var i=0;i<=7;i++)','for(var i=0;i<=NQ;i++)'),
            ("(i===0?'Introducción':'Argomento '+i)","(i===0?TITLES[0]:'Argomento '+(i+QOFF))"),
            ('Spagnolo · Videolezione interattiva','Tecnologie dei materiali · Videolezione interattiva'),('<h1>¿De dónde eres?</h1>','<h1>Preparazione · parte I — Parte %d</h1>'%part),
            ('Spagnolo_Lez1_VIDEO_FINALE.mp4',VIDEO)]:
    assert a in P,a; P=P.replace(a,b)
P=P.replace('{{STOPS}}',json.dumps(stops)+',NQ=%d,QOFF=%d'%(N,QOFF))
P=P.replace('/*FONTS*/',fonts).replace('{{LOGO}}',logo).replace('{{TOPS}}',json.dumps(tops))
P=P.replace("localStorage.removeItem('telesio_sp1');localStorage.removeItem('telesio_sp2')","localStorage.removeItem('telesio_tec1')")
open(OUT+'index.html','w').write(P)
if not os.path.exists(OUT+VIDEO): os.link(D+VIDEO,OUT+VIDEO)
print('parte',part,'stops',stops,'tops',tops)
