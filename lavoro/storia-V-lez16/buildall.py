from kore import *
import sys,hashlib
from teacher import build_teacher
FORCE=os.environ.get('FORCE','')
VC=[];TL=[];PREV={'png':None};NUMS={'n':0,'k':{}}
def numbering(k):
    if k not in NUMS['k']:NUMS['n']+=1;NUMS['k'][k]=NUMS['n']
    return NUMS['k'][k]
def pm(p):
    import hashlib
    return hashlib.md5(open(p,'rb').read()).hexdigest() if p and os.path.exists(p) else None
def cached(nome,key,fn):
    kf=f'{OUT}/{nome}.key';o=f'{OUT}/{nome}.mkv'
    kk=hashlib.md5(json.dumps(key,default=str).encode()).hexdigest()
    if not FORCE and os.path.exists(o) and os.path.exists(kf) and open(kf).read()==kk:return o,dur(o)
    r=fn();open(kf,'w').write(kk);return r
def reg(nome,o,d,prov=False):
    TL.append([nome,o,d,prov]);PREV['png']=last_frame(o,f'{B}/png/last_{nome}.png')
def vc_sent(nome,off,S_,st_,vd):
    for i,x in enumerate(S_):
        a=off+st_[i];b=off+(st_[i+1] if i+1<len(S_) else vd)
        VC.append([nome,round(a,3),round(b,3),screen(x)])
def vc_one(nome,off,vd,text):VC.append([nome,round(off,3),round(off+vd,3),screen(text)])
def key_voice(*names):
    return [(n,(os.path.getmtime(real(n)) if real(n) else 0)) for n in names]
# ---------------- pezzi ----------------
def p_kit(nome,mp4):
    o=f'{OUT}/{nome}.mkv'
    if not os.path.exists(o):sh(['ffmpeg','-v','error','-y','-i',mp4,'-vf','fps=30,scale=1920:1080,format=yuv420p']+V_ENC+['-c:a','pcm_s16le','-ar','48000','-ac','2',o])
    reg(nome,o,dur(o))
def p_teacher(ch):
    key=[ch,pm(PREV['png']),'cam-v2']
    o,d=cached(ch['nome'],key,lambda:build_teacher(ch,PREV['png'],numbering))
    # il numero di pagina va comunque registrato anche se il pezzo e' in cache
    reg(ch['nome'],o,d)
def blue_piece(nome,inner_states,D,sfx,audios,vk=()):
    ensure_blu_bg();flush()
    key=[nome,inner_states,D,sfx,audios,vk,pm(PREV['png'])]
    o,d=cached(nome,key,lambda:compose(nome,inner_states,audios,D,PREV['png'],blue=True,sfx=sfx))
    return o,d
def p_titolo(a):
    n=a['n'];st=[(0,png(blu_title(n,7,a['nome']),f'T{n}',True))];flush()
    o,d=blue_piece(f'T{n}',st,4.0,[(0.0,SND+'titolo.wav')],[]);reg(f'T{n}',o,d)
def p_pillola(a,pname):
    n=a['n'];txt=TEXTS[pname];vn=vname(pname);w,vd,prov=prepare(vn,txt)
    D=LEAD+vd+1.4;st=[(0,png(blu_pill(a['nome']),f'PI{n}',True))];flush()
    o,d=blue_piece(f'PI{n}',st,D,[(0.0,SND+'repaso.wav')],[(1.7,w)],key_voice(vn));reg(f'PI{n}',o,d,prov);vc_one(f'PI{n}',1.7,vd,txt)
def p_quiz(a):
    n=a['n'];st=[(0,png(blu_quiz(n,a['nome']),f'Q{n}',True))];flush()
    o,d=blue_piece(f'Q{n}',st,5.0,[(0.5,SND+'quiz.wav')],[]);reg(f'Q{n}',o,d)
def white_piece(nome,states,audios,D,vk,prov,sfx=None):
    flush()
    key=[nome,states,audios,D,vk,pm(PREV['png']),sfx]
    o,d=cached(nome,key,lambda:compose(nome,states,audios,D,PREV['png'],sfx=sfx));reg(nome,o,d,prov);return o,d
