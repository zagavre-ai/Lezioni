import sys,os,json,re
sys.path.insert(0,'/home/claude/w/b')
from scenes import *
from plan import *
from slides import slide_html
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,landscape
os.makedirs(B+'/dp',exist_ok=True)
HIDE='<style>.cam,.band{display:none!important}</style>'
VT='''(()=>{const out=[];document.querySelectorAll('body *').forEach(e=>{if([...e.children].some(c=>c.tagName!='BR')&&!e.matches('.bx,.c,.row,.ln'))return;if(e.closest('#fo'))return;const rr=e.getBoundingClientRect();if(rr.width==0||rr.height==0||getComputedStyle(e).display=='none'||e.closest('.arg[style*=none]'))return;let o=1,n=e;while(n&&n!==document.body){o*=parseFloat(getComputedStyle(n).opacity);n=n.parentElement}
 if(o<0.4)return;const t=(e.innerText||'').trim();if(!t||e.tagName=='STYLE'||e.tagName=='SCRIPT'||e.tagName=='svg')return;const r=e.getBoundingClientRect();out.push([Math.round(r.top/20),r.left,t])});
 out.sort((a,b)=>a[0]-b[0]||a[1]-b[1]);return out.map(x=>x[2])})()'''
def shot_page(html,t,out,num=None):
    pg=page(); pg.set_content(html.replace('</head>',HIDE+'</head>')); pg.wait_for_timeout(250)
    if t is not None: pg.evaluate(f'render({t:.3f})')
    if num: pg.evaluate("""(n)=>{const b=document.body;const dk=b.classList.contains('dark');let f=b.querySelector('.foot'),p=b.querySelector('.pg');if(!f){f=document.createElement('div');f.className='foot';f.textContent='STORIA';b.appendChild(f)}if(!p){p=document.createElement('div');p.className='pg';b.appendChild(p)}p.textContent='Pagina '+n;if(dk){f.style.color='#DCE6F7';p.style.color='#DCE6F7'}}""",num)
    pg.screenshot(path=out); return pg.evaluate(VT)
def add_pg(html,n):
    return html
def rolling_t(S,w,per=3):
    last=min(w*per+per-1,len(S)-1); t=S[last][0]+0.7
    if (w+1)*per<len(S): t=min(t,S[(w+1)*per][0]-0.1)
    return t
def cover_diss(mappe=False):
    h=cover_html(False,anim=False)
    h=h.replace('STORIA · VIDEOLEZIONE','STORIA').replace('<div class="arg"','<div class="arg" style="display:none"')
    if mappe: h=h.replace('<div class="lab" style="top:146px">STORIA</div>','<div class="lab" style="top:146px">STORIA</div><div class="chip" style="position:absolute;left:80px;top:196px;background:#FFE600;color:#0B1530">MAPPE</div>').replace('class="ct h1"','class="ct h1" style="top:300px"').replace('class="bar"','class="bar" style="top:670px"')
    return h
def build_pages():
    pages=[];P=plan()
    for i,(k,x,w) in enumerate(P):
        n=i+1; out=f'{B}/dp/p{n:02d}.png'
        if k=='cover': txt=shot_page(cover_diss(),8,out,n)
        elif k=='dic': d=dic_scene(); txt=shot_page(d['html'],d['dur']-0.6,out,n)
        elif k=='sub':
            arg,ci,t0,anc=SUB[x]; cs=[cards[j] for j in ci]; kws=[]
            for j in ci: kws+=KW[j]
            h=slide_html(f'{arg:02d} · {ARG[arg]}'.upper(),cs,None,kws[:5],n,cam=False)
            txt=shot_page(h,None,out,n)
        elif k=='an':
            d=appro_scene(x); S=vox.info(x)['sent'][1:]; txt=shot_page(d['html'],rolling_t(S,w),out,n)
        elif k=='sch': d=schema_scene(x); txt=shot_page(d['html'],d['dur']-1.0,out,n)
        elif k=='glos':
            d=glossario_scene(); S=vox.info('GL1')['sent'][1:]; txt=shot_page(d['html'],rolling_t(S,w),out,n)
        elif k=='rip':
            d=ripasso_scene(x); S=vox.info(f'R{x}')['sent']; S=S[1:] if S[0][2].lower().startswith('ripassiamo') else S; txt=shot_page(d['html'],rolling_t(S,w),out,n)
        elif k=='compi':
            sc=dict((nm,f) for nm,f in __import__('build').scene_list())['compi%d'%(w+1)]; d=sc(); txt=shot_page(d['html'],d['dur']-1.0,out,n)
        pages.append((out,txt,(k,x,w)))
    return pages
def make_pdf(pages,outpdf,title):
    c=canvas.Canvas(outpdf,pagesize=landscape(A4)); c.setTitle(title); c.setAuthor('Centro Studi Telesio'); c.setSubject('Storia')
    W_,H_=landscape(A4); ih=W_*1080/1920
    for png,txt,_ in pages:
        c.drawImage(png,0,(H_-ih)/2,W_,ih)
        t=c.beginText(30,H_-40); t.setTextRenderMode(3); t.setFont('Helvetica',9)
        for line in txt:
            for ln in re.sub(r'\s+',' ',line).split('\n'):
                try: t.textLine(ln.encode('cp1252','replace').decode('cp1252'))
                except Exception: pass
        c.drawText(t); c.showPage()
    c.save()
if __name__=='__main__':
    pages=build_pages(); json.dump([(a,b,c) for a,b,c in pages],open(B+'/dp/pages.json','w'),ensure_ascii=False)
    make_pdf(pages,B+'/Storia_Lez7_dispensa.pdf','Storia · Gli Stati Uniti: dal boom economico al New Deal')
    print(len(pages),'pagine')
