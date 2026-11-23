# -*- coding: utf-8 -*-
import sys,os,json,re,math,subprocess
sys.path.insert(0,'/home/user/work18/lib')
from part import *
from render import *
from maps import *
from dark import frames as dframes
from content import *
from cuts import cut,info,last_words,level,WAV
import numpy as np
PROFRAW=W+'/a/prof_clean.f32'
if not os.path.exists(PROFRAW):
    run(['ffmpeg','-y','-loglevel','error','-i',W+'/a/prof_clean.wav','-ac','2','-ar','48000','-f','f32le',PROFRAW])
PM=np.memmap(PROFRAW,dtype=np.float32,mode='r').reshape(-1,2)
def prof_audio(t0,t1):
    a=PM[int(round(t0*SR)):int(round(t1*SR))].copy()
    return a
PGAIN=float(open(W+'/a/pgain').read()) if os.path.exists(W+'/a/pgain') else 1.0
from cuts import prev_end
OVR={}
def CS(T):
    if T in OVR:return round(OVR[T]*30)/30
    return round((T-0.15)*30)/30
def CE(T):
    if T in OVR:return round(OVR[T]*30)/30
    pe=prev_end(T)
    for c in (min(T-0.15,pe+0.7),T-0.15):
        c=round(c*30)/30
        if float(level(c,WAV))<-42:return c
    from taglio import snap
    return round(snap(T,WAV,0.6,0.0)*30)/30
INTRO_S=CS(0.55);INTRO_E=CE(184.13)
A3E=round((2096.58-0.15)*30)/30   # fine arg3: dopo «Quindi c'è la fiducia.»
END=4273.9
AN_LIST={1:[(CE(484.81),CS(484.81),'AN1a'),(CE(664.1),CS(664.1),'AN1b')],2:[(CE(1355.8),CS(1355.8),'AN2a'),(CE(1630.8),CS(1630.8),'AN2b')],3:[],4:[(CE(2483.05),CS(2483.05),'AN4a')],5:[(CE(3330.85),CS(3330.85),'AN5b')],6:[(CE(4047.14),CS(4047.14),'AN6a')]}
ARG_RANGE={1:(CS(187.72),CE(880.9)),2:(CS(880.9),CE(2030.4)),3:(CS(2034.6),A3E),4:(CS(2098.47),CE(2985.35)),5:(CS(2985.35),CE(3584.13)),6:(CS(3584.13),END)}
A1S=ARG_RANGE[1][0]
def fi(t):return int(round(t*FPS))
def lead_voice(part,name,states_fn,voice,lead=0.7,tail=0.7,**kw):
    pass
# ---------------- prof: finestre con card ----------------
def clip_windows(wins,ps,pe):
    out=[]
    for w in wins:
        a,b=max(w['t0'],ps),min(w['t1'],pe)
        if b-a<0.5:continue
        cs=[c for c in w['card'] if a-0.01<=c['t']<b]
        if not cs and out:out[-1]=dict(out[-1],t1=b);continue
        out.append(dict(w,t0=a,t1=b,card=cs))
    out[0]['t0']=ps;out[-1]['t1']=pe
    return out
def regroup_img(wins,per=2):
    """appiattisce le card e le raggruppa a 2 (finestre con immagine)"""
    cs=[c for w in wins for c in w['card']];a=wins[0]['t0'];b=wins[-1]['t1'];out=[]
    for i in range(0,len(cs),per):
        g=cs[i:i+per];t0=a if i==0 else g[0]['t']-0.0
        t1=b if i+per>=len(cs) else cs[i+per]['t']
        out.append(dict(t0=t0,t1=t1,card=g,kw_on=wins[0].get('kw_on',[])))
    return out
