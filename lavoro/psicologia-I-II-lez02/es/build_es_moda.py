# Esercizi interattivi Moda: domande a scelta multipla della docente (1 giusta + 5 sbagliate)
import json,base64,random,sys
sys.path.insert(0,'/home/claude/lezioni/psicologia-I-II-lez02')
import struttura as S
Z='/home/claude/l1/fz/33157a64-Bricolage_GrotesqueDM_MonoFigtree/'
def b64(p):return base64.b64encode(open(p,'rb').read()).decode()
SRC=open('/home/claude/v5/es/build_es.py').read()
FONTS=SRC[SRC.find("FONTS=''.join"):SRC.find("LOGO=")]
exec(FONTS)
LOGO=b64('/home/claude/logo/out/Telesio_logo_blu.svg')
Q=json.load(open('/home/claude/lezioni/psicologia-I-II-lez02/quiz_raw.json'))
E=[];rnd=random.Random(7)
by={}
for i,q in enumerate(Q): by.setdefault(q['quiz'],[]).append((i,q))
for k,qs in sorted(by.items()):
    items=[]
    for i,q in qs:
        opts=[q['a']]+q['w']; rnd.shuffle(opts)
        items.append({'p':'%d. %s'%(i+1,q['p']),'opts':opts,'a':q['a'],'h':'Dalla lezione: «'+q['ref']+'»'})
    E.append({'id':'Q%d'%k,'quiz':k,'title':'Domande · '+S.ARG[k-1][1],'type':'mc','items':items})
QUIZ={k:S.ARG[k-1][1] for k in by}
TPL=open('/home/claude/v5/es/player.html').read()
def rep(a,b):
    global TPL
    assert a in TPL,a[:60]; TPL=TPL.replace(a,b,1)
# punteggio massimo e tipo «mc»
rep("function maxPts(e){return e.type==='match'","function maxPts(e){return e.type==='mc'?e.items.length:e.type==='match'")
rep(" var hd=mk('div','row head');"," if(e.type==='mc'){e.items.forEach(function(it,i){var r=mk('div','row mc');r.appendChild(mk('div','p',esc(it.p)));var d=mk('div');var g='mc'+e.id+i;var rd=mk('div','rd mcl');it.opts.forEach(function(o,k){var l=document.createElement('label');var x=document.createElement('input');x.type='radio';x.name=g;x.value=o;l.appendChild(x);l.appendChild(document.createTextNode(' '+o));rd.appendChild(l)});d.appendChild(rd);var res=mk('div','res');d.appendChild(res);r.appendChild(d);el.appendChild(r);c.rows.push({row:r,rd:rd,inp:{value:'',disabled:false,tagName:'X'},res:res,i:i})});return c}\n var hd=mk('div','row head');")
rep("   if(e.type==='match'){var val=r.inp.value;","   if(e.type==='mc'){var itm=e.items[r.i];var sel=(r.rd.querySelector('input:checked')||{}).value;ok=sel===itm.a?1:0;msg=ok?itm.h:'La risposta giusta è: «'+itm.a+'». '+itm.h}\n   else if(e.type==='match'){var val=r.inp.value;")
# tastiera dei caratteri spagnoli: solo se servono campi di testo
rep(" v.appendChild(keys());"," if(ex.some(function(e){return e.type!=='mc'}))v.appendChild(keys());")
rep("'Le risposte considerate corrette sono proposte da validare dalla docente prima della consegna.'","'Domande e risposte della docente.'")
TPL=TPL.replace('Spagnolo · Esercizi','Tecnologie della moda · Esercizi').replace('Spagnolo','Tecnologie della moda')
# stile delle opzioni
rep('</style>','.row.mc{grid-template-columns:1fr!important;display:block}.row.mc>.p{font-weight:700;margin-bottom:8px}.mcl{display:flex;flex-direction:column;gap:6px}.mcl label{display:flex;gap:10px;align-items:flex-start;padding:8px 12px;border:1.5px solid #D5DCE8;border-radius:12px;cursor:pointer;line-height:1.35}.mcl label:has(input:checked){border-color:#2060AF;background:rgba(32,96,175,.07)}.mcl input{margin-top:4px;flex:none}</style>')
html=TPL.replace('/*FONTS*/',FONTS).replace('__LOGO__',LOGO).replace('__DATA__',json.dumps({'E':E,'Q':QUIZ},ensure_ascii=False))
open('/home/claude/lezioni/psicologia-I-II-lez02/es/Esercizi_Moda_Lez1_anteprima.html','w').write(html)
json.dump(E,open('/home/claude/lezioni/psicologia-I-II-lez02/es/esercizi.json','w'),ensure_ascii=False,indent=1)
print(len(E),'quiz',sum(len(e['items']) for e in E),'domande')
