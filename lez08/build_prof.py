# monta i pezzi del prof: sfondo (slide a card / opere con zoom) + webcam 4:3 + audio pulito
import sys, os, json, subprocess, numpy as np, cv2
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from plan import *; from gfx import *; from slidedata import SL; import frames
B='/tmp/w/b'; OP='/tmp/w/op'
CAM=(851,335,181,136)  # riquadro 4:3 nella webcam originale (247x137): risoluzione d'origine 181x136
def pages():
    n=0; pg={}
    for p in PROF:
        for i,s in enumerate(p['scenes']):
            n+=1; pg[(p['id'],i)]=n
    return pg
PG=pages()
def shots(man): 
    mf=f'{B}/man_{os.getpid()}.json'; json.dump(man,open(mf,'w')); r=subprocess.run(['node',os.path.join(os.path.dirname(os.path.abspath(__file__)),'shot.js'),mf],capture_output=True,text=True)
    if r.returncode: raise SystemExit(r.stderr)
    return json.load(open(mf+'.res'))
def cards_of(page):
    if page in (71,72): t,c=SL[7]; return t,(c[:2] if page==71 else c[2:])
    t,c=SL[page]; return t,c
def titlen(t): return 2 if len(t)>38 else 1
def seg_states(sc):
    """[(t, active, mode)] nel tempo originale, con alternanza panoramica/focus nei tratti lunghi"""
    act=[(sc['t0'],None)]+[(t,c) for t,c in sc['act']]
    out=[]
    for k,(t,c) in enumerate(act):
        e=act[k+1][0] if k+1<len(act) else sc['t1']
        t=snap_inizio(t,2.5) if k>0 else t
        d=e-t
        if c is not None and d>45:
            k2=0; tt=t
            while tt<e-1:
                out.append((tt,c,'overview')); tt+=28
                if tt<e-6: out.append((tt,c,'focus')); tt+=22
            continue
        elif c is None and d>45:
            tt=t
            while tt<e-1: out.append((tt,c,'overview')); tt+=60
            continue
        else: out.append((t,c,'overview'))
    return out
def build_pngs(piece,pgmap):
    man=[]; ref={}
    for i,sc in enumerate(piece['scenes']):
        pg=pgmap[(piece['id'],i)]; arg=sc.get('arg',piece['arg'])
        if sc['kind']=='cards':
            t,c=cards_of(sc['page']); tl=titlen(t)
            for (_,a,m) in seg_states(sc):
                f=f'{B}/{piece["id"]}_{i}_{a}_{m}'
                if (a,m) in ref.get(i,{}): continue
                open(f+'.html','w').write(cards_slide(LAB[arg],t,c,a,pg,sc['keys'],m,tl)); man.append({'html':f+'.html','out':f+'.png'}); ref.setdefault(i,{})[(a,m)]=f+'.png'
        elif sc['kind']=='art':
            f=f'{B}/{piece["id"]}_{i}_art'; open(f+'.html','w').write(art_slide(LAB[arg],'',sc['cap'],pg,sc['keys']).replace('<div class="title"','<div class="title" style="display:none"',1) if False else art_slide(LAB[arg],'',sc['cap'],pg,sc['keys']))
            man.append({'html':f+'.html','out':f+'.png'}); ref[i]=f+'.png'
        elif sc['kind']=='grid':
            f=f'{B}/{piece["id"]}_{i}_art'; open(f+'.html','w').write(art_slide(LAB[arg],'',sc['cap'],pg,sc['keys'])); man.append({'html':f+'.html','out':f+'.png'}); ref[i]=f+'.png'
        elif sc['kind']=='cover':
            f=f'{B}/cover'; open(f+'.html','w').write(cover_html(pg)); man.append({'html':f+'.html','out':f+'.png'}); ref[i]=f+'.png'
    shots(man); return ref
def cover_html(pg):
    arg=''.join(f'<li><b>{n}</b>{esc(t)}</li>' for n,t in ARG.items())
    h=base("Storia dell'arte · Videolezione",TITOLO,pg,None,True)
    css='<style>.arg{position:absolute;left:80px;top:330px;width:1290px;background:#F5F8FC;border-radius:18px;padding:26px 36px;box-shadow:0 8px 26px rgba(70,80,100,.13)}.arg h4{font-weight:700;font-size:22px;letter-spacing:.14em;color:#2060AF;margin-bottom:14px}.arg ol{list-style:none}.arg li{font-size:38px;line-height:1.28;font-weight:600;margin:4px 0}.arg li b{display:inline-block;width:56px;color:#2060AF;font-weight:800}.title{font-size:96px !important;top:200px !important}</style>'
    body='<div class="bar" style="top:318px"></div><div class="arg"><h4>ARGOMENTI</h4><ol>'+arg+'</ol></div>'
    return h.replace('</head>',css+'</head>').replace('@@BODY@@',body)
def make_cam(a,b,out):
    x,y,w,h=CAM; d=b-a
    vf=f"crop={w}:{h}:{x}:{y},scale=412:309:flags=lanczos,unsharp=5:5:0.5:3:3:0.0,eq=contrast=1.03:saturation=1.05,fps=30"
    af=f"highpass=f=75,afftdn=nr=6:nf=-45,afade=t=in:st=0:d=0.03,afade=t=out:st={d-0.03:.3f}:d=0.03"
    r=subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{a:.3f}','-t',f'{d:.3f}','-i',ORIG,'-vf',vf,'-af',af,'-c:v','libx264','-preset','veryfast','-crf','12','-pix_fmt','yuv444p','-c:a','pcm_s16le','-ar','48000','-ac','2',out],capture_output=True,text=True)
    if r.returncode: raise SystemExit(r.stderr)
def build_piece(pid,out):
    piece=[p for p in PROF if p['id']==pid][0]; a,b,_,_=taglio(piece); d=b-a
    ref=build_pngs(piece,PG)
    tl=[]
    for i,sc in enumerate(piece['scenes']):
        t0=max(sc['t0'],a)-a if i>0 else 0.0
        if sc['kind']=='cards':
            for (t,act,m) in seg_states(sc):
                tl.append((max(t-a,0.0),frames.Static(ref[i][(act,m)])))
        elif sc['kind']=='art':
            dur=min(sc['t1'],b)-sc['t0']
            tl.append((t0,frames.Art(ref[i],f'{OP}/{sc["img"]}.png',ART_BOX,dur,sc['zmax'],sc['focus'],sc['start'])))
        elif sc['kind']=='grid':
            tl.append((t0,frames.Static(ref[i])))  # sostituito dalla griglia delle opere
        elif sc['kind']=='cover':
            tl.append((0.0,frames.Static(ref[i])))
    tl.sort(key=lambda x:x[0])
    cam=f'{B}/cam_{pid}.mkv'; make_cam(a,b,cam)
    ff=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1920x1080','-r','30','-i','-','-i',cam,
      '-filter_complex','[0:v][1:v]overlay=1428:148:shortest=1,format=yuv420p[v]','-map','[v]','-map','1:a','-c:v','libx264','-preset','veryfast','-crf','18','-c:a','pcm_s16le','-shortest',out],stdin=subprocess.PIPE)
    frames.render_timeline(tl,d,ff.stdin); ff.stdin.close(); ff.wait()
    print(pid,'ok',round(d,1),'s',flush=True)
if __name__=='__main__':
    for pid in sys.argv[1:]: build_piece(pid,f'{B}/p_{pid}.mkv')