def prof_piece(part,name,wins,kw,label,title,img0=None,camfade=True):
    ps=wins[0]['t0'];pe=wins[-1]['t1']
    T0=fi(ps)/FPS;T1=fi(pe)/FPS
    part.pm.append((f'{name}_0',T0,T1))
    for k,w in enumerate(wins):
        a=fi(w['t0']);b=fi(w['t1']);n=b-a
        cs=w['card'];part.page+=1;pg=part.page;cards=[c['testo'] for c in cs]
        img=w.get('img',img0)
        def png(act,pg=pg,cards=cards,k=k,w=w,img=img):
            key=f'{name}_{k}_{act}'
            if img and w.get('imgmode')=='wide':return img_slide_wide(label,pg,img,cards[0],f'{W}/st/{key}.png',kw,w.get('kw_on',()),True) if cards else img_slide_wide(label,pg,img,'',f'{W}/st/{key}.png',kw,w.get('kw_on',()),True)
            if img:return img_slide(label,title,pg,img,cards,act,f'{W}/st/{key}.png',kw,w.get('kw_on',()),True)
            return slide_cards(label,title,cards,act,pg,kw,w.get('kw_on',()),True,f'{W}/st/{key}.png')
        part.slides.append(dict(png=png(-1),cards=cards,page=pg,title=title,label=label,img=img,wide=(w.get('imgmode')=='wide')))
        bs=[fi(c['t']) for c in cs]
        states=[]
        if not cs:states=[(png(-1),n)]
        else:
            if bs[0]-a>=30:states.append((png(-1),bs[0]-a));start=bs[0]
            else:start=a
            for j in range(len(cs)):
                s0=start if j==0 else bs[j];s1=bs[j+1] if j+1<len(cs) else b
                states.append((png(j),s1-s0))
            states=[(p,f) for p,f in states]
        tot=sum(f for _,f in states)
        if tot!=n:states[-1]=(states[-1][0],states[-1][1]+n-tot)
        aud=[(0,fade(prof_audio(T0,T1)*PGAIN,15),1.0)] if k==0 else []
        part.scene(f'{name}_{k}',states,cam=a/FPS,aud=aud,kind='prof',whoosh_=(k==0),camfade=(k==0 and camfade),xin=12 if k==0 else 9)

LEAD=0.7;TAIL=0.8
def vaud(name,off,g=1.0):return (off,fade(rdwav(vpath(name))),g,name)
def fill(items,total):
    """items=[(png,t_inizio_s)] crescente -> stati (png,frames) che riempiono total frame"""
    out=[]
    for i,(p,t) in enumerate(items):
        a=fi(t) if i else 0;b=fi(items[i+1][1]) if i+1<len(items) else total
        if b>a:out.append((p,b-a))
    d=total-sum(f for _,f in out)
    if d:out[-1]=(out[-1][0],out[-1][1]+d)
    return out
def dark_scene(part,name,spec,aud,fps=30,whoosh_=True,wmode=None):
    pat,n=dframes(spec,name,fps)
    part.scene(name,[(pat,n)],aud=aud,kind='dark',whoosh_=whoosh_,wmode=wmode)
def sc_title(part,i):
    a=ARG[i];spec={"type":"title","num":"%02d"%i,"total":6,"lines":a['lines'],"ex":a['ex'],"fs":a['fs'],"lineY":a['ly'],"dur":4.0}
    dark_scene(part,f'T{i}',spec,[(0.1,jingle('titolo'),0.9)])
def tfs(s):return 84 if len(s)<=24 else max(52,int(84*24/len(s)))
def sc_quizcard(part,qn,act,topic,pts):
    spec={"type":"quiz","act":act,"tfs":tfs(topic),"topic":topic,"pts":pts,"dur":5.0}
    dark_scene(part,f'Q{qn}',spec,[(0.5,jingle('quiz'),1.0)])
def group_sent(S,maxc=330,maxn=3):
    g=[];cur=[]
    for i,s in enumerate(S):
        if cur and (len(cur)>=maxn or sum(len(S[j]) for j in cur)+len(s)>maxc):g.append(cur);cur=[]
        cur.append(i)
    if cur:g.append(cur)
    return g
