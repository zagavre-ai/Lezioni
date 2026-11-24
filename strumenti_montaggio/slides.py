from lib import *
CSS='''
.logo{position:absolute;left:80px;top:46px;width:166px;height:52px;background:url("%s") no-repeat left center/contain}
.rule{position:absolute;left:80px;right:80px;top:124px;height:2px;background:#E4E9F0}
.rule2{position:absolute;left:80px;right:80px;top:981px;height:2px;background:#E4E9F0}
.kick{position:absolute;left:80px;top:146px;font:700 24px Fig;letter-spacing:.14em;color:#2060AF;text-transform:uppercase;width:1300px}
.tit{position:absolute;left:80px;top:188px;width:1300px;font:800 56px/1.08 Bri;color:#0B1530;letter-spacing:-.01em}
.tit:after{content:"";display:block;width:84px;height:7px;background:#2060AF;border-radius:4px;margin-top:14px}
.foot{position:absolute;left:80px;top:1000px;font:700 22px Fig;letter-spacing:.12em;color:#2060AF}
.pag{position:absolute;right:80px;top:1000px;font:700 22px Fig;letter-spacing:.12em;color:#2060AF}
.cards{position:absolute;left:80px;width:1300px}
.card{position:relative;background:#fff;border:3px solid #DCE3EE;border-radius:20px;padding:20px 36px 20px 58px;margin-bottom:24px;
  font:500 40px/1.5 Fig;color:#0B1530;box-shadow:0 10px 28px rgba(60,72,98,.13);opacity:.55}
.card b{font-weight:800}
.card.on{opacity:1;border:6px solid #FFE600;padding:17px 33px 17px 55px;box-shadow:0 0 0 4px rgba(255,230,0,.35),0 12px 30px rgba(60,72,98,.18)}
.card .dot{position:absolute;left:22px;top:34px;width:20px;height:20px;border-radius:50%%;background:#C9D2E0}
.card.on .dot{background:#FFE600;box-shadow:0 0 0 3px #0B1530}
.cam{position:absolute;left:1428px;top:148px;width:412px;height:309px;border-radius:16px;background:#EEF1F6;box-shadow:0 14px 34px rgba(60,72,98,.28)}
.band{position:absolute;left:1428px;top:466px;width:412px;height:104px;background:#FFE600;border-radius:12px;transform:rotate(-1.6deg);
  box-shadow:0 10px 24px rgba(60,72,98,.25);padding:18px 24px}
.band .n{font:800 36px/1.1 Bri;color:#0B1530}.band .m{font:800 21px Fig;letter-spacing:.06em;margin-top:8px;color:#0B1530}
.kw{position:absolute;left:1428px;top:640px;width:412px}
.kw h4{margin:0 0 12px;font:800 22px Fig;letter-spacing:.14em;color:#2060AF}
.kw span{display:inline-block;margin:0 10px 10px 0;padding:8px 16px;border-radius:999px;background:#FFF3BF;border:3px solid #A16207;font:700 26px Fig;color:#0B1530}
.photo{position:absolute;border-radius:16px;box-shadow:0 14px 34px rgba(60,72,98,.28);overflow:hidden;background:#fff}
.photo img{width:100%%;height:100%%;object-fit:contain;display:block}
.cap{position:absolute;font:600 30px/1.4 Fig;color:#0B1530}
'''%'file:///home/user/Lezioni/kit/docenti/Telesio_logo_blu.svg'
def slide_html(kicker,title,cards=None,on=None,kw=None,page=1,photos=None,cap=None,prof=True,foot='STORIA V',title_size=None):
    h=[f'<!doctype html><meta charset=utf-8><style>{BASE}{CSS}</style><body>']
    h.append('<div class=logo></div><div class=rule></div><div class=rule2></div>')
    h.append(f'<div class=kick>{esc(kicker)}</div>')
    n_=len(title);title_size=title_size or (56 if n_<=36 else 48 if n_<=44 else 42)
    ts=f'style="font-size:{title_size}px"'
    h.append(f'<div class=tit id=tit {ts}>{esc(title)}</div>')
    if prof:
        h.append('<div class=cam></div><div class=band><div class=n>Giorgio Mazzotti</div><div class=m>PROF. DI STORIA</div></div>')
        if kw: h.append('<div class=kw><h4>PAROLE CHIAVE</h4>'+''.join(f'<span>{esc(k)}</span>' for k in kw[:5])+'</div>')
    h.append(f'<div class=foot>{esc(foot)}</div><div class=pag>Pagina {page}</div>')
    if cards:
        h.append('<div class=cards id=cards>')
        for i,c in enumerate(cards):
            h.append(f'<div class="card{" on" if on==i else ""}"><span class=dot></span>{rich(c)}</div>')
        h.append('</div>')
        h.append('<script>var t=document.getElementById("tit");var yy=t.offsetTop+t.offsetHeight+30;document.getElementById("cards").style.top=yy+"px";</script>')
    if photos:
        n=len(photos);aw=1300;ah=510;gap=30
        tw=sum(w/hh*ah for _,w,hh in photos);sc=min(1,(aw-gap*(n-1))/tw)
        xs=80+(aw-(tw*sc+gap*(n-1)))/2
        for uri,w,hh in photos:
            pw=w/hh*ah*sc;ph=ah*sc
            h.append(f'<div class=photo style="left:{xs:.0f}px;top:{290+(ah-ph)/2:.0f}px;width:{pw:.0f}px;height:{ph:.0f}px"><img src="{uri}"></div>');xs+=pw+gap
        if cap: h.append(f'<div class=cap style="left:80px;top:{290+ah+26}px;width:1300px">{rich(cap)}</div>')
    h.append('</body>')
    return ''.join(h)
