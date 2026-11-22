import sys;sys.path.insert(0,'/home/claude/w19/lib')
from piano import *
S=lambda i:SEG[i]['inizio']
E_=lambda i:SEG[i]['fine']
def cues(l): return [(S(i),pg,c) for i,pg,c in l]
def imgs(l): return [(S(a),E_(b),k) for a,b,k in l]
MANUAL_OK={352,406}
def run1():
    r=Run('p1')
    if True:
        r.clip('sigla',KIT+'/sigle/Sigla_Storia_15s.mp4',tipo='sigla')
        # copertina animata, voce di benvenuto, senza riquadro del prof
        d=vd('BENV1_R2')
        html=cover_html(False,anim=True)
        f=render_scene('cover_kore',html,round(d+2.4,2))
        r.scena('cover_kore',(f,[(VX+'BENV1_R2.wav',1.0,0)]),'copertina')
        cv=O+'cover_box.png';pa=[O+f'arg_{i}.png' for i in range(3)]
        with B() as b:
            b.shot(cover_html(True,pg=1),cv)
            for i,items in enumerate([[1,2,3],[4,5,6],[7,8]]): b.shot(argomenti_html(items,2+i),pa[i])
        r.prof('intro_cover',0,37,[],[],0,{},tipo='intro',statesfn=lambda R:[(0,cv)])
        def st_args(R):
            D=dur_r(R);return [(0,pa[0]),(D/3,pa[1]),(2*D/3,pa[2])]
        r.prof('intro_args',38,58,[],[],0,{},tipo='intro',statesfn=st_args)
        r.pg=4
        def arg(n,pezzi,mapk=None):
            r.scena(f't{n}',s_titolo(n),'titolo',arg=n)
            for p in pezzi:
                if p[0]=='P': _,pid,a,bb,cu,im,co,*dr=p;r.prof(pid,a,bb,cues(cu),imgs(im),n,co,drop=dr[0] if dr else (),arg=n) if False else r.prof(pid,a,bb,cues(cu),imgs(im),n,co,drop=dr[0] if dr else ())
                elif p[0]=='AN': r.scena(p[1],s_an(p[1],p[2]),'approfondimento',arg=n)
            if mapk: r.scena(f'map{mapk}',s_mappa(mapk),'mappa',arg=n)
            r.scena(f'sch{n}',s_schema(n),'ripasso',arg=n)
            r.scena(f'q{n}',s_quiz(n),'quiz',arg=n)
        C2a={2:[0,1]};C2b={2:[2,3]};C4={4:[0,1,2,3]};C6={6:[0,1,2,3]}
        arg(1,[('P','a1a',59,75,[(59,2,0)],[],C2a),
               ('AN','an1_13_18',[('AN13','none',None),('AN18','none',None)]),
               ('P','a1b',76,136,[(76,2,0),(79,2,1),(87,2,0),(123,2,1),(130,2,0)],[],C2a,{77}),
               ('P','a1c',138,162,[(138,2,0)],[],C2a),
               ('AN','an1_14',[('AN14',None,None)])])
        arg(2,[('P','a2a',163,191,[(163,2,2),(183,2,3)],[],C2b),
               ('AN','an2_1',[('AN1','operai',None),('A2N',None,None)]),
               ('P','a2b',192,201,[(192,2,3)],[],C2b)])
        arg(3,[('P','a3a',202,238,[(202,4,0),(220,4,2)],[(230,238,'fontana')],C4,{229}),
               ('AN','an3_2',[('AN2','fontana',None)]),
               ('P','a3b',239,259,[(239,4,2),(249,4,1)],[],C4),
               ('AN','an3_20',[('AN20',None,None)]),
               ('P','a3c',260,290,[(260,4,2),(270,4,1)],[],C4),
               ('AN','an3_19',[('AN19',None,None)]),
               ('P','a3d',291,309,[(291,4,3)],[],C4),
               ('AN','an3_16',[('AN16','moro_br',None)]),
               ('P','a3e',310,329,[(310,4,3)],[],C4)],mapk=1)
        arg(4,[('P','a4a',330,352,[(330,6,0),(332,6,1),(337,6,2),(342,6,3)],[(333,334,'moro_br')],C6),
               ('AN','an4_4_21',[('AN4','moro_br',None),('AN21',None,None)]),
               ('P','a4b',355,372,[(355,6,3)],[(369,372,'berlinguer')],C6),
               ('AN','an4_17',[('AN17','berlinguer',None)]),
               ('P','a4c',373,386,[(373,6,3)],[],C6)],mapk=2)
        r.scena('gl1',s_gloss(1),'glossario')
        r.scena('rf1',s_ripasso_finale(1),'ripasso_finale')
        r.scena('fin1',s_testo('fin1','ARRIVEDERCI','Per oggi è tutto','FIN1',dur=round(vd('FIN1')+2.5,2),jingle=('finale.wav',0.2,-6)),'saluto')
        r.clip('finale',KIT+'/sigle/Sigla_finale_5s_con_avviso_diritti.mp4',last=True,tipo='finale')
    open(W+'/pg_fine_p1.txt','w').write(str(r.pg))
    return r
if __name__=='__main__':
    r=run1();json.dump(r.tl,open(W+'/timeline_P1_tmp.json','w'),ensure_ascii=False,indent=0)
    print('Parte 1 durata',round(r.t,1),'s',round(r.t/60,2),'min')