def voice_cards_scene(part,name,vname,label,title,pill=None,img=None,per=3,extra_aud=(),hold=None,mapimg=None,wide=False):
    """scheda bianca con le frasi della voce come card che si accendono"""
    S=sents(vname);st=sent_times(vname);vd=vdur(vname)
    total=fi(LEAD+vd+TAIL);G=group_sent(S,maxn=1 if wide else (per if not img else 2))
    items=[];gmark=[]
    for g in G:
        part.page+=1;pg=part.page;cards=[xs(disp(S[j])) for j in g];gmark.append((len(part.slides),LEAD+st[g[0]] if g[0] else 0.0))
        for k,j in enumerate(g):
            if img and wide:p=img_slide_wide(label,pg,img,cards[0],f'{W}/st/{name}_{j}.png',None,(),False)
            elif img:p=img_slide(label,title,pg,img,cards,k,f'{W}/st/{name}_{j}.png',None,(),False)
            else:p=slide_cards(label,title,cards,k,pg,None,(),False,f'{W}/st/{name}_{j}.png')
            items.append((p,LEAD+st[j] if j else 0.0))
        part.slides.append(dict(png=slide_cards(label,title,cards,-1,pg,None,(),False,f'{W}/st/{name}_g{g[0]}.png') if not img else (img_slide_wide(label,pg,img,cards[0],f'{W}/st/{name}_g{g[0]}.png',None,(),False) if wide else img_slide(label,title,pg,img,cards,-1,f'{W}/st/{name}_g{g[0]}.png',None,(),False)),cards=cards,page=pg,title=title,label=label,img=img,wide=wide))
    if mapimg:
        mk,fr_=mapimg;tm=LEAD+st[fr_];drop=[i for i,t in gmark if t>=tm-0.01]
        for i in sorted(drop,reverse=True):del part.slides[i]
        part.page-=len(drop);part.page+=1;mp=map_step(mk,len(ORDER[mk])+1,f'{W}/st/mapsp_{mk}_{part.page}.png',part.page);items=[(p,t) for (p,t) in items if t<tm-0.01];items.append((mp,tm))
        part.slides.append(dict(png=mp,cards=[],page=part.page,title='Mappa',label='Mappa',mapref=True))
    part.scene(name,fill(items,total),aud=[vaud(vname,LEAD)]+list(extra_aud),kind='kore')
    part.sub.append((name,vname,LEAD))
def sc_an(part,n,voice,tag):
    a=ARG[n];img=W+'/img/hd_carta.png' if n==4 else None
    voice_cards_scene(part,f'AN{n}{tag}',voice,f'Approfondimento · {a["nome"]}',a['nome'],img=img,wide=bool(img))
def sc_map(part,n,key,vnames):
    order=ORDER[key];vd=[vdur(v) for v in vnames];GAP=0.3
    part.page+=1;pg=part.page
    items=[];t=LEAD;aud=[]
    for i,v in enumerate(vnames):
        step=i+1 if i<len(order) else len(order)+1
        p=map_step(key,step,f'{W}/st/map{key}_{step}_{pg}.png',pg)
        items.append((p,t if i else 0.0));aud.append(vaud(v,t))
        t+=vd[i]+GAP
    full=map_step(key,len(order)+1,f'{W}/st/map{key}_{len(order)+1}_{pg}.png',pg)
    # la mappa intera resta ferma almeno 4 s dopo la voce che la chiude
    last_start=items[-1][1];end=max(last_start+vd[-1]+TAIL,last_start+4.0)
    total=fi(end)
    part.scene(f'MAP{n}',fill(items,total),aud=aud,kind='kore')
    part.slides.append(dict(png=full,cards=[],page=pg,title='Mappa',label='Mappa',map=key,n=n))
    part.sub.append((f'MAP{n}',vnames,LEAD))