def p_ap(a,name,label):
    vn=vname(name);txt=TEXTS[vn if vn in TEXTS else name];S_=sentences(txt)
    w,vd,prov=prepare(vn,txt);st_,vd,prov=starts(vn,txt,S_)
    q=S_[0];cards=[dict(t=screen(s)) for s in S_[1:]]
    eb=f"APPROFONDIMENTO · {a['n']:02d} {a['nome']}" if a else label
    tl=2 if len(q)>62 else 1
    states=[(0,png(wslide(eb,q,[],None,numbering(('ap',name,0)),tl=tl),'ap'))]
    for j in range(1,len(S_)):
        wi=(j-1)//3;pg=numbering(('ap',name,wi));shown=cards[wi*3:j]
        states.append((LEAD+st_[j],png(wslide(eb,q,shown,len(shown)-1,pg,tl=tl),'ap')))
    # fotogramma finale della finestra per la dispensa: tutte le card, nessuna accesa
    D=LEAD+vd+TAIL
    white_piece(f'AP{label_key(name)}',states,[(LEAD,w)],D,key_voice(vn),prov);vc_sent(f'AP{label_key(name)}',LEAD,S_,st_,vd)
def label_key(name):return name[2:] if name.startswith('AP') else name
def p_ps(a,names):
    n=a['n'];ws=[];lines=[];tt=[]
    for nm in names:
        vn=vname(nm);txt=TEXTS[vn if vn in TEXTS else nm];w,vd,prov=prepare(vn,txt);ws.append((w,vd,prov,vn));lines.append(screen(txt))
    pg=numbering(('ps',n));eb=f"SCHEMA DI RIPASSO · {n:02d} {a['nome']}"
    states=[(0,png(blu_schema(eb,a['nome'],lines,None),'psb',True))]
    aud=[];t=LEAD;prov_any=False;vtmp=[]
    for i,(w,vd,prov,vn) in enumerate(ws):
        states.append((t,png(blu_schema(eb,a['nome'],lines,i),'psb',True)));aud.append((t,w));vtmp.append((t,vd,lines[i]));t+=vd+0.5;prov_any|=prov
    D=t+TAIL-0.5;flush()
    o,d=blue_piece(f'PS{n}',states,D,[],aud,key_voice(*[x[3] for x in ws]));reg(f'PS{n}',o,d,prov_any)
    for (tt_,vd_,tx_) in vtmp:vc_one(f'PS{n}',tt_,vd_,tx_)
def p_map(k):
    m=MAPS[k-1];nm=f'MD{k}';vn=vname(nm);txt=TEXTS[vn];S_=sentences(txt);w,vd,prov=prepare(vn,txt);st_,vd,prov=starts(vn,txt,S_)
    nodes=[x[0] for x in map_nodes(m)];assert len(S_)==len(nodes)+1,(nm,len(S_),len(nodes))
    pg=numbering(('map',k));shown=set();states=[(0,png(map_html(m,set(),None,pg),'map'))]
    for i,nd in enumerate(nodes):
        shown.add(nd);states.append((LEAD+st_[i+1],png(map_html(m,set(shown),nd,pg),'map')))
    t_end=LEAD+vd+0.4;states.append((t_end,png(map_html(m,set(shown),None,pg),'map')))
    D=t_end+4.0
    white_piece(f'MAP{k}',states,[(LEAD,w)],D,key_voice(vn),prov,sfx=[(t_end,SND+'titolo.wav')]);vc_sent(f'MAP{k}',LEAD,S_,st_,vd)
def p_cover(teacher=False):
    pg=numbering('cover');vn=vname('BENV1');txt=TEXTS[vn];w,vd,prov=prepare(vn,txt)
    states=[(0,png(cover(["Gli anni Sessanta","tra crisi e progressi"],[x['nome'] for x in ARGS],False,pg),'cover_n'))]
    white_piece('COVERV',states,[(LEAD,w)],LEAD+vd+1.5,key_voice(vn),prov);vc_one('COVERV',LEAD,vd,txt)
def p_indice():
    vn=vname('DCP1');txt=TEXTS[vn];S_=sentences(txt);w,vd,prov=prepare(vn,txt);st_,vd,prov=starts(vn,txt,S_)
    pg=numbering('indice');css=".card{padding-top:6px;padding-bottom:6px;line-height:56px}.card .n{top:6px}.card.lit{padding-top:4px;padding-bottom:4px}"
    rows=[dict(t=a['nome']) for a in ARGS]
    states=[(0,png(wslide('Videolezione','Di cosa parliamo',[],None,pg,extra_css=css),'idx'))]
    for i in range(len(rows)):
        states.append((LEAD+st_[i+1],png(wslide('Videolezione','Di cosa parliamo',rows,i,pg,extra_css=css),'idx')))
    white_piece('ARGS',states,[(LEAD,w)],LEAD+vd+TAIL,key_voice(vn),prov);vc_sent('ARGS',LEAD,S_,st_,vd)
