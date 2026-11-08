# Slide 16:9 Telesio V4 per Tecnologie della moda – impaginazione automatica nel browser
import json,re,html,sys
sys.path.insert(0,'/home/claude/lezioni/afm-inglese-triennio-lez01')
import struttura as S
s=open('/home/claude/gen/gen.py').read()
a=s.find('CSS_FONTS="""')+len('CSS_FONTS="""'); b=s.find('"""%{')
FZ='/home/claude/l1/fz/33157a64-Bricolage_GrotesqueDM_MonoFigtree'
CSS=s[a:b]%{'z':FZ} if '%(z)s' in s[a:b] else s[a:b]
a=s.find('CSS=CSS_FONTS+"""')+len('CSS=CSS_FONTS+"""'); b=s.find('"""\ndef esc')
CSS+=s[a:b]
CSS+="""
.tt{width:68cqw!important;font-size:3.2cqw}
.bd{width:68cqw!important;top:18.6cqw!important;height:30.6cqw!important;bottom:auto!important;display:block!important;overflow:hidden}
.bd>*{margin-bottom:.75cqw}
.ey{font-family:'FG'!important;font-weight:800!important;letter-spacing:.16em!important;font-size:1.15cqw!important}
.tx p{font-size:1.6cqw;font-weight:500;line-height:1.42;margin-bottom:.55cqw;border-radius:.4cqw;padding:.05cqw .35cqw;margin-left:-.35cqw;transition:none}
.tx p.cont{margin-top:-.35cqw}
.tx p.bu.cont:before{display:none}
.tx p b{font-weight:800;color:var(--ink)}
.kw{position:absolute;left:74.4cqw;top:32.2cqw;width:21.5cqw;border-top:.25cqw solid var(--blue);padding-top:.8cqw}
.kw .l{font-family:'FG';font-weight:800;font-size:.95cqw;letter-spacing:.16em;color:var(--blue);text-transform:uppercase;margin-bottom:.6cqw}
.kw .w{font-family:'FG';font-weight:700;font-size:1.3cqw;line-height:1.25;color:var(--ink);padding:.45cqw 0;border-bottom:.05cqw solid #E3E8F0}
.tbl2{display:grid;border:.07cqw solid #D5DCE8;border-radius:1cqw;overflow:hidden;box-shadow:0 .7cqw 2.2cqw rgba(11,21,48,.07);font-size:1.45cqw;line-height:1.38}
.tbl2 div{padding:.55cqw 1cqw;border-bottom:.06cqw solid #E3E8F0;border-right:.06cqw solid #E6EAF1;font-weight:500}
.tbl2 div.h{background:var(--ink);color:#fff;font-weight:800;font-size:1cqw;letter-spacing:.14em;text-transform:uppercase}
.tbl2 div.k{background:rgba(32,96,175,.07);color:var(--blue);font-weight:800}
.tbl2 b{font-weight:800}
.sup{display:grid;grid-template-columns:repeat(3,1fr);gap:.5cqw .9cqw;font-size:1.45cqw}
.sup div{border-radius:.5cqw;background:rgba(32,96,175,.06);padding:.35cqw .8cqw;display:flex;justify-content:space-between;font-weight:700}
.sup div span{color:var(--blue);font-weight:800}
.sup .cap{grid-column:1/4;background:none;padding:0;font-family:'FG';font-weight:800;font-size:.95cqw;letter-spacing:.16em;color:var(--blue);text-transform:uppercase}
.doc{background:#F3F5F9}
.sheet.s16{background:#F5F8FC!important}
.bd{background:#fff;border:.07cqw solid #DCE4F0;border-radius:1.1cqw;box-shadow:0 .6cqw 1.8cqw rgba(11,21,48,.06);padding:1.1cqw 1.4cqw!important;box-sizing:border-box}
.tx p{font-size:1.58cqw!important}
.tx p.lead{color:var(--blue);font-weight:800!important;font-size:1.7cqw!important;text-decoration:underline;text-decoration-color:#FFE600;text-decoration-thickness:.32cqw;text-underline-offset:.4cqw;margin-bottom:.8cqw!important}
.tx p.lead b{color:var(--blue)}
.tx p.bu{background:#F1F5FB;border:.07cqw solid #D3DDEC;border-radius:.8cqw;padding:.5cqw 1cqw .5cqw 2.1cqw!important;margin-left:0!important;position:relative}
.tx p.bu:before{left:.85cqw!important;top:1.15cqw!important}
.tx p.bu.cont{border-top:0;border-radius:0 0 .8cqw .8cqw;margin-top:-.8cqw!important}
.tx p.pl{border-left:.28cqw solid #C9D8EE;padding-left:.9cqw!important;margin-left:0!important;border-radius:0 .4cqw .4cqw 0}
.tx p.cont.pl{border-left-color:#E1E9F5}

.sp .r{text-transform:none!important;letter-spacing:0!important;font-weight:700!important;font-size:1.02cqw!important;line-height:1.25!important;white-space:normal}
.sp .r2{font-family:'FG';font-weight:800;font-size:1cqw;letter-spacing:.06em;text-transform:uppercase;margin-top:.3cqw}
.sp .n{font-size:1.12cqw!important;white-space:nowrap}
.kw{top:34.4cqw!important}

/* ---- impaginazione v3 (A+B): una card per frase, max 3 per slide, numeri chiave a lato ---- */
.bd{background:none!important;border:0!important;box-shadow:none!important;padding:0!important;overflow:visible!important}
.bd.nar{width:47cqw!important}
.tx p.pl,.tx p.bu{background:#fff!important;border:.08cqw solid #DCE3EE!important;border-radius:1.1cqw!important;padding:1cqw 1.4cqw 1cqw 5cqw!important;margin:0 0 1cqw 0!important;position:relative;box-shadow:0 .7cqw 2cqw rgba(11,21,48,.07);font-size:1.72cqw!important;line-height:1.42!important}
.tx p.pl:before,.tx p.bu:before{content:attr(data-n);position:absolute!important;left:1.25cqw!important;top:1cqw!important;width:2.6cqw;height:2.6cqw;border-radius:.75cqw;background:#EEF3FA;color:var(--blue);font:800 1.45cqw 'BG';display:flex;align-items:center;justify-content:center}
.tx p.bu:before{content:''!important;width:.95cqw;height:.95cqw;border-radius:50%;background:var(--blue);left:2.1cqw!important;top:1.75cqw!important}
.tx p.bu.cont,.tx p.cont.pl{margin-top:0!important;border-top:.08cqw solid #DCE3EE!important;border-radius:1.1cqw!important}
.tx p.lead{font-size:1.85cqw!important;margin:.2cqw 0 1cqw 0!important}
.nk{position:absolute;left:52.6cqw;top:18.6cqw;width:19.6cqw;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:1cqw}
.tx p.bu.cont:before{display:flex!important}
.nk .t{overflow:hidden;background:#fff;border-radius:1cqw;padding:1cqw 1.2cqw;box-shadow:0 .7cqw 2cqw rgba(11,21,48,.08);border:.08cqw solid #DCE3EE}
.nk .t.w2{grid-column:1/3}
.nk .v{font:800 2.9cqw/1.05 'BG';color:var(--blue);letter-spacing:-.02em;white-space:nowrap}
.nk .v.m{font-size:2.4cqw}.nk .v.l{font-size:1.9cqw}
.nk .v small{display:block;font-size:.47em;margin-top:.25cqw;letter-spacing:0}
.nk .v small.pc{display:inline;font-size:.55em}
.nk .lb{font:700 1.2cqw/1.25 'FG';color:var(--ink);margin-top:.5cqw}
.nk .cap{grid-column:1/3;font:800 .95cqw 'FG';letter-spacing:.16em;color:var(--blue);text-transform:uppercase}
"""
LG=__import__('base64').b64encode(open('/home/claude/logo/out/Telesio_logo_blu.svg','rb').read()).decode()
MAT='Inglese'
DOC='Maria Vittoria Fontanesi'
def esc(t):return html.escape(t,quote=False)
def rh(runs):return ''.join(('<b>%s</b>'%esc(t)) if b else esc(t) for b,t in runs)
def md(t):return re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',esc(t))
def unit_html(u,i):
    if u['t']=='tab':
        nc=len(u['cols']); w={4:'.55fr 1.5fr 1.2fr 1.1fr',3:'.7fr .7fr 2.2fr'}[nc]
        o='<div class="tbl2 un" data-i="%d" style="grid-template-columns:%s">'%(i,w)
        o+=''.join('<div class="h">%s</div>'%esc(c) for c in u['cols'])
        for r in u['rows']: o+=''.join('<div class="%s">%s</div>'%('k' if k==0 else '',md(c)) for k,c in enumerate(r))
        return o+'</div>'
    if u['t']=='super':
        o='<div class="sup un" data-i="%d"><div class="cap">Denominazione · diametro massimo delle fibre</div>'%i
        o+=''.join('<div>%s<span>%s</span></div>'%(esc(a),esc(b)) for a,b in u['rows'])
        return o+'</div>'
    cls={'p':'pl','li':'bu','cont':'bu cont'}[u['t']]
    if u['t']=='p' and not u.get('par0',True): cls='cont pl'
    if u['txt'].rstrip().endswith(':'): cls='lead'
    return '<p class="%s un" data-i="%d">%s</p>'%(cls,i,rh(u['runs']))