def sc_pill(part,n):
    a=ARG[n];R=a['R'];vd=vdur(R);S=sents(R);st=sent_times(R);off=1.6
    caps=[[round(off+st[i],2),round(off+(st[i+1] if i+1<len(S) else vd),2),xs(disp(S[i]))] for i in range(len(S))]
    spec={"type":"repaso","kicker":"Pillola di storia","big":"RIPASSO","topic":a['nome'],"tfs":tfs(a['nome']),"caps":caps,"dur":round(off+vd+0.9,2)}
    dark_scene(part,f'R{n}',spec,[(0,jingle('repaso'),0.8),vaud(R,off)],fps=15)
    # schema di ripasso: scheda blu scura (come la pillola), una riga alla volta accesa con la voce
    P=a['P'];SCn=[f'{a["SC"]}_{k}' for k in range(1,5)];rows=SCH[n];off=0.9;t=off;caps=[];aud=[]
    caps.append([round(t,2),round(t+vdur(P),2),xs(disp(sents(P)[0] if False else TXT[P]))]);aud.append(vaud(P,t));t+=vdur(P)+0.35
    for k,v in enumerate(SCn):
        caps.append([round(t,2),round(t+vdur(v),2),f'{rows[k][0]}: {rows[k][1]}']);aud.append(vaud(v,t));t+=vdur(v)+0.35
    spec={"type":"repaso","kicker":"Schema di ripasso","big":"RIPASSO","topic":a['nome'],"tfs":tfs(a['nome']),"caps":caps,"dur":round(t+0.6,2)}
    dark_scene(part,f'S{n}',spec,aud,fps=15)
    part.page+=1;pg=part.page
    part.slides.append(dict(png=table_png('Schema di ripasso',a['nome'],pg,rows,-1,f'{W}/st/sch{n}_x.png'),cards=[f'{x}: {y}' for x,y in rows],page=pg,title=a['nome'],label='Schema di ripasso',table=True))
def qlist(items,label,n,part,names,start_q):
    pass
def sc_quiz_body(part,tag,label,items,qn,think_scale=1.0):
    L=len(items)
    for i,it in enumerate(items):
        it=dict(it);ex=xs
        it['p']=ex(it['p']);it['a']=ex(it['a']);it['w']=[ex(x) for x in it['w']];it['e']=ex(it.get('e',''))
        opts=[it['a']]+list(it['w']);k=(i+len(it['p']))%4
        order=opts[1:];order.insert(k,opts[0])
        part.page+=1;pg=part.page
        chars=len(it['p'])+sum(len(o) for o in order)
        think=max(12.0,min(26.0,8+0.045*chars))*think_scale;rev=max(8.0,min(14.0,5+0.04*len(it.get('e',''))))
        q1=quiz_png(label,i+1,L,it['p'],order,k,False,'',pg,f'{W}/st/{tag}_{i}_q.png')
        q2=quiz_png(label,i+1,L,it['p'],order,k,True,it.get('e',''),pg,f'{W}/st/{tag}_{i}_r.png')
        part.scene(f'D{tag}_{i+1}',[(q1,fi(think)),(q2,fi(rev))],aud=[(0,bed(fi(think)/FPS+fi(rev)/FPS),1.0)],kind='kore')
        part.slides.append(dict(png=q1,cards=[it['p']]+order,page=pg,title=label,label=label,quiz=True))
        part.qa.append((tag,i+1,it['p'],order,k,it.get('e','')))