def p_glossario():
    vn=vname('GL1');txt=TEXTS[vn];S_=sentences(txt);w,vd,prov=prepare(vn,txt);st_,vd,prov=starts(vn,txt,S_)
    terms=[]
    for s in S_[1:]:
        l,_,r=s.partition(':');terms.append(dict(l=l.strip(),t=screen(r.strip())))
    states=[(0,png(wslide('Glossario','Le parole chiave della lezione',[],None,numbering(('gl',0))),'gl'))]
    for j in range(len(terms)):
        wi=j//3;pg=numbering(('gl',wi));shown=terms[wi*3:j+1]
        states.append((LEAD+st_[j+1],png(wslide('Glossario','Le parole chiave della lezione',shown,len(shown)-1,pg),'gl')))
    white_piece('GL',states,[(LEAD,w)],LEAD+vd+TAIL,key_voice(vn),prov);vc_sent('GL',LEAD,S_,st_,vd)
def p_riep():
    righe=[(a['n'],a['nome']) for a in ARGS];t=LEAD;states=[];aud=[];prov_any=False;ks=[];vr=[]
    for i in range(7):
        nm=f'R{i+1}';vn=vname(nm);txt=TEXTS[vn];w,vd,prov=prepare(vn,txt);prov_any|=prov;ks.append(vn)
        body=screen(txt.replace('Ripassiamo.','').strip())
        states.append((t,png(blu_rows('Ripasso finale','RIEPILOGO',righe,i,body),'rie',True)));aud.append((t,w));vr.append((t,vd,txt));t+=vd+0.6
    vn=vname('RF1');txt=TEXTS[vn];w,vd,prov=prepare(vn,txt);prov_any|=prov;ks.append(vn)
    states.append((t,png(blu_rows('Ripasso finale','RIEPILOGO',righe,None,screen(txt.replace('Ripasso finale.','').strip())),'rie',True)));aud.append((t,w));vr.append((t,vd,txt));t+=vd+0.6
    vn=vname('FIN1');txt=TEXTS[vn];w,vd,prov=prepare(vn,txt);prov_any|=prov;ks.append(vn)
    states.append((t,png(blu_text('PER OGGI È TUTTO','Mettiti alla prova','Verifica finale e compiti'),'rie',True)));aud.append((t,w));vr.append((t,vd,txt));t+=vd+1.0
    st0=[(0,states[0][1])]+states;st0[0]=(0,png(blu_rows('Ripasso finale','RIEPILOGO',righe,None,None),'rie',True))
    flush()
    o,d=blue_piece('RIEP',[(0,st0[0][1])]+states,t,[],aud,key_voice(*ks));reg('RIEP',o,d,prov_any)
    for tt_,vd_,tx_ in vr:vc_one('RIEP',tt_,vd_,tx_)
def p_verifica():
    vn=vname('VER1');txt=TEXTS[vn];w,vd,prov=prepare(vn,txt)
    st=[(0,png(blu_text('PAUSA DEL VIDEO','Verifica finale','Serve almeno l\'80% per continuare'),'ver',True))];flush()
    o,d=blue_piece('VER',st,LEAD+vd+2.0,[(0.5,SND+'quiz.wav')],[(1.2,w)],key_voice(vn));reg('VER',o,d,prov);vc_one('VER',1.2,vd,txt)