STOPW=set('di del della dello dei degli delle da dal dalla dai dalle per il lo la i gli le e a ad in con su tra fra un una uno che al alla ai alle nel nella nei nelle sul sulla circa oltre fino appena ben quasi è sono'.split())
N_=r"(\d{1,3}(?:\.\d{3})+|\d+(?:,\d+)?)"
U_=r"(?:\s?(%|percento|micron|cm|mm|kg|g|°C|gradi|anni|mesi|volte|giorni|ore)(?![\w]))?"
RNG=re.compile(r"(?:\btra|\bda|\bdal|\bdai)\s+"+N_+r"\s+(?:e|a|al|ai)\s+"+N_+U_+r"|(?<![\w/.,])"+N_+r"\s?[-–]\s?"+N_+U_)
ONE=re.compile(r"(?<![\w/.,])"+N_+U_+r"(?![\w/])")
VERB=set('è sono viene vengono presenta presentano risulta risultano rappresenta può possono ha hanno'.split())
def _lab(t,pos,bold):
    st=max([t.rfind(c,0,pos) for c in ',;:.']+[t.rfind(' mentre ',0,pos),-1])+1
    cand=[(bp,bt) for bp,bt in bold if st<=bp<pos]
    if cand:return cand[-1][1]
    cand=[(bp,bt) for bp,bt in bold if pos-90<=bp<pos]
    if cand:return cand[-1][1]
    ws=[w for w in re.findall(r"[A-Za-zÀ-ÿ']+",t[st:pos]) if w.lower() not in STOPW and w.lower() not in VERB and len(w)>3 and not w.endswith("'") and not re.search(r'(ando|endo|ato|ata|ati|ate|ito|ita|abile)$',w.lower()) and w.lower() not in ('intorno','ogni','circa','oltre','anche','pari','valore','misura')]
    return ws[-1] if ws else ''