def sc_gloss(part,gi,vname):
    S=sents(vname);st=sent_times(vname);vd=vdur(vname);total=fi(LEAD+vd+TAIL)
    terms=[xs(disp(x)) for x in S[2:]];groups=[list(range(0,min(3,len(terms)))),list(range(3,len(terms)))]
    items=[];pgs={}
    for gk,g in enumerate(groups):
        if not g:continue
        part.page+=1;pg=part.page;cards=[terms[j] for j in g]
        for k,j in enumerate(g):
            p=slide_cards('Glossario','Le parole chiave di questa parte',cards,k,pg,None,(),False,f'{W}/st/gl{gi}_{gk}_{k}.png')
            items.append((p,LEAD+st[2+j]))
        part.slides.append(dict(png=slide_cards('Glossario','Le parole chiave di questa parte',cards,-1,pg,None,(),False,f'{W}/st/gl{gi}_{gk}_x.png'),cards=cards,page=pg,title='Glossario',label='Glossario'))
    first=slide_cards('Glossario','Le parole chiave di questa parte',[terms[j] for j in groups[0]],-1,part.slides[-len([g for g in groups if g])]['page'] if False else part.slides[-len([g for g in groups if g])]['page'],None,(),False,f'{W}/st/gl{gi}_0_x.png')
    items.insert(0,(first,0.0))
    part.scene(f'GL{gi}',fill(items,total),aud=[vaud(vname,LEAD)],kind='kore')
    part.sub.append((f'GL{gi}',vname,LEAD))
def sc_final(part,fi_,args,voices,kicker="Storia · L'Italia repubblicana"):
    vd=[vdur(v) for v in voices];off=1.0;t=off;aud=[]
    for v,d in zip(voices,vd):aud.append(vaud(v,t));t+=d+0.5
    spec={"type":"final","kicker":kicker,"l1":"RIEPILOGO","l2":"FINALE","items":[[ARG[i]['nome'],""] for i in args],"sub":"Ripassiamo insieme ciò che abbiamo imparato.","dur":round(t+0.5,2)}
    dark_scene(part,f'RF{fi_}',spec,aud,fps=15)
    part.sub.append((f'RF{fi_}',voices,off))
SIGLA=lambda n:'/home/user/Lezioni/kit/sigle/'+n
def mp4_scene(part,name,mp4,gain=1.0,dissolve=True):
    key=h8('mp4',name,fh(mp4),fh(part.prev) if (part.prev and dissolve) else None);out=f'{CL}/{key}.mp4';last=f'{CL}/{key}.png'
    if not os.path.exists(out):
        inp=['-i',mp4];vf='[0:v]scale=1920:1080:flags=lanczos,fps=30,format=yuv420p,setsar=1[a]'
        if part.prev and dissolve:
            inp+=['-loop','1','-framerate','30','-t','0.5','-i',part.prev];vf+=';[1:v]format=rgba,fade=t=out:st=0:d=0.4:alpha=1[b];[a]format=rgba[a2];[a2][b]overlay=eof_action=pass,format=yuv420p[v]'
        else:vf+=';[a]null[v]'
        run(['ffmpeg','-y','-loglevel','error']+inp+['-filter_complex',vf,'-map','[v]']+ENC+[out+'.t.mp4']);os.rename(out+'.t.mp4',out)
        run(['ffmpeg','-y','-loglevel','error','-sseof','-0.1','-i',out,'-update','1','-frames:v','1',last])
    n=int(run(['ffprobe','-v','error','-count_packets','-select_streams','v:0','-show_entries','stream=nb_read_packets','-of','csv=p=0',out]).stdout)
    t0=part.n/FPS
    au=rdwav(mp4) if subprocess.run(['ffprobe','-v','error','-select_streams','a','-show_entries','stream=index','-of','csv=p=0',mp4],capture_output=True,text=True).stdout.strip() else None
    if au is not None:
        au=au[:int(n/FPS*SR)];part.ev.append((t0,au,gain))
    if part.items and dissolve:part.ev.append((t0-0.8,whoosh(),1.0)) if part.kind!='prof' else None
    part.tl.append([name,round(t0,3),round(n/FPS,3)]);part.items.append(out);part.n+=n;part.prev=last;part.kind='sigla'

