from assemble import *
QUIZ=json.load(open('/home/user/Lezioni/scambio/storia-V-lez21/quiz.json'))
def _it(p,a,w,e): return dict(p=p,a=a,w=w,e=e)
NUOVE5=[_it("Che cosa porta la crisi del 2008 nei paesi europei?","Severe politiche di austerità",["Una forte crescita economica","La nascita dell'euro","L'uscita della Grecia dalla NATO"],"La crisi del 2008 colpisce duramente i paesi europei, portando a severe politiche di austerità."),
        _it("Quale cancelliera guida la Germania per anni?","Angela Merkel",["Emmanuel Macron","Giorgia Meloni","Anna Politkovskaja"],"La Germania è guidata per anni dalla stabilità di Angela Merkel.")]
NUOVE6=[_it("Quali governi si alternano in Italia nei primi anni Duemila?","Centrodestra di Berlusconi e centrosinistra di Prodi",["Solo governi tecnici","Governi militari","Governi di unità nazionale"],"I primi anni Duemila sono segnati dal bipolarismo e dall'alternanza tra centrodestra e centrosinistra."),
        _it("Quali forze politiche si impongono alle elezioni del 2018?","Il Movimento 5 Stelle e la Lega",["Il governo Monti e il governo Letta","Solo Fratelli d'Italia","Il centrosinistra di Prodi"],"Alle elezioni del 2018 si impongono il Movimento 5 Stelle e la Lega, intercettando il forte dissenso popolare."),
        _it("Quale governo di unità nazionale guida l'Italia durante la pandemia, dopo il secondo governo Conte?","Il governo Draghi",["Il governo Renzi","Il governo Monti","Il governo Meloni"],"Durante la pandemia si formano governi di coalizione allargata, tra cui il secondo governo Conte e il governo Draghi.")]
QZ={1:QUIZ['Q1']['items'][:5],2:QUIZ['Q2']['items'][:5],3:QUIZ['Q3']['items'][:5],4:QUIZ['Q4']['items'][:5],
    5:QUIZ['Q5']['items'][:3]+NUOVE5,6:QUIZ['Q5']['items'][3:5]+NUOVE6,7:QUIZ['Q6']['items'][:5]}
MAPS_ARG={1:[],2:['M3'],3:['M1'],4:['M2'],5:[],6:['M4A','M4B'],7:[]}
SCN={1:['SC1_1','SC1_2','SC1_3','SC1_4'],2:['SC2_1','SC2_2','SC2_3','SC2_4','SC2_5'],3:['SC3_1','SC3_2','SC3_3','SC3_4'],4:['SC4_1','SC4_2','SC4_3','SC4_4'],
     5:['SC5_1','SC5_2','SC5_3','SC5_4'],6:['SC6_1','SC6_2','SC6_3','SC6_4','SC6_5'],7:['SC7_1','SC7_2','SC7_3','SC7_4']}
APFOTO={'AP1_1':'bush','AP2_0':'gheddafi','AP3_3':'obama','AP3_1':'trump','AP4_0':'putin','AP6_1':'renzi'}
FORCE={'AP2_0':156,'AP3_1':247}
def ap_cuts(a,B):
    cuts=[]
    kept=set(B['sl'])
    for (v,t) in a['ap']:
        c=[i for i in B['sl'] if SEGS[i]['fine']>=t-0.01 and valid_cut(i)]
        i=FORCE.get(v,c[0]);iv=[x for x in B['iv'] if x[0]<=SEGS[i]['fine']<=x[1]][0]
        to=min(SEGS[i]['fine']+0.35,iv[1])
        cuts.append((v,i,to,fr(o2c(B,to))))
    return cuts
