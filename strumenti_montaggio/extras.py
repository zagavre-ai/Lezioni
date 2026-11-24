from lesson import *
import openpyxl, re
def il(t): return esc(t)
# ---------- glossario (due schermate da 4 termini) ----------
GLOS=['LG1','LG2','LG5','LG3','LG4','LG6','LG7','LG8']
def glossario(ctx,n_prefix):
    R_=ctx.rend
    rows=[]
    for nome in GLOS:
        txt=TESTI[nome]
        term,defn=txt.split(': ',1)
        rows.append((f'<b>{esc(term)}:</b> {esc(defn)}',nome))
    for k,(sub,intro) in enumerate([(rows[:4],'LG0'),(rows[4:],None)]):
        out=f'{OUTD}/p{ctx.part}_glos{k}.mkv';png=f'{SL}/glos{k}.png'
        if not os.path.exists(out): lista_scene(R_,f'Glossario · {k+1} di 2',intro,sub,out,png=png,size=42)
        ctx.add(out,'glossario',f'Glossario {k+1}/2',None,png=png,testo=f'Glossario · {k+1} di 2')
RIP=[("Argomento 1 · L'11 settembre 2001 gli attentati di Al-Qaeda aprono l'era dell'angoscia. Bush risponde con la guerra al terrore in Afghanistan e, nel 2003, con la guerra in Iraq.",'R1'),
     ("Argomento 2 · Il Medio Oriente resta instabile tra il conflitto israelo-palestinese e l'ascesa di Hamas. Le primavere arabe fanno cadere vecchi regimi, ma portano guerre civili e l'ascesa dell'ISIS (Stato Islamico).",'R2'),
     ("Argomento 3 · La crisi dei mutui subprime del 2008 provoca una recessione globale. Obama punta su riforme e dialogo, Trump su protezionismo e America First, fino all'assalto a Capitol Hill.",'R3'),
     ("Argomento 4 · Nel mondo multipolare i BRICS (Brasile, Russia, India, Cina, Sudafrica) contestano l'egemonia degli Stati Uniti. La Cina diventa una superpotenza, mentre la Russia di Putin reprime il dissenso e segue una politica estera aggressiva.",'R4'),
     ("Argomenti 5 e 6 · In Europa la crisi porta austerità, euroscetticismo e la Brexit. In Italia, dopo il bipolarismo, arrivano i governi tecnici, i partiti populisti, i governi di unità nazionale e il governo Meloni.",'R5'),
     ("Argomento 7 · La pandemia, la guerra in Ucraina, la crisi climatica e le migrazioni sono le grandi questioni aperte del nostro tempo.",'R6')]
def ripasso_finale(ctx):
    R_=ctx.rend
    for k,(sub,intro) in enumerate([(RIP[:3],'RF1'),(RIP[3:],None)]):
        out=f'{OUTD}/p{ctx.part}_ripf{k}.mkv';png=f'{SL}/ripf{k}.png'
        if not os.path.exists(out): lista_scene(R_,f'Ripasso finale · {k+1} di 2',intro,[(il(t),v) for t,v in sub],out,png=png,size=38)
        ctx.add(out,'ripasso',f'Ripasso finale {k+1}/2',None,png=png,testo=f'Ripasso finale · {k+1} di 2')
def mappa_finale(ctx):
    """le mappe del prof, intere, una dopo l'altra, con la voce della mappa di tutta la lezione"""
    out=f'{OUTD}/p{ctx.part}_mapfin.mkv'
    p,d,txt,_=voce('MF_0')
    order=['M1','M2','M3','M4A','M4B']
    # tempi proporzionali: 1 s di apertura, poi uguali; ultima 4 s
    lead=1.0;seg=max(3.2,(d-lead)/len(order))
    if not os.path.exists(out):
        L=[]
        for k,m in enumerate(order):
            dd=fr(seg) if k<len(order)-1 else fr(seg+4.0)
            L.append(f"file '{SL}/{m}.png'\nduration {dd+(lead if k==0 else 0):.4f}\n")
        L.append(f"file '{SL}/{order[-1]}.png'\n")
        lst=out+'.txt';open(lst,'w').write(''.join(L))
        tot=lead+d+0.2+4.0-lead+lead if False else None
        v=out+'.v.mp4'
        sh(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lst,'-vf','fps=30,scale=1920:1080,format=yuv420p','-r','30','-c:v','libx264','-preset','veryfast','-crf','14',v])
        T=dur(v);a=out+'.a.wav';chime=f'{W}/voc/chime.wav';sp=[(p,0.6,0)]+[(chime,lead+k*seg,-16) for k in range(len(order))]+[(chime,T-3.6,-14)];mix(sp,T,a);mux(v,a,out,T);os.remove(v);os.remove(a)
    ctx.add(out,'mappa',"Mappa finale della lezione",None,png=f'{SL}/M4B.png',testo='Mappa finale della lezione')