def insert_img(wins,a,b,img):
    for i,w in enumerate(wins):
        if w['t0']<=a<w['t1']:
            cs=w['card'];before=[c for c in cs if c['t']<a];act=before[-1] if before else (cs[0] if cs else None)
            L=dict(w,t1=a,card=before);inside=[c for c in cs if a<=c['t']<b];M=dict(w,t0=a,t1=min(b,w['t1']),card=inside if inside else ([dict(act,t=a)] if act else []),img=img)
            R=dict(w,t0=min(b,w['t1']),card=[c for c in cs if c['t']>=b])
            new=([L] if a-w['t0']>=1.0 else [])+[M]+([R] if R['t1']-R['t0']>=1.0 else [])
            wins[i:i+1]=new;return
def do_arg(part,n,first_in_part=False):
    a=ARG[n];d=load_cards(n);ps,pe=ARG_RANGE[n];kw=d['kw']
    label=f'{n:02d} · {a["nome"]}';title=a['prof']
    wins=[dict(w) for w in d['finestre']]
    ce1,cs1=(AN_LIST[n][0][0],AN_LIST[n][0][1]) if AN_LIST[n] else (None,None)
    if n==4:
        pre=[w for w in wins if w['t1']<=2207.8];car=[w for w in wins if 2207.8<=w['t0']<2476.0]
        post=[w for w in wins if w['t0']>=2476.0]
        cw=regroup_img(car,1)
        for w in cw:w['img']=W+'/img/hd_carta.png';w['kw_on']=[2];w['imgmode']='wide'
        cw[-1]['t1']=ce1
        post[0]['t0']=cs1;post[0]['card']=[c for c in post[0]['card'] if c['t']>=cs1-0.01]
        ina=dict(t0=2926.6,t1=pe,kw_on=[3],img=W+'/img/hd_inacasa.png',card=[dict(t=2928.9,testo="Il Piano INA-Casa, cioè il piano per far costruire case, serve a ripartire l'Italia e a costruire le case distrutte dalla guerra."),dict(t=2940.8,testo="Il piano aiuta le famiglie a trovare casa e a uscire da situazioni di fortuna, come grotte, cantine, solai e abitazioni distrutte.")])
        wins=pre+cw+post+[ina]
    if n==5:
        d6=load_cards(6);tail=[c for w in d6['finestre'] for c in w['card'] if 3549.5<=c['t']<pe]
        wins.append(dict(t0=3549.5,t1=pe,kw_on=[],card=tail))
    if n==1:insert_img(wins,848.0,854.6,W+'/img/hd_degasperi.png')
    if n==6:insert_img(wins,3815.0,3816.45,W+'/img/hd_fanfanimoro.png');insert_img(wins,3816.45,3824.6,W+'/img/hd_fanfanimoro.png')
    sc_title(part,n)
    L=AN_LIST[n]
    starts=[ps]+[x[1] for x in L];ends=[x[0] for x in L]+[pe]
    for i in range(len(L)+1):
        seg=clip_windows(wins,starts[i],ends[i])
        prof_piece(part,f'P{n}{"abc"[i]}',seg,kw,label,title)
        if i<len(L):sc_an(part,n,L[i][2],'' if i==0 else 'b')
    if n==3:sc_an(part,3,'AN3a','')
    if n in MAPSET:
        key,vn=MAPSET[n];sc_map(part,n,key,vn)
    sc_pill(part,n)
    sc_quizcard(part,n,f'Quiz {n}',a['nome'],"5 domande · per continuare almeno l'80%")
    sc_quiz_body(part,str(n),f'Quiz · {a["nome"]}',QUIZ[a['Q']]['items'],n)