def p_compiti():
    vn='COMPI';txt=TEXTS[vn];w,vd,prov=prepare(vn,txt)
    st=[(0,png(blu_text('E ORA TOCCA A TE','Compiti'),'comp',True))];flush()
    o,d=blue_piece('COMPI',st,3.5,[(0.0,SND+'titolo.wav')],[(0.5,w)],key_voice(vn));reg('COMPI',o,d,prov);vc_one('COMPI',0.5,vd,txt)
    cs=json.load(open(W+'/compiti.json'))['compiti'] if os.path.exists(W+'/compiti.json') else None
    C=[dict(t=c) for c in COMPITI]
    ws=[];t=LEAD;states=[];aud=[];pa=False;ks=[];vco=[]
    css=".card{line-height:56px}"
    for i in range(4):
        vn=vname(f'CO{i+1}');txt=TEXTS[vn];w,vd,prov=prepare(vn,txt);pa|=prov;ks.append(vn)
        wi=i//2;pg=numbering(('co',wi));shown=C[wi*2:i+1]
        states.append((t,png(wslide('Compiti del prof','Compiti',shown,len(shown)-1,pg,extra_css=css),'co')));aud.append((t,w));vco.append((t,vd,txt));t+=vd+0.8
    states=[(0,png(wslide('Compiti del prof','Compiti',[],None,numbering(('co',0))),'co'))]+states
    white_piece('CO',states,aud,t+TAIL,key_voice(*ks),pa)
    for tt_,vd_,tx_ in vco:vc_one('CO',tt_,vd_,tx_)
COMPITI=["Quali fattori economici favorirono l'età del benessere nei paesi occidentali durante gli anni Sessanta e quali furono le principali trasformazioni sociali e demografiche che ne derivarono?",
"Quali furono gli obiettivi principali del programma della «Nuova Frontiera» di John F. Kennedy e quali leggi fondamentali vennero approvate durante la presidenza di Lyndon Johnson per tutelare i diritti civili della popolazione afroamericana?",
"Quali furono i principali momenti di tensione della guerra fredda nel corso degli anni Sessanta e come si sviluppò il confronto tra Stati Uniti e Unione Sovietica nella corsa allo spazio?",
"Contro quali aspetti della società insorsero i movimenti di contestazione del Sessantotto, quali furono le principali rivendicazioni del movimento femminista e quale fu il bilancio storico di queste proteste?"]
PSN={1:['SC1_1','SC1_2','SC1_3','SC1_4','SC1_5'],2:['SC2_1','SC2_2','SC2_3','SC2_4'],3:['SC3_1','SC3_2','SC3_3','SC3_4'],4:['SC4_1','SC4_2','SC4_3','SC4_4'],5:['SC5_1','SC5_2','SC5_3','RV5_4'],6:['SC6_1','SC6_2','SC6_3','SC6_4'],7:['SC7_1','SC7_2','SC7_3','SC7_4']}
def main(upto=None):
    p_kit('SIGLA','/home/user/Lezioni/kit/sigle/Sigla_Storia_15s.mp4')
    p_cover()
    ch={c['nome']:c for c in CH}
    p_teacher(ch['D0']);p_indice()
    for a in ARGS:
        n=a['n'];p_titolo(a)
        for nm in [k for k in ch if k.startswith(f'D{n}')]:
            p_teacher(ch[nm])
            if nm=='D2a':p_ap(ARGS[1],'AP2A','2A')
            if nm=='D3a':p_ap(ARGS[2],'AP3A','3A')
            if nm=='D5a':p_ap(ARGS[4],'AP5A','5A')
        p_ap(a,f'AP{n}',str(n))
        if n==6:p_map(2);p_map(3)
        if n==7:p_map(1)
        p_pillola(a,f'P{n}');p_ps(a,PSN[n]);p_quiz(a)
    p_glossario();p_riep();p_verifica();p_kit('FINALE','/home/user/Lezioni/kit/sigle/Sigla_finale_5s_con_avviso_diritti.mp4');p_compiti()
    # timeline
    t=0.0;rows=[]
    for nome,o,d,prov in TL:rows.append([nome,round(t,3),round(d,3)]);t+=d
    json.dump(rows,open(W+'/out/timeline_edit.json','w'));json.dump([[n,o,d,p] for n,o,d,p in TL],open(W+'/out/pieces.json','w'))
    open(W+'/out/concat.txt','w').write(''.join(f"file '{o}'\n" for n,o,d,p in TL))
    json.dump({str(k):v for k,v in NUMS['k'].items()},open(W+'/out/pagine.json','w'),default=str);json.dump(VC,open(W+'/out/vc.json','w'),ensure_ascii=False)
    print('pezzi',len(TL),'durata totale %.1f s = %d:%04.1f'%(t,t//60,t%60),'| provvisorie:',[n for n,o,d,p in TL if p])
if __name__=='__main__':main()