def verifica(ctx):
    R_=ctx.rend
    wb=openpyxl.load_workbook('/home/claude/w/src/TEST/DOMANDE LEZIONE 21.xlsx');ws=wb.active
    qs=[]
    for r in ws.iter_rows(min_row=2,values_only=True):
        if r[0]: qs.append(dict(p=str(r[0]).strip(),a=str(r[1]).strip(),w=[str(x).strip() for x in r[2:5]],e=''))
    FIXV=[('seconda guerra del golfo','seconda guerra del Golfo'),('Make America great again','Make America Great Again')]
    SIG=[('MES','MES = Meccanismo europeo di stabilità'),('PNRR','PNRR = Piano nazionale di ripresa e resilienza'),('BRICS','BRICS = Brasile, Russia, India, Cina, Sudafrica'),('ONU','ONU = Organizzazione delle Nazioni Unite')]
    refusi=[]
    for q in qs:
        allt=q['p']+' '+q['a']+' '+' '.join(q['w'])
        for a_,b_ in FIXV:
            if a_ in allt:
                refusi.append((a_,b_)); q['p']=q['p'].replace(a_,b_);q['a']=q['a'].replace(a_,b_);q['w']=[x.replace(a_,b_) for x in q['w']]
        allt=q['p']+' '+q['a']+' '+' '.join(q['w'])
        q['n']='Sigle: '+'; '.join(v for k,v in SIG if re.search(r'\b'+k+r'\b',allt)) if any(re.search(r'\b'+k+r'\b',allt) for k,_ in SIG) else ''
    json.dump(qs,open(f'{W}/verifica.json','w'),ensure_ascii=False,indent=1);json.dump(refusi,open(f'{W}/verifica_refusi.json','w'))
    out=f'{OUTD}/p{ctx.part}_verifica.mkv';png=f'{SL}/verifica.png'
    if not os.path.exists(out):
        quiz_scene(R_,'Verifica di sbarramento','',qs,out,f'Per superare la verifica servono almeno {int(len(qs)*0.8)} risposte giuste su {len(qs)}.',png=png,think=14.0,reveal=4.0,seed=77)
    ctx.add(out,'verifica','Verifica di sbarramento',None,png=png,testo='Verifica di sbarramento')
def compiti(ctx):
    R_=ctx.rend
    out=f'{OUTD}/p{ctx.part}_compi_intro.mkv'
    if not os.path.exists(out):
        p,d,_,_=voce('COMPI')
        items=[dict(id='t',html='<div class=big style="font-size:140px">Compiti</div>',x=160,y=380,t_in=0.2),dict(id='b',html='<div style="width:300px;height:10px;background:#FFE600;border-radius:5px"></div>',x=160,y=600,t_in=0.7)]
        h=dark_page(items);still(R_,h,3.4,f'{SL}/compi_intro.png')
        run_scene(R_,h,3.6,[(JING['titolo'],0.0,-9),(p,0.5,0)],out)
    ctx.add(out,'compiti','Compiti · intro',None,png=f'{SL}/compi_intro.png',testo='Compiti')
    out=f'{OUTD}/p{ctx.part}_compiti.mkv';png=f'{SL}/compiti.png'
    q=json.load(open(f'{W}/compiti_prof.json'))
    p,d,txt,_=voce('COMPITI')
    f,tm=tempi_frasi('COMPITI',txt,d)
    cards=[f'<b>Compito {k+1}:</b> {esc(q[k])}' for k in range(4)]+['<b>Svolgi i compiti qui sotto e premi Consegna:</b> arrivano al docente nel tuo quaderno dei compiti.']
    items=[dict(id='k',html='<div class=k2>Compiti</div>',x=120,y=50,t_in=0.3,w=1700)];act=[];lead=0.8
    for i_,c_ in enumerate(cards):
        a_,b_=tm[min(i_,len(tm)-1)]
        items.append(dict(id=f'L{i_}',html=f'<div class=line style="font-size:36px;line-height:1.38;padding:12px 30px 12px 62px"><span class=dot style="top:24px"></span>{c_}</div>',x=120,y=0,w=1690,t_in=lead+a_-0.15))
        act.append((f'L{i_}',lead+a_-0.15,lead+b_+0.2))
    tot=lead+d+1.5
    js='var yy=110;for(var i=0;i<%d;i++){var e=document.getElementById("L"+i);e.style.top=yy+"px";yy+=e.offsetHeight+14;}'%len(cards)
    h=dark_page(items,extra_js=act_js(act)).replace('function render(t){',f'function render(t){{{js}',1)
    if not os.path.exists(out): still(R_,h,tot,png);run_scene(R_,h,tot,[(p,lead,0)],out)
    elif not os.path.exists(png): still(R_,h,tot,png)
    ctx.add(out,'compiti','Compiti',None,png=png,testo='Compiti')