MAPSET={2:('A',[f'M2_{i:02d}' for i in range(1,9)]),5:('B',[f'M5_{i:02d}' for i in range(1,11)]),6:('C',[f'M6_{i:02d}' for i in range(1,8)])}
def cover_part(part,args_idx,welcome,sigla_name):
    mp4_scene(part,'SIGLA',SIGLA(sigla_name),dissolve=False)
    names=[ARG[i]['nome'] for i in args_idx]
    vd=vdur(welcome);S=sents(welcome);st=sent_times(welcome);total=fi(LEAD+vd+TAIL)
    items=[(cover_png(names,f'{W}/st/cov_{args_idx[0]}_n.png',False,-1),0.0)]
    t1=LEAD+st[1] if len(S)>1 else LEAD+vd/2;t2=LEAD+vd
    for k in range(len(names)):
        items.append((cover_png(names,f'{W}/st/cov_{args_idx[0]}_{k}.png',False,k),t1+(t2-t1)*k/len(names)))
    part.scene('CO',fill(items,total),aud=[vaud(welcome,LEAD)],kind='kore',wmode='before')
    part.sub.append(('CO',welcome,LEAD))
def sc_spiegone(part,k,vname,mapfull=None):
    a=ARG[k];mi=('A',1) if k==2 else None
    voice_cards_scene(part,f'SP{k}',vname,f'Ripasso · {a["nome"]}',a['nome'],mapimg=mi)

import pyloudnorm as pyln
def finalize(part,outname,subtitle=None):
    total=part.n/FPS
    lst=f'{W}/out/{outname}.txt';os.makedirs(W+'/out',exist_ok=True)
    open(lst,'w').write(''.join(f"file '{p}'\n" for p in part.items))
    vid=f'{W}/out/{outname}_v.mp4'
    run(['ffmpeg','-y','-loglevel','error','-f','concat','-safe','0','-i',lst,'-c','copy',vid])
    mix=part.mix(total)
    m=pyln.Meter(SR);L=m.integrated_loudness(mix)
    g=10**((-16.0-L)/20);mix=mix*g
    print('mix LUFS prima',round(L,2),'gain',round(g,3))
    wav=f'{W}/out/{outname}.f32';mix.astype(np.float32).tofile(wav)
    aac=f'{W}/out/{outname}.m4a'
    run(['ffmpeg','-y','-loglevel','error','-f','f32le','-ar','48000','-ac','2','-i',wav,'-af','alimiter=limit=0.8:level=disabled','-c:a','aac','-b:a','192k','-ar','48000',aac])
    final=f'{W}/out/{outname}_1080p.mp4'
    run(['ffmpeg','-y','-loglevel','error','-i',vid,'-i',aac,'-c:v','copy','-c:a','copy','-t',f'{total:.4f}','-movflags','+faststart',final])
    json.dump(part.tl,open(f'{W}/out/timeline_{outname}.json','w'),ensure_ascii=False)
    json.dump(sorted(PROV),open(f'{W}/out/voci_provvisorie_{outname}.json','w'))
    print('FINALE',final,os.path.getsize(final)/1e6,'MB',total/60,'min')
def part1():
    P=Part('1')
    names=[ARG[i]['nome'] for i in (1,2,3)]
    cover_part(P,[1,2,3],'INTRO1_R2','Sigla_Storia_15s.mp4')
    SW=CS(112.97)
    pc=cover_png(names,f'{W}/st/cov_prof.png',True,-1);pa=argomenti_png(names,f'{W}/st/argomenti1.png',2,True)
    a=fi(INTRO_S);m=fi(SW);b=fi(INTRO_E);T0=a/FPS;T1=b/FPS
    P.pm.append(('IN1',T0,T1))
    P.scene('IN1',[(pc,m-a)],cam=a/FPS,aud=[(0,fade(prof_audio(T0,T1)*PGAIN,15),1.0)],kind='prof')
    P.scene('IN2',[(pa,b-m)],cam=m/FPS,kind='prof',whoosh_=False,camfade=False,xin=9)
    P.slides.append(dict(png=pa,cards=names,page=2,title='Di cosa parliamo',label='Di cosa parliamo',noprint=True))
    P.page=2
    for n in (1,2,3):do_arg(P,n)
    sc_gloss(P,1,'GL1')
    sc_final(P,1,(1,2,3),['RF1','FIN1'])
    mp4_scene(P,'FI',SIGLA('Sigla_finale_5s_con_avviso_diritti.mp4'))
    return P