import os as _os
NKOV=json.load(open('/home/claude/lezioni/afm-inglese-triennio-lez01/numeri_chiave.json')) if _os.path.exists('/home/claude/lezioni/afm-inglese-triennio-lez01/numeri_chiave.json') else {}
U_IDX={}
def keynums(u):
    if u['t'] not in ('p','li','cont'):return []
    t=u['txt'];out=[];used=[]
    bold=[];pos=0
    for b,x in u['runs']:
        if b and len(x.strip())>2:bold.append((pos+len(x)-len(x.lstrip()),x.strip(' ,.;:')))
        pos+=len(x)
    for m in RNG.finditer(t):
        g=[x for x in m.groups()];n1,n2,un=(g[0],g[1],g[2]) if g[0] else (g[3],g[4],g[5])
        un=(un or '').replace('percento','%')
        if not un:
            m2=re.match(r"\s*(%|micron|cm|mm|kg|g|°C|anni|mesi)\b",t[m.end():])
            if m2:un=m2.group(1)
        out.append({'v':n1+'–'+n2,'u':un,'l':_lab(t,m.start(),bold)[:32],'p':m.start()});used.append((m.start(),m.end()))
    for m in ONE.finditer(t):
        if any(a<=m.start()<b for a,b in used):continue
        n,un=m.group(1),(m.group(2) or '').replace('percento','%')
        pre=t[max(0,m.start()-6):m.start()]
        if re.search(r'n\.\s*$',pre) or t[m.end():m.end()+1]=='/':continue
        v=int(n.replace('.','').split(',')[0])
        if 1800<=v<=2100 and not un:continue
        if not un and v<=10:continue
        out.append({'v':n,'u':un,'l':_lab(t,m.start(),bold)[:32],'p':m.start()})
    out.sort(key=lambda x:x['p'])
    for k in range(1,len(out)):
        if not out[k]['l']:out[k]['l']=out[k-1]['l']
    OV=NKOV.get(str(U_IDX.get(id(u),-1)))
    if OV is not None:return [{'v':a,'u':b,'l':c} for a,b,c in OV]
    if len(out)>4:return []
    return out