def spiegone(ctx):
    """ripasso animato (voce Kore) di tutta la Parte precedente: foto, schermate e mappe"""
    R_=ctx.rend
    blocks=[('SP_0',[]),
            ('SP_1',[('photo','wtc+bush')]),
            ('SP_2',[('photo','gheddafi+siria'),('map','M3')]),
            ('SP_3',[('photo','obama+trump'),('map','M1')])]
    for k,(vn,shots) in enumerate(blocks):
        out=f'{OUTD}/p{ctx.part}_spieg{k}.mkv';png=f'{SL}/spieg{k}.png'
        p,d,_,_=voce(vn)
        if k==0:
            if not os.path.exists(out):
                items=[dict(id='k',html='<div class=k2>Storia V</div>',x=160,y=330,t_in=0.4),dict(id='t',html='<div class=big style="width:1600px">Ripasso della prima parte</div>',x=160,y=395,t_in=0.7)]
                h=dark_page(items);still(R_,h,d+1,png);run_scene(R_,h,d+1.2,[(p,0.5,0)],out)
            ctx.add(out,'spiegone','Spiegone · apertura',None,png=png,testo='Ripasso della prima parte');continue
        if not os.path.exists(out):
            pngs=[]
            for s in shots:
                f=f'{SL}/sp{k}_{"_".join(s[1:]).replace("+","-")}.png'
                if s[0]=='map': f=f'{SL}/{s[1]}.png'
                else:
                    ks=s[2].split('+') if s[0]=='win' else s[1].split('+')
                    ph=[(img_uri(x),)+img_size(x) for x in ks]
                    R_.load(slide_html(f'Ripasso · Argomento {k}',ARG[k-1]['slide'] if k<=4 else '',None,None,None,0,photos=ph,cap=' · '.join(CAP[x].split('.')[0] for x in ks),prof=False)
                            .replace('Pagina 0','').replace('<div class=pag>','<div class=pag style="display:none">'))
                    R_.shot(f)
                pngs.append(f)
            T=d+1.4;part=T/len(pngs);L=''
            for f in pngs: L+=f"file '{f}'\nduration {fr(part):.4f}\n"
            L+=f"file '{pngs[-1]}'\n";lst=out+'.txt';open(lst,'w').write(L)
            v=out+'.v.mp4'
            sh(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lst,'-vf','fps=30,scale=1920:1080,format=yuv420p','-r','30','-t',f'{fr(T):.3f}','-c:v','libx264','-preset','veryfast','-crf','14',v])
            T2=dur(v);a=out+'.a.wav';mix([(p,0.6,0)],T2,a);mux(v,a,out,T2);os.remove(v);os.remove(a)
            sh(['ffmpeg','-v','error','-y','-i',out,'-vf','select=eq(n\\,15)','-frames:v','1',png])
        ctx.add(out,'spiegone',f'Spiegone · argomento {k}',None,png=png,testo=f'Ripasso · argomento {k}')
def fine_parte(ctx,voce_nome,etichetta):
    R_=ctx.rend
    p,d,_,_=voce(voce_nome)
    out=f'{OUTD}/p{ctx.part}_fine.mkv';png=f'{SL}/fine{ctx.part}.png'
    if not os.path.exists(out):
        items=[dict(id='k',html=f'<div class=k2>Storia V</div>',x=160,y=330,t_in=0.4),dict(id='t',html=f'<div class=big style="width:1600px">{esc(etichetta)}</div>',x=160,y=395,t_in=0.7)]
        h=dark_page(items);still(R_,h,d+1,png);run_scene(R_,h,d+1.8,[(p,0.6,0)],out)
    ctx.add(out,'fine',etichetta,None,png=png,testo=etichetta)