def part2():
    P=Part('2')
    cover_part(P,[4,5,6],'INTRO2_R2','Sigla_Storia_15s.mp4')
    for k in (1,2,3):sc_spiegone(P,k,f'SP2_{k}')
    for n in (4,5,6):do_arg(P,n)
    sc_gloss(P,2,'GL2')
    sc_final(P,2,(4,5,6),['RF2','FIN2'])
    sc_quizcard(P,7,'Verifica finale',"L'Italia repubblicana","10 domande · per continuare almeno l'80%")
    sc_quiz_body(P,'7','Verifica finale',json.load(open(W+'/verifica_finale.json')),7)
    mp4_scene(P,'FI',SIGLA('Sigla_finale_5s_con_avviso_diritti.mp4'))
    # compiti
    spec={"type":"repaso","kicker":"Dopo la videolezione","big":"COMPITI","topic":"Esercitazione","tfs":84,"caps":[],"dur":3.5}
    dark_scene(P,'CINTRO',spec,[(0.1,jingle('titolo'),0.9)])
    comp=[x.strip() for x in re.split(r'\n(?=\d\))',open(W+'/compiti.txt').read().strip())]
    comp=[re.sub(r'\s+',' ',re.sub(r'^\d\)\s*','',c)) for c in comp]
    S=sents('COMPITI');st=sent_times('COMPITI');vd=vdur('COMPITI');total=fi(LEAD+vd+TAIL);items=[]
    for k,c in enumerate(comp):
        P.page+=1
        p=label_slide(f'Compiti · {k+1} di {len(comp)}','Compiti',P.page,f'<div class="card on" style="font-size:38px;line-height:1.5;padding:30px 66px 30px 40px;width:1760px">{H.escape(c)}</div>',f'{W}/st/comp{k}.png',extra='#col{width:1760px}')
        items.append((p,0.0 if k==0 else LEAD+st[2*k]))
        P.slides.append(dict(png=p,cards=[c],page=P.page,title='Compiti',label='Compiti'))
    P.page+=1
    fin='Svolgi i compiti qui sotto e premi Consegna: arrivano al docente nel tuo quaderno dei compiti.'
    p=label_slide('Compiti','Compiti',P.page,f'<div class="card on" style="font-size:40px;line-height:1.5;padding:30px 66px 30px 40px;width:1760px">{H.escape(fin)}</div>',f'{W}/st/comp_fin.png',extra='#col{width:1760px}')
    items.append((p,LEAD+st[len(S)-1]));P.slides.append(dict(png=p,cards=[fin],page=P.page,title='Compiti',label='Compiti'))
    P.scene('COMP',fill(items,total),aud=[vaud('COMPITI',LEAD)],kind='kore')
    P.sub.append(('COMP','COMPITI',LEAD))
    return P
if __name__=='__main__':
    w=sys.argv[1]
    P=part1() if w=='1' else part2()
    finalize(P,f'Storia_Lez18_Parte{w}')
    json.dump(P.slides,open(f'{W}/out/slides_parte{w}.json','w'),ensure_ascii=False,default=str)
    json.dump(P.sub,open(f'{W}/out/sub_parte{w}.json','w'),ensure_ascii=False,default=str)
    json.dump(P.qa,open(f'{W}/out/qa_parte{w}.json','w'),ensure_ascii=False,default=str)
    json.dump(P.vl,open(f'{W}/out/vl_parte{w}.json','w'),ensure_ascii=False,default=str)
    json.dump(P.pm,open(f'{W}/out/pm_parte{w}.json','w'))
