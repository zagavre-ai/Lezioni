import sys;sys.path.insert(0,'/home/claude/w19/lib')
from piano import *
from parte1 import cues,imgs,S,E_
def s_spiegone():
    tit=frasi(TV['RIP2A'])
    html='<div class="dk">'+logo()
    html+=T(0.2,'RIPASSO DELLA PRIMA PARTE','position:absolute;left:140px;top:150px;font:800 30px Figtree;letter-spacing:.22em;color:#FFE600')
    ev=[(VX+'RIP2A.wav',1.0,0)];t=1.0+vd('RIP2A')+0.6
    html+=T(0.3,'Che cosa abbiamo visto',"position:absolute;left:140px;top:200px;width:1640px;font:800 62px/1.1 'Bricolage Grotesque'",extra=f'data-out="{t-0.2:.2f}"')
    foto={1:None,2:'operai',3:'MAP1',4:'MAP2'}
    for k in range(1,5):
        v=f'R{k}';d=vd(v);fr=[cifre(x) for x in frasi(TV[v])][1:]
        tm=tempi_frasi(fr,t+0.3,d-0.3);ev.append((VX+v+'.wav',t,0));t1=t+d+0.6
        f=foto[k];w=1100 if f else 1640
        html+=T(t-0.1,f'{k} · {viste.ARGT[k]}',"position:absolute;left:140px;top:200px;width:1640px;font:800 56px/1.1 'Bricolage Grotesque'",extra=f'data-out="{t1-0.2:.2f}"')
        html+=f'<div style="position:absolute;left:140px;top:340px;width:{w}px;display:flex;flex-direction:column;gap:14px">'
        for x,(a,b) in zip(fr,tm):
            html+=(f'<div data-t0="{a-0.1:.2f}" data-t1="{b+0.2:.2f}" data-out="{t1-0.2:.2f}" style="opacity:0;box-sizing:border-box;padding:12px 28px;border-radius:16px;background:rgba(255,255,255,.08);border-left:10px solid #FFE600;font:600 38px/1.3 Figtree">{x}</div>')
        html+='</div>'
        if f and f.startswith('MAP'): html+=T(t,f'<img src="file://{O}map{f[3]}.png" style="width:560px;border-radius:12px;box-shadow:0 14px 34px rgba(0,0,0,.4)">','position:absolute;left:1260px;top:340px;width:560px',extra=f'data-out="{t1-0.2:.2f}"')
        elif f: html+=T(t,f'<img src="file:///home/claude/w19/foto/{f}.png" style="max-width:520px;max-height:620px;border-radius:14px;box-shadow:0 14px 34px rgba(0,0,0,.4)">','position:absolute;left:1280px;top:340px;width:520px',extra=f'data-out="{t1-0.2:.2f}"')
        t=t1+0.3
    return render_scene('spiegone',html+'</div>',round(t+0.4,2)),ev
def run2():
    r=Run('p2')
    r.clip('sigla2',KIT+'/sigle/Sigla_Storia_15s.mp4',tipo='sigla')
    r.scena('spiegone',s_spiegone(),'spiegone')
    r.pg=int(open(W+'/pg_fine_p1.txt').read())
    def arg(n,pezzi,mapk=None):
        r.scena(f't{n}',s_titolo(n),'titolo',arg=n)
        for p in pezzi:
            if p[0]=='P': _,pid,a,bb,cu,im,co,*dr=p;r.prof(pid,a,bb,cues(cu),imgs(im),n,co,drop=dr[0] if dr else ())
            elif p[0]=='AN': r.scena(p[1],s_an(p[1],p[2]),'approfondimento',arg=n)
        if mapk: r.scena(f'map{mapk}',s_mappa(mapk),'mappa',arg=n)
        r.scena(f'sch{n}',s_schema(n),'ripasso',arg=n)
        r.scena(f'q{n}',s_quiz(n),'quiz',arg=n)
    C5={8:[0,1,2,3],9:[0,1,2,3,4]};C6={10:[0,1,2,3],12:[0,1,2,3]};C7={14:[0,1,2,3]};C8={17:[0,1,2,3]}
    arg(5,[('P','a5a',387,406,[(387,8,0),(388,8,3),(391,8,1),(394,8,2)],[],C5),
           ('AN','an5_5',[('AN5',None,None)]),
           ('P','a5b',407,418,[(407,8,2),(411,9,0),(415,9,1)],[],C5),
           ('P','a5c',419,432,[(419,9,2),(421,9,3),(427,9,4)],[],C5),
           ('AN','an5_6_7',[('AN6',None,None),('AN7',None,None)]),
           ('P','a5d',433,441,[(433,9,4)],[],C5)])
    arg(6,[('P','a6a',442,468,[(442,10,0),(461,10,1)],[(461,468,'marcia')],C6),
           ('AN','an6_8',[('AN8','marcia',None)]),
           ('P','a6c',469,517,[(469,10,0),(485,12,0),(497,12,1),(507,12,3)],[(497,501,'craxi')],C6),
           ('AN','an6_9',[('AN9','craxi',None)]),
           ('P','a6d',519,583,[(519,12,3),(544,10,0),(545,10,2),(546,12,2),(566,10,2),(568,10,3)],[],C6,{523,524})])
    arg(7,[('P','a7a',584,647,[(584,14,0),(609,14,1),(635,14,3)],[(623,625,'dipietro')],C7),
           ('AN','an7_10_11',[('AN10','capaci',None),('AN11',None,None)]),
           ('P','a7b',648,682,[(648,14,3),(670,14,2)],[(670,677,'capaci')],C7)],mapk=3)
    arg(8,[('P','a8a',683,707,[(683,17,0),(692,17,1),(694,17,2)],[],C8),
           ('AN','an8_12_22',[('AN12',None,None),('AN22',None,None)]),
           ('P','a8b',708,714,[(708,17,3)],[],C8)])
    r.scena('gl2',s_gloss(2),'glossario')
    r.scena('rf2',s_ripasso_finale(2),'ripasso_finale')
    r.scena('verifica',s_testo('verifica','VERIFICA FINALE','Verifica finale',None,rows='10 domande · serve almeno l’80% · Rispondi · premi Controlla · poi Continua',dur=6.0,jingle=('quiz.wav',0.5,-2)),'verifica')
    r.scena('fin2',s_testo('fin2','ARRIVEDERCI','Per oggi è tutto','FIN2',dur=round(vd('FIN2')+2.5,2),jingle=('finale.wav',0.2,-6)),'saluto')
    r.clip('finale2',KIT+'/sigle/Sigla_finale_5s_con_avviso_diritti.mp4',tipo='finale')
    r.scena('compiti_i',s_testo('compiti_i','ORA TOCCA A TE','Compiti',None,dur=3.5,jingle=('titolo.wav',0.2,-4)),'compiti_intro')
    r.scena('compiti_voce',s_compiti(),'compiti',last=True)
    return r
if __name__=='__main__':
    r=run2();json.dump(r.tl,open(W+'/timeline_P2_tmp.json','w'),ensure_ascii=False,indent=0)
    print('Parte 2 durata',round(r.t,1),'s',round(r.t/60,2),'min')