def build(path='/home/claude/lezioni/afm-inglese-triennio-lez01/slides.html',keep=None):
    U=S.units()
    for i in range(len(U)-1):
        if U[i].get('txt','').rstrip().endswith(':') and U[i+1]['s']!=U[i]['s']: U[i]['s']=U[i+1]['s'];U[i]['a']=U[i+1]['a']
    DATA=[]
    for i,u in enumerate(U):U_IDX[id(u)]=i
    for i,u in enumerate(U):
        if keep is not None and i not in keep: continue
        bold=[t.strip(' ,.;:') for b,t in u.get('runs',[]) if b and 3<len(t.strip())<38]
        DATA.append({'id':i,'a':u['a'],'s':u['s'],'h':unit_html(u,i),'kw':bold,'big':u['t'] in('tab','super'),'lead':u.get('txt','').rstrip().endswith(':'),'li':u['t'] in ('li','cont'),'nk':keynums(u)})
    page="""<!doctype html><html><head><meta charset="utf-8"><style>%s
body{margin:0}.sheet{margin:0 0 20px 0}</style></head><body><div id="root"></div>
<script>
const D=%s,ARG=%s,SUB=%s,LG='%s',MAT=%s,DOC=%s;
function shell(n,a,s){const d=document.createElement('div');d.className='sheet s16';
 d.innerHTML='<div class="hd"><img src="data:image/svg+xml;base64,'+LG+'"></div>'
 +'<div class="ey">'+String(a+1).padStart(2,'0')+' · '+ARG[a]+'</div><div class="tt">'+SUB[s]+'</div><div class="bar"></div>'
 +'<div class="bd tx"></div><div class="doc"></div><div class="sp"><div class="n">Prof.ssa '+DOC+'</div><div class="r">Inglese</div><div class="r2">Triennio Amministrazione, Finanza e Marketing</div></div>'
 +'<div class="nk"></div><div class="kw"><div class="l">Parole chiave</div></div>'
 +'<div class="ft"><span>'+MAT.toUpperCase()+' &nbsp;·&nbsp; Prof.ssa '+DOC+'</span><span>Pagina '+n+'</span></div>';
 document.getElementById('root').appendChild(d);return d}
function nkfill(sh,ids){const k=sh.querySelector('.nk');const seen=new Set();let n=0;
 for(const i of ids)for(const x of D[i].nk){const key=x.v+x.u;if(seen.has(key)||n>=6)continue;seen.add(key);n++;
  const e=document.createElement('div');e.className='t';e.dataset.u=D[i].id;const L=x.v.length+(x.u=='%%'?1:0),cl=L>9?'v l':(L>6?'v m':'v');e.innerHTML='<div class="'+cl+'">'+x.v+(x.u?(x.u=='%%'?'<small class="pc">%%</small>':'<small>'+x.u+'</small>'):'')+'</div><div class="lb">'+x.l+'</div>';k.appendChild(e)}
 if(!n)k.style.display='none';else{if(n%%2)k.lastElementChild.classList.add('w2');k.insertAdjacentHTML('afterbegin','<div class="cap">Numeri chiave</div>');
  k.querySelectorAll('.v').forEach(v=>{let f=parseFloat(getComputedStyle(v).fontSize);while(v.clientWidth>0&&v.scrollWidth>v.clientWidth&&f>14){f-=1;v.style.fontSize=f+'px'}})}}
function kwfill(sh,ids){const k=sh.querySelector('.kw');const seen=new Set();let n=0;
 for(const i of ids){for(const w of D[i].kw){const key=w.toLowerCase();if(seen.has(key)||n>=5||w.length>30)continue;seen.add(key);n++;
   const e=document.createElement('div');e.className='w';e.textContent=w;k.appendChild(e)}}
 if(!n)k.style.display='none'}
const SL=[];let cur=null,ids=[];
function over(bd){const l=bd.lastElementChild;if(!l)return false;const c=getComputedStyle(bd);return l.getBoundingClientRect().bottom>bd.getBoundingClientRect().bottom-parseFloat(c.paddingBottom)+1}
function close(){if(cur){kwfill(cur,ids);nkfill(cur,ids);let c=0;cur.querySelectorAll('.bd p.pl,.bd p.bu').forEach(e=>{if(!e.classList.contains('bu'))e.dataset.n=++c});SL.push({ids:ids.map(i=>D[i].id),a:D[ids[0]].a,s:D[ids[0]].s})}}
// gruppi: stessa sottosezione, tabelle da sole
const G=[];for(let i=0;i<D.length;i++){const u=D[i],g=G[G.length-1];
 if(!g||D[g[0]].s!==u.s||u.big||D[g[g.length-1]].big)G.push([i]);else g.push(i)}
// altezza di ogni unità (sonda)
const probe=shell(0,0,0),pb=probe.querySelector('.bd');const cs=getComputedStyle(pb);const HB=pb.clientHeight-parseFloat(cs.paddingTop)-parseFloat(cs.paddingBottom)-2;const HW={},HN={};let HU=HW;
for(const g of G)for(const i of g){pb.classList.remove('nar');pb.innerHTML=D[i].h;let e=pb.firstElementChild;HW[i]=e.getBoundingClientRect().height+parseFloat(getComputedStyle(e).marginBottom);
 pb.classList.add('nar');pb.innerHTML=D[i].h;e=pb.firstElementChild;HN[i]=e.getBoundingClientRect().height+parseFloat(getComputedStyle(e).marginBottom)}
probe.remove();
function fit(g,C){const out=[[]];let h=0;for(const i of g){if(out[out.length-1].length&&h+HU[i]>C){out.push([]);h=0}out[out.length-1].push(i);h+=HU[i]}return out}
function atoms(g){const A=[];for(const i of g){const last=A[A.length-1];if(last&&D[i].li&&D[last[0]].lead&&last.reduce((a,j)=>a+HU[j],0)+HU[i]<=HB)last.push(i);else if(last&&D[i].li&&last.length>1&&D[last[last.length-1]].li&&D[last[0]].lead&&last.reduce((a,j)=>a+HU[j],0)+HU[i]<=HB)last.push(i);else A.push([i])}return A}
const MAXC=3;function cards(a){return a.reduce((x,j)=>x+(D[j].lead?0:(D[j].li&&HU[j]<HB*0.16?0.5:1)),0)}
function fitA(A,C){const out=[[]];let h=0,c=0;for(const a of A){const ha=a.reduce((x,j)=>x+HU[j],0),ca=cards(a);if(out[out.length-1].length&&(h+ha>C||c+ca>MAXC)){out.push([]);h=0;c=0}out[out.length-1].push(...a);h+=ha;c+=ca}return out}
for(const g of G){const nar=g.some(i=>D[i].nk.length);HU=nar?HN:HW;const A=atoms(g);let parts=fitA(A,HB);const n=parts.length;
 if(n>1){let lo=Math.max(...A.map(a=>a.reduce((x,j)=>x+HU[j],0))),hi=HB;for(let k=0;k<30;k++){const m=(lo+hi)/2;if(fitA(A,m).length<=n)hi=m;else lo=m}parts=fitA(A,hi)}
 for(const p of parts){cur=shell(SL.length+1,D[p[0]].a,D[p[0]].s);ids=p.slice();const bd=cur.querySelector('.bd');if(nar&&p.some(i=>D[i].nk.length))bd.classList.add('nar');for(const i of p)bd.insertAdjacentHTML('beforeend',D[i].h);close()}}
window.SLIDES=SL;
document.querySelectorAll('.sheet .bd').forEach(b=>{if(over(b))b.parentElement.dataset.over=1});
</script></body></html>"""%(CSS,json.dumps(DATA,ensure_ascii=False),json.dumps([t for _,t in S.ARG],ensure_ascii=False),
       json.dumps([t for _,t in S.SUB],ensure_ascii=False),LG,json.dumps(MAT),json.dumps(DOC))
    open(path,'w').write(page)
    return U
