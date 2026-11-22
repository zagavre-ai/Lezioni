import sys,os,html,re
sys.path.insert(0,'/home/claude/w/b')
from lib import *
from data import *
from plan import pagenum
os.makedirs(B+'/st',exist_ok=True)
logo_b64=None
def lead_split(c):
    i=c.index(':'); return c[:i],c[i+1:].strip()
def card_html(c,state):
    a,b=lead_split(c)
    cl='card '+state
    return f'<div class="{cl}" style="position:relative"><b>{html.escape(a)}:</b> {html.escape(b)}</div>'
def slide_html(label,cards,lit,kws,pagina,cam=True):
    cs=''.join(card_html(c,'on' if lit==i else ('dim' if lit is not None else '')) for i,c in enumerate(cards))
    kw=''.join(f'<span>{html.escape(k)}</span>' for k in kws[:5])
    camhtml='<div class="cam"></div><div class="band"><b>Giorgio Mazzotti</b><i>PROF. DI STORIA</i></div>' if cam else ''
    return head()+f'''<img class="logo" src="{LOGO}"><div class="hr"></div>
<div class="lab">{html.escape(label)}</div>
<div style="position:absolute;left:80px;top:182px;width:1290px;display:flex;flex-direction:column;gap:16px">{cs}</div>
{camhtml}<div class="kw"><h4>PAROLE CHIAVE</h4>{kw}</div>
<div class="hr2"></div><div class="foot">STORIA</div><div class="pg">Pagina {pagina}</div></body></html>'''
def render_all():
    meas={}
    for n,(arg,ci,t0,anc) in enumerate(SUB):
        cs=[cards[i] for i in ci]; kws=[]
        for i in ci: kws+=KW[i]
        kws=kws[:5]
        label=f'{arg:02d} · {ARG[arg]}'.upper()
        for lit in [None]+list(range(len(ci))):
            f=f'{B}/st/s{n:02d}_{"n" if lit is None else lit}.png'
            shot(slide_html(label,cs,lit,kws,pagenum('sub',n)),f)
        h=page().evaluate("document.querySelector('div[style*=flex]').getBoundingClientRect().height")
        meas[n]=h
    return meas
if __name__=='__main__':
    m=render_all(); print({k:round(v) for k,v in m.items()})