def build_arg(ctx,a,quiz_think=9.0):
    n=a['n'];R_=ctx.rend;kick=f"Argomento {n} · {a['tit']}"
    # 1) scheda titolo
    out=f'{OUTD}/p{ctx.part}_titolo{n}.mkv'
    if not os.path.exists(out): titolo_scene(R_,n,a['tit'],out,png=f'{SL}/titolo{n}.png')
    ctx.add(out,'titolo',f'Argomento {n} · {a["tit"]}',n,png=f'{SL}/titolo{n}.png',testo=f'Argomento {n}: {a["tit"]}')
    # 2) pezzi del prof + approfondimenti
    B=snap(build(a));cam,aud=extract_arg(f'a{n}',B);wins,m=windows(R_,a)
    cuts=ap_cuts(a,B)
    pts={B['iv'][0][0],B['iv'][-1][1]}
    for c,s in a['cards']:
        if s is not None and pts and B['iv'][0][0]<s<B['iv'][-1][1]: pts.add(s)
    for k,x,y in a['photos']:
        for v in (x,y):
            if B['iv'][0][0]<v<B['iv'][-1][1]: pts.add(v)
    for v,i,to,c in cuts: pts.add(to)
    pts=sorted(pts);states=[]
    for p,q in zip(pts,pts[1:]):
        c0=fr(o2c(B,p));c1=fr(o2c(B,q))
        if c1-c0<1/30-1e-6: continue
        k=key_at(a,wins,(p+q)/2)
        if states and states[-1][2]==k: states[-1][1]=c1
        else: states.append([c0,c1,k])
    states[0][0]=0.0;states[-1][1]=fr(B['dur'])
    bounds=[0.0]+[c for _,_,_,c in cuts]+[fr(B['dur'])]
    for pi in range(len(bounds)-1):
        c0,c1=bounds[pi],bounds[pi+1]
        sts=[]
        for s0,s1,k in states:
            a0=max(s0,c0);a1=min(s1,c1)
            if a1-a0>=1/30-1e-6:
                png=f'{SL}/a{n}_{"_".join(map(str,k))}.png'
                pk=(n,k[0],k[1])
                if pk not in ctx.pagemap:
                    dp=f'{SL}/a{n}_win_{k[1]}_None.png' if k[0]=='win' else png
                    pg=ctx.dpage(dp,a['slide'] if k[0]=='win' else a['slide']+' · immagine',pk)
                    render_key(R_,a,wins,('win',k[1],None) if k[0]=='win' else k,pg,dp)
                pg=ctx.pagemap[pk]
                render_key(R_,a,wins,k,pg,png)
                sts.append((a0,a1,png))
        sts[0]=(c0,sts[0][1],sts[0][2]);sts[-1]=(sts[-1][0],c1,sts[-1][2])
        # tutte le card/foto distinte come pagine per la dispensa
        out=f'{OUTD}/p{ctx.part}_a{n}_{pi}.mkv'
        if not os.path.exists(out): make_piece(f'a{n}',cam,aud,c0,c1,sts,out)
        ctx.add(out,'prof',f'{a["tit"]} · docente ({pi+1})',n,anim=False)
        if pi<len(cuts):
            v=cuts[pi][0];out=f'{OUTD}/p{ctx.part}_{v}.mkv'
            png=f'{SL}/{v}.png';pg=ctx.dpage(png,f'Approfondimento · {a["tit"]}',(v,))
            if not os.path.exists(out): ap_scene(R_,v,f'Argomento {n} · Approfondimento',a['slide'],out,pg,APFOTO.get(v),png=png)
            ctx.add(out,'approfondimento',f'Approfondimento {v}',n)
    # 3) mappe
    for mk in MAPS_ARG[n]:
        out=f'{OUTD}/p{ctx.part}_{mk}.mkv';png=f'{SL}/{mk}.png'
        if not os.path.exists(out): build_map(R_,MAPS[mk],out,png)
        elif not os.path.exists(png): build_map(R_,MAPS[mk],None,png)
        ctx.add(out,'mappa',f'Mappa · {MAPS[mk]["kick"]}',n,png=png,testo=MAPS[mk]['kick'])
    # 4) pillola di ripasso
    out=f'{OUTD}/p{ctx.part}_pill{n}.mkv';png=f'{SL}/pill{n}.png'
    if not os.path.exists(out): pillola_scene(R_,n,a['tit'],f'PI{n}',SCN[n],out,png=png)
    ctx.add(out,'pillola',f'Ripasso · {a["tit"]}',n,png=png,testo=f'Ripasso · {a["tit"]}')
    # 5) quiz
    q=dict(items=QZ[n]);out=f'{OUTD}/p{ctx.part}_quiz{n}.mkv';png=f'{SL}/quiz{n}.png'
    if not os.path.exists(out): quiz_scene(R_,f'Quiz · {a["tit"]}','',q['items'],out,'Per continuare servono almeno 4 risposte giuste su 5.',png=png,think=quiz_think,seed=n)
    ctx.add(out,'quiz',f'Quiz · {a["tit"]}',n,png=png,testo=f'Quiz · {a["tit"]}')
Ctx.rerender=False