if __name__=='__main__':
    import os
    keep=set(json.load(open('/home/claude/lezioni/afm-inglese-triennio-lez01/sync2.json' if os.path.exists('/home/claude/lezioni/afm-inglese-triennio-lez01/sync2.json') else '/home/claude/lezioni/afm-inglese-triennio-lez01/sync.json'))['spoken']) if os.environ.get('SPOKEN') else None
    build(keep=keep)
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        br=p.chromium.launch();pg=br.new_page(viewport={'width':1920,'height':1080})
        pg.goto('file:///home/claude/lezioni/afm-inglese-triennio-lez01/slides.html');pg.wait_for_timeout(800)
        SL=pg.evaluate('window.SLIDES');json.dump(SL,open('/home/claude/lezioni/afm-inglese-triennio-lez01/slides.json','w'))
        over=pg.evaluate("[...document.querySelectorAll('.sheet')].map((s,i)=>s.dataset.over?i+1:0).filter(x=>x)")
        print(len(SL),'slide; troppo piene:',over)
        els=pg.query_selector_all('.sheet')
        only=[int(x) for x in sys.argv[1:]]
        for n in only: els[n-1].screenshot(path=f'/home/claude/lezioni/afm-inglese-triennio-lez01/fr/sl{n:02d}.png')
