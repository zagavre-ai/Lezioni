# Costruisce e assembla una Parte di lez01. Uso: python3 parte.py N   (VOX=... per le voci)
import sys,os,json
sys.path.insert(0,'/home/user/lav/prod')
import costruisci as C
from assembla import assembla
L='/home/user/lav/lez01/';SIG='/home/user/Lezioni/scambio/caputi/kit_caputi/sigle/Sigla_Tecnologie_moda_15s.mp4'
FIN='/home/user/Lezioni/kit/sigle/Sigla_finale_5s_con_avviso_diritti.mp4'
ARG={1:(1,4),2:(5,8),3:(9,10)}
def ren(x,n):
    x['scena']=x.get('scena',x['nome']);x['nome']=n;return x
def intro_prof():
    nome='D00_intro'
    if C.fatto(nome):return C.clip(nome)
    import prof_bg as PB,prof_comp as PC
    from frasi import parole_asr,frasi
    from piani import PEZZI,Mappa,intervalli
    tr=json.load(open(L+'trasc.json'));W=parole_asr(tr);a,b=PEZZI[0];M=Mappa(intervalli(a,b,W))
    fr=frasi(L+'Lezione.1.-.Preparazione.pt.1.1.pdf')
    import pymupdf
    t=' '.join(pymupdf.open(L+'Lezione.1.-.Preparazione.pt.1.1.pdf')[0].get_text().split('\n')[5:8])
    t="Parleremo di classificazione generale delle fibre tessili e approfondiremo le caratteristiche, l'origine e i processi di lavorazione delle fibre naturali di origine animale: lana e seta."
    items=[dict(T=1.0,html=PB.card_html(t),note='')]
    out,G,h=PB.build_bg(nome,items,M.dur,'Preparazione',[],L+'bg/D00')
    PC.comp(0,out,L+'bg/D00/prof.mp4',a,b,W)
    C.salva(nome,L+'bg/D00/prof.mp4',None,True);return dict(v=L+'bg/D00/prof.mp4',a=None,trans=True,nome=nome)
def prof(n):
    p=L+f'bg/A{n:02d}/prof.mp4'
    return dict(v=p,a=None,trans=True,nome=f'D{n}')
def argomento(n):
    A=C.carica(n);out=[]
    t=C.titolo(f'T{n}_titolo',f'ARGOMENTO {n}',A['titolo'],C.MAT);ren(t,f'T{n}');out.append(t)
    out.append(prof(n))
    a=C.approf(n);ren(a,f'E{n}');out.append(a)
    m=C.mappa(n);ren(m,f'M{n}');out.append(m)
    r=C.pillola(n);ren(r,f'R{n}');out.append(r)
    q=C.quiz(n);ren(q[0],f'Q{n}')
    for i,x in enumerate(q[1:],1):ren(x,f'QD{n}_{i}')
    return out+q
def parte(N):
    a,b=ARG[N];cl=[dict(v=SIG,a=None,trans=False,nome='SIGLA')]
    if N==1:
        v=C.copertina(1,'P1_BENVENUTO_V3',[C.B2.TITOLI[i] for i in range(0,4)]);ren(v,'COPERTINA');cl.append(v);cl.append(intro_prof())
    elif N==2:
        v=C.copertina(2,'P2_BENVENUTO_V3',[C.B2.TITOLI[i] for i in range(4,8)]);ren(v,'COPERTINA');cl.append(v)
        r=C.pillola_gen('P2_ripasso1','P2_RIPASSO_V2','RIPASSO DELLA PARTE PRECEDENTE','Che cosa abbiamo visto',C.RIGHE_FIN()[:4],C.B2.RIPF[:4],prefisso='Prima di ricominciare, ripassiamo la prima parte.');ren(r,'RP');cl.append(r)
    else:
        v=C.copertina(3,'P3_BENVENUTO_V3',[C.B2.TITOLI[i] for i in range(8,10)]+['Glossario, ripasso, mappa e verifica finale']);ren(v,'COPERTINA');cl.append(v)
        r=C.pillola_gen('P3_ripasso2','P3_RIPASSO_V2','RIPASSO DELLA PARTE PRECEDENTE','Che cosa abbiamo visto',C.RIGHE_FIN()[4:8],C.B2.RIPF[4:8],prefisso='Prima di ricominciare, ripassiamo la seconda parte.');ren(r,'RP');cl.append(r)
    for n in range(a,b+1):cl+=argomento(n)
    if N<3:
        c=C.chiusura(f'P{N}_chiusura',f'P1_CHIUSURA_V2' if N==1 else 'P2_CHIUSURA_V2','Continua nella prossima parte');ren(c,'CH');cl.append(c)
    else:
        g=C.glossario();ren(g,'GL');cl.append(g)
        f=C.ripasso_finale();ren(f,'RF');cl.append(f)
        m=C.mappa_finale();ren(m,'FM');cl.append(m)
        t=C.test_finale();ren(t[0],'QT')
        for i,x in enumerate(t[1:],1):ren(x,f'QT_{i}')
        cl+=t
        co=C.compiti();ren(co[0],'CI');ren(co[1],'CO');cl+=co
        c=C.chiusura('P3_chiusura','P2_CHIUSURA','Buon lavoro!');ren(c,'CH');cl.append(c)
    cl.append(dict(v=FIN,a=None,trans=True,nome='SIGLA_FINALE'))
    return cl
if __name__=='__main__':
    N=int(sys.argv[1]);cl=parte(N)
    out=L+f'Tecnologie_Preparazione_Parte{N}_1080p.mp4'
    tl,dur=assembla(cl,out,log=lambda *a:print(*a,flush=True))
    json.dump([[n,round(t,3),round(l,3)] for n,t,l in tl],open(L+f'timeline_Parte{N}.json','w'),ensure_ascii=False,indent=1)
    json.dump([[c['nome'],c.get('scena',c['nome'])] for c in cl],open(L+f'scene_Parte{N}.json','w'),ensure_ascii=False)
    print('durata',round(dur,1),'s',round(dur/60,1),'min')
