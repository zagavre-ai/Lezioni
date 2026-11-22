import sys,os,json
sys.path.insert(0,'/home/user/work/build')
exec(open('/home/user/work/build/build2.py').read())
wins,VC,pn=plan()
json.dump(dict(wins=[[k[0],k[1],v] for k,v in wins.items()],pn=[[k[0],list(k[1]),v] for k,v in pn.items()],VC={k:[v[0],v[1]] for k,v in VC.items()}),open(B+'/plan.json','w'))
os.makedirs(B+'/clips',exist_ok=True)
pa=rdwav(B+'/prof_clean.wav',1)
# cover (pagina 1)
CSS_COVER="""
#c1{position:absolute;left:80px;top:300px;font:800 26px FG;letter-spacing:.18em;color:#2060AF}
#c2{position:absolute;left:80px;top:350px;width:1280px;font:800 118px/1.0 BG;letter-spacing:-.015em;color:#0B1530}
#cb{position:absolute;left:80px;top:610px;width:90px;height:7px;background:#2060AF;border-radius:4px}
#cg{position:absolute;left:80px;top:640px;font:500 30px FG;color:#3A4560}
#ca{position:absolute;left:80px;top:700px;width:1280px;background:#F4F7FC;border:2px solid #E2E8F0;border-radius:22px;padding:18px 36px 22px;box-shadow:0 14px 34px rgba(60,72,100,.12)}
#ca .h{font:800 22px FG;letter-spacing:.16em;color:#2060AF;margin-bottom:10px}
#ca ul{list-style:none;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(3,auto);grid-auto-flow:column;gap:6px 40px}
#ca li{font:600 30px/1.3 FG;color:#0B1530;padding-left:34px;position:relative}
#ca li:before{content:'';position:absolute;left:6px;top:14px;width:12px;height:12px;border-radius:50%;background:#2060AF}
"""
def cover(cam,out):
    items=''.join(f'<li>{T["t"]}</li>' for T in TOP)
    h=f'<img id=logo src="data:image/svg+xml;base64,{LOGO}"><div id=hl></div><div id=c1>STORIA V · VIDEOLEZIONE</div><div id=c2>L\'URSS di Stalin<br>(1924-1939)</div><div id=cb></div><div id=cg>URSS: Unione delle Repubbliche Socialiste Sovietiche</div><div id=ca><div class=h>ARGOMENTI</div><ul>{items}</ul></div>'
    if cam: h+='<div id=cam></div><div id=band><div class=nm>Giorgio Mazzotti</div><div class=ms>PROF. DI STORIA</div></div>'
    h+='<div id=fl></div><div id=ft>STORIA V</div><div id=pg>Pagina 1</div>'
    r.shot(h,out,CSS_COVER)
cover(False,B+'/cover_a.png');cover(True,B+'/cover_b.png')
SUB=[('D0',0.0,57.6)]+SUBCLIPS
for name,a,b in SUB:
    cname='D'+name[1:] if name.startswith('T') else name
    out=f'{B}/clips/{cname}.mkv'
    if os.path.exists(out+'.ok'): continue
    d=nfr(b-a)/30
    if name=='D0':
        fp=B+'/foto_b.png';r.shot(foto_html(pn[('FOTO',(0,))],True),fp)
        seq=[[0,54.3,B+'/cover_b.png'],[54.3,d,fp]]
    else:
        seq=clip_seq(r,wins,name,a,b,pn)
    fl=fade_list(seq,d);cc=f'{B}/clips/{cname}.txt';write_concat(fl,cc)
    compose(cc,a,a+d,None,out)
    x=pa[int(a*SR):int((a+d)*SR)]
    m=Mix(d);m.add(0,x,0,0.0);m.save(f'{B}/clips/{cname}.wav')
    open(out+'.ok','w').write('1');print(name,d,flush=True)
